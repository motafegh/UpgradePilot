# Deferred Phase D — D3 supporting note: coverage and failure classification

**Date:** 2026-10-06  
**Branch:** `learning/deferred-api-interpretation-phase-d-2026-10-05`  
**Status:** Supporting D3 learning evidence; D3 remains IN PROGRESS.  
**Active tracker:** `working-memory/2026-10-06_deferred-D_post-design-evidence-integration.md`.  
**Mutation boundary:** learning documentation only.

## Ownership established in this checkpoint

Ali correctly classified these failure classes:

- exact intended request cannot fit the loaded model context -> **capacity/input-fit failure**; independently acquired source evidence remains valid while no semantic result is established;
- complete, valid, correctly grounded proposal with wrong meaning -> **semantic failure**; source, provider, structure and grounding may remain valid while the interpretation does not;
- clean, sufficiently budgeted completion that omits material supplied changes -> **omission/semantic-coverage failure**; individually correct admitted observations may remain usable within their scope, but complete interpretation cannot be claimed.

Ali also correctly retained the distinction for incomplete acquisition: a correctly interpreted observation from the source that was actually acquired can remain usable within that explicit scope, while the whole required release/upgrade window remains incomplete.

## Refinement still being resolved

The completion-budget case needs one exact distinction:

```text
context window
= total model envelope available for prompt/input plus generated completion (subject to provider/runtime accounting)

request completion ceiling / max output tokens
= explicit cap on how many tokens this particular call may generate
```

In the first real Gemma pass, the intended input fit the measured loaded context, but the full and partial HTTPX outputs stopped exactly at the 1,536-token completion ceiling. Therefore the primary observed failure was **completion-budget/truncation**, not input-context fit.

Increasing only the model context would not necessarily repair that run if the request still kept `max_tokens=1536`; generation could still stop at 1,536 tokens. Conversely, increasing only `max_tokens` can be insufficient if the larger reserved output no longer fits the total context window. A valid capacity repair therefore needs both conditions to hold:

```text
rendered input + schema/provider allowance + reserved completion <= effective context

and

requested completion ceiling is large enough for the intended response
```

The later repair increased the loaded Gemma context to 16,384 and the completion reserve/ceiling to 8,192. All 18 calls then completed without truncation, while independent semantic errors persisted. This distinguishes capacity repair from semantic repair.

## Coverage distinction reinforced

Case A from the preceding checkpoint is now precise:

- all required HTTPX source acquired -> acquisition/source coverage succeeds;
- model omits material changes and does not mark them unassessed -> interpretation/semantic coverage fails;
- the source producer's success is not retroactively invalidated by the model omission;
- no complete interpretation claim is allowed.

Case B remains scoped:

- only part of the required release window acquired -> whole-window acquisition incomplete;
- a correct observation from the acquired part remains usable within that source scope;
- no claim of complete release/upgrade coverage is allowed.

## D3 state after this checkpoint

Established at intended depth:

- evaluator separation and development-vs-independent-admission;
- acquisition/source coverage versus interpretation/semantic coverage;
- scoped usefulness of partial acquisition;
- semantic failure versus coverage failure;
- preservation of valid upstream/source evidence when later layers fail.

Still to complete before D3 closure:

- final confirmation of context-window versus completion-ceiling distinction;
- provider and contract/grounding failure proof implications across changed cases;
- `unassessed` quality versus evasion/all-unknown output;
- complete failure-class ownership checkpoint and proof-preservation matrix.
