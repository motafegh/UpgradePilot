# Working Memory — B2 R1 Step 2C uv Membership Composition Trace

**Date:** 2026-08-23  
**Status:** RESPONSIBILITY TRACE COMPLETE; CODE MIGRATION NEXT  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Parent implementation record:** `2026-08-23_B2-R1-step-2b-implementation.md`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Step responsibility

Reconcile exact-file/provenance validation in `src/upgradepilot/dependency/uv_membership.py` against the strengthened R1 contracts without redesigning uv traversal/reachability semantics.

Step 2C is deliberately different from Step 2B.

Step 2B semantic extractors receive exact files assembled through one controlled PR integration route. uv membership composes several independently produced evidence branches:

```text
UvLockDependencyContext
+ ProjectEnvironmentSelectionDeclaration
+ exact pyproject.toml evidence
+ exact uv.lock evidence
→ bounded explicit-root lock-backed membership result
```

Therefore the evaluator itself currently owns real cross-branch coherence checks.

## 2. Product responsibility is independently admitted

Repository search found no current normal-application call that assembles and invokes `evaluate_uv_selected_environment_membership(...)`; CI consumes the resulting membership type rather than invoking the evaluator itself.

That absence does **not** make the function's checks test-only authority. AUDIT-007 and the active reconciliation plan already admit the bounded product proposition:

```text
exact changed package from uv.lock
+ exact project/lock source at one immutable revision
+ one static explicit uv group/extra selection
→ is the changed package reachable from the selected roots?
```

So the evaluator is a real deterministic capability awaiting broader application integration, not an arbitrary helper kept alive by fixtures.

## 3. Producer/owner trace

### Dependency context

`dependency/analysis.py::_source_contexts()` creates `UvLockDependencyContext` from trusted dependency-change evidence:

```text
repository = PullRequestIdentity.repository
revision = PullRequestIdentity.head_sha
normalized_package = trusted dependency identity
source_evidence = uv-lock dependency source evidence
```

The context therefore owns the exact-head dependency/source identity used by later composition.

### Static uv declaration

`environment_selection.observe_project_environment_selection(...)` receives an independently known `project_file_path`, validates/binds workflow command location, and emits `ProjectEnvironmentSelectionDeclaration`.

The declaration preserves:

```text
manager
operation
segment_index
project_root
explicit selectors
```

It is workflow/static-selection evidence; it does not prove lock membership.

The observer may emit a uv declaration with no explicit selectors only as part of an unresolved observation because uv defaults require additional evidence.

### Exact project/lock files

The membership evaluator accepts generic `RepositoryFileEvidence` for `pyproject.toml` and `uv.lock`. Each successful `RepositoryTextFile` already owns structural repository/path/revision/content validity; provider returned-path/blob/byte transport checks belong upstream.

No current integration owner pre-binds these two exact files to the dependency context/declaration before the evaluator, so the evaluator must retain the composition relations that actually establish that they belong together.

## 4. Current `_validate_exact_source_identity(...)` pressure map

### A. `declaration.manager == "uv"`

**Decision: KEEP.**

Reason: `ProjectEnvironmentSelectionDeclaration` supports both pip and uv. This uv-specific evaluator must establish that it is interpreting an admitted uv declaration.

### B. explicit selector presence

**Decision: KEEP as semantic precondition.**

Reason: the current proposition is explicit selected-root reachability. The selection observer deliberately treats a uv command with no visible explicit roots as unresolved because default groups/config require additional evidence. Membership must not invent those roots.

This is semantic admissibility, not exact-source identity, even though the current private helper mixes those concerns.

### C. typed exact-file unavailability

**Decision: KEEP.**

Reason: `RepositoryFileEvidence` deliberately includes `UnavailableRepositoryFile`; membership cannot parse or compose a missing historical source and must degrade explicitly.

### D. project path structural validation

Current code repeats `repository_relative_parts(project_file.path)` to establish normalized repository syntax.

**Decision: REMOVE repeated structural validation.**

Reason: successful `RepositoryTextFile` construction already owns normalized repository-relative path structure.

### E. project-file role (`pyproject.toml`)

**Decision: KEEP.**

Reason: the exact project file is still a generic repository text file. No other retained relation proves that the supplied source has the project-metadata role that `_parse_project(...)` interprets. Use the already-valid path only to establish/derive this semantic role/root.

### F. lock path structural/basename validation

**Decision: REMOVE the separate repeated lock-role check after retaining the stronger source-path join.**

Reason:

```text
UvLockDependencyContext.source_path
→ produced from an admitted uv-lock dependency source

lock_file.path == context.source_path
→ binds this exact lock file to that dependency source
```

For an admitted `UvLockDependencyContext`, the source-path join already identifies the lock role. A second basename check exists only to defend manually malformed context construction, which is not an independently supported product route.

### G. `returned_path == path`

**Decision: REMOVE.**

Reason: external GitHub response-path equality is provider-owned and `returned_path` no longer exists in the strong exact-file contract.

### H. context repository/revision ↔ exact project/lock files

Current proposition:

```text
project_file.repository == context.repository
lock_file.repository == context.repository
project_file.revision == context.revision
lock_file.revision == context.revision
```

**Decision: KEEP.**

Reason: the objects are independently valid evidence branches. Without this join, membership could combine a dependency transition from repository/revision A with project/lock source from B and manufacture a false relation.

This is the central contrast with Step 2B:

```text
valid object != coherent composition
```

### I. lock path ↔ dependency source path

Current proposition:

```text
lock_file.path == context.source_evidence.path
```

**Decision: KEEP**, preferably through `context.source_path`.

Reason: one repository/revision can contain several `uv.lock` files. Without this relation, a dependency change established from `services/a/uv.lock` could be rebound to the graph in `services/b/uv.lock`.

### J. `source_evidence.head_revision == context.revision`

**Decision: REMOVE.**

Reason: the field no longer exists. More importantly, the earlier trace established that both values were copied from the same `PullRequestIdentity.head_sha`; the check re-proved circular propagation rather than an independent evidence relation.

### K. source-evidence blob/byte rebinding

**Decision: REMOVE.**

Includes:

```text
head_blob_sha ↔ lock_file.blob_sha
head_byte_count ↔ lock_file.decoded_byte_count
```

Reason: these fields did not establish an independent dependency/membership proposition and were removed from the durable contracts.

### L. exact-file blob existence / reported-vs-decoded byte consistency

**Decision: REMOVE.**

Reason: provider/strong exact-file ownership already controls the admitted exact text. Membership does not own transport metadata integrity.

### M. declaration project root ↔ exact project-file location

Current proposition:

```text
declaration.project_root == dirname(project_file.path)
```

**Decision: KEEP.**

Reason: the static declaration was derived from workflow command/project-location evidence, while the exact project file is supplied independently. Without the join, a selector for one workspace member/root could be applied to another project's metadata/lock graph.

### N. project ↔ lock workspace package binding

The later `_bind_workspace_package(...)` relation remains in Step 2C:

```text
project name
+ project path relative to lock root
↔ exactly one editable/virtual workspace package
```

**Decision: KEEP for now.**

Reason: this is semantic root binding, not provider validation. AUDIT-007 questions whether project content is necessary for the eventual narrower R4 reachability proposition, but R4—not Step 2C—owns that redesign.

### O. selected project group/extra names ↔ lock roots

**Decision: KEEP for now.**

Reason: changing project-content participation or root semantics would cross into AUDIT-007/R4 proposition redesign. Step 2C only reconciles the exact-source/composition contract.

## 5. Target Step-2C validation shape

After migration, the input gate should conceptually establish only:

```text
uv declaration
+ explicit selectors
+ project/lock source available
+ project file has pyproject.toml role
+ project exact file repository/revision == dependency context
+ lock exact file repository/revision == dependency context
+ lock exact path == dependency context source path
+ declaration project_root == exact project-file root
```

Then existing project/lock parsing, workspace binding, root selection, and traversal remain unchanged.

Provider metadata and copied dependency-source revision/blob/byte fields must not participate.

## 6. Test migration requirements

Nearest membership tests must be updated from the removed exact-file/source metadata contract.

### Keep semantic/traversal coverage

Preserve S001 positive witness, direct root, `not_established`, marker/fork ambiguity, activated extras, all-groups/all-extras, cycles, repeated-record discriminators, nested project-root binding, and universal-lock boundary tests.

### Remove obsolete metadata fixture authority

Remove:

```text
returned_path
blob_sha
reported_byte_count
decoded_byte_count
source_evidence.head_revision/head_blob_sha/head_byte_count
```

from membership fixtures.

The existing blob-mismatch test no longer represents a product proposition and should be removed/replaced.

### Add/retain real composition-join tests

The focused tests should explicitly protect at least:

```text
context repository mismatch → unresolved source identity
context/exact-file revision mismatch → unresolved source identity
lock path != context.source_path → unresolved source identity
declaration.project_root != exact project root → unresolved source identity
unavailable project/lock source → unresolved source identity
```

These tests protect independent composition relations rather than legacy metadata.

## 7. What Step 2C does NOT do

Do not use this migration to redesign:

```text
uv.lock structural parser duplication
versionless-record drift
--all-packages scope
include vs only environment semantics
mandatory project-content participation
not_established completeness
naming from membership to reachability
```

Those remain owned by R2–R4 / AUDIT-007.

## 8. Proof state and next action

```text
R1 Step 2B              IMPLEMENTED + STATICALLY REVIEWED / NOT EXECUTION-VALIDATED
R1 Step 2C trace        COMPLETE
R1 Step 2C code         NEXT / NOT STARTED
R2                      NOT STARTED
```

No runtime validation is claimed.

The next bounded implementation should touch only:

```text
src/upgradepilot/dependency/uv_membership.py
nearest membership tests
```

plus a caller/consumer only if static inspection proves the new contract otherwise breaks a supported normal path.
