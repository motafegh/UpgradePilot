# S005 Case Record — ModelArrayIO pytest 9.0.3 → 9.1.1

## Final state

**Run:** `s005-20260723T123700Z-r1`  
**Mode:** prospective manual simulation  
**State:** complete at action-changing stop; degraded structural validation pending/finalizing  
**Baseline:** `run_targeted_checks`  
**Full action:** `merge_after_normal_review`  
**Classification:** `baseline_wrong_action`

## Why this case was selected

S001–S003 showed the same broad action with stronger support. S004 showed the baseline could be sufficient. S005 tests the missing class: repository-specific evidence changes the broad action.

Candidate screening is preserved in [`../../S005_CANDIDATE_SCREENING.md`](../../S005_CANDIDATE_SCREENING.md).

## Frozen event

Dependabot proposed changing pytest 9.0.3 → 9.1.1 in `PennLINC/ModelArrayIO` PR #85.

- base: `915781a6c967f22b9236ecba072300932c2f41f0`;
- head: `b590cfe93fbe49235f0f68d2b87102672f8a0aa0`;
- changed file: `uv.lock` only;
- observed merge commit: `f7f58496507477c7ebaba40921859c18c771c1e4`.

The observed merge is action history, not correctness evidence.

## Transparent baseline

Restricted inputs:

- minor update;
- passing CI;
- direct dependency;
- literal `breaking`, `removals`, `deprecations`, and `deprecated` signals.

Rule B04 selected:

> `run_targeted_checks`

This was coherent under the baseline's deliberate blindness, but wrong for the frozen target.

## Exact dependency and CI path

Pytest is a direct `test` extra. The PR changes only pytest in `uv.lock`. The tox `latest` environments use `uv-venv-lock-runner`, then execute pytest.

Exact-head results:

- Python 3.11 latest: passed;
- Python 3.12 latest: passed, including downloaded-data tests;
- Python 3.13 latest: passed;
- Python 3.14 latest: passed;
- Python 3.11 minimum-dependency comparison: passed.

The minimum environment is robustness evidence, not proof of pytest 9.1.1 identity. The four latest jobs are exact-lock evidence.

## Upstream caution mapping

The official pytest 9.1.1 tagged changelog identifies one breaking behavior: with `--doctest-modules`, inline autouse fixtures at module/package/session scope may execute twice.

ModelArrayIO does not use `--doctest-modules`, so that behavior is inactive.

The frozen repository was also checked for:

- class-scoped fixture instance methods;
- teardown-time `request.getfixturevalue()`;
- non-Collection parametrization values;
- `config.inicfg`;
- private `FixtureDef` registration/location APIs;
- hook configuration markers;
- `--pastebin`;
- `pytest.console_main`;
- `yield_fixture`.

No deprecated direct surface was found. Every discovered parametrization site uses concrete list or tuple values. A comparison to the later default branch changed no source or tests, so current indexed negative searches do not conceal a frozen-head use deleted afterward.

## Decision

No remaining target-specific pytest 9.1 question identifies an additional check with decision value. Therefore the full action is:

> `merge_after_normal_review`

This supersedes the baseline action for this frozen case only.

## Limits

- network S3 tests were excluded;
- external pytest plugin internals were not independently audited;
- negative source search is bounded;
- passing CI and this recommendation do not prove update safety.

These limitations do not identify a relevant pytest 9.1 check and therefore do not retain the baseline's extra gate.

## Artifact behavior

`CHECK_EXECUTIONS.jsonl` activated naturally because exact lock-backed matrix relationships were material. `FAILURE_ATTRIBUTION.json` did not activate because there was no failing or conflicting execution. Separate dependency-versus-PR decision dimensions were unnecessary because both assessments support normal review.

## Transitions

Create a new run if the head, lock, tox runner, workflow command, test selection, or repository usage changes, or if new evidence identifies a relevant warning or failure.

No target repository mutation was performed. Ali review remains pending; AI-produced completion does not establish Ali-owned capability.