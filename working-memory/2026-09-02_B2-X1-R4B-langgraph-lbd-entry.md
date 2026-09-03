# B2/X1 R4-B — LangGraph Learning-by-Doing Entry

**Date:** 2026-09-02 / consolidated 2026-09-03  
**Session status:** SUPERSEDED  
**Superseded/continued by:** `2026-09-03_1804_B2-X1-R4B-comparison-boundary-reframe.md`  
**Historical interpretation:** This record preserves the research consolidation and reasoning that produced the earlier implementation-preserving LangGraph candidate. Its architecture conclusions are no longer the active R4-B design route. Use the successor record, current plans, and `MEMORY.md` for the corrected comparison boundary.  
**Mode at time recorded:** Learning-by-Doing / Planning-Design leading into Build  
**Stage:** R4-B LangGraph implementation/comparison  
**State at time recorded:** RESEARCH CONSOLIDATED / DESIGN-LEARNING ACTIVE / GRAPH NOT YET FROZEN  
**Product runtime integration:** not authorized

## Historical record preservation notice

The detailed reasoning previously stored in this file established a leading candidate that preserved the R4-A A1/A3/A2/A4 structure, wrapped existing R4-A domain objects in LangGraph workflow state, retained `EvidenceGapTransitionTrace` as the graph semantic proof object, and compared internal R4-A/R4-B state representations directly.

The subsequent Learning-by-Doing design review identified that approach as too implementation-preserving for the intended production-oriented framework comparison. The corrected route is now owned by:

- `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`
- `../plans/B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`
- `../plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`
- `../MEMORY.md`
- `2026-09-03_1804_B2-X1-R4B-comparison-boundary-reframe.md`

The earlier conclusions remain useful **historical evidence** for how the over-constrained candidate emerged and which LangGraph concepts/research findings were considered. They must not be treated as current architecture authority.

## Preserved historical conclusions (superseded as active design)

The earlier record had consolidated the following candidate direction:

```text
trusted UpgradePilot evidence/state
→ A1 bounded projection, candidate outside graph
→ START
→ A3 model node
→ planner-result routing
   ├─ model invocation problem → END
   ├─ no-action → A4 transition → END
   └─ ACTION_SELECTED → A2 fresh-admission node
                         ↓
                    admission routing
                    ├─ admission problem → END
                    └─ admitted → A4 transition → END
```

It also treated the following as likely or established R4-B design constraints:

```text
EvidenceGapInvestigationState
→ canonical trusted evolving domain state reused inside graph

EvidenceGapWorkflowState
→ orchestration envelope wrapping existing typed R4-A objects

EvidenceGapTransitionTrace + replay_evidence_gap_transition(...)
→ semantic proof reused directly by graph

A2
→ separate explicit LangGraph authority node

A4
→ cohesive LangGraph node unless later pressure justified splitting
```

Those ideas are **not deleted**; they remain hypotheses/evidence that may be rediscovered independently. The correction is that R4-B no longer begins by assuming them.

## Corrected interpretation of the evidence carried forward

The R4-A evidence itself remains valid at its bounded scope:

```text
A1 10/10 PASS
A2 13/13 PASS
A3 13/13 PASS
A4 7/7 PASS
combined focused family 47/47 PASS
real S001 A3 selection/admission PASS
real S001 A4 execution/update/trace/replay PASS
```

The useful lessons carried forward include:

- bounded model observation matters;
- model proposal must not self-authorize execution;
- current deterministic pre-execution authority matters;
- no-action semantics matter;
- semantic/domain result, operational failure, and implementation defect must remain distinguishable;
- budget/action-consumption consequences must remain correct;
- external-call boundaries and semantic consequences need focused proof;
- product/domain truth should not be duplicated inside experiments/frameworks.

What is no longer carried forward as an automatic requirement:

- exact A1/A2/A3/A4 physical decomposition;
- exact `EvidenceGapInvestigationState` representation;
- exact `EvidenceGapTransitionTrace` representation;
- exact Python class reuse inside graph state;
- direct internal-state equality as the cross-framework oracle;
- the earlier leading graph topology.

## Historical deferred framework surface

The earlier record deferred, and the corrected route still generally defers until a real trigger appears:

```text
checkpointing / persistence / time travel
interrupts / HITL
automatic retry / generalized error policy
custom reducers
Command unless justified by selected routing design
ToolNode
create_agent until R4-C
subgraphs
parallelism / Send
automatic multi-turn / graph back-edge
persistent Store / cross-thread memory
advanced streaming
LangSmith as required correctness proof
product-runtime integration
```

Exact re-entry triggers are now owned by the current learning-depth map and bounded R4-B plan.

## Historical handoff replaced

The prior handoff to resolve A1 placement, exact workflow-state wrapper shape, A2/A4 node mapping, and direct semantic-state equality is superseded.

Current continuation is instead:

```text
classify framework-independent requirements
vs reusable product capabilities
vs R4-A lessons/evidence
vs Python-specific implementation choices
→ learn minimum LangGraph execution concepts
→ independently derive LangGraph architecture
→ freeze only then
→ Build
→ compare through framework-neutral observable semantics
```

See the successor working memory for the active detailed route.

## Provenance

This file is intentionally retained as historical design provenance rather than rewritten to pretend the earlier reasoning never happened.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
