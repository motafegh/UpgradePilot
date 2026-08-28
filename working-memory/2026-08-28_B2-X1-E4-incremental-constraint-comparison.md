# B2/X1 E4 — Incremental Constraint Comparison

**Date:** 2026-08-28  
**Status:** ACTIVE — E4.1 COMPLETE; E4.2 COMPLETE; E4.3 DETERMINISTIC ADMISSION NEXT  
**Parent exploration:** `working-memory/2026-08-28_B2-X1-evidence-first-llm-risk-and-design-exploration.md`

## Purpose

E4 tests candidate planner controls one at a time, starting from the successful E3 minimally constrained S001 planner behavior.

The comparison discipline is:

```text
freeze the successful planner state
→ change one control
→ observe what changed
→ do not reacquire unrelated live evidence unless that is the variable being tested
```

## E3 control result

The successful E3 run showed that `gemma-4-e4b-it-ud`, given the real typed pre-investigation S001 propositions and bounded planning question, naturally proposed acquiring the exact target Python declaration.

The model correctly followed:

```text
upstream support drop established
→ exact target declaration unresolved / insufficient
→ range intersection depends on that missing declaration
→ acquire target declaration next
```

It did not receive a closed action catalog, JSON Schema, deterministic admission, or raw upstream changelog prose.

Persisted local E3 evidence:

```text
/tmp/upgradepilot-b2-x1-e3-minimal-s001-planner.json
```

## E4.1 design correction before valid execution

The first E4.1 implementation reacquired the entire real S001 normal product path. That was methodologically wrong for an incremental-control comparison because it added GitHub REST state, provider acquisition, the support-drop semantic-model pass, and grounding as uncontrolled variables.

Observed failed attempts before the correction were therefore **not planner results**:

1. one run did not retain the expected pre-investigation assessment;
2. a diagnostic revision was prepared to preserve that upstream prerequisite state;
3. the next run stopped at public GitHub acquisition with the client's `forbidden_or_rate_limited` category.

The experiment was then corrected to replay the exact successful E3 planner input instead of reacquiring S001.

Correct E4.1 flow:

```text
persisted successful E3 JSON
→ validate exact S001 identity / baseline / boundary facts
→ fingerprint replay source
→ retain exact E3 question + propositions
→ add one trusted action descriptor from build_target_python_declaration_action(...)
→ call LM Studio
→ record proposal only
→ execute nothing
```

## E4.1 live controlled result — PASS

User-executed result:

```text
case: pydantic/pydantic#13432
comparison_basis: exact persisted E3 planner input + one trusted action
e3_replay_sha256: d2a1cf7455571402b8b82633b2e951473159b857194a76f853ed808adf25a179
github_acquisition_performed: False
support_drop_model_reexecuted: False
model: gemma-4-e4b-it-ud
elapsed_seconds: 6.425
expected_action_id_mentioned: True
capability_executed: False
```

Model proposal:

```text
The most useful next investigation step is to acquire the exact target Python declaration...

action_id: "acquire_exact_target_python_declaration"
```

Its explanation correctly connected:

```text
exact_target_python_declaration_established
→ unresolved
→ action directly acquires that missing evidence
→ required before declared_python_range_intersects_dropped_line can be resolved
```

No raw upstream changelog text was supplied to the planner.

## E4.1 finding — closed action context improves binding precision

The strongest evidence-backed interpretation is:

```text
E3 typed state only
→ correct conceptual next step

same exact E3 state
+ one trusted closed action descriptor
→ same reasoning direction
+ exact action_id binding
```

Therefore the closed action descriptor earned a concrete role:

```text
trusted action context
→ maps good planning reasoning onto a known executable capability identity
```

Do **not** over-credit it. E3 had already demonstrated the core S001 reasoning before the action catalog existed.

The action descriptor also supplied repository/revision/path and action metadata. If the model repeats those values later, that is consumption of trusted context, not independent discovery.

## E4.2 controlled JSON-Schema comparison — PASS

E4.2 replayed the exact persisted E4.1 `planner_input` and changed only the provider output contract by adding strict JSON Schema structured output.

No GitHub acquisition or support-drop-model rerun occurred.

User-executed result:

```text
case: pydantic/pydantic#13432
comparison_basis: exact persisted E4.1 planner input + JSON Schema only
e4_1_replay_sha256: 4f9c0fd9950b824b5c1ca8dd8e0959ffc9b024af1ae874fac4d60e3f80b7fdae
github_acquisition_performed: False
support_drop_model_reexecuted: False
model: gemma-4-e4b-it-ud
elapsed_seconds: 5.607
expected_action_id_selected: True
capability_executed: False
```

Exact structured model result:

```json
{
  "action_id": "acquire_exact_target_python_declaration",
  "explanation": "The planning question requires determining if the upstream Python 3.8 support drop affects the target project's exact declared Python range. The current state shows that 'exact_target_python_declaration_established' is unresolved due to insufficient evidence. Acquiring this declaration is the necessary next step to resolve this proposition and subsequently evaluate whether the dependency update impacts the target project's supported Python versions."
}
```

The JSON Schema deliberately did **not** enumerate the accepted action ID. It allowed `action_id` to be any non-empty string or `null`, so the correct action selection still came from the model consuming the trusted action catalog rather than being forced by the output schema.

## E4.2 finding — JSON Schema improves integration shape, not observed reasoning quality

The controlled comparison is:

```text
E4.1
same typed state + same trusted action descriptor
→ correct action in free-form text

E4.2
same exact planner input
+ strict JSON Schema only
→ same correct action
→ directly parseable {action_id, explanation}
```

Therefore E4.2 supports this bounded responsibility:

```text
JSON Schema
→ machine-readable field/type shape
→ deterministic parsing boundary
→ less output-format ambiguity for integration
```

E4.2 does **not** show that JSON Schema made the planner reason better. The reasoning direction and action selection were already correct in E4.1.

## Current evidence-backed responsibility separation

```text
typed proposition projection
→ planner reasoning input

closed trusted action descriptor
→ exact capability/action binding

JSON Schema
→ machine-readable shape / integration reliability

deterministic admission
→ candidate trusted-state revalidation / consequence containment
```

The first three now have direct evidence in the controlled S001 sequence. Deterministic admission remains the next responsibility to test on its own.

## What E4.1/E4.2 do not prove

They do not establish that:

- the model will select correctly across multiple available actions;
- one successful call proves repeatability;
- a closed action catalog is sufficient for all future planner seams;
- structured output prevents a semantically wrong but schema-valid action choice;
- deterministic admission is unnecessary;
- a model-selected action should be executed without fresh trusted-state revalidation.

## E4.3 — next discriminating control: deterministic admission

Do not call the model again merely to test admission.

Use the exact successful E4.2 parsed result as the untrusted model proposal and reconstruct the exact trusted S001 snapshot/action state from the frozen planner input.

The observed happy-path check should answer:

```text
correct schema-valid E4.2 proposal
+ exact current trusted state
→ admitted read-only action?
```

Admission's responsibility is consequence containment, so one bounded counterfactual rejection is also justified without another model call. At minimum verify that an unknown/tampered action identity is rejected rather than executable. If a second counterfactual is useful, prefer a stale/non-actionable trusted proposition state because that tests fresh-state revalidation rather than output formatting.

Do not turn E4.3 into a generalized security suite. Reuse the existing `admit_agent_plan(...)` owner and preserve the distinction:

```text
model correctness
!=
action admission correctness
```
