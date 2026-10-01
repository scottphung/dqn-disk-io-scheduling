# Experiment Ideas

This document contains possible experiments.

Ideas listed here are NOT automatically part of the required project scope.
Experiments should only move into implementation after team discussion.

---

# Minimum Experiment

## DQN vs Traditional Scheduling

### Research Question

Can a DQN learn a disk I/O request-ordering strategy that produces
measurable differences in simulated batch completion time compared with
traditional scheduling algorithms?

### Algorithms

- DQN
- FCFS
- SSTF

### Experimental Control

Each algorithm should receive:

- The same workload
- The same simulated disk
- The same DiskSim configuration
- The same relevant initial conditions

### Primary Metric

- Batch completion time

### Possible Additional Metrics

- Throughput
- Mean request response time
- Tail response time
- Training time
- Scheduler/model inference overhead

These are optional until the team decides which DiskSim statistics are
appropriate.

---

# Experiment Idea 1 — Workload Patterns

### Question

Does DQN performance change depending on the spatial/locality pattern of
the workload?

Possible workloads:

- Random requests
- Clustered requests
- Sequential/local requests

Compare:

    DQN
    FCFS
    SSTF

across each workload type.

---

# Experiment Idea 2 — Generalization

### Question

Can a trained DQN perform effectively on workloads it did not see during
training?

Possible design:

Training workloads
        ↓
Train DQN
        ↓
Freeze model
        ↓
Unseen test workloads
        ↓
Compare against FCFS/SSTF

Training and final testing workloads must remain separate.

---

# Experiment Idea 3 — Different Batch Sizes

### Question

How does scheduler performance change as the number of pending requests
changes?

Possible sizes:

- Small
- Medium
- Large

Exact batch sizes TBD.

This experiment depends on whether the chosen DQN representation supports
variable batch sizes.

---

# Experiment Idea 4 — DQN vs NEAT

### Status

OPTIONAL / FUTURE WORK

### Research Question

How does reinforcement-learning-based scheduling compare with an
evolutionary neural-network approach?

Possible comparison:

    DQN
     vs
    NEAT
     vs
    FCFS / SSTF

### Warning

This significantly increases project scope and should not be attempted
until the minimum DQN experiment works reliably.

---

# Experiment Idea 5 — Request-by-Request DiskSim Interaction

### Status

OPTIONAL / ADVANCED

Current proposed implementation:

    DQN builds complete order
            ↓
         DiskSim
            ↓
      Batch completion time

Possible advanced implementation:

    DQN selects request
            ↓
         DiskSim
            ↓
       Updated state
            ↓
    DQN selects next request
            ↓
           ...

### Research Question

Does allowing the DQN to make decisions using updated simulated disk
state improve scheduling?

This depends on whether DiskSim can practically be integrated at this
level.

---

# Experiment Checklist

Before running a final experiment:

- [ ] Research question clearly defined
- [ ] Workloads fixed
- [ ] Training/test split fixed
- [ ] Disk configuration fixed
- [ ] Baselines fixed
- [ ] Metric definitions fixed
- [ ] Random seeds recorded where applicable
- [ ] DQN training configuration recorded
- [ ] Raw results saved
- [ ] Experiment reproducible