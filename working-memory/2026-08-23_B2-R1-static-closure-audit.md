# B2 R1 Static Closure Audit

**Date:** 2026-08-23  
**Branch:** `agent/r1-exact-file-contract-migration`  
**Plan:** `plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`  
**Status:** STATIC CLOSURE CANDIDATE — local execution and `main` reconciliation still required before R1 can be marked complete.

## 1. Closure question

R1 exists to strengthen exact repository-file evidence ownership without weakening the external GitHub trust boundary or preserving historical metadata merely because downstream code/tests/tools once used it.

This audit asks:

```text
Does any surviving R1 production path still depend on the retired exact-file/source-evidence shape
for a current admitted product responsibility, proof need, material risk, or compatibility obligation?
```

The branch-specific static answer is **no surviving production blocker identified**.

This is not runtime acceptance. The migration branch must still pass the accumulated focused tests and complete deterministic suite, then absorb current `origin/main` and pass again.

## 2. Final strong exact-file ownership

Successful exact repository text:

```text
RepositoryTextFile
├── repository
├── path
├── revision
└── content
```

Typed unavailability:

```text
UnavailableRepositoryFile
├── repository
├── path
├── revision
├── reason
└── detail
```

Provider/acquisition details not retained as durable evidence:

```text
returned_path
reported_byte_count
decoded_byte_count
blob_sha
retrieved_at
```

Important distinction:

```text
retired as durable evidence field
!= forbidden as local provider-validation state
```

`github/repository.py` still reads GitHub's returned path and verifies it against the requested normalized path before admitting the response. The provider also bounds compact base64 input, performs strict base64 decoding, bounds actual decoded bytes, and decodes UTF-8 before constructing `RepositoryTextFile`.

Resource protection therefore follows data actually processed rather than relying on a provider-reported size field.

## 3. Exact-file producer → consumer review

### GitHub provider

`src/upgradepilot/github/repository.py`

Owns external acquisition truth and intrinsic exact-file construction.

Retained:

- canonical repository identity;
- normalized repository-relative path;
- immutable canonical Git revision;
- regular-file response type;
- returned-path equality at the provider boundary;
- base64/decoded-content bounds;
- strict base64;
- UTF-8 text;
- typed 404/unavailability.

Exact-file aliases such as `ExactRepositoryTextFile` / `ExactRepositoryFileEvidence` are not exported by the migration-branch provider.

### Dependency orchestration

`src/upgradepilot/dependency/analysis.py`

Normal flow:

```text
PullRequestIdentity + ChangedFile
→ source role/status admission
→ exact base/head acquisition
→ source semantic extractor
→ PR-wide comparison
→ dependency source context
```

The orchestration layer owns PR repository/head identity when it later derives `DependencySourceContext`.

### Dependency semantic extractors

`src/upgradepilot/dependency/uv_lock.py`  
`src/upgradepilot/dependency/pyproject.py`

Consume already-admitted exact base/head files. They own availability plus source-format semantics, not repeated PR/provider binding.

Final source provenance:

```text
DependencyChangeSourceEvidence
├── path
├── file_format
└── extraction_method
```

### uv membership composition

`src/upgradepilot/dependency/uv_membership.py`

This remains a genuine independent evidence-composition boundary. It intentionally keeps repository/revision/source-path/project-root joins because individually valid dependency context, workflow declaration, project source, and lock source can still be mutually incoherent.

Those joins are not provider revalidation.

### Target artifact environment

`src/upgradepilot/target/artifact_environment.py`

Consumes strong workflow-file evidence and independently supplied dependency-source path. Keeps `repository + revision + workflow_path` as derived Target provenance and the separate dependency-source semantic check. No transport metadata is propagated.

### Target Python

`src/upgradepilot/target/python.py`

Final successful evidence:

```text
TargetPythonDeclaration
├── path
├── revision
└── requires_python
```

The path check is a semantic role check (`pyproject.toml`), not structural path revalidation. Revision remains because later impact composition uses it to prevent evidence from another target head being rebound to the current candidate.

### Tagged changelog/upstream source

`src/upgradepilot/upstream/interval_evidence.py`  
`src/upgradepilot/upstream/interval.py`  
`src/upgradepilot/upstream/changelog.py`

Final durable tagged source:

```text
TaggedChangelogEvidence
├── repository
├── interval
├── resolved_commit_sha
├── path
└── content
```

Normal investigation orchestration pre-binds repository/commit/path before the composer. Later independently supplied upstream authority objects keep only the relations needed by their own proposition.

### Application orchestration

`src/upgradepilot/investigation.py`

Still owns real cross-object identity checks. In particular, selected Target-Python investigation repository/revision must match the frozen PR repository/head before exact-head acquisition. That is a genuine orchestration proposition and was retained.

### CLI

`src/upgradepilot/cli.py`

Renders current domain evidence only. It no longer exposes deleted Target-Python blob provenance or other exact-file transport metadata.

## 4. Residual fan-out reconciled

After the initial production migrations, the red full suite was treated as migration pressure rather than 56 independent bugs.

Subsequent branch-specific migrations reconciled:

### CI/workflow test fixtures

```text
tests/test_github_workflow_definition.py
tests/test_workflow_commands.py
tests/test_workflow_dependency_evidence.py
tests/test_ci_dependency_exercise.py
tests/test_ci_dependency_coverage.py
```

Production CI logic was not changed because its revision/path composition checks are independently justified.

### Application/end-to-end fixtures

```text
tests/test_investigation.py
tests/test_step7f_end_to_end.py
```

Only stale exact-file construction changed. Conditional Target acquisition and bounded-model → deterministic-grounding behavior remain protected.

### Developer live-proof tools

```text
tools/live_s001_upstream_interval_proof.py
tools/live_s001_support_drop_extractor_proof.py
```

Diagnostics now present durable exact source locators rather than depending on deleted blob/count fields.

### PR-specific provider tests

```text
tests/test_pull_request_repository_files.py
```

The suite now protects PR base/head wrapper semantics and delegates generic provider/base64/boundary coverage to the shared exact-commit provider suite rather than duplicating the retired representation.

## 5. Branch-specific spot checks already current

The following neighboring surfaces were inspected on `agent/r1-exact-file-contract-migration` and already use the reconciled contract:

```text
src/upgradepilot/github/repository.py
src/upgradepilot/dependency/change.py
src/upgradepilot/dependency/analysis.py
src/upgradepilot/dependency/pyproject.py
src/upgradepilot/dependency/uv_lock.py
src/upgradepilot/dependency/uv_membership.py
src/upgradepilot/target/python.py
src/upgradepilot/target/artifact_environment.py
src/upgradepilot/upstream/interval_evidence.py
src/upgradepilot/investigation.py
src/upgradepilot/cli.py

tests/test_dependency_change_contracts.py
tests/test_dependency_environment.py
tests/test_target_artifact_environment.py
tests/test_uv_lock_change.py
tests/test_uv_lock_versionless_records.py
tests/test_tagged_changelog_acquisition.py
tests/test_upstream_interval_acquisition_integration.py

experiments/step6_support_drop_smoke.py
```

Default-branch GitHub code-search results were not treated as migration-branch facts; branch-specific fetches were used for closure decisions.

## 6. Static disposition

### KEEP

- provider returned-path equality while admitting an external GitHub response;
- encoded and decoded actual-data bounds;
- UTF-8 and regular-file admission;
- exact repository/path/revision/content type invariants;
- typed exact-file unavailability;
- semantic source-role checks;
- genuine independent composition joins (repository/revision/source path/project root/workflow identity as applicable);
- Target-Python revision provenance needed by later impact composition;
- bounded-model/deterministic-grounding separation.

### REMOVE / already removed

- exact-file durable `blob_sha`;
- durable returned-path copy;
- reported/decoded byte-count propagation;
- exact-file retrieval timestamp propagation;
- copied `head_revision` on `DependencyChangeSourceEvidence`;
- redundant downstream re-proof of PR/provider facts on controlled normal paths;
- exact-file compatibility aliases that imply a second strong type without a distinct responsibility;
- test/tool dependence on retired provider representation.

### NOT R1

The following known problems remain intentionally outside R1:

```text
duplicate uv.lock structural parsers
versionless-record drift between transition/reachability models
--all-packages workspace scope loss
membership naming/proposition breadth
bounded explicit-root reachability redesign
CI rebinding to the later R2–R4 model
```

Those belong to R2–R5 and must not be smuggled into R1 closure.

## 7. Runtime acceptance required now

R1 is a static closure candidate only until local execution establishes the current branch state.

Required local proof order:

```text
branch identity / clean checkout
→ active-surface retired-contract grep
→ accumulated focused R1 tests
→ experiment tests
→ compileall
→ full standard suite
```

If any focused/full test fails, do not merge `main`; classify the earliest failing responsibility and repair R1 first.

## 8. Main reconciliation after branch green

Only after the migration branch is internally green:

```text
fetch current origin/main
→ merge origin/main INTO agent/r1-exact-file-contract-migration
→ resolve non-destructively if necessary
→ rerun affected/focused R1 validation
→ rerun full suite
```

If that combined tree is green, the migration branch may be integrated into `main`. If `main` has not advanced after the reconciliation merge, a fast-forward from `main` to the validated migration branch is preferred because it preserves the exact validated tree.

## 9. R1 completion criterion

R1 may be marked **COMPLETE** only when all are true:

1. this static ownership audit remains valid;
2. migration branch focused R1 tests are green;
3. migration branch full standard suite is green;
4. current `main` has been merged into the same migration branch without unresolved conflict/proof regression;
5. the reconciled branch focused/full validation is green;
6. the validated branch tree is integrated into `main`;
7. final main-tree deterministic validation is green and recorded;
8. `MEMORY.md` is updated to `R1 COMPLETE; R2 NOT STARTED` with the exact accepted commit/test evidence.

Until then, R2 remains blocked.
