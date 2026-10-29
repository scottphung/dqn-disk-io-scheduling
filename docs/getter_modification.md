### Getting the Disk State

Added `disksim_get_disk_state()` to get the disk's cylinder, head, and rotational angle. It returns `0` if successful or `-1` if the state is unavailable.

Our C wrapper can call it after DiskSim finishes a request and no seek is in progress:

```c
struct disksim_disk_observation state;

if (disksim_get_disk_state(iface, 0, completion_time_ms, &state) == 0) {
    printf("%d %d %f\n",
           state.cylinder,
           state.head,
           state.angle_turns);
}
```

The angle is a fraction of one rotation. Multiply it by `360` to get degrees.

### Calling DiskSim from Python

We can still use `subprocess`, but we cannot start a new DiskSim process for every request because that would reset the disk state.

Instead, we will use `subprocess.Popen()` to start a C wrapper once per episode. The wrapper will keep DiskSim running, receive requests from Python, and return the disk state and completion time after each step.

Python will use these values to update the DQN's state and calculate the reward:

```python
reward = -(completion_time_ms - previous_completion_time_ms)
```