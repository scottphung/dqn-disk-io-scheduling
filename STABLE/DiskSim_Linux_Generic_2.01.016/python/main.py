#!/usr/bin/env python3

# Failed experiments (clearly poorer results or superfluous):
    # ("layers", {"hidden_sizes": "256,96"}),
    # ("layers", {"hidden_sizes": "32,256,32"}),
    # ("layers", {"hidden_sizes": "32,64,256,512,1024,4096,64"}),
    # ("layers", {"hidden_sizes": "1024,4096,1024"}),
    # ("layers", {"hidden_sizes": "1024"}),
    # ("layers", {"hidden_sizes": "256,128,128,64"}),
    # ("layers", {"hidden_sizes": "128,64,64,32"}),
    # ("layers", {"hidden_sizes": "512,256,256,128"}),
    # ("layers", {"hidden_sizes": "512,256,256,128,128,64"}),
    # ("activation", {"activation": "tanh"}),
    # ("activation", {"activation": "sig"}), $
    # ("layers", {"hidden_sizes": "96,96"}),
    # ("layers", {"hidden_sizes": "64,64"}),
    # ("layers", {"hidden_sizes": "256,128,64"}),
    # ("layers", {"hidden_sizes": "64"}), #
    # ("layers", {"hidden_sizes": "128,96,64"}),
    # ("layers", {"hidden_sizes": "96"}),
    # ("layers", {"hidden_sizes": "64,128"}),
    # ("layers", {"hidden_sizes": "64,128,64"}),
    # ("layers", {"hidden_sizes": "96,128,256,64"}),
    # ("layers", {"hidden_sizes": "196,196"}),
    # ("layers", {"hidden_sizes": "256,256"}),
    # ("layers", {"hidden_sizes": "128,64"}),
    # ("layers", {"hidden_sizes": "64,64,64"}),
    # ("layers", {"hidden_sizes": "100"}),
    # ("layers", {"hidden_sizes": "32"}),
    # ("layers", {"hidden_sizes": "96,32"}),
    # ("activation", {"activation": "celu"}),
    # ("activation", {"activation": "elu"}),
    # ("activation", {"activation": "silu"}),
    # ("activation", {"activation": "mish"}),
    # ("train_every", {"train_every": 6}),
    # ("train_every", {"train_every": 1}),
    # ("policy_dropout", {"policy_dropout": 0.05}),
    # ("policy_dropout", {"policy_dropout": 0.10}),
    # ("policy_dropout", {"policy_dropout": 0.15}),
    # ("policy_dropout", {"policy_dropout": 0.20}),
    # ("policy_dropout", {"policy_dropout": 0.50}), #
    # ("policy_dropout", {"policy_dropout": 0.01}),
    # ("policy_dropout", {"policy_dropout": 0.02}),
    # ("policy_dropout", {"policy_dropout": 0.03}),
    # ("policy_dropout", {"policy_dropout": 0.04}),
    # ("lr", {"lr0": 1e-2, "lr1": 1e-3}),
    # ("lr", {"lr0": 2.5e-4, "lr1": 5e-5}),
    # ("lr", {"lr0": 1e-4, "lr1": 1e-6}), #
    # ("lr", {"lr0": 3e-3, "lr1": 3e-4}),
    # ("lr", {"lr0": 2e-3, "lr1": 2e-4}),
    # ("lr", {"lr0": 1e-3, "lr1": 5e-4}),
    # ("lr", {"lr0": 5e-4, "lr1": 1e-4}),
    # ("lr", {"lr0": 5e-3, "lr1": 1e-4}),
    # ("lr", {"lr0": 1e-2, "lr1": 1e-4}),
    # ("lr", {"lr0": 1e-2, "lr1": 1e-5}),
    # ("gamma", {"gamma": 0.95}),
    # ("gamma", {"gamma": 0.90}),
    # ("gamma", {"gamma": 0.85}),
    # ("gamma", {"gamma": 0.80}), #
    # ("gamma", {"gamma": 0.96}),
    # ("gamma", {"gamma": 0.94}),
    # ("gamma", {"gamma": 0.93}),
    # ("wd", {"weight_decay": 1e-1}),
    # ("wd", {"weight_decay": 5e-2}),
    # ("wd", {"weight_decay": 5e-3}),
    # ("wd", {"weight_decay": 3e-3}),
    # ("wd", {"weight_decay": 2e-3}),
    # ("wd", {"weight_decay": 9e-4}),
    # ("wd", {"weight_decay": 8e-4}),
    # ("wd", {"weight_decay": 7e-7}),
    # ("wd", {"weight_decay": 5e-5}),
    # ("wd", {"weight_decay": 1e-5}),
    # ("wd", {"weight_decay": 5e-6}),
    # ("wd", {"weight_decay": 1e-6}),
    # ("optim", {"optim": "Adagrad"}),
    # ("optim", {"optim": "SGD"}),
    # ("tgt_update", {"tgt_update": 500}),
    # ("tgt_update", {"tgt_update": 8000}), #
    # ("tgt_update", {"tgt_update": 5000}),
    # ("tgt_update", {"tgt_update": 2500}),
    # ("tgt_update", {"tgt_update": 1500}),
    # ("hold", {"hold": 0.40}),
    # ("hold", {"hold": 0.05}),
    # ("hold", {"hold": 0.10}),
    # ("hold", {"hold": 0.15}),
    # ("hold", {"hold": 0.20}),
    # ("eps_end", {"eps_end": 0.10}),
    # ("eps_end", {"eps_end": 0.0065}),
    # ("eps_end", {"eps_end": 0.006}),
    # ("eps_end", {"eps_end": 0.0055}),
    # ("eps_end", {"eps_end": 0.004}),
    # ("eps_end", {"eps_end": 0.0045}),
    # ("eps_end", {"eps_end": 0.0035}),
    # ("eps_end", {"eps_end": 0.003}),
    # ("eps_end", {"eps_end": 0.0025}),
    # ("eps_end", {"eps_end": 0.002}),
    # ("replay", {"replay_cap": 300_000}),
    # ("replay", {"replay_cap": 600_000}),
    # ("replay", {"replay_cap": 800_000}), #
    # ("replay", {"replay_cap": 400_000}),
    # ("replay", {"replay_cap": 450_000}),
    # ("replay", {"replay_cap": 550_000}),
    # ("env", {"reward_scale": 10.0}),
    # ("env", {"reward_scale": 5.0}),
    # ("env", {"reward_scale": 15.0}), #
    # ("env", {"reward_scale": 25.0}),
    # ("env", {"reward_scale": 30.0}),
    # ("env", {"reward_scale": 40.0}),
    # ("env", {"reward_scale": 50.0}),
    # ("env", {"reward_scale": 60.0}),
    # ("env", {"reward_scale": 75.0}),
    # ("env", {"reward_scale": 80.0}),
    # ("env", {"reward_scale": 90.0}),
    # ("env", {"reward_scale": 95.0}),
    # ("env", {"reward_scale": 105.0}),
    # ("env", {"reward_scale": 110.0}),
    # ("env", {"reward_scale": 125.0}),
    # ("env", {"reward_scale": 130.0}),
    # ("env", {"reward_scale": 140.0}),
    # ("env", {"reward_scale": 150.0}),
    # ("env", {"reward_scale": 160.0}),
    # ("env", {"reward_scale": 175.0}),
    # ("env", {"reward_scale": 200.0}),
    # ("env", {"reward_scale": 170.0}),
    # ("env", {"reward_scale": 180.0}),
    # ("env", {"reward_scale": 185.0}),
    # ("env", {"reward_scale": 190.0}),
    # ("env", {"reward_scale": 195.0}),

"""Run "current vs try" hyperparameter experiments for the DiskSim DQN, one knob at a time.

Every experiment is the baseline (the "current" values) with ONE setting changed to its "try" value.
Each run is a separate process (examples/dqn_smoke.py), so DiskSim's one-instance-per-process limit and
its memory leak don't matter, and runs execute in parallel (--jobs).

  python3 main.py --dry-run                      # show the plan, run nothing
  python3 main.py --episodes 1000 --jobs 4       # run everything (one seed)
  python3 main.py --groups gamma,batch --seeds 3 # only some groups, 3 seeds each
  python3 main.py --name sweep1 --resume         # continue an interrupted sweep (skips finished runs)
  python3 main.py --combo --groups lr,batch --dry-run   # combinations: every lr try x every batch try (plus the singles)
  python3 main.py --combo --combo-max 200        # all group pairs, randomly sample 200 combinations
  python3 main.py --combo-all --groups layers,lr,batch   # full factorial: one value from every listed group at once

Default: one knob at a time. With --combo, every active experiment is also run together with every active
experiment of each OTHER selected group (two knobs changed at once; same-group pairs are skipped because they
set the same knob). The single-knob runs are included so each pair gets an interaction estimate.

Results: results/sweeps/<name>/  ->  results.csv, comparison.png, runs/<label>_s<seed>/<run folder>/...
"""
import argparse, csv, glob, json, os, signal, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
TRAIN = os.path.join(HERE, "examples", "dqn_smoke.py")

# (group, overrides).  The label / run-folder name is derived from the overrides.  Overrides use dqn_smoke.py option names with '_' for '-'.
# "current" = dqn_smoke.py defaults; the baseline row runs those unchanged.
EXPERIMENTS = [
    ("baseline", {}),
    # ("layers", {"hidden_sizes": "512"}),
    # ("layers", {"hidden_sizes": "384"}),
    # ("layers", {"hidden_sizes": "300"}),
    # ("layers", {"hidden_sizes": "256"}),
    # ("layers", {"hidden_sizes": "225"}),
    # ("layers", {"hidden_sizes": "215"}),
    # ("layers", {"hidden_sizes": "196"}),
    # ("layers", {"hidden_sizes": "180"}),
    # ("layers", {"hidden_sizes": "165"}),
    # ("layers", {"hidden_sizes": "150"}),
    # ("layers", {"hidden_sizes": "128"}),
    # ("layers", {"hidden_sizes": "115"}),
    ("layers", {"hidden_sizes": "96"}),  # Best
    ("layers", {"hidden_sizes": "80"}),
    ("layers", {"hidden_sizes": "64"}),
    ("layers", {"hidden_sizes": "50"}),
    ("layers", {"hidden_sizes": "64,64"}),
    ("layers", {"hidden_sizes": "96,96"}),
    ("layers", {"hidden_sizes": "64,32"}),

    ("activation", {"activation": "selu"}),  # best
    # ("activation", {"activation": "leakyrelu"}),
    # ("activation", {"activation": "prelu"}),
    # ("activation", {"activation": "rrelu"}),
    # ("activation", {"activation": "relu6"}),
    # ("activation", {"activation": "gelu"}),
    # ("activation", {"activation": "glu"}),

    # ("train_every", {"train_every": 5}),
    # ("train_every", {"train_every": 3}),

    # ("episodes", {"episodes": 1500}),
    ("episodes", {"episodes": 2000}),  # best
    # ("episodes", {"episodes": 2500}),
    # ("episodes", {"episodes": 3000}),
    # ("episodes", {"episodes": 3500}),
    # ("episodes", {"episodes": 5000}), #
    # ("episodes", {"episodes": 1300}),
    # ("episodes", {"episodes": 1400}),
    # ("episodes", {"episodes": 1600}),
    # ("episodes", {"episodes": 1700}),

    # ("gamma", {"gamma": 1.00}),
    # ("gamma", {"gamma": 0.97}),

    # ("batch", {"batch": 128}),
    # ("batch", {"batch": 256}),
    ("batch", {"batch": 384}),  # best
    # ("batch", {"batch": 512}), #
    # ("batch", {"batch": 200}),
    # ("batch", {"batch": 300}),

    # ("lr", {"lr0": 1e-3, "lr1": 1e-4}),
    # ("lr", {"lr0": 5e-3, "lr1": 5e-4}),
    # ("lr", {"lr0": 9e-4, "lr1": 9e-5}),
    ("lr", {"lr0": 8e-4, "lr1": 8e-5}),  # best
    # ("lr", {"lr0": 1e-3, "lr1": 1e-4}),

    # ("policy_dropout", {"policy_dropout": 0.005}),
    # ("policy_dropout", {"policy_dropout": 0.001}),

    ("wd", {"weight_decay": 1e-3}),  # best
    # ("wd", {"weight_decay": 7e-3}),
    # ("wd", {"weight_decay": 5e-4}),

    # ("optim", {"optim": "Adam"}),
    # ("optim", {"optim": "NAdam"}),

    ("tgt_update", {"tgt_update": 2000}),  # best
    # ("tgt_update", {"tgt_update": 3000}),
    # ("tgt_update", {"tgt_update": 1700}),
    # ("tgt_update", {"tgt_update": 2200}),

    # ("hold", {"hold": 0.30}), #
    ("hold", {"hold": 0.35}),  # best

    # ("decay", {"decay": 0.30}),
    ("decay", {"decay": 0.65}),  # best
    # ("decay", {"decay": 0.75}),

    ("eps_end", {"eps_end": 0.05}),  # best
    # ("eps_end", {"eps_end": 0.02}),
    # ("eps_end", {"eps_end": 0.01}),
    # ("eps_end", {"eps_end": 0.005}),
    # ("eps_end", {"eps_end": 0.001}), #
    # ("eps_end", {"eps_end": 0.007}),

    ("replay", {"replay_cap": 500_000}),

    # environment constructor arguments (only with --groups env or --include-env)
    # ("env", {"reward_mode": "queue_time"}),
    # ("env", {"reward_mode": "response"}),
    # ("env", {"reward_scale": 225.0}),
    ("env", {"reward_scale": 250.0}),  # best
    # ("env", {"reward_scale": 275.0}),
    # ("env", {"reward_scale": 300.0}),
]
DEFAULT_GROUPS = [g for g in dict.fromkeys(e[0] for e in EXPERIMENTS) if g != "env"]

ap = argparse.ArgumentParser(description=__doc__.split("\n")[0], formatter_class=argparse.ArgumentDefaultsHelpFormatter)
ap.add_argument("--name", default=None, help="sweep name (default: timestamp)")
ap.add_argument("--episodes", type=int, default=1000, help="episodes for every run (the episodes group overrides it)")
ap.add_argument("--seeds", type=int, default=3, help="agent (training) seeds per experiment (0..N-1); more seeds = less noise")
ap.add_argument("--jobs", type=int, default=4, help="parallel runs (each uses 1 CPU thread)")
ap.add_argument("--groups", default=",".join(DEFAULT_GROUPS), help=f"comma list from: {','.join(dict.fromkeys(e[0] for e in EXPERIMENTS))}")
ap.add_argument("--include-env", action="store_true", help="also run the environment-argument group")
ap.add_argument("--combo", action="store_true", help="also run every pair of experiments from different groups (default: one knob at a time)")
ap.add_argument("--combo-all", action="store_true", help="full factorial: every combination taking one experiment from EACH selected group at once (baseline + all combinations; no singles)")
ap.add_argument("--combo-max", type=int, default=0, help="with --combo: randomly keep at most N pair runs (0 = all; the full cross-product can be thousands)")
ap.add_argument("--combo-seed", type=int, default=0, help="with --combo-max: RNG seed for the sample")
ap.add_argument("--eval-episodes", type=int, default=50, help="evaluation workloads for each run's FINAL greedy score")
ap.add_argument("--snap-eval-episodes", type=int, default=10, help="workloads for intermediate snapshot evaluations (cheaper)")
ap.add_argument("--snap-every", type=int, default=100, help="snapshot (PNG + weights + greedy eval) interval; larger = faster")
ap.add_argument("--resume", action="store_true", help="skip runs that already finished in this sweep")
ap.add_argument("--dry-run", action="store_true", help="print the plan and exit")
args = ap.parse_args()

groups = {"baseline"} | set(args.groups.split(","))
if args.include_env: groups.add("env")
unknown = groups - {e[0] for e in EXPERIMENTS}
if unknown: sys.exit(f"unknown group(s): {sorted(unknown)}")

def label_of(over):
    """Experiment label derived from the actual overrides (not the hand-written string in EXPERIMENTS),
    so it is also the run-folder name and can never disagree with what is really run."""
    return "+".join(f"{k}={v}" for k, v in sorted(over.items())) or "baseline"

plan = [(g, label_of(o), o) for g, o in EXPERIMENTS if g in groups]
dupes = sorted({l for l in (e[1] for e in plan)
                if sum(1 for e in plan if e[1] == l) > 1})
if dupes: sys.exit(f"duplicate experiments (identical overrides) in EXPERIMENTS: {dupes}")

combo_parts = {}                    # pair label -> (label_a, label_b)
if args.combo_all:
    import itertools, random
    bygroup = {}
    for e in plan:
        if e[0] != "baseline": bygroup.setdefault(e[0], []).append(e)
    full = []
    for combo in itertools.product(*bygroup.values()):
        over = {}
        for e in combo: over.update(e[2])
        full.append(("combo-all:" + "+".join(bygroup), " + ".join(e[1] for e in combo), over))
    if args.combo_max and len(full) > args.combo_max:
        full = random.Random(args.combo_seed).sample(full, args.combo_max)
    plan = [e for e in plan if e[0] == "baseline"] + full
    print(f"--combo-all: {' x '.join(f'{g}({len(v)})' for g, v in bygroup.items())} = {len(full)} combinations per seed")
elif args.combo:
    import itertools, random
    singles = [e for e in plan if e[0] != "baseline"]
    pairs = []
    for a, b in itertools.combinations(singles, 2):
        if a[0] == b[0] or set(a[2]) & set(b[2]): continue          # same knob: not a combination
        lab = f"{a[1]} + {b[1]}"
        pairs.append((f"combo:{a[0]}+{b[0]}", lab, {**a[2], **b[2]})); combo_parts[lab] = (a[1], b[1])
    if args.combo_max and len(pairs) > args.combo_max:
        pairs = random.Random(args.combo_seed).sample(pairs, args.combo_max)
        combo_parts = {l: combo_parts[l] for _, l, _ in pairs}
    plan = plan + pairs
    print(f"--combo: {len(singles)} single experiments -> {len(pairs)} pair runs per seed")

name = args.name or time.strftime("sweep-%Y%m%d-%H%M%S")
SWEEP = os.path.join(HERE, "results", "sweeps", name)
RUNS = os.path.join(SWEEP, "runs")

def episodes_of(over): return over.get("episodes", args.episodes)
def cost(job):                       # rough relative cost, used to start the slow runs first
    _, label, over, seed = job
    return episodes_of(over) * (4 / over.get("train_every", 4) * 0.6 + 0.4)

jobs = [(g, l, o, s) for (g, l, o) in plan for s in range(args.seeds)]
jobs.sort(key=cost, reverse=True)

def out_dir(job): return os.path.join(RUNS, f"{job[1]}_s{job[3]}")
def command(job):
    _, label, over, seed = job
    cmd = [sys.executable, "-I", TRAIN, str(episodes_of(over))]
    for k, v in over.items():
        if k != "episodes": cmd += [f"--{k.replace('_', '-')}", str(v)]
    return cmd + ["--seed", str(seed), "--snap-every", str(args.snap_every), "--eval-episodes", str(args.eval_episodes),
                  "--snap-eval-episodes", str(args.snap_eval_episodes), "--threads", "1", "--out-dir", out_dir(job)]
def summary_of(job):
    f = glob.glob(os.path.join(out_dir(job), "*", "summary.json"))
    return json.load(open(f[0])) if f else None
def finished(job):
    s = summary_of(job); return bool(s and s.get("status") == "ok")

print(f"sweep '{name}': {len(plan)} experiments x {args.seeds} seed(s) = {len(jobs)} runs, {args.jobs} in parallel")
print(f"{'group':12s} {'experiment':22s} episodes   change vs baseline")
for g, l, o in (plan if len(plan) <= 150 else plan[:60]):
    print(f"{g:12s} {l:22s} {episodes_of(o):7d}   {o if o else '(current values)'}")
if len(plan) > 150: print(f"... ({len(plan) - 60} more experiments not listed; full plan in plan.json)")
MIN_PER_BASELINE = 11.0         # was 6.3 (18:16 sweep, 4 jobs in parallel); runs have since taken ~75% longer (6.3 * 1.75 ~= 11.0)
work = sum(cost(j) for j in jobs) / 1000 * MIN_PER_BASELINE
longest = max(cost(j) for j in jobs) / 1000 * MIN_PER_BASELINE
print(f"rough estimate: ~{max(work / args.jobs, longest):.0f} min wall-clock ({work:.0f} CPU-min of work over {args.jobs} jobs; "
      f"longest single run ~{longest:.0f} min). Assumes ~{MIN_PER_BASELINE:.1f} min per 1000-episode baseline run (measured earlier, not for this exact sweep).")
if args.dry_run:
    sys.exit("dry run: nothing executed")

os.makedirs(RUNS, exist_ok=True)
json.dump(dict(args=vars(args), plan=[dict(group=g, label=l, overrides=o) for g, l, o in plan]),
          open(os.path.join(SWEEP, "plan.json"), "w"), indent=1)

todo = [j for j in jobs if not (args.resume and finished(j))]
if len(todo) < len(jobs): print(f"resuming: {len(jobs) - len(todo)} runs already finished, {len(todo)} to run")
env_vars = dict(os.environ, OMP_NUM_THREADS="1", MKL_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")

running, done_n, t0 = [], 0, time.time()
def reap(block=False):
    global done_n
    for p, job, t in running[:]:
        if p.poll() is not None:
            running.remove((p, job, t)); done_n += 1
            s = summary_of(job)
            res = f"final greedy {s['final_greedy_ms']:.1f} ms" if s and s.get("final_greedy_ms") else "NO RESULT (see log)"
            print(f"[{done_n}/{len(todo)}] {job[1]} seed {job[3]}: exit {p.returncode}, {res}, {time.time()-t:.0f}s", flush=True)
try:
    queue = list(todo)
    while queue or running:
        while queue and len(running) < args.jobs:
            job = queue.pop(0); os.makedirs(out_dir(job), exist_ok=True)
            log = open(os.path.join(out_dir(job), "log.txt"), "w")
            running.append((subprocess.Popen(command(job), stdout=log, stderr=subprocess.STDOUT, env=env_vars, cwd=HERE), job, time.time()))
        time.sleep(2); reap()
except KeyboardInterrupt:
    print("\ninterrupted: stopping runs (their snapshots so far are kept); summarizing what finished")
    for p, _, _ in running: p.send_signal(signal.SIGINT)
    for p, _, _ in running:
        try: p.wait(timeout=60)
        except subprocess.TimeoutExpired: p.kill()

# ---------------------------------------------------------------- statistics, table, chart
import numpy as np

def tcrit(df):
    """Two-sided 95% t critical value (no scipy available): table lookup, normal approximation for large df."""
    table = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228,
             12: 2.179, 15: 2.131, 20: 2.086, 25: 2.060, 30: 2.042, 40: 2.021, 60: 2.000, 120: 1.980}
    if df < 1: return float("nan")
    k = max(k for k in table if k <= df)
    return table[k] if df < 120 else 1.96

rows = {}                                   # (group, label) -> {seed: summary}
for g, l, o, sd in jobs:
    sm = summary_of((g, l, o, sd))
    if sm and sm.get("final_greedy_ms") is not None and sm["status"] == "ok":
        rows.setdefault((g, l), {})[sd] = sm
if not rows: sys.exit("no finished runs to summarize")
BASEKEY = ("baseline", "baseline")
bruns = rows.get(BASEKEY, {})
bmean = float(np.mean([s["final_greedy_ms"] for s in bruns.values()])) if bruns else float("nan")

def compare(runs):
    """Difference vs the baseline with a 95% CI, and a verdict.
    >=2 seeds: Welch t-test on the per-training-seed means (includes training AND workload noise).
    1 seed:    paired difference over the same evaluation workloads (workload noise only)."""
    m = np.array([r["final_greedy_ms"] for r in runs.values()])
    b = np.array([r["final_greedy_ms"] for r in bruns.values()])
    if len(m) >= 2 and len(b) >= 2:
        va, vb = m.var(ddof=1) / len(m), b.var(ddof=1) / len(b)
        se = float(np.sqrt(va + vb)); d = float(m.mean() - b.mean())
        df = (va + vb) ** 2 / ((va ** 2 / (len(m) - 1)) + (vb ** 2 / (len(b) - 1))) if (va + vb) > 0 else 1
        basis = f"{len(m)} vs {len(b)} seeds (Welch)"
    else:
        sd = next(iter(runs))
        if sd in bruns and runs[sd].get("final_per_seed") and bruns[sd].get("final_per_seed") \
                and len(runs[sd]["final_per_seed"]["dqn"]) == len(bruns[sd]["final_per_seed"]["dqn"]):
            diff = np.array(runs[sd]["final_per_seed"]["dqn"]) - np.array(bruns[sd]["final_per_seed"]["dqn"])
            diff = diff[~np.isnan(diff)]; n = len(diff)
            se = float(diff.std(ddof=1) / np.sqrt(n)); d = float(diff.mean()); df = n - 1
            basis = f"paired over {n} workloads, 1 seed (workload noise only)"
        else:
            return float("nan"), float("nan"), float("nan"), float("nan"), "no baseline to compare", "n/a"
    t = tcrit(df); lo, hi = d - t * se, d + t * se
    verdict = "better" if hi < 0 else ("worse" if lo > 0 else "within noise")
    return d, lo, hi, se, basis, verdict

table = []
for exp_no, ((g, l), runs) in enumerate(rows.items(), 1):
    v = np.array([r["final_greedy_ms"] for r in runs.values()])
    se_disp = float(v.std(ddof=1) / np.sqrt(len(v))) if len(v) > 1 else float(np.mean([r["final_greedy_se"] for r in runs.values()]))
    if (g, l) == BASEKEY:
        d = lo = hi = float("nan"); basis, verdict = "reference", "baseline"
    else:
        d, lo, hi, _, basis, verdict = compare(runs)
    table.append(dict(exp=exp_no, group=g, experiment=l, seeds=len(v), final_greedy_ms=float(v.mean()), std_error=se_disp,
                      diff_vs_baseline_ms=d, ci95_lo=lo, ci95_hi=hi, verdict=verdict, basis=basis,
                      interaction_ms=float("nan"),
                      last_train_ms=float(np.mean([r["last_train_mean_ms"] for r in runs.values()])),
                      hangs=sum(r["disksim_hangs"] for r in runs.values()),
                      minutes=float(np.mean([r["seconds"] for r in runs.values()])) / 60))
if combo_parts:
    # interaction = combo - (single_a + single_b - baseline): negative = the pair helps more than the sum of its parts
    by_label = {d["experiment"]: d for d in table}
    for d in table:
        pa = combo_parts.get(d["experiment"])
        if pa and pa[0] in by_label and pa[1] in by_label and bmean == bmean:
            d["interaction_ms"] = d["final_greedy_ms"] - (by_label[pa[0]]["final_greedy_ms"] + by_label[pa[1]]["final_greedy_ms"] - bmean)
table.sort(key=lambda d: d["final_greedy_ms"])
fc = float(np.mean([r["fcfs_ms"] for rr in rows.values() for r in rr.values()]))
ss = float(np.mean([r["sstf_ms"] for rr in rows.values() for r in rr.values()]))
print(f"\nFCFS {fc:.1f} ms   SSTF {ss:.1f} ms   baseline {bmean:.1f} ms   (final greedy eval, lower is better; {args.eval_episodes} workloads/run)")
print(f"{'experiment':22s} {'seeds':>5s} {'final ms':>9s} {'±s.e.':>6s} {'diff vs base':>13s} {'95% CI':>19s}  verdict")
shown = table[:30] if combo_parts else table
if combo_parts: print(f"(--combo: showing the best 30 of {len(table)} rows; all rows, with interaction_ms, are in results.csv)")
for d in shown:
    ci = f"[{d['ci95_lo']:+.1f}, {d['ci95_hi']:+.1f}]" if d["ci95_lo"] == d["ci95_lo"] else "-"
    df_ = f"{d['diff_vs_baseline_ms']:+.1f}" if d["diff_vs_baseline_ms"] == d["diff_vs_baseline_ms"] else "-"
    print(f"{d['experiment']:22s} {d['seeds']:5d} {d['final_greedy_ms']:9.1f} {d['std_error']:6.1f} {df_:>13s} {ci:>19s}  {d['verdict']}"
          + (f"  interaction {d['interaction_ms']:+.1f}" if d["interaction_ms"] == d["interaction_ms"] else ""))
print("verdict = 'better'/'worse' only if the 95% CI of (experiment - baseline) excludes 0; otherwise 'within noise'.")
if args.seeds == 1:
    print("note: with 1 seed the CI reflects evaluation-workload noise only; run-to-run training noise is NOT included. Use --seeds 3 or more.")
with open(os.path.join(SWEEP, "results.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(table[0])); w.writeheader(); w.writerows(table)
with open(os.path.join(SWEEP, "experiments.csv"), "w", newline="") as f:      # key for the numbered bars in comparison.png
    w = csv.writer(f)
    for d in sorted(table, key=lambda d: d["exp"]): w.writerow([d["exp"], d["experiment"]])

import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
if combo_parts: table = table[:40]          # chart only the best 40 when there are many combinations
fig, ax = plt.subplots(figsize=(10, 0.45 * len(table) + 2.4))
labels = [f"#{d['exp']}" for d in table]; vals = [d["final_greedy_ms"] for d in table]
colmap = {"better": "#08519c", "worse": "#d95f5f", "within noise": "#9e9e9e", "baseline": "#ff7f0e", "n/a": "#cccccc"}
y = np.arange(len(table))[::-1]
ax.barh(y, vals, xerr=[d["std_error"] for d in table], color=[colmap[d["verdict"]] for d in table], capsize=3)
for yi, d in zip(y, table):
    ax.text(d["final_greedy_ms"] + d["std_error"], yi, f"  {d['final_greedy_ms']:.1f} ms  ({d['verdict']})", va="center", fontsize=8)
ax.axvline(bmean, color="#ff7f0e", ls="--", lw=1, label=f"baseline {bmean:.1f}")
ax.axvline(ss, color="#2ca02c", ls="--", lw=1, label=f"SSTF {ss:.1f}"); ax.axvline(fc, color="#d62728", ls="--", lw=1, label=f"FCFS {fc:.1f}")
ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=8); ax.set_xlabel("final greedy mean response time (ms) - lower is better; bars = ± std. error")
ax.set_title(f"{name}: {args.seeds} seed(s), {args.episodes} episodes, {args.eval_episodes} eval workloads\n"
             "blue = significantly better than baseline, red = significantly worse, grey = within noise (95% CI)", fontsize=9)
ax.legend(fontsize=8, loc="upper left", bbox_to_anchor=(1.01, 1.0))
fig.tight_layout(); fig.savefig(os.path.join(SWEEP, "comparison.png"), dpi=130)
print(f"\nsaved: {SWEEP}/results.csv, experiments.csv, comparison.png  ({time.time()-t0:.0f}s)")
