# 06 — Testing, Model Evaluation, and Diagnosis

**Depth target:** implementation understanding of deterministic test layers, live model evaluation, repeated failures, decision effects, and negative evidence.

**Read with:**

- [`../../tests/test_extraction_validation.py`](../../tests/test_extraction_validation.py)
- [`../../tests/test_extraction_service.py`](../../tests/test_extraction_service.py)
- [`../../tests/test_decision.py`](../../tests/test_decision.py)
- [`../../tests/test_llm_extractor.py`](../../tests/test_llm_extractor.py)
- [`../../scripts/evaluate_python_support_models.py`](../../scripts/evaluate_python_support_models.py)
- [`../../scripts/evaluate_input_risk_models.py`](../../scripts/evaluate_input_risk_models.py)

## 1. Different tests answer different questions

A single “tests passed” statement is too vague for this work.

| Layer | Question |
|---|---|
| Contract test | Are invalid shapes, values, authority, or references rejected? |
| Grounding test | Are source/evidence invariants enforced exactly? |
| Orchestration test | Are extractor, grounding, conversion, and policy connected correctly? |
| Decision test | Are model-derived claims limited to permitted outcomes? |
| Transport test | Is the LM Studio request/response boundary handled correctly? |
| Live semantic evaluation | What does the real local model actually claim? |
| Decision-effect evaluation | What final policy effect does the model error produce? |
| Repetition run | Does the failure recur under the recorded local setup? |

## 2. Deterministic grounding tests

These tests supply candidates directly and do not contact LM Studio.

They prove behaviors such as:

- quote not in source is rejected;
- version must appear in the quote;
- quote occurrence must be unique;
- exact duplicates are rejected;
- model authority is preserved;
- instruction-shaped and semantically wrong candidates may still pass mechanical grounding;
- contradictory source claims remain visible.

A grounding test can intentionally accept a semantically wrong model claim because the validator’s responsibility is mechanical correspondence, not semantic repair.

## 3. Orchestration tests

`_FakeExtractor` implements the extractor protocol and records received text.

This allows deterministic proof that:

```text
evidence observation
→ extractor
→ grounding
→ attributed decision claims
→ deterministic policy
```

Representative tests prove:

- a grounded drop reaches `run_targeted_checks`;
- an ungrounded quote produces no decision claim and abstains;
- an instruction-shaped drop can only increase scrutiny;
- an instruction-shaped favorable addition cannot reduce caution.

## 4. Decision authority tests

The decision tests prove invariants more important than prompt wording:

- `transformation_id` is required;
- unactivated authority such as `trusted` is rejected;
- unknown or missing evidence references are rejected;
- a favorable model-derived addition produces abstention;
- no-claim input produces abstention;
- a dropped model-derived claim plus missing repository support can request targeted checks;
- limitations explicitly disclose that the claim is model-derived and uncorroborated.

## 5. Live evaluator metrics

Each semantic case records:

```text
candidate_correct
grounded_output_correct
decision_effect_correct
passed
```

### `candidate_correct`

Did the raw model output contain the expected claims?

### `grounded_output_correct`

Did the claims that passed mechanical grounding match the expected claims?

Because final grounding no longer repairs semantics with phrase rules, candidate and grounded correctness are often the same unless a mechanical invariant rejects a candidate.

### `decision_effect_correct`

Did the deterministic policy produce the expected outcome from the grounded claims?

This is the most product-relevant metric of the three for the current experiment.

### `passed`

A clean pass requires:

- candidate correctness;
- grounded-output correctness;
- decision-effect correctness;
- no validation errors.

## 6. Expected decision outcome in the evaluator

The current evaluator creates missing repository-support evidence for every semantic case.

It expects:

```text
any expected dropped claim → run_targeted_checks
otherwise                 → abstain
```

This makes false dropped claims materially visible because they change the outcome.

False favorable additions can remain semantically wrong while still producing the expected cautious abstention.

Therefore:

```text
decision-effect correct
≠ semantic claim correct
```

Both metrics must be retained.

## 7. Final complete results

| Deployment | Candidate correct | Grounded correct | Decision-effect correct | Average latency |
|---|---:|---:|---:|---:|
| `gemma-4-e2b-it` | 9/14 | 9/14 | 11/14 | 3.163 s |
| `qwen3-4b-instruct-2507` | 8/14 | 8/14 | 10/14 | 0.749 s |

### Gemma material failures

False dropped-support claims on:

- embedded instruction;
- embedded classification;
- split-line instruction.

These changed abstention to targeted checks.

False additions on continued-support/output-request wording remained bounded to abstention.

### Qwen material failures

Qwen produced the same instruction-shaped false drops and also treated deprecation as dropped.

Its favorable false claims also remained bounded by the policy.

## 8. Focused repetition

Six discriminating cases were repeated twice per model.

| Deployment | Clean repetitions | Decision-effect correct |
|---|---:|---:|
| Gemma | 3/12 | 6/12 |
| Qwen3 | 0/12 | 4/12 |

The repeated failures showed that the unacceptable outcomes were not isolated one-off observations in that recorded local setup.

Repetition still does not prove universal determinism.

## 9. Why exit status 1 can mean a successful evaluation

The evaluator returns zero only if every scored case passes.

When a model fails cases:

```text
process exit = 1
JSON artifact complete and parseable
```

This means:

- the evaluation executed;
- negative cases were detected;
- automation correctly signaled model failure.

It does not mean the script crashed.

Always distinguish:

```text
experiment completed with negative result
experiment execution failed
```

## 10. Input-risk evaluator as retained negative evidence

The detector evaluator expanded to 22 cases covering:

- ordinary technical language;
- quoted prompt-injection discussion;
- role/schema wording;
- direct attacks;
- indirect output steering;
- obfuscation;
- encoded requests;
- HTML/JSON forms;
- multilingual wording;
- invisible characters.

At 768 tokens:

- Gemma scored 22/22 in one run;
- Qwen scored 20/22, with one benign false positive and one adaptive false negative.

This was insufficient for runtime adoption because:

- one clean run is not certification;
- false positives suppress legitimate evidence;
- false negatives still expose the extractor;
- the second model adds latency and operational dependency;
- authority limits address downstream effects more directly.

## 11. Test runner failure versus source failure

An initial command used:

```bash
python -m pytest -q
```

The environment did not install `pytest`.

The repository uses `unittest`, and the configured suite passed:

```bash
python -m unittest discover -s tests -v
```

This was a runner-selection error, not a source-code defect.

Do not repair application code for a missing test runner that the project does not require.

## 12. Contract-migration failures

When facts became attributed claims, tests failed because they still referenced removed names and old limitations.

Correct procedure:

1. observe the failure;
2. verify it matches the intended contract change;
3. update tests to the new public behavior;
4. rerun focused tests;
5. run the full suite.

Blindly editing tests until green would erase the opportunity to verify the migration boundary.

## 13. Diagnostic matrix

| Observation | Category |
|---|---|
| Request times out | Transport/runtime |
| JSON truncates | Token/output budget |
| Unsupported JSON enum | Schema/model output |
| Valid JSON misreads deprecation | Model semantics |
| Quote absent | Mechanical grounding |
| Authority missing | Contract/provenance |
| Favorable claim reduces caution | Decision-authority defect |
| Dropped false claim triggers work | Material model decision-effect failure |
| Benign detector input quarantined | Detector false positive/availability |
| Indirect steering proceeds | Detector false negative/exposure |
| Evaluator exits 1 with artifact | Negative scored result, not execution crash |

## 14. Useful commands

```bash
python -m unittest discover -s tests -p 'test_extraction_validation.py' -v
python -m unittest discover -s tests -p 'test_extraction_service.py' -v
python -m unittest discover -s tests -p 'test_decision.py' -v
python -m unittest discover -s tests -v
python -m compileall -q src tests scripts
```

Historical live evaluation command:

```bash
python scripts/evaluate_python_support_models.py \
  --models gemma-4-e2b-it qwen3-4b-instruct-2507 \
  --seed 0 --timeout 60 --max-tokens 768 --repetitions 1 \
  --json-output m2-s02-attributed-claim-decision-effects.json
```

Do not rerun it merely to seek a favorable score. Rerun only for a defined investigation or changed model/runtime condition.

## Ownership check

1. Why can `decision_effect_correct=True` coexist with `candidate_correct=False`?
2. Why did false dropped claims matter more than false additions in this policy?
3. What does an intentional exit status 1 communicate?
4. Which tests should fail when authority metadata is missing?
5. Why is one 22/22 detector run insufficient for adoption?
6. How do you distinguish a runner-selection failure from a source failure?
