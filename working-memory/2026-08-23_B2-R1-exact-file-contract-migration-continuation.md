# Working Memory — B2 R1 Exact-File Contract Migration Continuation

**Date:** 2026-08-23  
**Status:** ACTIVE  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Base branch:** `main`  
**Parent working record:** `2026-08-22_B2-source-evidence-and-uv-reconciliation-session.md`  
**Mode:** learning by doing and building

## Why this continuation exists

The August 22 record contains the R0 findings, retention-rule hardening, R1 design investigation, frozen minimum exact-file contract, migration branch decision, and R1 Step 1 implementation.

On August 23 Ali reported that he temporarily has no access to the WSL/laptop checkout. We therefore cannot execute the focused or full local test suite now.

This changes the **validation cadence**, not the evidence standard:

```text
small implementation step
→ static/source review
→ explicit UNVALIDATED marker
→ progressive working-memory record
→ next bounded step
→ later accumulated focused + integration + full local execution
```

No branch commit may be described as runtime-validated until that execution actually occurs. The historical full product-runtime validation point remains `bfdfd4257574f85cc3a2d094bf46a37ad6373dea` (`508 tests / OK`).

## Learning/execution discipline remains controlling

Ali explicitly requires:

1. implementation remains learning-by-doing rather than a bulk AI refactor;
2. concepts and relevant code/data-flow are taught as they become necessary;
3. progressive working memory is maintained during the migration;
4. work advances in bounded steps and must not jump across the whole migration at once;
5. Ali's reasoning is learning input, while technical/product/proof requirements remain engineering authority.

Current per-step rhythm:

```text
one responsibility
→ teach the minimum mental model
→ inspect actual code/data relation
→ make bounded change
→ inspect static diff/remaining pressure
→ record implemented vs unproven
→ continue only to the next bounded responsibility
```

## R1 Step 1 — current state

**Status:** IMPLEMENTED ON MIGRATION BRANCH; EXECUTION VALIDATION DEFERRED.

Step 1 established the strong exact repository-file owner:

```text
RepositoryTextFile
├── repository
├── path
├── revision
└── content
```

and typed unavailability:

```text
UnavailableRepositoryFile
├── repository
├── path
├── revision
├── reason
└── detail
```

Step 1 commits:

```text
709aba4cdab1fd666579f90cbe6a5e974cad8626
→ repository/provider contract

e88b1e21e3b1efd09c226b5ca1512230f6477057
→ nearest workflow-file provider tests

74fd3aaede37b15cb2eedbfda41128bc4d81f46c
→ exact-commit provider/construction tests
```

No runtime claim is attached to those commits yet.

## R1 Step 2 — dependency source provenance

### Mental model: provenance vs rebinding

A dependency transition source record answers:

> Where did this package/version transition come from, and how was it established?

It should not become a copy of every provider metadata field.

For exact base/head extraction, later code can legitimately need immutable revisions only if those revisions add a proposition not already owned by surrounding PR/context evidence.

By contrast, provider transport metadata such as blob identity and byte counts was not shown to support an independent dependency-domain proposition.

### Step 2A — narrow the shared source-evidence record

**Status:** IMPLEMENTED; EXECUTION VALIDATION DEFERRED; REVISION RETENTION REOPENED BY STEP 2B TRACE.

Commit:

```text
4ccf14aef0b473870e63eb482ba3409fe239926f
```

The intermediate Step-2A contract is:

```text
path
file_format
extraction_method
base_revision
head_revision
```

Removed:

```text
base_blob_sha
head_blob_sha
base_byte_count
head_byte_count
```

Step 2B later found that `base_revision` / `head_revision` also fail the end-to-end retention trace and should be removed in the coherent Step-2B implementation. The Step-2A commit is therefore an intermediate migration state, not the final accepted contract.

## Step 2B precondition correction — trace upstream guarantees before retaining downstream checks

During the Step 2B learning review, Ali challenged the preliminary statement that repository/path relationship checks should remain inside `uv_lock.py` and `pyproject.py`.

That challenge exposed a real review gap. The earlier reasoning correctly distinguished:

```text
intrinsic object validity
!=
relationship between objects
```

but it stopped too early. A relationship check being conceptually legitimate does **not** prove that every downstream consumer should repeat it.

The normal production route is:

```text
investigate_public_pull_request(...)
→ GitHubPullRequestClient.get_pull_request(...)
→ PullRequestIdentity(repository, base_sha, head_sha, ...)
→ GitHubPullRequestClient.get_changed_files(identity)
→ analyze_dependency_change(identity, changed_files, repository_client)
→ for one ChangedFile:
     get_pull_request_base_file(identity, changed_file.filename)
     get_pull_request_head_file(identity, changed_file.filename)
→ extract_uv_lock_changes(...) / extract_pyproject_optional_extra_change(...)
```

Therefore the ordinary product path already binds the PR, repository, changed-file path, and base/head acquisition roles before the source-specific semantic extractors run.

## Durable governance correction from the Step 2B miss

The local lesson has been promoted into stable project controls so it applies beyond exact-file validation.

### General rule

For a material cross-layer mechanism, do not decide ownership from the local file alone.

```text
1. state the exact proposition / behavior supplied by the mechanism
2. trace admitted producer → integration/orchestration → consumer flow
3. identify the earliest boundary that already guarantees the proposition
4. decide whether a later layer is an independent supported trust/public/composition boundary
5. identify the concrete failure / proof loss / material risk if the repeat mechanism disappears
6. distinguish supported alternate invocation from fixture/manual misuse
7. only then KEEP / MOVE / NARROW / REMOVE
```

This applies to checks, fields, transformations, metadata propagation, compatibility surfaces, defensive branches, and similar cross-layer mechanisms—not only validation.

### Durable owners updated

```text
AGENTS.md
→ standing safeguard: do not decide ownership file-locally

OPERATING_GUIDE.md §4.2
→ executable end-to-end responsibility-trace method

Core specification
→ JUST-004 end-to-end ownership trace
→ JUST-005 direct-call/fixture misuse is not production-boundary justification

Active reconciliation plan
→ end-to-end trace gate bound across R1–R7
```

These governance/process changes do not create product-runtime validation evidence.

## R1 Step 2B responsibility trace — COMPLETE BEFORE IMPLEMENTATION

**Trace status:** COMPLETE.  
**Source implementation status:** NOT YET PERFORMED.  
**Execution validation:** NOT AVAILABLE / NOT CLAIMED.

### Normal ownership chain inspected

```text
investigation.py
→ acquires PullRequestIdentity
→ acquires changed files from that same PR identity

dependency/analysis.py
→ is the PR-wide dependency integration boundary
→ admits supported source path/status
→ passes the same identity + same ChangedFile.filename to base/head acquisition

github/repository.py
→ base acquisition uses identity.repository + identity.base_sha + requested path
→ head acquisition uses identity.repository + identity.head_sha + requested path
→ validates returned GitHub path == requested path
→ returns strong RepositoryTextFile(repository, path, revision, content)

dependency/uv_lock.py / dependency/pyproject.py
→ source-specific semantic extraction/parsing/comparison
```

`repository_relative_parts()` is strict rather than normalizing: it rejects absolute paths, backslashes, empty components, `.` and `..`, and preserves exact spelling. Therefore `analysis.py` admission plus repository acquisition does not hide a path-normalization gap.

### Candidate 1 — base/head repository equality

**Proposition:** the two exact files compared for one transition belong to the same repository.

**Earliest sufficient owner on admitted flow:** `dependency/analysis.py` + `GitHubRepositoryClient`.

```text
same PullRequestIdentity
→ get_pull_request_base_file(identity, path)
→ get_pull_request_head_file(identity, path)
→ both acquisitions use identity.repository
```

Each resulting exact-file object also structurally validates its own repository identity.

**Independent later boundary?** No second product caller/composition route was found. Current product code calls the exact uv/pyproject extractors from `dependency/analysis.py`; other observed direct calls are tests. Module-local `__all__`/“public API” labeling does not by itself establish an external compatibility obligation.

**Decision:** REMOVE the repeated repository-equality check from `uv_lock.py` and `pyproject.py` during Step-2B implementation.

### Candidate 2 — base/head path equals ChangedFile path

**Proposition:** both acquired exact files are the same repository path GitHub reported as the changed dependency source.

**Earliest sufficient owner:** `dependency/analysis.py` + repository provider.

```text
analysis.py admits ChangedFile.filename structurally/semantically
→ same exact filename is passed to both base/head acquisition methods
→ repository provider requires returned GitHub path == requested path
→ RepositoryTextFile preserves that normalized repository-relative path
```

Because `repository_relative_parts()` is strict and spelling-preserving, the path is not silently collapsed into a different value between admission and acquisition.

**Independent later boundary?** No admitted second product composition route found for the extractors.

**Decision:** REMOVE repeated base/head-vs-ChangedFile path equality checks from the source-specific extractors.

### Additional finding — source path/status admission is duplicated too

The same trace exposed another file-local duplication:

```text
analysis.py
→ checks uv.lock / pyproject.toml role
→ checks modified status
→ only then acquires exact files and calls extractor

extractor
→ checks role/status again
```

This is the same ownership issue, not a separate safety proof. Under the current admitted product route, `analysis.py` is the integration/admission owner and the exact-file extractors are semantic consumers.

**Implementation direction:** Step 2B should remove or narrow these repeated admission guards as part of making the extractor contract match its real semantic responsibility. Do not retain them solely because direct unit tests currently call the extractor with arbitrary `ChangedFile` objects.

### Candidate 3 — `base_revision` in DependencyChangeSourceEvidence

**Originally claimed proposition:** preserve the exact historical base snapshot used to establish the old version.

**Trace findings:**

- `PullRequestIdentity.base_sha` already owns the PR base snapshot.
- exact base `RepositoryTextFile.revision` owns the revision while semantic parsing occurs.
- `PublicPullRequestInvestigation` preserves `pull_request`, and CLI already prints the PR base SHA before dependency source details.
- no current downstream product semantic consumer of `DependencyChangeSourceEvidence.base_revision` was found.
- patch-derived requirements evidence uses the same PR transition context but carries no base/head revision fields, showing that the dependency source record is not the owner of a self-contained PR snapshot identity.

**Decision:** REMOVE `base_revision` from `DependencyChangeSourceEvidence` in the coherent Step-2B implementation. Step 2A’s retention was an intermediate conclusion superseded by this end-to-end trace.

### Candidate 4 — `head_revision` in DependencyChangeSourceEvidence

**Originally claimed proposition:** preserve/rebind the exact HEAD snapshot used by later environment evidence.

**Trace findings:**

- `PullRequestIdentity.head_sha` already owns PR HEAD.
- `dependency/analysis.py::_source_contexts()` builds `UvLockDependencyContext.revision` directly from `identity.head_sha`.
- later uv membership already compares supplied exact project/lock file revisions to `context.revision`.
- its additional comparison `evidence.head_revision == context.revision` therefore re-proves a value copied from the same PR identity rather than establishing a new proposition.
- CLI already prints PR HEAD from `PullRequestIdentity`; per-source HEAD printing is duplicate presentation.

**Decision:** REMOVE `head_revision` from `DependencyChangeSourceEvidence` in Step 2B. In Step 2C, remove the now-unjustified `evidence.head_revision` rebinding check from `uv_membership.py` while preserving genuinely independent context↔project/lock relations.

### Resulting smallest dependency-source provenance contract

The Step-2B trace now supports:

```text
DependencyChangeSourceEvidence
├── path
├── file_format
└── extraction_method
```

Meaning:

```text
path
→ which dependency source inside the already-owned PR context established the fact

file_format
→ which admitted source semantics were interpreted

extraction_method
→ which evidence method established the transition
```

PR base/head identity remains owned once by `PullRequestIdentity`; exact file locator/revision remains owned by `RepositoryTextFile` while parsing; exact-head downstream dependency context remains owned by `DependencySourceContext` variants where later composition genuinely needs it.

### Important contrast for Step 2C

The exact-file extractors receive evidence assembled through one controlled integration route. `uv_membership.py`, by contrast, accepts a dependency context, a workflow-derived declaration, an exact project file, and an exact lock file that represent **separate evidence branches being composed**.

Therefore Step 2C must not mechanically delete every relation check. It should remove provider/redundant propagation checks but keep cross-branch repository/revision/path/project-root relations that genuinely establish the composition proposition.

This contrast is an important learning checkpoint:

```text
same relation-looking code
+
different composition boundary
→ different ownership decision
```

## Superseding current position after the completed trace

The earlier “Step 2B responsibility review reopened” state is now superseded by:

```text
R0                  COMPLETE
R1 design           FROZEN, with Step-2A revision retention corrected by trace
R1 Step 1           IMPLEMENTED / NOT EXECUTION-VALIDATED
R1 Step 2A          INTERMEDIATE IMPLEMENTATION / revision fields now scheduled for removal
R1 Step 2B trace    COMPLETE
R1 Step 2B code     NEXT, NOT STARTED
R1 Step 2C          NOT STARTED
R2                  NOT STARTED
```

### Exact next implementation boundary

If/when Step 2B implementation is selected, keep it bounded to:

```text
src/upgradepilot/dependency/change.py
src/upgradepilot/dependency/uv_lock.py
src/upgradepilot/dependency/pyproject.py
nearest affected tests/fixtures
```

Goals:

1. finish `DependencyChangeSourceEvidence` as `path + file_format + extraction_method`;
2. migrate uv/pyproject exact-file extractors to the strong `RepositoryFileEvidence` contract;
3. remove provider metadata and upstream-owned PR-binding revalidation;
4. preserve exact-file availability handling and actual uv/pyproject semantic parsing/comparison;
5. update source orientation/comments so extractor preconditions and ownership are explicit;
6. do not touch `uv_membership.py` until Step 2C.

No source implementation should be described as validated until the deferred local test ledger is actually executed.
