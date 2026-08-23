# Working Memory — B2 R1 Step 2B Dependency-Source Migration

**Date:** 2026-08-23  
**Status:** IMPLEMENTED + STATICALLY REVIEWED; EXECUTION VALIDATION DEFERRED  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Parent record:** `2026-08-23_B2-R1-exact-file-contract-migration-continuation.md`

## 1. Step responsibility

Implement the completed Step-2B end-to-end responsibility-trace conclusions for exact dependency sources without entering uv-membership composition or changing uv/pyproject semantic parsing.

The final ownership chain is:

```text
PullRequestIdentity + ChangedFile
→ dependency/analysis.py admits supported source path/status
→ GitHubRepositoryClient acquires base/head from the same PR identity + requested path
→ strong RepositoryFileEvidence
→ uv_lock.py / pyproject.py semantic extraction
→ minimal DependencyChangeSourceEvidence
```

The source-specific exact-file extractors are not independent PR trust/composition boundaries.

## 2. Final dependency-source provenance contract

`DependencyChangeSourceEvidence` now contains only:

```text
path
file_format
extraction_method
```

Removed from the intermediate Step-2A contract:

```text
base_revision
head_revision
```

Previously removed provider metadata remains absent:

```text
base/head blob SHA
base/head byte counts
```

Ownership after migration:

```text
PullRequestIdentity
→ repository + PR base/head revision identity

RepositoryTextFile
→ exact repository/path/revision/content while exact source is consumed

DependencySourceContext
→ repository + exact HEAD revision when later composition genuinely needs it

DependencyChangeSourceEvidence
→ dependency source path + format + extraction method only
```

## 3. Extractor boundary after migration

### `dependency/pyproject.py`

Final semantic entry:

```python
extract_pyproject_optional_extra_change(base_file, head_file)
```

The normal caller already admitted a modified `pyproject.toml` and acquired both exact historical files. The extractor now owns:

- typed exact-file unavailability;
- TOML / PEP 621 / PEP 508 interpretation;
- conservative optional-extra comparison;
- minimal dependency-source provenance.

It no longer owns:

- changed-file path/status admission;
- base/head repository equality;
- exact-file path rebinding to `ChangedFile`;
- returned-path validation;
- revision/blob/byte transport/invariant revalidation.

### `dependency/uv_lock.py`

Final semantic entry:

```python
extract_uv_lock_changes(base_file, head_file)
```

It now owns:

- typed exact-file unavailability;
- uv.lock TOML/schema/package-record structural interpretation;
- conservative base/head transition comparison;
- minimal dependency-source provenance.

It no longer owns the same upstream PR-binding/provider checks listed above.

The extractor provenance path comes from the admitted exact HEAD file path. Normal orchestration has already established that base/head acquisition uses the same changed-file path.

## 4. Integration owner retained

`dependency/analysis.py` remains the source-admission/integration owner. Static inspection confirms it:

1. classifies exact lowercase `uv.lock` / `pyproject.toml` paths;
2. rejects unsupported non-modified status before acquisition;
3. calls base/head repository acquisition with the same `PullRequestIdentity` and exact `ChangedFile.filename`;
4. passes only the resulting base/head exact-file evidence to the semantic extractor;
5. builds downstream `DependencySourceContext` repository/revision identity directly from `identity.repository` / `identity.head_sha`.

This is the correct owner for the relationships removed from the extractors.

## 5. Presentation/integration migration

Static review found `cli.py` still dereferenced removed dependency-source revision/blob/byte fields. That would make the normal supported application path fail even though it was not part of parsing.

The CLI dependency evidence rendering was therefore migrated in Step 2B to print only:

```text
path
file format
extraction method
```

PR base/head revision identity is already printed once from `PullRequestIdentity` at the investigation level.

Nearest dependency integration/contract tests were also migrated so they protect responsibilities at the correct owner:

- source-level uv/pyproject tests protect semantic parsing/comparison and typed availability;
- `dependency_analysis` tests protect path/status admission and exact base/head acquisition calls;
- source-context tests protect repository/HEAD revision context constructed from PR identity;
- shared dependency-contract tests protect the minimal provenance shape.

## 6. Static review result

The `uv_lock.py` and `pyproject.py` diffs were inspected after editing.

No intended changes were made to:

- uv TOML schema semantics;
- package-record validation;
- versionless editable/virtual record semantics;
- repeated-record ambiguity behavior;
- uv structural comparison/canonicalization;
- PEP 621 optional-extra interpretation;
- PEP 508 parsing;
- exact-pin comparison semantics.

The material source changes are ownership/signature/provenance changes around those semantic bodies.

During the review, concurrent branch updates were detected through GitHub optimistic-concurrency conflicts. Files were re-read before any retry; newer branch content was preserved rather than overwritten. The final branch state independently converged on the same two-file extractor contract described above.

## 7. Proof state

```text
R1 Step 2B responsibility trace    COMPLETE
R1 Step 2B source migration        IMPLEMENTED
R1 Step 2B static/source review    COMPLETE
R1 Step 2B runtime execution       NOT PERFORMED
```

No tests were executed from the assistant environment. No green/runtime claim is attached to this step.

Latest historical accepted full runtime proof remains:

```text
bfdfd4257574f85cc3a2d094bf46a37ad6373dea
508 tests / OK
```

## 8. Deferred Step-2B validation slice

When local WSL execution is available, include at least:

```text
tests.test_dependency_change_contracts
tests.test_uv_lock_change
tests.test_uv_lock_versionless_records
tests.test_pyproject_optional_extra_change
tests.test_dependency_analysis
tests.test_pyproject_dependency_analysis
tests.test_dependency_environment
```

along with the earlier Step-1 provider/type focused tests, then continue through Step-2C integration and the later full-suite ledger.

## 9. Exact next step — R1 Step 2C

Inspect/migrate `src/upgradepilot/dependency/uv_membership.py` as a **real independent evidence-composition boundary**.

Current old-contract pressure still visible there includes:

```text
ExactRepositoryFileEvidence alias
returned_path checks
blob SHA checks
reported/decoded byte checks
DependencyChangeSourceEvidence.head_revision/head_blob_sha/head_byte_count rebinding
```

These are candidates for removal.

But Step 2C must not mechanically delete all relation checks. Membership composes independently produced:

```text
UvLockDependencyContext
+ workflow-derived ProjectEnvironmentSelectionDeclaration
+ exact pyproject.toml
+ exact uv.lock
```

Therefore independently necessary relations such as context repository/revision ↔ project/lock exact files, source path ↔ lock path, and project-root ↔ declaration may still earn retention after the full end-to-end ownership trace.

Do not redesign uv graph/reachability semantics in Step 2C. R2/R4 own later structural/reachability reconciliation.
