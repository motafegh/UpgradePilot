# B2/X1 R4-B — LangGraph Learning-by-Doing Entry

**Date:** 2026-09-02  
**Mode:** Learning-by-Doing / Building  
**Stage:** R4-B LangGraph implementation/comparison  
**State:** LBD ORIENTATION ACTIVE / GRAPH DESIGN NOT YET FROZEN  
**Product runtime integration:** not authorized

## 1. Continuity and evidence horizon

This record continues from:

`working-memory/2026-09-02_B2-X1-R4A4-runtime-lbd-and-reconciliation-closure.md`

The ordinary-Python R4-A reference/control is now accepted as a coherent comparison baseline at its bounded scope:

```text
A1 model-visible projection / decision contract
→ A3 local-model request/response
→ A2 fresh deterministic rebinding/admission
→ A4 execution / domain interpretation / immutable state transition / trace / replay
```

Established proof carried into R4-B:

```text
A1 10/10 PASS
A2 13/13 PASS
A3 13/13 PASS
A4 7/7 PASS
combined A1+A2+A3+composition+A4 47/47 PASS
real S001 A3 selection/admission PASS
real S001 A4 execution/update/trace/replay PASS
post-action A4 Learning-by-Doing ownership closure PASS
```

This is the comparison anchor. It does not establish production reliability, broad planner quality, multi-action generality, product-runtime integration, or framework adoption value.

## 2. Selected next responsibility

R4-B asks one bounded engineering question:

> How should the already-understood `EvidenceGapPlanner` responsibility be expressed with LangGraph so that we can compare workflow/state/routing structure against the ordinary-Python control without weakening deterministic authority boundaries or manufacturing new capabilities?

The main implementation plan already authorizes R4-B once R4-A is coherent enough to serve as a baseline. That trigger is now satisfied.

The learning-depth companion now selects these entry concepts only:

```text
what LangGraph is responsible for
State / state schema
StateGraph
nodes
edges
conditional edges
compile/invoke flow
mapping planner / admission / execution / update responsibilities onto graph structure
```

Deeper framework features remain deferred until materially triggered:

```text
checkpoints / persistence
interrupts / human-in-the-loop
state reducers
streaming
tracing/observability hooks
advanced failure routing
async/concurrency
```

## 3. Current Learning-by-Doing exploration point

The written Learning-by-Doing Skill and Planning/Design Skill have been reloaded and are active for this responsibility.

The current orientation has established the minimum LangGraph execution model needed to begin reasoning about the real graph:

```text
State
→ shared workflow data carried between graph steps

node
→ one callable that reads current state and returns an update

edge
→ deterministic execution order

conditional edge
→ deterministic routing based on an already-established result/state

START / END
→ graph entry / termination markers

StateGraph
→ graph builder

compile()
→ produce executable compiled graph

invoke(...)
→ execute from initial state/context
```

No final R4-B graph state schema, node decomposition, edge layout, or A4 mapping is frozen yet.

The exploration is intentionally using the plain-Python responsibility model as an anchor rather than redesigning the planner from scratch or mechanically wrapping every A1/A2/A3/A4 function in a node.

## 4. Design constraints already inherited

The LangGraph experiment must preserve the existing authority split unless evidence justifies a deliberate redesign:

```text
model-visible context
!= hidden execution authority

EvidenceGapDecision
= untrusted proposal

A2 admission/revalidation
= deterministic execution authorization

semantic result
!= operational failure

budget spent
!= action consumed

replay
!= external re-execution
```

Experiment isolation remains:

```text
R4-B work under experiments/ + experiments/tests/
→ no product runtime import/adoption
```

Still prohibited:

```text
NO automatic multi-turn loop
NO fabricated second action
NO generic executor registry without demonstrated pressure
NO database/event-sourcing/checkpoint infrastructure merely because LangGraph supports it
NO product-runtime integration
NO LangGraph adoption claim before comparison evidence
```

## 5. Proof direction for the first future slice

The first R4-B implementation slice should eventually produce evidence that answers a narrow comparison proposition, not merely show that a graph compiles.

Candidate proof direction, to be refined during the LbD design step:

```text
same bounded trusted inputs / recorded outcomes
→ plain-Python baseline semantics
→ LangGraph semantics
→ compare resulting trusted state / routing / authority behavior
```

Exact test shape and graph decomposition remain undecided until the LbD design discussion.

## 6. LbD checkpoint — framework/domain distinction and first branch mechanics

The current exploration has established several material design constraints worth carrying forward.

### Framework role vs UpgradePilot ownership

LangGraph is being evaluated as the orchestration/runtime representation for the same bounded UpgradePilot responsibility. Existing R4-A semantics and authority do not become framework semantics merely because LangGraph carries or routes their values.

```text
UpgradePilot domain/responsibility layer
→ EvidenceGapPlannerContext
→ EvidenceGapDecision
→ A2 deterministic admission
→ EvidenceGapInvestigationState
→ semantic result / operational failure rules
→ budget / consumption semantics
→ trace / replay semantics

LangGraph orchestration layer
→ shared workflow State
→ nodes
→ edges
→ conditional routing
→ graph execution
```

`EvidenceGapInvestigationState` is therefore not automatically identical to the whole LangGraph workflow state. A future graph state may carry trusted evolving domain state plus temporary inter-node values. Likewise, A1 remains the model-observation projection boundary; graph state is not automatically model-visible state.

### Current routing conclusion

After A3 produces a valid parsed `EvidenceGapDecision`, routing from the planner result is deterministic:

```text
ACTION_SELECTED
→ route to A2 admission

no-action decision
→ route to the no-action transition path
```

Do not ask another LLM to decide this mechanical consequence of an already-established decision contract.

After A2 executes, a second deterministic branch exists:

```text
AdmittedInvestigationAction
→ execution may proceed

EvidenceGapAdmissionProblem
→ execution must not begin
```

A2 remains the authorization owner. A LangGraph conditional edge would only route based on A2's already-established result; it must not duplicate or weaken admission checks.

### Three branch classes now distinguished

```text
1. planner semantic branch
   EvidenceGapDecision
   → ACTION_SELECTED vs no-action

2. deterministic admission branch
   A2 result
   → admitted vs rejected

3. execution outcome branch
   A4 execution
   → semantic result vs operational failure
```

The first two branch responsibilities are now conceptually clear. The third is the next material design question because the existing A4 owner already distinguishes semantic result from operational failure and applies different trusted-state consequences.

### Admission rejection does not fake an A4 transition

If A2 returns an admission problem, capability execution has not begun. Therefore the existing investigation-domain state is not changed merely because the graph itself progressed through planner/admission nodes:

```text
budget unchanged
consumed_actions unchanged
domain assessment unchanged
```

This reinforces:

```text
workflow progress
!= domain state transition
```

### Still deliberately unresolved

Do not yet freeze:

```text
exact LangGraph state schema
whether planner context is stored or composed locally
exact node count/boundaries
whether A4 remains one node or is decomposed
whether semantic-result vs operational-failure deserves graph-level branching
whether existing EvidenceGapTransitionTrace remains unchanged or is adapted for graph comparison
checkpoint/persistence use
```

## 7. Next continuation

**Next Learning-by-Doing question:** inspect the existing A4 ownership boundary and decide whether LangGraph should expose `semantic result` vs `operational failure` as graph-level routing, or whether A4 should remain an encapsulated execution/transition node that returns the already-correct next trusted state/trace.

This is a Planning/Design exploration step. Do not implement LangGraph until the smallest honest graph mapping is understood sufficiently.

**Skill provenance:** `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-planning-design`.
