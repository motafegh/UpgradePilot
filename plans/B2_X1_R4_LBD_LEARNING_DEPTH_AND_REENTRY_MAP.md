# B2/X1 R4 Learning-by-Doing Depth and Re-entry Map

**Status:** ACTIVE R4 learning-depth companion  
**Date:** 2026-08-30  
**Revision:** R4-A ownership complete; R4-B learning route corrected on 2026-09-03 for independent LangGraph design and then refined to evaluate Graph API vs Functional API before StateGraph-specific learning  
**Parent plan:** `B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**R4-B bounded plan:** `B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`  
**Current corrected research evidence:** `../proposals/2026-09-03_B2_X1_R4B_CORRECTED_LANGGRAPH_INDEPENDENT_RESEARCH_AND_DESIGN_PROPOSAL.md`  
**Responsibility:** own what Ali should understand now, what should deepen through repeated real use, what may remain operational/lookup-level, and what is deliberately deferred until a concrete trigger appears  

This map does not own live project position, implementation semantics, framework adoption, or architecture. `MEMORY.md` owns live continuation. Accepted specifications/ADRs own stable semantics/methods. Source/tests/runtime evidence establish implementation truth.

---

## 1. Learning doctrine for R4

R4 is not a detached Python/LangGraph/LangChain course.

Use the real responsibility:

```text
EvidenceGapPlanner / bounded agentic investigation
→ identify the next material evidence gap
→ select one useful bounded action or explicit no-action outcome
→ preserve deterministic authority and evidence semantics
→ execute only when admitted
→ inspect/update knowledge honestly
```

For each concept classify depth proportionately:

```text
MUST MASTER
→ central mechanism Ali should be able to explain, challenge, test, diagnose, and later direct/modify

UNDERSTAND OPERATIONALLY
→ material mechanism Ali should recognize/use safely; exact syntax/API may remain lookup-assisted

DEFERRED CORE
→ important later but not required for the current decision

OPTIONAL EXPLORATION
→ interesting but not part of the active dependency chain
```

The depth assigned to one concept may increase later when repeated real use makes deeper ownership valuable.

---

## 2. Cross-stage concepts to retain

These concepts recur across R4 and should strengthen through real use rather than repeated lectures.

### Must master across the journey

```text
model output / proposal
!= deterministic execution authority

model-visible context
!= hidden trusted execution data

semantic/domain result
!= provider/operational failure
!= unexpected implementation defect

current trusted state at execution boundary
!= stale observation used to ask the model

existing implementation
= evidence
!= architecture authority

product/domain owner
!= experiment/framework orchestration owner

workflow communication/runtime mechanism
!= product/domain truth

passing test
= evidence for exercised behavior
!= proof of architectural necessity
```

### Understand operationally and deepen when repeated

```text
structured output contracts
prompt/context projection
boundary-oriented failure classification
immutable state/value replacement patterns
trace/observability evidence
controlled comparison and semantic projection
```

---

# 3. R4-A — ordinary-Python reference/control

**Implementation state:** COMPLETE for the bounded comparison reference.

The purpose of retaining R4-A learning here is not to make it the template for LangGraph. It provides a concrete reference implementation, real engineering lessons, and concepts that may or may not reappear independently in R4-B.

---

## 3.1 R4-A1 — model observation / decision contract

### Learned at practical ownership depth

Ali should retain the ability to recover:

```text
why the model receives a bounded explicit context
what is intentionally hidden from the model
why structured output/schema is useful but not semantic authority
how a valid EvidenceGapDecision remains an untrusted proposal
how boundary dataclasses/types protect local coherence without becoming upstream truth owners
```

Important mechanisms encountered:

- dataclass/type representation at practical level;
- `Literal`/union concepts at practical recognition level;
- explicit projection/rendering;
- JSON Schema vs parser/cross-field validation;
- structured planning evidence;
- exact hidden-key/projection testing.

### Operational/lookup level

- exact `dataclasses` internals;
- advanced typing machinery;
- JSON-Schema implementation internals.

### Re-entry trigger

Reopen deeper type/schema/projection design when a later framework or product boundary materially changes what the model can observe or return.

---

## 3.2 R4-A3 — local model/provider boundary

### Learned at practical ownership depth

Ali should retain:

```text
planner context
→ explicit request/prompt
→ local OpenAI-compatible/LM Studio call
→ provider envelope
→ structured model content
→ strict parse
→ typed decision OR typed invocation problem
```

And the separation:

```text
provider/transport failure
!= structured-output failure
!= semantically poor but valid decision
!= deterministic execution rejection
```

Important practical mechanisms:

- `Mapping[str, Any]` as an untrusted input boundary;
- runtime narrowing;
- JSON serialization/deserialization;
- `requests.Session` / POST / timeout at practical level;
- structured outputs;
- try/except → typed problem translation;
- prompt/context engineering for the exact responsibility.

### Operational/lookup level

- requests/HTTP stack internals;
- advanced dependency-injection typing;
- exact provider API details not used by the experiment.

### Re-entry triggers

- second provider/model becomes genuinely required;
- connection/TLS/proxy/streaming behavior becomes a real engineering issue;
- retry/backoff becomes a real policy responsibility;
- evaluation shows prompt/context quality is the material bottleneck.

---

## 3.3 R4-A2 — deterministic action authority

### Learned at practical ownership depth

Ali should retain:

```text
model selects stable action identity
→ trusted implementation rebinds it
→ current execution conditions are checked
→ exact hidden action authority is established or rejected
```

Important concepts:

- proposal/recommendation != authorization;
- stable-ID rebinding;
- consumed-action suppression;
- planning-budget check;
- current precondition/policy check;
- TOCTOU (time-of-check to time-of-use) at practical level;
- early-return deterministic guards;
- typed admitted result vs typed admission problem.

### Re-entry trigger

When R4-B independently designs its execution-authority boundary, retrieve the **problem/invariant** first. Do not assume the exact A2 class/function/node shape is the solution.

---

## 3.4 R4-A4 — execution / state consequence / trace / replay

### Learned at practical ownership depth

Ali should retain:

```text
bounded execution
→ valid semantic evidence OR expected operational failure
→ correct budget/action-consumption consequence
→ domain interpretation/update
→ inspectable before/outcome/after evidence
```

Important concepts:

- state-machine/transition reasoning;
- budget decrement timing;
- action-consumption timing;
- immutable state replacement;
- semantic result vs operational failure;
- trace/event record as proof/debug evidence;
- replay as deterministic reconstruction rather than blind external re-execution.

### Important correction for R4-B

These lessons remain valuable, but the exact R4-A representations:

```text
EvidenceGapInvestigationState
EvidenceGapTransitionTrace
replay_evidence_gap_transition(...)
A4 as one physical function/module responsibility
```

are **implementation evidence**, not mandatory LangGraph architecture.

R4-B may independently converge on some of them, reuse them, replace them, or represent their underlying responsibility differently if accepted semantics/proof remain correct.

### Deferred depth / triggers

**Event sourcing / persistent workflow architecture**  
Trigger: durable product persistence/recovery/audit responsibility appears.

**Async/concurrency**  
Trigger: real parallel investigations, streaming, concurrent effects, or race/freshness pressure appears.

---

# 4. R4-B — LangGraph independent implementation/comparison

**Implementation state:** DESIGN-LEARNING ACTIVE; no LangGraph source implementation yet.

The corrected learning responsibility is:

> Learn enough LangGraph and enough cross-implementation design reasoning to build the same bounded UpgradePilot responsibility **naturally with LangGraph**, without treating either R4-A's Python structure or one LangGraph API paradigm as an architectural premise.

---

## 4.1 First mastery target — requirement/evidence classification

Before learning framework APIs deeply, Ali should be able to distinguish four categories.

### Must master

```text
ACCEPTED FRAMEWORK-INDEPENDENT REQUIREMENT
→ every implementation must preserve it

REUSABLE PRODUCT-OWNED CAPABILITY
→ existing normal owner should be reused when the same product/domain responsibility is needed

R4-A ENGINEERING LESSON / EVIDENCE
→ a real problem, failure mode, trade-off, or proof insight that should pressure R4-B

R4-A / PYTHON-SPECIFIC IMPLEMENTATION CHOICE
→ open to independent redesign unless another owner independently requires it
```

This classification remains the immediate R4-B1 ownership target because it determines what LangGraph is free to redesign.

### Ali-owned practice

For important R4-A concepts such as model projection, admission/freshness, investigation state, trace/replay, and A4 cohesion, Ali should be able to ask:

```text
what problem did this solve?
is that problem framework-independent?
is an existing product owner already responsible?
what exactly is merely the Python representation?
what evidence would justify retaining a similar boundary in LangGraph?
```

---

## 4.2 R4-B2A — Graph API vs Functional API

### Why this now comes before deep StateGraph learning

The corrected independent research established that LangGraph currently offers two first-class workflow styles relevant to this responsibility:

```text
GRAPH API
→ StateGraph
→ explicit graph topology
→ nodes + edges / dynamic routing
→ explicit shared workflow communication/state
→ static visualization and inspectable structure

FUNCTIONAL API
→ @entrypoint + optional @task
→ ordinary Python control flow
→ local workflow values rather than requiring a shared graph-state schema
→ LangGraph runtime/durability model with lower structural ceremony
```

Both can implement the same framework-independent EvidenceGapPlanner responsibility. Therefore shared `StateGraph` state is no longer a premise of R4-B learning.

### Must master at design level

Ali should be able to explain:

```text
what structural commitment Graph API adds
what ceremony it costs
why explicit authority/effect/routing visibility could be valuable here

what Functional API keeps procedural
what ceremony it avoids
why a small bounded workflow may fit it naturally

why either API can preserve:
→ bounded model observation
→ proposal != authority
→ current pre-effect authorization
→ explicit no-action/rejection/failure semantics
→ deterministic consequence proof
```

### Current research position — not architecture authority

The corrected proposal's strongest candidate is Graph API because this responsibility already has meaningful planning, authority, effect, and conclusion/control-flow boundaries and credible future action-family/replanning pressure.

Functional API is a serious fallback/alternative because today's bounded path remains small and may not justify explicit state/topology plumbing.

Do **not** build both by default.

### Decision evidence

Graph API should earn selection through present value such as:

- trust/effect boundary visibility;
- routing/control-flow clarity;
- inspectable workflow communication;
- test/debug/observability leverage;
- change locality under already-known future growth.

Functional API should gain weight if:

- Graph API state plumbing dominates the implementation;
- several intermediate workflow values exist only to satisfy graph ceremony;
- static topology adds little understanding/proof value;
- the responsibility remains naturally procedural.

### Operational/lookup depth now

- exact `StateGraph` generic syntax;
- exact `@entrypoint`/`@task` decorator signatures;
- minor version-specific APIs.

Learn exact syntax only after the paradigm decision/implementation makes it material.

---

## 4.3 Workflow communication vs domain truth vs runtime dependencies

This is the deeper cross-API concept.

### Must master

Ali should reason in three distinct categories:

```text
WORKFLOW COMMUNICATION / EVOLVING VALUES
→ information one responsibility produces that later workflow logic genuinely needs

PRODUCT / DOMAIN TRUTH
→ established semantic facts/capabilities owned by UpgradePilot product/domain modules

RUN-SCOPED DEPENDENCIES / RESOURCES
→ model/provider client, repository client, configuration, trusted current-state supplier, etc.
```

The core rule is:

> **Do not create ambiguous competing sources of accepted truth, and do not put a value into framework-managed workflow state merely because it exists during execution.**

Graph API may express workflow communication through shared state/channels. Functional API may express much of it through local values and task/entrypoint results. The responsibility distinction survives either implementation style.

### Important freshness implication

Current deterministic authority information should not be precomputed before the model call and later mislabeled current merely because it was stored in workflow state/local variables.

The currentness requirement is:

```text
model proposal exists
→ obtain/check sufficiently current trusted execution conditions
→ authorize or reject
→ only then external effect may occur
```

Exact representation remains open.

---

## 4.4 Graph API mechanics — learn deeply only if Graph API remains selected

### Must understand at architectural/practical depth if selected

```text
StateGraph
START / END
node work vs routing work
shared workflow state
partial state updates
input schema vs internal state vs output schema
runtime context/resources
conditional edges
Command for cohesive update + goto when justified
compile / invoke
basic trace/stream visibility
```

### State-design reasoning

Ask:

```text
what values really need to cross node boundaries?
what should be derived rather than stored?
what should be graph input?
what should remain internal?
what final output should expose?
what should be runtime context rather than shared state?
```

Do **not** begin from `EvidenceGapInvestigationState` or any R4-A wrapper choice.

### Node/routing reasoning

Do not mechanically translate:

```text
A1 → node
A3 → node
A2 → node
A4 → node
```

Instead ask where a real responsibility/control-flow change earns a node and whether routing belongs in a conditional edge, `Command`, or fixed edge.

### Learn when materially used

- `TypedDict`, dataclass, Pydantic, or selected schema form;
- reducers only if actual multi-writer/aggregation semantics appear;
- exact router/`Command` typing and APIs.

### Deferred

Custom reducers for hypothetical parallelism or append-only history.

Trigger: multiple writers or accumulated history becomes a selected real requirement.

---

## 4.5 Functional API mechanics — learn deeply only if Functional API becomes selected

### Must understand at architectural/practical depth if selected

```text
@entrypoint
→ workflow execution boundary

ordinary Python if/return control flow
→ main routing mechanism

local workflow values
→ communication between sequential responsibilities without a shared StateGraph schema

@task
→ independently managed task boundary only when durability/concurrency/trace/side-effect needs justify it

runtime context / dependencies
→ run-scoped resources remain separate from semantic truth

return value
→ final public workflow result
```

### Critical proportionality rule

Do not wrap every helper in `@task` merely because the API supports it. Without a current durability/concurrency/retry responsibility, ordinary helpers may be the cleaner implementation.

### Comparison pressure

If Functional API becomes so close to ordinary Python that LangGraph adds little material capability/clarity for this responsibility, that is valid negative evidence for framework adoption rather than a reason to manufacture framework usage.

---

## 4.6 Model observation / execution authority

### Must master

The accepted security/authority idea remains:

```text
what workflow code internally knows
!= what the model is allowed to observe

model proposal
!= executable authority
```

Ali should understand:

- framework-internal/private state or local variables do not automatically prove model-hidden authority;
- the exact prompt/request construction remains the real observation boundary;
- a model decision still cannot self-authorize an external action;
- sufficiently current deterministic execution authority must be established after proposal and before effect;
- this requirement does **not** automatically require a dedicated authorization node or task.

### Design reasoning target

Ask:

```text
what trusted information exists before the model step?
what subset should be projected?
what output may the model control?
what current trusted conditions must be checked before an effect?
what physical boundary best exposes/proves that responsibility in the selected API?
```

---

## 4.7 Effect boundary vs deterministic consequence

### Must understand at design level

R4-A kept acquisition, interpretation, semantic consequence, and trace creation cohesive in A4. Corrected research independently surfaced another credible design:

```text
external investigation effect
→ valid semantic observation OR expected operational failure
→ separate pure deterministic consequence/finalization
```

Potential present value:

- isolates external I/O from pure semantic rules;
- makes budget/consumption/continuation consequence easier to test/reconstruct;
- gives retry/persistence reasoning a cleaner effect boundary if later admitted.

Potential cost:

- extra node/task/helper/intermediate value;
- risk of inventing generic observation abstractions for one current action.

### Current learning rule

Understand the trade-off; do not treat the four-stage `plan → authorize → investigate → conclude` proposal as selected architecture yet.

Reopen cohesion if the intermediate representation is mostly ceremony.

---

## 4.8 Expected outcome vs exception

### Must master

```text
expected semantic/no-action/rejection/domain outcome
!= expected operational/provider failure
!= unexpected programmer/framework exception
```

A LangGraph workflow should not convert all non-happy outcomes into exceptions merely because framework error handling exists.

Likewise it should not encode every expected outcome as a bespoke R4-A typed class merely because R4-A did so.

### Retry re-entry trigger

A real retry responsibility, measured provider instability, idempotency need, or checkpoint/resume design makes retry semantics material.

Before then, do not add generalized retry policy merely because LangGraph supports it.

---

## 4.9 Trace, observability, checkpointing, replay

### Must understand before design freeze

Separate the jobs:

```text
semantic/domain proof
workflow execution trace
framework checkpoint/history
re-execution / resume / time travel
```

R4-A implemented one semantic trace/replay mechanism. R4-B may reuse it or may use a different semantic proof representation if the same proof need remains and the new design is cleaner.

Do **not** assume:

```text
LangGraph checkpoint == semantic replay
```

or:

```text
R4-A EvidenceGapTransitionTrace must remain the R4-B proof object
```

### Operational depth now

Know broadly what checkpointing/resume/time-travel do and why external work may be re-executed depending on the workflow/task boundary.

### Deferred core

- persistent checkpointers;
- thread history;
- fault-tolerant resume;
- time travel/forking.

Trigger: real crash/restart, durable pause/resume, workflow history, or recovery responsibility appears.

---

## 4.10 Runtime context/resources

### Must understand at practical design level

Some values are required by workflow code but are not evolving workflow facts, for example potentially:

```text
model/provider client
repository client
configuration
narrow trusted current-state acquisition capability
```

LangGraph runtime-context mechanisms are candidates for these run-scoped dependencies.

Important:

```text
runtime context
!= trust or authorization by itself
```

Trust comes from the owning product/domain contract and deterministic checks.

### Operational/lookup level

Exact `context_schema` / `Runtime` syntax until first material implementation.

---

## 4.11 Input / internal / output design

### Must master at conceptual level

A strong workflow does not have to expose all internal orchestration data as its public input/output contract.

Ali should reason about:

```text
caller input
→ what the workflow needs to start

internal communication/local values
→ what later responsibilities genuinely need

final output
→ what caller/comparison/test actually needs
```

Graph API may formalize input/internal/output schemas. Functional API may express the distinction through entrypoint arguments, local values/task results, and return value.

### Comparison implication

The cross-implementation oracle should be a framework-neutral **observable semantic projection**, not identical internal state objects.

---

## 4.12 Framework-neutral comparison — must master

A valid architecture comparison can hold the responsibility/evidence constant while permitting different internals.

Use controlled scenarios and compare observable consequences such as:

```text
action/no-action/rejection outcome
whether execution occurred
current deterministic authority result
budget consequence
consumed-action consequence
final domain/applicability conclusion
semantic vs operational failure class
forbidden external-call absence
semantic consequence reproducibility/testability
```

Do not require:

```text
Python state object == LangGraph state object
Python trace object == LangGraph trace object
same node/function/task count
same module boundaries
```

### Must also understand

Architecture comparison has a different purpose from a microbenchmark with one isolated variable.

For the production-oriented R4 decision we want:

```text
same bounded responsibility
+ same accepted semantics
+ each approach implemented competently according to its strengths
→ compare resulting engineering quality/value
```

---

## 4.13 Ali-owned architecture decision before Build

After the prerequisites above are established, Ali should participate meaningfully in deciding:

```text
LangGraph API paradigm for the first implementation
a serious alternative/reassessment trigger
workflow responsibility/non-responsibility
input boundary
workflow communication/value model
runtime resources
meaningful work/control-flow responsibilities
routing/termination
execution-authority placement
external-effect boundary
final output/comparison projection
proof/observability strategy
features deliberately deferred
```

This is not a quiz gate. The decision happens after enough mental model exists to make the alternatives meaningful.

---

## 4.14 Learn when first implemented materially

Only after architecture freeze, learn exact APIs/syntax actually used.

If Graph API is selected:

```text
installed LangGraph version/dependency surface
StateGraph declaration
selected state-schema syntax
add_node / add_edge / add_conditional_edges and/or Command forms used
START / END imports
Runtime/context access if selected
compile()
invoke() / stream() behavior actually used
basic graph debug/trace surface needed for proof
```

If Functional API is selected:

```text
installed LangGraph version/dependency surface
entrypoint declaration
task declaration only where selected
runtime/context access
invoke/stream behavior actually used
basic workflow trace/debug surface needed for proof
```

Exact API memory is not the mastery goal. Read/modify/test/diagnose capability is.

---

## 4.15 Explicitly deferred LangGraph surface

Remain deferred until the stated trigger appears.

### Persistent checkpointing / time travel

Trigger: real durable recovery, long-running pause/resume, workflow-history/forking requirement.

### Interrupts / Human-in-the-Loop (HITL)

Trigger: an admitted human approval/input boundary materially changes execution.

### Automatic retry / generalized error handlers

Trigger: a real retry/idempotency policy responsibility appears.

### Custom reducers

Trigger: selected Graph API design has multiple writers/aggregation semantics that default overwrite cannot represent safely.

### ToolNode / generic model-tool execution

Trigger: a real tool-calling responsibility exists where model tool calls are intentionally part of the execution contract and deterministic authority remains safe/explicit.

### `create_agent`

Trigger: R4-C; do not consume the higher-level LangChain abstraction during R4-B.

### Subgraphs

Trigger: independently meaningful reusable nested workflow responsibility appears.

### Parallelism / `Send`

Trigger: 2+ genuinely parallelizable admitted investigations or map-reduce style work appears.

### Automatic multi-turn / graph back-edge

Trigger: richer planner reactivation criteria in the parent plan are met.

### Persistent Store / cross-thread memory

Trigger: durable cross-run memory becomes an admitted product responsibility.

### Advanced streaming

Trigger: product/UI/debug behavior needs incremental event/token/state delivery.

### LangSmith as required proof

Trigger: external tracing/evaluation service becomes materially useful and accepted for the proof/operational boundary.

### Second LangGraph API implementation

Trigger: implementation evidence leaves framework value ambiguous specifically because the selected API's ceremony/structure may be driving the result.

Do not build both APIs merely for exposure.

---

# 5. R4-C — LangChain bounded learning

**State:** DEFERRED until R4-B lower-level LangGraph mechanics and comparison are understood enough to judge the abstraction.

When activated, focus on only the LangChain concepts intersecting the real responsibility:

```text
model abstraction
create_agent / agent loop
tool definitions/calls
middleware/hooks
relationship to LangGraph runtime
retry/fallback/guardrails when materially relevant
```

### Must learn then

What LangChain abstracts away, what it preserves, what it makes harder to see, and whether its defaults fit UpgradePilot's deterministic-authority/evidence semantics.

Do not learn the entire framework surface.

---

# 6. R4-D — comparison ownership deepening

R4-D should deepen concepts through real evidence:

```text
semantic-equivalence reasoning
architecture comparison
API-paradigm fit
workflow/state/control-flow clarity
trust/authority review
failure classification
observability/debugging
framework overhead/value
future growth fitness
```

By R4-D, Ali should increasingly propose the comparison dimensions, identify misleading evidence, and challenge whether a framework mechanism actually earns retention.

---

## 7. Current continuation gate

Before LangGraph Build begins, the learning path should establish proportionately:

```text
1. R4-A requirement / product-capability / lesson / Python-choice classification
2. Graph API vs Functional API mental model and first-implementation decision
3. workflow communication vs domain truth vs runtime-dependency distinction
4. selected-paradigm mechanics only to the depth needed for architecture
5. model-observation / execution-authority reasoning
6. effect-boundary / deterministic-consequence trade-off
7. expected outcome vs exception
8. trace/observability/checkpoint/replay job distinction
9. framework-neutral comparison model
10. jointly selected independent LangGraph architecture
```

Then stop Planning/Design and hand off to Build/Implement.

---

## 8. Provenance

The R4-B comparison-boundary correction is detailed in:

`../working-memory/2026-09-03_1804_B2-X1-R4B-comparison-boundary-reframe.md`

The current API-paradigm refinement is informed by:

`../proposals/2026-09-03_B2_X1_R4B_CORRECTED_LANGGRAPH_INDEPENDENT_RESEARCH_AND_DESIGN_PROPOSAL.md`

The superseded earlier R4-B working-memory reasoning and 2026-09-02 proposal remain historical provenance.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`