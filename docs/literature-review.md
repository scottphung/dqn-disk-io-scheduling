# Literature Review

## Research Questions

For each paper, we want to answer:

1. What AI/ML modifications to disk I/O scheduling have previously been researched?
2. What metrics were used to measure success?
3. What tools/simulators were used?
4. What can our project do differently?

---

## Papers

### A Survey on AI for Storage

**Year:** 2022

**Purpose:**
Survey of AI applications across different components of storage systems.

**Why it matters:**
Provides broader context for how AI has been applied to storage systems.

**Questions to investigate:**
- Which sections specifically discuss I/O scheduling?
- Which ML/RL methods have already been attempted?
- Which papers should we follow from its references?

---

### Towards Machine Learning-Based I/O Scheduling

**Year:** 2025? — verify publication information.

**Approaches:**

1. Classify workloads and choose the scheduler expected to provide the
   highest throughput.
2. Modify shortest-job-first by training a neural network to predict request
   latency and prioritize requests expected to complete quickly.

**Metrics:**
- HDD throughput (operations/second)

**Tools:**
- TODO: determine from paper.

**Possible difference from our project:**
Rather than using a neural network to select an existing scheduler or predict
latency, our current project proposes using reinforcement learning to learn
request-ordering decisions based on simulated performance feedback.

---

### Hardware Design of a New Genetic Based Disk Scheduling Method

**Year:** 2011

**Approach:**
Used genetic programming for disk-request scheduling and a neural network
to simulate seek time.

**Metric:**
- Makespan: time at which the final task in the execution order completes.

**Why it matters:**
Contains a useful review of earlier HDD scheduling research.

**Possible difference from our project:**
DiskSim may provide the disk simulation rather than requiring a neural
network to model seek time.

**Need to verify:**
- Exact experimental setup
- Simulator/hardware used
- How workloads were generated

---

### Evolving Neural Networks Through Augmenting Topologies

**Authors:** Stanley and Miikkulainen

**Year:** 2002

**Approach:**
Introduces NEAT, an evolutionary approach that evolves neural-network
weights and topology.

**Relevance:**
This was part of the project's original NEAT direction.

**Current status:**
NEAT is not part of the current minimum DQN implementation.

**Possible future experiment:**
Compare DQN with a NEAT-based scheduling approach if time and project
scope allow.

---

### Self-Learning Disk Scheduling

**Year:** 2009

**Purpose:**
Investigated learning-based disk scheduling and discussed the research
gap around machine learning for disk I/O scheduling at the time.

**Why it matters:**
Useful for establishing the historical development of ML-based disk
scheduling.

**Need to investigate:**
- Learning algorithm
- Workload
- Evaluation metrics
- Simulator/hardware
- Main findings

---

### Optimization of Disk Seek Operations Using Neural Networks

**Year:** 2002

**Approach:**
Used a neural network to select an appropriate disk I/O scheduling
algorithm based on current conditions.

The neural network selected between existing algorithms rather than
creating a new scheduling policy.

**Possible difference from our project:**
Our DQN attempts to construct the request ordering itself rather than
only choosing an existing scheduler.

---

### Towards Better Understanding of Black-box Auto-Tuning:
### A Comparative Analysis for Storage Systems

**Year:** 2018

**Approach:**
Investigated several optimization techniques, including AI/genetic
algorithms, for storage-system parameter tuning.

**Why it matters:**
Closely related application of learning/optimization to storage systems.

**Difference from our project:**
The work focuses more broadly on storage-system parameter tuning rather
than specifically learning HDD request ordering.

---

## Literature Comparison Table

| Paper | Year | Approach | Scheduling Modification | Metrics | Simulator/Tools | Difference From Our Project |
|---|---:|---|---|---|---|---|
| A Survey on AI for Storage | 2022 | Survey | N/A | TODO | TODO | Provides background |
| Towards ML-Based I/O Scheduling | 2025? | NN / workload classification | Scheduler selection + latency prediction | Throughput | TODO | DQN directly learns ordering |
| Genetic Based Disk Scheduling | 2011 | GP + NN | Request scheduling | Makespan | TODO | DQN + DiskSim |
| NEAT | 2002 | Neuroevolution | General NN optimization | N/A | N/A | Original project direction |
| Self-Learning Disk Scheduling | 2009 | TODO | Learning-based scheduling | TODO | TODO | Determine after reading |
| Disk Seek Optimization Using NN | 2002 | NN | Select existing scheduler | TODO | TODO | DQN generates ordering |
| Black-box Auto-Tuning | 2018 | Multiple optimization algorithms | Storage parameter tuning | TODO | TODO | We focus on request scheduling |

## Current Research Gap / Motivation

Current working hypothesis:

Previous research has applied machine learning to areas including:

- Selecting existing scheduling algorithms
- Predicting request latency
- Genetic/evolutionary scheduling
- Storage-system parameter tuning

Our project investigates whether a DQN can instead learn request-ordering
decisions from simulated disk-performance feedback.

This statement is currently a working hypothesis and should be refined
after completing the literature review.

## TODO

- [ ] Verify publication information for each paper
- [ ] Complete missing metrics
- [ ] Identify simulator/hardware used by each study
- [ ] Record dataset/workload design
- [ ] Record main findings
- [ ] Identify limitations stated by authors
- [ ] Search references for additional related work
- [ ] Finalize research gap only after literature review is complete