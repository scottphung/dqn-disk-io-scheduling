# DQN on DiskSim

## Memory Leak

DiskSim is a 2000s-era C simulator built on global state. It has no "rewind" operation, so the only way to get a clean disk at t=0 is to tear it down and call dsim_init again, which re-parses the .parv file and rebuilds the disk model. dsim.py notes that only one instance can be open per process (DiskSim._live).

That gives these counts:

- dqn_smoke.py: one reset() per training episode (dqn_smoke.py:154-155). It also resets for each periodic snapshot evaluation and for the final evaluation (--eval-episodes, with fixed seeds 1000..). A run of 1000 training episodes plus evals therefore makes thousands of dsim_init calls.
- main.py: this is a sweep driver. It builds jobs = experiments × seeds and launches each as a separate python -I dqn_smoke.py ... subprocess, with --jobs of them in parallel. So every job is its own process, and each one runs the reset-per-episode loop above.

2. Why recycling is needed

It isn't garbage collection in the Python sense. The docstring in disksim_env/recycling.py gives the reason: DiskSim leaks about 0.5 MB on every (re)initialization and never frees it.

- dsim_shutdown doesn't release everything that dsim_init allocates. The leaked memory is malloc'd C memory, so Python's gc can't see it or reclaim it.
- At 0.5 MB per reset and thousands of resets (training, snapshot evals, final evals), that reaches gigabytes. With several sweep jobs in parallel, the total multiplies.

The workaround is RecyclingEnv. It runs the real DiskSchedEnv in a worker subprocess (worker.py) and replaces that process every --recycle-every resets (default 250). When a process exits, the OS reclaims all its memory, leaked or not. That keeps memory flat however long the run is.

Related details:

- The worker uses os._exit(0) so it never touches DiskSim's global state during interpreter teardown.
- The parent restarts a worker that crashes or hangs.
- Callers must pass seed= to reset(), because a fresh worker can't continue the old one's random stream.

The real fix

The proper fix would be in the C code: make dsim_shutdown free what dsim_init allocates, or add a cheap dsim_reset that restores initial state without reparsing. Neither is done, so process recycling is the workaround. I haven't measured the 0.5 MB figure myself. It comes from the comments and the --recycle-every help text. If you'd like, I can run valgrind or a tracemalloc/RSS loop over dsim_init/dsim_shutdown to see which allocations leak.