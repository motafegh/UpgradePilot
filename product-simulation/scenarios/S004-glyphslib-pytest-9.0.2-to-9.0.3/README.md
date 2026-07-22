# S004 — glyphsLib: pytest 9.0.2 → 9.0.3

> **Execution status:** Complete at the justified early-stop point.  
> **Artifact lifecycle:** Complete prospective run with separate screening, frozen-baseline, authority-confirmation, decision, and validation checkpoints.  
> **Primary result:** Transparent baseline sufficient; deeper investigation added no material decision value.  
> **Factual review:** AI review complete.  
> **Ali review:** Pending.

## Frozen case

- Repository: `googlefonts/glyphsLib`
- Pull request: `#1145`
- Base SHA: `044f19e4b1437bfc4343592486f4e3c6040306d9`
- Head SHA: `f3cda8a94600e58d27f1bc17c99b7693718b6350`
- Observed merge commit: `a007710184f634557e6524b7e3b115bf74c91b73`
- Dependency: `pytest`
- Transition: `9.0.2` → `9.0.3`
- Run: `s004-20260722T224500Z-r1`

## Result

Both the transparent baseline and full simulation selected:

> `merge_after_normal_review`

The full process confirmed only the baseline’s material authority gap:

- pytest is directly pinned in the development requirements;
- tox installs that exact changed file and invokes pytest;
- exact-head ordinary tests passed on Python 3.10 and 3.14 across Ubuntu and Windows;
- a separate exact-head regression workflow reinstalled the proposed requirements and passed direct pytest regression tests;
- official pytest material describes 9.0.3 as a drop-in bug-fix release.

No action, targeted check, or material uncertainty changed. The scenario therefore stopped without activating failure attribution, dynamic reproduction, adapter analysis, advisory exploitability, platform analysis, or other conditional stages.

## Read in this order

1. [`CASE.md`](CASE.md)
2. [`artifacts/STOPPING_EVALUATION.json`](artifacts/STOPPING_EVALUATION.json)
3. [`artifacts/BASELINE_RESULT.json`](artifacts/BASELINE_RESULT.json)
4. [`artifacts/DECISION.json`](artifacts/DECISION.json)
5. [`artifacts/HUMAN_REPORT.md`](artifacts/HUMAN_REPORT.md)
6. [`artifacts/MACHINE_REPORT.json`](artifacts/MACHINE_REPORT.json)
7. [`artifacts/FOLLOW_UP_STATE.json`](artifacts/FOLLOW_UP_STATE.json)

No target repository was mutated, commented on, approved, rerun, closed, or merged by UpgradePilot.
