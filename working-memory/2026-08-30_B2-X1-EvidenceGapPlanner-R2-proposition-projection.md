# B2/X1 EvidenceGapPlanner R2 — Proposition Projection

**Date:** 2026-08-30  
**Status:** R2 SLICE COMPLETE — proposition field boundary decided  
**Plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Parent R2 memory:** `2026-08-30_B2-X1-EvidenceGapPlanner-R2-model-visible-context.md`  
**Previous R2 slice:** `2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-question.md`

## 1. Product truth inspected

Current product owner:

`src/upgradepilot/impact/applicability.py::PropositionAssessment`

Current fields:

```text
key
state
  established | refuted | unresolved | conflicted

evidence_coverage
  sufficient | insufficient | unresolved

evidence_owner
detail
```

There is no product `origin` field and no product `raw_external_text` flag.

E2 created experiment-only lineage labels such as:

```text
model_derived_semantics_deterministically_grounded
deterministic_pre_acquisition_state
deterministic_derived_state
```

Those labels were useful for tracing semantic/raw-text carryover, but they are not current product proposition state and should not be promoted into the planner contract without a separate product need.

## 2. Decision — model-visible proposition projection

Use:

```text
proposition:
    key
    state
    evidence_coverage
    evidence_owner
    detail
```

Do not add `origin` or `raw_external_text` to the base proposition projection in the current first seam.

## 3. Why each field earns model visibility

### `key`

Purpose:

- stable semantic identity for the proposition;
- lets the planner relate unresolved state to action targets/preconditions;
- supports dependency/prerequisite reasoning between propositions;
- avoids relying on prose matching alone.

The key is project-owned. The model does not invent proposition identities.

### `state`

Purpose:

- core epistemic status;
- distinguishes established, refuted, unresolved, and genuinely conflicted propositions;
- directly supports stopping, pruning, prerequisite, and evidence-gap reasoning.

This is deterministic/domain-owned trusted state.

### `evidence_coverage`

Purpose:

- distinguishes missing/insufficient evidence from a proposition that remains unresolved despite sufficient admitted evidence;
- supports open-world reasoning and negative-inference boundaries;
- helps the planner distinguish "acquire more evidence" from "the current method cannot decide this proposition."

Important example from the real Python-support path:

```text
state = unresolved
evidence_coverage = insufficient
→ exact target declaration has not yet been acquired
```

versus:

```text
state = unresolved
evidence_coverage = sufficient
→ exact declaration exists, but the accepted comparison method cannot resolve activation
```

These states should not lead to the same investigation automatically.

### `evidence_owner`

Purpose:

- gives the bounded domain/location of the proposition/evidence responsibility;
- supports the Product Decision Model requirement to start from the location/reason of uncertainty/conflict;
- helps distinguish upstream, target, CI/environment, relevance/comparison, and other evidence gaps;
- can improve later capability matching without exposing exact provider/source locators.

Examples:

```text
upstream.claim
target.python
target.relevance
dependency.ci
```

This is a compact responsibility/location signal, not execution authority.

### `detail`

Purpose:

- bounded project-authored/domain-interpreted explanation of what the state means in this case;
- preserves distinctions that state/coverage alone cannot communicate;
- can explain prerequisites, unsupported comparison boundaries, or reason for conflict.

Current product examples are interpreted/domain-authored text such as:

```text
Exact target Python declaration evidence has not yet been acquired.

Activation cannot be evaluated before exact target declaration evidence has been acquired.

The exact target declaration was acquired, but the accepted deterministic comparison method cannot resolve the activation proposition...
```

The current planner projection may expose such bounded detail.

## 4. `detail` safety / projection rule

Do not define the R4 request renderer as:

```text
serialize any future PropositionAssessment.detail blindly
```

Instead preserve the architectural rule:

> planner-visible `detail` must be bounded project-authored or already-interpreted domain text whose content is intentionally admitted for planning.

If a future proposition owner places raw/near-raw external content into `detail`, that does not automatically authorize the content to cross the planner boundary.

Therefore:

```text
product field exists
!= every future value is automatically model-admitted
```

R4 should make the projection explicit and test for the intended first-seam owners/cases rather than relying on whole-object serialization.

## 5. Why `origin` is not included now

E2 proved an important fact:

```text
raw external text omitted
!= semantic influence absent
```

The upstream support-drop proposition can carry model-derived semantics even when raw source prose is absent.

However the current `origin` labels were experiment-side classification logic, not a stable product contract. Adding them now would require answering broader questions such as:

- what complete origin taxonomy exists across all proposition owners?
- can one proposition have mixed deterministic/semantic provenance?
- what exact planning behavior should change based on origin?
- is origin a proposition property, evidence property, or provenance-chain property?

No current first-seam planning decision has demonstrated that such metadata changes action selection.

Decision:

```text
origin
→ retain as experiment/provenance learning
→ do not add to base model-visible proposition state now
```

If later reliability/risk reasoning needs semantic provenance, prefer designing it as evidence/provenance metadata deliberately rather than inventing an incomplete proposition-level flag.

## 6. Why `raw_external_text` flag is not included now

The current boundary already keeps Level-3 raw evidence outside the first-seam model context by construction.

Therefore a proposition-level flag such as:

```text
raw_external_text = false
```

adds little planning information and risks creating a false sense that one Boolean can describe the complete provenance/safety story.

Decision:

```text
raw_external_text flag
→ omit from first-seam proposition projection
```

If future context intentionally admits bounded raw/near-raw evidence, the trust/source classification should be represented at that evidence item's actual boundary rather than retrofitted onto every proposition.

## 7. Relationship to `EvidenceGapPlanningEvidence`

Keep the responsibilities separate:

```text
PropositionAssessment projection
→ decision-state spine
→ what proposition is known/refuted/unresolved/conflicted and with what coverage

EvidenceGapPlanningEvidence
→ selected richer mechanism/witness/limitation/unresolved-condition details
  when those facts materially affect which investigation is useful next
```

Do not overload `detail` until it becomes a second evidence object graph.

If structured CI reachability, witness path, unresolved marker conditions, or other richer facts matter, represent them in `EvidenceGapPlanningEvidence` rather than stuffing them into one long proposition string.

## 8. Current proposition projection candidate

```text
propositions:
  - key: upstream_python_support_drop_crossed
    state: established
    evidence_coverage: sufficient
    evidence_owner: upstream.claim
    detail: <bounded interpreted explanation>

  - key: exact_target_python_declaration_established
    state: unresolved
    evidence_coverage: insufficient
    evidence_owner: target.python
    detail: <bounded interpreted explanation>

  - key: declared_python_range_intersects_dropped_line
    state: unresolved
    evidence_coverage: insufficient
    evidence_owner: target.relevance
    detail: <bounded interpreted explanation>
```

No target repository/PR/revision identity is required in the model-visible proposition entries.

## 9. LbD concepts earned in this slice

- proposition identity vs human explanation;
- epistemic state vs evidence coverage;
- uncertainty location / evidence ownership;
- provenance metadata vs planning state;
- experiment-only lineage vs product-owned state;
- explicit projection vs whole-object serialization;
- bounded interpreted text vs raw external evidence;
- avoiding both context starvation and evidence dumping.

## 10. Next R2 slice

Continue with trusted attempted-action history:

```text
action_id
outcome
```

and answer:

- what exactly counts as an attempted action?
- when is an action recorded: proposal, admission, start, or completion?
- is `completed | problem | rejected` expressive enough?
- what result/finding belongs in trusted propositions / planning evidence rather than action history?
- how should retryable transport failure differ from a completed domain/evidence problem?
