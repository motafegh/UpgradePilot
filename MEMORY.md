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
- **Gate A review:** [`working-memory/2026-07-29_B2-gemma-e4b-v1.2-gate-a-3-of-3-independent-review.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.2-gate-a-3-of-3-independent-review.md)
- **Latest Gates B/C result:** [`working-memory/2026-07-29_B2-gemma-e4b-v1.2-gates-b-c-result.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.2-gates-b-c-result.md)
- **Current independent review:** [`working-memory/2026-07-29_B2-gemma-e4b-v1.2-gate-b-compatibility-claim-partition-review.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.2-gate-b-compatibility-claim-partition-review.md)
- **Authorized runner:** [`working-memory/evidence/2026-07-29-gemma-e4b-v1.3-claim-partition-diagnostic/run.sh`](working-memory/evidence/2026-07-29-gemma-e4b-v1.3-claim-partition-diagnostic/run.sh)

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

## Frozen model responsibility

The model may extract bounded, explicitly attributed candidate claims from authoritative release text. It does not select authority, evidence sufficiency, stopping, safety, or maintainer action.

Result states:

- `resolved`: minimum explicit source meaning can be represented responsibly;
- `no_decision_relevant_claim`: no supported decision-relevant claim is present;
- `unresolved`: no supported category/change-state pair can represent the minimum meaning without invention;
- `conflicting`: materially opposing grounded claims cannot responsibly be collapsed.

Category/change-state matrix:

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

Frozen request controls unless a dated diagnostic explicitly changes one variable:

```text
flat JSON Schema
category/change-state matrix
max_tokens 1024
temperature 0
seed 0
stream false
Instructor not used
retries none
```

## Verified semantic evidence

### Gate A

State-contract v1.2 Gate A passed 3/3 for:

```text
Compatibility behavior was adjusted for older environments.
```

All three returned:

```text
state: resolved
one interface_or_behavior_change / changed_unspecified claim
exact grounding
zero unresolved reasons
```

Reviewed evidence:

```text
Gate A evidence commit: bb32fcd1c3858a9a88811efd6d42a9278dc5fa58
Gate A review commit: e9e3f0a6ba9480f334ec43835c5f9d76677332f8
```

Gate A establishes repeatability only for that exact weak explicit behavior-change case.

### Gate B execution

Reviewed evidence commit:

```text
8e703c86b9da824268119e9437af4eb0ac2c4d8e
```

Gate B case 1 passed:

```text
Request retry behavior changed for slow networks.
→ resolved
→ interface_or_behavior_change / changed_unspecified
```

Gate B case 2 failed:

```text
This release remains backward compatible with the previous patch release and requires no migration.
```

Observed:

```text
claim 1: compatibility_assurance / compatibility_assured
claim 2: support_boundary_change / compatibility_assured
```

The first claim is correct. The second pair is invalid because `support_boundary_change` permits only `support_added` or `support_dropped`.

Operational evidence remained valid:

```text
clean preflight: passed
finish reason: stop
restoration exit: 0
loaded models after unload: none
product tests: 64 passed
manifest verification: 129/129 passed
```

Gate B remaining cases and Gate C were correctly not run.

## Current diagnosis

The failure is classified as:

```text
primary: claim-partition and over-extraction failure
secondary: invalid category/change-state pairing
```

Gemma correctly recognized the explicit backward-compatibility assurance and the absence of required migration. It then treated the no-migration clause as a second claim and forced it into an invalid support-boundary category.

State contract v1.2 defines the compatibility meaning but does not explicitly define how multiple clauses supporting the same proposition should be partitioned into claims.

The selected representation rule is:

> Emit one claim per distinct supported category/change-state proposition, not one claim per clause. Clauses that jointly support the same proposition are combined into one claim.

For the failed sentence:

```text
remains backward compatible
+ requires no migration
→ one compatibility_assurance / compatibility_assured claim
```

The previous generated `semantic_pass: True` field does not establish semantic success. The inherited evaluator skipped semantic-oracle evaluation after domain-structure validation failed. The accurate status is:

```text
structure/domain validation: failed
semantic oracle: not evaluated
model result: failed
```

## Selected v1.3 diagnostic

Append only the claim-partition instruction:

```text
Emit one claim per distinct supported category/change-state proposition, not one claim per clause or phrase. Combine clauses that jointly support the same proposition. Backward compatible and requires no migration jointly express one compatibility_assurance / compatibility_assured claim. Absence of required migration is never a support_boundary_change. Do not emit an extra claim merely to restate supporting evidence. Validate every category/change-state pair before returning JSON.
```

The source, one-claim oracle, model, schema, taxonomy, grounding, runtime configuration, and request controls remain frozen.

Run the exact failed sentence up to three times. Stop on the first failure.

Required per repetition:

```text
finish_reason: stop
state: resolved
exactly one compatibility_assurance / compatibility_assured claim
exact contiguous source quote
zero unresolved reasons
no support_boundary_change claim
```

## Exact continuation

From the repository root:

```bash
git pull --ff-only origin main
bash working-memory/evidence/2026-07-29-gemma-e4b-v1.3-claim-partition-diagnostic/run.sh
```

After the first run, do not rerun automatically. Push the generated result and evidence for independent review.

Do not proceed yet to:

- remaining Gate B cases;
- Gate C;
- broader semantic corpus or real pytest release input;
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

v1.2 Gate A evidence:
bb32fcd1c3858a9a88811efd6d42a9278dc5fa58

v1.2 Gate A independent review:
e9e3f0a6ba9480f334ec43835c5f9d76677332f8

v1.2 Gates B/C evidence:
8e703c86b9da824268119e9437af4eb0ac2c4d8e

v1.2 compatibility claim-partition review:
58bfd87212c6f261c64f6807b090a982f7a726e4

v1.3 diagnostic runner:
5505167a044644b61f1606476c3e1b9736d05e2f
```

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its own stable responsibility or dated evidence changes.
