# B2/X1 R4 Learning-by-Doing Depth and Re-entry Map

**Status:** ACTIVE R4 learning-depth companion  
**Date:** 2026-08-30  
**Revision:** R4-A ownership complete for the bounded ordinary-Python control; R4-B learning route corrected on 2026-09-03 to support independent LangGraph design  
**Parent plan:** `B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**R4-B bounded plan:** `B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`  
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

These concepts recur across R4 and should strengthen through real use rather than repeated lectures:

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

> Learn enough LangGraph and enough cross-implementation design reasoning to build the same bounded UpgradePilot responsibility **naturally with LangGraph**, without treating the R4-A Python classes/topology as architectural premises.

---

## 4.1 First mastery target — requirement/evidence classification

Before learning graph APIs deeply, Ali should be able to distinguish four categories.

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

This classification is the immediate R4-B1 ownership target because it determines what LangGraph is free to redesign.

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

## 4.2 LangGraph core execution model — understand before architecture freeze

### Must understand at architectural/practical depth

```text
StateGraph
→ graph builder for stateful workflow execution

START / END
→ virtual entry/termination points

node
→ one meaningful unit of work that reads available state/context and returns an update/result

edge
→ control-flow relationship

conditional edge / router
→ deterministic or programmatic next-destination selection based on current workflow information

graph state
→ shared workflow communication/state snapshot used by the selected graph design

partial state update
→ a node normally returns only changed keys/values

input schema
!= internal workflow state
!= output schema

runtime context/resources
!= evolving/shared workflow facts

compile / invoke
→ builder-to-executable boundary and one execution entry point
```

### Important correction from the superseded route

Do **not** begin with:

```text
LangGraph workflow state
!= EvidenceGapInvestigationState
```

as though the existence of the R4-A state class decides the graph model.

Instead begin with:

```text
what information must persist or communicate between meaningful LangGraph steps?
what information is trusted product/domain state?
what can be derived?
what belongs in runtime resources?
what should remain ordinary product/domain code?
```

Only then decide whether a LangGraph state should wrap an existing object, flatten selected semantic facts, use new experiment-owned types, or combine approaches.

### Operational/lookup level initially

- exact generic typing of `StateGraph`;
- exact annotation syntax;
- exact router typing;
- exact compile/invoke signatures;
- minor version-specific API details.

Learn exact syntax when the selected implementation first uses it.

---

## 4.3 State design — must reason independently

### Must master at design level

Ali should be able to reason about:

```text
what state means in our selected LangGraph design
what values need persistence between nodes
what should be derived rather than stored
what should be graph input
what should remain internal
what final output should expose
what should be runtime context instead of shared state
what is semantic/domain truth vs orchestration/intermediate data
```

The key rule is not “reuse the Python state object.” The key rule is:

> **Do not create ambiguous competing sources of accepted truth, and do not duplicate product/domain responsibility without an independent reason.**

A new LangGraph-specific state model is allowed when it is the cleanest design and does not silently fork product semantics.

### Learn when materially used

- `TypedDict`, dataclass, Pydantic, or other state-schema form actually selected;
- reducers only if the state design genuinely needs merge/accumulation semantics;
- private/internal channels only if selected.

### Deferred

Custom reducers for hypothetical parallelism or append-only history.

Trigger: multiple node writers or accumulated history becomes a real selected design requirement.

---

## 4.4 Node and routing design — must master the responsibility distinction

Do not mechanically translate:

```text
A1 → node
A3 → node
A2 → node
A4 → node
```

Instead reason:

```text
what are the meaningful workflow steps in a LangGraph-native implementation?
where does stochastic/model work occur?
where does trusted deterministic authority occur?
where do external effects occur?
which results genuinely change routing?
which operations are cohesive and which should be separated?
```

### Must master

- node work vs routing work;
- deterministic routing vs model reasoning;
- authority decision vs route selection;
- effect boundary vs pure state transformation;
- why node boundaries can matter later for retry/resume/checkpoint behavior even if those features remain deferred.

### Operational/lookup level

- exact conditional-edge syntax;
- `Command` API until/if selected.

### `Command` re-entry trigger

Use/deepen only if the selected design shows that update + goto is one genuinely cohesive responsibility and separate router functions become awkward/duplicative.

---

## 4.5 Model observation / authority in LangGraph

### Must master

The accepted security/authority idea remains:

```text
what the graph internally knows
!= what the model is allowed to observe
```

But R4-B must independently decide **where** the projection/observation boundary belongs in the graph architecture.

Ali should understand:

- framework-internal/private state does not automatically prove model-hidden authority;
- the exact prompt/request construction remains the real observation boundary;
- a model decision still cannot self-authorize an external action;
- the deterministic execution-authority mechanism may be represented differently from R4-A A2, but its accepted responsibility must remain intact.

### Design reasoning target

Ask:

```text
what trusted information exists before the model step?
what subset should be projected?
what output may the model control?
what current trusted conditions must be checked before an effect?
where should that check live in this graph?
```

Do not pre-answer those questions with R4-A file boundaries.

---

## 4.6 Expected outcome vs exception

### Must master

```text
expected semantic/no-action/rejection/domain outcome
!= unexpected programmer/framework exception
```

A graph should not convert all non-happy outcomes into exceptions merely because framework error handling exists.

Likewise it should not encode every expected outcome as a bespoke R4-A typed class merely because R4-A did so.

The selected representation should preserve semantic distinctions and remain easy to test/route.

### Learn when materially used

- LangGraph retry policy/error handling API only if selected;
- node exception behavior needed for the actual implementation.

### Retry re-entry trigger

A real retry responsibility, measured provider instability, idempotency need, or checkpoint/resume design makes retry semantics material.

Before then, do not add generalized retry policy merely because LangGraph supports it.

---

## 4.7 Trace, observability, checkpointing, replay

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

Know what checkpointing/time travel broadly do and why they can re-execute downstream work/effects.

### Deferred core

- persistent checkpointers;
- thread history;
- fault-tolerant resume;
- time travel/forking.

Trigger: real crash/restart, durable pause/resume, workflow history, or recovery responsibility appears.

---

## 4.8 Runtime context/resources

### Must understand at practical design level

Some values are required by nodes but are not evolving workflow facts, for example potentially:

```text
model/provider client
repository client
configuration
narrow trusted current-state acquisition capability
```

LangGraph provides runtime-context mechanisms for such run-scoped resources.

The exact resources should be chosen only after graph responsibilities are selected.

### Operational/lookup level

Exact `context_schema` / `Runtime` syntax until first material implementation.

---

## 4.9 Input / internal / output design

### Must master at conceptual level

A strong graph does not have to expose all internal orchestration data as its public input/output contract.

Ali should reason about:

```text
caller input
→ what the graph needs to start

internal state
→ what nodes need to communicate

final output
→ what caller/comparison/test actually needs
```

This becomes important for comparing two architectures with different internals.

### Comparison implication

The cross-implementation oracle should be a framework-neutral **observable semantic projection**, not identical internal state objects.

---

## 4.10 Framework-neutral comparison — must master

This is a central R4-B/R4-D concept.

### Must master

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
same node/function count
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

## 4.11 Ali-owned architecture decision before Build

After the prerequisites above are established, Ali should participate meaningfully in deciding:

```text
graph responsibility/non-responsibility
input boundary
state model
runtime resources
node responsibilities
routing/termination
execution-authority placement
external-effect boundary
final output/comparison projection
proof/observability strategy
features deliberately deferred
```

This is not a quiz gate. The decision happens after enough LangGraph mental model exists to make the alternatives meaningful.

---

## 4.12 Learn when first implemented materially

Only after architecture freeze, learn exact APIs/syntax actually used by the graph:

```text
installed LangGraph version/dependency surface
StateGraph declaration
actionable state-schema syntax
add_node / add_edge / add_conditional_edges forms used
START / END imports
Runtime/context access if selected
compile()
invoke() / stream() behavior actually used
basic graph debug/trace surface needed for proof
```

Exact API memory is not the mastery goal. Read/modify/test/diagnose capability is.

---

## 4.13 Explicitly deferred LangGraph surface

Remain deferred until the stated trigger appears.

### Persistent checkpointing / time travel

Trigger: real durable recovery, long-running pause/resume, workflow-history/forking requirement.

### Interrupts / Human-in-the-Loop (HITL)

Trigger: an admitted human approval/input boundary materially changes execution.

### Automatic retry / generalized error handlers

Trigger: a real retry/idempotency policy responsibility appears.

### Custom reducers

Trigger: selected graph has multiple writers/aggregation semantics that default overwrite cannot represent safely.

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

---

# 5. R4-C — LangChain bounded learning

**State:** DEFERRED until R4-B lower-level graph mechanics and comparison are understood enough to judge the abstraction.

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
state/control-flow clarity
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
2. StateGraph execution model
3. state/context/input/internal/output distinctions
4. node/routing/effect/authority reasoning
5. expected outcome vs exception
6. trace/observability/checkpoint/replay job distinction
7. framework-neutral comparison model
8. jointly selected independent LangGraph architecture
```

Then stop Planning/Design and hand off to Build/Implement.

---

## 8. Provenance

The R4-B learning-route correction is detailed in:

`../working-memory/2026-09-03_1804_B2-X1-R4B-comparison-boundary-reframe.md`

The superseded earlier R4-B working-memory reasoning remains useful provenance for how the over-constrained candidate emerged.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`
