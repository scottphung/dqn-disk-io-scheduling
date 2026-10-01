# Literature Review

## Purpose

This document tracks research related to machine learning, artificial intelligence, optimization, and disk I/O scheduling.

For each paper, we want to answer four questions:

1. **What AI/ML modifications to disk I/O have already been researched?**
2. **What metrics were used to measure success?**
3. **What tools or simulators were used?**
4. **What can our project do differently?**

---

# Literature Matrix

| Paper | Year | Approach | Modification | Metrics | Tools | Relevance / Difference |
|---|---:|---|---|---|---|---|
| **A Survey on AI for Storage** | 2022 | Survey | Reviews AI applications across storage systems | TBD | TBD | Broad background for AI + storage |
| **Towards Machine Learning-Based I/O Scheduling** | 2025? ⚠️ | ML / Neural Networks | Workload classification + scheduler selection; NN latency prediction | HDD throughput (ops/sec) | TBD | Our DQN may directly learn request ordering |
| **Hardware Design of a New Genetic Based Disk Scheduling Method** | 2011 | Genetic Programming + NN | GP schedules requests; NN models seek time | Makespan | TBD | DiskSim may replace the need for an NN seek-time model |
| **Evolving Neural Networks Through Augmenting Topologies** | 2002 | NEAT | Evolves NN topology and weights | N/A | NEAT | Original project direction; possible future comparison |
| **Self-Learning Disk Scheduling** | 2009 | Learning-based scheduling | TBD after review | TBD | TBD | Useful historical reference for ML disk scheduling |
| **Optimization of Disk Seek Operations Using Neural Networks** | 2002 | Neural Network | NN selects an existing disk scheduling algorithm | TBD | TBD | Our DQN attempts to construct scheduling decisions rather than only select an existing algorithm |
| **Towards Better Understanding of Black-box Auto-Tuning** | 2018 | Multiple optimization techniques | Storage-system parameter tuning | TBD | TBD | Related AI/optimization work but broader than disk request ordering |

> ⚠️ Information marked **TBD** or **?** has not yet been verified from the paper.

---

# 1. A Survey on AI for Storage

**Year:** 2022

### Current Notes

Survey of artificial intelligence applications across different components of storage systems.

### Why It Matters

Useful for:

- Establishing broader AI + storage context
- Identifying previous approaches
- Finding additional papers through its references

### Review Status

| Question | Answer |
|---|---|
| AI/ML modification | Broad survey |
| Metrics | TBD |
| Tools | TBD |
| Useful citations found | TBD |
| Fully reviewed | ⬜ |

---

# 2. Towards Machine Learning-Based I/O Scheduling

**Year:** 2025? — **needs verification**

### Current Notes

Two approaches were identified from the current team notes.

#### Approach 1

Classify workloads and choose the scheduler with the highest expected throughput.

#### Approach 2

Modify shortest-job-first by training a neural network to predict the latency of each request and prioritize requests expected to complete quickly.

### Current Metric

- HDD throughput in operations per second

### Possible Difference From Our Project

Their approach appears to use neural networks for scheduler selection and/or latency prediction.

Our proposed DQN attempts to learn request-ordering decisions using simulated performance feedback.

### Review Status

| Question | Answer |
|---|---|
| AI/ML modification | Classification + NN |
| Metrics | Throughput |
| Tools | TBD |
| Dataset/workload | TBD |
| Main result | TBD |
| Fully reviewed | ⬜ |

---

# 3. Hardware Design of a New Genetic Based Disk Scheduling Method

**Year:** 2011

### Current Notes

The study used:

- Genetic Programming for scheduling disk requests
- A neural network to simulate seek time

### Metric

**Makespan**

Defined in the current notes as the time when the final task in the execution order completes.

### Why It Matters

The paper reportedly contains a useful review of HDD scheduling research available at the time.

### Possible Difference From Our Project

Our project intends to use DiskSim for disk simulation rather than training a neural network specifically to simulate seek time.

This needs to be confirmed after reviewing DiskSim's capabilities and the paper's methodology.

### Review Status

| Question | Answer |
|---|---|
| AI/ML modification | Genetic Programming + NN |
| Metrics | Makespan |
| Tools | TBD |
| Workload | TBD |
| Main result | TBD |
| Fully reviewed | ⬜ |

---

# 4. Evolving Neural Networks Through Augmenting Topologies

**Authors:** Stanley & Miikkulainen  
**Year:** 2002

### Approach

Introduces **NEAT — NeuroEvolution of Augmenting Topologies**.

NEAT evolves neural-network topology and weights through evolutionary methods.

### Project Relevance

NEAT was part of the original project direction.

The current project direction instead focuses on **Deep Q-Networks**.

### Current Decision

| Approach | Status |
|---|---|
| DQN | 🔴 Primary |
| NEAT | 🟢 Optional / Future Experiment |

NEAT should not increase the minimum implementation scope unless the team later decides to include it.

---

# 5. Self-Learning Disk Scheduling

**Year:** 2009

### Current Notes

The paper appears useful for understanding the historical research gap surrounding machine learning and disk I/O scheduling.

### Potential Use

Could help establish a chronological development:

```text
Traditional Scheduling
        ↓
Early Neural Network Approaches
        ↓
Self-Learning Scheduling
        ↓
Genetic / Optimization Methods
        ↓
Modern ML / RL Approaches
        ↓
Our DQN Experiment
```

### Review Status

| Question | Answer |
|---|---|
| Learning technique | TBD |
| Scheduling modification | TBD |
| Metrics | TBD |
| Simulator/hardware | TBD |
| Main findings | TBD |
| Fully reviewed | ⬜ |

---

# 6. Optimization of Disk Seek Operations Using Neural Networks

**Year:** 2002

### Current Notes

A neural network was used to select an appropriate existing disk I/O scheduling algorithm based on current conditions.

The neural network therefore selected among algorithms rather than directly creating a new scheduling policy.

### Possible Difference From Our Project

```text
Previous Approach

Current conditions
       ↓
Neural Network
       ↓
Choose Existing Scheduler


Our Proposed Approach

Current requests/state
       ↓
      DQN
       ↓
Choose Request Ordering
```

### Review Status

| Question | Answer |
|---|---|
| AI/ML modification | NN scheduler selection |
| Metrics | TBD |
| Tools | TBD |
| Main findings | TBD |
| Fully reviewed | ⬜ |

---

# 7. Towards Better Understanding of Black-box Auto-Tuning:
## A Comparative Analysis for Storage Systems

**Year:** 2018

### Current Notes

The study examines several optimization techniques, including AI/genetic approaches, for storage-system parameter tuning.

### Why It Matters

This is related to our project because it applies learning/optimization techniques to storage-system performance.

### Difference

The research appears to focus on broader storage-system parameter tuning rather than specifically learning HDD request ordering.

### Review Status

| Question | Answer |
|---|---|
| Optimization techniques | Multiple |
| Disk scheduling specifically | Not primary focus |
| Metrics | TBD |
| Tools | TBD |
| Main findings | TBD |
| Fully reviewed | ⬜ |

---

# Research Timeline

As papers are reviewed, we can develop a timeline such as:

| Period | Research Direction | Example |
|---|---|---|
| Early 2000s | Neural networks + disk scheduling | NN scheduler selection |
| Late 2000s | Self-learning scheduling | Self-Learning Disk Scheduling |
| Early 2010s | Evolutionary optimization | Genetic-based scheduling |
| Late 2010s | Storage auto-tuning | Black-box optimization |
| 2020s | Broader AI/storage + modern ML | AI for Storage survey / ML I/O scheduling |
| **2026 Project** | **Reinforcement learning** | **DQN request ordering + DiskSim** |

This timeline is preliminary and should be updated as papers are fully reviewed.

---

# Current Working Research Gap

### What Previous Work Appears to Have Explored

- Selecting existing scheduling algorithms using neural networks
- Predicting request latency
- Genetic/evolutionary scheduling
- Self-learning scheduling
- Storage-system parameter optimization

### What We Are Investigating

> Whether a Deep Q-Network can learn disk I/O request-ordering decisions using performance feedback from DiskSim.

⚠️ **This is currently a working research gap, not a final novelty claim.**

It should only become part of the final paper after the literature review confirms that closely equivalent work has not already addressed it.

---

# Literature Review Checklist

| Task | Status |
|---|---|
| Verify publication information | ⬜ |
| Read each paper beyond abstract/introduction | ⬜ |
| Record ML/AI technique | ⬜ |
| Record scheduling modification | ⬜ |
| Record workload/dataset | ⬜ |
| Record evaluation metrics | ⬜ |
| Record simulator/hardware | ⬜ |
| Record baselines | ⬜ |
| Record main findings | ⬜ |
| Record limitations | ⬜ |
| Search references for additional papers | ⬜ |
| Finalize research gap | ⬜ |

---

# References / Reading List

Add the team's paper links and formal citations here as they are verified.

When adding a paper, also update the **Literature Matrix** at the top of this document.