# B2 Step 7 — CI dependency exercise implementation

**Recorded:** 2026-07-31 20:41 +03:30  
**Route:** B2 — Public PR vertical slice  
**Step:** 7 — Migrate CI result names and semantics  
**Status:** Implemented; repository validation required

## Controlling authority

- Parent plan: [`../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- Focused Step 7 plan: [`../plans/B2_STEP_7_CI_DEPENDENCY_EXERCISE_MIGRATION_PLAN.md`](../plans/B2_STEP_7_CI_DEPENDENCY_EXERCISE_MIGRATION_PLAN.md)
- Architecture: [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- Previous validation: [`2026-07-31_2031_B2-step-6-downstream-dependency-input-validation.md`](2026-07-31_2031_B2-step-6-downstream-dependency-input-validation.md)

## Implemented revision boundary

Step 6 validated state before Step 7:

```text
f7457fdc2ec983cd5972ecf48f546f3e1c5bbc5a
```

Latest Step 7 product/test implementation revision:

```text
93f93dd2da10bc98cf1b14363f2164eefbee75c1
```

No Step 8 multi-format command integration was implemented.

## Commits

Plan:

```text
791cc82eb909ef33f96665c330eef3a9e6f915fb
Finalize Step 7 CI exercise migration plan
```

Tests first:

```text
1fb829e8bdb07f199ac50c7ed0a3a23703c6b763
Test Step 7 CI exercise semantics

60e81a9b1ecb00173ad6ae5e95bf51d4b95d4d03
Test Step 7 CLI exercise presentation

a7b4594201cdb37dd5e9ff3f14dbfb891b4aa442
Test Step 7 package exports
```

Runtime source:

```text
ebaf446ca461220385f3c4156c16b20a774609aa
Add shared CI dependency exercise contract

b39820400be132924f238fcc0702e98c3a226abb
Migrate CLI to CI dependency exercise

46cf061d2da8dd18be6c71d5b1a9be51462409f1
Export CI dependency exercise contracts

e34ac99df1fb76a82822071e378d39880626766c
Retire legacy CI authority module

93f93dd2da10bc98cf1b14363f2164eefbee75c1
Retire legacy CI authority tests
```

## Implemented shared contract

Created:

```text
src/upgradepilot/ci_dependency_exercise.py
```

Public contracts:

```text
DependencyCIExerciseState
WorkflowDependencyExerciseInput
WorkflowDependencyExerciseResult
DependencyCIExerciseResult
evaluate_dependency_ci_exercise
```

Shared states:

```text
proven
no_successful_ci
unresolved
```

### `proven`

One completed successful exact-head CI path satisfies the currently admitted direct-requirements consumption and changed-package exercise rule.

The current rule still requires:

```text
explicit direct_requirements_install_path
+
visible pip install -r <that exact path>
+
direct changed-package invocation
+
completed successful exact-head workflow and job evidence
```

The state does not mean complete coverage, compatibility, safety, or a recommendation.

### `no_successful_ci`

No completed successful exact-head job is available.

Implemented overall cases:

```text
no workflow inputs
→ no_successful_ci / no_exact_head_workflows

workflow inputs but no completed successful job anywhere
→ no_successful_ci / no_successful_exact_head_jobs
```

Per-workflow execution absence is represented as:

```text
no_successful_ci / no_successful_jobs
```

### `unresolved`

At least one completed successful exact-head job exists, but no admitted rule proves dependency consumption and package exercise.

Implemented unresolved boundaries include:

- successful job with non-successful workflow run;
- unavailable exact workflow definition;
- workflow-definition revision mismatch;
- missing explicit direct-requirements path;
- several statically visible workflow jobs;
- tox or another indirect execution path without configuration tracing;
- visible commands that do not prove both installation and direct invocation.

## Corrected decision order

Per workflow:

```text
completed successful jobs?
├── none → no_successful_ci
└── present
    ├── workflow run not completed-successful → unresolved
    ├── definition unavailable/mismatched → unresolved
    ├── explicit requirements path absent → unresolved
    ├── command rule unsupported/incomplete → unresolved
    └── direct install + invoke rule satisfied → proven
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

This prevents the former broad `insufficient` label from hiding whether successful CI exists.

## Preserved Step 6 input split

The evaluator receives:

```text
DependencyVersionChange
+ WorkflowDependencyExerciseInput[]
+ keyword-only direct_requirements_install_path: str | None
```

The canonical dependency record supplies package identity only.

The explicit path remains separate source-specific operational evidence for the current direct-requirements rule.

The evaluator does not inspect or select:

```text
DependencyFileEvidence.path
```

as installation proof.

Controlled tests retain tempting negative cases:

```text
uv.lock
constraints/base.txt
```

Neither path can prove consumption without a separately admitted rule.

## CLI migration

Active labels now are:

```text
CI dependency exercise: <state>
CI dependency exercise reason: <reason>
CI dependency exercise detail: <detail>
```

Per-workflow output:

```text
Dependency exercise workflow: <name> | state=<state> | reason=<reason>
```

Unsupported dependency identity now reports:

```text
CI dependency exercise: not evaluated
```

The active CLI no longer imports or prints the broader `CI authority` vocabulary.

Package, upstream, and target evidence continue independently when CI exercise is `unresolved` or `no_successful_ci`.

## Package interface

`src/upgradepilot/__init__.py` now exports:

```text
DependencyCIExerciseResult
DependencyCIExerciseState
WorkflowDependencyExerciseInput
WorkflowDependencyExerciseResult
evaluate_dependency_ci_exercise
```

No legacy CI-authority contracts are exported.

## Retired active legacy code

Removed:

```text
src/upgradepilot/ci_authority.py
tests/test_ci_authority.py
```

Historical plans, learning records, and validation documents retain old names where they describe historical truth.

## Changed files

```text
plans/B2_STEP_7_CI_DEPENDENCY_EXERCISE_MIGRATION_PLAN.md
src/upgradepilot/ci_dependency_exercise.py
src/upgradepilot/cli.py
src/upgradepilot/__init__.py
tests/test_ci_dependency_exercise.py
tests/test_cli.py
tests/test_package_interface.py
```

Removed:

```text
src/upgradepilot/ci_authority.py
tests/test_ci_authority.py
```

Reviewed and intentionally not expanded:

```text
src/upgradepilot/workflow_commands.py
```

Its mechanism already accepts one explicit requirements path and package identity. Step 7 does not broaden its YAML or shell interpretation.

## Controlled proof obligations

### CI exercise tests

`tests/test_ci_dependency_exercise.py` contains 11 tests proving:

1. direct requirements install plus direct invocation produces `proven`;
2. no workflow inputs produces `no_successful_ci`;
3. no successful job produces `no_successful_ci`;
4. execution absence takes precedence over unavailable definition text;
5. successful job plus unavailable definition remains `unresolved`;
6. successful job plus non-successful run remains `unresolved`;
7. green tox without tracing remains `unresolved`;
8. several statically visible jobs remain `unresolved`;
9. missing explicit requirements path remains `unresolved`;
10. `uv.lock` and constraints paths never become automatic install proof;
11. one proven workflow wins overall while every workflow result remains preserved.

### CLI tests

`tests/test_cli.py` contains 8 tests covering:

- new `CI dependency exercise` labels;
- absence of active `CI authority` labels;
- canonical identity and explicit path passed separately;
- unresolved exercise does not block package or upstream work;
- `no_successful_ci` presentation;
- package and upstream stopping behavior;
- unsupported dependency-stage skipping;
- generic dependency-evidence presentation.

### Package interface test

`tests/test_package_interface.py` contains 1 test proving that all new shared contracts are package-level exports and legacy CI-authority names are not added to `__all__`.

## Validation status

No repository test pass is claimed in this record.

The GitHub connector exposes no repository test runner. The available container still cannot resolve `github.com`, so it could not clone and execute the committed repository.

Expected focused count:

```text
20 tests
```

Expected complete deterministic count:

```text
138 tests
```

These counts are derived from the previously observed 130-test suite, removal of 6 legacy CI tests, addition of 11 replacement CI tests, addition of 2 CLI tests, and addition of 1 package-interface test.

They are expectations, not observed results.

## Required validation

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
pytest 9.0.2 → 9.0.3
project_table_absent
published pytest==9.0.3
2 of 2 provenance
pytest-dev/pytest release tag 9.0.3
unresolved_claim
```

Required Step 7 behavior:

```text
CI dependency exercise: proven
CI dependency exercise reason: exact_head_dependency_exercised
```

The active output must not include:

```text
CI authority:
```

## Scope explicitly not implemented

Step 7 does not implement:

- normal CLI `uv.lock` recognition or exact-file acquisition;
- PR-wide multi-format dependency coordination;
- one-line installed S001 behavior;
- `uv sync`, `uv run`, constraints, or another new consumption rule;
- broader workflow, YAML, shell, tox, nox, task-runner, or reusable-workflow interpretation;
- PEP 440 ordering;
- Python-support relevance;
- compatibility, safety, recommendation, or maintainer action;
- a dynamic plugin framework.

## Stop line

Step 7 remains open until:

```text
focused Step 7 tests pass
+
complete deterministic suite passes
+
installed anonymous S004 passes with new labels
```

Do not begin Step 8 before those proofs are observed and recorded.
