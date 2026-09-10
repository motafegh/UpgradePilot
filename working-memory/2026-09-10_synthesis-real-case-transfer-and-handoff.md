# Synthesis Real-Case Transfer and Investigation Handoff — Working Memory

**Date:** 2026-09-10  
**Session status:** ACTIVE  
**Primary mode:** Planning/Design + Learning-by-Doing  
**Selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-08_overall-evidence-sufficiency-synthesis-orientation.md`](2026-09-08_overall-evidence-sufficiency-synthesis-orientation.md)  
**Plan re-anchor commit:** `9472d392d3fafede6acb1fb25feef83470633e24`

## Session anchor

This record continues the same overall synthesis responsibility after a material route correction. The previous orientation record remains dated provenance for the September 8–10 design evolution, including the favorable-action discussion, artifact-serviceability pressure, planner-to-synthesis correction, proposal reconciliation, and initial Python handoff inspection. It should no longer be treated as the clearest current continuation surface.

The stable implementation boundary is unchanged:

```text
PublicPullRequestInvestigation
→ heterogeneous typed mechanism/evidence state
→ no accepted overall synthesis owner yet
→ no source/test implementation admitted until synthesis semantics are accepted
```

The selected plan remains the Overall Evidence Sufficiency and Maintainer Action Synthesis Plan. The September 10 plan refinement at `9472d392` did not change the product Charter, Product Decision Model specification, product source/tests, or framework status. It changed the design route so existing product-simulation evidence is used before new hypothetical cases or new simulation work.

## Why the route changed

During the previous learner reasoning point, Ali correctly chose the interpretation that a Python-support selector returning `None` after a typed target problem does **not** prove all useful investigation is finished. It means only that the selector does not select its supported exact-declaration acquisition again in that state. Whether another useful and admissible investigation remains requires a separate owner/evidence basis.

Ali also questioned whether `None` itself should be replaced by a more expressive return. That remains an open design question, but the discussion sharpened the ownership distinction:

```text
mechanism-specific selector responsibility
→ should this selector choose its supported check now?

investigation-to-synthesis handoff responsibility
→ what was selected/attempted, what resulted, and what continuation is justified or unknown?
```

Do not redesign the selector merely because synthesis needs richer state. First determine whether the required handoff facts are already available or derivable from existing producers. Add explicit state only for a genuine missing responsibility.

Ali then identified a more important learning/design problem: the reasoning example had been presented without clearly identifying whether it was real, real-derived, or synthetic. The Python `requires_python_absent` / repeat-suppression example was a **synthetic/controlled semantic example** derived from current source/test behavior, not a preserved public product-simulation scenario.

That challenge exposed a broader process correction: UpgradePilot already has a substantial product-simulation arm containing real and real-derived cases expressly intended to pressure later synthesis. Continuing mainly from convenient synthetic examples would ignore higher-value existing evidence.

## Product-simulation transfer finding

The product-simulation workspace was re-read under its local governance. Its role is discovery and pressure-testing evidence, not product semantic authority. Historical case actions are not automatically current UpgradePilot actions. New cases are admitted only for an explicit material uncertainty that existing evidence cannot answer; case count is not a reason to create S013.

The current synthesis responsibility already has strong transfer anchors:

| Evidence | Current synthesis value |
|---|---|
| S007 — package-family contradiction / stale planned check | selected investigation can lose value after stronger evidence; pressure historical selection versus current continuation |
| S008 — CARLA/OpenCV artifact serviceability | wheel-path loss, source fallback availability, source-build success, exact environment coverage and stopping remain distinct |
| S009 — pandas publication/reproducibility context | repository purpose/provenance can be decision-relevant without becoming technical applicability |
| S010 — NumPy requirement broadening | multiple mechanism candidates, different target handling, repository context and bounded discovery coverage must survive synthesis without scalar collapse |
| S011 — MLX optional environment/CI coverage | an owned environment/coverage question may be settled while deeper compatibility remains unresolved |
| S012 — persisted scikit-learn state | historical producer state can be required for applicability; a specific useful outside capability can remain identifiable |
| Conversation-C Investigation-Selection Pressure Test 01 | resolved-and-stop, path-pruned, and unresolved-with-no-supported-check are different stop reasons |
| Cross-Candidate + Repository-Context Synthesis Pressure Test 01 | preserve evidence vector, candidate/context distinction, coverage limits and stopped questions before action projection |
| B2/X1 No-Tool Disposition Transfer Evaluation | stop/defer/unresolved depend on the owned question, evidence state, admitted capability, attempt history and known outside responsibility |

A key historical handoff became newly relevant: the cross-candidate synthesis pressure test explicitly said it should be reused when main opens cross-candidate synthesis, overall sufficiency, repository-context admission, or maintainer-action projection. That condition is now satisfied.

## Evidence-class discipline for the current design

From this point, every material contrast used in the synthesis decision matrix should identify its evidence class:

```text
real public / preserved real-case evidence
real-derived controlled variant
current source/test state
synthetic/generated semantic control
```

Prefer real or real-derived evidence when it already discriminates the question. Use synthetic controls for exact variable isolation or state combinations that existing real cases do not cleanly expose.

A synthetic example must not be taught or recorded as though it were an observed public case, and it must not alone establish public prevalence, production reliability, a new domain capability, or a maintainer-action permission boundary.

## Revised plan route now in force

The plan was updated at `9472d392d3fafede6acb1fb25feef83470633e24` with these execution consequences:

```text
1. Re-anchor current synthesis questions against existing product-simulation evidence.
2. Recover actual heterogeneous producer/input state.
3. Reconcile transferred distinctions with real producer reachability.
4. Define the smallest deterministic transparent synthesis baseline.
5. Build and pressure the decision matrix using real evidence first.
6. Identify genuine evidence gaps only after the existing corpus is exhausted for the question.
7. Ask product simulation for bounded new work only when such a gap survives.
8. Accept/promote stable synthesis semantics before Build.
```

The semantic acceptance gate now explicitly requires an evidence-transfer coverage map and evidence-class labels before implementation.

## Current evidence-transfer questions

The next analysis should not try to decide all five Charter outcomes immediately. It should build a compact transfer map around the questions that currently block a clean synthesis contract.

### Investigation continuation / stopping

Primary evidence: S007, Conversation-C pressure test, B2/X1 no-tool evaluation, and the current Python declaration acquisition source/tests.

Need to determine:

```text
what facts distinguish historical selection/attempt from current useful continuation?
which stop distinctions are already supported by existing evidence?
what is derivable from current producers?
what genuinely requires a new handoff fact?
```

The learner conclusion already accepted for the current reasoning checkpoint is:

```text
selector returns None after a typed problem
!= all worthwhile UpgradePilot investigation is finished
```

### Artifact exact applicability and consequence

Primary evidence: S008 plus current artifact-serviceability and Target artifact-environment source/tests.

Need to keep separate:

```text
published wheel capability loss
exact target wheel compatibility
source fallback availability
source fallback success
CI/environment coverage of the relevant branch
```

Current normal application still does not produce exact target wheel-tag evidence. This is not automatically a reason to outsource work to maintainers or add a product capability. First decide whether an admitted useful UpgradePilot investigation exists and whether current producers can represent that continuation.

### Repository/context admission and heterogeneous combination

Primary evidence: S009 + S010 + the cross-candidate synthesis pressure test.

Need to determine the smallest context/evidence responsibilities that may alter action permission without:

- coercing repository context into technical applicability;
- averaging mechanism states;
- treating one resolved candidate as discovery completeness;
- erasing a mitigated or secondary material candidate;
- inventing repository policy or risk tolerance.

### Stop / defer / abstain and outside capability

Primary evidence: S011 + S012 + the no-tool transfer evaluation.

Need to pressure the difference between:

```text
owned question settled while adjacent uncertainty remains
specific useful outside responsibility exists
no admitted useful action and no grounded outside responsibility exists
```

Do not import old experiment disposition labels as final synthesis actions. Transfer the underlying semantic distinction first.

### Investigate versus block, maintainer-check handoff, favorable permission

These remain likely pressure areas, but they are **candidate gaps**, not established gaps.

Before requesting new product-simulation work, verify whether existing S003/S006/S007/S008/S010 and cross-case evaluations already discriminate them adequately. Only if a material decision remains unresolved should a bounded gap request be prepared for Ali to authorize.

## Current working hypotheses — not accepted semantics

1. Synthesis should consume richer investigation-handoff meaning than a selector's `Selection | None` result, but that does not yet justify changing the selector API.
2. Action-relative sufficiency remains the simplest credible baseline; a separate sufficiency enum needs independent value before adoption.
3. A useful unresolved proposition/check first belongs to investigation-value and UpgradePilot-execution-admissibility reasoning; maintainer-facing `run targeted checks` comes later and needs its own permission basis.
4. Technical mechanism truth does not directly determine overall maintainer action.
5. Existing real-case evidence is likely sufficient to pressure much of V1 synthesis; new simulation should be requested only for a surviving semantic gap.

None of these are accepted stable synthesis rules yet.

## Current Learning-by-Doing cycle

```text
Slice: re-anchor synthesis design on existing product-simulation evidence

A — DONE:
    clarified that the previous Python reasoning example was synthetic/controlled and oriented the role of the simulation arm.

B — DONE:
    inspected the product-simulation governance, scenario/case inventory and the synthesis-relevant S007–S012 / cross-case transfer evidence; revised the selected plan to make real-case transfer the first design stage.

C — DONE:
    this continuation record preserves the corrected evidence classes, transfer anchors, revised route and current hypotheses.

D — DONE for the route correction:
    Ali identified the synthetic-versus-real ambiguity and explicitly directed the work back toward the existing real-case evidence arm.

E — ACTIVE:
    begin the first evidence-transfer coverage map, using existing real cases plus current producer/source truth; identify genuine handoff gaps before inventing new fields, action rules or cases.
```

## Immediate continuation

Begin with one bounded cross-owner contrast rather than all action classes at once:

```text
INVESTIGATION CONTINUATION / STOPPING

S007 + Conversation-C pressure evidence
        ↕
current Python declaration selection/attempt/result path
        ↓
map:
what is already available
what is derivable
what is genuinely missing
what historical simulation distinction cannot yet be represented by normal product producers
```

Then move to S008/current artifact exact-compatibility state and repeat the same transfer/reachability test.

The immediate output should be a compact evidence-transfer + producer-reachability map, not a new runtime type. Only after those two contrasts are grounded should the decision matrix resume action-permission pressure.

No new product-simulation case, stable specification change, source/test implementation, framework work, or LLM synthesis experiment is currently authorized by this record.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
