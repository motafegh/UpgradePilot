# M2-S02 Learning Path

**Purpose:** Build Ali's confidence and real ownership of the current semantic-extraction implementation before further method or model decisions.

**Implementation snapshot:** 2026-07-22 current `main` source and tests, including the mandatory pre-extraction input-risk gate.

This package is educational material, not a second specification, plan, progress tracker, or claim of mastery. The authoritative implementation remains the linked source, tests, commands, and runtime evidence.

## What this learning path should produce

After completing the lessons and exercises, Ali should be able to:

1. trace one release-note item through preprocessing, risk screening, semantic extraction, validation, and deterministic decision;
2. distinguish preserved evidence, normalized inspection text, detector candidates, validated risk assessment, extraction candidates, trusted facts, and decision facts;
3. explain why both the risk detector and semantic extractor remain untrusted even with JSON Schema;
4. explain the deterministic proceed/quarantine route and why detector failure quarantines;
5. locate and explain both LM Studio request boundaries, their schemas, settings, provenance IDs, and failure paths;
6. walk through the deterministic input-risk and semantic-validation gates in execution order;
7. distinguish unit tests, orchestration tests, semantic-model evaluation, and input-risk-model evaluation;
8. diagnose whether a failure belongs to preprocessing, risk detection, risk validation/routing, extraction transport, extraction semantics, semantic validation, orchestration, or decision policy;
9. make one bounded prediction-driven test or behavior change with an accurate explanation.

## Depth language used here

Do not reduce learning to completed/not-completed.

| Depth | Meaning |
|---|---|
| **Introduced** | You recognize the term and its role. |
| **Operational** | You can use or inspect it correctly in the current repository. |
| **Implementation** | You can explain the mechanism from the code and diagnose representative failures. |
| **Ownership practice** | You can predict, test, modify, and defend the bounded behavior with decreasing assistance. |

This package targets **implementation depth** for the current M2-S02 path and begins **ownership practice**. It does not claim broad LLM security, general NLP expertise, model safety, or production readiness.

## Study order

Do one lesson at a time. Do not read all files passively in one sitting.

| Order | Lesson | Main outcome |
|---:|---|---|
| 1 | [`01_PIPELINE_AND_TRUST_BOUNDARIES.md`](01_PIPELINE_AND_TRUST_BOUNDARIES.md) | Trace the complete product path, including proceed and quarantine routes. |
| 2 | [`02_CONTRACTS_PYDANTIC_AND_ORCHESTRATION.md`](02_CONTRACTS_PYDANTIC_AND_ORCHESTRATION.md) | Understand the contracts, protocols, immutable states, and two-dependency service composition. |
| 3 | [`03_INPUT_RISK_SCREENING_AND_QUARANTINE.md`](03_INPUT_RISK_SCREENING_AND_QUARANTINE.md) | Understand preserved versus inspection text, untrusted risk detection, deterministic validation, and fail-closed routing. |
| 4 | [`04_LM_STUDIO_STRUCTURED_OUTPUT_AND_DIAGNOSTICS.md`](04_LM_STUDIO_STRUCTURED_OUTPUT_AND_DIAGNOSTICS.md) | Understand the two local model boundaries, structured output, seeds, diagnostics, and provenance. |
| 5 | [`05_DETERMINISTIC_SEMANTIC_VALIDATION.md`](05_DETERMINISTIC_SEMANTIC_VALIDATION.md) | Understand post-extraction admission controls and why they remain bounded containment rather than a general semantic method. |
| 6 | [`06_TESTING_MODEL_EVALUATION_AND_DIAGNOSIS.md`](06_TESTING_MODEL_EVALUATION_AND_DIAGNOSIS.md) | Understand what each test/evaluator layer proves and how to localize failures. |
| 7 | [`07_OWNERSHIP_WORKBOOK.md`](07_OWNERSHIP_WORKBOOK.md) | Demonstrate explanation, prediction, diagnosis, and bounded modification ability. |

## How to study each lesson

Use this loop rather than only reading:

```text
orient to the responsibility
→ inspect the linked source symbols
→ predict a result before reading the explanation
→ read the explanation
→ inspect the relevant tests
→ run the narrow test
→ explain the result without copying the document
→ record the exact remaining confusion
```

A lesson is not owned because it felt understandable while reading. Ownership evidence comes from recall, prediction, diagnosis, and modification.

## Current source map

| Responsibility | Source |
|---|---|
| Evidence contracts | [`../../src/upgradepilot/evidence.py`](../../src/upgradepilot/evidence.py) |
| Input preparation, risk contracts, validation, and routing | [`../../src/upgradepilot/input_risk.py`](../../src/upgradepilot/input_risk.py) |
| Local schema-constrained risk detector | [`../../src/upgradepilot/llm_input_risk_detector.py`](../../src/upgradepilot/llm_input_risk_detector.py) |
| Candidate/trusted extraction contracts and orchestration | [`../../src/upgradepilot/extraction.py`](../../src/upgradepilot/extraction.py) |
| Local semantic extractor and diagnostics | [`../../src/upgradepilot/llm_extractor.py`](../../src/upgradepilot/llm_extractor.py) |
| Deterministic post-extraction validation | [`../../src/upgradepilot/extraction_validation.py`](../../src/upgradepilot/extraction_validation.py) |
| Decision contracts and policy | [`../../src/upgradepilot/decision.py`](../../src/upgradepilot/decision.py) |
| Input-risk deterministic tests | [`../../tests/test_input_risk.py`](../../tests/test_input_risk.py) |
| Risk-detector transport tests | [`../../tests/test_llm_input_risk_detector.py`](../../tests/test_llm_input_risk_detector.py) |
| Semantic validation tests | [`../../tests/test_extraction_validation.py`](../../tests/test_extraction_validation.py) |
| Semantic-extractor transport tests | [`../../tests/test_llm_extractor.py`](../../tests/test_llm_extractor.py) |
| Screened orchestration and decision integration tests | [`../../tests/test_extraction_service.py`](../../tests/test_extraction_service.py) |
| Live semantic-model evaluator | [`../../scripts/evaluate_python_support_models.py`](../../scripts/evaluate_python_support_models.py) |
| Live input-risk-model evaluator | [`../../scripts/evaluate_input_risk_models.py`](../../scripts/evaluate_input_risk_models.py) |

## Supporting project records

- Current responsibility: [`../../plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md`](../../plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md)
- Current continuation: [`../../MEMORY.md`](../../MEMORY.md)
- Detailed implementation and evaluation evidence: [`../../working-memory/2026-07-22_M2-S02_llm-extraction-session.md`](../../working-memory/2026-07-22_M2-S02_llm-extraction-session.md)
- Learning and method-selection rules: [`../../OPERATING_GUIDE.md`](../../OPERATING_GUIDE.md)
- Minimum useful generality: [`../../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)

## Useful deterministic commands

Run from the repository root in the existing project environment.

```bash
python -m unittest discover -s tests -p 'test_input_risk.py'
python -m unittest discover -s tests -p 'test_llm_input_risk_detector.py'
python -m unittest discover -s tests -p 'test_extraction_validation.py'
python -m unittest discover -s tests -p 'test_llm_extractor.py'
python -m unittest discover -s tests -p 'test_extraction_service.py'
python -m unittest discover -s tests
```

The live evaluators are separate because they require LM Studio and actual local models.

```bash
python scripts/evaluate_input_risk_models.py \
  --models qwen3-4b-instruct-2507 \
  --seed 0 \
  --max-tokens 512

python scripts/evaluate_python_support_models.py \
  --models qwen3-4b-instruct-2507 \
  --seed 0 \
  --repetitions 1 \
  --max-tokens 512
```

Do not interpret a command as successful merely because it ran. Each lesson states what its checks do and do not prove.

## Stop condition before resuming implementation

Resume the unresolved responsibility-level method decision only after Ali can:

- explain both the proceed and quarantine paths without reading a prepared answer;
- explain why `none_detected` is permission to continue, not proof of safety;
- predict representative preprocessing, detector, risk-validation, extraction, and semantic-validation outcomes;
- identify the owning layer for representative failures;
- run and interpret the narrow tests and both evaluator types;
- explain why phrase lists or regex-per-category cannot become the project's general natural-language method;
- complete the practical ownership task in the workbook with honest assistance notes.
