# Working Memory — B2 R1 CI/Workflow Fixture Fan-out Trace

**Date:** 2026-08-23  
**Status:** TRACE COMPLETE; TEST-FIXTURE MIGRATION AUTHORIZED  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Why this slice exists

Focused runtime gates established the already-migrated exact-file/provider, dependency, uv-membership, Target artifact-environment, and tagged-changelog surfaces as green. The later 507-test full-suite run still reported broad failures, and Target-Python was one confirmed stale contract family.

After migrating Target-Python, the next bounded task is not to redesign every remaining `RepositoryTextFile` consumer. The correct task is to identify whether the next failures are caused by:

1. a real production responsibility that still depends on retired exact-file metadata; or
2. test fixtures that still construct historical evidence shapes.

The CI/workflow family is the first coherent residual cluster.

## 2. Production trace

Current production flow:

```text
exact workflow RepositoryTextFile
→ github/workflow_definition.py
→ bounded WorkflowDefinition IR
→ ci/workflow_commands.py
→ static dependency consumption / direct invocation evidence
→ ci/dependency_exercise.py
→ static/runtime CI coverage composition
```

Production modules inspected:

```text
src/upgradepilot/github/workflow_definition.py
src/upgradepilot/ci/workflow_commands.py
src/upgradepilot/ci/dependency_exercise.py
```

These modules already consume the strong exact-file contract through the fields they materially need:

```text
path
revision
content
```

No production use of provider transport metadata (`blob_sha`, returned path, byte counts, retrieval time) is required in this family.

## 3. Production checks that must remain

The following are not duplicate provider checks; they are genuine cross-object CI composition checks:

```text
workflow definition revision == workflow run head SHA
```

and:

```text
external static consumption workflow path/revision
== current exact workflow path/revision
```

plus dependency-source context revision/package joins where independently supplied context is composed with a workflow.

These checks protect coherent composition between independently valid runtime/static/domain evidence. They remain.

Therefore:

```text
production CI redesign: NOT JUSTIFIED
```

## 4. Residual stale test contracts found on migration branch

The following current branch tests still construct the historical exact-file shape:

```text
tests/test_github_workflow_definition.py
tests/test_workflow_commands.py
tests/test_workflow_dependency_evidence.py
tests/test_ci_dependency_exercise.py
tests/test_ci_dependency_coverage.py
```

Observed stale patterns:

```python
RepositoryTextFile(
    path=...,
    revision=...,
    blob_sha=...,
    content=...,
)
```

Current contract requires:

```python
RepositoryTextFile(
    repository=...,
    path=...,
    revision=...,
    content=...,
)
```

`tests/test_ci_dependency_exercise.py` also constructs `UnavailableRepositoryFile` without its required repository identity.

`tests/test_ci_dependency_coverage.py` additionally still passes retired `head_revision` into `DependencyChangeSourceEvidence`; revision belongs to the typed `DependencySourceContext`, while source evidence now owns only path/format/extraction method.

## 5. Decisions

### KEEP

All existing CI/workflow semantic assertions, including:

- workflow YAML structural parsing and bounds;
- job/step ordering;
- reusable-workflow abstention;
- requirements install recognition;
- static consumption vs direct exercise separation;
- exact workflow revision/runtime-head join;
- external consumption path/revision rebinding;
- S001/S011 proof-boundary behavior;
- no static→runtime correlation claim.

### REMOVE FROM FIXTURES

```text
blob_sha
DependencyChangeSourceEvidence.head_revision
```

### ADD TO FIXTURES

```text
RepositoryTextFile.repository = "example/project"
UnavailableRepositoryFile.repository = "example/project"
```

### NO PRODUCTION CHANGE

This slice must not edit:

```text
src/upgradepilot/github/workflow_definition.py
src/upgradepilot/ci/workflow_commands.py
src/upgradepilot/ci/dependency_exercise.py
```

unless a separate source-level defect is discovered during static review.

## 6. Learning point

A failing test after a contract migration does not automatically mean production behavior is wrong.

```text
strong production contract changed
+ test still fabricates old object
→ fixture migration pressure
!= new product responsibility
```

The converse also matters: we do not delete real CI revision/path joins merely because the exact-file type is stronger. Those joins compare independent evidence branches and therefore remain genuine composition proof.

## 7. Intended implementation slice

Migrate exactly the five CI/workflow test files listed above to current evidence contracts while preserving every semantic assertion.

Then statically compare the changes and record the result. Runtime validation remains deferred until local execution is available again.

## 8. Stop line

Do not use this fixture cleanup as authority to enter R2. After this family is migrated, continue the residual R1 inventory for other integration/end-to-end fixtures or real production consumers. R1 closes only after the migration branch is internally full-suite green and later reconciled with `main` on the same branch.
