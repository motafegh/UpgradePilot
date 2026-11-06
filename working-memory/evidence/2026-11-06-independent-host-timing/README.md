# Independent host timing method: prospective qualification

November6, 2026; product horizon `1e5d3aec`. [Cycle](../../2026-11-06_independent-host-timing-and-retained-traversal_cycle.md) and [frozen timing responsibility](../2026-11-06-native-normal-product-attempt-contract/CONTRACT.md#timing-preflight-and-separate-retained-traversal).

This dated developer diagnostic measures local controlled work, not a fresh product capture. No product code, policy/worker clocks, resource caps, machine settings, credentials, external service or target code changes. Earlier packets remain immutable.

## Frozen preflight before observation

`run_preflight.py --output NEW_PRIVATE_DIRECTORY` freezes method/installed source hashes before starting `host_clock.ps1` through Windows PowerShell with NoProfile/NoLogo/NonInteractive and an explicit trusted command body. No execution-policy override. The Windows process owns .NET Stopwatch/QPC and reports its frequency/high-resolution flag, elapsed ticks, absolute QPC timestamps and UTC ticks. Local stdin/stdout protocol is ready→begin/sample/end→quit. It cannot collect or select product evidence.

The begin acknowledgement precedes WSL child creation; end follows child exit. Thus host duration encloses command launch/import/exit and protocol delay. Inner counters cover only probe work. These scopes are retained separately; no startup subtraction or false equal-span assertion. Fixed phases: empty child;10-second sleep;10-process-CPU-second serial loop. One sequence,90host-second cap after watcher readiness; startup/response watchdog5raw-monotonic seconds. No replacement probe or automatic enlargement. An unavailable bridge before the first phase is an unperformed preflight, not a passed clock test.

Poll at approximately250ms and retain every host observation gap plus child exit/output. A gap above2seconds makes active-time interpretation inconclusive. Outer elapsed still includes the observed gap; no pause is silently subtracted. Interrupt/timeout stops the actual child process group and preserves the recorded failure; no restart.

Prospective qualification requires all three phases exit0; positive consistent high-resolution QPC frequency; no gap above2seconds; idle/CPU outer QPC versus matching Windows UTC interval disagreement at most5%; CPU probe process/getrusage disagreement at most5%; serial CPU consumption no greater than105% of its enclosing host elapsed. These are coherence screens, not proof of perfect physical calibration. Failure is retained as unavailable/failed/inconclusive; do not retune the criteria to obtain a pass. Report WSL monotonic/raw readings and their ratios to the host envelope, with launch overhead unremoved. Qualifying a host envelope does not require rewriting WSL clocks or explaining their root cause.

Only sufficiently qualified independent observation admits the separately frozen one60-page traversal. Its method/input/installed freeze and exact content/cold-recovery checks must be recorded before execution. No new live provider attempt follows automatically.
