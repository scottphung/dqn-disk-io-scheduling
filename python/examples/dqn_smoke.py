"""Minimal DQN using only the Gymnasium API (no DiskSim-specific code).

Uses info["action_mask"] (valid queue slots) for exploration, the greedy choice and the Bellman target
(--no-mask turns that off). Every hyperparameter is a command-line option: see  --help.

Output (under --out-dir, default results/):
  <RUN>/epNNNN.png, epNNNN.pt   PNG + weights every --snap-every episodes (RUN = hyperparameter tag + timestamp)
  <RUN>/summary.json            final metrics + hyperparameters (read by main.py)
  <RUN>_history.csv             per-episode history of the whole run
"""
import sys, os, random, time, math, json, argparse
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, torch.nn as nn, gymnasium as gym
import disksim_env
from baselines import fcfs, sstf, evaluate

HERE = os.path.dirname(os.path.abspath(__file__))

ap = argparse.ArgumentParser(description=__doc__.split("\n")[0], formatter_class=argparse.ArgumentDefaultsHelpFormatter)
ap.add_argument("episodes", nargs="?", type=int, default=50, help="training episodes (positional, or use --episodes)")
ap.add_argument("--episodes", dest="episodes_opt", type=int, default=None, help="same as the positional episodes")
g = ap.add_argument_group("exploration (epsilon: 1.0 for HOLD, linear decay over DECAY, then EPS_END)")
g.add_argument("--hold", type=float, default=0.25, help="fraction of episodes at epsilon=1.0")
g.add_argument("--decay", type=float, default=0.50, help="fraction of episodes spent decaying epsilon")
g.add_argument("--eps-end", type=float, default=0.02, help="final epsilon")
g = ap.add_argument_group("optimisation")
g.add_argument("--lr0", type=float, default=5e-4, help="learning rate at the start (cosine decay)")
g.add_argument("--lr1", type=float, default=5e-5, help="learning rate at the end")
g.add_argument("--gamma", type=float, default=0.99, help="discount factor")
g.add_argument("--batch", type=int, default=64, help="minibatch size")
g.add_argument("--train-every", type=int, default=4, help="one gradient step every N environment steps")
g.add_argument("--warmup", type=int, default=1000, help="transitions in the buffer before training starts")
g.add_argument("--tgt-update", type=int, default=1000, help="copy online -> target network every N environment steps")
g.add_argument("--replay-cap", type=int, default=100_000, help="replay buffer capacity (transitions)")
g.add_argument("--steps", type=int, default=1000, help="initial value of the global step counter (shifts the update cadence)")
g = ap.add_argument_group("run / environment")
g.add_argument("--seed", type=int, default=0, help="agent seed (init, exploration, sampling) and training-workload seeds")
g.add_argument("--no-mask", action="store_true", help="do not use the action mask")
g.add_argument("--reward-mode", default=None, choices=["response", "service", "queue_time"], help="environment reward (default: the env's)")
g.add_argument("--reward-scale", type=float, default=None, help="environment reward scale (default: the env's)")
g.add_argument("--eval-episodes", type=int, default=10, help="workloads (seeds 1000..) for the FINAL greedy evaluation; more = less noise")
g.add_argument("--snap-eval-episodes", type=int, default=10, help="workloads for each intermediate snapshot's evaluation (a prefix of the final set)")
g.add_argument("--recycle-every", type=int, default=250, help="replace the DiskSim worker process every N resets (DiskSim leaks ~0.5 MB per reset); 0 = run in-process")
g.add_argument("--snap-every", type=int, default=25, help="save PNG + weights (and run a greedy eval) every N episodes")
g.add_argument("--out-dir", default=os.path.join(HERE, "..", "results"), help="where runs are written")
g.add_argument("--threads", type=int, default=None, help="torch CPU threads (1 is best when running several jobs)")
A = ap.parse_args()
EPISODES = A.episodes_opt if A.episodes_opt is not None else A.episodes
USE_MASK = not A.no_mask
if A.threads: torch.set_num_threads(A.threads)

ekw = {}
if A.reward_mode: ekw["reward_mode"] = A.reward_mode
if A.reward_scale: ekw["reward_scale"] = A.reward_scale
env = gym.make("DiskSchedRecycled-v0", recycle_every=A.recycle_every, **ekw) if A.recycle_every > 0 else gym.make("DiskSched-v0", **ekw)
nin, nout = env.observation_space.shape[0], env.action_space.n
mk = lambda: nn.Sequential(nn.Linear(nin, 128), nn.ReLU(), nn.Linear(128, 128), nn.ReLU(), nn.Linear(128, nout))
torch.manual_seed(A.seed); random.seed(A.seed); np.random.seed(A.seed)
net, tgt = mk(), mk(); tgt.load_state_dict(net.state_dict())
opt = torch.optim.Adam(net.parameters(), lr=A.lr0)

class Replay:
    """Preallocated NumPy ring buffer: O(1) add, O(batch) random sampling."""
    def __init__(self, cap, nin, nact):
        self.cap, self.n, self.i = cap, 0, 0
        self.o = np.zeros((cap, nin), np.float32); self.n_ = np.zeros((cap, nin), np.float32)
        self.a = np.zeros(cap, np.int64); self.r = np.zeros(cap, np.float32)
        self.d = np.zeros(cap, np.float32); self.m = np.zeros((cap, nact), bool)
    def add(self, o, a, r, n_, d, m):
        i = self.i
        self.o[i], self.a[i], self.r[i], self.n_[i], self.d[i], self.m[i] = o, a, r, n_, d, m
        self.i = (i + 1) % self.cap; self.n = min(self.n + 1, self.cap)
    def sample(self, bs):
        j = np.random.randint(0, self.n, bs)
        return self.o[j], self.a[j], self.r[j], self.n_[j], self.d[j], self.m[j]
    def __len__(self): return self.n

buf = Replay(A.replay_cap, nin, nout); steps = A.steps
NEG = -1e9
TRAIN_SEED0 = 1_000_000 * (A.seed + 1)      # training workloads never overlap the eval seeds (1000-1009)

def greedy(obs, mask=None, rng=None):
    with torch.no_grad():
        q = net(torch.as_tensor(obs))
        if USE_MASK and mask is not None:
            q = q.masked_fill(~torch.as_tensor(mask), NEG)
        return int(q.argmax())

# Per-run identity: TAG encodes the hyperparameters; RUN adds a timestamp so every run gets its own folder.
TAG = (f"dqn_{EPISODES}ep_rew-{env.unwrapped.reward_mode}x{env.unwrapped.reward_scale:g}"
       f"_eps-h{A.hold:g}d{A.decay:g}e{A.eps_end:g}_lr-{A.lr0:g}to{A.lr1:g}"
       f"_g{A.gamma:g}_bs{A.batch}_te{A.train_every}_tu{A.tgt_update}_rc{A.replay_cap // 1000}k"
       f"_mask{int(USE_MASK)}_s{A.seed}")
OUT = os.path.abspath(A.out_dir)
RUN = f"{TAG}_{time.strftime('%Y%m%d-%H%M%S')}"
RUN_DIR = os.path.join(OUT, RUN)                                  # PNG + weights snapshots + summary.json
CSV = os.path.join(OUT, f"{RUN}_history.csv")                     # full-run history, flat in the out dir
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plain = lambda d: json.loads(json.dumps(d, default=lambda o: o.item() if hasattr(o, "item") else str(o)))  # no numpy types
hist, eval_hist, LAST = [], [], {}        # eval_hist: (episodes_done, greedy mean ms); LAST: last snapshot's results
SEEDS = range(1000, 1000 + A.eval_episodes)                     # final evaluation workloads
SNAP_N = min(A.snap_eval_episodes, A.eval_episodes)          # snapshots use the first SNAP_N of them
os.makedirs(RUN_DIR, exist_ok=True)

def atomic(write, path):
    write(path + ".tmp"); os.replace(path + ".tmp", path)           # a crash mid-save never corrupts the last file

def save_weights(ep_done):
    e = env.unwrapped
    atomic(lambda f: torch.save({
        "state_dict": net.state_dict(), "episodes_done": ep_done,
        "nin": int(nin), "nout": int(nout), "hidden": 128, "use_mask": USE_MASK, "tag": TAG, "run": RUN,
        "env_kwargs": plain(dict(queue_slots=e.K, episode_requests=e.N, mean_interarrival_ms=e.mean_ia,
                           read_fraction=e.read_frac, sizes=list(e.sizes), reward_mode=e.reward_mode,
                           reward_scale=e.reward_scale, invalid_penalty=e.invalid_penalty,
                           max_consecutive_invalid=e.max_invalid, wait_scale_ms=e.wait_scale)),
        "train": plain(vars(A)),
    }, f), os.path.join(RUN_DIR, f"ep{ep_done:04d}.pt"))

def save_csv():
    atomic(lambda f: np.savetxt(f, np.array(hist, dtype=float).reshape(-1, 6), delimiter=",",
           header="episode,epsilon,lr,mean_response_ms,completed,disksim_hang", comments=""), CSV)

def last_train_mean(k=25):
    r = [x[3] for x in hist[-k:] if x[4]]
    return float(np.mean(r)) if r else float("nan"), min(k, len(hist))

def save_png(ep_done, res, n_eval):
    h = np.array(hist, dtype=float); ep_, eps_, lr_, resp = h[:, 0], h[:, 1], h[:, 2], h[:, 3]
    w = max(1, min(25, len(h) // 10)); ma = np.convolve(resp, np.ones(w) / w, mode="valid")
    fig, ax = plt.subplots(1, 3, figsize=(17, 4.8))
    ax[0].plot(ep_, resp, color="#9ecae1", lw=0.8, label="training, per episode")
    ax[0].plot(ep_[w - 1:], ma, color="#08519c", lw=2, label=f"training, {w}-episode mean")
    if eval_hist:
        ee = np.array(eval_hist); ax[0].plot(ee[:, 0] - 1, ee[:, 1], "o-", color="#ff7f0e", lw=1.5, label="greedy eval at snapshots")
    ax[0].axhline(res["SSTF"][0], color="#2ca02c", ls="--", label="SSTF (eval)")
    ax[0].axhline(res["FCFS"][0], color="#d62728", ls="--", label="FCFS (eval)")
    ax[0].set(xlabel="episode", ylabel="mean response time (ms)", yscale="log",
              title=f"Training (includes exploration) - {ep_done}/{EPISODES} episodes"); ax[0].legend(fontsize=8, loc="lower left")
    ltm, k = last_train_mean()
    ax[0].text(0.98, 0.97,
               f"{'FINAL' if ep_done >= EPISODES else f'at ep {ep_done}'} greedy eval: {res['DQN greedy'][0]:.1f} ms\n"
               f"  (n={n_eval} workloads: spread ±{res['DQN greedy'][1]:.1f}, std. error ±{res['DQN greedy'][1] / math.sqrt(n_eval):.1f})\n"
               f"SSTF {res['SSTF'][0]:.1f} ms   FCFS {res['FCFS'][0]:.1f} ms\n"
               f"training mean, last {k} eps: {ltm:.1f} ms",
               transform=ax[0].transAxes, ha="right", va="top", fontsize=10, family="monospace",
               bbox=dict(boxstyle="round", facecolor="white", edgecolor="#555", alpha=0.92))
    a2 = ax[1]; a2.plot(ep_, eps_, color="#e6550d", lw=2, label="epsilon"); a2.set(xlabel="episode", ylabel="epsilon", title="Schedules")
    a3 = a2.twinx(); a3.plot(ep_, lr_, color="#756bb1", lw=2, label="learning rate"); a3.set_ylabel("learning rate")
    a2.legend(*[sum(z, []) for z in zip(a2.get_legend_handles_labels(), a3.get_legend_handles_labels())], loc="center right")
    names = list(res); vals = [res[n][0] for n in names]; errs = [res[n][1] for n in names]
    ax[2].bar(names, vals, yerr=errs, capsize=4, color=["#d62728", "#2ca02c", "#08519c"])
    for i, v in enumerate(vals): ax[2].text(i, v, f"{v:.0f}", ha="center", va="bottom")
    ax[2].set(ylabel="mean response time (ms)", title=f"Greedy evaluation, {n_eval} workloads (seeds {SEEDS.start}-{SEEDS.start + n_eval - 1})")
    fig.suptitle(RUN, fontsize=8, color="#555")
    fig.tight_layout(); png = os.path.join(RUN_DIR, f"ep{ep_done:04d}.png"); fig.savefig(png, dpi=130); plt.close(fig)
    return png

def snapshot(ep_done, final=False):
    """Weights + CSV first (cheap, safe), then a greedy eval and the PNG (may fail without losing the rest).
    final=True evaluates on all A.eval_episodes workloads; otherwise on the first SNAP_N (cheaper)."""
    save_weights(ep_done); save_csv()
    try:
        k = len(SEEDS) if final else SNAP_N
        dq = evaluate(greedy, env, range(SEEDS.start, SEEDS.start + k), return_all=True)
        res = {n: ms(BASE_ALL[n][:k]) for n in ("FCFS", "SSTF")}; res["DQN greedy"] = ms(dq)
        eval_hist.append((ep_done, res["DQN greedy"][0]))
        LAST.update(ep=ep_done, res=res, n=k, final=final, dq_all=dq, base_all={n: BASE_ALL[n][:k] for n in BASE_ALL})
        save_png(ep_done, res, k)
        print(f"  [snapshot ep {ep_done}] greedy eval {res['DQN greedy'][0]:.1f} ms over {k} workloads (FCFS {res['FCFS'][0]:.0f}, SSTF {res['SSTF'][0]:.0f})", flush=True)
    except Exception as ex:
        print(f"  [snapshot ep {ep_done}] weights+CSV saved; eval/PNG failed: {ex!r}", flush=True)

BASE_ALL = {n: evaluate(p, env, SEEDS, return_all=True) for n, p in [("FCFS", fcfs), ("SSTF", sstf)]}   # computed once, per workload
def ms(v): return (float(np.nanmean(v)), float(np.nanstd(v)))
BASE = {n: ms(v) for n, v in BASE_ALL.items()}                                                       # over the full final set
print(f"run folder: {RUN_DIR}\nbaselines ({A.eval_episodes} workloads): FCFS {BASE['FCFS'][0]:.1f} ms, SSTF {BASE['SSTF'][0]:.1f} ms", flush=True)

t0 = time.time(); status = "interrupted"
try:
  for ep in range(EPISODES):
    obs, info = env.reset(seed=TRAIN_SEED0 + ep); done = False; mask = info["action_mask"]
    frac = ep / EPISODES
    eps = 1.0 if frac < A.hold else max(A.eps_end, 1.0 - (1.0 - A.eps_end) * (frac - A.hold) / A.decay)
    lr = A.lr1 + 0.5 * (A.lr0 - A.lr1) * (1 + math.cos(math.pi * frac))
    for pg in opt.param_groups: pg["lr"] = lr
    while not done:
        if random.random() < eps:
            a = int(np.random.choice(np.flatnonzero(mask))) if USE_MASK else env.action_space.sample()
        else:
            a = greedy(obs, mask)
        nobs, r, term, trunc, info = env.step(a)
        nmask = info["action_mask"]
        buf.add(obs, a, r, nobs, float(term), nmask)   # time-limit => bootstrap (not terminal)
        obs, mask, done, steps = nobs, nmask, term or trunc, steps + 1
        if len(buf) >= A.warmup and steps % A.train_every == 0:
            o, a_, r_, n_, d_, m_ = buf.sample(A.batch)
            q = net(torch.as_tensor(o)).gather(1, torch.as_tensor(a_).long()[:, None]).squeeze(1)
            with torch.no_grad():
                qn = tgt(torch.as_tensor(n_))
                if USE_MASK:
                    qn = qn.masked_fill(~torch.as_tensor(m_), NEG)
                y = torch.as_tensor(r_, dtype=torch.float32) + A.gamma * (1 - torch.as_tensor(d_, dtype=torch.float32)) * qn.max(1).values
            loss = nn.functional.smooth_l1_loss(q, y); opt.zero_grad(); loss.backward(); opt.step()
        if steps % A.tgt_update == 0: tgt.load_state_dict(net.state_dict())
    hist.append((ep, eps, lr, info['mean_response_ms'], info['completed'], float(bool(info.get('disksim_hang')))))
    if ep % 25 == 0:
        print(f"ep {ep:4d} eps={eps:.4f} lr={lr:.1e} train mean response {info['mean_response_ms']:8.1f} ms  hangs so far {int(sum(x[5] for x in hist))}  ({time.time()-t0:.0f}s)", flush=True)
    if (ep + 1) % A.snap_every == 0:
        snapshot(ep + 1, final=(ep + 1 == EPISODES))
  status = "ok"
finally:   # normal end, crash or Ctrl-C: keep whatever was trained so far
    if not LAST.get("final"):
        snapshot(len(hist), final=True)
    hangs = int(sum(x[5] for x in hist))
    if LAST:
        res = LAST["res"]
        print(f"--- final eval after {LAST['ep']} episodes, {LAST['n']} workloads (mask={'on' if USE_MASK else 'off'}) ---")
        for n in ("FCFS", "SSTF", "DQN greedy"):
            print(f"{n:11s} mean response {res[n][0]:8.2f} ms (spread ±{res[n][1]:.2f}, std. error ±{res[n][1] / math.sqrt(LAST['n']):.2f})")
    ltm, k = last_train_mean()
    summary = plain(dict(status=status, episodes_done=len(hist), episodes_planned=EPISODES, seconds=time.time() - t0,
                         final_greedy_ms=LAST["res"]["DQN greedy"][0] if LAST else None,
                         final_greedy_std=LAST["res"]["DQN greedy"][1] if LAST else None,
                         final_greedy_se=(LAST["res"]["DQN greedy"][1] / math.sqrt(LAST["n"])) if LAST else None,
                         n_eval=LAST.get("n"), final_snapshot=bool(LAST.get("final")),
                         final_per_seed=dict(dqn=[float(x) for x in LAST["dq_all"]],
                                             fcfs=[float(x) for x in LAST["base_all"]["FCFS"]],
                                             sstf=[float(x) for x in LAST["base_all"]["SSTF"]]) if LAST else None,
                         fcfs_ms=BASE["FCFS"][0], sstf_ms=BASE["SSTF"][0], last_train_mean_ms=ltm,
                         disksim_hangs=hangs, tag=TAG, run=RUN, run_dir=RUN_DIR, hparams=vars(A)))
    with open(os.path.join(RUN_DIR, "summary.json"), "w") as f: json.dump(summary, f, indent=1)
    print(f"DiskSim hangs during training: {hangs}/{len(hist)} episodes")
    print(f"saved: {RUN_DIR}  (PNG + weights every {A.snap_every} episodes, summary.json)\n       {CSV}")
