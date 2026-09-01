# B2/X1 R4 — Real-Flow Proof and Live A3 Continuation

**Date/time:** 2026-09-01 20:55 Europe/Berlin  
**Session status:** ACTIVE  
**Primary responsibility/mode:** Learning-by-Doing / Build — R4 ordinary-Python real-flow proof and live A3 evidence  
**Primary plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Learning-depth owner:** `../plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`  
**Previous:** `2026-09-01_B2-X1-R4-ownership-reentry-and-next-route.md`

## 1. Session anchor

This record continues the earlier 2026-09-01 ownership/composition working memory after:

```text
Step 1 ownership closure
→ COMPLETE

Step 2 real-product composition seam
→ IMPLEMENTED / INSPECTED
```

Current route:

```text
Step 3 prove real product flow → A1 composition
→ Step 4 run live A3 planner on that real composed context
→ inspect provider/model evidence
→ close A3 LbD slice if evidence supports it
→ then enter A4 design/implementation discussion
```

The earlier architecture ideas about generalized proposition production and possible durable/database-backed investigation state remain preserved in the previous record and are intentionally deferred to the A4 design boundary.

## 2. Step 3 — COMPLETE

### Focused runtime proof

Local WSL focused run:

```text
python -m unittest discover \
  -s experiments/tests \
  -p 'test_b2_x1_evidence_gap_*.py' \
  -v

Ran 40 tests in 0.006s
OK
```

This includes current A1, A2, A3 mocked/provider-boundary tests plus the new real-state composition tests.

Observed proof:

```text
40/40 PASS
```

This establishes the focused contracts and the new composition seam under local Python execution. It does not by itself establish the real public S001 acquisition path or live planner-model behavior.

### Direct-script import failure and correction

First real-flow launch used:

```text
python experiments/b2_x1_s001_real_flow_composition_probe.py
```

and failed before product execution with:

```text
ModuleNotFoundError: No module named 'experiments'
```

Cause:

```text
file-path execution from experiments/
→ script directory becomes the import root
→ package-style `from experiments...` imports cannot resolve from repository root
```

This is the same class of failure already recorded during the earlier E3 experiment.

Correction:

```text
python -m experiments.b2_x1_s001_real_flow_composition_probe
```

The probe documentation was updated accordingly in commit:

```text
7d38b10f7dc904d5ad670ad8c99060bded80a2b4
```

No `sys.path` hack or folder relocation was added.

### Real S001 normal-product-flow proof

Process-local public GitHub isolation was used:

```text
env \
  -u GITHUB_TOKEN \
  -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY \
  -u http_proxy -u https_proxy -u all_proxy \
  python -m experiments.b2_x1_s001_real_flow_composition_probe
```

Observed output:

```text
case: pydantic/pydantic#13432
normal_product_path_used: True
new_a3_planner_invoked: False
expected_s001_transition_preserved: True
expected_product_propositions_preserved: True
expected_ci_witness_preserved: True
hidden_source_action_authority_absent_from_request: True
output: /tmp/upgradepilot-b2-x1-r4-s001-real-flow-composition.json
```

Therefore Step 3 establishes the intended real composition path:

```text
real public S001 evidence
→ investigate_public_pull_request(...)
→ product-owned DependencyVersionChange
→ product-owned Python-support PropositionAssessment state
→ product-owned CI consumption/reachability evidence
→ experiment composition seam
→ bounded EvidenceGapPlannerContext
→ A1 request projection
```

and confirms that repository/revision/path/command/action authority remains absent from the model-visible request.

### Existing semantic extractor observation

The real S001 product path invoked the already-adopted local support-drop semantic extractor before the new planner boundary.

LM Studio evidence showed:

```text
model: gemma-4-e4b-it-ud
structured support-drop extraction request
candidate: Python 3.8 support drop introduced in Soup Sieve 2.8
finish_reason: stop
no truncation
```

This was the existing product semantic-extraction responsibility, not A3 planner inference.

LM Studio also emitted:

```text
detected an outdated gemma4 chat template, applying compatibility workarounds
```

Current classification: observational warning, not a blocker. The request completed successfully and produced the expected bounded candidate. Revisit only if later planner behavior/structured-output reliability gives evidence that the template materially affects the current responsibility.

## 3. Step 4 — live A3 smoke — COMPLETE / PASS

Added:

```text
experiments/b2_x1_s001_real_flow_a3_smoke.py
```

Commit:

```text
c664fe66b1324cd17b0f15fc7c22fbc35b73fdcf
```

The smoke intentionally does not reuse the historical Phase-4A hand-built development-case harness. Its path is the current architecture:

```text
real S001 product investigation
→ current composition seam
→ EvidenceGapPlannerContext
→ LocalEvidenceGapPlanner.decide(...)
→ EvidenceGapDecision OR typed invocation problem
→ if ACTION_SELECTED: current A2 admission only
→ no capability execution
```

### Observed terminal result

```text
case: pydantic/pydantic#13432
model: gemma-4-e4b-it-ud
outcome: decision
elapsed_seconds: 5.909
decision_kind: ACTION_SELECTED
action_id: acquire_exact_target_python_declaration
explanation: The planning question requires determining if the upstream Python support drop intersects the target declaration. The proposition 'exact_target_python_declaration_established' is currently unresolved, and this action directly targets acquiring that necessary evidence.
basic_expectation_match: True
admission_kind: admitted_action
admission_action_id: acquire_exact_target_python_declaration
capability_executed: False
output: /tmp/upgradepilot-b2-x1-r4-s001-real-flow-a3-smoke.json
```

### Provider/model evidence

LM Studio logs independently confirmed two sequential local model calls:

```text
1. existing product support-drop semantic extractor
2. current EvidenceGapPlanner A3 request
```

The second request used:

```text
model: gemma-4-e4b-it-ud
schema: upgradepilot_evidence_gap_decision_v1
prompt tokens: 695
completion tokens: 419
reasoning tokens: 324
finish_reason: stop
truncated: false
```

Returned structured decision:

```json
{
  "decision_kind": "ACTION_SELECTED",
  "action_id": "acquire_exact_target_python_declaration",
  "explanation": "The planning question requires determining if the upstream Python support drop intersects the target declaration. The proposition 'exact_target_python_declaration_established' is currently unresolved, and this action directly targets acquiring that necessary evidence."
}
```

The model reasoning aligned with the bounded state:

```text
upstream support drop → already established
exact target Python declaration → unresolved
range intersection → unresolved and dependent on target declaration
one current allowed action → acquire exact target declaration
```

A2 then rebound the selected ID to trusted hidden action authority and admitted it against current deterministic state. The smoke deliberately stopped before capability execution.

### A3 closure judgment

Current A3 evidence is sufficient to close the first real ordinary-Python request/response slice:

```text
real product state
→ bounded composition
→ A1 projection
→ live local A3 structured-output inference
→ technically valid EvidenceGapDecision
→ semantically expected first decision
→ A2 deterministic admission
→ no capability execution
```

This establishes the first real live A3 seam for S001. It does **not** establish general planner quality, production reliability, multi-case generality, execution/update correctness, persistence design, or framework adoption value.

### Gemma template warning

The same LM Studio warning appeared on both semantic-extractor and planner calls:

```text
detected an outdated gemma4 chat template, applying compatibility workarounds
```

Current classification remains **observational / non-blocking** because both strict structured-output calls completed correctly with `finish_reason=stop` and no truncation. Do not change model/template deployment solely because of this warning; reopen only if real behavior/reliability evidence makes it material.

## 4. A4 entry — CURRENT CHECKPOINT

The learning-depth owner defines A4 as:

```text
no-tool/action transition
→ execution/update seam
→ trace/replay
```

and introduces these responsibilities when materially used:

```text
state machine / transition model
planner state vs execution state
budget decrement timing
consumed-action update timing
immutable-state replacement/update patterns
execution result → domain interpretation → trusted state update
trace/event record design
replay and deterministic comparison
operational failure vs domain/evidence result
```

Before implementing A4, explicitly revisit the two architecture questions surfaced during ownership learning:

1. **proposition production/generalization** — how domain owners should produce reusable proposition state across different investigation responsibilities without making the planner/composition layer a second truth owner;
2. **state durability/persistence** — what investigation state actually needs durable storage for transition history/replay/resume, and whether the current experiment only needs an in-memory trace first.

Do not jump directly to a database, event-sourcing architecture, generic rule engine, LangGraph, or large orchestration loop. The R4 learning-depth owner explicitly defers full workflow persistence/event sourcing until replay/checkpoint requirements become durable product responsibilities.

## 5. Current route

```text
A3 live real-flow slice → COMPLETE / PASS
→ A4 pre-implementation design: define minimal state + transition ownership
→ revisit proposition-production and persistence questions against that concrete A4 need
→ choose smallest ordinary-Python execution/update/trace seam
→ implement/prove A4 incrementally
→ ordinary-Python reference/control closure when coherent
→ R4-B LangGraph comparison
→ R4-C bounded LangChain slice
→ R4-D comparison
```

**Current checkpoint:** Step 4 live A3 is complete and closed for the first S001 real-flow slice. Next is A4 design before implementation; no capability execution has yet been added to the planner experiment.

**Procedure provenance:** `UP-SKILL:upgradepilot-learning-by-doing`, `UP-SKILL:upgradepilot-build-implement`, `UP-SKILL:upgradepilot-working-memory`
