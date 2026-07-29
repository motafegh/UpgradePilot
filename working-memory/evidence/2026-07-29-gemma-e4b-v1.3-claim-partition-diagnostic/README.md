# Gemma E4B v1.3 Claim-Partition Diagnostic

This directory contains the bounded diagnostic selected by:

- `working-memory/2026-07-29_B2-gemma-e4b-v1.2-gate-b-compatibility-claim-partition-review.md`

## Purpose

The v1.2 Gate B compatibility case produced the required compatibility-assurance claim and then added an invalid support-boundary claim for the phrase `requires no migration`.

This diagnostic adds only the claim-partition rule selected in the review:

```text
one distinct supported category/change-state proposition
→ one claim
```

The phrases `remains backward compatible` and `requires no migration` must be represented as one composite `compatibility_assurance / compatibility_assured` claim.

## Frozen controls

```text
model: gemma-4-e4b-it-ud, Q4_K_XL
context: 4096
GPU: max
parallelism: 1
TTL: 900
identifier: upgradepilot-gemma-e4b-smoke
speculative MTP: disabled
schema: unchanged flat JSON Schema
category/change-state matrix: unchanged
source and one-claim oracle: unchanged
max_tokens: 1024
temperature: 0
seed: 0
streaming: false
Instructor: not used
retries: none
```

Required preflight:

```text
GPU used <= 2000 MiB
GPU free >= 6000 MiB
no loaded LM Studio model
```

## Execution

From the repository root:

```bash
bash working-memory/evidence/2026-07-29-gemma-e4b-v1.3-claim-partition-diagnostic/run.sh
```

The runner:

1. freezes the v1.3 prompt addition and unchanged oracle;
2. self-tests the validator;
3. enforces the resource and no-loaded-model preflight;
4. loads Gemma once;
5. runs the exact failed sentence up to three times;
6. stops on the first failure;
7. unloads Gemma;
8. runs the product tests;
9. writes the result record and evidence manifest.

Do not rerun into this directory. Preserve and push the first result regardless of pass or failure.
