# UpgradePilot current ownership learning roadmap

**Branch:** `learning/current-ownership-roadmap-2026-10-31`  
**Purpose:** temporary learning/ownership branch. It records what Ali should understand, what is already sufficiently owned, what remains, and how ongoing `main` progress should alter the learning plan.  
**Initial main sync:** `034665d7032fed622e33149ba1977413f64a56d6` — `Record final executable freeze preparation and no-live boundary`.  
**Authority boundary:** this document is a learning map, not the live project authority. `MEMORY.md` on `main` remains the sole live-state owner. Product/build decisions must not be inferred from this branch when they conflict with current `main`.

## Goal and mastery standard

The objective is not to memorize UpgradePilot or Python internals. The objective is **working engineering ownership**:

- understand WHY each important capability/owner exists;
- follow the WHAT and HOW through real source/evidence when shown;
- distinguish fact, candidate relation, premise, unresolved state, runtime evidence and product conclusion;
- inspect new AI-authored work critically enough to detect unsupported claims or broken boundaries;
- explain the important data/evidence flow in our own words;
- know when deeper implementation detail is required and when it is reference-only knowledge.

A topic is `OWNED ENOUGH` when Ali can explain its purpose, follow its real evidence path, identify what it does **not** prove, and supervise consequential changes. Writing the whole implementation from scratch is not required unless a later project need makes that skill directly useful.

---

# 1. Where UpgradePilot currently is

## Big pipeline

```text
PUBLIC PR
   │
   ▼
1. Observe exact PR + dependency update
   │
   ▼
2. Acquire bounded target repository source
   │
   ▼
3. Acquire exact/qualified old + proposed dependency source
   │
   ▼
4. Discover possible source relationships
   │
   ▼
5. Compare target call arguments against candidate callable signatures
   │
   ▼
6. Preserve premises, gaps, omissions and bounded coverage
   │
   ▼
7. Save immutable/inspectable evidence
   │
   ▼
8. Reopen evidence offline without rerunning acquisition/AST/checker/discovery
   │
   ▼
9. Later: combine with runtime/CI/product evidence and justified maintainer conclusion
```

## Current live position at initial sync

As of main `034665d7`:

- source correspondence and protocol/factory evidence are implemented and controlled/retained proof exists;
- staged acquisition policy and source-priority/reservation behavior are qualified under controlled providers;
- the first fresh ordinary PR contract is frozen around HTTPX PR #20;
- reader integrity was repaired so any protocol residue requires the full ordered factory witness;
- explicit `Class.__call__` / `Class.__getattr__` declarations are correctly distinguished from allocation-backed factory/protocol witnesses;
- the fresh outer-attempt lifecycle is now implemented and controlled-qualified;
- the next live-project step is preparing the **final actual executable freeze**;
- live provider/token activation remains withheld;
- product/native Workspace/report adoption remains later and separate.

### Learning consequence

Our earlier roadmap item “learn the fresh lifecycle when main implements it” has already become active. We must now include the implemented lifecycle and forthcoming execution-freeze evidence in the learning queue rather than learning only the October30 definition.

---

# 2. Major capability/evidence layers we should understand

These layers are related but must not be flattened into one “analysis result”.

## A. Dependency / package evidence

Questions:

- what package changed?
- old version and proposed version?
- what declarations/constraints/extras/markers exist?
- what version/source identity is actually qualified versus merely sampled?

Required mastery: **good working understanding**, not resolver implementation expertise.

## B. Source acquisition

Questions:

- which target files were inspected?
- which old/proposed package source was obtained?
- what exact repository/tag/commit/source identity supports it?
- what was omitted/refused/unavailable?
- did an operational/resource limit stop us?

Required mastery: **must consolidate**.

## C. Source correspondence

Question:

> How may a target source call correspond to a dependency callable under explicit source evidence and premises?

Examples already learned:

```text
pytest.mark.parametrize(...)
→ pytest.mark re-export
→ MARK_GEN allocation
→ MarkGenerator.__getattr__
→ returned MarkDecorator
→ MarkDecorator.__call__
```

Required mastery: **good**, then reinforce through implementation/dataflow inspection.

## D. Argument/signature binding

Question:

> Under the selected candidate relation/receiver premise, do the caller arguments structurally fit this callable signature?

Core states:

- `BOUND`
- `REJECTED`
- `UNDETERMINED`

Required mastery: **must consolidate next**.

## E. Runtime / CI / environment evidence

Questions:

- what version/environment actually existed?
- was the path exercised?
- what did CI/runtime show?
- what relationships remain unresolved despite source evidence?

Required mastery: existing project foundation is substantial, but the recent API-source track must later be reconnected to it.

## F. Product conclusion / maintainer action

Questions:

- what decision is justified?
- merge/check/investigate/defer/abstain?
- what evidence remains missing?

Critical rule:

```text
source candidate ≠ runtime fact
BOUND ≠ compatibility
completed experiment ≠ useful evidence
useful evidence ≠ maintainer action permission
```

---

# 3. What is already learned well enough

Status here means “working ownership achieved enough to proceed”; it does not mean permanent mastery.

## Python/source foundations — OWNED ENOUGH

- class vs object/instance;
- instance creation / allocation concept;
- methods and `self` / receiver idea;
- imports and aliases/re-exports;
- attribute access;
- `__getattr__` as dynamic fallback mechanism at the level needed by this project;
- `__call__` and callable objects;
- `*args` and `**kwargs`;
- why we do not currently need descriptors/MRO/metaclass internals.

## Real pytest protocol/factory path — OWNED ENOUGH

Ali can follow conceptually:

```text
glyphsLib pytest.mark.parametrize(...)
→ pytest.mark
→ MARK_GEN
→ MarkGenerator instance
→ .parametrize attribute lookup
→ conditional __getattr__("parametrize")
→ returned MarkDecorator
→ callable-object __call__
→ target positional args into *args
→ ids= into **kwargs
```

## `@overload` vs runtime implementation — OWNED ENOUGH

- overload declarations describe alternative type-level call shapes;
- final ordinary `def` is the executable implementation;
- preserving all declarations avoids unsafe first-match selection;
- mixed local binding results across overload declarations are not contradictions.

## Candidate vs truth — STRONG

Ali understands that source correspondence is a conditional candidate relation, not runtime dispatch proof.

## Producer / retained evidence / reader — GOOD

Ali understands:

```text
producer → derives evidence
saved bundle → preserves exact evidence
reader → validates/presents saved evidence without re-analysis
```

and why a reader-integrity bug differs from a producer-analysis bug.

## Definition freeze / execution freeze / actual attempt — GOOD

- definition freeze = selected experimental rules before implementation/live outcome;
- execution freeze = exact executable code/config/runtime/contract that will run;
- attempt = the historical event that actually happens.

## Attempt-start / terminal / unknown-completion model — GOOD

Ali understands why immutable `attempt-started` and terminal records are distinct and why a missing terminal record is `unknown_completion`, not automatic permission to rerun.

---

# 4. Must-learn items that still need proper consolidation

These are the immediate core gaps. Do these before diving deeply into implementation internals.

## 4.1 `BOUND` vs `REJECTED` vs `UNDETERMINED`

Need to be able to explain precisely:

- what each state says locally;
- what it does not say globally;
- how receiver uncertainty, starred arguments and incomplete source facts produce `UNDETERMINED`;
- why an independently definite keyword rejection may survive unrelated uncertainty;
- how HTTPX and pytest show different useful cases.

Use real retained HTTPX + pytest evidence rather than synthetic examples where possible.

## 4.2 Premises and uncertainty

Need to internalize the pattern, not memorize every premise string:

```text
Established X
under premise Y
while Z remains unresolved.
```

Representative examples:

- installed namespace/dispatch not established;
- effective export binding not established;
- receiver binding not established;
- attribute lookup / `__getattr__` activation not established;
- branch reaches selected return not established;
- adapter sample is not target resolution.

## 4.3 Acquisition budgets as different resources

Need to understand WHY different counters exist, not memorize their values:

- GitHub request budget;
- all-provider request budget;
- stage/source reservation;
- target file attempts;
- adapter candidate attempts;
- source release identities;
- module questions;
- admitted source bytes;
- retained files / AST/facts;
- candidate/comparison cap;
- path/depth/state/diagnostic caps;
- acquisition clock vs analysis worker clock.

Learning target: identify which explosion/starvation each control prevents and what a hit means for coverage.

## 4.4 Source acquisition vs source correspondence

```text
Acquisition: Do we possess qualified source/material?
Correspondence: What source-backed relation may connect target call to callable?
```

Obtaining `MarkDecorator` source does not prove `pytest.mark.parametrize` reaches it.

## 4.5 Candidate generation vs candidate evaluation

```text
source correspondence → generate evidence-linked candidate
argument checker → evaluate local call/signature structure
```

Candidate generation must not secretly decide compatibility or applicability.

## 4.6 Coverage and bounded negatives

Must understand:

- zero candidates does not necessarily mean no exposure;
- a source/candidate/path limit can make a result partial;
- `0 omitted gap records` is not complete repository coverage;
- useful evidence can coexist with incomplete coverage;
- absence claims are only as broad as the admitted examined supported domain.

---

# 5. Next-tier learning after core semantics

These are important once section 4 is consolidated.

## 5.1 `api_source_correspondence.py` conceptual architecture

Learn the responsibility/dataflow, not every AST node:

```text
retained source units
→ target roots/binding evidence
→ resolver
→ re-export/declaration/class/factory alternatives
→ source relationship steps + premises
→ candidate pairs
→ unchanged argument checker
→ gaps/coverage
```

Goal: supervise and review changes; not reimplement it from memory.

## 5.2 Acquisition orchestration

Understand how these owners compose:

- shared native PR/dependency prefix;
- `TrialPublicSession` / staged policy;
- target inventory/file selection;
- source run and exact-release/module acquisition;
- adapter exploration;
- `prepare_ordinary_inputs`;
- source priorities/reservations/caches.

Use the old-greedy vs current-priority controlled contrast to understand why starvation occurred.

## 5.3 Retention and replay

Understand why we retain:

- exact source text/material identity;
- target/source roles;
- source relationship steps;
- premises and gaps;
- comparisons;
- coverage/omissions;
- acquisition receipts;
- method/code/config/runtime identity;
- immutable attempt disposition.

Cold-open rule: reader must not rerun network/AST/checker/correspondence.

## 5.4 Fresh outer-attempt lifecycle implementation — NOW ACTIVE

At the October31 initial roadmap sync, main has implemented and qualified this responsibility. We now need to learn the **actual implementation**, not only its earlier definition:

- before-credential immutable start record;
- original observation retained before guard refusal;
- partial material retained on handled failures;
- acquisition freeze before analysis;
- existing bounded worker exactly once;
- terminal and unknown-completion states;
- fresh-vs-controlled proof label separation;
- explicit activation interlock;
- procedural result vs structural usefulness.

## 5.5 Final executable freeze — CURRENT MAIN WORK

Main is currently preparing this. When closed, sync the roadmap and learn:

- what exact code/config/runtime/contract identities are bound;
- what the snapshot/admission checks actually verify;
- why a frozen `live_activation` mode is not itself authorization or execution;
- how the operation-level interlock protects the no-live boundary.

## 5.6 First real HTTPX ordinary attempt — FUTURE MAJOR CHECKPOINT

After final inspection and explicit live activation:

- what actual provider work occurred;
- exact request/source/material costs;
- which source relationships were found or missed;
- old/proposed local comparison results;
- which gaps/limits/premises remained;
- whether evidence is useful, useful-partial or insufficient;
- whether a product/API/Workspace adoption step is justified.

This should become a major consolidation checkpoint, not merely a pass/fail event.

---

# 6. What is reference-only for now — do NOT overlearn

Unless a real project problem requires it, do not divert learning time into deep mastery of:

- Python descriptor protocol internals;
- exact `__getattribute__`/`__getattr__` implementation details;
- metaclasses and `__new__`;
- complete MRO implementation;
- Python bytecode;
- AST API/node taxonomy from memory;
- mypy/Pyright internals;
- pytest's complete marking subsystem;
- every `Mark`/`MarkDecorator` branch;
- Requests streaming internals beyond what our transport contract needs;
- GitHub REST internals beyond provider/accounting/provenance needs;
- every exception class and serialized field;
- all numeric limits from memory;
- writing the correspondence engine or acquisition stack from scratch.

Re-enter any of these only when real evidence or implementation work makes it decision-critical.

---

# 7. Deeper engineering concepts this journey should consolidate

These are career-level skills, not merely UpgradePilot trivia.

## Evidence engineering

Distinguish:

```text
source fact
→ relation/candidate
→ premise/uncertainty
→ local evaluation
→ runtime evidence
→ product conclusion
```

## Provenance

Always ask:

- where did this fact come from?
- exact repository/version/commit/source?
- which owner produced it?
- can the claim be traced back to retained material?

## Bounded analysis

All analysis has finite scope. Limits must be explicit, observable and reflected in coverage claims.

## Fail-closed reasoning

Missing/unsupported evidence stays missing/unsupported. It does not become success, failure or a fabricated negative.

## Immutability and historical truth

Old attempts/results are historical evidence. New method versions produce successor evidence, not retroactive regrades.

## Experimental design

Freeze consequential rules before seeing the live outcome. Distinguish development controls from fresh ordinary evidence and independent evaluation.

## Separation of concerns / owner boundaries

Keep acquisition, source association, structural checking, runtime/CI, synthesis/reporting and action authority separate unless an explicit contract connects them.

## Reproducibility and offline inspection

Saved evidence should remain inspectable after restart without recreating the historical event.

## AI-native engineering supervision

AI may write code, tests and designs; ownership requires being able to inspect architecture, evidence, limitations and consequential changes rather than merely accepting green tests.

---

# 8. Current ownership matrix

This is deliberately approximate and should be updated during syncs.

| Area | Current learning state | Required next action |
| --- | --- | --- |
| UpgradePilot product purpose | STRONG | Maintain through syncs |
| Evidence/provenance philosophy | STRONG | Reinforce through real attempt |
| Python foundations for current source cases | GOOD / OWNED ENOUGH | No deeper internals unless needed |
| pytest protocol/factory path | GOOD | Revisit only when reading implementation/evidence |
| `@overload` distinction | ADEQUATE | No separate deep study now |
| Source correspondence concept | GOOD | Learn implementation architecture later |
| Producer / saved evidence / reader | GOOD | Reinforce through cold-open code |
| Definition / execution freeze / attempt | GOOD | Learn actual final freeze once published |
| Attempt lifecycle concepts | GOOD | Inspect October31 implementation |
| `BOUND` / `REJECTED` / `UNDETERMINED` | PARTIAL | Immediate checkpoint |
| Premises / uncertainty semantics | PARTIAL | Immediate checkpoint |
| Coverage / bounded negatives | PARTIAL | Immediate checkpoint |
| Acquisition budget model | PARTIAL | Immediate checkpoint after evidence semantics |
| Acquisition implementation/orchestration | NOT CONSOLIDATED | Next-tier code/dataflow study |
| Source-correspondence implementation | NOT CONSOLIDATED | Next-tier code/dataflow study |
| Fresh lifecycle implementation | NOT CONSOLIDATED | Newly active due main progress |
| Final execution-freeze implementation | MAIN IN PROGRESS | Sync after closure, then learn |
| Fresh real-run interpretation | NOT YET POSSIBLE | Major checkpoint after live attempt |
| Native Workspace/report API adoption | LATER | Re-enter only after useful fresh proof |

---

# 9. Recommended learning roadmap and progression

The roadmap is organized as checkpoints, not days. We can stop after any chunk and test understanding before proceeding.

## Checkpoint A — Finish evidence semantics

Cover together:

1. `BOUND`, `REJECTED`, `UNDETERMINED` using real HTTPX + pytest examples.
2. Premises and unresolved states.
3. Candidate relation versus local comparison versus actual applicability.
4. Coverage/gaps/partial evidence and bounded negative statements.

**Exit criterion:** Ali can interpret a saved comparison without turning local structural evidence into a runtime/product claim.

## Checkpoint B — Understand acquisition and work budgets

Cover:

1. each budget/resource family and its purpose;
2. starvation vs capability limitation;
3. stage reservations and priority;
4. request bytes vs admitted source bytes;
5. acquisition clock vs worker clock;
6. what budget exhaustion permits us to claim.

**Exit criterion:** Ali can explain why `50 requests`, `12 module questions` and `256 candidates` are different controls and diagnose which layer stopped.

## Checkpoint C — Read the end-to-end implementation architecture

Trace real code/dataflow:

```text
repo + PR
→ native dependency inputs
→ target/source acquisition
→ retained catalog/modules
→ correspondence candidates
→ argument checker
→ saved evidence
→ cold reader/view
```

Identify owner/function boundaries and inputs/outputs, without line-by-line memorization.

**Exit criterion:** Ali can locate the likely owner when a new defect appears and can explain the main evidence flow.

## Checkpoint D — Fresh lifecycle + final execution freeze

Because main progressed during this learning session, this checkpoint now has two parts:

1. inspect and understand the implemented October31 outer-attempt lifecycle;
2. after main closes the final executable-freeze cycle, sync and inspect that exact freeze/interlock implementation.

**Exit criterion:** Ali can explain what is frozen at definition, execution and acquired-input horizons; what happens under refusal/interruption; and what explicitly authorizes/does not authorize live execution.

## Checkpoint E — First real HTTPX ordinary attempt

When explicitly activated and executed:

1. inspect actual acquisition receipts/material;
2. inspect source roles and omissions;
3. inspect candidate paths and premises;
4. inspect old/proposed argument comparisons;
5. classify procedural outcome and structural usefulness separately;
6. decide what result means for the method and for subsequent native/API/Workspace adoption.

**Exit criterion:** treat the fresh attempt as an engineering/evidence review, not a pass/fail ceremony.

## Checkpoint F — Consolidation and ownership review

After E, perform a short review across sections 1–8:

- what can Ali explain without notes?
- what can Ali follow when shown code/evidence?
- what remains reference-only?
- which newly emerged main work adds a genuinely new learning requirement?

Then either close this temporary learning branch, archive/merge only durable learning artifacts if justified, or continue with the next product phase.

---

# Main-sync protocol for this temporary learning branch

The main build is allowed to continue independently. This branch should **track learning impact**, not compete with `MEMORY.md` or become a second live-state owner.

## When to sync

Sync when one of these happens:

- a consequential `main` cycle closes;
- a new capability/owner/representation is introduced;
- a current roadmap item becomes implemented or obsolete;
- a fresh real attempt/result is produced;
- product/native adoption begins;
- before starting a new major learning checkpoint if `main` has moved materially.

Do not sync for every trivial commit.

## Sync procedure

1. Read latest `main` head and current `MEMORY.md` position.
2. Compare latest main against the **last recorded main sync SHA** below.
3. Inspect only relevant changed code/design/evidence for learning impact.
4. Classify each material change:
   - `NO LEARNING CHANGE` — implementation detail within already understood responsibility;
   - `ROADMAP UPDATE` — changes priority/status of an existing learning item;
   - `NEW LEARNING REQUIREMENT` — introduces a genuinely new concept/owner that Ali should own;
   - `REFERENCE ONLY` — useful to know exists but not worth active study now.
5. Update sections 1, 5, 8 and/or 9 as needed.
6. Append one sync-log entry with main SHA, what changed, and learning consequence.
7. Do **not** copy product-live authority into this branch or overwrite `MEMORY.md` from here.

## Branch synchronization policy

This branch does not need to mechanically merge/rebase every `main` commit. The preferred learning workflow is:

```text
main moves
→ inspect delta since last sync SHA
→ update this roadmap/learning notes with only material learning consequences
```

If later code inspection needs the newest implementation, read it directly from `main` at its exact SHA. This avoids turning a temporary learning branch into a competing product branch or creating unnecessary conflicts.

---

# Sync log

## Sync 0 — 2026-10-31

**Main SHA:** `034665d7032fed622e33149ba1977413f64a56d6`  
**Branch base:** same SHA.  
**Main position:** fresh ordinary outer-attempt lifecycle already delivered and qualified; final actual executable-freeze cycle has started; live activation still withheld.  
**Learning impact:** roadmap updated so fresh lifecycle implementation is now an active next-tier learning item, and final execution-freeze implementation is tracked as current-main work. The first live HTTPX result remains future.

**Last main sync SHA:** `034665d7032fed622e33149ba1977413f64a56d6`

---

# Next learning action

Continue with **Checkpoint A — evidence semantics**, beginning with `BOUND` / `REJECTED` / `UNDETERMINED`, then premises and bounded coverage. Before Checkpoint D or sooner if `main` closes another consequential cycle, run the sync protocol first.
