# B2 Step 6D — Contract-v2 live evaluation result

**Date:** 2026-08-03  
**Scope:** bounded support-drop extractor evaluation only  
**Model:** `gemma-4-e4b-it-ud`  
**Contract:** v2  
**Retries:** disabled

## Deterministic validation reported by Ali

```text
Ran 336 tests in 0.059s

OK
```

## Live execution

Ali ran:

```bash
python tools/run_step6d_contract_v2_evaluation.py
```

The run completed all 25 planned calls.

Observed summary:

```text
strict_oracle_passed: 24
strict_oracle_failed: 1
adoption_safety_passed: 25
adoption_safety_failed: 0
strict_all_runs_pass: false
adoption_safety_all_runs_pass: true
```

The only strict failure was:

```text
ambiguous_support_wording r1
actual: no_relevant_claim
expected: unresolved
```

This remained a safe abstention. No candidate was emitted and Step 2 returned `no_support_drop_claim`.

The raised-minimum-only control returned `unresolved` in all three live v2 trials and no support-drop candidate was admitted.

S001 returned the correct grounded Python 3.8 / release 2.8 claim in all three trials.

Support-added, negated-drop, and future-drop controls all abstained in all three repeated trials.

## Repeat-consistency metric defect discovered after the run

The live evaluator reported the raised-minimum critical repeat as inconsistent even though all three runs produced the same semantic/trust outcome:

```text
candidate state: unresolved
candidate count: 0
trust kind: problem
trust state: candidate_unresolved
adoption safety: pass
```

The differing field was only free-text `detail` wording.

The Step 6 plan requires materially consistent trusted outcomes, not byte-identical explanatory prose. Therefore the original repeat-consistency metric is too strict for adoption review.

A deterministic post-run assessment is being added to:

- ignore free-text detail when measuring material repeat consistency;
- retain candidate identity, candidate state, trusted claim identity/problem state, and adoption-safety result;
- review the ten Step 6 adoption-gate conditions from the committed live evidence;
- make zero new model calls.

## Durable evidence

Committed evidence:

```text
working-memory/evidence/2026-08-03-step6d/contract-v2-replay.json
working-memory/evidence/2026-08-03-step6d/contract-v2-live-evaluation.json
```

Evidence commit reported by Ali:

```text
d19f5da
```

## Current conclusion boundary

The live v2 result is substantially stronger than v1 and satisfies the measured adoption-safety score on all 25 runs. Step 6 is not closed yet because the material-repeat/adoption-gate assessment must be executed and reviewed first.

No model/provider/runtime integration is authorized by this record alone.
