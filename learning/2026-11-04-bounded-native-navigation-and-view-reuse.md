# Bounded native navigation: evidence views, delivery and recovery

**Snapshot:** November 4, 2026. The consumer repair entered at `6e98d0a0`; the additional publication reuse is at `38741c3c`. Product/test teaching uses `38741c3c`, which includes both. The original failed qualification is preserved at `068ba7b4`. This is one focused study note, not live project state or execution authority. The [cycle](../working-memory/2026-11-04_caller-signature-connected-retained-qualification_cycle.md) preserves engineering progression; [MEMORY.md](../MEMORY.md) owns continuation.

Repository links below are navigation aids. For frozen reconstruction or a later derived lesson, resolve source/tests at `38741c3c` (for example, `git show 38741c3c:src/upgradepilot/workspace/consumer_access.py`). Later qualification evidence is separately dated; it does not silently replace the pinned source.

## Start with the real problem

UpgradePilot had already acquired and analyzed retained HTTPX-related source. The ordinary case retained 24 files and produced one target root with four native old/proposed witnesses. The application saved its report and Workspace; the report and original source opened offline.

Then a different consumer tried reading the structured native evidence in pages. Six pages succeeded. The next page refused:

```text
storage_resource_limit: Original-basis closure exceeds read capacity.
```

The six page bodies contained only 24,576 characters. Why could such small responses exhaust a 64 MiB allowance? Because the allowance counted more than the displayed text: it included the original material needed to recover the retained interaction history.

The important debugging move was to identify the affected relationship. Missing native old/proposed evidence in the earlier acquisition attempt had required restoring the accepted four-adapter allocation. Here that evidence was already present and report delivery worked. The failure belonged to consumer/view/publication/recovery composition. Changing the argument checker would not repair it.

## Four things that must stay distinct

| Concept | Meaning here | What it does not establish |
|---|---|---|
| Native evidence | Owner-produced structured calls, signatures, paths, local comparisons and premises | Installed versions, actual dispatch or executed target calls |
| ConsumerView | A retained description of offered native material and omissions at an exact basis | That every offered byte was actually delivered or examined |
| ViewDelivery | One actual response, its exact content, purpose, method and view reference | That the recipient used it correctly or gained action permission |
| Original material basis | The frozen native boundary against which a historical interaction was recorded | Present authorization or present validity merely because it is retained |

The **recovery closure** is the selected revision plus the original bases required to reconstruct and validate its retained history. A digest or reference alone cannot replace the evidence content needed for those checks.

Think of a view as a precisely attributed evidence menu. Each page response is its own delivery receipt. Several deliveries can refer to the same unchanged menu. Reusing the menu does not merge the receipts or make repeated information independent support.

## Trace the failure through the real owners

The bounded consumer is [WorkspaceEvidenceAccess](../src/upgradepilot/workspace/consumer_access.py). Its `native_page` method selects one registered native record, validates the retained family, takes a bounded character range and constructs a JSON response containing the record identity/digest, range, exact text and next cursor.

Before the repair, its delivery helper always did:

```python
view = host.prepare_view(...)
host.deliver_view(..., view.view_id, ...)
```

The [host](../src/upgradepilot/workspace/lifecycle_host.py) published a new ConsumerView and then a separate ViewDelivery. Each new view had an original basis tied to that view publication. Deliveries retained the same original basis as their view.

Repeated paging therefore accumulated distinct basis references even while the native evidence remained unchanged:

```text
page 1 → view V1 / basis B1 → delivery D1
page 2 → view V2 / basis B2 → delivery D2
page 3 → view V3 / basis B3 → delivery D3
```

The [checkpoint reader](../src/upgradepilot/workspace/checkpoint_store.py) reconstructs referenced bases separately. `_composed_material_size` conservatively counts native material and lifecycle bodies for each distinct referenced revision. Existing investigation history already consumes part of the budget before the first page.

SQLite shares immutable stored records within the lineage. The recovery admission calculation still charges the composed material of each distinct basis. Database file size, delivered text length, encoded recovery accounting and actual Python heap usage are different measurements.

Three limits were relevant:

| Limit | Responsibility |
|---|---|
| 256 KiB full native view | Admit or explicitly omit a complete offered payload |
| 4,096 characters per page | Bound one native text slice; characters are not always UTF-8 bytes |
| 64 MiB recovery closure | Bound encoded material accounted for when reconstructing referenced bases |

A small page does not guarantee a small recovery closure. Conversely, crossing the full-view limit can legitimately lead to paging without implying an analysis failure.

## Why the refusal preserved earlier progress

`CheckpointStore.publish` validates a proposed revision through the same reader before `COMMIT`. The resource refusal occurred during that validation. The failed page was not acknowledged as delivered.

The original six deliveries and last acknowledged navigation revision remained readable. The failed navigation used a validated backup, leaving the successful acquisition/report store untouched. Recovery did not invent a page, retry acquisition, regenerate analysis or select another head.

This is an important distinction when reading errors: a failed operation can leave valid earlier state. A lost acknowledgement would require exact publication inspection; it must not be casually relabelled as known absence.

## The repair and why it belongs in the consumer

The consumer knows it is requesting repeated bounded responses from a fixed offered universe. The existing host already supports multiple deliveries referring to one valid view. The lifecycle reader already verifies their shared basis/reference relationship. Neither the schema nor the storage admission method needed a new meaning.

The repaired flow is:

```text
unchanged native boundary + same selection + currently valid view
    → view V / basis B
        → delivery D1 with page 1
        → delivery D2 with page 2
        → delivery D3 with page 3
```

The consumer keeps an in-memory dictionary. Its key is the exact tuple of selected native record IDs. Its value holds a complete native boundary and the acknowledged view ID.

The essential condition is:

```python
boundary, view_id = self._views.get(native_ids, (None, None))
if (
    boundary != current.boundary
    or view_id is None
    or self.host.current_validity(view_id).status != "valid"
):
    # Prepare and retain a fresh view, then remember it for this selection.
    ...
```

The `or` conditions short-circuit: there is no validity lookup for a missing view ID. Tuple keys distinguish native selections; returning to the same selection can reuse its own valid view. The dictionary is scoped to one access instance, rather than shared globally across investigations.

`boundary != current.boundary` compares native material, not the logical Workspace revision ID. A page delivery advances lifecycle history and creates a new logical revision while leaving the native boundary equal. That is exactly the situation where reuse is useful.

Full boundary equality is deliberately stronger than the host's material-validity test. An old view may still have valid referenced material after an unrelated addition or reordering. A newly requested offered/omitted universe should reflect the new boundary. The consumer therefore creates a fresh view when that complete boundary changes, even if the older view remains historically valid.

The host still checks purpose, scope, installed method and current material validity on each operation/delivery. A cached view is not permission to bypass those checks. Withdrawing the method blocks access after the cache has been populated.

Every response still receives a new delivery ID and exact retained content. Source citations remain bound to the specific delivery that actually contained the cited line. Sharing a view cannot make a line delivered in D1 count as delivered in D2.

The cache is absent from the persisted format. Cold opening reconstructs historical records without restoring execution authority. A separately authorized consumer session starts with an empty cache.

## A second cache with a different responsibility

The publication refinement was selected only after a separate count-based experiment. One real retained page caused156 original-basis decodes for15 distinct transaction/basis pairs, with one pair decoded27 times. That is evidence of repeated work, independently of any disputed elapsed-time interpretation.

Publication checks all historical revisions. Before the refinement, each such check decoded shared original bases again. The same locked SQLite transaction guarantees those original rows remain unchanged while that publication is checked. The store can therefore reuse their already decoded immutable boundaries within that transaction.

| Cache | Key and validity | Lifetime | What still happens |
|---|---|---|---|
| Consumer view reuse | Selected IDs, equal complete native boundary, current host validity | One access instance | A distinct exact delivery and present permission checks per response |
| Original-basis decoding reuse | Lineage and original revision in one locked database snapshot | One publication transaction | Every historical root, ancestry, size charge, digest and lifecycle relationship still validates |

`_OriginalBasisReadCache` keeps a dictionary of decoded original boundaries and conservative encoded-byte accounting. It retains entries only within the existing encoded allowance. If that optional cache fills, the reader decodes uncached. Importantly, the closure-size guard runs **before** the cache lookup: a hit cannot make required material disappear from admission accounting.

The cache is created after `BEGIN IMMEDIATE` in `publish`, shared across that transaction's historical and proposed-revision checks, and discarded afterward. A later publication starts fresh. A permanent cache would require a different validity proof and could conceal changed stored data; that is not selected.

The actual retained-page read-count control falls from156 to15 original-basis decodes, with at most one per transaction/basis pair. This does not imply a90% total speedup. Other work remains, including decoding historical roots, validating relations and serializing retained content. A focused regression reduced26 decodes beyond a13-decode bound to compliance; a second control verifies cached bases still count toward an actual publication refusal and earlier acknowledged recovery remains valid.

One implementation error was caught before qualification: cache initialization initially landed in store creation rather than the publication transaction, producing `NameError`. It was corrected at the transaction owner. The failed log is preserved; no fixture or assertion was weakened.

## Alternatives and the evidence that chose this repair

| Alternative | Why it was not selected for this repair |
|---|---|
| Enlarge the recovery allowance | Accumulation remains; the threshold moves and the deliberate resource contract changes |
| Intern all views in the generic host | Broadens lifecycle behavior for every caller before the consumer-local repair is tested |
| Change storage reconstruction/accounting | Changes a cross-cutting resource/recovery method and requires its own proof |
| Add a per-root projection immediately | Adds selection/representation responsibilities before using existing one-view/many-delivery support |

The selection is an engineering judgment grounded in the owner trace and real failure. It is not a claim that other approaches can never become useful. A future projection requires its own demonstrated consumer need and preservation of all necessary premises.

The optimization leaves payload meaning and existing decoding unchanged, so the consumer method/representation and lifecycle/native codec versions remain compatible. Recorded source hashes distinguish the implementation horizons.

## What the tests actually protect

The original repeated-page test failed with eight views where one unchanged view was required. The repaired consumer family passes 30 tests, including seven new controls. The fixtures use actual product preparation, consumer and host owners with controlled data. They isolate attribution/validity/failure behavior; they are not real-provider observations.

| Control | Regression caught |
|---|---|
| Eight distinct exact pages share one basis/view | Reintroducing a new original view for every page |
| Interleaved native selections | Reusing the wrong offered native IDs |
| Two source reads and delivery-specific citation | Treating a shared view as proof a line appeared in every delivery |
| Description-family identity progress | Rebinding an old delivery to changed native context |
| Reordered native universe | Reusing an obsolete omission menu merely because old referenced material remains valid |
| Method withdrawal after reuse begins | Letting cache presence replace present permission |
| Durable failure on a later cached page | Claiming delivery, losing acknowledged progress or automatically retrying publication |

The existing guarded fresh-process test now restores two exact pages with one shared view, alongside source delivery and attributed citation. Acquisition, source querying, evaluator and network entry points are forbidden during that recovery.

The consumer-only horizon passed1,071 full product tests and55 installed consumer/composition/delivery controls. The combined source passes1,073 product tests, including the two publication refinements, alongside194 API and7 architecture controls. Installed proof for each horizon remains separately identified in the evidence packet. Existing venv dependencies are reused, so dependency isolation is not claimed.

The separately frozen retained HTTPX successor, its actual outcome and guarded recovery are recorded in the linked cycle/evidence packet. Passing synthetic controls alone does not close that real retained task. Preserve the original refusal when assessing any successor.

The final combined-source task (`navigation-04`) completes60 actual pages/245,760 characters at the original64-page allowance, delivering282,355 JSON response bytes. All four native witnesses match, including ordered paths/comparisons/premises. Those60 deliveries share one view and one original basis; the native boundary remains equal to the original capture. Guarded checkout and installed-package cold opening and the separate installed delivery review pass. The original six-page refusal remains a negative control. These later dated results qualify the pinned source against this exposed retained task; they do not establish independent usefulness, untouched transfer, active whole-run latency or runtime compatibility.

## Boundaries to remember

View reuse removes repeated creation of original bases for an unchanged selection. Each delivery still adds retained history. Large payloads and long histories still have processing/retention costs and supported limits. This repair does not promise unlimited paging, constant total memory or low latency for every input.

The ordinary HTTPX case's four native alternatives are locally bound under a sampled newer forwarder. The separate curated old-forwarder control rejects `app` against proposed HTTPX. Those outcomes concern different retained call/forwarder/signature relationships. Neither proves installed dispatch, executed tests, whole-program compatibility or maintainer permission.

The fixed source-only navigation baseline remains incomplete. Its missing reexport ranges are not silently filled after grading. Machine delivery counts and elapsed time are not independently measured human review time or usefulness.

## A timing mistake worth learning from

During qualification, the assistant described a process elapsed-time reading of about55 minutes as active traversal time. Ali pointed out that the session had been paused. That criticism exposed an unsupported inference: the retained elapsed readings did not separate active work from paused/resumed environment intervals. The active55-minute claim was withdrawn.

The assistant had already interrupted that successor at47 acknowledged pages on the mistaken latency interpretation. Its raw outputs remain incomplete, with exit130, acknowledged/attempted identities and the original counter reading preserved. That is an assistant-caused interruption, not a comparison failure or a completed qualification. Earlier acknowledged pages remained readable; the attempted revision ID was absent on exact selection. The full staged value was not retained by that diagnostic, so no exact `inspect_publication(staged)` receipt is invented.

Source inspection separately shows repeated original-basis decoding while publication validates history. That is an implementation fact. Whether it causes an unacceptable active latency is a further measurement and product-budget question. The elapsed anecdote did not justify expanding into a storage optimization; none was implemented on that basis.

The corrected successor records per-page monotonic elapsed and process-CPU counter deltas and labels their interpretation explicitly. Those readings improve observation; they do not manufacture a pause trace, human review time or a latency acceptance threshold. Keep these steps separate: read a counter → identify what interval it measures → account for unknown pauses/environment behavior → make only the supported performance claim → decide whether another owner needs repair.

## Why more CPU or RAM is not the first change

A point-in-time WSL observation exposed20 logical CPUs, roughly49GiB available RAM and no swap use. This did not indicate RAM pressure. It also did not prove the complete machine was free of every possible hardware bottleneck.

This path does serial validation inside an ordered SQLite publication. Idle additional cores do not automatically divide that algorithm. More RAM does not remove duplicate decoding, and the64MiB software admission allowance is not the physical RAM available to the machine.

The useful order is: establish correct results and measurement meaning → count/profile repeated work → remove justified duplication → measure the remaining cost → consider parallelism for genuinely independent work. Independent cases/checks can run concurrently. Parallelizing work inside one publication would need a clear snapshot, deterministic reference/accounting and ordered commit model; it is not simply increasing a thread count.

Possible later methods include profiling, avoiding redundant representation round trips, batching known operations or a question-oriented per-root view. Each needs a real remaining consumer bottleneck and its own proof. A faster per-root view must preserve paths, source references, uncertainty and all necessary premises. Learning value is a reason to explain these alternatives; it does not justify adding every mechanism to the product.

One additional method was actually probed and rejected: a streaming-search replacement for the byte-wise JSON preflight. It matched6,012 seeded guard outcomes, but interleaved measurements on retained comparison/native-envelope/lifecycle buffers were mixed. It was slower on comparison data, modestly faster on the envelope, and approximately neutral on lifecycle data. Correctness and the idea of using C-level search were insufficient reasons to adopt it. The product JSON resource guard remains unchanged. Keep rejected prototypes as evidence, rather than hiding them or forcing a new feature to justify the effort.

## Depth and a fast return route

**Own:** available/view/delivered/current-valid distinctions; original-basis attribution; why revision inequality differs from native-material change; the failed-publication boundary; what each proof establishes.

**Understand operationally:** the dictionary key/value, short-circuit condition, invalidation branch, distinct receipt/citation checks and the normal consumer → host → store → cold-reader flow.

**Lookup when needed:** exact JSON codec fields, SQL size queries, dataclass syntax and backup API details. Deeper storage redesign and a future per-root projection are separate responsibilities.

For a quick return: read the failure and repaired flow diagrams, open `_deliver`, follow `prepare_view`/`deliver_view`, then inspect the repeated-page and publication-failure tests in [test_workspace_consumer_access.py](../tests/test_workspace_consumer_access.py). The [implementation plan](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md#stable-material-view-reuse-for-bounded-navigation) records the bounded design/proof responsibility.

For transaction reuse, follow `publish` → `_read(..., basis_cache=...)` in the store, then the two publication decode-count/resource controls in [test_workspace_checkpoint_store.py](../tests/test_workspace_checkpoint_store.py). The [repair packet](../working-memory/evidence/2026-11-04-bounded-native-navigation-repair/README.md) links actual evidence and rejected experiments.

Useful self-checks, without assuming mastery from reading:

1. Why can two deliveries have different content but the same view and original basis?
2. Why does a new logical revision after a delivery not automatically invalidate the old view?
3. What should happen if the native boundary changes while the cached view still passes material-validity checks?
4. Why must a failed later page leave the earlier delivery readable but block an automatic publication retry?
5. Why can an unchanged view survive later logical revisions while a decoded-basis cache is discarded after each database transaction?
6. Why does156→15 original-basis decodes not imply a90% total speedup, and why did a correct scanner prototype still fail to earn adoption?
