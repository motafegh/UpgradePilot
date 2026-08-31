# B2/X1 EvidenceGapPlanner R4-A3 — local model request/response seam

**Date:** 2026-08-31  
**Mode:** Learning-by-Doing / Build  
**Scope:** experiment-owned ordinary-Python reference/control  
**Product runtime integration:** not authorized

## 1. Re-anchor after governance update

Before continuing R4-A3, current `main` governance/Skill updates were re-read proportionately:

- `AGENTS.md`
- `.agents/skills/upgradepilot-build-implement/SKILL.md`
- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`
- relevant `OPERATING_GUIDE.md` sections
- `ENVIRONMENT.md` because local LM Studio/runtime topology is now material
- `SECURITY.md` because local inference transport and untrusted model output are now material
- ADR-0006 because it owns the existing accepted direct-LM-Studio structured-output method used as a technical precedent
- Build Source Clarity heuristics because the new provider module is a non-trivial cross-file/model boundary

The governance update reinforced rather than changed the selected route: keep one smallest substantive Build responsibility, load conditional owners when their boundary becomes material, use focused tests as explicit proof propositions, preserve transport/security distinctions, and close the Learning-by-Doing loop after actual evidence.

## 2. Slice contract

### Build target

Implement only the planner-specific local model invocation seam:

```text
EvidenceGapPlannerContext
→ existing explicit model-visible projection
→ one LM Studio OpenAI-compatible structured-output request
→ provider envelope validation
→ strict EvidenceGapDecision parser
→ EvidenceGapDecision
   OR EvidenceGapModelInvocationProblem
```

Do not add admission, capability execution, state update, multi-turn orchestration, LangGraph, or LangChain in this increment.

### Learning target

Material concepts introduced by the actual code:

```text
Mapping[str, Any] as a broad/untrusted response-envelope view
runtime narrowing with isinstance
JSON serialization vs deserialization
HTTP/provider envelope vs model-owned message content
strict JSON Schema structured output
provider request failure vs HTTP failure vs malformed provider envelope
structured model-output invalidity vs semantic decision quality
completion truncation as a distinct provider/model-call outcome
bounded timeout and no automatic retry
loopback HTTP with requests.Session.trust_env = False
prompt/context engineering at the exact EvidenceGapPlanner responsibility
```

Deeper requests internals, generic provider abstractions, retry/backoff frameworks, advanced JSON Schema, async/concurrency, and prompt-optimization frameworks remain deferred behind the active learning-depth map triggers.

## 3. Existing technical precedent reused conceptually

`src/upgradepilot/upstream/support_drop_extractor.py` already establishes a product-owned precedent for:

```text
requests
→ LM Studio localhost /v1/chat/completions
→ strict json_schema response_format
→ temperature 0 / seed 0
→ stream false
→ bounded timeout
→ no automatic retry
→ Session.trust_env = False
→ provider envelope validation
→ inner structured-output parsing
```

ADR-0006 accepts that method only for the bounded support-drop product role. R4-A3 therefore reuses the already-deployed model and transport pattern for an experiment without extending ADR-0006's planner/product adoption authority.

A new generic product provider abstraction was deliberately not created because product integration is not authorized and the current experiment does not yet justify that ownership expansion.

## 4. Executable changes

New source:

`experiments/b2_x1_evidence_gap_model.py`

New focused tests:

`experiments/tests/test_b2_x1_evidence_gap_model.py`

Commits:

```text
initial source
6db4b183a50aa9d427b396961576110873ccf3ce

initial tests
f7e0a9d8de333677305564f0b9031cdf68cab78d

separate provider-envelope vs structured-output failure ownership
2121953f09c7e1d217c42d4d2c727b9265cb78b4

align focused tests
21929c55b8a22ed70635191217e1c5b25c2a19e2

clarify model-invocation problem vocabulary
8f3bd9b46cd451a84429d6dfcafa50a9f8088c57

align tests with final invocation vocabulary
9d1f02f5b4b17e07af772b29924613114a23e350
```

## 5. New model invocation boundary

### `LocalEvidenceGapPlanner`

Primary public experiment entry point:

```text
decide(EvidenceGapPlannerContext)
→ EvidenceGapModelInvocationResult
```

Result union:

```text
EvidenceGapDecision
OR
EvidenceGapModelInvocationProblem
```

A successful `EvidenceGapDecision` is still untrusted semantic planner output. It is not an admitted action and does not execute anything.

### `EvidenceGapModelInvocationProblem`

This name deliberately refers to failure of obtaining a usable structured planner decision through the model/provider invocation boundary. It does not mean the model made a semantically poor but otherwise valid decision.

Current reason vocabulary:

```text
provider_request_failed
provider_http_error
provider_response_malformed
completion_truncated
structured_output_invalid
```

Semantic planner quality remains a separate evaluation responsibility. Deterministic selected-action authorization remains R4-A2.

## 6. Request construction

The provider adapter does not rediscover the model-visible context. It calls:

`render_evidence_gap_planner_request(context)`

and serializes only its existing `context` projection into the user message.

The existing three-field schema is passed through LM Studio's strict JSON-Schema response format:

```text
decision_kind
action_id
explanation
```

Current experiment request settings:

```text
endpoint: http://127.0.0.1:12345/v1/chat/completions
model: gemma-4-e4b-it-ud
temperature: 0
seed: 0
max_tokens: 512
stream: false
timeout: 180 seconds
automatic retry: none
```

Using the already-deployed model here is an experiment choice, not an extension of ADR-0006's product adoption decision.

## 7. Transport/security boundary

The experiment creates a `requests.Session()` with:

```python
session.trust_env = False
```

so local inference does not silently inherit ambient HTTP(S) proxy settings. This follows the same accepted loopback security invariant already present in product support-drop inference and required by `SECURITY.md` / `ENVIRONMENT.md`.

No credentials, external tools, target mutation, or model tool calling are involved.

## 8. Failure-layer separation

The implementation now keeps these distinct:

```text
request raises / transport problem
→ provider_request_failed

non-2xx HTTP
→ provider_http_error

outer JSON / choices / message content envelope unusable
→ provider_response_malformed

provider finish_reason == length
→ completion_truncated

message content exists but inner JSON or EvidenceGapDecision contract is invalid
→ structured_output_invalid

valid EvidenceGapDecision but bad reasoning/choice
→ NOT an invocation problem; semantic evaluation responsibility

valid ACTION_SELECTED but stale/consumed/disallowed at T2
→ NOT an invocation problem; deterministic R4-A2 admission responsibility
```

This separation is a central R4-A3 learning/proof target.

## 9. Focused tests written

The mocked provider suite covers:

```text
exact localhost endpoint + timeout
model/temperature/seed/max_tokens/stream settings
strict three-field JSON Schema
bounded user context excludes hidden authority
valid ACTION_SELECTED response
valid no-tool response
request timeout and no automatic retry
non-2xx HTTP
malformed outer JSON
missing provider choice
missing message content
completion truncation
malformed inner JSON
cross-field-invalid EvidenceGapDecision
extra model authority field
loopback Session.trust_env == False
```

These tests are mocked at the HTTP boundary. They do not establish live LM Studio reachability, current model availability, model semantic quality, or end-to-end admission/execution behavior.

## 10. Current proof state

```text
R4-A3 source landed
→ YES

focused mocked tests landed
→ YES

post-write source/test inspection
→ YES

Source Clarity pass
→ YES

mocked focused runtime PASS
→ PENDING

live LM Studio/model behavior
→ NOT YET TESTED IN R4-A3
```

## 11. Next bounded gate

Run the existing combined focused family first:

```bash
python -m unittest discover \
  -s experiments/tests \
  -p 'test_b2_x1_evidence_gap_*.py' \
  -v
```

Expected test count after adding R4-A3: 36 tests (23 prior A1/A2 tests + 13 A3 tests).

If the mocked suite is green:

```text
mocked provider-adapter proof
→ close
→ build/run one minimal live LM Studio R4-A3 smoke
→ inspect actual provider/model decision
→ only then decide whether A3 needs repair or can close before R4-A4
```

If it fails, diagnose the smallest failing ownership layer before adding live inference.

## 12. Skill provenance

```text
UP-SKILL:upgradepilot-build-implement
UP-SKILL:upgradepilot-learning-by-doing
```
