# M2-S02 Learning Package — Historical Experiment

**Status:** Archived historical learning; not part of the active B1/B2 sequence  
**Exact implementation snapshot:** `e7425dcfc20f093ac10c9a903f1c4ae50a8b2638`  
**Reset decision:** [`../../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](../../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)

## Purpose

This directory preserves lessons from the closed M2 semantic-extraction and local-model
experiments. It does not describe current source, current architecture, or a method that B2
must reuse.

The experiment taught useful distinctions:

```text
raw text
≠ untrusted model output
≠ mechanically grounded claim
≠ accepted product interpretation
≠ final decision
```

It also produced negative evidence:

- schema validity did not establish semantic correctness;
- exact quote grounding did not resolve deprecation, negation, or instruction context;
- tested local models produced unsafe false positives;
- model/provider configuration and diagnostics were separate from product authority;
- the model could not be allowed to select a favorable final recommendation.

## Current disposition

The related modules, tests, scripts, dependencies, and generated outputs were removed from
the active tree and preserved through the archive manifest:

- [`../../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md`](../../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md)

Do not use this package as the current learning order, restore its code, copy its tests, or
assume an LLM belongs in B2. Consult a lesson only when a later responsibility names the
relevant question.

## Ownership boundary

Ali directed the experiment and surfaced important failures, but the implementation and
learning material were substantially AI-generated. This package remains historical evidence,
not proof of current implementation ownership or semantic-model capability.