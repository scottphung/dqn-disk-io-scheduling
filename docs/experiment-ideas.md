# Experiment Ideas

This document tracks possible experiments for the project.

> **Important:** An experiment appearing here does not mean it is required.  
> Our priority is getting the minimum DQN experiment working first.

---

## Experiment Overview

| Priority | Experiment | Research Question | Status |
|---|---|---|---|
| 🔴 **Required** | DQN vs FCFS vs SSTF | Can DQN learn request ordering that reduces simulated batch completion time? | Planned |
| 🟡 Optional | Different Workload Patterns | Does DQN performance change with request locality? | Idea |
| 🟡 Optional | Generalization | Does the trained DQN work on unseen workloads? | Planned |
| 🟡 Optional | Different Batch Sizes | How does performance change with batch size? | Idea |
| 🟢 Future | DQN vs NEAT | How does RL compare with neuroevolution? | Future |
| 🟢 Future | Interactive DQN ↔ DiskSim | Does making decisions using updated disk state improve scheduling? | Future |

---

# 1. DQN vs Traditional Scheduling

**Priority:** 🔴 Required

### Research Question

Can a DQN learn a disk I/O request-ordering strategy that produces measurable differences in simulated batch completion time compared with traditional scheduling algorithms?

### Algorithms

| Scheduler | Description |
|---|---|
| DQN | Learned request-ordering policy |
| FCFS | Requests serviced in arrival order |
| SSTF | Request selected based on shortest seek-distance criterion |

### Experimental Controls

All methods should use:

- Same workload
- Same simulated HDD
- Same DiskSim configuration
- Same relevant initial conditions

### Metrics

| Metric | Priority |
|---|---|
| Batch completion time | **Primary** |
| Throughput | Optional |
| Mean response time | Optional |
| Tail response time | Optional |
| Model inference overhead | Optional |

---

# 2. Workload Pattern Experiment

**Priority:** 🟡 Optional

### Research Question

Does DQN performance change depending on workload locality?

| Workload | Description |
|---|---|
| Random | Requests distributed across disk locations |
| Clustered | Groups of requests located near one another |
| Sequential / Local | Requests concentrated around sequential locations |

Comparison:

```text
              Random
             /
DQN ─────── Clustered
             \
              Sequential

vs.

FCFS / SSTF
```

---

# 3. Generalization Experiment

**Priority:** 🟡 Recommended

### Research Question

Can the trained DQN perform effectively on workloads it did not encounter during training?

```text
Training Workloads
        ↓
     Train DQN
        ↓
    Freeze Model
        ↓
Unseen Test Workloads
        ↓
 DQN vs FCFS vs SSTF
```

### Rule

> Final testing workloads must remain separate from DQN training.

---

# 4. Different Batch Sizes

**Priority:** 🟡 Optional

### Research Question

How does scheduler performance change when the number of pending requests changes?

| Batch | Size |
|---|---|
| Small | TBD |
| Medium | TBD |
| Large | TBD |

This experiment depends on whether our DQN representation supports variable batch sizes.

---

# 5. DQN vs NEAT

**Priority:** 🟢 Future Work

### Research Question

How does reinforcement-learning-based scheduling compare with neuroevolution?

Possible comparison:

```text
DQN ───┐
NEAT ──┼──→ DiskSim → Performance
FCFS ──┤
SSTF ──┘
```

### Decision

Do **not** implement this until the primary DQN experiment works.

NEAT was part of the original project direction and remains useful as a possible extension.

---

# 6. Interactive DQN ↔ DiskSim

**Priority:** 🟢 Advanced / Future Work

### Current Approach

```text
DQN
 ↓
Build complete order
 ↓
DiskSim
 ↓
Completion time
```

### Possible Advanced Approach

```text
DQN chooses request
        ↓
DiskSim executes request
        ↓
Updated disk state
        ↓
DQN chooses next request
        ↓
       ...
```

### Research Question

Does providing updated simulated disk state after every scheduling decision improve the learned scheduler?

### Dependency

We must first determine whether DiskSim can practically support this interaction.

---

# Experiment Checklist

Before declaring an experiment ready:

| Requirement | Complete? |
|---|---|
| Research question defined | ⬜ |
| Workloads fixed | ⬜ |
| Training/test split fixed | ⬜ |
| DiskSim configuration fixed | ⬜ |
| Baselines fixed | ⬜ |
| Metrics defined | ⬜ |
| Random seeds recorded | ⬜ |
| DQN configuration recorded | ⬜ |
| Raw results preserved | ⬜ |
| Experiment reproducible | ⬜ |