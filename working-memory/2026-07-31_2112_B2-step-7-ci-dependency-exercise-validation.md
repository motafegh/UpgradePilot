# B2 Step 7 — CI dependency exercise validation

**Recorded:** 2026-07-31 21:12 +03:30  
**Route:** B2 — Public PR vertical slice  
**Step:** 7 — Migrate CI result names and semantics  
**Status:** Complete and behavior-validated

## Controlling authority

- Parent plan: [`../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- Focused Step 7 plan: [`../plans/B2_STEP_7_CI_DEPENDENCY_EXERCISE_MIGRATION_PLAN.md`](../plans/B2_STEP_7_CI_DEPENDENCY_EXERCISE_MIGRATION_PLAN.md)
- Architecture: [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- Implementation record: [`2026-07-31_2041_B2-step-7-ci-dependency-exercise-implementation.md`](2026-07-31_2041_B2-step-7-ci-dependency-exercise-implementation.md)

## Validated repository boundary

The local checkout was updated from:

```text
f7457fd
```

to the current implementation-record state:

```text
9c980b3
```

The Step 7 product/test implementation within that history is:

```text
93f93dd2da10bc98cf1b14363f2164eefbee75c1
```

Later implementation-record and memory commits did not alter the Step 7 product/test source.

## Deterministic suite

Observed user-supplied result:

```text
----------------------------------------------------------------------
Ran 138 tests in 0.033s

OK
```

This establishes that the complete deterministic repository suite passed after the Step 7 migration.

The transcript did not visibly contain a separate `Ran 20 tests` focused-suite summary. The focused Step 7 tests are included in the complete 138-test discovery run, but an independent focused invocation is not claimed.

## Installed anonymous S004 regression

Observed command:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

The installed public command preserved the validated S004 dependency, target, package, provenance, and upstream evidence chain:

```text
Repository: googlefonts/glyphsLib
PR: 1145
Changed file: requirements-dev.txt (modified)
Package: pytest
Old version: 9.0.2
Proposed version: 9.0.3
Target Python declaration: project_table_absent
Exact-head workflow runs: 2
Published package: pytest==9.0.3
Distribution files: 2
Upstream repository: pytest-dev/pytest
Provenance coverage: 2 of 2 files
Accepted tag: 9.0.3
Tag object SHA: 24ec4b54c06a74721a285dcc317825b1735f4717
Claim state: unresolved_claim
```

## Validated Step 7 CI exercise behavior

The active command produced:

```text
CI dependency exercise: proven
CI dependency exercise reason: exact_head_dependency_exercised
CI dependency exercise detail: Workflow 'Regression Tests' installed 'requirements-dev.txt' and directly invoked 'pytest' in successful exact-head CI.
```

The proving workflow remained:

```text
Regression Tests
state=proven
reason=source_installed_and_dependency_invoked
```

with visible installation and execution evidence.

The multi-job workflow remained transparent non-proof:

```text
Test + Deploy
state=unresolved
reason=multiple_or_zero_workflow_jobs
```

This validates the intended existential overall rule: one admitted proven workflow establishes overall `proven`, while unresolved workflow results remain preserved rather than erased.

The active output did not contain the former label:

```text
CI authority:
```

## Step 7 stop-line result

Validated:

```text
DependencyCIExerciseResult is active
+
proven / no_successful_ci / unresolved are the active shared states
+
no_successful_ci is reserved for absence of completed successful exact-head jobs
+
successful-but-unproven CI remains unresolved
+
the direct-requirements proving rule remains intact
+
generic dependency evidence paths are not installation proof
+
package, upstream, and target evidence remain independent of CI state
+
legacy CI-authority module and tests are retired
+
complete deterministic suite passes
+
installed anonymous S004 passes with new labels
```

Step 7 is therefore complete and behavior-validated.

## What Step 7 established

Active shared contracts:

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

The current proving rule remains deliberately narrow:

```text
explicit direct_requirements_install_path
+
visible pip install -r <that path>
+
direct changed-package invocation
+
completed successful exact-head workflow/job evidence
```

No broader workflow, shell, tox, nox, reusable-workflow, constraints, or `uv.lock` consumption interpretation was introduced.

## What Step 7 did not establish

This validation does not establish:

- one-line installed S001 behavior;
- normal CLI recognition or exact-file acquisition for `uv.lock`;
- PR-wide multi-format dependency coordination during command execution;
- `uv.lock`, constraints, or another new CI-consumption rule;
- PEP 440 ordering;
- Python-support relevance;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery.

## Next bounded step

Step 8 is now authorized:

```text
integrate the multi-format dependency command path
```

Step 8 must connect admitted exact-requirements/constraints and `uv.lock` extraction through the shared comparator, then feed the established canonical downstream and CI-exercise contracts.

The intended installed command outcome is:

```bash
upgradepilot pydantic/pydantic 13432
```

using the real `uv.lock` acquisition and extraction path rather than a temporary developer script.

Step 8 must preserve S004 and must not invent `uv.lock` CI-consumption proof. For S001, dependency identity may be established while CI dependency exercise remains `unresolved` unless a separately admitted rule proves consumption and exercise.
