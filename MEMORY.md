# UpgradePilot Current Memory

**Last updated:** 2026-07-31 21:12 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable plans, ADRs, source, tests, and dated evidence retain their own responsibilities. This file records only the current state needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Parent plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Step 7 plan:** [`plans/B2_STEP_7_CI_DEPENDENCY_EXERCISE_MIGRATION_PLAN.md`](plans/B2_STEP_7_CI_DEPENDENCY_EXERCISE_MIGRATION_PLAN.md)
- **Accepted architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Step 6 validation:** [`working-memory/2026-07-31_2031_B2-step-6-downstream-dependency-input-validation.md`](working-memory/2026-07-31_2031_B2-step-6-downstream-dependency-input-validation.md)
- **Step 7 implementation:** [`working-memory/2026-07-31_2041_B2-step-7-ci-dependency-exercise-implementation.md`](working-memory/2026-07-31_2041_B2-step-7-ci-dependency-exercise-implementation.md)
- **Step 7 validation:** [`working-memory/2026-07-31_2112_B2-step-7-ci-dependency-exercise-validation.md`](working-memory/2026-07-31_2112_B2-step-7-ci-dependency-exercise-validation.md)
- **Behavior-validated Step 7 product/test revision:** `93f93dd2da10bc98cf1b14363f2164eefbee75c1`.
- **Step 7 validation-record revision:** `a7f73ad575c7a8f6d8593a284de2a5348f123f2a`.

The user updated local `main` from `f7457fd` to `9c980b3`, then ran the complete suite and installed S004 command. Later validation and memory commits do not alter the Step 7 product/test revision.

## Current phase

Steps 1–7 are complete and behavior-validated.

Step 8 is now the next bounded plan step:

```text
integrate the multi-format dependency command path
```

Step 8 is the integration step that should make the real installed command:

```bash
upgradepilot pydantic/pydantic 13432
```

use `uv.lock` acquisition, extraction, PR-wide comparison, canonical downstream identity, and the shared CI dependency-exercise contract.

## Step 7 validated boundary

### Deterministic execution

Observed complete-suite result:

```text
Ran 138 tests in 0.033s
OK
```

A separate focused `Ran 20 tests` summary was not visible in the supplied transcript. The focused Step 7 tests are included in the complete discovery run; an independent focused invocation is not claimed.

### Installed anonymous S004 regression

Observed command:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Preserved material behavior:

```text
requirements-dev.txt
pytest 9.0.2 → 9.0.3
project_table_absent
2 exact-head workflow runs
published pytest==9.0.3
2 of 2 provenance
pytest-dev/pytest release tag 9.0.3
unresolved_claim
```

Validated Step 7 behavior:

```text
CI dependency exercise: proven
CI dependency exercise reason: exact_head_dependency_exercised
```

The `Regression Tests` workflow remained proven through visible installation of `requirements-dev.txt` and direct invocation of `pytest`.

The multi-job `Test + Deploy` workflow remained:

```text
state=unresolved
reason=multiple_or_zero_workflow_jobs
```

The former active label `CI authority:` was absent.

## What Step 7 established

### Shared CI dependency-exercise contracts

```text
DependencyCIExerciseState
WorkflowDependencyExerciseInput
WorkflowDependencyExerciseResult
DependencyCIExerciseResult
evaluate_dependency_ci_exercise
```

Active states:

```text
proven
no_successful_ci
unresolved
```

Exact meanings:

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

### Corrected decision order

Per workflow:

```text
completed successful jobs?
├── none → no_successful_ci
└── present
    ├── workflow run not completed-successful → unresolved
    ├── definition unavailable or mismatched → unresolved
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

no completed successful job anywhere
→ no_successful_ci

otherwise
→ unresolved
```

`no_successful_ci` is never used when a completed successful exact-head job exists.

### Preserved direct-requirements rule

The evaluator receives:

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

`DependencyFileEvidence.path` is not automatic installation proof.

`uv.lock` and constraints still have no admitted CI-consumption rule.

### Active source and interface

Created and validated:

```text
src/upgradepilot/ci_dependency_exercise.py
```

Retired:

```text
src/upgradepilot/ci_authority.py
tests/test_ci_authority.py
```

The package-level `upgradepilot` interface exports the new shared contracts.

## Step 8 responsibility

Step 8 must replace the temporary command ingress:

```text
ChangedFile[]
→ legacy exact-requirements extractor
→ LegacyDependencyIngress
```

with one explicit multi-format dependency-analysis coordinator.

Required command flow:

```text
complete changed-file records
        │
        ├── admitted exact requirements / constraints
        │     └── patch-based extraction
        │
        └── admitted modified uv.lock
              └── exact base/head acquisition and extraction
                         │
                         ▼
        compare_extracted_dependency_changes
                         │
            ┌────────────┴────────────┐
            ▼                         ▼
DependencyVersionChange   DependencyChangeEvidenceProblem
            │
            ├── target-Python acquisition
            ├── package evidence
            ├── upstream evidence
            ├── generic dependency presentation
            └── CI dependency exercise
```

### Required S001 result

The installed command should establish:

```text
pydantic/pydantic #13432
uv.lock
soupsieve 2.6 → 2.8.4
```

with the exact validated source provenance:

```text
base revision: 652a61ce4f9d7d76eaada31535807a485ece0e21
base blob: b4a68ab725de337889d50d5374ac0f05db7fb484
base bytes: 606307

head revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
head blob: def33fe05d78ab851ce91a33db5bc55a439873a1
head bytes: 606313
```

### Required CI behavior for S001

Step 8 must not infer `uv.lock` consumption from the evidence path.

Unless a separately admitted rule proves dependency consumption and exercise, S001 should remain:

```text
CI dependency exercise: unresolved
```

while dependency, target, package, and upstream evidence continue independently.

### Required S004 preservation

The installed command:

```bash
upgradepilot googlefonts/glyphsLib 1145
```

must preserve:

```text
pytest 9.0.2 → 9.0.3
requirements-dev.txt evidence
CI dependency exercise: proven
package and upstream evidence
```

## Exact continuation

Before Step 8 source changes:

1. inspect current command ingress, exact-requirement extractor, `uv.lock` extractor, repository base/head acquisition, shared comparator, CLI presentation, and all associated tests;
2. compare the parent Step 8 entry against the real integration surface;
3. create a focused Step 8 execution plan when the parent entry is too terse to control orchestration, stopping behavior, and validation;
4. freeze tests before runtime changes for:
   - mixed source discovery;
   - exact-file acquisition only for admitted `uv.lock`;
   - PR-wide comparison;
   - recognized evidence problems stopping downstream work;
   - S001 integrated output and exact provenance;
   - S001 unresolved CI exercise without path inference;
   - S004 preservation;
   - generic future-format extension boundary;
5. implement the coordinator and CLI integration without adding new CI-consumption semantics or unrelated version/compatibility logic;
6. run focused tests, complete suite, installed S004, and installed S001 before closing Step 8.

## Not established

- Step 8 multi-format command integration;
- one-line installed S001 behavior;
- normal CLI `uv.lock` recognition and exact-file acquisition;
- PR-wide multi-format comparison during command execution;
- `uv.lock`, constraints, or another new CI-consumption rule;
- PEP 440 semantics;
- Python-support relevance;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery.

## Learning state

Step 7 concepts introduced, implemented, and behavior-validated:

- domain-specific naming versus overly broad naming;
- mutually exclusive evidence states;
- precedence rules in evidence classification;
- execution absence versus interpretation uncertainty;
- per-workflow evidence versus overall existential proof;
- package identity versus source-specific CI operational evidence;
- active API migration and deliberate legacy retirement.

Current depth:

```text
structured explanation completed
+ focused plan created
+ tests written before source
+ source and CLI migration implemented
+ package interface migrated
+ legacy active code retired
+ complete deterministic suite observed
+ installed S004 regression observed
but
no user-owned technical explanation recorded
no independent implementation practice recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
