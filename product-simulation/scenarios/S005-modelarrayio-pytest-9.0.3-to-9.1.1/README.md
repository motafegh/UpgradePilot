# S005 — ModelArrayIO: pytest 9.0.3 → 9.1.1

> **Execution status:** Complete at the justified action-changing stop.  
> **Artifact lifecycle:** Complete prospective run with screening, frozen-baseline, evidence, decision, and degraded-validation checkpoints.  
> **Primary result:** Repository-specific evidence changed the baseline action.  
> **Factual review:** AI review complete.  
> **Ali review:** Pending.

## Frozen case

- Repository: `PennLINC/ModelArrayIO`
- Pull request: `#85`
- Base SHA: `915781a6c967f22b9236ecba072300932c2f41f0`
- Head SHA: `b590cfe93fbe49235f0f68d2b87102672f8a0aa0`
- Observed merge commit: `f7f58496507477c7ebaba40921859c18c771c1e4`
- Changed file: `uv.lock`
- Dependency: pytest `9.0.3` → `9.1.1`
- Run: `s005-20260723T123700Z-r1`

## Result

Transparent baseline v0.1 selected:

> `run_targeted_checks`

The completed full simulation selected:

> `merge_after_normal_review`

Classification:

> `baseline_wrong_action`

The action changed because the exact proposed pytest 9.1.1 lock resolution passed across Python 3.11–3.14, the Python 3.12 job included downloaded-data tests, the official breaking behavior was not activated, and every listed deprecation surface was absent or used in a supported form. No remaining target-specific question identified a useful additional check.

## Read in this order

1. [`CASE.md`](CASE.md)
2. [`artifacts/BASELINE_RESULT.json`](artifacts/BASELINE_RESULT.json)
3. [`artifacts/FINDINGS.json`](artifacts/FINDINGS.json)
4. [`artifacts/CHECK_EXECUTIONS.jsonl`](artifacts/CHECK_EXECUTIONS.jsonl)
5. [`artifacts/DECISION.json`](artifacts/DECISION.json)
6. [`artifacts/HUMAN_REPORT.md`](artifacts/HUMAN_REPORT.md)
7. [`artifacts/MACHINE_REPORT.json`](artifacts/MACHINE_REPORT.json)
8. [`artifacts/FOLLOW_UP_STATE.json`](artifacts/FOLLOW_UP_STATE.json)

No target repository was mutated, commented on, approved, rerun, closed, or merged by UpgradePilot.