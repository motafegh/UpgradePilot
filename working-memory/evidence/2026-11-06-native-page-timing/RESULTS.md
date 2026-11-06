# Matched page result: lower CPU counters, elapsed verdict inconclusive

The six prospectively frozen trials completed in the declared order without replacement, timeout or product edits. Every trial used its pinned112-file product tree, the same captured revision, a fresh process/store backup and identical first-page request. All delivered the same4,873 bytes with the same digest, unchanged native boundary and successful exact acknowledged-revision readback. The supervising maximum observed sampling gap was0.251seconds; no pause was detected by that screen. This does not prove every possible suspension absent.

| Page-stage counter median | Baseline `6e98d0a0` | Refined `38741c3c` |
|---|---:|---:|
| Process CPU seconds |15.238|12.377|
| Monotonic elapsed seconds |14.002|11.392|
| Raw monotonic seconds |15.275|12.427|

All three refined/baseline paired CPU ratios were below1; the median ratio was0.81265, approximately18.7% lower recorded CPU time. This is a repeatable local counter result for one page operation. It is not a90% speedup, a full60-page comparison, a cold-filesystem result or whole-product latency. The separate earlier156→15 decoder count measures only one component of work.

**The frozen overall timing verdict is `timing_inconclusive`.** All trials showed monotonic/raw disagreement around8.3%, above the5% limit, and CPU/monotonic ratios around1.09, above1.05. CPU and `getrusage` agree within0.000045%, so the raw summary's phrase `CPU clock inconsistency` specifically denotes the CPU-versus-monotonic screen; it does not mean those two CPU counters disagreed. Do not infer which clock is physically correct, why the discrepancy occurs, or that a VM/pause/threading explanation is established. The cause was not investigated or repaired in this slice. The lower CPU readings and elapsed qualification failure are separate conclusions.

The product change being measured already existed. This work added a frozen diagnostic and evidence, not another optimization. Imports, backup, reconstruction, host configuration and purpose publication are outside the page stage and remain separately recorded; trials are not fresh-provider runs. No limits, credentials, target code, source analyzer, storage semantics or historical packet changed.

## What the result permits

The capacity repair and complete60-page retained qualification remain established at their previous horizons. The publication optimization now has same-input CPU-counter evidence alongside decoder-count evidence. A reliable active or physical elapsed-latency claim remains unestablished; the earlier55-minute claim remains unsupported. No trial was rerun, no threshold was relaxed and no counter was silently discarded to obtain a positive verdict.

The bounded measurement's evidence collection and content checks completed; elapsed-performance acceptance did not pass. This planned inconclusive outcome creates no demonstrated product correctness defect and does not justify additional optimization by itself. If a real user-visible latency requirement later demands it, investigate clock calibration and re-enter under a new explicit protocol. Otherwise the project can return to the separately frozen normal-product attempt contract; this packet authorizes no live acquisition.

See [prospective protocol](README.md), [all trial counters and paired ratios](results-summary.json), [method/product/input/private artifact hashes](verification.json), and [cycle progression](../../2026-11-06_native-page-timing_cycle.md). Private evidence includes the original contract, complete supervision gaps, per-trial exact page/stores/results/logs and both historical source copies. The prospective README/method files remain unchanged after freezing.
