# Deep Q-Network Based Disk I/O Scheduling

CSC 720 – Storage Systems  
Missouri State University

## Project Goal

Investigate whether a Deep Q-Network (DQN) can learn an effective
disk I/O scheduling strategy using performance feedback from DiskSim.

## System Overview

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

## Team Responsibilities

### DQN Development & Training
- DQN implementation
- State/action representation
- Training
- Reward integration

### DiskSim & Workload Integration
- DiskSim configuration
- Workload generation
- Python/DiskSim integration
- Simulation output parsing

### Testing & Performance Analysis
- FCFS/SSTF baselines
- Experiment execution
- Performance comparison
- Results and visualization

## Project Status

Current Phase: Week 0 — Research & Planning

Implementation begins: October 5, 2026