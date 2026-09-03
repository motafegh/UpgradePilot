# B2/X1 R4-B — Comparison Boundary Reframe and Corrected Learning-by-Doing Entry

**Date/time:** 2026-09-03 18:04 (+03:30)  
**Last material update:** 2026-09-03 19:09 (+03:30)  
**Session status:** ACTIVE  
**Primary responsibility/mode:** R4-B LangGraph comparison/design / Learning-by-Doing + Planning/Design  
**Related parent plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Related bounded plan:** `../plans/B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`  
**Learning-depth owner:** `../plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`  
**Current corrected research:** `../proposals/2026-09-03_B2_X1_R4B_CORRECTED_LANGGRAPH_INDEPENDENT_RESEARCH_AND_DESIGN_PROPOSAL.md`  
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
- action execution must be governed by sufficiently current trusted deterministic authority at the appropriate pre-execution point;
- rejected/unauthorized action does not execute;
- no-action outcomes remain explicit and semantically distinguishable;
- expected semantic/domain outcomes remain distinct from operational/provider failures and unexpected implementation defects;
- investigation budget and action-consumption consequences remain correct;
- exact evidence identity/scope and established product interpretation responsibilities remain owned by their normal product/domain owners;
- external effects/calls are observable and testable;
- semantic consequences can be tested/reconstructed without silently repeating nondeterministic/external work when that proof responsibility applies.

The exact Python classes, workflow-state representation, node/task boundaries, routing mechanism, internal trace shape, and framework observability representation are **not automatically shared invariants**.

## 4. Product-owned reuse boundary

Independent LangGraph design does not mean duplicating product/domain capabilities merely to be different.

Existing product-owned mechanisms such as exact repository acquisition, target declaration interpretation, target relevance, and Python-support impact evaluation should be reused when they still own the same product responsibility. R4-B is allowed to redesign experiment/orchestration structure around those capabilities; it is not authorized to create a second product truth implementation.

## 5. Correct comparison method

The comparison should no longer require identical internal representations such as:

```text
plain-Python EvidenceGapInvestigationState
==
LangGraph workflow state
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

Framework-specific state/local values, topology/control flow, trace, checkpoint, and observability evidence may also be compared as **value/overhead characteristics**, but they do not become the semantic oracle merely because one framework/API provides them.

## 6. Initial owner alignment completed

The repository owner chain was reconciled to the comparison correction:

1. **Parent R4 plan** — states that R4 compares competent implementations of the same bounded responsibility and that R4-A is evidence/reference rather than architectural authority for R4-B.
2. **Bounded R4-B plan** — reframed around framework-neutral responsibility classification → LangGraph learning → independent design → Build → normalized semantic comparison.
3. **R4 learning-depth map** — preserved R4-A learning while removing the old mandatory graph/state/A-number mapping.
4. **`MEMORY.md`** — selected the corrected live route and stated that LangGraph source implementation had not begun.
5. **Previous R4-B working memory** — marked historical/superseded and points to this record.
6. **2026-09-02 research/design proposal** — intentionally left unchanged as non-controlling historical research evidence.
7. **Specifications/ADRs** — no new specification or ADR was created because accepted framework-independent semantics already have owners and no product framework adoption has been selected.

That alignment established the correct comparison boundary but did not yet prove or select a LangGraph architecture.

## 7. Learning-by-Doing resumed — first classification slice

After the owner correction, Learning-by-Doing resumed against the real R4-A source.

The first focused slice examined **model observation vs execution authority** using:

- `experiments/b2_x1_evidence_gap_planner.py`;
- `experiments/b2_x1_evidence_gap_admission.py`.

### Classification established

Framework-independent requirements:

```text
model receives only justified bounded observation
model proposal does not self-authorize execution
sufficiently current deterministic authority must exist after proposal and before effect
rejected/unauthorized proposal must not execute
```

R4-A engineering lessons/evidence:

```text
explicit request projection prevents accidental context expansion
T1 observation vs T2 currentness exposes real TOCTOU/freshness pressure
stable action identity should not let the model redefine hidden execution authority
```

R4-A/Python-specific mechanisms, not automatic R4-B requirements:

```text
EvidenceGapPlannerContext
EvidenceGapAdmissionState
BoundInvestigationAction as this exact class
project_action_descriptor(...)
admit_selected_investigation_action(...) as this exact function
physical A1 / A2 decomposition
```

### Ali reasoning result

Ali correctly selected the framework-neutral interpretation:

```text
required:
current deterministic authorization after model proposal and before external effect

not established:
a dedicated authorization node is mandatory
```

Important refinement: this is not merely because R4-A evidence is limited. Even stronger evidence for the authorization responsibility would not by itself establish one mandatory physical node/function shape.

## 8. Corrected independent research proposal reviewed

A new research agent added:

`proposals/2026-09-03_B2_X1_R4B_CORRECTED_LANGGRAPH_INDEPENDENT_RESEARCH_AND_DESIGN_PROPOSAL.md`

Repository evidence horizon used by that proposal: `main@9bb534eda0ef68d701b031b5a19add432a52e910`.

The proposal is non-controlling and explicitly respects the corrected comparison boundary.

### Strong accepted research findings

The proposal materially improves the route in these areas:

1. **R4-A classification is treated as design evidence, not topology authority.**
2. **Workflow communication, product/domain truth, and runtime dependencies are separated explicitly.**
3. **Current authority should be obtained after the proposal rather than precomputed and carried as supposedly fresh state.**
4. **Framework-neutral comparison remains the semantic oracle.**
5. **Effect vs deterministic consequence is a real independent design question rather than an A4-preservation decision.**
6. **`Command` is a credible Graph API mechanism when update + dynamic routing are one cohesive responsibility; it is not mandatory.**
7. **Persistence/retry/HITL/ToolNode/subgraph/parallelism/multi-turn remain unjustified for the first slice.**
8. **Functional API is a first-class LangGraph alternative that the earlier route had not evaluated sufficiently.**

### Strongest researched Graph API candidate — not frozen

The proposal independently derives:

```text
START
→ PLAN
   → model problem / no-action → CONCLUDE
   → action proposal → AUTHORIZE
       → rejected → CONCLUDE
       → authorized → INVESTIGATE
           → CONCLUDE
→ END
```

Its rationale is responsibility-derived rather than A-number-derived:

- `plan` — bounded model observation + provider/model result;
- `authorize` — current deterministic pre-effect authority decision;
- `investigate` — admitted external investigation effect + product-owned interpretation;
- `conclude` — pure deterministic budget/consumption/domain/continuation consequence.

This is currently the strongest researched **candidate**, not accepted architecture.

### Serious Functional API alternative

The proposal correctly identifies LangGraph Functional API (`@entrypoint` + optional `@task`) as a serious fit for the current small sequential/branching responsibility.

Potential strength:

```text
ordinary Python control flow
+ lower explicit state/topology ceremony
+ LangGraph runtime
```

Potential weakness:

```text
less explicit static topology/state inspection
+ weaker discrimination of Graph API orchestration value
+ possible later migration if real action/state/branching complexity grows
```

The correct first question therefore became:

```text
which LangGraph API paradigm best implements this bounded responsibility now?
```

not:

```text
what should our StateGraph state fields be?
```

Do not build both APIs by default.

## 9. Owner alignment after proposal review

The proposal review produced a targeted owner refinement, not another plan family.

Updated:

1. **`plans/B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`**
   - adds explicit R4-B2A Graph API vs Functional API gate;
   - moves deep StateGraph mechanics to selected-paradigm learning;
   - keeps four-stage Graph API as research evidence, not frozen architecture;
   - records when a second API implementation may be reopened.

2. **`plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`**
   - teaches Graph API vs Functional API before StateGraph-specific design;
   - elevates workflow communication vs product truth vs runtime dependencies as the cross-API concept;
   - makes Graph API and Functional API mechanics conditional on selection;
   - keeps exact framework syntax lookup-assisted until Build.

3. **`MEMORY.md`**
   - selects the API-paradigm-aware live route;
   - records the proposal as non-controlling current research evidence;
   - records the first R4-B1 ownership result;
   - keeps LangGraph implementation stopped.

Not changed:

- accepted specifications;
- ADRs;
- parent R4 route materially;
- source/tests/dependencies;
- either research proposal.

No new plan or working-memory record was created because the responsibility remains the same R4-B session/design journey.

## 10. Current Learning-by-Doing route

```text
CURRENT
→ continue R4-B1 classification only where high-value R4-A mechanisms still need ownership-level distinction

THEN
→ R4-B2A Graph API vs Functional API
   learn at design depth against the real EvidenceGapPlanner responsibility
   decide which paradigm deserves the first implementation

THEN
→ R4-B2B learn only selected-paradigm mechanics

THEN
→ R4-B3 independently derive/freeze the smallest architecture
   include serious fallback/reassessment trigger

THEN
→ Build/Implement handoff
→ implement under experiments/
→ controlled framework-neutral semantic comparison
→ bounded real S001 smoke
→ R4-D evidence
```

### Cross-API mental model to preserve

```text
model observation
!= model proposal
!= current deterministic execution authority
!= external effect
!= deterministic semantic/domain consequence

workflow communication/evolving values
!= product/domain truth
!= run-scoped dependencies
```

## 11. Current stop lines

Remain stopped before LangGraph source/dependency implementation until the API paradigm and resulting architecture are sufficiently understood for Build.

Still prohibited unless separately admitted:

- product runtime integration;
- fabricated second investigation action;
- automatic multi-turn planner loop;
- framework/API adoption claim;
- building both LangGraph APIs merely for exposure;
- checkpoint/persistence/HITL/retry/subgraph/parallel machinery merely for exposure;
- duplication of established product-owned semantics/capabilities.

## 12. Evidence / non-proof

Established by the current planning/LbD work:

- the live owner chain now describes one coherent corrected comparison method;
- R4-A remains a serious reference/control and evidence source without becoming R4-B architecture authority;
- model-proposal vs current deterministic authorization has been classified at ownership level;
- Graph API and Functional API are now both admitted as real LangGraph implementation paradigms for evaluation;
- the four-stage StateGraph is the strongest researched candidate but is not frozen;
- the learning route no longer assumes shared graph state before the API-paradigm decision;
- product/domain owner reuse and framework-independent semantic constraints remain protected.

Not established:

- any LangGraph source behavior;
- which LangGraph API will actually win the design gate;
- semantic equivalence between Python and LangGraph;
- that four stages are better than a coarser Graph API or Functional API flow;
- LangGraph superiority/adoption value;
- product runtime readiness;
- multi-action/multi-turn planner value.

## 13. Provenance

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`