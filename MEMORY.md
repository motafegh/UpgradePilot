# UpgradePilot Current Memory

**Last updated:** 2026-07-31 20:41 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable plans, ADRs, source, tests, and dated evidence retain their own responsibilities. This file records only the current state needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Parent plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Step 7 controlling plan:** [`plans/B2_STEP_7_CI_DEPENDENCY_EXERCISE_MIGRATION_PLAN.md`](plans/B2_STEP_7_CI_DEPENDENCY_EXERCISE_MIGRATION_PLAN.md)
- **Accepted architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Step 6 validation:** [`working-memory/2026-07-31_2031_B2-step-6-downstream-dependency-input-validation.md`](working-memory/2026-07-31_2031_B2-step-6-downstream-dependency-input-validation.md)
- **Step 7 implementation:** [`working-memory/2026-07-31_2041_B2-step-7-ci-dependency-exercise-implementation.md`](working-memory/2026-07-31_2041_B2-step-7-ci-dependency-exercise-implementation.md)
- **Behavior-validated Step 6 product/test revision:** `885d8aab5a3cfd187bf3fce179aabcbfccebeaac`.
- **Latest Step 7 product/test implementation revision:** `93f93dd2da10bc98cf1b14363f2164eefbee75c1`.
- **Step 7 implementation-record revision:** `54011e8e93fac9306732a6dd6cb1eaa08b5b8466`.

Later evidence or memory commits do not alter the Step 7 product/test implementation revision.

## Current phase

Steps 1–6 are complete and behavior-validated.

Step 7 is fully implemented in source and controlled tests but remains **open and unvalidated**:

```text
migrate CI result names and semantics
```

Do not begin Step 8 multi-format command integration before Step 7 validation is complete.

## Step 7 implemented boundary

### Shared module and public contracts

Created:

```text
src/upgradepilot/ci_dependency_exercise.py
```

Active public contracts:

```text
DependencyCIExerciseState
WorkflowDependencyExerciseInput
WorkflowDependencyExerciseResult
DependencyCIExerciseResult
evaluate_dependency_ci_exercise
```

The package-level interface exports these names.

### Exact state meanings

```text
proven
→ one completed successful exact-head path satisfies an explicitly admitted
  dependency-consumption and package-exercise rule

no_successful_ci
→ no completed successful exact-head job is available

unresolved
→ at least one completed successful exact-head job exists, but no admitted
  rule proves dependency consumption and package exercise
```

`unresolved` is visible non-proof. It is not green evidence, compatibility evidence, safety evidence, or a recommendation.

### Corrected evaluation order

Per workflow:

```text
completed successful jobs?
├── none → no_successful_ci
└── present
    ├── workflow run not completed-successful → unresolved
    ├── exact definition unavailable or mismatched → unresolved
    ├── explicit requirements path absent → unresolved
    ├── command rule unsupported or incomplete → unresolved
    └── direct install + direct invoke rule satisfied → proven
```

Overall:

```text
no workflow inputs
→ no_successful_ci

any proven workflow
→ proven

no successful job anywhere
→ no_successful_ci

otherwise
→ unresolved
```

This ensures `no_successful_ci` is never used when a completed successful exact-head job exists.

### Preserved direct-requirements rule

The evaluator still requires:

```text
DependencyVersionChange
+ WorkflowDependencyExerciseInput[]
+ keyword-only direct_requirements_install_path: str | None
```

The current proving rule remains:

```text
visible pip install -r <explicit exact requirements path>
+
direct changed-package invocation
+
completed successful exact-head run and job evidence
```

`DependencyFileEvidence.path` is never selected automatically as installation proof.

Controlled tests preserve negative cases for:

```text
uv.lock
constraints/base.txt
```

Neither has an admitted consumption rule in Step 7.

### CLI migration

Active labels:

```text
CI dependency exercise: <state>
CI dependency exercise reason: <reason>
CI dependency exercise detail: <detail>
```

Per-workflow label:

```text
Dependency exercise workflow: <name> | state=<state> | reason=<reason>
```

Unsupported dependency identity reports:

```text
CI dependency exercise: not evaluated
```

The active CLI no longer uses the broader `CI authority` vocabulary.

Package, upstream, and target acquisition remain independent of `proven`, `no_successful_ci`, or `unresolved` CI state.

### Retired active legacy code

Removed:

```text
src/upgradepilot/ci_authority.py
tests/test_ci_authority.py
```

Historical documents retain old names where they describe earlier implemented truth.

## Step 7 changed files

Added:

```text
plans/B2_STEP_7_CI_DEPENDENCY_EXERCISE_MIGRATION_PLAN.md
src/upgradepilot/ci_dependency_exercise.py
tests/test_ci_dependency_exercise.py
tests/test_package_interface.py
working-memory/2026-07-31_2041_B2-step-7-ci-dependency-exercise-implementation.md
```

Modified:

```text
src/upgradepilot/cli.py
src/upgradepilot/__init__.py
tests/test_cli.py
```

Removed:

```text
src/upgradepilot/ci_authority.py
tests/test_ci_authority.py
```

`src/upgradepilot/workflow_commands.py` was intentionally not broadened. It remains the current narrow direct-command reader.

## Controlled test boundary

Step 7 focused tests:

```text
tests/test_ci_dependency_exercise.py: 11
tests/test_cli.py: 8
tests/test_package_interface.py: 1
```

Expected focused total:

```text
20 tests
```

Expected complete deterministic total:

```text
138 tests
```

These counts are derived from committed test methods. They are not observed passing results yet.

## Validation status

No Step 7 repository test pass or live S004 pass is claimed.

The GitHub connector exposes no repository test runner. The available container could not resolve `github.com`, so it could not clone and execute the committed repository.

## Exact continuation

From the real checkout:

```bash
git switch main
git pull --ff-only
```

Run focused Step 7 tests:

```bash
python -m unittest \
  tests.test_ci_dependency_exercise \
  tests.test_cli \
  tests.test_package_interface \
  -v
```

Expected:

```text
Ran 20 tests
OK
```

Run the complete suite:

```bash
python -m unittest discover -s tests -v
```

Expected:

```text
Ran 138 tests
OK
```

Run installed anonymous S004:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Required material behavior remains:

```text
requirements-dev.txt
pytest 9.0.2 → 9.0.3
project_table_absent
published pytest==9.0.3
2 of 2 provenance
pytest-dev/pytest release tag 9.0.3
unresolved_claim
```

Required Step 7 presentation:

```text
CI dependency exercise: proven
CI dependency exercise reason: exact_head_dependency_exercised
```

The output must not include:

```text
CI authority:
```

After all three proofs are supplied, create a dated Step 7 validation record, close Step 7 in this memory, and only then authorize Step 8.

## Not established

- Step 7 focused-suite pass;
- Step 7 complete-suite pass;
- post-migration installed S004 behavior;
- one-line installed S001 behavior;
- normal CLI `uv.lock` recognition or exact-file acquisition;
- PR-wide multi-format command coordination;
- `uv.lock`, constraints, or another new CI-consumption rule;
- PEP 440 semantics;
- Python-support relevance;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery.

## Learning state

Step 7 concepts introduced and implemented:

- domain-specific naming versus overly broad naming;
- mutually exclusive evidence states;
- precedence rules in evidence classification;
- difference between execution absence and interpretation uncertainty;
- per-workflow evidence versus overall existential proof;
- active API migration and deliberate legacy retirement.

Current depth:

```text
structured explanation completed
+ focused plan created
+ tests written before source
+ source and CLI migration implemented
+ package interface migrated
+ legacy active code retired
+ implementation diff reviewed
but
repository execution not yet observed
no user-owned technical explanation recorded
no independent implementation practice recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
