# Working Memory — B2 R1 CI/Workflow Fixture Fan-out Migration

**Date:** 2026-08-23  
**Status:** IMPLEMENTED + STATICALLY REVIEWED; RUNTIME VALIDATION DEFERRED  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Parent trace:** `2026-08-23_B2-R1-ci-workflow-fixture-fanout-trace.md`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Scope

Migrate one coherent residual R1 test-fixture family to the already-accepted strong exact-file/dependency-source contracts without changing CI/workflow production semantics.

Files migrated:

```text
tests/test_github_workflow_definition.py
tests/test_workflow_commands.py
tests/test_workflow_dependency_evidence.py
tests/test_ci_dependency_exercise.py
tests/test_ci_dependency_coverage.py
```

No production source file was changed.

## 2. Why no production change was justified

The production path was traced before editing:

```text
RepositoryTextFile
→ github/workflow_definition.py
→ WorkflowDefinition
→ ci/workflow_commands.py
→ static consumption/direct-invocation evidence
→ ci/dependency_exercise.py
→ runtime/static coverage result
```

Those modules already consume only current exact-file fields (`path`, `revision`, `content`) and preserve real independent composition checks.

Examples that remain intentionally protected:

```text
workflow definition revision == workflow run head SHA
external consumption workflow path/revision == current exact workflow path/revision
dependency source context revision/package == workflow/dependency under composition
```

These are not provider revalidation. They join independently valid evidence branches and therefore remain genuine proof responsibilities.

## 3. Fixture migration

### RepositoryTextFile fixtures

Historical fixture shape:

```python
RepositoryTextFile(
    path=...,
    revision=...,
    blob_sha=...,
    content=...,
)
```

Current fixture shape:

```python
RepositoryTextFile(
    repository="example/project",
    path=...,
    revision=...,
    content=...,
)
```

`blob_sha` was removed because it is no longer part of successful exact-file evidence.

### UnavailableRepositoryFile fixtures

`tests/test_ci_dependency_exercise.py` now supplies the required repository identity to typed unavailability:

```python
UnavailableRepositoryFile(
    repository="example/project",
    path=...,
    revision=...,
    reason=...,
    detail=...,
)
```

### Dependency source evidence fixtures

`tests/test_ci_dependency_coverage.py` still copied `head_revision` into `DependencyChangeSourceEvidence` for uv-lock and pyproject-extra cases.

That field was removed. The exact revision remains on the corresponding typed `DependencySourceContext`, which is the proper owner used by CI composition.

Resulting split:

```text
DependencyChangeSourceEvidence
→ path / format / extraction method

DependencySourceContext
→ repository / revision / changed package / source semantics
```

## 4. Semantic behavior intentionally preserved

No assertions were removed or weakened around:

- YAML structural parsing and parser resource guards;
- ordered jobs/steps;
- reusable-workflow boundaries;
- direct requirements consumption;
- constraints not becoming installation proof;
- multiple-job behavior;
- static consumption vs direct package exercise;
- successful exact-head runtime evidence;
- no static↔runtime correlation claim;
- external workflow revision/path rebinding;
- S001 positive project-environment witness;
- S011 non-membership under dev-vs-mlx selection.

## 5. Static review

Comparison from trace commit:

```text
01c220b6c78489adea487b8ead4c2c7bf8db5554
→ current branch after fixture migration
```

showed exactly five modified files, all under `tests/`:

```text
test_ci_dependency_coverage.py       +5 / -6
test_ci_dependency_exercise.py       +4 / -1
test_github_workflow_definition.py   +1 / -1
test_workflow_commands.py            +1 / -1
test_workflow_dependency_evidence.py +1 / -1
```

No production source, governance, plan, or unrelated test file changed in this implementation tranche.

## 6. Proof state

```text
responsibility trace    COMPLETE
fixture migration       COMPLETE
static diff review      COMPLETE
runtime execution       NOT PERFORMED after this migration
```

The previous local 507-test failure inventory must not be treated as current post-fix results. A later local run is required before any claim that this family is runtime green.

## 7. Next residual family found

Branch-specific inspection found the next coherent integration/end-to-end fixture family:

```text
tests/test_investigation.py
tests/test_step7f_end_to_end.py
```

Both still construct historical exact-file shapes in controlled application-path fixtures.

Examples include:

```text
Target pyproject RepositoryTextFile with blob_sha
Tagged changelog RepositoryTextFile with returned_path/blob/count/time
```

These files test orchestration/end-to-end composition rather than a new production exact-file consumer. They should receive their own bounded fixture-fan-out trace/migration next, with special care not to weaken the real investigation identity checks or bounded local-model path.

## 8. Learning checkpoint

This slice reinforces a critical migration distinction:

```text
production relationship check still has independent proof purpose
→ KEEP production check

fixture constructs a type using fields the type no longer owns
→ MIGRATE fixture
```

A test failure is evidence about mismatch with the current contract; it is not automatic authority to restore deleted production fields.
