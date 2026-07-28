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
- **Gate A evidence:** [`working-memory/2026-07-29_B2-gemma-e4b-v1.2-gate-a-repetitions-2-3-result.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.2-gate-a-repetitions-2-3-result.md)
- **Current independent review:** [`working-memory/2026-07-29_B2-gemma-e4b-v1.2-gate-a-3-of-3-independent-review.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.2-gate-a-3-of-3-independent-review.md)
- **Authorized runner:** [`working-memory/evidence/2026-07-29-gemma-e4b-v1.2-gates-b-c/run.sh`](working-memory/evidence/2026-07-29-gemma-e4b-v1.2-gates-b-c/run.sh)

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

- `resolved`: the extractor can responsibly represent the minimum explicit source meaning. It does not mean the source is sufficient, compatible, safe, or actionable.
- `no_decision_relevant_claim`: no supported decision-relevant claim is present.
- `unresolved`: no supported category/change-state pair can represent the minimum source meaning without invention.
- `conflicting`: materially opposing grounded claims cannot responsibly be collapsed into one meaning.

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

Frozen request controls:

```text
state-contract prompt: v1.2
flat JSON Schema: frozen
category/change-state matrix: frozen
source cases and oracles: frozen
max_tokens: 1024
temperature: 0
seed: 0
stream: false
Instructor: not used
retries: none
```

## Latest verified result — Gate A passed 3/3

Reviewed Gate A evidence commit:

```text
bb32fcd1c3858a9a88811efd6d42a9278dc5fa58
```

Independent review commit:

```text
e9e3f0a6ba9480f334ec43835c5f9d76677332f8
```

All three ambiguity repetitions used identical identities:

```text
system prompt SHA-256: 31dbadbd0a4c5f865817d320c4dfb4991619790f7506a9e0b532664a95210eaa
schema SHA-256: 32bb4fde057436c5c51f7d0288b7e028d9f094642bab93be290cbdb1849cdf96
request SHA-256: 9257bcfb6c83ea4278b40183a48328ff76df115f5b0eadf359a848b401d31b6f
```

For:

```text
Compatibility behavior was adjusted for older environments.
```

all three returned:

```text
state: resolved
category: interface_or_behavior_change
change state: changed_unspecified
one exact grounded claim
zero unresolved reasons
```

Gate A repetitions 2 and 3:

```text
repetition 2 pre-load GPU used/free: 1028 / 6991 MiB
repetition 3 pre-load GPU used/free: 996 / 7023 MiB
finish reason: stop for both
completion tokens: 458 for both
reasoning tokens: 360 for both
structure validation: passed
semantic oracle: passed
post-unload loaded models: none after each repetition
workflow exit: 0
restoration exit: 0
product tests: 64 passed
manifest verification: 212/212 passed
```

Gate A establishes repeatability for this exact weak explicit behavior-change case under the frozen v1.2 contract. It does not establish broader semantic reliability or model adoption.

## Immediate blocker

```text
Gate A passed 3/3
→ frozen Gate B contrast suite
→ frozen Gate C conflicting-support case only if Gate B passes
→ independent review
```

## Exact continuation

Use:

```text
working-memory/evidence/2026-07-29-gemma-e4b-v1.2-gates-b-c/run.sh
```

Execution order:

1. enforce the clean GPU/no-loaded-model preflight;
2. load the same Gemma E4B configuration;
3. run the five frozen Gate B cases once each, in order;
4. stop on the first failed, truncated, invalid, or unsupported result;
5. only if all Gate B cases pass, run the frozen Gate C conflicting-support case once;
6. unload the model and confirm no loaded models remain;
7. run product tests;
8. preserve requests, responses, reasoning/logs, validation, snapshots, load/unload, hashes, and manifest verification;
9. stop and push the first result for independent review.

Frozen Gate B cases:

```text
1. Request retry behavior changed for slow networks.
2. This release remains backward compatible with the previous patch release and requires no migration.
3. Older environments may be affected.
4. Python version support policy changed in this release.
5. Documentation examples were reorganized and several spelling errors were corrected.
```

Frozen Gate C case:

```text
This release adds Python 3.13 support. This release drops Python 3.13 support.
```

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

corrected completion-recovery evidence:
154d83a3ad0741dc60262f0deaafed07d0536669

Gate A repetitions 2 and 3 evidence:
bb32fcd1c3858a9a88811efd6d42a9278dc5fa58

Gate A 3-of-3 independent review:
e9e3f0a6ba9480f334ec43835c5f9d76677332f8

Gates B/C runner:
c36c28d4c975c906045a6816fc87ba39ba413d84
```

## Detailed dated evidence

- [`working-memory/2026-07-28_B2-transparent-decision-method.md`](working-memory/2026-07-28_B2-transparent-decision-method.md)
- [`working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md`](working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md`](working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md)
- [`working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md`](working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md)
- [`working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-independent-review.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-independent-review.md)
- [`working-memory/2026-07-29_B2-gemma-e4b-v1.2-gate-a-repetitions-2-3-result.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.2-gate-a-repetitions-2-3-result.md)
- [`working-memory/2026-07-29_B2-gemma-e4b-v1.2-gate-a-3-of-3-independent-review.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.2-gate-a-3-of-3-independent-review.md)

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its own stable responsibility or dated evidence changes.
