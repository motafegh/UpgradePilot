# B2/X1 Phase 3B — Development Smoke Cases and Deferred Local Validation

**Date:** 2026-08-28  
**Status:** MODEL-READY DEVELOPMENT PATH IMPLEMENTED — BUILD PAUSED FOR LEARNING-ONLY MASTERY REVIEW; LOCAL EXECUTION / LM STUDIO EVIDENCE DEFERRED BY CURRENT ENVIRONMENT ACCESS  
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

## 2. Development cases implemented

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

## 4. Minimum local planner smoke runner prepared

Existing local-model evidence was inspected before adding another transport path:

```text
ENVIRONMENT.md
→ WSL control plane
→ LM Studio on Windows
→ 127.0.0.1:12345
→ /v1/chat/completions
→ ambient-proxy caveat

tools/run_step6c_support_drop_smoke.py
→ removes HTTP_PROXY / HTTPS_PROXY / ALL_PROXY + lowercase equivalents
→ sets NO_PROXY / no_proxy = 127.0.0.1,localhost,::1
→ runs the child experiment without changing the user's global environment

experiments/step6_support_drop_smoke.py
→ already-proven project pattern for requests + LM Studio strict json_schema output
```

The planner path reuses that method rather than creating a provider framework.

### `experiments/b2_x1_phase4a_planner_smoke.py`

Prepared development-only flow:

```text
build development PlannerEvaluationCase
→ render_planner_request(...)
→ system task + trusted planning question/snapshot
→ strict LM Studio json_schema response_format
→ parse_structured_plan(...)
→ agent_plan_result_from_mapping(...)
→ admit_agent_plan(...)
→ development evidence record
```

Important boundaries:

- only `d-a1-smoke` and `d-s004-stop` are used;
- no protected scored case is used for prompt/model tuning;
- repository/revision/path remain pre-bound trusted state;
- no capability is actually executed by this smoke;
- semantic model errors remain observable development evidence rather than being hidden by retries;
- transport/response-shape failure remains distinct from a semantically wrong but observable model decision.

The prepared smoke uses exactly two development cases × two repetitions = **4 future calls**.
That is small enough for an early smoke while exposing obvious output instability.

### `tools/run_b2_x1_phase4a_planner_smoke.py`

A thin WSL runner reuses:

```python
from tools.run_step6c_support_drop_smoke import build_localhost_http_environment
```

so the already-tested proxy-isolation policy remains the single transport owner. No new proxy
abstraction or duplicated environment policy was introduced.

## 5. Offline-focused tests written but not executed

`experiments/tests/test_b2_x1_phase3b_harness.py` now protects:

1. exact `d-a1-smoke` identity/proposition/action/oracle construction;
2. exact real `d-s004-stop` identity/proposition/no-action/oracle construction;
3. the same oracle-isolating request renderer for both development cases.

`experiments/tests/test_b2_x1_phase4a_planner_smoke.py` adds offline tests for:

1. strict LM Studio payload construction and evaluator-metadata exclusion;
2. STOP payload with no allowed action despite remaining step budget;
3. strict structured `choose_action` parsing;
4. action-case deterministic admission using a mocked LM Studio envelope;
5. STOP-case deterministic no-tool admission using a mocked LM Studio envelope;
6. malformed LM Studio response rejection.

These are committed implementation, **not runtime PASS evidence** until executed in the normal
WSL environment.

## 6. Repository impact

Development-case commits:

```text
536ff38aef16dd41c52773dfbe3450dd91668d74
→ add development case builders + neutral evaluator names

f79dd6aa99ddb3c73ad4eece96bd24416251389a
→ add focused development-case tests
```

Prepared smoke commits:

```text
44b4d59109edc4f8ee3ad9824e310047f092bd34
→ add experiments/b2_x1_phase4a_planner_smoke.py

8a7bf850b9c50b147377853bb8b68c786db36b7f
→ add localhost-safe tool wrapper

079951bd8308cded71663ee7585788b91d3489a5
→ add offline planner-smoke tests
```

GitHub range inspection from calibrated-plan tip `6c47cbf...` through `079951b...` shows only:

```text
experiments/b2_x1_phase3b_harness.py
experiments/b2_x1_phase4a_planner_smoke.py
experiments/tests/test_b2_x1_phase3b_harness.py
experiments/tests/test_b2_x1_phase4a_planner_smoke.py
tools/run_b2_x1_phase4a_planner_smoke.py
this working-memory record
```

No `src/upgradepilot`, accepted protocol, product test, target repository, agent framework, or
product integration changed.

## 7. Current continuation under unavailable local system

The calibrated route remains:

```text
Phase 3B-1 minimum model-ready boundary
→ early development-only local-model smoke
→ only if viable, complete protected-scoring machinery
```

The code needed to reach the development smoke is now prepared. The next **discriminating** event
is execution in the real WSL/LM Studio environment.

Because that environment is temporarily unavailable, do not compensate by building the entire
protected scoring system. Further pre-smoke implementation would be speculative rather than
required by an observed model/harness result.

Use the waiting period for post-implementation Learning-by-Doing explanation/review of the code,
request shape, parser/admission flow, and transport boundary if useful. Resume implementation
only if another responsibility is independently required regardless of smoke outcome.

## 8. Deferred validation and live smoke

When Ali regains system access:

1. synchronize the checkout to the then-current `main`;
2. run the accumulated focused Phase-2/Phase-3B/Phase-4A offline tests + compile checks;
3. inspect failures and repair before any live model conclusion;
4. refresh LM Studio model inventory/readiness only as needed;
5. execute `tools/run_b2_x1_phase4a_planner_smoke.py`;
6. inspect the 4 development decisions as untrusted model evidence.

The exact command bundle should be derived from the final touched files at that point rather than
frozen prematurely here.

A later deterministic PASS can establish harness/runtime readiness. The live smoke can establish
only development model behavior. Neither alone establishes protected planner value or product
adoption.

## 9. Current Learning-Only mastery pause and AI/LLM engineering lens

Ali explicitly paused building at this model-ready point to **review, recall, relearn, and master**
the material already implemented before continuing. Product/experiment implementation therefore
stays paused until Ali explicitly resumes building.

The review must cover both:

```text
UPGRADEPILOT-SPECIFIC MECHANISM
→ exact code / contracts / cases / evidence / data flow

BROADER AI/LLM ENGINEERING CONCEPT
→ common name
→ why it exists
→ where the same idea appears in our real implementation
→ failure/trade-off
→ depth needed now vs later
```

Do not teach only project-local names when a reusable AI-engineering concept is present.

### 9.1 Direct concepts already encountered and worth mastering

The current implementation already gives real exposure to:

```text
PropositionAssessment / InvestigationSnapshot
→ typed agent state, epistemic state, uncertainty/evidence representation

AllowedInvestigationAction
→ closed action space, tool/action schema, pre-bound tool authority

AgentPlanResult + JSON Schema
→ structured outputs, model output contracts

agent_plan_result_from_mapping(...)
→ strict parsing / contract validation

admit_agent_plan(...)
→ deterministic guardrails, policy enforcement, least authority

PlannerEvaluationCase + PlannerDecisionOracle
→ eval-case design, oracle/ground truth, evaluator-owned metadata

render_planner_request(...)
→ context engineering, request projection, information minimization

case_key exclusion
→ label/oracle leakage prevention

development vs protected cases
→ calibration/eval separation, contamination/overfitting control

Phase-3B/4A machinery
→ evaluation harness, smoke evaluation, capability probing

S001 replay design
→ deterministic replay/state transition around nondeterministic model decisions

LM Studio /v1/chat/completions
→ local inference runtime, inference API/client boundary

system + user messages
→ prompt architecture / role separation

temperature + seed + repeated calls
→ sampling configuration, nondeterminism, repeated evaluation

raw outputs + admission/result records
→ tracing, observability, failure taxonomy

localhost proxy isolation
→ local inference transport/security boundary

untrusted_evidence_notes
→ prompt-injection/untrusted-data boundary
```

These should be learned through the real source/tests/evidence, not as detached definitions.

### 9.2 Adjacent high-value exposure

When materially connected to the current code, provide concise exposure to concepts such as:

- hooks / lifecycle callbacks;
- middleware/interceptors;
- function calling / tool calling;
- agent loops and state machines;
- checkpoints;
- model routing/fallbacks;
- semantic retries;
- prompt/config versioning;
- caching;
- LLM-as-a-judge;
- MCP;
- RAG;
- agent frameworks and observability platforms.

The rule is **exposure without technology-demo engineering**. Explain the concept and its relation
when useful; implement it only if a real UpgradePilot responsibility or observed failure later
requires it.

### 9.3 Learning depth for this review

Use three practical classes:

```text
MUST MASTER / DIRECTLY USED
→ Ali should be able to reconstruct the flow, explain why the mechanism exists,
  interpret its focused tests/evidence, and diagnose a representative failure

UNDERSTAND OPERATIONALLY / ADJACENT
→ Ali should recognize the concept, purpose, relationship, and when it becomes useful
  without reproducing its internals

DEFERRED
→ real but not currently responsibility-unlocking; acknowledge and return to the active route
```

Initial mastery route for the current pause:

```text
1. proposition/evidence state foundation
2. InvestigationSnapshot + AllowedInvestigationAction + AgentPlanResult
3. schema validity vs deterministic semantic admission
4. choose_action / stop / defer / unresolved and bounded autonomy
5. planning_question + snapshot + oracle + development/protected partition
6. real S001 end-to-end evidence-gap/action reasoning
7. Phase-3B evaluation harness + request projection + leakage prevention
8. development smoke cases and capability probing
9. LM Studio inference payload/response/parser/admission flow
10. transport, tracing, tests, reproducibility, and failure classification
11. end-to-end reconstruction + critique before build resumes
```

This route is adaptive. Expand a chunk when it exposes a real prerequisite or high-value AI/LLM
engineering concept; compress familiar/repeated material. Do not turn the mastery pause into a
generic AI course or require perfect memorization before resuming the project.