# B2 Step 6D — contract-v1 analysis and contract-v2 replay plan

**Date:** 2026-08-03  
**Scope:** Historical/evaluation record only. This file does not activate a model or product runtime.

## Durable evidence reviewed

Committed Step 6D evidence:

```text
working-memory/evidence/2026-08-03-step6d/support-drop-evaluation.json
```

Evidence commit supplied by Ali:

```text
a4b2e37
```

Observed completed run:

```text
runs planned: 25
runs completed: 25
passed: 14
failed: 11
semantic passed: 14
trust-oracle passed: 14
all critical repeats consistent: true
```

No transport failure or truncation stopped the evaluation.

## Failure decomposition

The terminal/evidence record separates the 11 failures into two high-level classes.

### A. Candidate-bearing state-coherence failures

Seven runs returned at least one candidate while also returning:

```text
state = unresolved
```

The v1 deterministic adapter correctly rejected that contradictory representation because
`CandidateUpstreamClaimResult` requires candidate-bearing results to use:

```text
state = candidates_available
```

Observed cases in this class were:

```text
drop_direct r1
drop_paraphrase_no_longer_supported r1
drop_paraphrase_removed r1
valid_drop_plus_unrelated_fix r1
s001_exact_excerpt r1
s001_exact_excerpt r2
s001_exact_excerpt r3
```

The committed evidence shows at least the direct and S001 examples selecting the correct
Python line, release, and source line while the reasoning itself describes the claim as a
current explicit drop. The conflicting information is the additional top-level state.

This reveals a contract redundancy:

```text
non-empty candidates
and
state = candidates_available
```

encode the same fact twice.

A model should not have to predict both independently when one is mechanically derivable.

### B. Genuine zero-candidate state disagreements

Four runs mapped successfully but chose:

```text
no_relevant_claim
```

where the frozen oracle requires:

```text
unresolved
```

They were:

```text
raised_minimum_without_explicit_dropped_line r1
raised_minimum_without_explicit_dropped_line r2
raised_minimum_without_explicit_dropped_line r3
ambiguous_support_wording r1
```

These remain genuine semantic responsibilities. Contract v2 must not automatically repair
or relabel them.

The raised-minimum reasoning is especially informative: Gemma recognized that the text
changes the support boundary and explicitly considered `unresolved`, but ultimately chose
`no_relevant_claim`. That is not a formatting/grounding problem.

## Contract-v2 principle

Remove only the redundant state prediction.

Model-facing semantic output becomes:

```text
candidates: [...]
unresolved_if_no_candidates: true | false
detail: string
```

The deterministic adapter derives the existing Step 2 contract:

```text
if candidates:
    state = candidates_available
elif unresolved_if_no_candidates:
    state = unresolved
else:
    state = no_relevant_claim
```

The unresolved flag is semantically meaningful only on the zero-candidate branch.

Everything else remains unchanged:

- exact Python X.Y candidates are source-bounded;
- introduced release must be a trusted crossed release;
- source line is selected by deterministic line ID;
- exact source quote/offset recovery remains deterministic;
- Step 2 grounding is unchanged;
- no automatic retries;
- no Instructor dependency;
- no model change;
- no production activation.

## Why replay before another model run

The original 25 raw structured outputs are already committed. A new 25-call run would
change both prompt/contract and model outputs at the same time.

Therefore the next evidence step is an **offline counterfactual replay**:

```text
historical v1 structured output
→ ignore v1 state only when candidates are non-empty
→ preserve v1 zero-candidate state choice
→ contract-v2 deterministic adapter
→ existing semantic oracle
→ existing Step 2 validator
```

This makes zero new model calls and isolates the effect of removing the duplicated state.

Artifacts:

```text
experiments/step6_support_drop_contract_v2.py
experiments/step6_support_drop_contract_v2_replay.py
tests/test_step6_support_drop_contract_v2.py
```

Default replay output:

```text
/tmp/upgradepilot-step6d-contract-v2-replay.json
```

## Decision after replay

The replay does not prove live contract-v2 model behavior. It answers only how much of the
historical score is attributable to the redundant v1 state field.

After the replay:

- if candidate-bearing failures are rescued while zero-candidate semantic failures remain,
  then a live contract-v2 run is justified to test the cleaner prompt/shape;
- if candidate identities themselves remain materially wrong, the model candidate becomes
  weaker and comparison/rejection may be appropriate sooner;
- no model adoption follows directly from replay success.
