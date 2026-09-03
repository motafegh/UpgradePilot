# B2/X1 R4 Learning-by-Doing Depth and Re-entry Map

**Status:** ACTIVE COMPANION TO THE SELECTED R4 IMPLEMENTATION PLAN  
**Date:** 2026-08-31 / updated 2026-09-03  
**Primary plan:** `B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**R4-B bounded plan:** `B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`  
**Responsibility:** record what implementation concepts Ali should understand now, what should be learned when first used materially, and what should remain deferred until a concrete project trigger makes deeper study useful.

---

## 1. Why this companion exists

The main implementation plan owns **what project stage happens next**. This companion owns **when learning depth should increase while those stages are implemented**.

The rule is:

```text
real implementation responsibility appears
→ identify concepts actually carrying that responsibility
→ learn the minimum complete depth needed to understand/own the current step
→ implement and inspect real evidence
→ deepen only when later code makes the deeper mechanism materially useful
```

Do not depend on chat memory to recall a deferred topic. A deferred topic should have a concrete **re-entry trigger**.

Do not turn this map into a fixed syllabus. New concepts may be added when real implementation exposes them; irrelevant entries may remain deferred indefinitely.

---

## 2. Learning-depth vocabulary

### UNDERSTAND NOW

Needed to read, reason about, modify, or validate the current implementation responsibility.

### LEARN WHEN FIRST USED MATERIALLY

Do not pre-study deeply. Stop briefly when the real code first relies on the concept, establish the minimum-complete model, then continue implementation.

### DEFER UNTIL TRIGGER

Interesting or potentially useful, but deeper study would currently be detached from the implementation responsibility. Reopen only when the listed trigger occurs.

### MASTER THROUGH REPEATED USE

Central concept that should become increasingly independent through later implementation/testing/debugging rather than one lecture.

These depth labels are about **engineering ownership**, not memorizing every syntax form. A concept can be important enough to understand while its implementation internals remain lookup-level knowledge. Mastery should be earned through repeated design, review, testing, debugging, comparison, and explanation across real project slices—not through stopping the project until every line can be reproduced from memory.

---

# 3. R4-A1 — model boundary / typed context / explicit projection

**Implementation state:** COMPLETE; focused runtime proof PASS (10/10 A1 tests; preserved in the latest 47/47 combined A1+A2+A3+composition+A4 run).

## Understand now

These are directly visible in the R4-A1 source and should be readable before the implementation grows substantially:

```text
@dataclass
frozen=True
slots=True at practical level
basic type annotations
X | None
tuple[X, ...]
Literal[...]
__post_init__
ValueError for contract violations
nested dict/list construction
list comprehensions
explicit request projection
JSON Schema vs Python parser responsibility
```

Required depth is practical, not implementation-internals depth.

The focused runtime repair also established one practical testing lesson that should remain readable now:

```text
assert the semantic structure/proposition owned by the test
!= search an incidental serialized substring

understand where information lives in the representation
before asserting about keys vs values
```

## Master through repeated use

```text
typed data/state modeling
runtime invariants
explicit model-observation projection
trusted internal state != model-visible state
wire-shape validation != execution authorization
focused tests as explicit proof propositions
```

These are central to the agent architecture and should recur through R4-A2/A3/A4, LangGraph, and replay work.

## Defer until trigger

### Dataclass implementation internals / descriptor protocol / deep `slots` mechanics

**Trigger:** reopen only if object-layout behavior, inheritance, serialization, performance, or framework integration creates a real dataclass/slots problem.

### Advanced Python typing (`TypeVar`, `Generic`, variance, protocols in depth)

**Trigger:** reopen when a real reusable abstraction requires parameterized types or structural interfaces and ordinary concrete types become repetitive/unclear.

### Deep copy/object identity internals

**Trigger:** reopen if mutable nested state, aliasing, checkpoint/replay behavior, or graph state produces an actual copy/identity bug or design decision.

### JSON Schema specification depth

**Trigger:** reopen when provider compatibility, conditional schema constraints, schema evolution, or structured-output limitations cannot be handled by the current simple three-field schema.

### Pydantic-vs-dataclass framework comparison

**Trigger:** reopen when validation/serialization/model-provider integration creates enough duplicated manual boundary code that an alternative data-model framework becomes a real candidate.

---

# 4. R4-A2 — deterministic action rebinding/admission

**Implementation state:** COMPLETE; focused runtime proof PASS (13/13 A2 tests; preserved in the latest 47/47 combined A1+A2+A3+composition+A4 run).

## Understand now / continue mastering through use

These concepts were introduced against the real admission code and should now be understandable at practical ownership depth:

```text
lookup by stable action ID
trusted action rebinding
early-return validation flow
typed admitted-result vs typed problem result
closed reason/status vocabulary
current-state/precondition checks
policy guard
stale-state revalidation
TOCTOU (time-of-check to time-of-use)
defense in depth
proposal/recommendation != authorization
```

Python syntax/patterns actually encountered:

```text
small result dataclasses / union-style result types
Python 3.12 `type Alias = A | B`
Literal problem reason codes
early returns
small lookup/helper functions
next(..., None) generator lookup at recognition/practical level
```

A `dict`-based action index was not required for the one-action seam; the current small lookup remains proportionate. Revisit indexed mappings only if the real catalog grows enough for it to improve clarity/performance.

## Master through repeated use

```text
model-selected action ID is untrusted proposal
trusted catalog owns executable identity
admission must use latest trusted state
hidden locator/preconditions remain deterministic
planning-time validity != execution-time authorization
```

## Defer until trigger

### Advanced authorization/policy framework design

**Trigger:** only if several independently different policy classes/actions make simple deterministic checks duplicated or brittle.

### General rule engine

**Trigger:** only if real action preconditions become numerous/compositional enough that explicit bounded checks materially fail maintainability. Do not build for the one-action seam.

---

# 5. R4-A3 — bounded local model request/response seam

**Implementation state:** COMPLETE for the first bounded slice; 13/13 A3 tests PASS, real-flow composition coverage PASS, and one real S001 LM Studio selection plus fresh A2 admission PASS. Broad planner semantic quality remains unproven.

## Understand now / ownership re-entry

Learn these against the actual implemented A3 source and its place between A1 and A2:

```text
Mapping[str, Any] as untrusted input boundary
runtime type narrowing with isinstance
JSON serialization with json.dumps
JSON deserialization with json.loads
local LM Studio/OpenAI-compatible request structure
structured outputs / schema-constrained generation
provider response envelope vs model-owned message content
provider response parsing
requests.Session / POST / timeout at practical level
Session.trust_env = False for the loopback boundary
try/except and exception-to-typed-problem translation
provider/model invocation failure vs semantic decision failure
completion truncation as a distinct invocation outcome
timeout/retry boundary at practical level
prompt/context engineering for the exact planner responsibility
Callable[..., Response] / injected HTTP-post function at practical recognition level
```

The goal is not to memorize every `requests` or typing API. Ali should be able to trace what enters `LocalEvidenceGapPlanner.decide(...)`, how the request is formed, where provider failures are classified, how model content is decoded and parsed, what result comes out, and why the result still has no execution authority.

Use runtime responsibility order for the active re-entry:

```text
A1 planner/context boundary
→ what the model is allowed to see and what decision shape may return

A3 model/provider boundary
→ how one untrusted decision is requested and recovered

A2 admission boundary
→ how a selected action ID is rebound to trusted executable authority
```

Learn the concrete LM Studio/OpenAI-compatible request form actually used by the experiment, not a broad provider API course.

## Master through repeated use

```text
untrusted external/model data
→ parse/validate
→ typed decision
```

and:

```text
model semantic responsibility
!= provider transport responsibility
!= deterministic execution authority
```

Also deepen over later slices:

```text
boundary-oriented failure classification
explicit context/prompt projection
structured-output contracts
safe model-to-deterministic-control handoff
```

These are higher-value AI/agent engineering responsibilities than memorizing provider-library syntax.

## Defer until trigger

### `requests` implementation internals / HTTP stack depth

**Trigger:** reopen when connection pooling, adapters, proxies, TLS, streaming, transport debugging, or performance materially affects a real UpgradePilot provider decision.

### Generic multi-provider abstraction

**Trigger:** a second provider/model must genuinely be supported or provider-specific code materially obstructs the experiment comparison.

### Sophisticated retry/backoff libraries

**Trigger:** real provider failures/retry policy become frequent or complex enough that explicit bounded retry handling is no longer adequate.

### Deep prompt-optimization framework

**Trigger:** repeated evaluation shows prompt/context design is a measurable planner-quality bottleneck that cannot be addressed by small explicit revisions.

### Advanced `Callable`, protocol, or dependency-injection typing

**Trigger:** several interchangeable provider/adaptor implementations make the current small callable seam unclear or insufficient.

---

# 6. R4-A4 — no-tool/action transition, execution/update seam, trace/replay

**Implementation state:** COMPLETE for the first bounded ordinary-Python baseline responsibility: 7/7 dedicated A4 tests, 47/47 combined focused tests, one real S001 execution/update/trace/replay PASS, and the guided post-action ownership closure completed. R4-A is accepted as a coherent comparison baseline; this is not a product adoption decision.

## Learned at practical ownership depth

```text
state machine / transition model
planner state vs execution state
budget decrement timing
consumed-action update timing
immutable-state replacement/update patterns
execution result → domain interpretation → trusted state update
trace/event record design
replay and deterministic comparison
operational failure vs domain/evidence result
```

The ownership closure also established:

```text
A1 → expose bounded planner context while hiding execution authority
A3 → untrusted model proposal
A2 → fresh deterministic authorization
A4 → execute/interpret/transition
Trace → preserve one complete transition
Replay → reconstruct deterministic state consequence without external re-execution
```

## Defer until trigger

### Event sourcing / full workflow persistence architecture

**Trigger:** replay/checkpoint requirements become durable product responsibilities rather than experiment trace needs.

### Async/concurrency depth

**Trigger:** real parallel investigations, streaming, concurrent provider operations, or race/freshness problems appear. Do not pre-build async complexity for a sequential seam.

---

# 7. R4-B — LangGraph implementation/comparison

**Implementation state:** ACTIVE DESIGN-LEARNING ENTRY; R4-A is a coherent baseline, the current LangGraph/LangChain research proposal has been reviewed, and the bounded R4-B plan now owns the evidence-refined route. No LangGraph source has been implemented yet.

**Bounded plan:** `B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`

## Understand before the R4-B architecture freeze

These are decision-critical now because misunderstanding them could change graph ownership, authority, proof, or state shape:

```text
LangGraph workflow state
!= UpgradePilot trusted investigation/domain state

StateGraph at practical execution-model depth
START / END
nodes as work/state-update steps
edges as control-flow relationships
conditional edges / pure routing
compile/invoke flow

partial state updates
→ node returns changed workflow values rather than reconstructing every state field
→ default singleton overwrite semantics at practical level

workflow state
!= runtime context/resources

input schema
!= internal workflow channels/state
!= output schema

expected typed workflow/domain outcome
!= unexpected framework/programmer exception

T1 model observation
→ A3 proposal
→ T2 fresh A2 admission

UpgradePilot semantic trace/replay
!= LangGraph trace/checkpoint/history/time-travel replay

framework-private/internal channel
!= model-observation security/authority boundary
```

Required depth is architectural/practical, not framework-internals depth. Ali should be able to explain **why** each distinction changes the real R4-B design before the graph is frozen.

## Current design-pressure concepts to reason about

Use the real R4-A seam and the bounded R4-B plan to reason about:

```text
A1 outside graph vs explicit A1 graph node
wrapping existing typed domain objects vs flattening/duplicating fields
what must cross A3/A2/A4 node boundaries
what belongs in Runtime/context_schema instead of workflow state
how A2 establishes fresh T2 admission state after A3 output
why A2 remains authority while a router only selects the next destination
why EvidenceGapAdmissionProblem is an expected terminal workflow outcome
why A4 may remain cohesive while semantic result/failure have the same downstream destination
what final graph output should expose vs keep internal for focused inspection
```

Do not ask Ali to choose exact framework syntax before these premises are understood.

## Learn when first used materially inside R4-B

Only when the implementation actually uses them, learn the exact API/syntax needed for our selected graph:

```text
StateGraph state-schema declaration used by our code
Runtime / context_schema access used by our nodes
conditional-edge/router typing used by our graph
input/output schema mechanics if selected
compile()/invoke() behavior used by our tests
basic graph tracing/debug visibility needed for comparison
LangGraph dependency/version surface actually installed
```

These may remain lookup-assisted. The learning target is to read, modify, test, and diagnose the real implementation—not memorize the full API.

## Master through repeated comparison

```text
framework orchestration vs UpgradePilot domain ownership
model proposal vs deterministic authorization
workflow state vs trusted domain truth
state-transition reasoning
semantic-equivalence testing
framework clarity/observability vs ceremony/dependency cost
near-future growth fitness without pre-building future actions/loops
```

## Explicitly defer until trigger

### Checkpointing / persistent graph history / time travel

**Trigger:** a real crash/restart, long-running pause/resume, thread-continuity, workflow-debug/forking, or durable recovery responsibility appears. Never reopen merely because semantic replay exists; the responsibilities differ.

### Interrupts / human-in-the-loop

**Trigger:** a real admitted action requires human approval, edit, or input before continuation.

### Automatic retry / framework error-handler policy

**Trigger:** UpgradePilot has explicit retry classes plus idempotency, attempt, external-call, and planning-budget semantics. Do not let framework retry silently redefine an investigation attempt.

### Custom reducers

**Trigger:** parallel writers or genuine accumulation semantics appear. Sequential singleton workflow values should keep the simpler update model.

### `Command`

**Trigger:** one node genuinely needs to own an atomic state update + dynamic destination and separate routing becomes duplication.

### ToolNode / framework-native model-to-tool execution

**Trigger:** R4-C explicitly evaluates tool calling while preserving/retesting fresh deterministic A2 authority.

### `create_agent` / default agent loop

**Trigger:** R4-C begins after the lower-level LangGraph responsibility is understood and compared.

### Subgraphs

**Trigger:** a real reusable nested or separately-owned agent/workflow responsibility appears.

### Parallelism / `Send`

**Trigger:** two or more independent admitted actions exist and concurrency has an explicit benefit, reducer/freshness model, and authority semantics.

### Automatic multi-turn / graph back-edge

**Trigger:** a second real planning turn/action is admitted with explicit continuation, budget, anti-repeat, and stopping semantics.

### Persistent Store / cross-thread memory

**Trigger:** a real cross-run/thread/user/application memory responsibility appears.

### Advanced streaming

**Trigger:** a concrete UX/diagnostic need requires progressive output with an explicit redaction/observability policy.

### LangSmith as required proof machinery

**Trigger:** its observability/evaluation value justifies an operational dependency. Focused tests and UpgradePilot semantic proof remain authoritative.

---

# 8. R4-C — LangChain bounded learning slice

**Implementation trigger:** the lower-level plain-Python and LangGraph responsibilities are understood well enough that higher-level abstractions can be judged rather than merely followed.

## Learn when entering R4-C

```text
LangChain model abstraction
agent/create_agent concept
tool definition/calling
middleware/lifecycle hooks
relationship between LangChain agents and LangGraph runtime
```

The current R4-B research adds an important ordering refinement: a clean first R4-C slice may compare only A3's provider/model + structured-output abstraction while preserving A1/A2/A4, before deciding whether tool/agent-loop abstractions deserve a second slice.

## Learn when materially relevant

```text
with_structured_output / provider-vs-tool structured-output strategy
ToolRuntime hidden dependency injection
retry/fallback middleware
early-stop behavior
guardrail hooks
model/tool middleware
provider abstraction
```

Important distinction to preserve when these appear:

```text
hidden ToolRuntime argument
!= execution authorization

automatic structured-output retry
!= current one-call A3 typed-failure semantics
```

The goal is to understand where these abstractions help or obscure `EvidenceGapPlanner`'s custom authority boundaries.

---

# 9. R4-D / R5 — comparison, testing, replay, ownership deepening

These stages are where several concepts should move from “understood” toward stronger ownership.

## Deepen through real comparison/debugging

```text
unit vs integration proof
fixtures vs development cases
replay/evaluation harnesses
semantic equivalence across implementations
trace interpretation
failure diagnosis
observability
framework overhead
state-transition debugging
structured-output failure diagnosis
growth-fitness reasoning without speculative implementation
```

The R4-A1 runtime repair gave a first practical example of distinguishing an implementation defect from a **test observation-model defect**. R4-A3 added another central separation: mocked provider-boundary proof is not live model semantic proof. R4-A4 added transition replay and diagnostic-serialization separation. R4-B now adds framework-workflow trace vs domain-semantic trace/replay as another required distinction. R4-D/R5 are the place to deepen these skills through broader real evidence rather than studying testing theory in isolation now.

This is also the preferred place to deepen syntax/concepts that remained shallow earlier **if actual failures or comparison questions make the deeper mechanics decision-relevant**.

---

# 10. Cross-stage re-entry rules

Regardless of the stage, pause implementation briefly and deepen a concept when any of these occurs:

```text
1. Ali cannot accurately explain the mechanism needed for the next material decision.
2. A test/failure contradicts the current mental model.
3. The implementation begins relying on syntax/abstraction whose behavior affects correctness or authority.
4. Two plausible designs cannot be compared without understanding the underlying mechanism more deeply.
5. A deferred concept becomes the direct cause of repetition, ambiguity, debugging difficulty, or architectural pressure.
6. A framework feature is about to be adopted rather than merely observed/compared.
```

The earlier R4-A ownership re-entry is now closed sufficiently for the comparison baseline. R4-B should use the same rule prospectively: do not pre-study the entire framework, but pause before a LangGraph abstraction becomes part of a material design or proof claim if its behavior is not yet understood well enough to challenge the choice.

When a test fails, first identify which proposition failed and whether the defect is in implementation, fixture/setup, observation/assertion method, or the current mental model. Do not automatically “fix the source” merely because a test is red.

Do **not** pause merely because a syntax feature exists in a file if it is incidental and can be safely recognized at shallow depth.

---

# 11. Current immediate learning position

R4-A ordinary-Python reference/control is COMPLETE as a coherent comparison baseline. Current recorded evidence remains:

```text
A1 10/10
A2 13/13
A3 13/13
A4 7/7
combined 47/47
real S001 A3 selection/admission PASS
real S001 A4 execution/update/trace/replay PASS
A4 post-action ownership closure PASS
```

R4-B has now progressed beyond raw framework entry. The current evidence horizon also includes:

```text
initial LangGraph mechanics orientation
→ current official LangGraph/LangChain research proposal
→ architecture alternatives and trade-offs
→ post-research LbD discussion
→ evidence-refined bounded R4-B plan
```

The immediate learning responsibility is **decision-critical R4-B design learning**, not implementation yet and not additional generic framework exploration.

Use this order:

```text
1. use `B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md` as the bounded R4-B execution/design route
2. learn workflow state vs trusted domain state
3. learn partial state updates + runtime context at the practical depth needed for A3/A2/A4
4. learn input/internal/output state-schema distinction if it affects the chosen graph boundary
5. consolidate expected outcome vs exception and T1→A3→T2 freshness placement
6. consolidate semantic replay vs checkpoint/time-travel replay
7. jointly resolve the remaining R4-B design gates:
   A1 placement
   exact workflow state/input/output shape
   T2 freshness mechanism
   runtime context
   routing representation
   A4 cohesion
   naming
8. only after those decisions are sufficiently clear, hand off to Build/Implement
9. implement the smallest experiment-owned graph and produce controlled semantic-equivalence evidence before the real S001 smoke
```

Required ownership before first LangGraph implementation should be proportional. Ali should be able to explain:

```text
what LangGraph is adding structurally
what remains UpgradePilot-owned
why workflow state is not domain truth
why deterministic A2 authority remains after graph routing
why T2 must be obtained after A3 proposal
why A4 trace/replay remains semantic proof
why the selected graph is preferable to the credible smaller/larger alternatives
```

No framework-internals course is required. Exact API/syntax may remain lookup-assisted until used materially.

No broad LangGraph course, checkpoint/persistence implementation, HITL machinery, retry policy, ToolNode, `create_agent`, subgraph/parallelism block, automatic multi-turn loop, fabricated second action, or product-runtime integration is required before the first bounded graph slice.

---

## Stop rule

This companion should change only when the R4 implementation exposes a materially new learning responsibility, a deferred concept earns a new trigger, or a current learning-depth decision proves wrong.

Do not update it after every ordinary line of code or every small explanation.
