# UpgradePilot Current Memory

**Last updated:** 2026-07-29  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. This file records only the live position needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected decision plan:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md)
- **Selected local-model re-evaluation:** [`plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md`](plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md)
- **Deferred network-learning slice:** [`plans/B2_LM_STUDIO_NETWORK_BOUNDARY_LEARNING_PLAN.md`](plans/B2_LM_STUDIO_NETWORK_BOUNDARY_LEARNING_PLAN.md)
- **State-contract v1.2 boundary:** [`working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md`](working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md)
- **Latest corrected result:** [`working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-load-flag-correction-result.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-load-flag-correction-result.md)
- **Current independent review:** [`working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-independent-review.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-independent-review.md)

B2 Increment D — minimum package and upstream evidence — is complete. B2 Increment E — transparent decision — remains selected. Ali approved a bounded local-LLM experiment direction, not model adoption or product integration.

No semantic interpretation method, recommendation policy, model/provider dependency, or recommendation code has been adopted.

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
→ matching GitHub upstream repository
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

## Frozen semantic boundary

### Model responsibility

The model may extract bounded, explicitly attributed candidate claims from authoritative release text. It does not select authority, evidence sufficiency, stopping, safety, or maintainer action.

### Result-state meaning

`resolved` means the extractor can responsibly represent the minimum explicit source meaning. It does not mean the source is sufficient, compatible, safe, or actionable.

`no_decision_relevant_claim` means no supported decision-relevant claim is present.

`unresolved` means no supported category/change-state pair can represent the minimum source meaning without invention.

`conflicting` means materially opposing grounded claims cannot responsibly be collapsed into one meaning.

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

### Ambiguity oracle

For:

```text
Compatibility behavior was adjusted for older environments.
```

required result:

```text
state: resolved
category: interface_or_behavior_change
change state: changed_unspecified
one exact grounded claim
zero unresolved reasons
```

Claim limit:

> The release states only that compatibility behavior for older environments was adjusted. It does not establish improvement, regression, compatibility assurance, migration requirements, safety, or sufficiency.

## Local deployment control

```text
model: gemma-4-e4b-it-ud
parameters: 7.5B
quantization: Q4_K_XL
context: 4096
GPU request: max
parallel: 1
Flash Attention: true
KV cache on GPU: true
speculative MTP: false
TTL: 900
identifier: upgradepilot-gemma-e4b-smoke
endpoint: local LM Studio OpenAI-compatible chat completions
```

Required scored-run preflight:

```text
GPU used <= 2000 MiB
GPU free >= 6000 MiB
no loaded LM Studio model
```

## Latest verified result

Reviewed evidence commit:

```text
154d83a3ad0741dc60262f0deaafed07d0536669
```

The corrected completion-recovery run met the clean baseline:

```text
pre-load GPU used: 1431 MiB
pre-load GPU free: 6588 MiB
loaded models before run: none
model load: passed in 4.22 seconds
post-load GPU used: approximately 4811 MiB
post-load GPU free: approximately 3208 MiB
```

Request controls:

```text
state-contract prompt: v1.2
flat JSON Schema: frozen
category/change-state matrix: frozen
source and oracle: frozen
max_tokens: 1024
temperature: 0
seed: 0
stream: false
Instructor: not used
retries: none
```

Observed response:

```text
finish reason: stop
prompt tokens: 543
completion tokens: 458
reasoning tokens: 360
total latency: 7.261621 seconds
throughput: 66.9463 tokens/second
```

Observed structured result:

```json
{
  "state": "resolved",
  "claims": [
    {
      "category": "interface_or_behavior_change",
      "subject": "compatibility behavior",
      "change_state": "changed_unspecified",
      "source_quote": "Compatibility behavior was adjusted for older environments."
    }
  ],
  "unresolved_reasons": []
}
```

Validation and restoration:

```text
structured shape: passed
state/claims/reasons invariant: passed
category/change-state matrix: passed
exact source grounding: passed
frozen semantic oracle: passed
unload exit: 0
loaded models after cleanup: none
product tests: 64 passed
manifest verification: 106/106 passed
```

This closes the completion-recovery blocker and counts as **state-contract v1.2 Gate A repetition 1 of 3**. It does not establish broader semantic reliability or model adoption.

## Immediate blocker

```text
v1.2 Gate A repetition 1/3 passed
→ two identical clean-baseline repetitions
→ frozen Gate B contrast suite
→ frozen Gate C conflicting-support case
→ independent review
```

## Exact continuation

Create a new dated evidence runner or bundle; do not overwrite any preserved evidence.

Keep frozen:

```text
Gemma E4B Q4_K_XL
4096 context
--gpu max
parallelism 1
TTL 900
identifier upgradepilot-gemma-e4b-smoke
--no-speculative-draft-mtp
state-contract v1.2 complete prompt
flat JSON Schema
category/change-state matrix
frozen source cases and oracles
max_tokens 1024
temperature 0
seed 0
non-streaming endpoint
no Instructor
no retries
pre-load GPU used <= 2000 MiB
pre-load GPU free >= 6000 MiB
no loaded model before the run
```

Execution order:

1. count the verified completion-recovery result as Gate A repetition 1;
2. run the exact ambiguity source for repetitions 2 and 3;
3. require both to return `resolved + interface_or_behavior_change/changed_unspecified`, exact grounding, and zero unresolved reasons;
4. stop on the first failure, truncation, resource-guard failure, or runtime failure;
5. only after Gate A reaches 3/3, run the frozen Gate B contrast cases once each;
6. stop on the first Gate B failure;
7. only after Gate B passes, run the frozen Gate C conflicting-support case;
8. preserve requests, responses, reasoning/logs, validation, resources, load/unload, product tests, hashes, and manifest verification;
9. stop and push for independent review before broader evaluation.

Do not proceed yet to:

- broader semantic corpus;
- real pytest release input;
- Instructor/Pydantic/OpenAI dependency installation;
- Qwen or Gemma 12B comparison;
- reasoning-mode changes;
- networking/CORS/LAN exposure;
- product-source integration;
- maintainer recommendations or Increment F.

## Relevant revisions

```text
last behavior-validated product revision:
bc5aafece111802f1e777dd2b8151ccad1fd822e

state-contract v1.1 result:
eba99c7e2940e2d01767d925cf473a9b79c537c1

v1.2 boundary review:
50fb08adad9126de358a0a31a41430aec98432fc

v1.2 truncation/resource review:
36bce8f08d0a569e4a07b28a13f70ca32c0239fa

first completion-recovery evidence:
dd46228f97b82f014c0d0f89693830fa9a9c9db1

corrected completion-recovery evidence:
154d83a3ad0741dc60262f0deaafed07d0536669

current independent review:
7a37717b9850e2dca5010f6d834dee6ff00b4395
```

## Detailed dated evidence

- [`working-memory/2026-07-28_B2-transparent-decision-method.md`](working-memory/2026-07-28_B2-transparent-decision-method.md)
- [`working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md`](working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md`](working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md)
- [`working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md`](working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-v1.2-truncation-and-resource-baseline-review.md`](working-memory/2026-07-28_B2-gemma-e4b-v1.2-truncation-and-resource-baseline-review.md)
- [`working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-load-flag-review.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-load-flag-review.md)
- [`working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-independent-review.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-independent-review.md)

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its own stable responsibility or dated evidence changes.
