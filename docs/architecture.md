# Project Architecture

## Overview

The goal of this project is to investigate whether a Deep Q-Network (DQN)
can learn an effective disk I/O scheduling strategy using performance
feedback from DiskSim.

## High-Level Architecture

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
   ↓
DQN Training

## Components

### 1. Workload

The workload contains a batch of disk I/O requests.

The exact workload format and batch size will be finalized after the team
finishes reviewing DiskSim and related literature.

Responsibilities:
- Generate reproducible workloads
- Separate training and testing workloads
- Ensure the same workloads can be used across scheduling methods

---

### 2. DQN Scheduler

The DQN examines the available requests and constructs a request ordering.

At each decision step:

1. Examine remaining requests
2. Estimate Q-values for available actions
3. Select the next request
4. Remove the selected request
5. Repeat until the schedule is complete

The exact state representation, network architecture, and training
hyperparameters are still under investigation.

---

### 3. DiskSim Integration

DiskSim acts as the simulated HDD environment.

The integration layer will:

1. Receive a workload and request ordering
2. Convert them into a DiskSim-compatible format
3. Execute DiskSim
4. Read the simulation output
5. Extract the required performance metrics
6. Return the result for training/evaluation

Target interface concept:

    completion_time = evaluate_schedule(requests, order)

The internal implementation is still to be determined.

---

### 4. Reward

Current proposed reward:

    R = -T_batch

where `T_batch` is the total simulated batch completion time.

A shorter completion time therefore produces a higher reward.

---

### 5. Evaluation

The trained DQN will be evaluated using workloads that were not used
during training.

Initial baseline algorithms:

- FCFS
- SSTF

Possible additional baselines/experiments may be added later.

Primary proposed metric:

- Total batch completion time

Additional DiskSim metrics may be evaluated if useful.

## Component Ownership

### DQN Development and Training
- DQN implementation
- State/action representation
- Training loop
- Exploration strategy
- Model configuration

### DiskSim and Workload Integration
- DiskSim setup/configuration
- Workload representation/generation
- DQN schedule → DiskSim integration
- Simulation execution
- Output parsing

### Testing and Performance Analysis
- Baseline testing
- Held-out workload evaluation
- Performance comparison
- Figures/tables
- Statistical/result analysis

## Open Architecture Questions

- What exactly constitutes one workload batch?
- Does 4 KB refer to each request or the entire workload?
- What information should the DQN receive as its state?
- How will request ordering be enforced in DiskSim?
- What exact data format will connect DQN and DiskSim?
- Which DiskSim output represents our batch completion time?
- Should additional metrics besides completion time be reported?
- Should NEAT remain an optional experiment or be removed from scope?

These questions should be resolved before the relevant implementation
depends on them.