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

## Artifact-layout departure from the historical full bundle

S006 intentionally does **not** reproduce the complete D1-era manual bundle described by [`../../RUNTIME_ARTIFACT_SPECIFICATION.md`](../../RUNTIME_ARTIFACT_SPECIFICATION.md) and [`../../SCENARIO_EXECUTION_TEMPLATE.md`](../../SCENARIO_EXECUTION_TEMPLATE.md).

That historical bundle was designed to model a broad runtime-style dependency-update investigation with invocation, operation history, evidence, findings, decision, reports, follow-up, review/ownership, and conditional artifacts. S006 owns a much narrower evaluation question: whether a discriminating targeted check can be derived from one mapped behavior/coverage gap and evaluated against an oracle.

The purpose-built split used here is:

| Logical responsibility needed by S006 | Durable location |
|---|---|
| admission, question, prospective checkpoints, safety, claim and stop boundary | [`../../S006_CANDIDATE_SCREENING.md`](../../S006_CANDIDATE_SCREENING.md) |
| frozen target/case identity and controlled-variable identity | [`artifacts/CASE_IDENTITY.json`](artifacts/CASE_IDENTITY.json) |
| restricted transparent comparator | [`artifacts/BASELINE_RESULT.json`](artifacts/BASELINE_RESULT.json) |
| authoritative upstream behavior + dependency-version/target-path activation | [`artifacts/UPSTREAM_AND_TARGET_ACTIVATION.json`](artifacts/UPSTREAM_AND_TARGET_ACTIVATION.json) |
| controlled visible-coverage state and unresolved behavior question | [`artifacts/VISIBLE_COVERAGE_EVALUATION.json`](artifacts/VISIBLE_COVERAGE_EVALUATION.json) |
| frozen next-check recommendation, alternatives, information value, claim limits | [`artifacts/TARGETED_CHECK_RECOMMENDATION.json`](artifacts/TARGETED_CHECK_RECOMMENDATION.json) |
| oracle comparison, evaluation integrity, case result, stopping | [`artifacts/ORACLE_AND_STOPPING_EVALUATION.json`](artifacts/ORACLE_AND_STOPPING_EVALUATION.json) |
| human-auditable scenario overview and navigation | this `README.md` |
| cross-artifact discoveries and wider-design implications | [`../../S006_POST_CASE_SYNTHESIS.md`](../../S006_POST_CASE_SYNTHESIS.md) |

The following full-bundle artifacts were therefore **not separately instantiated** for S006: `RUN_MANIFEST.json`, `INVOCATION.json`, `OPERATION_EVENTS.jsonl`, generic `EVIDENCE_ITEMS.jsonl`, generic `CLAIMS_AND_INTERPRETATIONS.jsonl`, generic `FINDINGS.json`, final `DECISION.json`, machine/human maintainer reports, `FOLLOW_UP_STATE.json`, and `REVIEW_AND_OWNERSHIP.json`.

This is not evidence that those responsibilities are generally unnecessary. They were outside this case's bounded evaluation purpose or were preserved directly in the purpose-specific records above. In particular, S006 produced **no final maintainer decision**, so manufacturing `DECISION.json` and maintainer reports merely to resemble the historical bundle would misrepresent the case.

This section is a **post-case integrity clarification** added during a later corpus-usability audit. It does not claim that this explicit mapping existed during the original S006 execution, and it does not rewrite the original prospective checkpoint history. Future cases should document a material departure from the default artifact model at admission/execution time rather than relying on a later clarification.

## Evidence durability and replayability boundary

Unlike S001–S005, S006 does not contain a separate `artifacts/raw/` capture set. Its durable records preserve the frozen target identity, attributed upstream-behavior statement, target activation mapping, controlled coverage classification, recommendation, oracle comparison, and stopping result, but they are not a self-contained archive of every external source payload used during screening/execution.

Consequently, future review should distinguish:

```text
reasoning/audit replay
→ can follow the committed S006 records and their transformations

external-evidence re-verification
→ should reacquire the official Pydantic migration evidence and the exact target files/test at the frozen qldebugger revision

dynamic behavior replay
→ was never performed by S006 and therefore cannot be reconstructed as a historical execution
```

The exact target SHA makes target-source re-verification strongly bounded, but an external documentation page remains an external observation whose current contents may change. Do not treat later reacquisition as proof of what a source looked like at the original observation time unless that identity is independently preserved.

This is a durability limitation, not a reason to fabricate retrospective raw captures now. If a future benchmark depends on independently reproducible source evidence, raw/immutable source snapshots or equivalent exact-content identities should be frozen prospectively.

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