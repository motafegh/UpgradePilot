# Bounded Evidence-Gap Planner Implementation Comparison Learning Depth and Re-entry Map

**Status:** ACTIVE implementation-comparison learning-depth companion  
**Date:** 2026-08-30  
**Revision:** ordinary-Python ownership established; LangGraph learning route corrected for independent design, Graph API versus Functional API evaluation, and semantic responsibility naming  
**Parent plan:** `BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_AND_EVALUATION_PLAN.md`  
**LangGraph bounded plan:** `LANGGRAPH_BOUNDED_EVIDENCE_GAP_PLANNER_INDEPENDENT_DESIGN_IMPLEMENTATION_AND_COMPARISON_PLAN.md`  
**Current corrected research evidence:** historical proposal at `../proposals/2026-09-03_B2_X1_R4B_CORRECTED_LANGGRAPH_INDEPENDENT_RESEARCH_AND_DESIGN_PROPOSAL.md`  
**Responsibility:** own what Ali should understand now, what should deepen through repeated real use, what may remain operational/lookup-level, and what is deliberately deferred until a concrete trigger appears  

This map does not own live project position, implementation semantics, framework adoption, or architecture. `MEMORY.md` owns live continuation. Accepted specifications/architecture decisions own stable semantics/methods. Source/tests/runtime evidence establish implementation truth.

Exact historical filenames may retain old execution codes as provenance. Current learning sections and re-entry steps use semantic responsibility names only.

---

## 1. Learning doctrine for the bounded implementation comparison

This is not a detached Python/LangGraph/LangChain course.

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

## 2. Cross-implementation concepts to retain

These concepts recur across the journey and should strengthen through real use rather than repeated lectures.

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

# 3. Ordinary-Python bounded reference/control learning

**Implementation state:** COMPLETE for the bounded comparison reference.

The purpose of retaining ordinary-Python learning here is not to make it the template for LangGraph. It provides a concrete reference implementation, real engineering lessons, and concepts that may or may not reappear independently in framework implementations.

---

## 3.1 Bounded model observation and decision contract

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

## 3.2 Local model/provider boundary

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

## 3.3 Deterministic action authority

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
- time-of-check to time-of-use at practical level;
- early-return deterministic guards;
- typed admitted result vs typed admission problem.

### Re-entry trigger

When another framework independently designs its execution-authority boundary, retrieve the **problem/invariant** first. Do not assume the exact ordinary-Python class/function shape is the solution.

---

## 3.4 Execution, state consequence, trace, and replay

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

### Important framework-comparison correction

These lessons remain valuable, but the exact ordinary-Python representations:

```text
EvidenceGapInvestigationState
EvidenceGapTransitionTrace
replay_evidence_gap_transition(...)
one physical execution/transition module responsibility
```

are **implementation evidence**, not mandatory LangGraph architecture.

A framework implementation may independently converge on some of them, reuse them behind a comparison boundary, replace them, or represent their underlying responsibility differently if accepted semantics/proof remain correct.

### Deferred depth / triggers

**Event sourcing / persistent workflow architecture**  
Trigger: durable product persistence/recovery/audit responsibility appears.

**Async/concurrency**  
Trigger: real parallel investigations, streaming, concurrent effects, or race/freshness pressure appears.

---

# 4. LangGraph independent implementation/comparison learning

**Implementation state:** a bounded Graph API implementation, controlled comparison, real pydantic Python-support smoke, and framework value/cost findings now exist. `MEMORY.md` owns live continuation.

The learning responsibility is:

> Learn enough LangGraph and enough cross-implementation design reasoning to build and evaluate the same bounded UpgradePilot responsibility **naturally with LangGraph**, without treating either ordinary-Python structure or one LangGraph API paradigm as an architectural premise.

---

## 4.1 Requirement/evidence classification

Before learning framework APIs deeply, Ali should be able to distinguish four categories.

### Must master

```text
ACCEPTED FRAMEWORK-INDEPENDENT REQUIREMENT
→ every implementation must preserve it

REUSABLE PRODUCT-OWNED CAPABILITY
→ existing normal owner should be reused when the same product/domain responsibility is needed

ORDINARY-PYTHON ENGINEERING LESSON / EVIDENCE
→ a real problem, failure mode, trade-off, or proof insight that should pressure LangGraph

ORDINARY-PYTHON / PYTHON-SPECIFIC IMPLEMENTATION CHOICE
→ open to independent redesign unless another owner independently requires it
```

### Ali-owned practice

For important ordinary-Python concepts such as model projection, admission/freshness, investigation state, trace/replay, and execution/consequence cohesion, Ali should be able to ask:

```text
what problem did this solve?
is that problem framework-independent?
is an existing product owner already responsible?
what exactly is merely the Python representation?
what evidence would justify retaining a similar boundary in LangGraph?
```

---

## 4.2 LangGraph Graph API versus Functional API

### Why this comes before deep StateGraph learning

LangGraph currently offers two first-class workflow styles relevant to this responsibility:

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

Both can implement the same framework-independent EvidenceGapPlanner responsibility. Therefore shared `StateGraph` state is not a premise of LangGraph learning.

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

### Current evidence-backed position

Graph API remains the tested candidate because this responsibility has meaningful planning, authority, effect, and conclusion/control-flow boundaries, explicit topology was visible in the real pydantic run, and runtime updates produced useful observability.

Functional API remains a serious fallback because the bounded path is still small and Graph API state/type plumbing is a real cost.

Do **not** build both by default.

Reopen Functional API only if the later cross-implementation comparison cannot judge LangGraph fairly because Graph API ceremony itself remains the material uncertainty.

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

## 4.4 Graph API mechanics

### Must understand at architectural/practical depth for the tested implementation

```text
StateGraph
START / END
node work vs routing work
shared workflow state
partial state updates
input schema vs internal state vs output schema
runtime context/resources
conditional edges / Command routing
compile / invoke / stream
basic runtime update visibility
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

Do **not** begin from `EvidenceGapInvestigationState` or another ordinary-Python wrapper choice.

### Node/routing reasoning

Do not mechanically translate historical ordinary-Python implementation steps into graph nodes.

Instead ask where a real responsibility/control-flow change earns a node and whether routing belongs in a conditional edge, `Command`, or fixed edge.

### Learn when materially used

- `TypedDict`, dataclass, Pydantic, or selected schema form;
- reducers only if actual multi-writer/aggregation semantics appear;
- exact router/`Command` typing and APIs.

### Deferred

Custom reducers for hypothetical parallelism or append-only history.

Trigger: multiple writers or accumulated history becomes a selected real requirement.

---

## 4.5 Functional API mechanics — learn deeply only if the fallback is reopened

### Must understand at architectural/practical depth if selected later

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

## 4.6 Model observation and execution authority

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

The ordinary-Python control kept acquisition, interpretation, semantic consequence, and trace creation cohesive. Independent LangGraph design surfaced another useful representation:

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

The tested LangGraph design uses the explicit responsibility path:

```text
plan → authorize → investigate → conclude
```

Retain the responsibility reasoning, not the assumption that this exact topology must survive forever.

---

## 4.8 Expected outcome vs exception

### Must master

```text
expected semantic/no-action/rejection/domain outcome
!= expected operational/provider failure
!= unexpected programmer/framework exception
```

A LangGraph workflow should not convert all non-happy outcomes into exceptions merely because framework error handling exists.

Likewise it should not encode every expected outcome as a bespoke ordinary-Python typed class merely because the control implementation did so.

### Retry re-entry trigger

A real retry responsibility, measured provider instability, idempotency need, or checkpoint/resume design makes retry semantics material.

Before then, do not add generalized retry policy merely because LangGraph supports it.

---

## 4.9 Trace, observability, checkpointing, and replay

### Must understand

Separate the jobs:

```text
semantic/domain proof
workflow execution trace
framework checkpoint/history
re-execution / resume / time travel
```

The ordinary-Python control implemented one semantic trace/replay mechanism. The tested LangGraph implementation uses final-result reconstruction plus runtime update visibility; framework persistence/checkpoint/replay remains deliberately unimplemented.

Do **not** assume:

```text
LangGraph checkpoint == semantic replay
```

or:

```text
ordinary-Python EvidenceGapTransitionTrace must remain the LangGraph proof object
```

### Operational depth now

Know broadly what checkpointing/resume/time-travel do and why external work may be re-executed depending on workflow/task boundaries.

### Deferred core

- persistent checkpointers;
- thread history;
- fault-tolerant resume;
- time travel/forking.

Trigger: real crash/restart, durable pause/resume, workflow history, or recovery responsibility appears.

---

## 4.10 Runtime context/resources

### Must understand at practical design level

Some values are required by workflow code but are not evolving workflow facts, for example:

```text
model/provider client
repository client
configuration
narrow trusted current-state acquisition capability
```

LangGraph runtime context is used for these run-scoped dependencies in the tested implementation.

Important:

```text
runtime context
!= trust or authorization by itself
```

Trust comes from the owning product/domain contract and deterministic checks.

### Operational/lookup level

Exact `context_schema` / `Runtime` syntax remains lookup-assisted.

---

## 4.11 Input, internal state, and output design

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

For the production-oriented decision we want:

```text
same bounded responsibility
+ same accepted semantics
+ each approach implemented competently according to its strengths
→ compare resulting engineering quality/value
```

---

## 4.13 Ali-owned architecture decision

Ali should participate meaningfully in deciding or challenging:

```text
LangGraph API paradigm for the tested implementation
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

## 4.14 Exact APIs and syntax — lookup-assisted

For the tested Graph API implementation, exact syntax may remain lookup-assisted for:

```text
installed LangGraph version/dependency surface
StateGraph declaration
selected state-schema syntax
add_node / add_edge / Command forms used
START / END imports
Runtime/context access
compile()
invoke() / stream() behavior
basic graph debug/trace surface
```

Exact API memory is not the mastery goal. Read/modify/test/diagnose capability is.

---

## 4.15 Explicitly deferred LangGraph surface

Remain deferred until a concrete trigger appears.

### Persistent checkpointing / time travel

Trigger: real durable recovery, long-running pause/resume, workflow-history/forking requirement.

### Interrupts / Human-in-the-Loop

Trigger: an admitted human approval/input boundary materially changes execution.

### Automatic retry / generalized error handlers

Trigger: a real retry/idempotency policy responsibility appears.

### Custom reducers

Trigger: selected Graph API design has multiple writers/aggregation semantics that default overwrite cannot represent safely.

### ToolNode / generic model-tool execution

Trigger: a real tool-calling responsibility exists where model tool calls are intentionally part of the execution contract and deterministic authority remains safe/explicit.

### `create_agent`

Trigger: bounded LangChain abstraction investigation; do not consume the higher-level LangChain abstraction while evaluating lower-level LangGraph orchestration.

### Subgraphs

Trigger: independently meaningful reusable nested workflow responsibility appears.

### Parallelism / `Send`

Trigger: two or more genuinely parallelizable admitted investigations or map-reduce style work appears.

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

# 5. LangChain bounded abstraction learning

When activated, focus only on LangChain concepts intersecting the real EvidenceGapPlanner responsibility:

```text
model abstraction
create_agent / agent loop
tool definitions/calls
middleware/hooks
relationship to LangGraph runtime
retry/fallback/guardrails when materially relevant
```

### Must learn

What LangChain abstracts away, what it preserves, what it makes harder to see, and whether its defaults fit UpgradePilot's deterministic-authority/evidence semantics.

Do not learn the entire framework surface.

---

# 6. Cross-implementation comparison ownership deepening

The final comparison should deepen concepts through real evidence:

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

Ali should increasingly propose the comparison dimensions, identify misleading evidence, and challenge whether a framework mechanism actually earns retention.

---

## 7. Semantic re-entry route

When returning to this learning responsibility, use semantic checkpoints rather than historical execution codes:

```text
1. recover the ordinary-Python requirement / product-capability / lesson / Python-choice classification
2. recover the Graph API vs Functional API mental model and tested-implementation decision
3. recover workflow communication vs domain truth vs runtime-dependency distinction
4. recover only the selected-paradigm mechanics needed for the current decision
5. recover model-observation / execution-authority reasoning
6. recover effect-boundary / deterministic-consequence trade-off
7. recover expected outcome vs exception
8. recover trace/observability/checkpoint/replay job distinction
9. recover framework-neutral comparison model
10. continue with the current semantic responsibility selected by MEMORY.md
```

Do not turn re-entry into a replay of the whole historical implementation sequence.

---

## 8. Provenance

The historical comparison-boundary correction is preserved at:

`../working-memory/2026-09-03_1804_B2-X1-R4B-comparison-boundary-reframe.md`

The historical corrected research proposal is preserved at:

`../proposals/2026-09-03_B2_X1_R4B_CORRECTED_LANGGRAPH_INDEPENDENT_RESEARCH_AND_DESIGN_PROPOSAL.md`

These exact old filenames remain only as provenance and are not current learning vocabulary.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`
