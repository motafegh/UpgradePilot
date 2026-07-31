# B2 Step 7 — CI Dependency Exercise Migration Plan

**Status:** Approved and controlling for Step 7  
**Owner:** Ali Rajabi  
**Parent plan:** [`B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)  
**Architecture control:** [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)  
**Previous validated step:** [`../working-memory/2026-07-31_2031_B2-step-6-downstream-dependency-input-validation.md`](../working-memory/2026-07-31_2031_B2-step-6-downstream-dependency-input-validation.md)

## Purpose

Replace the legacy CI-authority vocabulary and module boundary:

```text
CIAuthorityResult
WorkflowAuthorityInput
WorkflowAuthorityAssessment
evaluate_ci_authority

sufficient
insufficient
unresolved
```

with the dependency-specific shared contract selected by ADR-0004:

```text
DependencyCIExerciseResult
WorkflowDependencyExerciseInput
WorkflowDependencyExerciseResult
evaluate_dependency_ci_exercise

proven
no_successful_ci
unresolved
```

while preserving the validated direct-requirements rule, the explicit CI-input split established in Step 6, package/target/upstream independence from CI state, and honest unresolved behavior.

Step 7 changes names and makes the state semantics exact. It does not add a new dependency-consumption rule and does not begin multi-format command integration.

## Owning question

> Can UpgradePilot represent exactly what current exact-head CI proves about dependency consumption and package exercise, using names and states whose meanings remain valid for requirements files, `uv.lock`, constraints, and later admitted source-specific rules?

## Why the legacy vocabulary must change

The current name:

```text
CI authority
```

is broader than the implemented evidence.

The evaluator does not establish authority over the whole pull request, release, repository, compatibility decision, or maintainer action. It answers one narrower question:

```text
Did one admitted successful exact-head CI path consume the changed dependency
and exercise the changed package under a supported deterministic rule?
```

The legacy state:

```text
insufficient
```

also combines several possible meanings. The new contract separates the only positive execution-absence state:

```text
no_successful_ci
```

from cases where successful CI exists but the dependency-exercise question remains unproven:

```text
unresolved
```

## Current validated input boundary

Step 6 established:

```text
DependencyVersionChange
+
WorkflowAuthorityInput[]
+
explicit direct_requirements_install_path: str | None
→ CIAuthorityResult
```

The dependency identity is canonical and format-independent. The direct-requirements path is explicit source-specific input for the current `pip -r` rule.

Step 7 must preserve that separation exactly. It must not inspect `DependencyFileEvidence.path` to invent installation evidence.

## Target public contract

### Shared state vocabulary

```python
DependencyCIExerciseState = Literal[
    "proven",
    "no_successful_ci",
    "unresolved",
]
```

Meanings:

### `proven`

One completed successful exact-head CI path satisfies one explicitly admitted dependency-consumption and package-exercise rule.

For the current direct-requirements rule, one statically readable successful job must visibly contain:

```text
pip install -r <explicit exact requirements path>
+
direct invocation of the changed package
```

This does not prove complete test coverage, compatibility, upgrade safety, or a merge recommendation.

### `no_successful_ci`

No completed successful exact-head job is available in the supplied evidence.

This state must not be used merely because:

- one workflow failed while another successful job exists;
- workflow definition text is unavailable;
- command interpretation is unsupported;
- no admitted dependency-consumption rule applies.

When any completed successful exact-head job exists, the overall result must be either `proven` or `unresolved`.

### `unresolved`

At least one completed successful exact-head job exists, but no admitted rule proves both dependency consumption and changed-package exercise.

Examples:

- exact workflow definition unavailable;
- workflow definition revision mismatch;
- workflow run-level state prevents a trusted path despite a successful job record;
- multiple statically visible jobs prevent same-environment proof;
- tox or another indirect command lacks configuration tracing;
- explicit direct-requirements install path is absent;
- constraints or `uv.lock` evidence has no selected consumption rule.

Unresolved is visible non-proof. It is not green evidence and does not erase dependency identity.

## Target records

### `WorkflowDependencyExerciseInput`

```text
run
jobs[]
definition
```

This remains one evidence bundle per exact-head workflow run.

### `WorkflowDependencyExerciseResult`

```text
workflow_name
workflow_path
state
reason
detail
install_command?
execution_command?
```

This preserves per-workflow transparency.

### `DependencyCIExerciseResult`

```text
state
reason
detail
workflows[]
```

This is the overall shared result consumed by the CLI and later decision work.

## Required decision order

### Per-workflow evaluation

For one workflow evidence bundle:

1. identify completed successful jobs;
2. if none exist, return `no_successful_ci`;
3. if a successful job exists but the workflow run is not completed-successful, return `unresolved`;
4. if exact workflow definition is unavailable, return `unresolved`;
5. if definition revision differs from the run head SHA, return `unresolved`;
6. if no explicit admitted direct-requirements path exists, return `unresolved`;
7. inspect the current direct install/invoke command rule;
8. supported commands return `proven`;
9. unsupported or incomplete commands return `unresolved`.

Execution absence precedes definition interpretation. An unavailable workflow file must not obscure the stronger fact that no completed successful job exists.

### Overall evaluation

1. no workflow inputs → `no_successful_ci`;
2. evaluate every supplied workflow;
3. any per-workflow `proven` result → overall `proven`;
4. no completed successful exact-head job anywhere → overall `no_successful_ci`;
5. otherwise → overall `unresolved`.

A proven workflow does not erase unresolved or no-successful-CI workflow records; all per-workflow results remain attached.

## Stable reason vocabulary

Step 7 changes state names and public record names. Existing precise reasons may remain when their meanings are still correct.

Overall reasons:

```text
exact_head_dependency_exercised
no_exact_head_workflows
no_successful_exact_head_jobs
dependency_exercise_not_proven
```

Per-workflow reasons:

```text
source_installed_and_dependency_invoked
no_successful_jobs
workflow_not_successful
workflow_definition_unavailable
workflow_definition_revision_mismatch
direct_requirements_install_path_unavailable
workflow_jobs_not_statically_readable
multiple_or_zero_workflow_jobs
direct_dependency_exercise_not_proven
```

Do not rename stable reasons only for stylistic consistency. Rename only when the existing reason would misstate the new semantics.

## Source migration

### Create `src/upgradepilot/ci_dependency_exercise.py`

Implement and document:

```text
DependencyCIExerciseState
WorkflowDependencyExerciseInput
WorkflowDependencyExerciseResult
DependencyCIExerciseResult
evaluate_dependency_ci_exercise
```

The new module owns the runtime behavior.

### Retire `src/upgradepilot/ci_authority.py`

After all runtime and controlled tests use the new module, remove the legacy module rather than keeping misleading aliases whose states changed meaning.

Historical learning, planning, and validation records are not mass-renamed.

### Update `src/upgradepilot/cli.py`

Replace runtime imports, type names, variable names, function call, and presentation labels.

Required labels:

```text
CI dependency exercise: <state>
CI dependency exercise reason: <reason>
CI dependency exercise detail: <detail>
```

Per-workflow presentation:

```text
Dependency exercise workflow: <name> | state=<state> | reason=<reason>
```

Unsupported dependency identity must print:

```text
CI dependency exercise: not evaluated
```

Do not retain `CI authority` as an active CLI label after migration.

### Update `src/upgradepilot/__init__.py`

Expose the shared public contracts:

```text
DependencyCIExerciseState
WorkflowDependencyExerciseInput
WorkflowDependencyExerciseResult
DependencyCIExerciseResult
evaluate_dependency_ci_exercise
```

No legacy CI-authority names are currently package-level exports, so no package-level compatibility alias is required.

### `src/upgradepilot/workflow_commands.py`

Expected unchanged.

It remains a narrow command-inspection helper returning supported/unresolved command evidence. It does not own overall CI exercise states.

## Test migration

### Replace the legacy CI test module

Create:

```text
tests/test_ci_dependency_exercise.py
```

Remove:

```text
tests/test_ci_authority.py
```

Required controlled tests:

1. explicit direct-requirements path plus direct package invocation → `proven`;
2. no workflow inputs → `no_successful_ci`;
3. no completed successful job → `no_successful_ci`;
4. unavailable definition with no successful job still → `no_successful_ci`;
5. successful job plus unavailable definition → `unresolved`;
6. successful job plus run-level non-success → `unresolved`;
7. successful tox path without trace → `unresolved`;
8. several workflow jobs → `unresolved`;
9. missing explicit direct-requirements path → `unresolved`;
10. `uv.lock` and constraints evidence paths are never promoted into install proof;
11. a proven workflow wins overall while all workflow results remain preserved.

### Update CLI tests

Prove:

- CLI calls `evaluate_dependency_ci_exercise`;
- the evaluator receives canonical identity and explicit path separately;
- `proven`, `no_successful_ci`, and `unresolved` labels render exactly;
- legacy `CI authority` labels are absent;
- unsupported dependency identity skips CI exercise evaluation;
- package, upstream, and target stages still proceed independently of an unresolved CI exercise result;
- S004 material identity and downstream evidence remain unchanged.

### Package boundary test

Add or extend a focused package-interface test when needed to prove the new shared contracts are exported and legacy CI-authority names are not added to `__all__`.

## Legacy containment

After Step 7 source migration, active product and controlled test code must not import or reference:

```text
CIAuthorityResult
CIAuthorityStatus
WorkflowAuthorityInput
WorkflowAuthorityAssessment
evaluate_ci_authority
CI authority:
```

Historical documents may retain those names as historical truth.

## Scope not included

Step 7 must not implement:

- normal CLI recognition or exact-file acquisition for `uv.lock`;
- PR-wide multi-format dependency coordination;
- `uv sync`, `uv run`, or constraints consumption rules;
- broader YAML, shell, reusable-workflow, action, tox, nox, or task-runner interpretation;
- PEP 440 ordering;
- Python-support relevance;
- compatibility, safety, recommendation, or maintainer action;
- a dynamic plugin framework.

## Build order

1. commit this focused plan;
2. create new Step 7 tests before runtime source;
3. create `ci_dependency_exercise.py`;
4. migrate CLI imports, orchestration, and labels;
5. expose shared contracts in `__init__.py`;
6. remove legacy source and test modules;
7. audit active source/tests for legacy names;
8. review the complete diff against the stop line;
9. record implementation and update `MEMORY.md` as unvalidated;
10. run focused tests, complete deterministic suite, and installed anonymous S004;
11. record validation and authorize Step 8 only after observed proof.

## Expected validation

Focused command:

```bash
python -m unittest \
  tests.test_ci_dependency_exercise \
  tests.test_cli \
  -v
```

The exact focused test count must be derived from the final committed tests and recorded as expected, not guessed before implementation closes.

Complete command:

```bash
python -m unittest discover -s tests -v
```

Installed public regression:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Required S004 material behavior remains:

```text
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

The active output must not include:

```text
CI authority:
```

## Rejection and reframing conditions

Stop and reframe if:

- `no_successful_ci` would be used while a completed successful exact-head job exists;
- `unresolved` is presented as sufficient, proven, green, or safe;
- preserving S004 requires repository-, package-, or PR-specific conditions;
- the migration begins inferring generic evidence paths as installation proof;
- new source-specific consumption rules are added without a selected case and focused plan;
- package, upstream, or target acquisition is made conditional on `proven` CI;
- compatibility aliases obscure the changed state semantics;
- work expands into Step 8 orchestration.

## Step 7 stop line

Stop Step 7 when:

```text
DependencyCIExerciseResult is the active shared overall contract
+
WorkflowDependencyExerciseResult preserves per-workflow evidence
+
proven / no_successful_ci / unresolved have exact implemented meanings
+
no generic dependency evidence path becomes installation proof
+
the direct-requirements S004 rule remains intact
+
CLI uses CI dependency exercise labels
+
legacy active CI-authority names are retired
+
package, target, and upstream stages remain independent of unresolved CI
+
complete deterministic suite passes
+
installed anonymous S004 passes
```

Step 7 does not establish one-line S001 behavior or any new CI-consumption rule.

## Exact continuation after implementation

After source and tests are committed, record the implementation as unvalidated. Supply the focused test command, complete-suite command, and installed S004 command. Do not authorize Step 8 until those outputs are observed and recorded.
