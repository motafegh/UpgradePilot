# B2 Step 6D — Contract-v2 offline replay result

**Date:** 2026-08-03  
**Scope:** Deterministic counterfactual replay only; no new model calls.  
**Input evidence:** `working-memory/evidence/2026-08-03-step6d/support-drop-evaluation.json`

## User-validated deterministic baseline

Before the replay, the user reported:

```text
Ran 332 tests in 0.059s

OK
```

The first direct-file replay invocation failed before execution with:

```text
ModuleNotFoundError: No module named 'experiments'
```

This was an invocation/import-root issue only. The replay then ran successfully with Python module mode:

```bash
python -m experiments.step6_support_drop_contract_v2_replay
```

## Replay result

The replay made:

```text
new model calls: 0
network calls: 0
retries: 0
```

Observed summary:

```json
{
  "contract_version": 2,
  "counterfactual_replay": true,
  "new_model_calls": 0,
  "historical_runs": 25,
  "historical_passed": 14,
  "replay_passed": 21,
  "replay_failed": 4,
  "historical_failures_rescued": 7,
  "failure_classes": {
    "zero_candidate_state_mismatch": 4
  },
  "critical_repeat_consistency": {
    "support_added_control": true,
    "negated_drop_control": true,
    "future_drop_control": true,
    "raised_minimum_without_explicit_dropped_line": true,
    "s001_exact_excerpt": true
  },
  "all_critical_repeats_consistent": true
}
```

## What contract v2 proved

Seven of the eleven v1 failures disappeared without changing any model output. These were candidate-bearing responses where Gemma selected the correct candidate identity but contradicted that selection with the redundant v1 top-level state.

Contract v2 derives:

```text
non-empty candidates -> candidates_available
```

instead of asking the model to predict that state separately.

This rescued:

- direct drop;
- both paraphrased drop forms;
- valid drop plus unrelated fix;
- S001 repetitions;
- other candidate-bearing v1 state contradictions represented in the historical run.

The replay therefore establishes that those failures were representation/contract failures rather than failures to select the support-drop candidate.

## Remaining four strict-oracle failures

All four remaining failures were the same class:

```text
zero_candidate_state_mismatch
```

Specifically:

- `raised_minimum_without_explicit_dropped_line` — all three trials returned `no_relevant_claim`, while the frozen oracle expects `unresolved`;
- `ambiguous_support_wording` — returned `no_relevant_claim`, while the frozen oracle expects `unresolved`.

No remaining replay failure was:

- a false positive support-drop candidate;
- a false negative on an explicit positive candidate;
- a wrong Python line;
- a wrong introduced release;
- a wrong source line;
- a grounding failure;
- a repeat inconsistency.

## Downstream meaning

The existing deterministic contracts preserve a diagnostic distinction:

```text
no_relevant_claim -> no_support_drop_claim
unresolved        -> candidate_unresolved
```

However, current target-Python relevance treats every `UpstreamSupportDropClaimProblem` identically for activation:

```text
any upstream claim problem
-> upstream_claim_unresolved
-> target Python comparison is not activated
```

Therefore the four strict-oracle mismatches are currently diagnostic-classification errors, not unsafe admissions of a support-drop claim.

This does **not** authorize rewriting the frozen oracle. The exact state distinction remains part of strict semantic scoring.

## Next evaluation rule

The next live contract-v2 evaluation must preserve two distinct metrics:

1. **strict oracle score** — exact frozen state/candidate/trust expectations, including `unresolved` vs `no_relevant_claim`;
2. **adoption-safety score** — exact positive/multiple-claim behavior plus safe zero-candidate abstention, where both `no_support_drop_claim` and `candidate_unresolved` are accepted only as downstream stopping outcomes.

The safety score must never permit a false positive or incorrect positive candidate to pass.

## Status

Contract v2 offline replay is complete and materially justifies a new live v2 scoring run.

No model is adopted yet. Instructor/retries remain out of the first-pass evaluation.
