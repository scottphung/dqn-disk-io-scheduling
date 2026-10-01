# Weekly Project Roadmap

**Project:** Deep Q-Network Based Disk I/O Scheduling  
**Course:** CSC 720 — Storage Systems  
**Timeline:** October–December 2026

---

## 🎯 Major Milestones

| Target | Milestone |
|---|---|
| **Oct 1–4** | Research, planning, GitHub setup, and architecture agreement |
| **Oct 18** | DQN, DiskSim, and testing components working independently |
| **Nov 1** | ⭐ First complete DQN → DiskSim → Reward pipeline |
| **Nov 15** | Stable training and experimental pipeline |
| **Nov 22** | ⭐ Final experiments completed |
| **Dec 6** | Complete first report draft |
| **Dec 7–13** | Final report, repository, and presentation |

---

# 📚 Week 0 — Oct 1–4
## Research & Planning

**No implementation required this week.**

| DQN Development & Training | DiskSim & Workload Integration | Testing & Performance Analysis |
|---|---|---|
| Read DQN literature | Read DiskSim documentation | Continue literature review |
| Understand state/action/reward | Understand DiskSim CLI | Research previous ML disk schedulers |
| Understand Q-values | Understand `.parv` files | Identify evaluation metrics |
| Understand epsilon-greedy | Understand trace format | Research FCFS/SSTF baselines |
| Research DQN scheduling examples | Understand DiskSim output | Identify related experiments |
| Propose state/action representation | Research how request ordering can be controlled | Identify potential research gap |

### Team Tasks

- [ ] Create GitHub repository
- [ ] Confirm team roles
- [ ] Review proposal
- [ ] Agree on high-level architecture
- [ ] Organize literature review
- [ ] Identify unresolved technical questions
- [ ] Create Week 1 GitHub Issues
- [ ] Schedule weekly team meeting

### Milestone

> **Everyone should understand the overall system and their individual responsibility before implementation begins.**

---

# 🛠️ Week 1 — Oct 5–11
## First Working Components

| DQN Development & Training | DiskSim & Workload Integration | Testing & Performance Analysis |
|---|---|---|
| Create Python environment | Setup/compile DiskSim | Define baseline testing procedure |
| Build smallest DQN prototype | Run supplied DiskSim example | Understand FCFS |
| Propose state representation | Understand input/output files | Understand SSTF |
| Propose action representation | Document exact execution command | Finalize initial metrics |

### Team Milestone

> **Each component should independently do something that works.**

---

# 💾 Week 2 — Oct 12–18
## Custom Workloads

| DQN Development & Training | DiskSim & Workload Integration | Testing & Performance Analysis |
|---|---|---|
| Implement Q-value output | Understand ASCII trace format | Define workload families |
| Implement action selection | Create custom request batch | Define training/test separation |
| Handle valid actions | Run custom workload | Establish baseline procedure |
| Test DQN independently | Begin Python workload generator | Verify baseline behavior |

### ⭐ Milestone — Oct 18

> **Custom workloads successfully run through DiskSim and all three project components have working foundations.**

---

# ⚙️ Week 3 — Oct 19–25
## Automation

| DQN Development & Training | DiskSim & Workload Integration | Testing & Performance Analysis |
|---|---|---|
| Implement training loop | Automate Python → DiskSim | Build experiment structure |
| Implement epsilon-greedy | Generate trace automatically | Automate baseline experiments |
| Begin replay/training logic | Parse DiskSim output | Define results format |
| Test training mechanics | Extract completion time | Verify FCFS/SSTF results |

### Team Milestone

> **DiskSim evaluation can be triggered and processed automatically.**

Conceptually:

```text
Python
   ↓
Generate workload
   ↓
DiskSim
   ↓
Parse output
   ↓
Completion time
```

---

# 🔗 Week 4 — Oct 26–Nov 1
## System Integration

| DQN Development & Training | DiskSim & Workload Integration | Testing & Performance Analysis |
|---|---|---|
| Produce valid request ordering | Accept DQN request order | Verify execution |
| Validate selected actions | Convert ordering for DiskSim | Check request counts |
| Connect training to reward | Execute DQN workload | Verify baseline fairness |
| Handle invalid actions | Return completion time | Test end-to-end results |

### ⭐ Major Milestone — Nov 1

```text
Workload
    ↓
   DQN
    ↓
Request Ordering
    ↓
 DiskSim
    ↓
Completion Time
    ↓
  Reward
    ↓
   DQN
```

> **FIRST COMPLETE END-TO-END RUN**

---

# 🧠 Week 5 — Nov 2–8
## First Real Training

| DQN Development & Training | DiskSim & Workload Integration | Testing & Performance Analysis |
|---|---|---|
| Begin real DQN training | Stabilize wrapper | Run small controlled experiments |
| Monitor rewards | Handle failed simulations | Compare DQN vs FCFS |
| Debug learning behavior | Handle invalid input | Compare DQN vs SSTF |
| Save training information | Improve output parsing | Sanity-check results |

### Team Milestone

> **First meaningful DQN vs traditional scheduler results.**

---

# 🔬 Week 6 — Nov 9–15
## Stabilization & Expanded Experiments

| DQN Development & Training | DiskSim & Workload Integration | Testing & Performance Analysis |
|---|---|---|
| Tune training parameters | Freeze major DiskSim configuration | Expand workload experiments |
| Track training progress | Improve reproducibility | Run multiple controlled tests |
| Select promising configuration | Automate repeated workloads | Collect metrics |
| Document parameters | Record simulator configuration | Begin preliminary analysis |

### ⭐ Milestone — Nov 15

> **Stable experimental pipeline. Major architecture changes should stop here unless necessary.**

---

# 🧪 Week 7 — Nov 16–22
## Final Experiments

| DQN Development & Training | DiskSim & Workload Integration | Testing & Performance Analysis |
|---|---|---|
| Freeze final model/configuration | Run final workloads | Run held-out comparisons |
| Run final training | Verify DiskSim configuration | Collect final metrics |
| Save trained model | Verify traces/results | DQN vs FCFS vs SSTF |
| Document training settings | Preserve experiment files | Check result consistency |

### ⭐ Major Milestone — Nov 22

> **FINAL EXPERIMENTS COMPLETE**

No final-test workloads should be used to retrain the DQN.

---

# 📊 Week 8 — Nov 23–29
## Analysis & Documentation

| DQN Development & Training | DiskSim & Workload Integration | Testing & Performance Analysis |
|---|---|---|
| Document model | Document DiskSim setup | Analyze final results |
| Document state/action/reward | Document workload pipeline | Generate figures |
| Document training procedure | Clean integration code | Generate tables |
| Document limitations | Create setup instructions | Identify findings/limitations |

### Team Milestone

> **Final experimental results and figures available.**

---

# 📝 Week 9 — Nov 30–Dec 6
## Report Draft

| Section | Primary Responsibility | Status |
|---|---|---|
| Introduction | Team | ⬜ |
| Literature Review / Related Work | Team | ⬜ |
| Project Architecture | Team | ⬜ |
| DQN Methodology | DQN | ⬜ |
| DiskSim Setup | DiskSim | ⬜ |
| Workload Generation | DiskSim | ⬜ |
| Experimental Design | Testing | ⬜ |
| Results | Testing | ⬜ |
| Discussion | Team | ⬜ |
| Limitations | Team | ⬜ |
| Conclusion | Team | ⬜ |

### ⭐ Milestone — Dec 6

> **COMPLETE FIRST REPORT DRAFT**

---

# 🎓 Week 10 — Dec 7–13
## Finalization

| Task | Status |
|---|---|
| Review technical accuracy | ⬜ |
| Finalize report | ⬜ |
| Finalize figures/tables | ⬜ |
| Clean GitHub repository | ⬜ |
| Verify README | ⬜ |
| Verify setup instructions | ⬜ |
| Test repository from clean environment | ⬜ |
| Prepare presentation/demo | ⬜ |
| Practice explaining entire system | ⬜ |

### Final Milestone

> 🎉 **PROJECT COMPLETE**

---

# Weekly Meeting Template

**Date:**  
**Meeting #:**

## Progress

| Area | Last Week's Goal | Completed? | Blocker | Next Goal |
|---|---|---|---|---|
| DQN | | ⬜ | | |
| DiskSim | | ⬜ | | |
| Testing | | ⬜ | | |

## Important Decisions

| Decision | Reason |
|---|---|
| | |

## Questions / Blockers

- 
- 
- 

## Knowledge Sharing

**DQN:** What should the other members understand from this week's work?

> 

**DiskSim:** What should the other members understand from this week's work?

> 

**Testing:** What should the other members understand from this week's work?

> 

## GitHub Issues for Next Week

| Issue | Owner | Target |
|---|---|---|
| | | |
| | | |
| | | |

## Next Meeting

**Date:**  
**Main target:**