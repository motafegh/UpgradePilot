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

For exact base/head extraction, later code can legitimately need the immutable revisions because they participate in real joins:

```text
changed dependency was established from HEAD revision H
+
later exact uv.lock is also revision H
→ both evidence objects refer to the same historical repository side
```

That is **rebinding/relationship evidence**.

By contrast:

```text
head_blob_sha
head_byte_count
```

were not shown to support an independent dependency-domain proposition. A downstream use of them that is itself under review is not sufficient retention proof.

### Step 2A — narrow the shared source-evidence record

**Status:** IMPLEMENTED; EXECUTION VALIDATION DEFERRED.

Commit:

```text
4ccf14aef0b473870e63eb482ba3409fe239926f
```

`src/upgradepilot/dependency/change.py` now models `DependencyChangeSourceEvidence` as:

```text
path
file_format
extraction_method
base_revision   # optional: exact-file method only
head_revision   # optional: exact-file method only
```

Removed from this domain record:

```text
base_blob_sha
head_blob_sha
base_byte_count
head_byte_count
```

Why revisions remain:

- they identify the historical base/head side used by exact-file extraction;
- later dependency/environment evidence may need to bind another exact file to that same immutable side.

Why blob/count metadata does not:

- no current admitted dependency proposition requires independent Git blob identity;
- provider transport/resource checks are already owned at acquisition;
- carrying provider byte metadata forward does not add dependency meaning.

### Deliberate Step 2A boundary

Step 2A changed the **shared contract only**. It intentionally did not yet migrate the exact-file constructors or uv membership consumer.

Therefore the migration branch is expected to have temporary call-site pressure until the next substeps are completed. This is acceptable on the isolated migration branch and must not be interpreted as a green or complete product state.

## Step 2B precondition correction — trace upstream guarantees before retaining downstream checks

**Status:** REVIEW CORRECTION RECORDED BEFORE IMPLEMENTATION.

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

Therefore the ordinary product path already binds:

```text
same PullRequestIdentity
→ same repository

same ChangedFile.filename supplied to both acquisitions
→ same requested repository path

base/head acquisition methods
→ identity.base_sha / identity.head_sha
```

The strong `RepositoryTextFile` then owns structural validity of the resulting repository/path/revision/content object.

### What was missed

The preliminary Step 2B reasoning classified repository/path comparisons as `relational/rebinding validation` and treated that category as enough to retain the checks locally.

That was incomplete. The necessary additional question is:

> Has the normal upstream construction/integration path already established this relationship, and is the downstream function an independent trust boundary that must defend arbitrary independently assembled arguments?

Without that question, a valid relationship can still be redundantly checked in the wrong layer.

This was not merely a later scheduled discovery. If Ali had not challenged it, the existing Step 2B framing created a real risk that the redundant repository/path checks would have been preserved. Passing tests would likely not expose this because redundant checks normally pass on the production route.

### New mandatory retention-review sequence for this reconciliation

Before retaining any downstream validation/rebinding check:

```text
1. state the exact proposition the check establishes;
2. trace the normal production producer/caller chain end to end;
3. identify the earliest boundary that already establishes that proposition;
4. inspect whether the downstream function is a real independent trust/public boundary
   or an internal semantic consumer of already-bound evidence;
5. retain a repeat check only if an independent responsibility/risk still requires it;
6. direct-call/test convenience is migration pressure, not retention authority.
```

This is the concrete operational form of the existing `JUST-*` retention rule for validation ownership.

### Step 2B scope is reopened, not yet implemented

Do **not** currently assume these survive in `uv_lock.py` / `pyproject.py`:

```text
base_file.repository == head_file.repository
base_file.path == changed_file.filename
head_file.path == changed_file.filename
```

They must first pass the upstream-guarantee / independent-boundary review above.

Likewise, `base_revision` / `head_revision` retention in `DependencyChangeSourceEvidence` remains implemented from Step 2A but is still open to later necessity pressure if the downstream rebinding proposition can be established more simply.

## Exact next bounded step

### Step 2B — finish responsibility-boundary investigation before editing constructors

Inspect and decide, in this order:

```text
investigation.py
→ dependency/analysis.py
→ github/repository.py
→ dependency/uv_lock.py
→ dependency/pyproject.py
```

For each candidate retained check/fact, answer:

```text
what proposition does it establish?
where is that proposition first guaranteed on the normal product path?
is this downstream function independently responsible for distrust/rebinding?
what real failure remains possible if the duplicate check is removed?
```

Only then modify:

```text
src/upgradepilot/dependency/uv_lock.py
src/upgradepilot/dependency/pyproject.py
```

Do not alter uv-lock semantic parsing or pyproject optional-dependency semantics in this substep.

After Step 2B, inspect remaining `uv_membership.py` pressure separately as Step 2C.

## Deferred execution-validation ledger

When WSL/laptop access returns, validation must be accumulated in order rather than represented as one opaque final run:

```text
Step 1 provider/type focused tests
→ Step 2 dependency extraction/provenance focused tests
→ later Target/upstream focused tests as migrated
→ nearest integration tests
→ full deterministic suite
```

Failures must be diagnosed against the earliest relevant bounded step; do not simply patch until the final suite turns green.

## Current proof state

```text
R0                  COMPLETE / historical reviewed state
R1 design           FROZEN
R1 Step 1           IMPLEMENTED / NOT EXECUTION-VALIDATED
R1 Step 2A          IMPLEMENTED / NOT EXECUTION-VALIDATED
R1 Step 2B          RESPONSIBILITY REVIEW REOPENED BEFORE EDIT
R2                  NOT STARTED
```

Do not mark R1 complete or start R2 until the migration is coherent and actual execution evidence is recorded.
