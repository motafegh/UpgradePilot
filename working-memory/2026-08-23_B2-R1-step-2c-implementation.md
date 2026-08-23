# Working Memory — B2 R1 Step 2C uv Membership Composition Migration

**Date:** 2026-08-23  
**Status:** IMPLEMENTED + STATICALLY REVIEWED; EXECUTION VALIDATION DEFERRED  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Parent reasoning record:** `2026-08-23_B2-R1-step-2c-responsibility-trace.md`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Step responsibility

Implement the completed Step-2C responsibility trace for `src/upgradepilot/dependency/uv_membership.py` without entering R2 lock-parser reconciliation or R3/R4 uv selection/reachability redesign.

This step treats uv membership as a genuine evidence-composition boundary:

```text
UvLockDependencyContext
+ workflow-derived ProjectEnvironmentSelectionDeclaration
+ exact pyproject.toml evidence
+ exact lock-source evidence
→ bounded explicit-root lock-backed membership result
```

The important distinction from Step 2B is:

```text
strong valid objects
!=
coherent relationship between independently produced objects
```

Therefore Step 2C removes repeated provider/intrinsic validation while retaining the smallest cross-branch joins that actually establish one coherent membership proposition.

## 2. Files changed

Production:

```text
src/upgradepilot/dependency/uv_membership.py
```

Nearest tests:

```text
tests/test_uv_selected_environment_membership.py
tests/test_uv_membership_universal_lock_boundary.py
```

Implementation commits:

```text
405aea0b1481050b9fc184b460b2238e7eb5e70e
→ migrate universal-lock boundary fixture to strong RepositoryTextFile

71e59493808142482516a93a9ab5f211bb46a62a
→ replace legacy metadata fixtures/tests with real membership-composition joins

33970053c7b5acf31d6fb4bf931be7c0e01f3f42
→ migrate uv membership to RepositoryFileEvidence and remove old metadata/rebinding checks

74309ccdbcc832b395ba5f579ba66b71b0f06f41
→ remove the remaining redundant lock-basename recheck so implementation matches the frozen Step-2C trace
```

## 3. Final exact-source input contract

The evaluator now accepts:

```python
project_file: RepositoryFileEvidence
lock_file: RepositoryFileEvidence
```

rather than the removed `ExactRepositoryFileEvidence` alias.

Successful exact files are still narrowed after typed-unavailability handling:

```text
RepositoryFileEvidence
→ UnavailableRepositoryFile ? unresolved
→ otherwise RepositoryTextFile
```

This keeps unavailability explicit while using the strong exact-file owner established in Step 1.

## 4. Final composition gate

`_validate_exact_source_identity(...)` now establishes only the responsibilities owned by this composition boundary.

### Retained — uv-specific semantic preconditions

```text
declaration.manager == "uv"
explicit selectors are present
```

Reason: the current proposition is uv explicit selected-root reachability. A pip declaration or selector-free uv command is not an admitted input to this bounded evaluator.

### Retained — typed source availability

```text
project/lock RepositoryFileEvidence must be available RepositoryTextFile values
```

Reason: missing exact source cannot support parsing/composition.

### Retained — project-file semantic role

```text
basename(project_file.path) == "pyproject.toml"
```

Reason: strong exact-file construction proves that the path is structurally valid, but not that an arbitrary exact repository file has the project-metadata role interpreted by `_parse_project(...)`.

### Retained — independent repository/revision joins

```text
project_file.repository == context.repository
lock_file.repository == context.repository
project_file.revision == context.revision
lock_file.revision == context.revision
```

Reason: dependency context and exact project/lock files are independent evidence branches at this boundary. Individually valid evidence from different repositories or immutable revisions must not be combined.

### Retained — dependency source path ↔ supplied lock source

```text
lock_file.path == context.source_evidence.path
```

Reason: one repository/revision may contain more than one lock source. A dependency transition established from one source path cannot be evaluated against another graph merely because both files are valid.

The separate `uv.lock` basename recheck was deliberately removed after review. `UvLockDependencyContext` already represents the admitted uv-lock dependency-source role, and the stronger exact path join is the relation this layer actually needs. Defending arbitrary manually malformed context construction is not an independently supported product responsibility.

### Retained — workflow declaration project root ↔ exact project location

```text
declaration.project_root == dirname(project_file.path)
```

Reason: the workflow-derived declaration and exact project source are independent branches. A selector bound to one workspace member/root cannot be attached to another project's metadata/lock graph.

## 5. Removed old-contract pressure

Step 2C removed all use of:

```text
ExactRepositoryFileEvidence
returned_path
source_evidence.head_revision
source_evidence.head_blob_sha
source_evidence.head_byte_count
RepositoryTextFile.blob_sha
reported_byte_count
decoded_byte_count
```

Reasons:

```text
returned_path
→ external GitHub response truth owned by provider

blob / byte metadata
→ acquisition/resource/provider concerns; no independent membership proposition

source_evidence.head_revision
→ circular copied provenance already owned by UvLockDependencyContext.revision

exact-file blob/count self-checks
→ intrinsic/provider checks no longer represented by the strong exact-file contract
```

Repository search/static review of the migrated membership source found no remaining occurrences of the removed alias, `returned_path`, `blob_sha`, `head_revision`, or `byte_count` vocabulary.

## 6. Test migration

The membership tests no longer fabricate provider transport metadata to make semantic fixtures constructible.

Strong fixtures now use only:

```text
repository
path
revision
content
```

The old blob-identity mismatch test was removed because blob equality is not a current membership proposition.

It was replaced with real composition-pressure coverage:

```text
context repository mismatch
→ unresolved source identity

exact project revision mismatch
→ unresolved source identity

lock path != dependency source path
→ unresolved source identity

workflow declaration project_root != exact project location
→ unresolved source identity

UnavailableRepositoryFile
→ unresolved source identity
```

Existing semantic coverage remains for:

```text
S001 transitive docs witness
direct selected root
not_established boundary
marker/fork ambiguity
activated dependency extras
optional-extra roots
all-groups/all-extras
missing selected roots
repeated lock records/version discriminator
cycles
nested workspace project-root binding
universal-lock resolution-marker boundary
```

## 7. Static review result

The production commit diff was inspected after editing.

Material source changes are limited to:

```text
module ownership/orientation comments
ExactRepositoryFileEvidence → RepositoryFileEvidence
removal of repository_relative_parts revalidation use
narrowing _validate_exact_source_identity(...)
```

No intended changes were made to:

```text
uv TOML parsing
lock schema/revision parsing
package/edge parsing
workspace package binding
selected-root construction
edge resolution
marker handling
repeated-record ambiguity
cycle safety
traversal bounds
direct/transitive witness semantics
member / not_established / unresolved result semantics
```

A working-memory review caught one initial implementation drift: the first source commit still retained a separate `uv.lock` basename check even though the frozen trace selected the stronger source-path join as sufficient. Commit `74309ccdbcc832b395ba5f579ba66b71b0f06f41` removed that repeat before Step 2C was closed.

This is a useful execution lesson:

```text
working memory is not only a history log
→ it is also a consistency check against implementation drift
```

## 8. Proof state

```text
R1 Step 1                         IMPLEMENTED / NOT EXECUTION-VALIDATED
R1 Step 2B                       IMPLEMENTED + STATICALLY REVIEWED / NOT EXECUTION-VALIDATED
R1 Step 2C responsibility trace  COMPLETE
R1 Step 2C code migration        IMPLEMENTED
R1 Step 2C static review         COMPLETE
R1 Step 2C runtime execution     NOT PERFORMED
```

No green/runtime claim is attached to this work.

Latest historical accepted full runtime proof remains:

```text
bfdfd4257574f85cc3a2d094bf46a37ad6373dea
508 tests / OK
```

## 9. Deferred validation addition

When the local WSL environment is available, Step-2C focused validation must include at least:

```text
tests.test_uv_selected_environment_membership
tests.test_uv_membership_universal_lock_boundary
```

alongside the already deferred Step-1 and Step-2B slices.

Failures must be diagnosed against the earliest changed ownership boundary, not patched merely to restore green output.

## 10. R1 disposition and next route

The active R1 implementation pressure has now covered:

```text
strong exact repository-file owner
→ dependency exact-file path migration
→ materially different independent-composition consumer sanity check
```

This satisfies the planned structural migration intent of R1, but the R1 execution gate is still deferred because focused tests cannot currently be run.

Current continuation should therefore be represented as:

```text
R0  COMPLETE
R1  IMPLEMENTATION COMPLETE / EXECUTION GATE DEFERRED
R2  NEXT BOUNDED DESIGN/IMPLEMENTATION STEP
```

Starting R2 must not retroactively describe R1 as runtime validated. R2 owns the separate problem of duplicated `uv.lock` structural truth and demonstrated versionless-record admission drift.
