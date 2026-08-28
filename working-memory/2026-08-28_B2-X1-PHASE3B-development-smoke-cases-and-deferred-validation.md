# B2/X1 Phase 3B — Development Smoke Cases and Deferred Local Validation

**Date:** 2026-08-28  
**Status:** IMPLEMENTED — LOCAL EXECUTION VALIDATION DEFERRED BY CURRENT ENVIRONMENT ACCESS  
**Owning plan:** `../plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`  
**Accepted protocol:** `../plans/B2_X1_PHASE3_EVALUATION_PROTOCOL.md` (`b2-x1-phase3a-v2`)

## 1. Why this slice continued without WSL execution

Ali temporarily does not have access to the normal project system/WSL environment and explicitly
requested that Learning-by-Doing/Building continue through real implementation, with local command
execution/testing batched for the later point when system access is available.

This does **not** convert unexecuted code into PASS evidence.

Current evidence rule:

```text
GitHub source/diff inspection
→ implementation existence / bounded repository impact evidence

later WSL execution
→ runtime/import/test/compile evidence

later LM Studio run
→ actual local-model behavior evidence
```

Until those later gates execute, runtime/model claims remain pending.

## 2. Bounded responsibility implemented

The calibrated X1 route requires a minimum development pair before the first local planner smoke:

```text
d-a1-smoke
→ minimal choose_action case

d-s004-stop
→ contrasting real no-tool STOP case
```

The accepted protocol already froze both cases, so this slice did not redesign their semantics.

### `d-a1-smoke`

```text
example/project#7@bbbb...bbbb
exact_target_python_declaration_established
→ unresolved / insufficient
A1 available
remaining_steps = 1
expected development result = choose_action → A1
```

This intentionally simple synthetic case isolates the smallest action-selection interaction. It
is development/calibration evidence only and cannot support final planner-quality claims.

### `d-s004-stop`

```text
googlefonts/glyphsLib#1145@f3cda8a94600e58d27f1bc17c99b7693718b6350
four decision-critical authority facts established
contradiction_or_gap_present → refuted / sufficient
no action
remaining_steps = 1
expected development result = stop
```

This is the real S004 stopping control. It establishes the important contrast that unused step
budget is not itself a reason to continue investigating.

## 3. Small source-clarity correction

The first harness slice used evaluator types named:

```text
ProtectedDecisionOracle
ProtectedPlannerCase
```

Once the same renderer began serving development cases, those names became misleading. The
experiment-owned names were generalized to:

```text
PlannerDecisionOracle
PlannerEvaluationCase
```

No hierarchy/framework was introduced. One neutral envelope now serves both development and
protected decisions, while partition membership remains evaluator-only metadata that is not
serialized into planner input.

`PlannerDecisionOracle.baseline_relationship` is optional because protected scoring needs that
field while development smoke cases do not perform final baseline comparison.

## 4. Files changed

```text
experiments/b2_x1_phase3b_harness.py
experiments/tests/test_b2_x1_phase3b_harness.py
```

Implementation commits:

```text
536ff38aef16dd41c52773dfbe3450dd91668d74
→ add development case builders + neutral evaluator names

f79dd6aa99ddb3c73ad4eece96bd24416251389a
→ add focused development-case tests
```

GitHub range inspection from calibrated-plan tip `6c47cbf...` to `f79dd6a...` shows exactly
those two experiment files changed. No `src/upgradepilot`, accepted protocol, product test,
provider, target repository, or model integration changed.

## 5. Focused tests added but not yet executed locally

The test module now also protects:

1. exact `d-a1-smoke` identity/proposition/action/oracle construction;
2. exact real `d-s004-stop` identity/proposition/no-action/oracle construction;
3. the same oracle-isolating request renderer for both development cases.

These tests are committed implementation, **not runtime PASS evidence** until executed in the
normal WSL environment.

## 6. Current continuation under unavailable local system

The calibrated route remains:

```text
Phase 3B-1 minimum model-ready boundary
→ early development-only local-model smoke
→ only if viable, complete protected-scoring machinery
```

Because local execution/model access is temporarily unavailable, continue only implementation
that is required before that early smoke and is useful regardless of the candidate model result.
Do not compensate by building the entire protected scoring system.

Next likely bounded build responsibility:

```text
reuse/inspect existing local LM Studio HTTP transport
→ implement the minimum development planner runner around:
   render request
   → local structured-output call
   → strict AgentPlanResult parsing
   → deterministic admit_agent_plan(...)
→ keep actual network/model execution deferred until local system access returns
```

Before that implementation, inspect existing ADR-0006/local HTTP experiment code and
`ENVIRONMENT.md` so the planner path reuses the accepted loopback/no-proxy method rather than
creating a second transport.

## 7. Deferred final validation bundle

When Ali regains system access, run the accumulated focused deterministic checks before treating
Phase 3B-1 as passed, then perform the small development-only LM Studio smoke. The exact command
bundle should be derived from the final touched files at that point rather than frozen prematurely
here.

A later PASS may establish deterministic harness/runtime readiness. It still cannot establish
planner value until actual model outputs are inspected.