# S004 Case Record — glyphsLib pytest 9.0.2 → 9.0.3

## Final state

**Run:** `s004-20260722T224500Z-r1`  
**Mode:** prospective manual simulation  
**State:** complete at the justified early-stop point  
**Baseline/full relationship:** baseline sufficient; full investigation added no material decision value  
**Decision:** merge after normal maintainer review  
**Ali review:** pending

## Why this case was selected

S001–S003 all produced the same broad action as the transparent baseline while the full investigation added materially stronger support. S004 tested the opposite possibility: a real case where the baseline already gives adequate decision support and deeper work should stop.

Candidate screening is preserved in [`../../S004_CANDIDATE_SCREENING.md`](../../S004_CANDIDATE_SCREENING.md).

## Frozen event

Dependabot proposed changing one pinned development dependency in `googlefonts/glyphsLib`:

```text
pytest==9.0.2
→ pytest==9.0.3
```

Frozen identity:

- PR `#1145`;
- base `044f19e4b1437bfc4343592486f4e3c6040306d9`;
- head `f3cda8a94600e58d27f1bc17c99b7693718b6350`;
- changed file `requirements-dev.txt`;
- observed merge commit `a007710184f634557e6524b7e3b115bf74c91b73`.

The historical merge is an observed maintainer action, not correctness evidence.

## Starting invocation

The simulated system received only the public PR locator. Exact revision identity, changed-file content, dependency role, upstream information, and CI responsibility were acquired after the run began.

## Transparent baseline

Inputs frozen before full confirmation:

- version category: `patch`;
- current CI conclusion: `passing`;
- dependency directness: `direct`;
- caution keyword matches: none;
- favorable literal signals: `fixed`, `bug fix`, `CVE`.

Rule B05 selected:

> `merge_after_normal_review`

The baseline could not determine whether current CI installed pytest 9.0.3 or exercised pytest-owned responsibilities.

## Precommitted full-investigation question

> Did exact-head CI install `requirements-dev.txt` containing pytest 9.0.3 and then successfully run the repository's ordinary and regression pytest responsibilities?

The run committed to stop if the answer was yes, official upstream information presented the patch as a drop-in bug-fix release, and no contradictory or missing decision-critical evidence appeared.

## Evidence acquired

### Exact change and role

- the PR changed only `requirements-dev.txt`;
- the exact mutation was `pytest==9.0.2` to `pytest==9.0.3`;
- `requirements-dev.in` directly declares pytest;
- tox test environments install `requirements.txt` and `requirements-dev.txt`;
- ordinary test commands invoke `coverage run --parallel-mode -m pytest`.

### CI authority

The exact-head `Test + Deploy` workflow triggered on the pull request and passed:

- test jobs on Python 3.10 and 3.14;
- Ubuntu and Windows platforms;
- dependency-installation steps;
- tox-driven pytest execution;
- the lint job.

The exact-head `Regression Tests` workflow also passed. It:

1. generated known-good regression files from `main`;
2. checked out the proposed head without deleting those files;
3. created a new regression environment;
4. reinstalled `requirements.txt` and the changed `requirements-dev.txt`;
5. invoked pytest directly on the regression suite.

### Upstream authority

The official pytest 9.0.3 tagged release announcement describes the version as:

> a bug-fix release, being a drop-in replacement.

## Stop-condition result

All six precommitted conditions passed:

1. direct pinned development role confirmed;
2. exact-head PR workflows confirmed;
3. the changed requirements file was installed by the owning test paths;
4. ordinary and regression pytest responsibilities passed;
5. official drop-in bug-fix status confirmed;
6. no contradictory or missing decision-critical evidence appeared.

The investigation stopped at operation `op-007-stop-investigation`.

## Conditional work deliberately not activated

- advisory exploitability analysis;
- repository runtime-usage search;
- adapter or framework compatibility analysis;
- causal failure attribution;
- comparable-run environment analysis;
- local or container reproduction;
- targeted-check design;
- private evidence acquisition;
- platform/native/compiler analysis;
- post-merge publication analysis.

The CVE keyword in the release material did not activate exploitability analysis because the case question concerned a test-only development dependency, upstream declared a drop-in patch replacement, and relevant target tests already passed. No decision or uncertainty depended on target exploitability.

## Decision

> Merge after normal maintainer review.

No additional check is justified. A stronger claim of update safety is unsupported, while a weaker action would ignore complete relevant exact-head test evidence without an identified unresolved risk.

## Baseline comparison

Classifications:

- `baseline_sufficient`;
- `full_investigation_added_no_material_value`.

The full process added a narrow auditability improvement by confirming the authority of the overall green CI. It did not change:

- the action;
- the required checks;
- material uncertainty;
- the maintainer's next step.

## Cost and stopping lesson

S004 used six bounded evidence groups, seven accepted evidence records, and four full-confirmation operations after the baseline. It used no dynamic execution, private source, paid source, or added targeted check.

The product lesson is not “trust patch updates with green CI.” It is:

> Verify the baseline’s authority-critical assumptions with the smallest sufficient evidence set, then stop when no open question can change the bounded action.

## Follow-up and new-run rule

Ordinary maintainer review is the only current next action. A material change to the head, dependency set, requirements, workflow commands, check outcome, or primary upstream evidence requires a new run or explicit comparison.

## Ownership and limits

- AI performed candidate screening, acquisition, analysis, artifact construction, decision, reporting, and validation preparation.
- Ali authorized the work and remains responsible for acceptance.
- No independent Ali capability is inferred.
- No target repository was changed.
- This one control case does not establish a universal stopping threshold.
