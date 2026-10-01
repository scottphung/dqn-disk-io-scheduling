# System Architecture

## 1. Objective

The project investigates whether a **Deep Q-Network (DQN)** can learn an effective disk I/O request-ordering strategy using simulated disk-performance feedback from **DiskSim**.

The minimum system consists of three major components:

1. DQN Scheduler
2. DiskSim & Workload Integration
3. Testing & Performance Analysis

---

# 2. High-Level Architecture

```text
                 ┌──────────────────┐
                 │     Workload     │
                 │   I/O Requests   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │  DQN Scheduler   │
                 │                  │
                 │ Choose request   │
                 │ ordering         │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Request Ordering │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │     DiskSim      │
                 │                  │
                 │ Simulate HDD     │
                 │ execution        │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Completion Time  │
                 └────────┬─────────┘
                          │
                    ┌─────┴─────┐
                    ▼           ▼
                 Reward     Evaluation
                    │
                    ▼
                   DQN
```

---

# 3. Component Responsibilities

| Component | Input | Responsibility | Output |
|---|---|---|---|
| **Workload Generator** | Workload configuration | Generate reproducible I/O request batches | Request batch |
| **DQN Scheduler** | Request batch / state | Determine request ordering | Request permutation |
| **DiskSim Integration** | Requests + ordering | Execute simulated HDD workload | Simulation results |
| **Reward** | Completion time | Convert performance into DQN feedback | Reward |
| **Evaluation** | Results | Compare scheduling approaches | Metrics / figures |

---

# 4. Workload

A workload represents a batch of disk I/O requests.

The exact representation is **not finalized**.

## Requirements

The workload system should eventually support:

- Reproducible workload generation
- Training workloads
- Held-out testing workloads
- Identical workloads across scheduler comparisons
- Unique request identification

## Open Questions

| Question | Status |
|---|---|
| What is the batch size? | 🔍 Research |
| Does 4 KB describe each request or the complete workload? | ❓ Needs clarification |
| What DiskSim trace format will be used? | 🔍 Research |
| Which request attributes are required? | 🔍 Research |
| Should multiple workload locality patterns be tested? | 💡 Proposed |

---

# 5. DQN Scheduler

The DQN will construct the request schedule **one decision at a time**.

Conceptually:

```text
Remaining Requests
        ↓
       DQN
        ↓
Q-value for each valid request
        ↓
Choose next request
        ↓
Remove selected request
        ↓
Repeat
```

until a complete request ordering has been produced.

## Proposed DQN Flow

```text
State
  ↓
Neural Network
  ↓
Q-values
  ↓
Action Selection
  ↓
Selected Request
```

## Training Concepts

| Concept | Purpose |
|---|---|
| Q-value | Estimate value of selecting an action |
| Epsilon-greedy | Balance exploration and exploitation |
| Reward | Provide performance feedback |
| Training episode | One scheduling/evaluation cycle |

Exact state representation, neural-network architecture, and hyperparameters remain **TBD**.

---

# 6. DiskSim Integration

DiskSim acts as the simulated HDD environment.

## Current DiskSim CLI

```text
disksim <parfile> <outfile> <tracetype> <tracefile> <synthgen> [overrides]
```

## Main Inputs

| Input | Purpose |
|---|---|
| `parfile` | Disk/controller/cache/scheduler configuration |
| `outfile` | Simulation output |
| `tracetype` | Trace format |
| `tracefile` | I/O request trace |
| `synthgen` | Input trace vs synthetic generation |
| Overrides | Optional runtime configuration changes |

## Proposed Integration Pipeline

```text
Python
   ↓
Receive requests + order
   ↓
Generate DiskSim-compatible trace
   ↓
Execute DiskSim
   ↓
Read output
   ↓
Extract completion time
   ↓
Return result
```

## Target Interface

Conceptually:

```python
completion_time = evaluate_schedule(requests, order)
```

The exact Python implementation is not yet defined.

---

# 7. Component Interface

One of the most important design decisions is establishing a clean boundary between the DQN and DiskSim components.

## Proposed Contract

### DQN → Integration

```text
Request Batch
+
Request Ordering
```

Example:

```text
Requests:
[A, B, C, D, E]

DQN Order:
[C, A, E, B, D]
```

### Integration → DQN

```text
Batch Completion Time
```

Example:

```text
14.72 ms
```

This allows the DQN implementation to remain independent from the internal details of DiskSim.

---

# 8. Reward

Current proposed reward:

```text
R = -T_batch
```

where:

`T_batch` = total simulated batch completion time.

Therefore:

```text
Shorter completion time
        ↓
Less negative reward
        ↓
Higher reward
```

The final reward design should be confirmed before training.

---

# 9. Evaluation Architecture

All scheduling methods should pass through equivalent evaluation conditions.

```text
              ┌── DQN ───┐
              │          │
Workload ─────┼── FCFS ──┼──→ DiskSim ──→ Results
              │          │
              └── SSTF ──┘
```

## Experimental Controls

All comparisons should attempt to maintain:

- Same workload
- Same simulated HDD
- Same DiskSim configuration
- Same relevant initial conditions

---

# 10. Initial Metrics

| Metric | Status |
|---|---|
| Batch completion time | 🔴 Primary |
| Throughput | 🟡 Candidate |
| Mean response time | 🟡 Candidate |
| Tail response time | 🟡 Candidate |
| DQN inference overhead | 🟢 Optional |
| Training time | 🟢 Optional |

Additional metrics should only be added when they contribute to the research question.

---

# 11. Current vs Future Architecture

## Minimum Project

```text
DQN
 ↓
Complete Request Ordering
 ↓
DiskSim
 ↓
Batch Completion Time
```

## Possible Future Extension

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

The interactive version should only be investigated after the minimum system works.

---

# 12. Open Architecture Questions

| Question | Owner | Status |
|---|---|---|
| Exact DQN state representation | DQN | 🔍 Research |
| Exact DQN action representation | DQN | 🔍 Research |
| DiskSim trace format | DiskSim | 🔍 Research |
| How to enforce request ordering | DiskSim | 🔍 Research |
| Python ↔ DiskSim interface | DiskSim | 🔍 Research |
| Primary output statistic | DiskSim + Testing | 🔍 Research |
| Training/test workload design | Testing + Team | 🔍 Research |
| Final evaluation metrics | Testing + Team | 🔍 Research |
| NEAT comparison | Team | 🟢 Optional |

---

# 13. Architecture Milestone

By **November 1**, the target system is:

```text
Workload
   ↓
DQN
   ↓
Request Order
   ↓
DiskSim
   ↓
Completion Time
   ↓
Reward
```

> **Goal: One complete end-to-end run before expanding the experiment.**