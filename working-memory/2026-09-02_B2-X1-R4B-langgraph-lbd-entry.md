# B2/X1 R4-B — LangGraph Learning-by-Doing Entry

**Date:** 2026-09-02  
**Mode:** Learning-by-Doing / Building  
**Stage:** R4-B LangGraph implementation/comparison  
**State:** ENTRY OPEN / DESIGN NOT YET STARTED  
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

## 3. Current stop point

No R4-B graph design or implementation has been chosen yet.

Before choosing state shape, node boundaries, edges, conditional routing, or writing LangGraph code:

```text
1. reload `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`
2. use its real responsibility → orientation → reasoning → bounded work sequence
3. reconstruct the plain-Python responsibility map as the comparison anchor
4. learn the minimum LangGraph concepts needed for the first material design choice
5. jointly decide the smallest honest graph mapping
```

This record must not pre-decide step 5 before that Learning-by-Doing design discussion occurs.

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

## 6. Next continuation

**Next action:** reload and apply the written Learning-by-Doing Skill, then begin the joint R4-B design step.

Do not implement LangGraph before that step is completed proportionately.
