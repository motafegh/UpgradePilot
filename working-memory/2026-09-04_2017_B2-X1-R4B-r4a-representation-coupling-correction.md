# B2/X1 R4-B — R4-A Representation Coupling Drift and Correction

**Date/time:** 2026-09-04 20:17 (+03:30)  
**Session status:** ACTIVE  
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

R4-B should own its workflow communication model, for example:

```text
PlannerActionProposal
PlannerNoAction
PlannerProviderProblem
→ R4-B PlannerOutcome

AuthorizedAction
AuthorityRejection
→ R4-B AuthorityOutcome

AuthoritySnapshot
→ R4-B current T2 product/orchestration snapshot

InvestigationOutcome
FinalResult
→ R4-B graph/result contracts
```

R4-A may still be reused **behind adapters** for experimental control:

```text
R4-B planner port
→ R4-A control planner adapter
   → compose existing bounded R4-A model context
   → invoke existing controlled model/provider seam
   → map R4-A result into R4-B PlannerOutcome

R4-B authority port
→ R4-A control admission adapter
   → translate R4-B current snapshot/proposal into temporary R4-A admission inputs
   → call existing deterministic admission oracle
   → map result into R4-B AuthorityOutcome
```

The R4-B graph itself should not need to know `EvidenceGapDecision`, `EvidenceGapPlannerContext`, `EvidenceGapAdmissionState`, or R4-A admission result classes.

## 5. Product-owned reuse remains direct

This correction does **not** mean reimplementing established product truth merely to look independent. Direct reuse remains appropriate for product/domain owners such as:

```text
PublicPullRequestInvestigation
PythonSupportDropImpactAssessment / product investigation selection
GitHub exact repository acquisition contract
interpret_target_python_declaration(...)
evaluate_target_python_relevance(...)
evaluate_python_support_drop_impact(...)
PropositionAssessment
```

The boundary being corrected is specifically R4-A experiment representation ownership, not legitimate product capability reuse.

## 6. File-layout correction

Ali also requested an explicit LangGraph implementation area rather than leaving the framework implementation mixed into the root experiment module collection.

Created:

`experiments/langgraph/`

with package marker:

`experiments/langgraph/__init__.py`

The R4-B implementation/adapters will move into this package. Focused experiment regression remains under the existing repository test boundary `experiments/tests/`.

## 7. Corrective Build route

```text
1. isolate LangGraph implementation under experiments/langgraph/
2. introduce R4-B-owned planner/authority/state/result contracts
3. move all direct R4-A comparison/control imports into a narrow adapter module
4. keep product/domain imports direct where they own truth
5. update focused tests to exercise R4-B-owned contracts
6. remove the old root-level LangGraph module
7. inspect resulting import/dependency direction
8. execute focused tests in WSL when available
```

## 8. Evidence / non-proof at correction start

Established:

- the coupling drift is visible in the written source;
- the reason for the drift is understood: comparison-control reuse escaped its intended adapter boundary;
- the correction preserves the valid goal of holding model/admission semantics constant without letting R4-A define LangGraph architecture;
- the dedicated LangGraph experiment package now exists.

Not yet established:

- the refactored source is complete;
- all R4-A representation imports are isolated from the graph core;
- focused tests have been updated;
- the refactored graph imports/compiles/runs in WSL;
- semantic equivalence or framework value.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-build-implement`
