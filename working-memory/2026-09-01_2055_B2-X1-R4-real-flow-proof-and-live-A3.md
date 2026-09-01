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

## 3. Step 4 — live A3 smoke prepared

Added:

```text
experiments/b2_x1_s001_real_flow_a3_smoke.py
```

Commit:

```text
c664fe66b1324cd17b0f15fc7c22fbc35b73fdcf
```

The new smoke intentionally does not reuse the historical Phase-4A hand-built development-case harness. Its path is the current architecture:

```text
real S001 product investigation
→ current composition seam
→ EvidenceGapPlannerContext
→ LocalEvidenceGapPlanner.decide(...)
→ EvidenceGapDecision OR typed invocation problem
→ if ACTION_SELECTED: current A2 admission only
→ no capability execution
```

The smoke records a semantic expectation for observation:

```text
ACTION_SELECTED
+ acquire_exact_target_python_declaration
```

because the real pre-target S001 state still has the exact target declaration proposition unresolved/insufficient and that action is currently offered. A semantically different but technically valid model decision remains evidence to inspect rather than an automatic transport/runtime failure.

## 4. Current next action

Pull the new smoke and run from repository root as a module:

```text
git pull --ff-only

env \
  -u GITHUB_TOKEN \
  -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY \
  -u http_proxy -u https_proxy -u all_proxy \
  python -m experiments.b2_x1_s001_real_flow_a3_smoke
```

Then inspect:

```text
provider/structured-output success or typed problem
decision kind
action ID
model explanation
basic expectation match
A2 admission result when action selected
LM Studio logs / finish reason / any truncation or template warning
```

**Current checkpoint:** Step 3 complete. Step 4 live A3 smoke is implemented but not yet executed.

**Procedure provenance:** `UP-SKILL:upgradepilot-learning-by-doing`, `UP-SKILL:upgradepilot-build-implement`, `UP-SKILL:upgradepilot-working-memory`
