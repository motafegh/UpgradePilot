# B2/X1 R4 Learning-by-Doing Depth and Re-entry Map

**Status:** ACTIVE COMPANION TO THE SELECTED R4 IMPLEMENTATION PLAN  
**Date:** 2026-08-31  
**Primary plan:** `B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
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

---

# 3. R4-A1 — model boundary / typed context / explicit projection

**Implementation state:** COMPLETE; runtime validation still pending.

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

## Master through repeated use

```text
typed data/state modeling
runtime invariants
explicit model-observation projection
trusted internal state != model-visible state
wire-shape validation != execution authorization
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

**Implementation state:** NEXT.

## Learn when first used materially

The following should be introduced against the real admission code rather than pre-studied abstractly:

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

Likely Python syntax/patterns to learn here:

```text
dict lookup / mapping by ID
small result dataclasses or union-style result types
Literal problem reason codes
`isinstance` narrowing where needed
early returns
small helper functions when one responsibility becomes clearer by extraction
```

## Master through repeated use

```text
model-selected action ID is untrusted proposal
trusted catalog owns executable identity
admission must use latest trusted state
hidden locator/preconditions remain deterministic
```

## Defer until trigger

### Advanced authorization/policy framework design

**Trigger:** only if several independently different policy classes/actions make simple deterministic checks duplicated or brittle.

### General rule engine

**Trigger:** only if real action preconditions become numerous/compositional enough that explicit bounded checks materially fail maintainability. Do not build for the one-action seam.

---

# 5. R4-A3 — bounded local model request/response seam

**Implementation state:** after R4-A2 focused proof.

## Learn when first used materially

```text
Mapping[str, Any] as untrusted input boundary
runtime type narrowing with isinstance
JSON serialization/deserialization
local model/provider request structure
structured outputs / schema-constrained generation
provider response parsing
provider/model failure vs semantic decision failure
timeout/retry boundary at practical level
prompt/context engineering for the exact planner responsibility
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

## Defer until trigger

### Generic multi-provider abstraction

**Trigger:** a second provider/model must genuinely be supported or provider-specific code materially obstructs the experiment comparison.

### Sophisticated retry/backoff libraries

**Trigger:** real provider failures/retry policy become frequent or complex enough that explicit bounded retry handling is no longer adequate.

### Deep prompt-optimization framework

**Trigger:** repeated evaluation shows prompt/context design is a measurable planner-quality bottleneck that cannot be addressed by small explicit revisions.

---

# 6. R4-A4 — no-tool/action transition, execution/update seam, trace/replay

**Implementation state:** after bounded model request/response seam.

## Learn when first used materially

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

If Python uses enums, discriminated result objects, or explicit transition records here, learn those when they appear.

## Defer until trigger

### Event sourcing / full workflow persistence architecture

**Trigger:** replay/checkpoint requirements become durable product responsibilities rather than experiment trace needs.

### Async/concurrency depth

**Trigger:** real parallel investigations, streaming, concurrent provider operations, or race/freshness problems appear. Do not pre-build async complexity for a sequential seam.

---

# 7. R4-B — LangGraph implementation/comparison

**Implementation trigger:** ordinary-Python reference seam is coherent enough to serve as a real control/baseline.

## Learn when entering R4-B

```text
what LangGraph is responsible for
State / state schema
StateGraph
nodes
edges
conditional edges
compile/invoke flow
how our planner/admission/execution/update responsibilities map onto graph nodes/transitions
```

Use the already-understood plain-Python seam as the comparison anchor.

## Learn when first used materially inside R4-B

```text
checkpoints/persistence
interrupts / human-in-the-loop
state reducers if actually needed
streaming if actually useful
tracing/observability hooks
error/failure routing
freshness/revalidation placement in graph execution
```

Do not study every LangGraph feature merely because the framework exposes it.

## Master through repeated comparison

```text
what the framework removes
what it makes clearer
what new complexity it introduces
what is framework mechanism vs UpgradePilot domain responsibility
```

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

## Learn when materially relevant

```text
retry/fallback middleware
early-stop behavior
guardrail hooks
model/tool middleware
provider abstraction
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
```

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

Do **not** pause merely because a syntax feature exists in a file if it is incidental and can be safely recognized at shallow depth.

---

# 11. Current immediate learning position

Before/during R4-A2, retain practical understanding of the R4-A1 Python surface:

```text
dataclass
frozen / slots at practical level
type annotations
X | None
tuple[X, ...]
Literal
__post_init__
comprehensions
explicit projection
schema vs parser
```

Then R4-A2 should introduce, in small real-code steps:

```text
stable-ID lookup/rebinding
typed admission result/problem
early-return guard flow
fresh-state validation
TOCTOU
proposal vs authorization
defense in depth
```

No deeper prerequisite block is required before beginning R4-A2.

---

## Stop rule

This companion should change only when the R4 implementation exposes a materially new learning responsibility, a deferred concept earns a new trigger, or a current learning-depth decision proves wrong.

Do not update it after every ordinary line of code or every small explanation.