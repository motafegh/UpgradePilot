# B2/X1 EvidenceGapPlanner R3 — Wire Shape and Deterministic Admission Contract

**Date:** 2026-08-30  
**Status:** R3 COMPLETE / PASS — candidate decision wire shape and deterministic admission responsibility frozen for R4 implementation  
**Plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Previous R3 slice:** `2026-08-30_B2-X1-EvidenceGapPlanner-R3-decision-semantics.md`

## 1. Question

What is the smallest structured `EvidenceGapDecision` that preserves the semantic decisions frozen in R3 while leaving trusted action metadata, current applicability, execution authorization and result contracts with deterministic owners?

## 2. Final candidate decision kinds

Use:

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

Detailed semantics are owned by `2026-08-30_B2-X1-EvidenceGapPlanner-R3-decision-semantics.md`.

## 3. Final first-seam wire shape

Use one fixed three-field object:

```text
EvidenceGapDecision
    decision_kind
    action_id
    explanation
```

Conceptual JSON:

```json
{
  "decision_kind": "ACTION_SELECTED",
  "action_id": "acquire_exact_target_python_declaration",
  "explanation": "The target declaration remains the discriminating missing evidence."
}
```

No-tool example:

```json
{
  "decision_kind": "QUESTION_SETTLED",
  "action_id": null,
  "explanation": "The bounded question has sufficient evidence and no further investigation is justified."
}
```

## 4. Why fixed shape instead of a tagged union

A tagged union could omit `action_id` entirely for no-tool decisions, but the current first seam does not earn that additional schema complexity.

A fixed shape gives:

- one stable logging/replay representation;
- one small provider JSON Schema;
- easy deterministic parsing;
- explicit `null` action for no-tool decisions;
- simple comparison across plain-Python/LangGraph implementations.

Cross-field semantic invariants remain deterministic parser responsibility rather than relying on sophisticated provider schema features.

Therefore:

```text
JSON Schema
→ field/type/membership shape

parser
→ cross-field semantic shape

admission
→ fresh action authority/current-state checks
```

## 5. Candidate provider JSON Schema

Conceptually:

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["decision_kind", "action_id", "explanation"],
  "properties": {
    "decision_kind": {
      "type": "string",
      "enum": [
        "ACTION_SELECTED",
        "QUESTION_SETTLED",
        "KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY",
        "NO_JUSTIFIED_INVESTIGATION_IDENTIFIED"
      ]
    },
    "action_id": {
      "anyOf": [
        {"type": "string", "minLength": 1},
        {"type": "null"}
      ]
    },
    "explanation": {
      "type": "string",
      "minLength": 1
    }
  }
}
```

Do not freeze an arbitrary explanation maximum length merely for neatness. Provider/model token limits and R4 request configuration already bound the experimental response; add an explicit semantic length limit only if actual model behavior requires it.

## 6. Deterministic parser invariants

After schema-valid parsing:

```text
ACTION_SELECTED
→ action_id must be non-null, non-empty, trimmed

QUESTION_SETTLED
KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
→ action_id must be null

all kinds
→ explanation must be non-empty trimmed text
```

A schema-valid but semantically inconsistent object is rejected before action admission.

Example:

```json
{
  "decision_kind": "QUESTION_SETTLED",
  "action_id": "acquire_exact_target_python_declaration",
  "explanation": "..."
}
```

is invalid even if the JSON types are correct.

## 7. Historical output fields removed

Do **not** include these historical model echoes in the new base decision:

```text
target_proposition
expected_result_categories
limitations
```

### `target_proposition`

The selected `action_id` rebinds to the trusted action's exact target proposition.

For no-tool decisions, forcing one target proposition is artificial because the reasoning may concern the bounded question/state as a whole.

### `expected_result_categories`

The trusted action owns exact result/problem families. R2 exposes semantic `evidence_yield` to the model for reasoning; the model does not need to echo Python result-class names.

Removing this field also removes the historical need for:

```text
expected_result_categories_mismatch
```

as an admission check.

### `limitations`

Free-form limitations are not trusted authority and materially overlap `explanation` for the current seam.

If later product behavior needs typed caveats/limitations as durable evidence, design that responsibility explicitly rather than retaining an untrusted model array because v2 had one.

## 8. Decision processing has three distinct layers

### Layer A — parse/shape validation

Owns:

- exact three fields;
- supported decision kind;
- action-id nullability invariant;
- non-empty explanation.

Produces:

```text
EvidenceGapDecision
```

This remains an **untrusted model decision**.

### Layer B — no-tool handling

For:

```text
QUESTION_SETTLED
KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

the decision executes no action.

Do not pretend deterministic admission proves the semantic explanation correct. The no-tool decision is model reasoning to be evaluated against trusted state; it simply grants no execution authority.

Therefore:

```text
parsed no-tool decision
→ no capability execution
→ preserve/return decision for orchestration/evaluation
```

No action admission object is required merely to make a no-tool result look authoritative.

### Layer C — action admission

Only `ACTION_SELECTED` enters deterministic action admission.

The model-selected `action_id` is looked up/rebound against fresh trusted state.

## 9. Pre-model action-space construction

The model-facing `allowed_actions` should be constructed from currently offered/admitted action candidates.

Before the model call, trusted orchestration/catalog construction should exclude actions that are already known not to be currently offerable, for example when applicable:

- action preconditions do not hold;
- action is already consumed for the exact bounded state;
- mutation policy excludes it;
- exact trusted action binding cannot be constructed.

This keeps model context semantically clean.

However, this pre-call filtering is **not sufficient authority** because state may change while the model is reasoning.

Post-model fresh admission remains mandatory.

## 10. Zero planning budget — deterministic pre-call gate

If:

```text
planning_budget.remaining_investigations <= 0
```

then orchestration should normally avoid asking the model to choose an investigation action at all.

Budget exhaustion is a deterministic control/resource state, not an `EvidenceGapDecisionKind`.

This avoids spending a model call to rediscover a hard control-plane fact.

If a race/state change causes budget to reach zero after the model request was constructed, post-model admission must still reject action execution.

## 11. Fresh deterministic action admission

For `ACTION_SELECTED`, rebind the selected ID to the fresh trusted action owner and re-check at least:

```text
1. action ID is known/currently offered by trusted catalog
2. action has not become consumed for this exact bounded state
3. planning budget still permits one investigation to begin
4. current proposition/evidence preconditions still hold
5. mutation/policy boundary still permits the action
6. exact repository/revision/path/arguments remain trusted and bound by deterministic owner
7. the action is still fresh/actionable immediately before execution
```

The model does not echo any of those authority fields.

This is the TOCTOU boundary:

```text
model saw action at T1
→ state may change
→ deterministic admission re-checks at T2
```

## 12. Candidate admission-problem vocabulary for R4

Use responsibility-oriented problems as needed by the first coherent implementation:

```text
invalid_decision_shape
unknown_action
action_consumed
budget_exhausted
action_not_currently_actionable
action_not_allowed_by_policy
```

Do not mechanically retain historical problems that existed only because the model echoed trusted metadata:

```text
target_proposition_mismatch
expected_result_categories_mismatch
```

Those checks disappear when those echoes disappear.

Exact final Python enum/class names belong to R4 implementation and may be refined by the Naming Clarity specification; R3 freezes the responsibilities, not every identifier.

## 13. Catalog filtering vs admission defense-in-depth

Correct relationship:

```text
PRE-CALL
build a clean currently offered action projection
→ helps model reason from a sane action space

POST-CALL
rebind/revalidate selected ID against fresh trusted state
→ execution authority / stale-state defense
```

Therefore an action can be absent from the model-visible catalog because it is consumed, while deterministic admission still keeps an `action_consumed` guard in case of stale/concurrent/replayed output.

This is intentional defense-in-depth, not redundant ownership.

## 14. Explanation is reasoning, not authority

The model explanation is useful for:

- debugging/evaluation;
- human understanding;
- comparing plain Python/LangGraph behavior;
- diagnosing whether the model selected an action for the right reason.

It does **not**:

- change proposition truth;
- create evidence;
- define tool arguments;
- override admission;
- establish compatibility/safety/merge truth.

## 15. R3 proof matrix for R4 tests

R4 should implement focused tests for at least:

```text
valid ACTION_SELECTED + known current action
→ admitted action

ACTION_SELECTED + null action_id
→ invalid decision shape

no-tool + non-null action_id
→ invalid decision shape

unknown action_id
→ deterministic admission problem

consumed action replay/stale output
→ deterministic admission problem

budget exhausted after request construction
→ deterministic admission problem

precondition changed after request construction
→ action_not_currently_actionable

settled no-tool
→ no execution

known outside-boundary no-tool
→ no execution

no-justified-investigation no-tool
→ no execution
```

## 16. R3 final decision

**PASS.**

The candidate first-seam output is:

```text
EvidenceGapDecision
    decision_kind
    action_id | null
    explanation
```

with semantic kinds:

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

and authority split:

```text
model
→ semantic choice + exact offered action ID + explanation

deterministic parser
→ shape/cross-field validity

deterministic admission
→ fresh action/current-state/budget/policy/execution authorization

domain owners
→ execution result interpretation + proposition/planning-evidence update
```

No R3 blocker remains for the experiment-owned R4 implementation.

## 17. R4 handoff

R4 is now authorized by this plan sequence to build the coherent experiment seam:

```text
R4-A ordinary-Python reference/control
R4-B same responsibility in LangGraph
R4-C bounded LangChain learning/integration slice
R4-D compare implementations
```

Before adding dependencies or source files, use the active Build/LbD procedure and preserve product-runtime isolation.

## 18. LbD concepts earned

- wire format vs semantic contract;
- JSON Schema shape vs cross-field semantic validation;
- tagged union vs fixed nullable-field representation;
- model echo elimination;
- trusted rebinding by stable action ID;
- pre-call catalog filtering vs post-call admission;
- TOCTOU / stale-plan defense;
- no-tool decision vs action authorization;
- resource gate vs epistemic decision;
- defense-in-depth without duplicate semantic ownership.
