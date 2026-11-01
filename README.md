# Deep Q-Network Based Disk I/O Scheduling

**CSC 720 — Storage Systems**  
**Missouri State University**  
**Fall 2026**

## Project Goal

This project investigates whether a **Deep Q-Network (DQN)** can learn an effective disk I/O scheduling strategy using performance feedback from **DiskSim**.

The DQN will construct an ordering of disk I/O requests. DiskSim will simulate that ordering and return the resulting completion time, which can then be used as feedback for training and evaluation.

---

## System Overview

```text
Workload
   ↓
DQN Scheduler
   ↓
Request Ordering
   ↓
DiskSim
   ↓
Batch Completion Time
   ↓
Reward / Evaluation
```

---

## Team Responsibilities

| Area | Responsibilities |
|---|---|
| 🧠 **DQN Development & Training** | DQN implementation, state/action representation, training loop, exploration strategy, model configuration |
| 💾 **DiskSim & Workload Integration** | DiskSim configuration, workload generation, DQN → DiskSim integration, simulation execution, output parsing |
| 📊 **Testing & Performance Analysis** | FCFS/SSTF baselines, experiment execution, held-out testing, performance analysis, figures/tables |

---

## Initial Evaluation

The minimum experiment will compare:

| Scheduler | Type |
|---|---|
| **DQN** | Learned scheduling policy |
| **FCFS** | Traditional baseline |
| **SSTF** | Traditional baseline |

All scheduling methods should be evaluated using the same workloads and DiskSim configuration.

### Primary Metric

**Total batch completion time**

Additional metrics may be added after further research.

---

## Hyperparameter Sweep (`python/main.py`)

`python/main.py` runs "current vs try" hyperparameter experiments for the DiskSim DQN, **one knob at a time**. The baseline uses the `examples/dqn_smoke.py` defaults, and every other experiment changes a single setting (train frequency, episodes, gamma, batch size, learning rate, target update, hold, final epsilon, replay size; optionally environment/reward options). Each run is a separate `dqn_smoke.py` process, and runs execute in parallel. At the end it compares each experiment to the baseline (95% CI verdict: better / worse / within noise) against the FCFS and SSTF baselines.

### Usage

```bash
cd python
python3 main.py --dry-run                      # show the plan and time estimate; runs nothing
python3 main.py --groups gamma,batch --seeds 1 --episodes 200 --jobs 4   # quick partial test
python3 main.py --episodes 1000 --seeds 3 --jobs 4                      # full sweep
python3 main.py --name sweep1 --resume         # continue an interrupted sweep (skips finished runs)
```

| Option | Default | Meaning |
|---|---|---|
| `--groups` | all except `env` | Comma list: `train_every, episodes, gamma, batch, lr, tgt_update, hold, eps_end, replay, env` |
| `--include-env` | off | Also run the environment-argument group |
| `--episodes` | 1000 | Episodes per run |
| `--seeds` | 3 | Training seeds per experiment (more = less noise, more time) |
| `--jobs` | 4 | Parallel runs (1 CPU thread each) |
| `--snap-every` | 100 | Snapshot interval (larger = faster) |
| `--name`, `--resume` | timestamp | Name the sweep / resume it |

Output goes to `python/results/sweeps/<name>/`: `results.csv`, `comparison.png`, and `runs/<label>_s<seed>/` (log, history CSV, weights, snapshots). Ctrl+C stops cleanly and still summarizes finished runs.

### ⚠️ Warning: the full sweep takes hours

The default full sweep is 23 experiments × 3 seeds = **69 training runs**. Rough estimates printed by `--dry-run` (based on ~6.3 min per 1000-episode baseline run with 4 jobs in parallel):

| Configuration | Estimated wall-clock |
|---|---|
| Default (`--seeds 3 --jobs 4`) | **~2.5 hours** (~580 CPU-minutes) |
| `--include-env --seeds 5 --jobs 6` | **~3 hours** (~1,060 CPU-minutes) |

The `episodes=3000`/`5000` and `train_every=1` runs are the slowest (a single run can take 30+ minutes), and the sweep keeps all `--jobs` CPUs busy the whole time. Always run `--dry-run` first, start with a small subset (`--groups`, `--seeds 1`, fewer `--episodes`), and use `--resume` if interrupted. Estimates are approximate and depend on your hardware.

---

## Project Timeline

| Target | Milestone |
|---|---|
| **Oct 1–4** | 📚 Research, planning, and architecture |
| **Oct 5** | 🛠️ Implementation begins |
| **Oct 18** | Individual components working |
| **Nov 1** | ⭐ First complete DQN → DiskSim pipeline |
| **Nov 15** | Stable experiment pipeline |
| **Nov 22** | ⭐ Final experiments complete |
| **Dec 6** | First report draft complete |
| **Dec 7–13** | 🎓 Final report, repository, and presentation |

Full roadmap: [`docs/weekly-progress.md`](docs/weekly-progress.md)

---

## Repository Structure

```text
dqn-disk-io-scheduling/
│
├── README.md
│
├── docs/
│   ├── architecture.md
│   ├── literature-review.md
│   ├── experiment-ideas.md
│   └── weekly-progress.md
│
├── dqn/
├── disksim/
├── workloads/
├── experiments/
└── results/
```

### Documentation

| Document | Purpose |
|---|---|
| [`architecture.md`](docs/architecture.md) | System architecture and component interfaces |
| [`literature-review.md`](docs/literature-review.md) | Related research and literature tracking |
| [`experiment-ideas.md`](docs/experiment-ideas.md) | Required and optional experiment ideas |
| [`weekly-progress.md`](docs/weekly-progress.md) | Weekly roadmap, milestones, and meeting notes |

---

## Current Status

### Week 0 — Research & Planning

- [x] Initial project proposal
- [x] Select DQN as primary learning approach
- [x] Define three main responsibility areas
- [x] Create GitHub repository
- [ ] Complete initial literature review
- [ ] Finalize high-level architecture
- [ ] Clarify workload representation
- [ ] Define component interfaces
- [ ] Create Week 1 GitHub Issues

> **Implementation begins next week.**

---

## Current Open Questions

- What exactly constitutes one workload batch?
- Does 4 KB refer to an individual request or an entire workload?
- What information should be included in the DQN state?
- How will the DQN-generated ordering be enforced in DiskSim?
- What exact interface should connect the DQN and DiskSim components?
- Which DiskSim statistic should be used as batch completion time?
- Which additional evaluation metrics should be reported?
- Should NEAT remain only as optional/future work?

---

## References

Research papers and related work are tracked in:

[`docs/literature-review.md`](docs/literature-review.md)

---

## Project Principle

> Build the smallest working end-to-end system first. Add additional experiments only after the core DQN → DiskSim → evaluation pipeline works reliably.