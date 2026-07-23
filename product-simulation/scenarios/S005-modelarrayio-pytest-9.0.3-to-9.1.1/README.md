# S005 — ModelArrayIO: pytest 9.0.3 → 9.1.1

> **Execution status:** Selected and frozen; transparent baseline complete; full contrast assessment pending.  
> **Artifact lifecycle:** Prospective run.  
> **Primary test:** Whether repository-specific evidence changes the baseline action.  
> **Ali review:** Pending.

## Frozen case

- Repository: `PennLINC/ModelArrayIO`
- Pull request: `#85`
- Base SHA: `915781a6c967f22b9236ecba072300932c2f41f0`
- Head SHA: `b590cfe93fbe49235f0f68d2b87102672f8a0aa0`
- Observed merge commit: `f7f58496507477c7ebaba40921859c18c771c1e4`
- Changed file: `uv.lock`
- Dependency: `pytest`
- Transition: `9.0.3` → `9.1.1`
- Run: `s005-20260723T123700Z-r1`

## Baseline result

Transparent baseline v0.1 selected:

> `run_targeted_checks`

The baseline used only minor-version category, passing overall CI, direct dependency status, and literal caution keywords from the release notes. It cannot interpret whether those breaking/deprecation signals apply to this repository or whether exact pytest 9.1.1 was exercised.

## Current next action

Map every material pytest 9.1 caution surface to the frozen repository, confirm exact lock-backed CI responsibility across the matrix, and determine whether any unresolved target risk still requires an additional check.