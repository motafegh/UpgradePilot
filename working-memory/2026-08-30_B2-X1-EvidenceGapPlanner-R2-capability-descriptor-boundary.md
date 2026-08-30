# B2/X1 EvidenceGapPlanner R2 — Model-Visible Capability Descriptor Boundary

**Date:** 2026-08-30  
**Status:** R2 SLICE COMPLETE — planner-visible action-space descriptor boundary decided  
**Plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Parent R2 memory:** `2026-08-30_B2-X1-EvidenceGapPlanner-R2-model-visible-context.md`  
**Previous R2 slice:** `2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-budget-envelope.md`

## 1. Why this slice exists

The historical experiment owns a rich trusted `AllowedInvestigationAction` with fields such as:

```text
action_id
purpose
target_proposition
repository
revision
path
required_proposition_state
required_evidence_coverage
mutation_class
result_families
cost_class
```

The historical request renderer exposed essentially the whole trusted action descriptor to the model.

That was useful experiment evidence, but it is not retention authority for the evidence-refined `EvidenceGapPlanner` contract.

R2 now applies the same projection rule used for case identity, propositions, evidence, history and budget:

```text
trusted action field exists
!=
model needs to see it
```

The model should receive enough information to understand the **available evidence-acquisition choice and its information value**, while deterministic code retains action definition, current applicability, authority, exact execution identity and result-family enforcement.

## 2. Working planner-facing concept

Use **`EvidenceGapActionDescriptor`** as the working name for the model-visible projection of one currently admitted bounded investigation action.

This is deliberately different from the full trusted action object.

Definition:

> `EvidenceGapActionDescriptor` is the bounded model-visible description of one currently admitted investigation action, exposing the action's stable identity, purpose, evidence gap and possible evidence contribution without exposing execution locators or transferring admission/authorization responsibility to the model.

Do not freeze a product dataclass from this design record. R4 owns the smallest experiment representation.

## 3. First-seam model-visible fields — DECIDED

Use:

```text
EvidenceGapActionDescriptor
    action_id
    purpose
    target_proposition
    evidence_yield
```

### `action_id`

Keep model-visible.

Purpose:

- stable trusted selection token;
- lets `EvidenceGapDecision` identify one exact currently offered action;
- supports consumed-action history and deterministic lookup/rebinding;
- avoids model-generated tool names/locators.

The model selects the ID; it does not define what the ID means.

Keep `action_id`, rather than renaming it to a generic `capability_id`, because the current trusted catalog entry is a **pre-bound action instance**. Future systems may admit the same general capability against different targets/inputs, so concrete action identity matters.

### `purpose`

Keep model-visible.

Purpose:

- tells the planner what decision-relevant uncertainty the action is intended to advance;
- supports information-value reasoning without exposing implementation detail;
- remains project-authored trusted description.

The purpose should be concise and responsibility-oriented, not a hidden instruction to choose the action.

### `target_proposition`

Keep model-visible.

Purpose:

- explicitly links the action to the proposition/evidence gap it can advance;
- supports future reasoning when several unresolved propositions/actions coexist;
- avoids relying on fuzzy prose matching between action purpose and proposition detail.

Deterministic admission still verifies this binding from the trusted action object.

### `evidence_yield`

Add as the preferred planner-facing semantic result description.

Meaning:

> a bounded project-authored description of what useful evidence/result this action can produce for planning purposes.

Example for current A1:

```text
evidence_yield:
    "Exact target Python declaration evidence or a typed target-declaration problem."
```

Why this is better than exposing raw `result_families`:

- Python class names such as `TargetPythonDeclaration` / `TargetPythonDeclarationProblem` are execution/domain-contract details, not the best semantic planning vocabulary;
- the planner needs to reason about **what it may learn**, not about implementation type names;
- deterministic code still owns and checks the exact accepted result families.

`evidence_yield` must be bounded project-authored semantics, not model-generated authority or raw provider content.

## 4. Fields kept deterministic/system-only in the first seam

### `repository`, `revision`, `path`

Omit from model context.

Already decided in earlier R2 slices:

```text
exact source/action identity
→ trusted action/executor/admission state
→ not current model reasoning context
```

After `action_id` selection, deterministic lookup recovers the exact repository/revision/path.

### `required_proposition_state`, `required_evidence_coverage`

Omit from the base model-visible descriptor.

Reason:

- the model already receives current proposition state/coverage;
- the **allowed action catalog should contain actions that are currently admissible/useful candidates** under trusted state;
- deterministic admission/revalidation owns enforcement of exact preconditions immediately before execution;
- exposing precondition fields risks making the model appear responsible for deciding whether the action is authorized.

This does not delete the fields from the trusted action object.

If a future planner responsibility intentionally reasons over **conditional/future actions not currently admitted**, that is a different action-space contract and should be designed explicitly rather than overloading `allowed_actions` now.

### `mutation_class`

Omit from current model context.

The current X1 responsibility admits read-only investigation actions only. Therefore every planner-visible action should already satisfy that policy before it reaches the model.

```text
all offered actions are read-only
→ mutation_class adds no current selection information
→ deterministic admission still enforces the boundary
```

If future scope ever includes actions with materially different mutation/authorization classes, that is a responsibility expansion requiring an explicit architecture/safety decision. Do not prepare the model for that hypothetical now.

### `result_families`

Do not expose raw implementation result-family/class names to the model.

Keep them trusted for:

- execution/result validation;
- domain interpretation routing;
- deterministic admission/rebinding where required.

Expose only the bounded semantic `evidence_yield` when it helps planning.

### `cost_class`

Keep trusted/system-side in the current one-action seam; do not expose merely for future extensibility.

Current values such as:

```text
local
low_network
moderate_network
local_model
```

are coarse categorical product/experiment metadata. With one real action they cannot affect selection.

Promote a planner-visible **resource profile** later only when:

1. multiple independently admitted actions are simultaneously plausible;
2. their cost/latency/resource differences are material;
3. the differences are measured or trustworthy enough to reason about;
4. a real planning-budget dimension can make the choice change.

Prefer a future semantic shape such as:

```text
resource_profile
    latency / external cost / compute / network dimensions
```

when earned, rather than assuming historical `cost_class` is the final planner vocabulary.

## 5. Current first-seam action projection

Candidate:

```text
allowed_actions:
  - action_id: acquire_exact_target_python_declaration
    purpose: >
      Acquire the exact target Python declaration needed to advance
      the unresolved Python-support exposure/activation question.
    target_proposition: exact_target_python_declaration_established
    evidence_yield: >
      Exact target Python declaration evidence or a typed
      target-declaration problem.
```

Hidden trusted action state still contains, where applicable:

```text
repository
revision
path
required state / coverage
mutation class
exact result families
cost class / telemetry
provider/executor metadata
```

## 6. Why not show preconditions just because they may help reasoning?

There is an important separation:

```text
MODEL QUESTION
Which currently offered action has the best discriminating value?

DETERMINISTIC QUESTION
Is this action actually still admissible under the latest trusted state/policy?
```

The first is planning.
The second is execution authority / freshness control.

If the model sees `required_state=unresolved` and checks it itself, that may be understandable, but it adds no authority and duplicates state already supplied. The system must re-check the condition anyway.

Therefore the first seam keeps the model observation focused on **evidence value**, not authorization mechanics.

## 7. Action space vs capability space — terminology learned

A useful distinction emerged:

```text
GENERAL CAPABILITY
"read an exact repository file"

PRE-BOUND ACTION INSTANCE
"acquire this exact target Python declaration for this exact trusted target state"
```

The current `AllowedInvestigationAction` is closer to the second because it carries exact repository/revision/path and proposition binding.

The model should select the pre-bound action ID, while deterministic code owns the hidden binding.

This is why `action_id` remains a better first-seam selection field than a generic `capability_id`.

Future richer catalogs may separately model reusable capability definitions and concrete bound action instances if real repetition justifies the distinction.

## 8. Relationship to planning budget

Current one-action descriptor does not expose cost because there is no meaningful trade-off.

Future richer planning may look like:

```text
planning_budget
    remaining_investigations
    remaining_time_seconds

action A resource_profile
    expected latency = low

action B resource_profile
    expected latency = high
```

Only then can resource information legitimately change evidence-gap selection.

R4/R5 should collect real timing/resource telemetry before quantitative cost-aware planner fields are invented.

## 9. Relationship to LangGraph/LangChain learning

This boundary remains framework-independent.

During R4:

```text
EvidenceGapActionDescriptor[]
→ bounded model observation / action-space input

trusted full action objects
→ deterministic graph/control-plane state
```

The LangGraph implementation must preserve the same separation rather than treating framework tool definitions as automatic model authority.

The LangChain slice should compare its tool-schema abstractions with this custom projection/admission boundary and identify where higher-level tool metadata helps or overexposes implementation details.

## 10. R4 implementation/test pressure

The coherent experiment should prove:

- rendered action descriptors contain only the decided planner-facing fields;
- repository/revision/path do not enter model context;
- precondition enforcement remains deterministic;
- mutation policy remains deterministic;
- raw result-family/class names are not required in model output/context;
- semantic `evidence_yield` is sufficient to explain what the action can learn;
- action ID still rebinds to the exact trusted action instance;
- future resource profile remains absent until a real decision need earns it.

R3 should also reconsider the historical model output field `expected_result_categories`: the evidence-refined contract should not require the model to echo deterministic result families merely because v2 did.

## 11. LbD concepts earned in this slice

- action space vs execution authority;
- general capability vs pre-bound action instance;
- information-value description vs implementation result types;
- model-visible descriptor vs trusted execution object;
- semantic projection vs whole-object serialization;
- deterministic preconditions / admission;
- policy enforcement vs reasoning context;
- cost telemetry vs cost-aware planning;
- why optional future extensibility should not pollute the first-seam observation.

## 12. Next R2 slice

The field-level decisions are now sufficiently complete to perform the **R2 synthesis/projection proof**.

Next:

1. create the final field/owner/visibility/reason table;
2. construct representative evidence-refined request shapes for:
   - S001 action state;
   - no-tool state;
   - richer `EvidenceGapPlanningEvidence` state;
   - consumed-action repeat state;
3. inspect for duplication, authority leakage, context starvation and stale historical fields;
4. reconcile any final contradiction in the active plan/memory;
5. if the projection proof passes, close R2 and advance to R3 `EvidenceGapDecision` / deterministic admission design.
