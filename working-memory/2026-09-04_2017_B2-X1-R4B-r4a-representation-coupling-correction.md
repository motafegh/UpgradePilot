# B2/X1 R4-B — R4-A Representation Coupling Drift and Correction

**Date/time:** 2026-09-04 20:17 (+03:30)  
**Session status:** CLOSED  
**Primary responsibility/mode:** R4-B LangGraph experiment corrective Build / Learning-by-Doing + Build/Implement  
**Related active Build memory:** `2026-09-04_1904_B2-X1-R4B-architecture-freeze-and-build-entry.md`  
**Related bounded plan:** `../plans/B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`  
**Product runtime integration:** not authorized

## 1. Starting point

The first R4-B source slice had been written as `experiments/b2_x1_evidence_gap_langgraph.py`, with focused offline tests under `experiments/tests/test_b2_x1_evidence_gap_langgraph.py`.

The implementation correctly introduced real LangGraph concepts such as `StateGraph`, explicit input/output schemas, runtime context, `Command` routing, and the four responsibility stages:

```text
PLAN → AUTHORIZE → INVESTIGATE → CONCLUDE
```

It also produced one useful implementation-derived refinement: final consequences must use the same coherent fresh T2 baseline that `AUTHORIZE` used, rather than reverting to stale T1 state.

However, before executable validation, Ali inspected the source and challenged a more fundamental issue: why did the supposedly independent LangGraph implementation directly import and expose many R4-A experiment representations?

## 2. Drift identified

The first implementation directly imported R4-A-specific types/functions including:

```text
EvidenceGapDecision
EvidenceGapPlannerContext
EvidenceGapModelInvocationResult
EvidenceGapAdmissionState
EvidenceGapAdmissionResult
AdmittedInvestigationAction
EvidenceGapAdmissionProblem
compose_pre_target_python_support_planner_context(...)
admit_selected_investigation_action(...)
```

Some controlled reuse was intentional, but the implementation crossed the intended boundary by allowing R4-A representations to define R4-B graph-facing protocols, State fields, result types, and node logic.

That drift conflicted with the already accepted comparison rule:

```text
R4-A
→ reference/control + engineering evidence + comparison oracle where useful

R4-A
!= architectural specification for R4-B
```

The corrected independent-design principle is:

```text
reuse product-owned truth directly
+
hide R4-A comparison/control machinery behind narrow adapters when holding semantics constant is useful
+
keep R4-B graph communication and node contracts R4-B-owned
```

## 3. Why the mistake happened

The immediate engineering goal was legitimate: avoid changing several variables at once while testing LangGraph. Reusing the already-proven R4-A planner/provider and deterministic admission behavior would let the experiment focus more cleanly on orchestration.

The mistake was treating:

```text
hold semantic behavior constant
```

as if it implied:

```text
reuse the control implementation's internal representations directly throughout the new architecture
```

That shortcut reduced initial implementation work but weakened the experiment's architectural independence. In particular:

- the graph's `planner_outcome` was typed as the R4-A model invocation result;
- the graph's authority snapshot contained the R4-A `EvidenceGapAdmissionState`;
- the graph's authority outcome was typed as the R4-A admission result;
- node branching used R4-A concrete classes to decide graph routing;
- the planner protocol accepted the R4-A `EvidenceGapPlannerContext` directly.

This would make R4-B too close to "R4-A wrapped in StateGraph" and could bias the eventual framework comparison.

## 4. Corrected ownership model

R4-B now owns its workflow communication model:

```text
EvidenceGapLangGraphActionProposal
EvidenceGapLangGraphNoAction
EvidenceGapLangGraphProviderProblem
→ EvidenceGapLangGraphPlannerOutcome

EvidenceGapLangGraphAuthorizedAction
EvidenceGapLangGraphAuthorityRejection
→ EvidenceGapLangGraphAuthorityOutcome

EvidenceGapLangGraphAuthoritySnapshot
→ R4-B current T2 product/orchestration snapshot

EvidenceGapLangGraphInvestigationOutcome
EvidenceGapLangGraphResult
→ R4-B graph/result contracts
```

R4-A is reused only **behind adapters** for experimental control:

```text
R4-B planner port
→ R4AControlPlannerAdapter
   → compose existing bounded R4-A model context
   → invoke existing controlled model/provider seam
   → map R4-A result into R4-B PlannerOutcome

R4-B authority port
→ R4AControlAuthorityAdapter
   → translate R4-B current snapshot/proposal into temporary R4-A admission inputs
   → call existing deterministic admission oracle
   → map result into R4-B AuthorityOutcome
```

The R4-B graph core no longer imports `EvidenceGapDecision`, `EvidenceGapPlannerContext`, `EvidenceGapAdmissionState`, or R4-A admission result classes.

## 5. Product-owned reuse remains direct

This correction does **not** mean reimplementing established product truth merely to look independent. Direct reuse remains appropriate for product/domain owners such as:

```text
PublicPullRequestInvestigation
PythonSupportDropImpactAssessment / PythonSupportDropInvestigationSelection
GitHub exact repository acquisition contract
interpret_target_python_declaration(...)
evaluate_target_python_relevance(...)
evaluate_python_support_drop_impact(...)
```

The boundary corrected here is specifically R4-A experiment representation ownership, not legitimate product capability reuse.

## 6. File-layout correction

Ali requested an explicit LangGraph implementation area rather than leaving the framework implementation mixed into the root experiment module collection.

Created:

```text
experiments/langgraph/
├── __init__.py
├── evidence_gap_workflow.py
└── r4a_control_adapters.py
```

Responsibilities:

- `evidence_gap_workflow.py` — native R4-B graph contracts, State/runtime context, nodes, routing, effect/conclusion logic;
- `r4a_control_adapters.py` — deliberate comparison bridge to the R4-A planner/admission control implementation;
- `experiments/tests/` remains the established experiment-regression home.

The superseded root-level `experiments/b2_x1_evidence_gap_langgraph.py` was removed.

## 7. Corrective Build performed

Completed:

```text
1. isolated LangGraph implementation under experiments/langgraph/
2. introduced R4-B-owned planner/authority/state/result contracts
3. moved direct R4-A comparison/control imports into r4a_control_adapters.py
4. kept product/domain imports direct where they own truth
5. updated the focused LangGraph graph tests to use R4-B-owned outcomes
6. added adapter-focused offline planner mapping tests
7. removed the old root-level LangGraph module
8. inspected resulting import/dependency direction
```

Relevant commits:

- `b0ad8400702143df8f2ee9a0402f9ca1536d0444` — create explicit LangGraph experiment package;
- `739954c937cf7e4f13b173da4b2ad96bc22e2a44` — add native LangGraph workflow contracts;
- `c5c7bfbf9f8291479cfc5ffc0409a1644fadde3a` — isolate R4-A control adapters;
- `0471b7aa37be2ad4601025d9f5b94e9634547ec9` — refactor LangGraph graph tests around native contracts;
- `b19d1c1cddfc788d9dd009b0f8ea798e54f18410` — remove superseded root-level LangGraph workflow;
- `4ce361b34483c0d029f67ee718b257eb1eaea388` — add offline adapter mapping proof.

## 8. Resulting dependency direction

Current native core:

```text
experiments/langgraph/evidence_gap_workflow.py
    ↓
LangGraph runtime primitives
+ UpgradePilot product/domain owners
```

Current comparison bridge:

```text
experiments/langgraph/r4a_control_adapters.py
    ↓
R4-A planner/provider/admission control implementation
    ↓ maps into
R4-B-owned workflow outcomes
```

This is the intended direction:

```text
R4-B core
← adapter maps control behavior into it

not

R4-B core
→ imports R4-A internal representations as its own contract
```

The focused graph regression now imports `R4AControlAuthorityAdapter` as an explicit test/control dependency, but it no longer imports R4-A admission/planner state/result types into the graph contract. A separate adapter-focused test intentionally imports R4-A control result types because its responsibility is to prove the translation boundary itself.

## 9. Engineering lesson retained

The important correction is not "never reuse old code." It is:

```text
reuse semantic/control behavior when it improves experimental isolation
!=
let the control implementation define the new architecture's internal contracts
```

A framework comparison can be invalidated in two opposite ways:

```text
rewrite everything
→ too many variables change at once

reuse everything directly
→ new implementation becomes a wrapper around the control architecture
```

The corrected middle path is:

```text
product truth reused directly
+ control behavior reused behind explicit adapters
+ new architecture owns its own workflow communication/topology
```

Ali's source inspection caught this before runtime validation, which prevented the first written implementation from silently becoming the R4-B reference architecture.

## 10. Evidence / proof limit after correction

Established by source/repository inspection:

- the dedicated LangGraph implementation package exists;
- the native graph core imports no R4-A planner/admission representations;
- direct R4-A imports are isolated in the explicit adapter module;
- graph State/planner/authority/result contracts are now R4-B-owned;
- product/domain capabilities remain reused directly;
- the old mixed root-level graph module is removed;
- graph-focused tests use R4-B contracts;
- adapter-focused tests cover planner action/no-action/provider-result translation at source level.

Not yet established:

- the refactored modules import successfully in the normal WSL environment;
- LangGraph 1.2.11 resolves/installs successfully there;
- the graph compiles/invokes successfully;
- the refactored focused tests pass;
- the adapter tests pass;
- R4-A/R4-B semantic comparison is green;
- real S001 LangGraph execution is green;
- LangGraph framework value/adoption.

## 11. Handoff

The coupling-correction responsibility is complete at source/design level. Return to the active R4-B Build route with executable proof next:

```text
WSL dependency resolution/install
→ focused native LangGraph graph tests
→ adapter-focused tests
→ diagnose/repair if needed
→ controlled R4-A vs R4-B semantic comparison
→ bounded real S001 smoke
```

For the corrected source-location/coupling story, this record supersedes the initial implementation-location/coupling description in the earlier active Build memory; that earlier record remains valid provenance for how the drift happened.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-build-implement`
