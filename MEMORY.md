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
- **First observed result:** [`working-memory/2026-07-28_B2-gemma-e4b-observed-evaluation-result.md`](working-memory/2026-07-28_B2-gemma-e4b-observed-evaluation-result.md)
- **Independent review and selected diagnostic:** [`working-memory/2026-07-28_B2-gemma-e4b-smoke-review-and-state-contract-diagnostic.md`](working-memory/2026-07-28_B2-gemma-e4b-smoke-review-and-state-contract-diagnostic.md)

B2 Increment D — minimum package and upstream evidence — is complete. B2 Increment E — transparent decision — remains selected. Ali approved a bounded local-LLM experiment direction, not automatic model adoption.

The first observed Gemma E4B deployment completed through its stop condition:

```text
operational load: passed
strict structured shape: passed
exact quotation grounding: passed
claim category/direction: passed
overall state selection: failed
restoration: passed
```

The independent audit accepts the evidence bundle and classifies the strongest current cause as **state-contract under-specification**, not yet a model-language-understanding failure.

The immediate blocker is now:

```text
explicit four-state prompt semantics
→ deterministic state/claims/reasons invariant
→ same clear-fix case under all other frozen variables
→ three-run Gate A
→ four-state micro-suite Gate B only if Gate A passes
→ reviewed result
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

network-boundary learning plan:
4be40bb5fcf37102ec48e891ebf313a858baa06c

first observed Gemma evidence:
d3380e91fb59d4603d0dbe4c1d16001cd01f7b91

independent Gemma smoke review:
1c03ec1e330c65992ae0f215d3151f3c8eab1397
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

Not established:

- complete CI coverage;
- release-prose meaning;
- target-repository compatibility or objective safety;
- evidence sufficiency or stopping;
- merge, targeted-check, investigate/block, defer, or abstain action.

## Decision-method design progress

Recorded design evidence includes:

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

## Local LM Studio environment

Established:

```text
LM Studio CLI commit: 71bd99c
server: localhost, port 12345
WSL2 localhost reachability: successful
Python: 3.12.3
GPU: RTX 3070 Laptop, 8192 MiB
```

First control deployment:

```text
model: gemma-4-e4b-it-ud
parameters: 7.5B
quantization: Q4_K_XL
context: 4096
parallel: 1
Flash Attention: true
KV cache on GPU: true
speculative decoding: false
```

Observed resources:

```text
pre-load GPU: 1392 MiB used / 6627 MiB free
post-load GPU: 4759 MiB used / 3260 MiB free
post-smoke GPU: 4792 MiB used / 3227 MiB free
post-unload GPU: 1175 MiB used / 6844 MiB free
```

No OOM, guardrail fallback, crash, restart, or UI instability was observed.

## First structured smoke

Source:

```text
This release fixes a crash when parsing empty configuration files.
```

Model result:

```text
state: unresolved
claim category: fix_or_remediation
claim direction: fixed
source quote: exact
unresolved reasons: none
```

The model's preserved reasoning correctly identified a direct remediation claim. The flat schema and current prompt did not ensure a consistent state choice.

Verified distinction:

```text
schema validity
≠ cross-field domain validity
≠ semantic correctness
```

The run passed schema shape, exact grounding, and claim-level semantics but failed the state/claims/reasons invariant.

## Current diagnosis

The state contract is under-specified in two ways:

1. the prompt explains `no_decision_relevant_claim` and `unresolved`, but does not explicitly define `resolved` and `conflicting`;
2. the flat schema permits every state to coexist with every claims/reasons combination.

For GGUF structured generation, the schema constrains output form but does not teach the model the state meanings. Explicit prompt semantics and deterministic post-validation are therefore mandatory.

A stronger branch schema is deferred until after the prompt-state diagnostic. It may reduce invalid combinations, but it cannot replace semantic instructions or deterministic validation.

## Exact continuation

Follow [`working-memory/2026-07-28_B2-gemma-e4b-smoke-review-and-state-contract-diagnostic.md`](working-memory/2026-07-28_B2-gemma-e4b-smoke-review-and-state-contract-diagnostic.md):

1. keep the same Gemma model, quantization, 4096 context, load settings, source sentence, categories, change states, flat schema, temperature, seed, token budget, endpoint, and validator;
2. change only the prompt's state-selection contract so all four states have explicit meanings and claims/reasons relationships;
3. enforce those relationships in deterministic validation;
4. run the identical clear-fix case once and stop on any failure;
5. if it passes, repeat the same clear-fix case twice more;
6. require three of three `resolved` outputs with one grounded fix claim and no unresolved reasons;
7. only after Gate A passes, run one example each for no relevant claim, ambiguity, and materially conflicting claims;
8. stop and push the evidence before the broader semantic corpus;
9. do not install Instructor, change model, load Qwen/Gemma 12B, alter reasoning mode, change networking, or modify product source during this diagnostic;
10. review the diagnostic result before selecting broader scoring, stronger schema branching, or another model.

## Product and experiment boundaries

Do not yet:

- produce maintainer recommendations;
- treat JSON Schema, Pydantic, Instructor, source quotation, or one successful case as semantic correctness;
- restore archived M2 source or dependencies;
- install Instructor/Pydantic/OpenAI dependencies before adapter comparison is authorized;
- rely on JIT defaults for scored deployments;
- load multiple candidate models concurrently;
- download another model without a named evidence gap and Ali's approval;
- infer safety from absence of an extracted warning;
- let a model select authority, sufficiency, stopping, or action;
- enable CORS or expose LM Studio beyond localhost before the network-boundary learning slice;
- mutate target repositories or require private access;
- begin Increment F until the transparent decision boundary is behavior-validated.

## Detailed dated evidence

- [`working-memory/2026-07-28_B2-transparent-decision-method.md`](working-memory/2026-07-28_B2-transparent-decision-method.md)
- [`working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md`](working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md)
- [`working-memory/2026-07-28_B2-upstream-semantic-boundary.md`](working-memory/2026-07-28_B2-upstream-semantic-boundary.md)
- [`working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md`](working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md)
- [`working-memory/2026-07-28_B2-current-stage-evidence-request.md`](working-memory/2026-07-28_B2-current-stage-evidence-request.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-observed-evaluation-result.md`](working-memory/2026-07-28_B2-gemma-e4b-observed-evaluation-result.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-smoke-review-and-state-contract-diagnostic.md`](working-memory/2026-07-28_B2-gemma-e4b-smoke-review-and-state-contract-diagnostic.md)

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its own stable responsibility or dated evidence changes.
