# UpgradePilot Current Memory

**Last updated:** 2026-07-29  
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
- **v1.2 semantic boundary:** [`working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md`](working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md)
- **v1.2 truncation/resource review:** [`working-memory/2026-07-28_B2-gemma-e4b-v1.2-truncation-and-resource-baseline-review.md`](working-memory/2026-07-28_B2-gemma-e4b-v1.2-truncation-and-resource-baseline-review.md)
- **First completion-recovery result:** [`working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-result.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-result.md)
- **Current independent review:** [`working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-load-flag-review.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-load-flag-review.md)

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

## Local-model evidence established

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

## v1.2 execution and recovery evidence

### First v1.2 execution

The first v1.2 runner completed its evidence lifecycle but produced no semantic result:

```text
finish_reason: length
completion tokens: 512
reasoning tokens: 509
assistant structured content: empty
```

Correct classification:

```text
completion budget exhausted in reasoning
→ no final structured output
→ truncation
→ secondary parser failure
```

That run was also resource-contaminated:

```text
pre-load GPU used: 7205 MiB
pre-load GPU free: 814 MiB
post-load GPU used: 7687 MiB
post-load GPU free: 332 MiB
```

Gemma therefore neither passed nor failed the v1.2 semantic contract in that run.

### First completion-recovery attempt

The required clean resource baseline was met:

```text
pre-load GPU used: 1383 MiB
pre-load GPU free: 6636 MiB
loaded LM Studio models: none
```

But no model loaded and no inference occurred. The runner supplied an unsupported LM Studio CLI option:

```text
--no-speculative-draft-simple
```

LM Studio rejected it before loading:

```text
error: unknown option '--no-speculative-draft-simple'
```

Verified recovery evidence:

```text
load exit: 1
workflow exit: 1
cleanup/unload exit: 0
post-cleanup loaded models: none
product tests: 64 passed
manifest verification: 63/63 passed
```

This was a runner defect, not a Gemma, semantic-contract, GPU, or 1024-token result.

## Immediate blocker

```text
remove unsupported load flag
→ preserve every semantic and runtime variable
→ recover one complete 1024-token v1.2 response
→ review state/category result
```

Gemma E4B still has neither passed nor failed the v1.2 semantic contract.

## Exact continuation

Use the corrected runner:

```text
working-memory/evidence/2026-07-29-gemma-e4b-v1.2-completion-recovery-load-flag-correction/run.sh
```

Preserve the failed first recovery bundle unchanged.

Required pre-load control:

```text
GPU used <= 2000 MiB
GPU free >= 6000 MiB
no loaded LM Studio model
```

Keep unchanged:

```text
Gemma E4B Q4_K_XL
4096 context
--gpu max
parallelism 1
TTL 900
identifier upgradepilot-gemma-e4b-smoke
--no-speculative-draft-mtp
v1.2 complete prompt
flat JSON Schema
category/change-state matrix
exact ambiguity source and revised oracle
max_tokens 1024
temperature 0
seed 0
non-streaming endpoint
no Instructor and no retries
```

Change only:

```text
remove unsupported --no-speculative-draft-simple from the load command
```

The corrected runner must:

1. enforce the GPU and no-loaded-model preflight;
2. run the exact ambiguity source once;
3. classify `finish_reason` before parsing inner content;
4. stop after the one response;
5. preserve load, snapshots, request, response, reasoning/logs, validation, unload, product tests, and hashes;
6. stop before repetitions, contrasts, conflict, broader corpus, pytest input, Instructor, Qwen, Gemma 12B, networking, or product integration;
7. push the first result for independent review.

After review:

- complete correct output → return to the v1.2 Gate A repetition plan;
- complete semantic failure → review prompt tension or compare Qwen under the same frozen contract;
- truncation at 1024 → evaluate reasoning-mode control or contract simplification separately;
- resource guard failure → identify the external GPU consumer;
- another load failure → classify its exact cause before changing another variable.

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

state-contract v1.1 result:
eba99c7e2940e2d01767d925cf473a9b79c537c1

v1.2 boundary review:
50fb08adad9126de358a0a31a41430aec98432fc

v1.2 execution evidence:
b645b9e690c20d0be2f3178dc75ad7b8c8c97ef4

v1.2 truncation/resource review:
36bce8f08d0a569e4a07b28a13f70ca32c0239fa

first completion-recovery evidence:
dd46228f97b82f014c0d0f89693830fa9a9c9db1

load-flag independent review:
82210bc4d79afb052ef878e5ecd881ae21ab5f46

corrected completion-recovery runner:
833aea21068ebb98d7a9ad490200146d7eac7212
```

## Detailed dated evidence

- [`working-memory/2026-07-28_B2-transparent-decision-method.md`](working-memory/2026-07-28_B2-transparent-decision-method.md)
- [`working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md`](working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md`](working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md)
- [`working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md`](working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.2-diagnostic-result.md`](working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.2-diagnostic-result.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-v1.2-truncation-and-resource-baseline-review.md`](working-memory/2026-07-28_B2-gemma-e4b-v1.2-truncation-and-resource-baseline-review.md)
- [`working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-result.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-result.md)
- [`working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-load-flag-review.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-load-flag-review.md)

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its own stable responsibility or dated evidence changes.
