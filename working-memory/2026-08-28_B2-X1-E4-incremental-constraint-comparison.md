# B2/X1 E4 — Incremental Constraint Comparison

**Date:** 2026-08-28  
**Status:** ACTIVE — E4.1 COMPLETE; E4.2 JSON-SCHEMA COMPARISON NEXT  
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

## What E4.1 does not prove

E4.1 does not establish that:

- the model will select correctly across multiple available actions;
- a closed action catalog is sufficient for all future planner seams;
- free-form text is integration-safe;
- JSON Schema is unnecessary;
- deterministic admission is unnecessary;
- a model-selected action should be executed without revalidation;
- one successful call proves repeatability.

It establishes only the bounded S001 comparison above.

## Responsibility separation emerging from E3/E4.1

Current evidence supports separating three mechanisms rather than treating them as one monolithic "guardrail" stack:

```text
typed proposition projection
→ planner reasoning input

closed trusted action descriptor
→ exact capability/action binding

JSON Schema
→ candidate machine-readable shape / integration reliability

deterministic admission
→ candidate trusted-state revalidation / consequence containment
```

The last two remain hypotheses until tested for their own responsibilities.

## E4.2 — next discriminating control

Keep the exact successful E4.1 replay input and closed action descriptor fixed. Add only provider structured output using a minimal JSON Schema.

Do not add deterministic admission yet.

The schema should require only the machine-readable equivalent of the E4.1 answer, for example:

```text
action_id: string | null
explanation: non-empty string
```

Question:

```text
same exact E4.1 planning state + same closed action
+ JSON Schema
→ does the decision remain correct?
→ does the provider return directly machine-readable output?
→ what integration ambiguity disappears?
```

If E4.2 succeeds, credit JSON Schema only for the shape/parseability it actually provides. Do not claim it improved planner reasoning unless the behavior comparison demonstrates that.
