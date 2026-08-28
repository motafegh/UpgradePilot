# B2/X1 E4 — Incremental Constraint Comparison

**Date:** 2026-08-28  
**Status:** ACTIVE — E4.1 CONTROLLED REPLAY READY; MODEL RESULT PENDING  
**Parent exploration:** `working-memory/2026-08-28_B2-X1-evidence-first-llm-risk-and-design-exploration.md`

## Purpose

E4 tests candidate planner controls one at a time, starting from the successful E3 minimally constrained S001 planner behavior.

The immediate question is deliberately narrow:

```text
same exact E3 typed S001 state
+ one trusted closed action descriptor
→ does the model bind its already-correct conceptual reasoning to the exact action_id?
```

E4.1 does not yet add JSON Schema, deterministic admission, extra hard-constraint prompting, or capability execution.

## E3 control result

The successful E3 run showed that `gemma-4-e4b-it-ud`, given the real typed pre-investigation S001 propositions and bounded planning question, naturally proposed acquiring the exact target Python declaration.

The model correctly followed the dependency:

```text
upstream support drop established
→ exact target declaration unresolved / insufficient
→ range intersection depends on that missing declaration
→ acquire target declaration next
```

It did not receive a closed action catalog, JSON Schema, deterministic admission, or raw upstream changelog prose.

The persisted local E3 evidence owner is:

```text
/tmp/upgradepilot-b2-x1-e3-minimal-s001-planner.json
```

## Initial E4.1 design mistake discovered during execution

The first E4.1 implementation reacquired the entire real S001 normal product path before asking the planner again.

That introduced unrelated live dependencies into a comparison whose intended independent variable was only closed action binding:

```text
GitHub REST acquisition
+ current public API rate state
+ provider/source acquisition
+ support-drop semantic model rerun
+ deterministic grounding rerun
+ state reconstruction
+ closed action descriptor
```

Observed attempts failed before a valid E4 planner comparison:

1. one run reached the normal product path but did not retain the expected pre-investigation assessment;
2. a diagnostic revision was prepared to preserve the upstream support-drop prerequisite state;
3. the next run stopped even earlier because unauthenticated public GitHub acquisition returned `forbidden_or_rate_limited` at the first pull-request request.

Neither failure is an E4 planner result.

## Methodological correction

A valid incremental-control comparison should keep the control state fixed.

Therefore E4.1 now replays the exact successful persisted E3 planner input instead of reacquiring S001.

Current flow:

```text
persisted successful E3 JSON
→ validate experiment kind and no-action/no-schema/no-admission/raw-text boundary facts
→ validate exact S001 repository / PR / head revision / step budget
→ validate deterministic baseline action identity
→ retain the exact E3 planning question + propositions
→ add exactly one trusted action descriptor using build_target_python_declaration_action(...)
→ call LM Studio
→ record natural-language output only
→ execute nothing
```

The output also records the SHA-256 fingerprint of the exact E3 evidence file used as the replay source.

## Why this is the stronger experiment

The corrected comparison isolates the intended variable:

```text
E3
= typed state

E4.1
= same typed state
+ one closed trusted action descriptor
```

It explicitly removes these confounders from E4.1:

```text
GitHub acquisition performed: false
support-drop model reexecuted: false
JSON Schema supplied: false
deterministic admission applied: false
capability executed: false
raw upstream text supplied to planner: false
```

This is not merely a workaround for rate limiting. It is a better experimental design.

## Interpretation rule for the pending E4.1 result

If the model names:

```text
acquire_exact_target_python_declaration
```

and correctly explains why the action discriminates the unresolved target-declaration/range-intersection state, then E4.1 supports:

```text
closed trusted action context
→ useful exact action binding
```

It does **not** establish that JSON Schema or deterministic admission are unnecessary. Their responsibilities remain separate candidates:

```text
JSON Schema
→ machine-readable shape / integration reliability

deterministic admission
→ trusted-state/action revalidation and consequence containment
```

If the model still fails to select/name the action despite the descriptor, inspect that specific behavior before adding another control.

## Current next step

Execute the corrected E4.1 replay once against the local adopted model. Do not reacquire S001 merely to run this comparison.
