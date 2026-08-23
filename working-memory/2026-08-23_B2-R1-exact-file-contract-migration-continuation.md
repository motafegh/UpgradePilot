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

## Exact next bounded step

### Step 2B — migrate exact dependency-source constructors

Inspect and change only:

```text
src/upgradepilot/dependency/uv_lock.py
src/upgradepilot/dependency/pyproject.py
```

Goals:

1. consume the strong `RepositoryTextFile` contract rather than revalidating removed provider fields;
2. preserve real relations:
   - base/head repository equality;
   - base/head path equals the changed-file path;
   - base/head immutable revisions retained in `DependencyChangeSourceEvidence`;
3. construct the new narrow dependency provenance record;
4. do not alter uv-lock semantic parsing or pyproject optional-dependency semantics in this substep.

After Step 2B, inspect the remaining `uv_membership.py` pressure separately as Step 2C rather than silently folding it into parser changes.

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
R1 Step 2B          NEXT
R2                  NOT STARTED
```

Do not mark R1 complete or start R2 until the migration is coherent and actual execution evidence is recorded.
