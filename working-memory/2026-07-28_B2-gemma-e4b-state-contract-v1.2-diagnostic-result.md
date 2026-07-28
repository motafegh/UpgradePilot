# B2 Gemma E4B State-Contract v1.2 Diagnostic Result

**Date:** 2026-07-28  
**Operation:** Execute the selected state-contract v1.2 category and ambiguity-boundary diagnostic through its stop condition  
**Selected diagnostic:** [`2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md`](2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md)  
**Prior result:** [`2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md`](2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md)  
**Raw evidence:** [`evidence/2026-07-28-gemma-e4b-state-contract-v1.2/`](evidence/2026-07-28-gemma-e4b-state-contract-v1.2/)  
**Result classification:** Gate A failed; independent review pending; no model or product adoption

## Compact result

```text
Gate A passed: False
Gate B passed: False
Gate C passed: False
product-test exit: 0
product-test count: 64
```

## Gate A

| Case | Pass | State | Claims | Reasons |
|---|---|---|---:|---:|
| `A_exact_compatibility_behavior_adjustment` | False | `None` | 0 | 0 |

## Gate B

| — | not run | — | — | — |

## Gate C

| — | not run | — | — | — |

## First failure

`A_exact_compatibility_behavior_adjustment`: unspecified failure

## Frozen change

The diagnostic changed only the v1.2 category and `changed_unspecified` prompt
semantics, the deterministic category/change-state matrix, and the revised frozen
oracles. The model, quantization, context, runtime configuration, endpoint, flat
schema, temperature, seed, output budget, grounding rule, and no-Instructor/no-retry
boundary remained frozen. Exact hashes are in `frozen-variable-comparison.json`.

## Restoration and validation

Load, unload, snapshots, logs, product-test output, repository status, and evidence
hashes are preserved in the raw evidence directory. `MEMORY.md` was not modified by
the runner; independent review must update the sole live-state owner.
