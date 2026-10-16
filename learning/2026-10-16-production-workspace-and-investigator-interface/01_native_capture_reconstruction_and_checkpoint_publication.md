# Production native capture, reconstruction and checkpoint publication

**Educational snapshot:** repository horizon **`5187f40ba974341eb29d765363f093922a881803`**, 2026-10-16. Product `src/` and `tests/` at this horizon retain the verified production Workspace native-foundation implementation. The strongest combined Stage 1–2 publication-order proof was recorded at `4f502989`, with later product work preserving these responsibilities. This note explains implemented production behavior; it does not claim learner mastery or close the independently tracked Stage 1–2 D/E ownership work.

**Responsibility:** understand how UpgradePilot preserves domain-owned native investigation facts across restart without rerunning their producers/evaluators, and how those retained facts become immutable Workspace revisions in a local SQLite checkpoint.

## Core mental model

The production path is deliberately one-way:

```text
normal native producer/evaluator runs once
        ↓
NativeInvestigationCapture
retains exact inputs + typed owner result + explicit gaps
        ↓
owner/family-specific versioned encoding
        ↓
CapturedNativeBoundary
        ↓
CheckpointRevision
immutable lineage / revision / predecessor identity
        ↓
CheckpointStore
coherent local SQLite publication
        ↓
fresh-process read + supported native reconstruction
        ↓
CI/runtime or Python-support native projection
```

The central boundary is:

```text
historical reconstruction
!= provider acquisition
!= source parsing
!= native reevaluation
!= fresh synthesis
!= continuation authority
```

The native/domain owner still owns what its result means. Workspace capture owns preservation and composition of the already-earned result and its material basis. The storage adapter owns persistence integrity and publication ordering. None of those layers may silently become another CI, runtime, impact or action evaluator.

The accepted method is [ADR-0013](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md). It rejects arbitrary class-tag hydration, current-default substitution and producer reruns as recovery mechanisms.

## 1. Capture happens while normal orchestration still owns the material

Start with [`NativeInvestigationCapture`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/native_capture.py).

The normal product path already has transient inputs that later consumers may need but the legacy final result does not retain completely. Examples include dependency source contexts, workflow definitions, workflow jobs and CI preparation inputs. Capture therefore occurs at those existing composition boundaries before local values disappear.

`NativeInvestigationCapture.start(...)` first establishes one exact investigation target and records the shared investigation inputs:

```text
PullRequestIdentity
changed files
dependency result
source contexts
```

It then creates explicit placeholders for the supported native families that have not run yet.

That distinction matters:

```text
not_evaluated
!= empty evidence
!= negative evidence
!= failed evaluation
```

For example, `ci_inputs` begins as an empty tuple with outcome `not_evaluated`; other result families begin as their explicit unevaluated representation. When a native owner later runs, capture replaces that family with the actual encoded result and binds it to the exact captured input record IDs.

The capture object itself does **not**:

```text
fetch evidence
run an evaluator
retry work
publish SQLite
synthesize a maintainer action
```

Its job is narrower: preserve what the existing product owners actually produced.

### Partial versus completed capture

`partial_snapshot()` returns the current coherent native progress without claiming the whole normal investigation completed.

`complete()` plus `snapshot()` seals only after normal orchestration reaches its completion boundary.

This lets Workspace publication preserve useful intermediate truth without inventing later work. An unevaluated family can move to new input identities as upstream material changes, while an already executed result keeps the exact input records it was actually evaluated against. Rebinding an old result to new inputs is forbidden; a native owner must produce a successor result.

That gives an important invariant:

> **Executed native meaning is historical and input-bound. New premises require a new owner result, not metadata surgery on the old one.**

## 2. Native codecs preserve owner meaning; they do not create it

Open [`native_codecs.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/native_codecs.py).

The initial production family table is explicit. Each family declares:

```text
owner
admitted representation shape
immediate input families
supported codec version
```

The first admitted closure includes investigation inputs, CI inputs/coverage/runtime state, upstream authority/support-drop material and the Python-support target/relevance/assessment chain.

The codec table deliberately does **not** discover arbitrary Python classes or dataclass fields at runtime. Version 1 support is fixed and reviewable. Unknown family/version combinations raise `unsupported_native_codec`.

This is different from generic serialization:

```text
bytes can be readable
but
reader support for their semantic family/version can still be absent
```

Likewise, codec version is representation compatibility, not a guessed producer semantic version. Where the original producer interface did not expose a stable version, capture records that gap explicitly rather than filling it with the current implementation version.

### Why fixed layouts matter

A later dataclass field can change meaning even if old JSON remains syntactically valid. Production tests therefore independently compare admitted layout fields with their constructors and refuse silent drift. A new native field requires a deliberate compatibility decision rather than being populated from today's default.

So:

```text
successful JSON parse
!= supported native reconstruction
```

## 3. Reconstruction validates material bindings before exposing typed values

The supported projection owner is [`native_projection.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/native_projection.py).

The two initial typed consumer projections are:

```text
CINativeProjection
PythonSupportNativeProjection
```

Reconstruction first validates the retained boundary and then checks family-specific relationships such as:

- exact target identity;
- retained changed-file membership;
- dependency source provenance;
- source-context repository/revision/package scope;
- exact native input-record references;
- recorded versus `not_evaluated` consistency;
- workflow/run/job/definition relationships;
- project-environment source bindings;
- CI/runtime correlation references;
- upstream/target/impact relationships.

Only after those checks does it expose the decoded owner values.

The projection layer does **not** re-run source parsers, CI evaluators, impact evaluators, providers or synthesis. It validates retained representation and relationships needed for the supported historical projection.

A useful rule is:

```text
reconstruction asks:
"What did the admitted historical owner record, and is its retained material coherent?"

reconstruction does not ask:
"What would today's owner conclude if we ran it again?"
```

### `not_evaluated` remains a first-class historical state

A record marked `not_evaluated` must contain the exact unevaluated representation for that family. If it contains an evaluated typed value, reconstruction refuses it as invalid material.

Conversely, a recorded family normally requires its immediate required inputs to have been recorded. Production has only specifically admitted exceptions where the historical product semantics really allow one operation to remain unexecuted.

This prevents a checkpoint from strengthening incomplete history merely because its bytes look structurally plausible.

## 4. Real cold-reconstruction proof forbids semantic re-entry

[`test_workspace_native_reconstruction.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/tests/test_workspace_native_reconstruction.py) does more than test an encode/decode round trip.

Its normal path first runs existing product owners once under controlled evidence, captures their actual native material, then starts a fresh child process for recovery. The child installs an execution guard covering provider, investigation, CI/runtime, impact, target, upstream, synthesis and common external-model/network entry points.

The recovered process may perform representation-only constructors and validation. It may not call the original semantic owners.

Four actual negative controls prove the guard is live by deliberately attempting entry into:

```text
GitHub repository acquisition
model-bound support-drop evaluation
runtime dependency-state evaluation
maintainer-action synthesis
```

Each is blocked.

The test then compares the complete recovered supported projections against an independent test-only representation of the original native values.

This proves something stronger than "JSON round-tripped":

> **the supported historical native consumer values can be reconstructed in a fresh process without reacquisition or reevaluation.**

It still does not prove those historical results are currently fresh, adequate or action-authorizing.

## 5. Immutable revision identity is distinct from native truth

[`CheckpointRevision`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/checkpoint_revision.py) binds:

```text
lineage_id
revision_id
predecessor_id
captured native boundary
optional lifecycle history
```

Its digest binds the header identity to the complete ordered encoded material.

That digest is an integrity/identity mechanism. It does **not** mean the retained native proposition is true today.

Keep these separate:

```text
revision digest
→ did these declared bytes/identities remain intact?

native owner result
→ what historical domain result was recorded?

current validity/authority
→ later responsibilities, not established by the digest
```

An existing native-only revision and a later revision carrying lifecycle history also remain distinguishable. Missing lifecycle history means `not_retained`; it is not silently converted into an empty recovered lifecycle.

## 6. `CheckpointStore` publishes one coherent immutable successor

Open [`checkpoint_store.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/checkpoint_store.py).

The store is a host-owned local SQLite persistence adapter. Its public contract uses typed checkpoint values; SQL stays private.

The supported storage settings are explicitly validated:

```text
SQLite WAL
synchronous FULL
foreign keys ON
bounded writer wait
owner-only local files outside Git
supported schema version
```

The engine settings are implementation requirements for this admitted store. They are not themselves proof of device/power-loss durability.

### Publication transaction

`publish(...)` validates the staged revision, establishes the retained lineage history, verifies the expected predecessor, inserts immutable payloads/records/references/revision membership, validates the newly stored revision through the normal read path, advances the lineage head and commits.

Earlier material is immutable. Reusing one exact record identity with changed bytes is rejected. Payload bytes may be shared when their digest matches, but scoped record identity remains separate.

The publication predecessor means:

> **which retained revision this writer is extending.**

It does not mean:

> **whether the old assessment is still evidentially valid now.**

Material validity is a later Stage 3 responsibility.

### Competing writers

Publication uses an expected predecessor and conditional head advancement. Two writers do not silently merge or overwrite each other. A stale writer receives `publication_conflict`.

A genuinely empty lineage with the wrong root predecessor is also a conflict. A lineage whose retained structural history is damaged is instead invalid storage; it must not masquerade as an ordinary concurrent-writer conflict.

That classification was important enough to earn a later dedicated publication-order repair and negative control.

## 7. Commit acknowledgement is not exactly-once execution

A publication receipt is returned only after commit.

If commit may have happened but acknowledgement is lost, `UnconfirmedPublication` carries the staged lineage/revision identity so the caller can inspect the store and reconcile that exact publication.

The correct response is **not**:

```text
"I did not see the receipt, so publish again."
```

Instead:

```text
commit may have happened
→ inspect staged identity
→ determine published/not published/refused
```

This solves storage publication uncertainty only. It does not establish exactly-once provider/model/capability effects and does not grant retry authority for external work.

That distinction later becomes central to lifecycle execution truth.

## 8. Reading a historical revision discloses later progress

A cold reader selects one exact lineage/revision/target.

The store validates the declared revision and returns a `StoredCheckpoint` containing:

```text
selected historical revision
current observed lineage head
excluded_successor_ids
```

So opening an earlier revision does not pretend later published progress never existed.

This is a useful recovery property:

```text
recover revision R2 intentionally
while head is R5
→ R2 stays R2
→ R3/R4/R5 remain disclosed as excluded later progress
```

There is no automatic fallback that silently combines histories or substitutes a newer revision.

## 9. Validated backup is a Workspace operation, not file copying

The production store uses SQLite's online backup API into a new destination and validates the copied schema, lineages, revisions and retained material before acknowledging success.

The source remains intact on backup failure. A failed new destination is cleaned up only within the new owned destination.

This is intentionally different from copying only `workspace.sqlite3`, especially when committed WAL state exists.

Initial retention has no pruning/expiry API. Every declared revision/material closure remains retained for the local investigation under this first contract. The cost is accepted initially so recovery semantics are clear before any later compaction policy.

## 10. Checkpoint versus saved report

A saved report and a Workspace checkpoint serve different responsibilities.

A saved report is a durable presentation/output artifact. It does not retain the complete native input closure, owner records, revision lineage and lifecycle material required for canonical recovery.

A Workspace checkpoint is recovery state:

```text
native premises/results
+ exact historical bindings
+ revision identity/history
+ retained lifecycle where supported
```

Therefore:

```text
saved report
!= Workspace recovery input
```

and:

```text
opening a checkpoint
!= regenerating a report or fresh synthesis
```

Fresh synthesis remains a separate admitted evaluation operation.

## 11. Refusal states are part of correctness

The implementation is intentionally conservative. Important refusal classes include:

| Refusal / state | Meaning |
| --- | --- |
| `unsupported_native_codec` | This family/version is not an admitted decoder contract. |
| `unsupported_native_semantic_version` | Historical producer-version meaning is not admitted for reconstruction. |
| `missing_native_material` | Required retained inputs/results are absent or substituted. |
| `wrong_target` | Material belongs to another exact investigation scope. |
| `invalid_native_material` | Retained relationships/representation contradict the admitted contract. |
| `native_resource_limit` | Encoded representation exceeds bounded parser/encoder capacity. |
| `publication_conflict` | Writer's expected predecessor differs from the coherent current lineage. |
| `unconfirmed_publication` | Commit/acknowledgement outcome needs identity reconciliation. |
| `unsupported_storage_schema` | Store layout/version is outside admitted support. |
| `invalid_checkpoint_storage` | Retained database structure/material is damaged or inconsistent. |
| `storage_resource_limit` | Stored encoded material exceeds supported read/publication capacity. |
| `storage_busy` / `storage_read_only` / `storage_full` | Storage could not admit the publication; no semantic retry is implied. |

A readable checksum does not override one of these failures.

## 12. Important engineering corrections

The implementation history is useful because it shows what the proof boundary actually required.

### Test fixtures can be wrong without product behavior being wrong

Early storage controls produced failures because some fixtures did not trigger the intended state:

- identical payload bytes meant an "after payload insert" kill point was never reached;
- one duplicate-revision fixture accidentally used itself as predecessor and correctly failed earlier;
- a WAL test held a connection but not a real read transaction, so its expected WAL state was not actually preserved.

The fixtures were corrected rather than weakening the product checks.

**Lesson:** a failed test only becomes product evidence after verifying the test actually created the intended system state.

### Later audit found real storage defects

Independent review then found genuine problems around absence classification, validating older retained material before successor publication, and safe initialization cleanup. Those were repaired with discriminating failing controls first.

The important ownership lesson is not the exact SQL patch. It is:

```text
coherent head alone
!= coherent retained lineage
```

A new successor extends retained history. If an older declared revision in that lineage is corrupt, publishing a new successor would falsely bless a broken recovery chain.

### Publication-order repair separated corruption from concurrency

A final follow-up showed structural-history validation needed to occur before predecessor-conflict classification. Otherwise a missing head in a nonempty lineage could appear to be an ordinary stale-writer conflict.

The repaired rule is:

```text
first establish coherent retained lineage/history
then compare expected predecessor
then publish successor
```

This is a general engineering lesson: **error classification is part of the contract**. Returning the wrong failure category can encourage an unsafe retry even when no bytes were silently accepted.

## 13. Strongest Stage 1–2 proof and its limits

The final publication-order verification at `4f502989` recorded:

- **132 focused tests PASS**, including storage, durable reconstruction, native reconstruction and nearby product owners;
- **833/833 checkout tests PASS**;
- **833/833 fresh noneditable installed tests PASS** in a newly created isolated virtual environment;
- all **87 installed/source product Python hashes matched**;
- `pip check`, installed CLI/module help, Ruff/format and dependency-direction checks passed;
- a parent-source negative control reproduced the old publication-order defect while current source passed.

[`test_workspace_checkpoint_reconstruction.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/tests/test_workspace_checkpoint_reconstruction.py) proves the composed recovery boundary in fresh processes. The child receives only the host-owned store plus explicit lineage/revision/target selection; network and provider/model/evaluator/synthesis entry are guarded. Normal positive/problem/unresolved/not-evaluated variants and validated backups are covered.

This evidence establishes the admitted Stage 1–2 responsibility. It does **not** establish:

```text
complete native-family coverage
full canonical lifecycle/report recovery
current material validity
current action authority
user-facing continuation
retry/replay
exactly-once external effects
device/power-loss durability
semantic accuracy/adequacy
Investigator usefulness
```

Those remain other owners/stages.

## 14. What to own versus what to look up

### Must master / own

- native semantic owner versus capture/storage responsibility;
- `not_evaluated` versus empty/negative;
- historical result/input binding;
- explicit family/version decoder authority;
- reconstruction versus reevaluation;
- immutable revision/predecessor meaning;
- publication conflict versus invalid retained history;
- commit acknowledgement uncertainty;
- checkpoint versus saved report;
- recovery proof versus current authority/continuation.

### Understand operationally

- fixed native layout tables and input-record references;
- cold projection validation sequence;
- immutable SQLite payload/record/revision membership;
- WAL/FULL/foreign-key settings and their bounded role;
- resource limits and refusal behavior;
- online backup plus validation.

### Lookup level

- exact JSON tags and all native variants;
- every SQL table/column/trigger;
- every corruption fixture and process-kill position;
- incidental SQLite API syntax.

### Deferred deliberately

- complete Stage 4 family expansion;
- direct synthesis/report migration;
- user-facing continuation/replay;
- pruning/schema migration;
- stronger device/power-loss guarantees.

## Fast relearning route

When returning later, do this instead of rereading everything:

1. Reconstruct the mental model: **owner result → capture → codec → boundary → revision → store → cold projection**.
2. Open `NativeInvestigationCapture.partial_snapshot()` and explain why unevaluated families have explicit records.
3. Open `FAMILY_CONTRACTS` and one projection `_decode(...)` path; explain why a readable payload can still be unsupported.
4. Open `CheckpointStore.publish(...)`; distinguish lineage coherence, predecessor conflict, commit and receipt.
5. Inspect one durable cold-reconstruction test and state which executions are forbidden.
6. Finish by listing three non-claims: **fresh semantic truth, continuation authority, power-loss durability**.

## Transfer questions

1. If a CI result was produced against input record IDs A/B/C, why is it wrong to update its references to D/E/F after new evidence arrives without rerunning the CI owner?
2. If a checkpoint payload parses successfully but its codec version is unsupported, what may remain inspectable and what must reconstruction refuse?
3. Why must a nonempty lineage with damaged/missing retained structure be classified differently from a coherent lineage whose head simply differs from a writer's expected predecessor?
4. A process is killed after SQLite commit but before UpgradePilot receives its publication receipt. What should the caller do, and what must it **not** infer about external effects?
5. Why can a saved report remain perfectly valid as a historical output while still being insufficient as the canonical Workspace recovery input?

## Primary anchors

- [ADR-0013 — versioned native reconstruction and Workspace checkpoint storage](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md)
- [`native_capture.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/native_capture.py)
- [`native_codecs.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/native_codecs.py)
- [`native_projection.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/native_projection.py)
- [`checkpoint_revision.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/checkpoint_revision.py)
- [`checkpoint_store.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/checkpoint_store.py)
- [`test_workspace_native_reconstruction.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/tests/test_workspace_native_reconstruction.py)
- [`test_workspace_checkpoint_reconstruction.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/tests/test_workspace_checkpoint_reconstruction.py)
- [Stage 1–2 implementation/proof record](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/working-memory/2026-10-10_1552_workspace-native-capture-reconstruction-and-publication_lbd-cycle.md)

The Oct 9 Workspace research package remains useful for understanding why these methods were selected. This note is the production successor: it teaches what the product implementation actually does at the pinned horizon.

`UP-SKILL:upgradepilot-learning-artifact`
