# S006 — qldebugger / Pydantic Validator Coverage Gap

> **Execution status:** Complete at the admitted simulation depth.  
> **Case form:** Real-derived controlled variant.  
> **Primary result:** Strong targeted-check traceability/design evidence with a blind-evaluation limitation.  
> **Maintainer-action result:** None; the case deliberately stops before merge/block/defer/safety judgment.

## Frozen case

- Target repository: `eduardoklosowski/qldebugger`
- Pull request: `#27`
- PR state observed: closed, unmerged
- Base SHA: `b9e24267507d29c364d32e60f2bdc6075d91c395`
- Head SHA: `a454b47b8e483dffc825a3c9998f38e7634ec93b`
- Changed file: `pyproject.toml`
- Dependency: `pydantic`
- Old requirement: `^1.10`
- Proposed requirement: `>=1.10,<3.0`
- Dependency role: direct production dependency
- Controlled variable: visibility of one exact discriminating target test
- Target source: `src/qldebugger/config/file_parser.py`
- Target symbol: `ConfigLambda._split_handler`

The source repository was **not** mutated. The controlled variant exists only in the simulation evidence boundary: the exact target test for a non-string handler was withheld from the simulation-visible evidence set.

## Owned question

S006 asks:

> When an authoritative upstream behavior change intersects exact target code, but the simulation-visible evidence does not directly exercise the implicated branch, can UpgradePilot derive a narrow check that discriminates the material behavior without broadening into a full compatibility or maintainer-action judgment?

This is a targeted-check-selection and evaluation question, not a general Pydantic V2 migration review.

## Material behavior chain

Official Pydantic V2 migration evidence states that `TypeError` raised inside validators is no longer converted into `pydantic.ValidationError`; the `TypeError` propagates directly.

The frozen qldebugger target contains a Pydantic validator that deliberately raises `TypeError('should be a str')` for non-string handler input.

The bounded reasoning chain is:

```text
Pydantic V2 validator exception semantic
→ proposed range permits Pydantic 2.x
→ exact historical resolved version remains unresolved
→ target validator contains the affected TypeError branch
→ controlled visible tests exercise nearby behavior but not that branch
→ open question: exception behavior across the V1/V2 boundary
→ narrow differential check selected
```

Two activation layers matter:

```text
dependency-version activation
→ an affected Pydantic 2.x version is selected or intentionally compared

then

target code-path activation
→ ConfigLambda receives a non-string handler
```

The case therefore does not equate “the new major is permitted” with “the affected behavior was historically executed.”

## Baseline

The frozen transparent baseline selected:

> `run_targeted_checks`

because exact-head retained CI execution evidence could not be established.

That coarse result was useful as a comparator, but it could not identify **which** targeted check mattered or why.

## Selected check

Before oracle scoring, S006 froze this bounded recommendation:

```text
same frozen qldebugger revision
same input: handler = 1

Pydantic 1.10.9
vs
Pydantic 2.0.0

observe top-level exception class/message
```

Expected discrimination from upstream evidence:

- Pydantic 1.10.9: validator `TypeError` represented through `ValidationError` behavior;
- Pydantic 2.0.0: validator `TypeError` propagates directly.

The check was selected because it executes the exact implicated target branch and controls the dependency-major boundary more cleanly than a generic import check, install-only check, valid-input check, or unconstrained full-suite run.

The dynamic reproduction itself was **not executed** during this case. S006 evaluates the evidence-to-check reasoning and its alignment with a real oracle.

## Oracle and evaluation integrity

The untouched repository contains a dedicated test that passes a non-string integer handler and expects a Pydantic `ValidationError` with the V1-style error shape.

That oracle materially aligns with the selected target symbol, input condition, and exception boundary.

However, the evaluator had already encountered the withheld test during earlier candidate screening.

Therefore S006 may claim:

> the reasoning is traceable, proportionate, and structurally aligned with an independent real repository assertion.

It may **not** claim:

> an oracle-unexposed model or autonomous planner independently discovered the check.

A future benchmark for independent planner discovery would require operational oracle isolation, such as a genuinely fresh evaluator that never receives the withheld test before recommendation freeze.

## Main discoveries

S006 provides bounded evidence for four useful distinctions:

1. **Activation can be layered.** Dependency-version applicability and target behavior-path activation are separate questions.
2. **Broad coverage is not discriminating coverage.** Testing the same component or validator does not prove that the exact behavior implicated by an upstream change is exercised.
3. **Targeted checks should expose information value.** The useful chain is `unresolved question → activating target path → controlled observation → materially different outcomes → bounded information gained`.
4. **Oracle isolation is an evaluation-design property.** Instructions to ignore an oracle already seen do not create a valid blind benchmark.

These are simulation discoveries, not approved runtime schemas or architecture.

## Read in this order

1. [`../../S006_CANDIDATE_SCREENING.md`](../../S006_CANDIDATE_SCREENING.md) — admission, exact case boundary, and real anchor.
2. [`artifacts/CASE_IDENTITY.json`](artifacts/CASE_IDENTITY.json) — frozen identity and controlled variant.
3. [`artifacts/BASELINE_RESULT.json`](artifacts/BASELINE_RESULT.json) — restricted comparator before semantic investigation.
4. [`artifacts/UPSTREAM_AND_TARGET_ACTIVATION.json`](artifacts/UPSTREAM_AND_TARGET_ACTIVATION.json) — authoritative upstream behavior and layered target applicability.
5. [`artifacts/VISIBLE_COVERAGE_EVALUATION.json`](artifacts/VISIBLE_COVERAGE_EVALUATION.json) — controlled visible-evidence coverage gap.
6. [`artifacts/TARGETED_CHECK_RECOMMENDATION.json`](artifacts/TARGETED_CHECK_RECOMMENDATION.json) — frozen narrow check and information-value reasoning.
7. [`artifacts/ORACLE_AND_STOPPING_EVALUATION.json`](artifacts/ORACLE_AND_STOPPING_EVALUATION.json) — oracle alignment, evaluation limitation, and stop decision.
8. [`../../S006_POST_CASE_SYNTHESIS.md`](../../S006_POST_CASE_SYNTHESIS.md) — cross-artifact synthesis and design implications.

## Claim boundary and stop

S006 does **not** establish:

- global Pydantic V2 compatibility for qldebugger;
- the exact Pydantic version installed by historical PR CI;
- that the untouched repository lacked the withheld test;
- autonomous planner reliability;
- representative frequency of this case shape;
- merge safety, upgrade safety, or a maintainer action;
- accepted UpgradePilot architecture.

The case stops because its owned uncertainty is resolved at the intended simulation depth: the upstream behavior, exact target branch, controlled coverage gap, discriminating check, oracle alignment, and evaluation limitation are all known.

No target repository mutation, comment, approval, workflow rerun, close, or merge was performed by UpgradePilot.
