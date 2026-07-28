# UpgradePilot Current Memory

**Last updated:** 2026-07-28  
**Authority:** Sole repository owner of live project position, selected plan, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. They must not duplicate this live state.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Completed evidence plan:** [`plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md`](plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md)
- **Selected decision plan:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md)
- **Selected local-model re-evaluation:** [`plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md`](plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md)
- **Deferred network-learning slice:** [`plans/B2_LM_STUDIO_NETWORK_BOUNDARY_LEARNING_PLAN.md`](plans/B2_LM_STUDIO_NETWORK_BOUNDARY_LEARNING_PLAN.md)
- **First observed-load record:** [`working-memory/2026-07-28_B2-first-observed-gemma-e4b-load-and-smoke.md`](working-memory/2026-07-28_B2-first-observed-gemma-e4b-load-and-smoke.md)

B2 Increment D — minimum package and upstream evidence — is complete. B2 Increment E — transparent decision — remains selected. Ali approved a bounded local-LLM experiment direction, not automatic model adoption.

The environment inventory, model metadata, candidate comparison, and low-confidence memory estimates are complete enough to select the first observed deployment. The immediate blocker is now:

```text
explicit Gemma E4B load
→ actual applied load configuration
→ real post-load GPU state
→ one strict JSON-Schema smoke request
→ classified result
```

No semantic interpretation method, decision contract, recommendation policy, active model/provider dependency, or recommendation code has been adopted or implemented.

## Relevant revisions

```text
last behavior-validated product revision in Ali's environment:
bc5aafece111802f1e777dd2b8151ccad1fd822e

CLI integration closure:
4ff281565593f5e74f5f79491497c9b36363050f

transparent-decision plan:
2a6664f4fae17583afdfcdd59889f5fa3cd0ef06

local-LLM re-evaluation plan:
010f667293d6acdfc71841200737a5b1c7e3dfc7

LM Studio server and Instructor assessment:
c4dcbb403b81014c4753e6c27dba124f539f4283

model inventory shortlist:
ce02cbcad7abcfb5c274c216e96eee98ae88d6f2

network-boundary learning plan:
4be40bb5fcf37102ec48e891ebf313a858baa06c

model metadata/networking correction:
3bfc1fbb57dce2d0fcae734b403ac4bb57ecea35

Gemma E4B estimate record:
8b01e538c20580ad5c17ff17afd67e01b87cf22e

first observed-load procedure:
41f88d26ba8237dfd9aaded29cf78540728a76f9
```

## Behavior-validated product boundary

Observed previously in Ali's WSL2 Python 3.12 environment:

```text
Ran 64 tests in 0.021s
OK
```

Validated public path:

```text
public repository + Dependabot PR
→ exact PR identity and complete changed files
→ one supported exact pinned Python dependency update
→ exact-head workflow/job/step evidence
→ bounded CI-authority classification
→ exact PyPI package/version/file identity
→ PyPI-reported file provenance
→ matching GitHub upstream repository
→ exact published release and tag reference
→ bounded release body
→ concise CLI evidence report
→ unresolved_claim
```

Validated S004 control evidence includes:

```text
repository: googlefonts/glyphsLib
PR: 1145
pytest: 9.0.2 → 9.0.3
CI authority: sufficient
published package: pytest==9.0.3
upstream repository: pytest-dev/pytest
provenance coverage: 2/2 files
accepted tag: 9.0.3
claim state: unresolved_claim
```

Permitted claim:

> UpgradePilot behavior-validly connects exact PR and dependency identity, bounded exact-head CI authority, exact PyPI release/file identity, PyPI-reported publisher provenance, matching upstream repository identity, and an exact GitHub Release/tag reference.

Not established:

- complete CI coverage;
- release-prose meaning;
- target-repository compatibility or objective safety;
- evidence sufficiency or stopping;
- merge, targeted-check, investigate/block, defer, or abstain action.

## Decision-method design progress

Recorded design evidence now includes:

- complete S004 evidence-role walkthrough;
- decision-evidence map;
- first typed decision input/output contract draft;
- action and readiness vocabulary drafts;
- stopping-rule draft;
- four upstream claim categories:
  - `fix_or_remediation`;
  - `compatibility_assurance`;
  - `interface_or_behavior_change`;
  - `support_boundary_change`;
- semantic states:
  - `resolved`;
  - `no_decision_relevant_claim`;
  - `unresolved`;
  - `conflicting`;
- source-span grounding and deterministic authority limits;
- local bounded structured extraction as the selected experiment direction;
- deterministic sufficiency, stopping, and maintainer action remaining outside model control.

These remain proposals until the method and deployment earn approval through controlled evidence.

## Local LM Studio evidence

Established:

```text
LM Studio CLI commit: 71bd99c
server running: true
port: 12345
JIT loading: active
WSL2 localhost reachability: successful
Python: 3.12.3
venv executable: /home/motafeq/projects/UpgradePilot/.venv/bin/python3
GPU: RTX 3070 Laptop, 8192 MiB
pre-load used VRAM: 1435 MiB
pre-load free VRAM: 6584 MiB
loaded instances at inventory capture: none
```

Candidate metadata:

```text
gemma-4-e4b-it-ud
7.5B, Q4_K_XL, ~4.751 GiB weights

qwen3.5-9b-ud
9B, Q4_K_XL, ~5.556 GiB weights

gemma-4-12b-it-qat
12B, Q4_0, ~6.497 GiB weights
```

Low-confidence LM Studio estimates:

```text
Gemma E4B: 4K/8K, full GPU → 4.75 GiB
Qwen 9B: 4K/8K, full GPU → 5.56 GiB
Gemma 12B: 4K/8K, full GPU → 6.50 GiB
Gemma 12B: 4K, 75% GPU → 6.50 GiB
```

Because context and offload changes did not materially change the estimates, they are treated as weight-dominated sizing hints rather than observed deployment proof.

## First observed deployment selected

```text
model: gemma-4-e4b-it-ud
context length: 4096
transport for load control: POST /api/v1/models/load
flash attention requested: true
KV cache GPU offload requested: true
echo final load config: true
semantic endpoint: POST /v1/chat/completions
parallel target: 1
speculative decoding: off
```

Why Gemma E4B first:

- best measured hardware headroom;
- materially stronger than the rejected Gemma E2B deployment;
- adequate context for the first bounded source;
- cleanest control for distinguishing runtime failure from semantic failure.

This selects the first control only. It does not select the final model.

## Exact continuation

Follow [`working-memory/2026-07-28_B2-first-observed-gemma-e4b-load-and-smoke.md`](working-memory/2026-07-28_B2-first-observed-gemma-e4b-load-and-smoke.md):

1. pull the latest repository revision;
2. explicitly load `gemma-4-e4b-it-ud` at 4096 context through the native LM Studio load endpoint with `echo_load_config=true`;
3. preserve `instance_id`, load time, final context, evaluation batch, Flash Attention state, and KV-cache placement;
4. capture `lms ps --json`, native `/api/v1/models`, and `nvidia-smi` immediately after loading;
5. send one non-streaming strict JSON-Schema smoke request through `/v1/chat/completions`;
6. preserve the complete outer response, inner JSON string, finish reason, token statistics, latency, model logs, and post-inference GPU state;
7. classify any failure by load, guardrail, GPU OOM, transport, authentication, schema, parsing, grounding, semantics, truncation, or runtime stability;
8. unload the exact instance and verify restoration;
9. review the control result before installing Instructor, loading Qwen, testing the 12B model, broad semantic scoring, or changing network exposure;
10. after one initial scored semantic result exists, activate the separate network-boundary learning plan;
11. do not begin Increment F until the transparent decision boundary is behavior-validated.

## Product and experiment boundaries

Do not yet:

- produce maintainer recommendations;
- treat JSON Schema, Pydantic, Instructor, source quotation, or one successful smoke case as semantic correctness;
- restore archived M2 source or dependencies;
- install Instructor/Pydantic/OpenAI dependencies before adapter comparison is authorized by the smoke result;
- rely on JIT defaults for scored deployments;
- load multiple candidate models concurrently;
- download another model without a named evidence gap and Ali's approval;
- infer safety from absence of an extracted warning;
- let a model select authority, sufficiency, stopping, or action;
- enable CORS or expose LM Studio beyond localhost before the network-boundary learning slice reviews bind, firewall, authentication, and restoration;
- mutate target repositories or require private access.

## Detailed dated evidence

- [`working-memory/2026-07-28_B2-transparent-decision-method.md`](working-memory/2026-07-28_B2-transparent-decision-method.md)
- [`working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md`](working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md)
- [`working-memory/2026-07-28_B2-upstream-semantic-boundary.md`](working-memory/2026-07-28_B2-upstream-semantic-boundary.md)
- [`working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md`](working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md)
- [`working-memory/2026-07-28_B2-lm-studio-server-and-instructor-assessment.md`](working-memory/2026-07-28_B2-lm-studio-server-and-instructor-assessment.md)
- [`working-memory/2026-07-28_B2-model-metadata-and-networking-sequencing-correction.md`](working-memory/2026-07-28_B2-model-metadata-and-networking-sequencing-correction.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-memory-estimate.md`](working-memory/2026-07-28_B2-gemma-e4b-memory-estimate.md)
- [`working-memory/2026-07-28_B2-first-observed-gemma-e4b-load-and-smoke.md`](working-memory/2026-07-28_B2-first-observed-gemma-e4b-load-and-smoke.md)

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its own stable responsibility or dated evidence changes.
