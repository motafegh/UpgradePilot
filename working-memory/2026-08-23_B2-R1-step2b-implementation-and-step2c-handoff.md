# Working Memory — B2 R1 Step 2B Implementation and Step 2C Handoff

**Date:** 2026-08-23  
**Status:** STEP 2B IMPLEMENTED + STATICALLY REVIEWED; EXECUTION VALIDATION DEFERRED  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Parent record:** `2026-08-23_B2-R1-exact-file-contract-migration-continuation.md`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Why this record exists

The parent record completed the Step-2B end-to-end responsibility trace and froze the target source-provenance contract. This continuation records the actual bounded implementation, one additional ownership simplification discovered during implementation, the static review result, and the exact Step-2C handoff.

No command/runtime validation is claimed here because the WSL/laptop test environment is not currently available.

## 2. Step-2B responsibility result implemented

The shared dependency source record is now:

```text
DependencyChangeSourceEvidence
├── path
├── file_format
└── extraction_method
```

It no longer carries:

```text
base_revision
head_revision
base/head blob identifiers
base/head byte counts
```

Ownership is now explicit:

```text
PullRequestIdentity
→ PR repository/base/head identity

RepositoryTextFile
→ exact file repository/path/revision/content

DependencyChangeSourceEvidence
→ dependency-source path + semantic format + extraction method

DependencySourceContext
→ exact-head repository/revision context when later composition actually needs it
```

This implements the earlier trace conclusion that useful identity/provenance facts should remain with their canonical owners rather than being copied through every downstream evidence record.

## 3. Additional Step-2B finding — orchestration context is not automatically semantic input

During implementation the new end-to-end ownership rule was applied again to the `ChangedFile` parameter of:

```text
extract_uv_lock_changes(...)
extract_pyproject_optional_extra_change(...)
```

After removing the duplicate path/status/repository validation, `ChangedFile` had only one remaining use: copying `changed_file.filename` into `DependencyChangeSourceEvidence.path`.

The normal path already establishes:

```text
analysis.py
→ admits exact source role + modified status
→ passes changed_file.filename to base/head acquisition
→ provider returns strong RepositoryTextFile for the requested path
→ semantic extractor receives that admitted exact file evidence
```

Therefore the `ChangedFile` object no longer supplied an independent semantic fact to the extractor.

Decision:

```text
REMOVE ChangedFile from exact-file semantic extractor signatures
```

and source provenance now takes its path from the admitted exact HEAD file:

```text
DependencyChangeSourceEvidence(path=head_file.path, ...)
```

Mental model:

```text
orchestration context
!= semantic input

an argument historically used by local defensive checks
!= current responsibility to keep the argument
```

This is a direct application of `JUST-004` / `JUST-005`, not an API-minimization preference by itself.

## 4. Source changes

### `src/upgradepilot/dependency/change.py`

Current branch source models `DependencyChangeSourceEvidence` as only:

```python
path
file_format
extraction_method
```

Its documentation now states that PR snapshot identity and exact-file identity remain in their canonical owners.

### `src/upgradepilot/dependency/analysis.py`

Commit:

```text
34b577b54a855f50eacc3eca3d6b0d8426f542a3
```

The PR-wide integration boundary continues to own:

```text
source path/role admission
+ modified-status admission
+ exact base/head acquisition using PullRequestIdentity + ChangedFile.filename
```

It now calls exact-file semantic extractors with only the acquired base/head evidence.

### `src/upgradepilot/dependency/uv_lock.py`

Commit:

```text
c19012359be6986fdc19f0c105b76bf5bb40a2bd
```

Current semantic signature:

```python
extract_uv_lock_changes(base_file, head_file)
```

Retained responsibilities:

```text
typed exact-file unavailability
uv.lock TOML/schema validation
package-record structural validation
normalized package grouping
conservative base/head comparison
artifact-only distinction
versionless editable/virtual handling
ambiguity/unsupported-state reporting
```

Removed responsibilities:

```text
PR path/status admission
repository equality rebinding
ChangedFile ↔ exact-file path rebinding
provider returned-path checks
blob/byte validation
copied base/head revision provenance
```

No uv parser/comparison semantic rule was intentionally changed.

### `src/upgradepilot/dependency/pyproject.py`

Commit:

```text
267bd2d96ff0bd27608b6070fb582d2f0075ad8c
```

Current semantic signature:

```python
extract_pyproject_optional_extra_change(base_file, head_file)
```

Retained responsibilities:

```text
typed exact-file unavailability
TOML / [project.optional-dependencies] structure
PEP 508 requirement parsing
normalized package identity
exact-pin transition rule
marker/extras/direct-reference comparison
ambiguous/multiple/unsupported-state reporting
neutral result for unrelated pyproject metadata change
```

Removed upstream/provider responsibilities mirror the uv-lock change.

## 5. Nearest test migration

### Shared contract

`tests/test_dependency_change_contracts.py`

Commit:

```text
f3e9c01aa4d4f2ff7e98a02f44dd0ea4df6aec35
```

Now protects only `path + file_format + extraction_method` as dependency-source provenance.

### pyproject semantic tests

`tests/test_pyproject_optional_extra_change.py`

Commit:

```text
0def155a62a327a015820d2a502d82cc8d6ceab8
```

Tests now begin from strong exact files and call the semantic extractor with base/head only. The PEP 508/optional-extra semantic cases remain.

### uv versionless regression tests

`tests/test_uv_lock_versionless_records.py`

Commit:

```text
11bcef2fd40efca30c63f61e9fc11e3133f0a754
```

Old exact-file aliases/provider metadata and `ChangedFile` semantic input are removed; versionless workspace semantics remain unchanged.

### main uv semantic tests

`tests/test_uv_lock_change.py`

Commit:

```text
01a8499eda33ed09f6343ce51733835e6f9e3415
```

The test suite still separately protects `is_modified_uv_lock_file(...)` as the admission helper, while semantic extraction tests now start after admission with exact base/head evidence only.

The old direct-extractor repository/path/status-defense cases are no longer retained as semantic responsibilities.

### integration tests

Current branch versions of:

```text
tests/test_dependency_analysis.py
tests/test_pyproject_dependency_analysis.py
```

are aligned to the strong exact-file contract and continue to prove that `analysis.py` owns file-status admission/acquisition. The pyproject integration test also explicitly proves that the downstream source context receives `repository` and `revision` from the PR identity, supporting removal of copied revision fields from `DependencyChangeSourceEvidence`.

## 6. Normal-path presentation check

`src/upgradepilot/cli.py` was inspected after the source-contract change.

The CLI already prints PR base/head once from `PullRequestIdentity` and now presents each dependency source only as:

```text
path
format
extraction method
```

Therefore no remaining CLI dependency on removed source-evidence revision/blob/byte fields blocks Step 2B.

## 7. Static review result

Step 2B is considered **implemented and statically reviewed**, not runtime validated.

Observed boundaries after the migration:

```text
analysis.py
→ PR source admission + exact acquisition

repository.py
→ external GitHub validation + strong exact-file evidence

uv_lock.py / pyproject.py
→ source-specific semantic parsing/comparison

change.py
→ source-independent provenance + PR-wide dependency consensus
```

No intentional change was made to uv transition semantics or pyproject optional-extra transition semantics.

## 8. Known remaining pressure — Step 2C

`src/upgradepilot/dependency/uv_membership.py` still represents the old exact-file/source-evidence contract. It currently contains pressure such as:

```text
ExactRepositoryFileEvidence alias
returned_path checks
blob/count checks
source_evidence.head_revision rebinding
```

This is expected and is now the exact next responsibility.

Unlike the Step-2B extractors, `uv_membership.py` composes separate evidence branches:

```text
UvLockDependencyContext
+ workflow-derived uv declaration
+ exact pyproject.toml
+ exact uv.lock
```

Therefore Step 2C must perform its own end-to-end ownership trace. It should remove provider/circular propagation checks but must preserve any repository/revision/path/project-root relationship that genuinely establishes coherence between independently assembled evidence branches.

Do not infer:

```text
Step 2B removed relational checks
→ Step 2C should remove all relational checks
```

Correct rule:

```text
same-looking relation
+ different composition boundary
→ independently evaluate ownership and proof need
```

## 9. Proof state

```text
R0                  COMPLETE
R1 Step 1           IMPLEMENTED / NOT EXECUTION-VALIDATED
R1 Step 2A          SUPERSEDED INTO COHERENT STEP-2B CONTRACT
R1 Step 2B trace    COMPLETE
R1 Step 2B code     IMPLEMENTED + STATICALLY REVIEWED / NOT EXECUTION-VALIDATED
R1 Step 2C          NEXT / NOT STARTED
R2                  NOT STARTED
```

Historical accepted runtime proof remains:

```text
bfdfd4257574f85cc3a2d094bf46a37ad6373dea
508 tests / OK
```

No Step-2B commit supersedes that runtime proof until the deferred focused/integration/full local execution is actually run.

## 10. Deferred execution-validation ledger

When WSL/laptop access returns:

```text
Step 1 provider/type focused tests
→ Step 2B dependency source/analysis focused tests
→ Step 2C membership focused tests once implemented
→ later R1 Target/upstream migrations
→ nearest integration/end-to-end tests
→ full deterministic suite
```

Failures must be diagnosed against the earliest relevant bounded responsibility rather than patched only to make the final suite green.
