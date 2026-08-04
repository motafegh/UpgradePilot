# B2 Step 6D — Support-Drop Semantic Evaluation Implementation

**Date:** 2026-08-03  
**Status:** Implemented; deterministic validation and live scoring pending.  
**Prerequisite closed:** Step 6C live S001 smoke PASS.  
**Product runtime changed:** No.

## Purpose

Step 6C established that the current WSL + LM Studio + `gemma-4-e4b-it-ud` deployment can correctly process one frozen S001 support-drop case through:

```text
transport
→ structured generation
→ deterministic candidate mapping
→ semantic oracle
→ Step 2 trust admission
```

Step 6D now evaluates whether that behavior generalizes across the entire frozen narrow support-drop responsibility before any model or adapter can be proposed for normal runtime.

## New evaluation artifacts

```text
experiments/step6_support_drop_evaluation.py
tools/run_step6d_support_drop_evaluation.py
tests/test_step6_support_drop_evaluation_harness.py
```

The scorer reuses the Step 6C semantic-selection boundary rather than introducing another model contract.

## Frozen case coverage

All 15 Step 6A cases are run once:

- direct drop;
- paraphrased no-longer-supported drop;
- paraphrased removed-support drop;
- raised minimum plus explicit old-line drop;
- raised-minimum-only ungroundable control;
- support-added control;
- continued-support control;
- negated-drop control;
- future-drop control;
- ambiguous support wording;
- irrelevant fix/no-Python control;
- multiple distinct dropped lines;
- valid drop plus unrelated fix;
- instruction-shaped documentation near a valid drop;
- exact S001 excerpt.

## Repeated critical controls

The following cases run three total trials each:

```text
support_added_control
negated_drop_control
future_drop_control
raised_minimum_without_explicit_dropped_line
s001_exact_excerpt
```

This adds two repetitions for each of five critical cases.

Total planned model calls:

```text
15 initial
+ 10 critical repetitions
= 25
```

There are no automatic retries. A repeated trial is a planned evaluation observation, not a retry after failure.

## Why evaluation continues after semantic failure

A case-level semantic, schema, or mapping failure is evidence and should not erase the rest of the model's error profile.

Therefore Step 6D continues after case-level failures and records them.

A transport/server failure stops the evaluation because subsequent cases would share a contaminated execution boundary and continuing would not measure model semantics meaningfully.

## No-Python control

The frozen `irrelevant_fix_only` case contains no explicit Python X.Y token.

Step 6C's single-case schema could assume at least one explicit Python token because S001 has `3.8` and `3.14`. Step 6D cannot make that assumption.

For a source with no explicit Python token, the Step 6D JSON Schema deterministically sets:

```text
candidates.maxItems = 0
```

The model must then select the appropriate non-candidate state. This avoids inventing a placeholder Python token solely to satisfy schema mechanics.

## Scored boundaries

Each run records separately:

- transport success/failure;
- raw request and outer response;
- latency;
- finish reason;
- usage/token accounting when returned;
- structured JSON parse;
- deterministic candidate mapping;
- semantic oracle errors;
- deterministic Step 2 trust result;
- whether trust outcome matches the frozen oracle;
- diagnostic flags:
  - state mismatch;
  - false positive;
  - false negative;
  - wrong Python line;
  - wrong introduced release;
  - wrong deterministic source selection.

## Candidate ordering is not semantic

The `multiple_distinct_dropped_lines` case may legitimately return the two correct candidates in either order.

Step 6D compares sorted semantic candidate identities rather than requiring model output order to match JSON fixture order.

This avoids turning list ordering into a false semantic failure.

## Critical repeat consistency

For each repeated critical case, the scorer compares the complete candidate/trust/semantic outcome signature across all three trials.

It reports:

```text
critical_repeat_consistency[case_id] = true | false
```

and one aggregate:

```text
all_critical_repeats_consistent
```

Consistency alone is not correctness. Three identically wrong answers remain wrong and will fail the semantic/trust oracle even if repeat consistency is true.

## Localhost execution

Step 6D is run through:

```text
tools/run_step6d_support_drop_evaluation.py
```

The wrapper reuses the already validated Step 6C localhost proxy-isolation helper:

- inherited HTTP/HTTPS/ALL proxy variables removed only for the child process;
- `NO_PROXY=127.0.0.1,localhost,::1`;
- active WSL virtual-environment Python;
- no system/shell/LM Studio proxy configuration change.

## Evidence output

Default output:

```text
/tmp/upgradepilot-step6d-support-drop-evaluation.json
```

The repository is not dirtied merely by running the evaluation.

## Exit behavior

The evaluator returns success only when:

```text
all planned runs complete
and
all runs pass their semantic/trust/finish gates
```

If scoring completes with semantic failures, it exits non-zero while preserving the complete evidence file and summary.

This is intentional. A non-zero exit can mean "evaluation completed and the model failed some cases," not only infrastructure failure.

## Model deployment caveat carried forward

The passing Step 6C LM Studio log reported:

```text
detected an outdated gemma4 chat template, applying compatibility workarounds. Consider updating to the official template.
```

Step 6D preserves the current deployment rather than changing the model/template between smoke and score. That keeps the first scored evaluation comparable to the Step 6C proof.

The warning must be considered when interpreting reproducibility and any eventual model disposition.

## Validation pending

The new deterministic Step 6D tests have not yet been run by Ali.

The live 25-call evaluation has not yet been run.

Do not infer model adoption or Step 6 completion from implementation alone.

## Stop line

Until Step 6D evidence is observed and reviewed:

- do not adopt a semantic extractor into `src/upgradepilot/`;
- do not add a normal-runtime model dependency;
- do not begin target-Python conditional orchestration;
- do not run full S001 relevance end-to-end;
- do not make compatibility/safety/maintainer-action claims.