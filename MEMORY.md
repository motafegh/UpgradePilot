# UpgradePilot Current Memory

**Last updated:** 2026-07-28  
**Authority:** Sole repository owner of live project position, selected plan, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. They must not duplicate this live state.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected decision plan:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md)
- **Selected local-model re-evaluation:** [`plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md`](plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md)
- **Deferred network-learning slice:** [`plans/B2_LM_STUDIO_NETWORK_BOUNDARY_LEARNING_PLAN.md`](plans/B2_LM_STUDIO_NETWORK_BOUNDARY_LEARNING_PLAN.md)
- **State-contract v1.1 result:** [`working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md`](working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md)
- **v1.2 boundary decision:** [`working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md`](working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md)
- **v1.2 execution result:** [`working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.2-diagnostic-result.md`](working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.2-diagnostic-result.md)
- **Current independent review:** [`working-memory/2026-07-28_B2-gemma-e4b-v1.2-truncation-and-resource-baseline-review.md`](working-memory/2026-07-28_B2-gemma-e4b-v1.2-truncation-and-resource-baseline-review.md)

B2 Increment D — minimum package and upstream evidence — is complete. B2 Increment E — transparent decision — remains selected. Ali approved a bounded local-LLM experiment direction, not automatic model adoption.

No semantic interpretation method, decision contract, recommendation policy, active model/provider dependency, or recommendation code has been adopted or implemented.

## Established product boundary

UpgradePilot behavior-validly reaches:

```text
public repository + Dependabot PR
→ exact PR identity and complete changed files
→ one supported exact pinned Python dependency update
→ exact-head workflow/job/step evidence
→ bounded CI-authority classification
→ exact PyPI package/version/file identity
→ PyPI-reported file provenance
→ matching upstream GitHub repository
→ exact published release and tag reference
→ bounded release body
→ concise CLI evidence report
→ unresolved_claim
```

Not established:

- complete CI coverage;
- release-prose meaning under an adopted method;
- target-repository compatibility or objective safety;
- evidence sufficiency or stopping;
- merge, targeted-check, investigate/block, defer, or abstain action.

## Local-model evidence established before v1.2

Gemma E4B operational control:

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

Previously observed under a high-headroom GPU baseline:

```text
runtime load and restoration: passed
strict structured output: passed
exact source quotation grounding: passed
simple fix claim classification: passed
clear-fix state contract v1.1: 3/3 passed
no decision-relevant claim: passed
```

State-contract v1.1 ambiguity output:

```text
source: Compatibility behavior was adjusted for older environments.
state: resolved
category: compatibility_assurance
change state: changed_unspecified
source quote: exact
unresolved reasons: none
```

That result exposed:

1. a category error — behavior adjustment is not a compatibility assurance;
2. an oracle overlap — `changed_unspecified` admitted a minimum explicit change while the old oracle forced `unresolved`.

## Frozen semantic boundary

### `resolved`

`resolved` means the extractor can responsibly represent the minimum explicit source meaning.

It does not mean:

```text
the source is sufficient for action
the upgrade is compatible or safe
investigation may stop
a maintainer action is justified
```

Those remain later deterministic responsibilities.

### `compatibility_assurance`

Use only when the source explicitly assures continued or backward compatibility, drop-in replacement behavior, or absence of required migration. The word `compatibility` alone is insufficient.

### `changed_unspecified`

Admit only when:

```text
an interface or behavior change is explicitly stated
+ changed subject or scope is identifiable
+ occurrence of the change is unambiguous
+ direction/effect is not stated
+ no compatibility, safety, support direction, or migration effect is invented
```

Meaning:

> An explicit interface or behavior change occurred; the source does not state its direction or effect.

### `unresolved`

Use when no supported category/change-state pair can represent the minimum source meaning without invention.

### Revised exact ambiguity oracle

```text
state: resolved
category: interface_or_behavior_change
change state: changed_unspecified
one exact grounded claim
zero unresolved reasons
```

### Category/change-state matrix

```text
fix_or_remediation
→ fixed

compatibility_assurance
→ compatibility_assured

support_boundary_change
→ support_added | support_dropped

interface_or_behavior_change
→ deprecated | removed | future_removal | changed_unspecified
```

Any other pair is invalid even when the flat JSON Schema accepts it.

## v1.2 execution review

The v1.2 runner completed its evidence lifecycle:

```text
workflow exit: 0
load command: passed
unload exit: 0
post-unload loaded models: none
product tests: 64 passed
manifest verification: 101/101 passed
```

But Gate A did **not** produce a semantic result.

Observed outer response:

```text
finish_reason: length
completion tokens: 512
reasoning tokens: 509
assistant structured content: empty
```

The harness then raised a secondary `JSONDecodeError` while parsing the empty content. Correct classification:

```text
completion budget exhausted in reasoning
→ no final structured output
→ truncation
→ secondary parser failure
```

### Resource-baseline drift

The run was not operationally comparable to the accepted earlier control.

```text
v1.2 pre-load GPU used: 7205 MiB
v1.2 pre-load GPU free: 814 MiB
v1.2 post-load GPU used: 7687 MiB
v1.2 post-load GPU free: 332 MiB
```

Earlier accepted Gemma controls began with approximately 6.6–6.9 GiB free and retained approximately 3.2–3.4 GiB free after loading.

The current LM Studio surfaces do not expose actual offloaded-layer count. Therefore no exact fallback mechanism is claimed. The observed run is classified as resource-contaminated and non-comparable.

Generation also fell to 7.27 tokens/second and took 75.47 seconds, versus about 64 tokens/second in the earlier clear smoke.

### Prompt tension still visible

The v1.2 prompt retained the v1.1 rule:

```text
resolved requires no material ambiguity
```

and appended the v1.2 rule:

```text
resolved represents the minimum explicit meaning
changed_unspecified permits unknown direction/effect
```

The preserved reasoning correctly rejected `compatibility_assurance` and recognized `changed_unspecified`, but also said `resolved` could not be used because direction/effect was unknown. No final JSON was emitted, so the semantic state/category cannot be scored.

## Immediate blocker

```text
restore comparable GPU baseline
→ correct truncation classification
→ recover one complete v1.2 response
→ review state/category result
```

Gemma E4B has neither passed nor failed the v1.2 semantic contract.

## Exact continuation

Create a new dated **v1.2 completion-recovery** evidence harness. Do not overwrite the preserved v1.2 evidence.

Keep unchanged:

```text
Gemma E4B model and Q4_K_XL quantization
4096 context and existing load settings
parallelism 1
Flash Attention and GPU KV-cache placement
v1.2 prompt
flat JSON Schema
category/change-state matrix
exact ambiguity source and revised oracle
temperature 0
seed 0
non-streaming endpoint
no Instructor and no retries
```

Required operational control before loading:

```text
pre-load GPU used <= 2000 MiB
pre-load GPU free >= 6000 MiB
no loaded LM Studio model
```

Change only the request completion budget:

```text
max_tokens: 512 → 1024
```

Harness requirements:

1. classify outer `finish_reason` before inner parsing;
2. classify empty content explicitly;
3. preserve truncation as the primary failure rather than `JSONDecodeError`;
4. refuse scored inference if the GPU control band is not met;
5. run the exact ambiguity case once;
6. stop after that one response;
7. if `finish_reason` remains `length`, preserve and stop;
8. if complete structured content is returned, validate structure, state invariant, category/change-state matrix, grounding, and the frozen oracle;
9. preserve load, resource, request, response, reasoning/log, validation, unload, product-test, and hash evidence;
10. stop before repetitions, contrast cases, conflict, broader corpus, pytest release input, Instructor, Qwen, Gemma 12B, networking changes, or product integration.

After independent review of that one completion:

- complete correct output → return to the v1.2 Gate A repetition plan;
- complete semantic failure → decide whether to normalize the conflicting prompt wording or retain Gemma only as an operational control and compare Qwen under a frozen contract;
- repeated truncation at 1024 → evaluate reasoning-mode control or contract simplification as a separate diagnostic;
- resource guard cannot be met → identify the external GPU consumer before another model load.

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

## Relevant revisions

```text
last behavior-validated product revision in Ali's environment:
bc5aafece111802f1e777dd2b8151ccad1fd822e

transparent-decision plan:
2a6664f4fae17583afdfcdd59889f5fa3cd0ef06

local-LLM re-evaluation plan:
010f667293d6acdfc71841200737a5b1c7e3dfc7

first observed Gemma evidence:
d3380e91fb59d4603d0dbe4c1d16001cd01f7b91

state-contract v1.1 result:
eba99c7e2940e2d01767d925cf473a9b79c537c1

v1.2 boundary review:
50fb08adad9126de358a0a31a41430aec98432fc

v1.2 execution evidence:
b645b9e690c20d0be2f3178dc75ad7b8c8c97ef4

v1.2 truncation/resource review:
36bce8f08d0a569e4a07b28a13f70ca32c0239fa
```

## Detailed dated evidence

- [`working-memory/2026-07-28_B2-transparent-decision-method.md`](working-memory/2026-07-28_B2-transparent-decision-method.md)
- [`working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md`](working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md)
- [`working-memory/2026-07-28_B2-upstream-semantic-boundary.md`](working-memory/2026-07-28_B2-upstream-semantic-boundary.md)
- [`working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md`](working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-observed-evaluation-result.md`](working-memory/2026-07-28_B2-gemma-e4b-observed-evaluation-result.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md`](working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md)
- [`working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md`](working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.2-diagnostic-result.md`](working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.2-diagnostic-result.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-v1.2-truncation-and-resource-baseline-review.md`](working-memory/2026-07-28_B2-gemma-e4b-v1.2-truncation-and-resource-baseline-review.md)

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its own stable responsibility or dated evidence changes.
