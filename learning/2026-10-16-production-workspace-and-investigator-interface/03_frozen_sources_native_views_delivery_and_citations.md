# Frozen sources, native views, delivery and citations

**Educational snapshot:** repository horizon **`5187f40ba974341eb29d765363f093922a881803`**, 2026-10-16. The common Investigator input/source-interface implementation is complete and verified at this horizon. A newer October 16 shared input freeze is also qualified and retained; the prepared future adapter cycle has not started.

**Responsibility:** understand how UpgradePilot offers one frozen evidence universe to a future Investigator while preserving native semantic ownership, bounded raw-source navigation, actual delivery provenance and the separation between citation and evaluated support.

## Core mental model

The interface is built from two distinct stores of meaning:

```text
COMMON NATIVE PREPARATION
product-owned dependency/CI facts
        ↓
canonical Workspace

FROZEN SOURCE PROFILE
retained raw repository/captured text
        ↓
RetainedSourceCatalog
```

A bounded consumer adapter joins them without merging their responsibilities:

```text
Workspace + RetainedSourceCatalog
        ↓
WorkspaceEvidenceAccess
        ↓
source views / native views
        ↓
actual ViewDelivery
        ↓
optional attributed proposal + citation
        ↓
separate evaluation, if an admitted evaluator exists
```

The core authority ladder is:

```text
available
!= delivered
!= observably used
!= cited
!= evaluated support
!= sufficient
!= action permission
```

## 1. Both future treatments start from the same product-native semantics

[`investigation_inputs.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/investigation_inputs.py) extracts two shared preparation functions:

```text
acquire_dependency_inputs(...)
prepare_ci_evidence(...)
```

The normal product investigation and the bounded preparation path both use these functions.

That means the future raw-oriented and structured-native treatments do **not** get separate implementations of dependency or CI meaning.

The shared flow is:

```text
exact PR identity + complete changed files
        ↓
existing dependency analysis owner
        ↓
exact source contexts
        ↓
exact-head runs/jobs/workflow definitions/project sources
        ↓
existing CI coverage owner
        ↓
existing runtime dependency-state owner
```

This matters experimentally and architecturally.

If the structured arm used a stronger CI producer than the raw arm, a later performance difference would be confounded:

```text
interface difference
+
semantic-input difference
```

The implementation instead preserves:

```text
same native owners
same underlying qualified evidence
then later different access/presentation treatment
```

## 2. Model-free Workspace preparation stops honestly

[`prepare_dependency_ci_workspace(...)`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/preparation.py) is a trusted bootstrap for an exact PR/base/head snapshot.

It:

```text
validates exact frozen base/head
→ runs shared dependency preparation
→ initializes NativeInvestigationCapture
→ publishes partial native Workspace progress
→ runs shared CI preparation when dependency transition is established
→ captures/publishes CI native results
→ reconstructs the supported CI projection as a guard
```

It deliberately does **not** perform upstream interpretation, target execution, synthesis, model inference or general adequacy evaluation.

Therefore unperformed families remain:

```text
not_evaluated
```

not empty, negative or safe.

## 3. `RetainedSourceCatalog` is a frozen raw-input universe, not another Workspace

Open [`source_access.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/source_access.py).

A `RetainedSourceScope` records:

```text
source_id
repository
revision
kind
capture_basis
coverage_limit
```

A `RetainedSourceFile` carries exact retained text plus optional capture metadata.

`RetainedSourceCatalog` freezes scopes/files and computes one identity from:

```text
exact target
scope descriptors
file descriptor digests
```

That identity helps prove two consumers are operating on the same retained universe.

But:

```text
catalog identity/hash
→ integrity and freeze identity

not
→ source authenticity
→ semantic truth
→ installed binding
→ action authority
```

The catalog's own docstring calls it an immutable data backend, **not a second investigation-state owner**.

### Catalog versus Workspace

Keep this boundary explicit:

```text
RetainedSourceCatalog
→ what raw retained source material is available

Workspace
→ what investigation state/history/native facts/deliveries/proposals/evaluations exist
```

The catalog can contain thousands of files without turning every file into a Workspace record.

## 4. Raw navigation is intentionally closed and bounded

The source catalog exposes only:

```text
list_sources
list_paths
search
read
resolve
```

No arbitrary filesystem access, network fetch, code execution or semantic parser is hidden behind this interface.

### `list_sources`

Shows which admitted source scopes are available.

### `list_paths`

Shows retained paths within one source scope.

### `search`

Performs literal case-insensitive text navigation and returns bounded previews plus addressable references.

A match establishes only that the literal text occurs in the retained capture.

### `read`

Returns exact retained line content and creates a reference such as:

```text
source:<file-id>:L42:7
```

### `resolve`

Resolves one exact reference back to retained content inside the same catalog.

## 5. `observed`, `empty`, `scoped_negative` and `problem` mean different things

Every source query returns one of four outcomes.

### `observed`

The requested operation returned actual material.

### `empty`

The operation is valid, but the requested page/range contains nothing meaningful—for example an offset beyond an otherwise nonempty result set.

### `scoped_negative`

The admitted search scope was actually examined and contained zero matches.

This means:

```text
not found in this exact frozen searched scope
```

not:

```text
absent everywhere relevant
```

### `problem`

The operation could not establish a valid observation—for example unknown scope, malformed query, unavailable path or invalid range.

So:

```text
bad query
!= negative evidence
```

This distinction prevents interface errors from becoming evidential claims.

## 6. Search preview is navigation, not complete delivered evidence

Search results contain a preview that can be truncated.

A preview may be enough to tell the consumer where to look next, but it is not necessarily the full line or context.

Therefore:

```text
search preview
→ navigation hint

read / resolve
→ exact delivered content
```

The source-reference validation logic requires the exact reference to have been delivered through a full `read`/`resolve` path before it may support a source citation.

This closes a subtle failure mode where a model cites a truncated preview whose omitted text changes the meaning.

## 7. Source capacity limits define interface support, not semantic absence

Current source-profile bounds include:

```text
4 MiB per retained source file
64 MiB aggregate source text
20,000 files
256 source scopes
256 KiB maximum source delivery
```

If a requested view is too large, the adapter returns/refuses with a capacity problem and tells the consumer to narrow the request.

It does not silently truncate evidence and then pretend the resulting partial content is complete.

A capacity refusal means:

```text
this interface cannot deliver this request as asked
```

not:

```text
the evidence does not exist
```

## 8. `WorkspaceEvidenceAccess` fixes one assignment's evidence boundary

Open [`consumer_access.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/consumer_access.py).

Construction binds:

```text
exact Workspace target
exact source catalog identity
allowed source IDs
allowed native families
native-view capacity
one method identity
```

The source catalog must match the current Workspace exact target.

The adapter's admitted scope is:

```text
frozen-sources:<catalog identity>
```

Before every operation `_guard(...)` asks the host to validate the purpose and current method/material basis.

So the consumer cannot silently expand itself to another source universe.

## 9. Delivery is a retained lifecycle fact

The adapter does not simply return bytes directly.

`_deliver(...)` first creates a `ConsumerView`, then asks the host to create a `ViewDelivery` containing the actual payload that was delivered.

This lets UpgradePilot distinguish:

```text
AVAILABLE
material existed in the frozen backend

SELECTED
material was included in a bounded view

DELIVERED
this exact payload actually crossed the consumer interface
```

`ViewAccessReceipt` additionally records mechanical accounting such as:

```text
operation
outcome
delivery ID
bytes delivered
files examined
lines examined
```

But this is system accounting, not model cognition.

```text
backend examined 20,000 lines
!= model reasoned over every line
```

and:

```text
payload delivered
!= payload semantically used
```

## 10. Native views expose owner facts without becoming a new evaluator

The initial native offering is intentionally narrow:

```text
investigation_inputs
ci_inputs
ci_coverage
runtime_dependency_state
```

Before native delivery the adapter reconstructs the supported CI projection against the current exact target.

A delivered native record contains provenance such as:

```text
record ID
family
owner
outcome
codec version
producer method/version
retention gaps
input record IDs
payload digest
payload
```

The view explicitly states that it carries only selected native material and grants no general applicability, adequacy or action permission.

So structured access is:

```text
product-owned facts made easier to consume
```

not:

```text
precomputed final maintainer answer
```

## 11. Oversized native records are omitted explicitly, not treated as absent

If one complete native record would exceed the normal native-view capacity, the view lists that record under `omitted` with:

```text
record_id
family
reason = native_view_capacity
page_access = native_page
```

The consumer may then request `native_page(...)` for exact retained UTF-8 payload text.

A partial page is labelled `partial_payload=true`.

Therefore:

```text
omitted from whole view
!= native evidence absent
```

and:

```text
partial page
!= complete native record
```

## 12. A source proposal may cite only content that was actually delivered

`propose_source(...)` validates:

- the supplied lifecycle value is a real `ViewDelivery`;
- the delivery representation is the source-view format;
- the delivery belongs to the exact catalog identity;
- the exact source reference was actually delivered through `read`/`resolve`;
- the delivery's material basis is still valid.

Only then does the host retain:

```text
AttributedProposal
+
ContentCitation
```

This closes a provenance loophole where a consumer could cite a line it never received.

But a valid citation still establishes only:

```text
this proposal points to this delivered content
```

not:

```text
the source entails the proposal
```

Semantic support requires another qualified evaluator.

## 13. Full authority ladder

The most useful compact model for this interface is:

```text
SOURCE/NATIVE MATERIAL AVAILABLE
        ↓
ACTUAL VIEW DELIVERED
        ↓
OPTIONAL OBSERVABLE USE RECEIPT
        ↓
ATTRIBUTED PROPOSAL / CITATION
        ↓
QUALIFIED SUPPORT/REFUTATION EVALUATION
        ↓
INVESTIGATION SUFFICIENCY / ADEQUACY
        ↓
MAINTAINER ACTION PERMISSION
```

Every arrow is an additional responsibility.

The common interface implementation reaches the delivery/citation/accounting layers. It does not collapse them into support, sufficiency or action.

## 14. Real HTTPX case — current API zero is scoped evidence, not historical absence

The October 15 qualification used the HTTPX 0.27.2 → 0.28.1 case, PR #20.

Qualified inputs established:

```text
exact PR/base/head
complete one-file dependency change
dependency/source context
```

At acquisition time the exact-head workflow-run response was empty.

Native owners therefore produced:

```text
CI coverage = no_successful_ci
runtime state = no_admitted_candidate
```

The source profile contained **2,632 files / 18,873,205 bytes**.

The critical evidence-strength rule is:

```text
current exact-head provider returned zero runs
!= CI never existed historically
```

Older captured CI remains separate historical raw evidence.

The preparation does not manufacture a stronger positive runtime fact simply because the future Investigator would prefer one.

## 15. Real glyphsLib case — static CI support remains weaker than runtime proof

The glyphsLib pytest 9.0.2 → 9.0.3 case, PR #1145, qualified:

```text
exact PR/base/head
complete one-file dependency change
source contexts
two workflow runs/jobs/definitions
required native source reads
```

Native results were:

```text
CI coverage = supported_not_correlated
runtime candidates = unresolved
```

The source profile contained **1,384 files / 16,035,160 bytes**.

This preserves the strength boundary:

```text
static dependency consumption
!= exact runtime execution
!= installed dependency version
!= compatibility
```

Raw RST remains addressable as source text without inventing a semantic parser.

## 16. Fair comparison requires one common evidence freeze

If new qualified evidence is added before a comparison, it cannot be given only to one treatment.

Otherwise the experiment would change two variables:

```text
interface treatment
+
evidence universe/strength
```

The proper rule is:

```text
new qualified evidence
→ new common freeze
→ both future treatments use it
```

The treatments may later differ in how evidence is exposed—for example mostly raw navigation versus structured native views plus bounded raw access—but not in the underlying evidence universe or native semantic ownership.

Historical model runs remain reference evidence, not paired controls for the new freeze.

## 17. Historical CI/source material may remain raw without becoming native truth

A historical summary can still be useful evidence even when it lacks the exact inputs required by a current native owner.

Correct handling:

```text
retain historical/raw statement
+ provenance/limitations
```

Incorrect handling:

```text
missing native inputs
→ synthesize native result
```

or:

```text
missing native inputs
→ call it empty/negative
```

Native truth is established only by its admitted owner with sufficient inputs.

## 18. Source profile and Workspace checkpoint retain different things

The source profile can hold thousands of files.

A Workspace checkpoint retains:

```text
native premises/results
lifecycle history
actual delivered source/native payloads
proposals/citations/evaluations
```

It does **not** embed the entire source inventory merely because those files were available for navigation.

Therefore cold checkpoint recovery can reconstruct:

```text
what investigation state existed
what exact content was actually delivered
```

while full future source navigation still requires the separate frozen source profile.

So:

```text
checkpoint recovery
!= full source-catalog reconstruction
```

This separation keeps the canonical investigation history distinct from the larger frozen input backend.

## 19. October 16 retention sequence — preserve loss honestly, then establish a new freeze

This later sequence is a strong real example of provenance discipline.

### First: retain what actually survived

The original research corpus and historical freeze/selection metadata were moved to durable owner-only local storage outside Git/temp.

The retained corpus is **40,036,196 bytes** and contains 4,000 original documents across the two cases.

But the later October 15 enriched preparation bundle—source profiles, public acquisition receipts and Workspace checkpoint stores—was not found.

The project explicitly recorded:

```text
original corpus retained
old enriched bundle unrecovered
```

It did **not** claim the raw corpus could recreate missing provider responses/checkpoint history without a new acquisition.

### Then: deliberately create a new common snapshot

Rather than silently relabel new data as the old freeze, the main workstream ran a new anonymous-public preparation and created a distinct qualified snapshot:

```text
common-freeze-2026-10-16-2025
```

The new bundle contains per case:

```text
common-sources.json
public-acquisition.json
checkpoint/workspace.sqlite3
```

plus a separately validated backup and cold-verification outputs.

All **14 public responses** were recorded with actual acquisition timing. Native owners ran exactly once per case.

The evidence explicitly says:

```text
new snapshot replaces unavailable old inputs for future use
!= recovery of October 15 exact bytes
```

That is the right freeze/provenance model.

## 20. New October 16 cold proof

The newly qualified freeze passed:

- **23 consumer-access tests**;
- all retained input hashes;
- all **96 product source hashes**;
- exact profile/checkpoint/backup identity checks.

Four guarded cold case reads—original and backup for both cases—reconstructed:

```text
16 revisions per case
5 actual deliveries
1 citation
unsupported proposal evaluation
supported native/lifecycle history
```

with nine forbidden-entry/network guards per child and unchanged database bytes.

The full source profiles were not needed to recover the retained delivered content from checkpoints. They were decoded separately to prove the complete frozen source universe remained available.

That is a concrete demonstration of the profile/checkpoint responsibility split.

## 21. Important engineering corrections

### Old research corpus shape exceeded native structural bounds

The roughly 40 MB legacy research corpus used acquisition manifests whose structure exceeded canonical native JSON limits.

The correct response was **not** to enlarge the production native parser/store merely to fit an old research representation.

A bounded diagnostic converter produced product-owned source profiles that each satisfy current interface limits.

**Lesson:** research file shape does not get to redefine production recovery contracts.

### Exact target is required for projection

An early retained-input composition omitted `expected_target` for offline native projection.

The caller was corrected to supply the actual exact target rather than weakening projection validation.

**Lesson:** native bytes alone are insufficient; target binding is part of the material meaning.

### Python mock patch points moved with the shared preparation seam

After extracting common dependency/CI preparation, some integration tests still patched the old lookup site.

The tests were corrected to patch where the dependency is now actually resolved/used.

**Lesson:** in Python, patch the binding used by the code under test—not merely the module where a function was originally defined.

## 22. Verification and non-proof

The original interface implementation recorded:

- **23/23 new consumer tests PASS**;
- **898/898 checkout tests PASS**;
- **898/898 fresh noneditable installed tests PASS**;
- all **96 product Python hashes match**;
- genuine HTTPX/glyphsLib public input qualification;
- current/fresh-installed guarded cold recovery;
- archived-reader compatibility/refusal.

The newer October 16 snapshot requalified current input availability without changing product source/tests.

This proves the declared input/interface mechanics.

It does **not** prove:

```text
LLM usefulness
structured treatment superiority
semantic correctness of Investigator claims
investigation adequacy
action permission
full native-family migration
user-facing continuation/replay
power-loss durability
```

## 23. What to own versus what to look up

### Must master / own

- shared semantic producer path across normal product and future consumers;
- source catalog versus canonical Workspace;
- freeze identity versus authenticity/truth;
- `observed` / `empty` / `scoped_negative` / `problem`;
- search preview versus exact read/resolve delivery;
- available versus delivered versus cited versus evaluated support;
- omitted native view versus absent native evidence;
- common-freeze fairness rule;
- historical raw evidence versus qualified native result;
- source profile versus checkpoint recovery.

### Understand operationally

- catalog identity construction;
- resource/page limits;
- native whole-view capacity and `native_page`;
- delivery/citation validation;
- operation receipts/accounting;
- durable input-retention and new-freeze qualification process.

### Lookup level

- exact file/reference regexes;
- every JSON field in source/native views;
- diagnostic conversion scripts;
- exact local retained paths.

### Deferred deliberately

- actual Investigator adapter/model loop;
- prompt/tool schema;
- model deployment qualification;
- semantic evaluator design;
- comparison conclusions.

## Fast relearning route

1. Recreate the two inputs: **canonical Workspace + separate frozen source catalog**.
2. Open `prepare_ci_evidence(...)` and explain why normal product and future consumer share one semantic producer.
3. Open `RetainedSourceCatalog.query(...)`; explain `scoped_negative` versus `empty` and why search preview is not citation evidence.
4. Open `WorkspaceEvidenceAccess._deliver(...)` and `propose_source(...)`; trace actual delivery to citation.
5. Use HTTPX or glyphsLib to state exactly what the native CI result proves and does not prove.
6. Explain why losing the Oct 15 enriched bundle required a **new** freeze rather than relabelling newly acquired inputs as the old one.

## Transfer questions

1. A literal search returns zero matches under one retained source/prefix. What exactly may you conclude, and what global claim remains unsupported?
2. Why must a model perform `read`/`resolve` before citing a line discovered through a truncated search preview?
3. A native record is omitted from the whole view due capacity. What should the interface expose next, and what must the consumer not infer?
4. Why would giving newly discovered CI evidence only to the structured treatment make a later raw-vs-structured comparison uninterpretable?
5. A checkpoint restores five delivered source payloads but the separate 2,632-file catalog is unavailable. What historical fact remains recoverable and what navigation capability is missing?

## Primary anchors

- [`investigation_inputs.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/investigation_inputs.py)
- [`workspace/preparation.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/preparation.py)
- [`source_access.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/source_access.py)
- [`consumer_access.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/consumer_access.py)
- [common interface implementation cycle](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/working-memory/2026-10-14_2345_common-investigator-inputs-and-source-interfaces_lbd-cycle.md)
- [October 15 interface qualification evidence](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/working-memory/evidence/2026-10-15-common-investigator-preparation/README.md)
- [October 16 durable raw-input retention](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/working-memory/evidence/2026-10-16-investigator-input-retention/README.md)
- [October 16 new common-input snapshot qualification](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/working-memory/evidence/2026-10-16-common-investigator-input-snapshot/README.md)

`UP-SKILL:upgradepilot-learning-artifact`
