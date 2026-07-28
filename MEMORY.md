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
- **State-contract v1.1 result:** [`working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md`](working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md)
- **Current independent review and selected diagnostic:** [`working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md`](working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md)

B2 Increment D — minimum package and upstream evidence — is complete. B2 Increment E — transparent decision — remains selected. Ali approved a bounded local-LLM experiment direction, not automatic model adoption.

No semantic interpretation method, decision contract, recommendation policy, active model/provider dependency, or recommendation code has been adopted or implemented.

## Current observed result

The first Gemma E4B deployment established:

```text
runtime load and restoration: passed
strict structured output: passed
exact source quotation grounding: passed
simple fix claim classification: passed
```

State-contract prompt v1.1 then established:

```text
clear fix: 3/3 passed
no decision-relevant claim: passed
ambiguity case: failed against frozen oracle
conflict case: not run after stop condition
```

Ambiguity source:

```text
Compatibility behavior was adjusted for older environments.
```

Observed:

```text
state: resolved
category: compatibility_assurance
change state: changed_unspecified
source quote: exact
unresolved reasons: none
```

The object was structurally and cross-field consistent. The failure contained two different issues:

1. **Category error:** an adjustment to compatibility-related behavior is not an explicit compatibility assurance.
2. **Oracle/vocabulary overlap:** the current prompt admits `changed_unspecified` for an explicit change with unknown direction, while the frozen oracle required missing direction/details to force `unresolved`.

## Current contract decision

### Semantic-state responsibility

`resolved` means the extractor can responsibly represent the minimum explicit source meaning.

It does not mean:

```text
the source is detailed enough for a maintainer action
evidence is sufficient
investigation may stop
the upgrade is compatible or safe
```

Those remain later deterministic responsibilities.

### `compatibility_assurance`

Use only when the source explicitly assures continued compatibility, backward compatibility, drop-in replacement behavior, or absence of required migration.

The word `compatibility` alone is insufficient.

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

Examples:

- potentially affected text without an explicit change;
- unidentified subject or referent;
- support-policy change without added versus dropped direction;
- current versus future timing cannot be resolved;
- materially different categories remain plausible;
- accepting a claim would overstate incomplete source meaning.

### Revised exact ambiguity oracle

```text
state: resolved
category: interface_or_behavior_change
change state: changed_unspecified
one exact grounded claim
zero unresolved reasons
```

Claim limit:

> The release states only that compatibility behavior for older environments was adjusted. It does not establish improvement, regression, compatibility assurance, migration requirements, safety, or sufficiency.

## Frozen category/change-state matrix

Deterministic validation must enforce:

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

## Behavior-validated product boundary

Previously observed in Ali's WSL2 Python 3.12 environment:

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

Not established:

- complete CI coverage;
- release-prose meaning under an adopted method;
- target-repository compatibility or objective safety;
- evidence sufficiency or stopping;
- merge, targeted-check, investigate/block, defer, or abstain action.

## Current local deployment control

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

The observed deployment fits and runs stably on Ali's RTX 3070 Laptop GPU. This establishes operational viability only, not semantic adoption.

All models are currently unloaded.

## Immediate blocker

```text
state contract v1.2 category definitions
→ revised changed_unspecified versus unresolved boundary
→ deterministic category/change-state matrix
→ revised exact ambiguity oracle
→ non-tailored contrast suite
→ conflict completion case
→ reviewed result
```

## Exact continuation

Follow [`working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md`](working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md):

1. keep the same Gemma E4B model, quantization, 4096 context, load configuration, endpoint, flat schema, temperature, seed, and grounding rules;
2. change the prompt contract from v1.1 to v1.2 only by adding the frozen category, compatibility-assurance, `changed_unspecified`, and `unresolved` boundaries;
3. add and self-test the deterministic category/change-state matrix;
4. freeze the revised ambiguity oracle and all contrast cases before inference;
5. run the exact ambiguity source three times and require 3/3 `resolved + interface_or_behavior_change/changed_unspecified` grounded results;
6. only after that passes, run the contrast suite covering generic unspecified behavior change, explicit compatibility assurance, genuine unresolved relevance, directionless support-boundary change, and the no-claim regression control;
7. only after the contrast suite passes, run the previously blocked conflicting-support case;
8. stop on the first failure and preserve the exact result without loosening multiple variables;
9. preserve raw requests, responses, reasoning/logs, validation, resources, hashes, restoration, and the current product test output;
10. stop and push before the broader corpus, pytest release input, Instructor, Qwen, Gemma 12B, networking changes, or product integration;
11. update this file with the observed result and exact continuation;
12. do not begin Increment F until the transparent decision boundary is behavior-validated.

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

first smoke review:
1c03ec1e330c65992ae0f215d3151f3c8eab1397

state-contract v1.1 diagnostic result:
eba99c7e2940e2d01767d925cf473a9b79c537c1

ambiguity-boundary review and selected v1.2 diagnostic:
50fb08adad9126de358a0a31a41430aec98432fc
```

## Detailed dated evidence

- [`working-memory/2026-07-28_B2-transparent-decision-method.md`](working-memory/2026-07-28_B2-transparent-decision-method.md)
- [`working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md`](working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md)
- [`working-memory/2026-07-28_B2-upstream-semantic-boundary.md`](working-memory/2026-07-28_B2-upstream-semantic-boundary.md)
- [`working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md`](working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md)
- [`working-memory/2026-07-28_B2-current-stage-evidence-request.md`](working-memory/2026-07-28_B2-current-stage-evidence-request.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-observed-evaluation-result.md`](working-memory/2026-07-28_B2-gemma-e4b-observed-evaluation-result.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-smoke-review-and-state-contract-diagnostic.md`](working-memory/2026-07-28_B2-gemma-e4b-smoke-review-and-state-contract-diagnostic.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md`](working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md)
- [`working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md`](working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md)

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its own stable responsibility or dated evidence changes.
