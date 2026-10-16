# Investigator adapter mechanical contract, packing and qualification

**Educational extension snapshot:** repository horizon **`4545d5f0b8717fb58c91e2a470aee5367b8d6846`**, 2026-10-16.

**Relationship to Notes 1–4:** the production `src/` and normal `tests/` responsibilities taught in Notes 1–4 did not change between their `5187f40...` snapshot and this extension. This note teaches the new **experiment-owned Investigator consumer layer** added afterward. It does not reinterpret the production Workspace as experiment code and does not claim model inference or semantic usefulness.

**Responsibility:** understand how one bounded Investigator assignment is now mechanically connected to UpgradePilot's real Workspace/source/native interfaces while preserving authority, reference provenance, treatment fairness, observable input visibility and cost accounting before any model is allowed to run.

## Core mental model

The new path is:

```text
qualified retained native boundary + frozen source catalog
                         │
                         ▼
              InvestigatorAssignment
     fresh host / lineage / references / notes
                         │
                         ▼
              WorkspaceEvidenceAccess
      real product raw/native delivery seam
                         │
                         ▼
               strict experiment tool menu
                         │
                         ▼
                  AdapterEvent
       exact result bytes + typed references
                         │
                         ▼
                whole-event packing
   only complete events that fit are consumer-visible
                         │
                         ▼
          trusted scripted consumer for proof
                         │
                         ▼
      attributed laboratory report + citations
                         │
                         ▼
             procedural termination

NO model transport in this proof
NO new semantic evaluator
NO action permission
```

Keep the ownership split explicit:

```text
product host/access
→ owns canonical Workspace validity, delivery and lifecycle facts

experiment adapter
→ owns the closed consumer wire/tool/reference mapping

trial driver
→ owns packing, visibility, resource admission and accounting

offline qualifier
→ owns model-free correspondence/fairness checks

future model/deployment layer
→ still must qualify runtime/template/context/token/offload/session behavior
```

The source implementation is [the adapter at `4545d5f0`](https://github.com/motafegh/UpgradePilot/blob/4545d5f0b8717fb58c91e2a470aee5367b8d6846/experiments/investigator_workspace_adapter.py), [the trial driver](https://github.com/motafegh/UpgradePilot/blob/4545d5f0b8717fb58c91e2a470aee5367b8d6846/experiments/investigator_workspace_trial.py), and the [mechanical qualification guide](https://github.com/motafegh/UpgradePilot/blob/4545d5f0b8717fb58c91e2a470aee5367b8d6846/experiments/INVESTIGATOR_WORKSPACE_MECHANICAL_QUALIFICATION.md).

## 1. `InvestigatorAssignment` is a fresh experiment consumer, not a restored investigation

Each assignment receives:

```text
CapturedNativeBoundary
RetainedSourceCatalog
one treatment: raw | structured
```

It creates a **new volatile `InvestigationWorkspaceHost`** and initializes that host from the retained native boundary.

It does **not** restore the preparation diagnostic's old interaction history.

This matters because the comparison must not leak:

```text
old views
old search choices
old notes
old proposals/citations
old stopping behavior
```

into a new assignment.

The immutable common native/source material may be shared. Mutable investigation state may not.

So the fairness boundary is:

```text
shared immutable evidence universe
+
separate host/lineage/reference registry/events/notes per assignment
```

That is stronger than merely creating two model chat sessions over one mutable experiment object.

### No execution authority is installed

Trusted composition installs the bounded evidence-view methods and one generic `DiscoveryObjective`.

The assignment configures:

```text
authority = None
capabilities = ()
```

Therefore the consumer cannot turn its tool JSON into provider execution authority. The offered operations are retained-evidence navigation/projection, not arbitrary external actions.

## 2. Raw and structured treatments differ at the interface, not the underlying evidence

Both treatments receive the same exact native boundary and source catalog.

The **raw** treatment can use the frozen source operations:

```text
list_sources
list_paths
read_source
search_sources
resolve_source
```

The **structured** treatment receives those same raw operations plus:

```text
read_native
read_native_page
```

The initial native families remain:

```text
investigation_inputs
ci_inputs
ci_coverage
runtime_dependency_state
```

The important experiment statement is:

```text
raw treatment does not see native views
!= native facts did not exist
```

Native access is intentionally **withheld as the treatment restriction**. The underlying preparation is common.

This preserves the comparison question: does structured native access help evidence use relative to raw navigation over the same evidence universe?

It does not compare different acquisitions or different semantic owners.

## 3. The consumer wire contract is intentionally closed

The adapter exposes a versioned contract:

```text
investigator-contract2-workspace/1
```

Tool requests are exact JSON objects with:

```text
{
  "tool": ...,
  "arguments": ...
}
```

The schema refuses:

```text
unknown tools
unoffered tools
missing fields
extra fields
wrong primitive types
out-of-range integers
unsupported enum values
```

There is no coercion such as:

```text
"4" → 4
```

and no repair that silently removes an extra authority-like field.

This is useful because mechanical qualification must prove that malformed model-shaped output cannot accidentally widen product authority.

The correct behavior is:

```text
bad request
→ charged/refused event
→ no hidden reinterpretation into a valid stronger request
```

## 4. Laboratory references are mappings to real product deliveries

The experiment report uses compact references shaped like:

```text
{kind, id}
```

Those IDs are not independent evidence objects.

Internally each `EvidenceReference` binds to:

```text
kind
laboratory reference id
actual product delivery_id
exact address/range/digest
native record IDs where relevant
```

The adapter therefore creates a bridge:

```text
laboratory reference
→ exact Workspace delivery
→ exact retained material address
```

### Source search versus source lines

A search result can create a `search_observation` reference.

That does **not** let the report cite its preview as though the full source line was read.

For source-line evidence:

```text
search preview
→ navigation only
→ read/resolve exact retained content
→ source_line reference
```

This preserves the source-strength lesson from Note 3 at the experiment boundary.

### Native record versus native page

A whole delivered native record may produce a `native_record` reference.

If a whole record is omitted because of the native-view capacity, the consumer must request a page.

That page becomes a distinct `native_page` reference.

So:

```text
page of record
!= whole record
```

The experiment cannot silently promote partial text to complete native evidence.

## 5. Product delivery is still not enough: the trial tracks consumer-visible input

This is one of the most important new distinctions.

The product host can truthfully record:

```text
ViewDelivery happened
```

but the future consumer may not receive every historical event in every request because the context/packing envelope is bounded.

Therefore the trial driver separately tracks which exact references were inside the packed input supplied to the consumer.

The adapter's report/reference validation accepts only references that are both:

```text
valid experiment references
AND
visible through a packed event delivered to that consumer interaction history
```

This adds a new layer to the evidence ladder:

```text
material exists
→ product delivered it
→ experiment event retained it
→ event was packed into consumer input
→ reference may be used in laboratory output
→ still not entailment/support/adequacy
```

Do not collapse **product delivery** into **model receipt**.

The current model-free proof uses a trusted script, but this distinction exists specifically so later model-session/context semantics can be measured truthfully rather than assumed.

## 6. Packing preserves whole-event identity rather than truncating arbitrary text

`pack_input(...)` starts from the newest events and includes each event only if the complete rendered input stays inside the configured byte envelope.

If an event does not fit, it is omitted as a whole.

The packed input records omitted events using:

```text
event_id
byte size
SHA-256
```

So the consumer sees truthful omission metadata instead of a silently clipped event.

The rule is:

```text
whole event included
OR
whole event omitted and identified
```

not:

```text
include whatever prefix happened to fit
```

This protects evidence meaning and later diagnosis.

### Byte capacity is not model context capacity

The current `packed_input_bytes` limit is a **mechanical envelope**.

It is not evidence that:

```text
N bytes == M tokens
```

or that a particular model/template can safely use that context.

The trial manifest therefore keeps deployment fields unresolved and explicitly says actual tokenizer/chat-template/context/output/reasoning fit still needs qualification.

## 7. Conservative admission charges and actual work receipts answer different questions

The trial driver has fixed operation admission charges such as:

```text
raw/native navigation request  → 4 units
note                           → 1
trial-event read               → 3
finish request                 → 3
final report                   → 4 + unique references
malformed/unoffered request    → 1
termination                    → 1 reserved
```

These are **conservative admission units**.

They answer:

> How much budget must be reserved before this request is allowed to proceed?

They do not claim every reserved internal operation actually executed.

Actual Workspace access receipts separately retain facts such as:

```text
operation
outcome
delivery ID
delivered bytes
examined files
examined lines
failure/refusal detail
```

So keep these distinct:

```text
admission charge
!= measured backend work
```

The accounting also separates:

```text
shared preparation cost
assignment composition time
consumer invocation attempts
consumer response bytes
packed input bytes
observation bytes
actual access receipts
scripted elapsed time
```

and deliberately records:

```text
model_calls = 0
model_tokens = None
native_producer_calls = 0
```

for this mechanical proof.

Unknown token usage is not written as zero.

## 8. Requests are charged before dispatch, including refusals

The driver charges every consumer request attempt before dispatch.

That includes malformed and refused requests.

Why?

Because an invalid request still consumed experiment interaction/budget and may have exposed a weakness in the model/interface.

The protocol must not reward invalid behavior by pretending it cost nothing.

At the same time, early refusal does not falsely record backend evidence access.

This gives two truthful facts:

```text
consumer attempted a request
```

and possibly:

```text
backend/product access did not occur
```

Both matter.

## 9. Capacity is admitted before backend work

Before dispatch, the driver reserves a conservative maximum observation size for operations that could return bounded raw/native data.

If the remaining observation budget cannot admit that reservation, the request is refused before backend work.

Unused reservation is released.

This prevents the system from doing expensive work and only afterward discovering that it cannot retain/report the result inside the experiment contract.

But the reservation is not measured cost.

Again:

```text
capacity admission
!= actual delivered bytes
```

## 10. Failure and correction semantics preserve originals

Malformed consumer responses can produce bounded visible correction opportunities.

The original response bytes remain retained.

The consumer must produce a new corrected response; the system does not rewrite the original into a valid result.

This protects diagnosis against invisible output salvage.

Important result classes remain distinct:

```text
refused
empty
scoped_negative
problem
failed
limit_exhausted
completed
```

### Publication/backend failure

A backend/publication failure is not translated into empty evidence.

The trial stops the affected flow and does not automatically retry.

Any already attempted/recorded work remains part of the accounting/history.

A failed publication creates no successful delivery just because underlying work may have been attempted.

This mirrors the production lifecycle principle:

```text
attempt/work
!= acknowledged published result
```

## 11. Finish, report and termination remain three different things

`finish_investigation` is a **procedural finish request**.

It does not establish that the investigation is adequate.

The final laboratory report has a strict schema with:

```text
summary
claims
conditions
unexamined
recommendation
recommendation_status
recommendation_evidence
recommendation_missing_observation
stopping_reason
```

Claims and recommendation use:

```text
asserted
inferred
unresolved
```

and must use offered evidence references.

A structurally valid report may then be retained as an attributed proposal/citation structure.

The generic semantic evaluation remains:

```text
unsupported
```

Finally, the trial records procedural termination separately.

So:

```text
finish request
!= valid report
!= supported semantics
!= investigation adequacy
!= maintainer action permission
```

## 12. The mechanical manifest deliberately refuses to authorize inference

`mechanical_manifest(...)` records the frozen mechanical protocol:

```text
prompt/task/schema
tool menu
source/native offering
operation charges
packing rules
code hashes
input inventory
lineage
```

but also records:

```text
inference_admitted = false
deployment = null
```

and names required unresolved deployment fields such as:

```text
GGUF identities/sizes/hashes
repository revision
runtime/backend versions
context tokens
actual GPU weight offload
KV-cache placement
chat-template content/hash
reasoning configuration
generation reserve
qualified rendered-input token measurements
```

This is an important architecture/process lesson:

> **A complete mechanical protocol is not a runnable model protocol until the actual deployment has been qualified.**

## 13. Offline qualification uses real retained inputs without reacquisition or inference

The offline qualifier consumes the already qualified common snapshot.

It checks retained input/code correspondence, opens supported checkpoints read-only, reconstructs the needed retained native/source state, then runs scripted assignments.

Its guards prohibit the selected network/subprocess/native-producer/model-session entry points for this diagnostic proof.

Those guards are bounded diagnostics, not a universal sandbox.

The final evidence packet is [the mechanical qualification record](https://github.com/motafegh/UpgradePilot/blob/4545d5f0b8717fb58c91e2a470aee5367b8d6846/working-memory/evidence/2026-10-16-investigator-adapter-mechanical/README.md).

## 14. Real retained-case qualification: four scripted assignments

The final qualification ran:

```text
HTTPX case    × raw
HTTPX case    × structured
glyphsLib case × raw
glyphsLib case × structured
```

These are **four scripted mechanical assignments**, not the later planned eight model assignments.

Each assignment has its own lineage.

The paired raw and structured assignments for each case preserve the same source catalog identity and the same checked raw passage hash.

That is useful fairness evidence:

```text
same retained raw evidence
+
different offered native interface
```

rather than:

```text
different source captures accidentally called different treatments
```

### Observed qualification summary

All four scripted assignments completed mechanically.

The public qualification records, among other accounting:

| Case / treatment | Consumer turns | Charged operations | Citations | Semantic evaluation |
| --- | ---: | ---: | ---: | --- |
| HTTPX raw | 5 | 23 | 3 | `unsupported` |
| HTTPX structured | 6 | 29 | 5 | `unsupported` |
| glyphsLib raw | 5 | 23 | 3 | `unsupported` |
| glyphsLib structured | 7 | 32 | 4 | `unsupported` |

These numbers describe the deterministic scripted qualification behavior, not model efficiency or treatment superiority.

The qualification also records:

```text
17 retained artifacts verified
96 product Python hashes unchanged
14 earlier shared-preparation public GET operations retained as separate preparation cost
0 forbidden execution attempts
0 model calls
0 native producer calls
retained bundle unchanged
```

## 15. Verification scope: green where claimed, not globally green

The final experiment evidence records:

```text
13 / 13 new experiment controls PASS
65 / 65 nearest product consumer/lifecycle/host tests PASS
```

The older planner entry review separately reports:

```text
23 PASS
4 errors
```

Those four errors come from untouched composition fixtures still passing a removed `segment_index` argument.

That establishes **fixture/composition drift debt**.

It does not establish that the planner's runtime semantics are broken.

This is another useful proof-classification lesson:

```text
fixture construction error
!= semantic planner failure
```

The new experiment increment did **not** rerun:

```text
full product suite
fresh installed suite
hosted CI
model load/inference
semantic review
maintainer usefulness evaluation
```

Do not quote the 13/65 checks as an all-product verification result.

## 16. Current status at this extension horizon

At `4545d5f0...`:

```text
adapter A0/A1/A2              DONE
adapter B                       DONE
scoped mechanical Verification GREEN
adapter D                       CURRENT
adapter E                       PENDING
model inference                 NOT performed
semantic comparison             NOT performed
```

Ali selected parallel progression:

```text
adapter D/E learning/closure
        ||
Deployment & Model-Interface Qualification successor A-phase
```

The successor may begin because the mechanical prerequisite is green, but a material D/E contradiction must block affected later inference/qualification.

The [parallel-supervision handoff](https://github.com/motafegh/UpgradePilot/blob/4545d5f0b8717fb58c91e2a470aee5367b8d6846/working-memory/2026-10-16_2215_adapter-d-e-parallel-supervision.md) explicitly preserves that condition.

This scheduling adaptation does not mean the adapter cycle is already closed.

## 17. What this new layer proves—and what it does not

### Established at the mechanical boundary

The current evidence supports:

```text
fresh assignment isolation
raw-versus-structured treatment restriction over shared retained inputs
strict closed tool/request schemas
real Workspace delivery reuse
lossless laboratory reference mapping to actual deliveries/ranges/digests
search-preview versus source-line distinction
native whole-record versus page distinction
whole-event packing with explicit omissions
consumer-input visibility tracking for evidence references
conservative admission accounting plus actual access receipts
bounded correction with original response retention
failure/no-retry distinctions
attributed report/citation publication
procedural termination separate from unsupported semantics
model-free offline qualification on the real retained HTTPX/glyphsLib inputs
```

### Still not established

This work does not establish:

```text
model transport correctness
model fit or speed
token/context sufficiency
chat-template correctness
GPU/offload/cache suitability
persistent model-session history semantics
semantic interpretation quality
stopping adequacy
raw-versus-structured model advantage
maintainer usefulness
action permission
durable replay
framework adoption
```

Those require the next separately qualified responsibilities.

## 18. Engineering progression worth remembering

The important progression is not merely “we wrote an adapter.”

It is:

```text
Stage 3 created a canonical host/evidence authority seam
→ common-input preparation created a fair frozen evidence universe
→ the adapter consumes those real product seams rather than rebuilding a research Workspace
→ model-free trial packing/ref mapping makes consumer visibility/accounting explicit
→ qualification proves the bridge before interpreting model behavior
```

This avoids diagnosing a model for errors caused by:

```text
wrong target
wrong source universe
leaked prior state
invalid reference mapping
silent truncation
unaccounted backend work
unoffered authority
broken experiment transport
```

The experiment is now mechanically testable before semantic claims are attempted.

## Learning depth

### Must master / own

- product delivery versus consumer-visible packed input;
- shared evidence universe versus treatment-specific interface;
- laboratory reference versus actual product delivery/material address;
- search observation versus exact source-line evidence;
- native page versus complete record;
- conservative admission charge versus actual access receipt;
- procedural finish/report publication versus semantic support/adequacy;
- mechanical qualification versus model/deployment qualification.

### Understand operationally

- strict JSON shape validation;
- assignment-local host/reference/event/note state;
- whole-event packing and omission metadata;
- resource admission and correction limits;
- offline qualifier roles and bounded guards;
- experiment-versus-product test scope.

### Lookup level

- exact schema field lengths;
- individual operation unit values;
- exact SHA-256 values;
- exact private artifact locations;
- incidental JSON helper implementation.

### Deferred deliberately

- model runtime/template/session mechanics;
- token/context tuning;
- GPU/KV-cache placement;
- semantic review methodology/results;
- broader planner repair;
- independent usefulness evaluation.

## Fast relearning route

1. Recall the ownership chain: **product host/access → experiment adapter → trial packing/accounting → offline qualifier → future model transport**.
2. Open `InvestigatorAssignment.__init__()` and `invoke()` in the adapter.
3. Open `pack_input()`, `run_scripted_trial()` and `mechanical_manifest()` in the trial driver.
4. Read the mechanical qualification guide's **Evidence and treatment contract** and **Accounting, packing and failure** sections.
5. Inspect `qualification.json` for one raw/structured pair and `verification.json` for the exact proof scope.
6. Explain why an evidence delivery can be valid but still unusable as a final report reference if its containing event never reached the consumer input.

## Transfer questions

1. Why does each raw/structured assignment need a new host/lineage even though both may share the exact same immutable native boundary and source catalog?
2. If `search_sources` returns a preview containing the desired sentence, why can that not be cited as a `source_line` without a subsequent read/resolve?
3. Why does the trial track `visible` references separately from the product host's `ViewDelivery` history?
4. What is the difference between a 4-unit admission charge and an access receipt showing the actual bytes/files/lines examined?
5. If a native record was omitted from a bounded view but a page was read later, what claim-strength difference must the laboratory reference preserve?
6. Why does a mechanically valid final report still receive `unsupported` semantic evaluation?
7. What would need to be measured before `packed_input_bytes=128 KiB` could become a justified model context configuration?
8. Why do four `segment_index` fixture-construction errors establish planner re-entry debt rather than a planner semantic failure?

## Source and evidence anchors

- [Adapter source at `4545d5f0`](https://github.com/motafegh/UpgradePilot/blob/4545d5f0b8717fb58c91e2a470aee5367b8d6846/experiments/investigator_workspace_adapter.py)
- [Trial driver at `4545d5f0`](https://github.com/motafegh/UpgradePilot/blob/4545d5f0b8717fb58c91e2a470aee5367b8d6846/experiments/investigator_workspace_trial.py)
- [Mechanical qualification guide](https://github.com/motafegh/UpgradePilot/blob/4545d5f0b8717fb58c91e2a470aee5367b8d6846/experiments/INVESTIGATOR_WORKSPACE_MECHANICAL_QUALIFICATION.md)
- [Mechanical evidence README](https://github.com/motafegh/UpgradePilot/blob/4545d5f0b8717fb58c91e2a470aee5367b8d6846/working-memory/evidence/2026-10-16-investigator-adapter-mechanical/README.md)
- [Final qualification summary](https://github.com/motafegh/UpgradePilot/blob/4545d5f0b8717fb58c91e2a470aee5367b8d6846/working-memory/evidence/2026-10-16-investigator-adapter-mechanical/qualification.json)
- [Verification summary](https://github.com/motafegh/UpgradePilot/blob/4545d5f0b8717fb58c91e2a470aee5367b8d6846/working-memory/evidence/2026-10-16-investigator-adapter-mechanical/verification.json)
- [Adapter cycle at this horizon](https://github.com/motafegh/UpgradePilot/blob/4545d5f0b8717fb58c91e2a470aee5367b8d6846/working-memory/2026-10-16_2045_investigator-adapter-and-mechanical-qualification_lbd-cycle.md)
- [Parallel D/E handoff](https://github.com/motafegh/UpgradePilot/blob/4545d5f0b8717fb58c91e2a470aee5367b8d6846/working-memory/2026-10-16_2215_adapter-d-e-parallel-supervision.md)

This note is a model-free mechanical learning artifact. It must not be used to claim that an LLM received, understood, correctly interpreted or usefully acted on this evidence.
