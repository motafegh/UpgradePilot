# B2/X1 R4-B — Comparison Boundary Reframe and Corrected Learning-by-Doing Entry

**Date/time:** 2026-09-03 18:04 (+03:30)  
**Session status:** ACTIVE  
**Primary responsibility/mode:** R4-B LangGraph comparison-boundary correction / Learning-by-Doing + Planning/Design  
**Related parent plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Related bounded plan:** `../plans/B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`  
**Learning-depth owner:** `../plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`  
**Previous:** `2026-09-02_B2-X1-R4B-langgraph-lbd-entry.md`  
**Product runtime integration:** not authorized

## 1. Session anchor

R4-A ordinary Python is complete and remains a valuable reference/control implementation and evidence source. The project then entered R4-B and produced a LangGraph research/design proposal, bounded R4-B plan, refined learning-depth route, and working-memory consolidation.

A subsequent Learning-by-Doing design discussion exposed a material comparison-design problem: the refined R4-B route had promoted too many R4-A experiment implementation choices into LangGraph architecture constraints. In particular, it increasingly treated the exact A1/A2/A3/A4 decomposition, `EvidenceGapInvestigationState`, `EvidenceGapTransitionTrace`, and related R4-A representations as structures R4-B should preserve or wrap rather than as evidence to inspect.

That pressure conflicts with UpgradePilot's existing retention discipline:

```text
existing implementation
= evidence to inspect
!= architectural authority to preserve
```

The corrected objective is therefore to compare competent implementations of the **same bounded UpgradePilot responsibility and framework-independent semantics**, while allowing each implementation approach to use an architecture natural to its own mechanism.

## 2. Accepted comparison reframe

Use this distinction going forward:

```text
R4-A
→ reference implementation
→ engineering evidence
→ lessons / failure modes / useful mechanisms
→ comparison result

R4-A
!= architectural specification for R4-B
```

R4-B should start from:

```text
accepted UpgradePilot framework-independent semantics
+ bounded EvidenceGapPlanner responsibility
+ trust / authority / failure / investigation constraints
+ real product-owned reusable capabilities
+ R4-A lessons and evidence
+ current LangGraph execution model
→ independently design the smallest proportionate LangGraph implementation
```

Do **not** start from:

```text
A1/A2/A3/A4 classes/functions
+ EvidenceGapInvestigationState
+ EvidenceGapTransitionTrace
→ find LangGraph containers/nodes that preserve those exact representations
```

This does not authorize redesign of accepted product semantics. It removes accidental implementation-retention constraints from the framework comparison.

## 3. What remains common across implementations

The cross-implementation comparison should preserve the applicable accepted semantics and observable responsibility, including where relevant:

- bounded model observation / no accidental authority leakage;
- model proposal does not itself authorize external action;
- action execution must be governed by current trusted deterministic authority at the appropriate pre-execution point;
- rejected/unauthorized action does not execute;
- no-action outcomes remain explicit and semantically distinguishable;
- expected semantic/domain outcomes remain distinct from operational/provider failures and unexpected implementation defects;
- investigation budget and action-consumption consequences remain correct;
- exact evidence identity/scope and established product interpretation responsibilities remain owned by their normal product/domain owners;
- external effects/calls are observable and testable;
- semantic consequences can be tested/reconstructed without silently repeating nondeterministic/external work when that proof responsibility applies.

The exact Python classes, graph-state representation, node boundaries, routing mechanism, internal trace shape, and framework observability representation are **not automatically shared invariants**.

## 4. Product-owned reuse boundary

Independent LangGraph design does not mean duplicating product/domain capabilities merely to be different.

Existing product-owned mechanisms such as exact repository acquisition, target declaration interpretation, target relevance, and Python-support impact evaluation should be reused when they still own the same product responsibility. R4-B is allowed to redesign experiment/orchestration structure around those capabilities; it is not authorized to create a second product truth implementation.

## 5. Correct comparison method

The comparison should no longer require identical internal representations such as:

```text
plain-Python EvidenceGapInvestigationState
==
LangGraph EvidenceGapInvestigationState
```

Instead define common controlled cases and compare framework-neutral observable outcomes. Depending on the scenario, inspect matters such as:

```text
action selected / no action / rejected
whether execution occurred
whether required current authority was checked at the correct time
which exact action/evidence path executed
budget consequence
action-consumption consequence
final domain/applicability conclusion
expected semantic result vs operational failure behavior
forbidden external-call absence
reproducible/testable semantic consequence
```

Framework-specific state, topology, trace, checkpoint, and observability evidence may also be compared as **value/overhead characteristics**, but they do not become the semantic oracle merely because one framework provides them.

## 6. Owner alignment completed

The repository owner chain has now been reconciled to this correction:

1. **Parent R4 plan** — explicitly states that R4 compares competent implementations of the same bounded responsibility and that R4-A is evidence/reference rather than architectural authority for R4-B.
2. **Bounded R4-B plan** — rewritten around framework-neutral responsibility classification → minimum LangGraph learning → independent LangGraph design → Build → normalized semantic comparison.
3. **R4 learning-depth map** — R4-A learning remains preserved, while R4-B learning no longer assumes the old graph/state/A-number mapping.
4. **`MEMORY.md`** — now selects the corrected live route and states that LangGraph source implementation has not begun.
5. **Previous R4-B working memory** — marked historical/superseded and points to this record; its earlier candidate remains provenance rather than current architecture authority.
6. **Research/design proposal** — intentionally left unchanged as non-controlling historical research evidence; its framework facts remain useful, but its implementation-preserving recommendations no longer control R4-B.
7. **Specifications/ADRs** — no new specification or ADR was created because accepted framework-independent semantics already have owners and no product framework adoption has been selected.

This alignment is a planning/design correction only. It does not establish LangGraph implementation or framework adoption evidence.

## 7. Corrected near-term Learning-by-Doing route

Before freezing any LangGraph architecture:

```text
A. extract/classify the bounded responsibility
   → accepted framework-independent requirement
   → reusable product-owned capability
   → R4-A engineering lesson/evidence
   → R4-A/Python-specific implementation choice

B. learn only the LangGraph concepts needed to design that responsibility naturally
   → StateGraph execution model
   → state as workflow communication
   → node/edge/conditional-routing semantics
   → input/internal/output state distinctions
   → runtime context/resources
   → expected outcome vs exception handling
   → effect/retry/checkpoint implications only when materially relevant

C. design the smallest credible LangGraph architecture from the clean requirement set

D. use R4-A as pressure/evidence
   → ask why each important R4-A mechanism existed
   → preserve the problem/invariant when still real
   → do not preserve the implementation form without independent justification

E. freeze only the LangGraph decisions needed for Build

F. implement under `experiments/`

G. prove common observable semantics through normalized comparison

H. use R4-D later to compare and potentially synthesize the strongest production architecture
```

## 8. Stop lines

Remain stopped before LangGraph source implementation until the independent LangGraph design is understood enough for Build.

Still prohibited unless separately admitted:

- product runtime integration;
- fabricated second investigation action;
- automatic multi-turn planner loop;
- framework adoption claim;
- checkpoint/persistence/HITL/retry/subgraph/parallel machinery merely for exposure;
- duplication of established product-owned semantics/capabilities.

## 9. Current session route

```text
OWNER ALIGNMENT
→ COMPLETE

CURRENT NEXT RESPONSIBILITY
→ R4-B1 framework-neutral classification of the R4-A seam

THEN
→ minimum LangGraph mechanics needed by the real responsibility
→ independent LangGraph architecture design/freeze
→ Build/Implement handoff
```

## 10. Evidence / non-proof

Established by this alignment work:

- the live owner chain now describes one coherent corrected comparison method;
- the R4-B plan no longer requires identical internal R4-A/R4-B state or trace objects;
- R4-A remains preserved as a serious reference/control and evidence source;
- product/domain owner reuse and framework-independent semantic constraints remain protected;
- no new specification/ADR was required for this planning correction.

Not established:

- any LangGraph source behavior;
- semantic equivalence between Python and LangGraph;
- LangGraph superiority/adoption value;
- product runtime readiness;
- multi-action/multi-turn planner value.

## 11. Provenance

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
