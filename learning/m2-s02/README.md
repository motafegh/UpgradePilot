# M2-S02 Learning Path

**Purpose:** Build Ali's confidence and real ownership of the semantic-extraction implementation before further model or method decisions.

**Implementation snapshot:** 2026-07-22 current `main` source and tests.

This package is educational material, not a second specification, plan, progress tracker, or claim of mastery. The authoritative implementation remains the linked source, tests, commands, and runtime evidence.

## What this learning path should produce

After completing the lessons and exercises, Ali should be able to:

1. trace one release-note sentence from `EvidenceItem` to `DecisionResult`;
2. distinguish raw evidence, model candidates, accepted extracted facts, and decision facts;
3. explain why JSON Schema and Pydantic structure do not establish semantic correctness;
4. locate and explain the LM Studio request, response parsing, diagnostics, and failure paths;
5. walk through every deterministic validation gate in execution order;
6. distinguish unit tests, orchestration tests, and live model evaluation;
7. diagnose whether a failure belongs to transport, schema parsing, model semantics, validation, orchestration, or decision policy;
8. make one bounded test or behavior change with a correct prediction and explanation.

## Depth language used here

Do not reduce learning to completed/not-completed.

| Depth | Meaning |
|---|---|
| **Introduced** | You recognize the term and its role. |
| **Operational** | You can use or inspect it correctly in the current repository. |
| **Implementation** | You can explain the mechanism from the code and diagnose representative failures. |
| **Ownership practice** | You can predict, test, modify, and defend the bounded behavior with decreasing assistance. |

This package targets **implementation depth** for the current M2-S02 path and begins **ownership practice**. It does not claim broad LLM security, general NLP expertise, or production readiness.

## Study order

Do one lesson at a time. Do not read all files passively in one sitting.

| Order | Lesson | Main outcome |
|---:|---|---|
| 1 | [`01_PIPELINE_AND_TRUST_BOUNDARIES.md`](01_PIPELINE_AND_TRUST_BOUNDARIES.md) | Trace the complete product path and its trust transitions. |
| 2 | [`02_CONTRACTS_PYDANTIC_AND_ORCHESTRATION.md`](02_CONTRACTS_PYDANTIC_AND_ORCHESTRATION.md) | Understand the Python/Pydantic contracts and service composition. |
| 3 | [`03_LM_STUDIO_STRUCTURED_OUTPUT_AND_DIAGNOSTICS.md`](03_LM_STUDIO_STRUCTURED_OUTPUT_AND_DIAGNOSTICS.md) | Understand the local model transport and why structured output remains untrusted. |
| 4 | [`04_DETERMINISTIC_VALIDATION_AND_PROMPT_INJECTION.md`](04_DETERMINISTIC_VALIDATION_AND_PROMPT_INJECTION.md) | Understand the admission controls, failure modes, and security boundary. |
| 5 | [`05_TESTING_MODEL_EVALUATION_AND_DIAGNOSIS.md`](05_TESTING_MODEL_EVALUATION_AND_DIAGNOSIS.md) | Understand what each test layer proves and how evaluation metrics differ. |
| 6 | [`06_OWNERSHIP_WORKBOOK.md`](06_OWNERSHIP_WORKBOOK.md) | Demonstrate explanation, prediction, diagnosis, and bounded modification ability. |

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
| Candidate/trusted extraction contracts and orchestration | [`../../src/upgradepilot/extraction.py`](../../src/upgradepilot/extraction.py) |
| LM Studio client and diagnostics | [`../../src/upgradepilot/llm_extractor.py`](../../src/upgradepilot/llm_extractor.py) |
| Deterministic extraction validation | [`../../src/upgradepilot/extraction_validation.py`](../../src/upgradepilot/extraction_validation.py) |
| Decision contracts and policy | [`../../src/upgradepilot/decision.py`](../../src/upgradepilot/decision.py) |
| Validation tests | [`../../tests/test_extraction_validation.py`](../../tests/test_extraction_validation.py) |
| LM Studio boundary tests | [`../../tests/test_llm_extractor.py`](../../tests/test_llm_extractor.py) |
| Orchestration and decision integration tests | [`../../tests/test_extraction_service.py`](../../tests/test_extraction_service.py) |
| Live model evaluator | [`../../scripts/evaluate_python_support_models.py`](../../scripts/evaluate_python_support_models.py) |

## Supporting project records

- Current responsibility: [`../../plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md`](../../plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md)
- Current continuation: [`../../MEMORY.md`](../../MEMORY.md)
- Detailed implementation and evaluation evidence: [`../../working-memory/2026-07-22_M2-S02_llm-extraction-session.md`](../../working-memory/2026-07-22_M2-S02_llm-extraction-session.md)
- Learning method: [`../../OPERATING_GUIDE.md`](../../OPERATING_GUIDE.md)

## Useful commands

Run from the repository root in the existing project environment.

```bash
# One deterministic validator test file
python -m unittest discover -s tests -p 'test_extraction_validation.py'

# One LM Studio boundary test file; this uses fake clients, not a live model
python -m unittest discover -s tests -p 'test_llm_extractor.py'

# Orchestration into the deterministic decision policy
python -m unittest discover -s tests -p 'test_extraction_service.py'

# Complete repository unit test suite
python -m unittest discover -s tests
```

The live evaluator is deliberately separate because it requires LM Studio and real local models:

```bash
python scripts/evaluate_python_support_models.py \
  --models qwen3-4b-instruct-2507 \
  --repetitions 1 \
  --max-tokens 512
```

Do not interpret a command as successful merely because it ran. Each lesson states what its checks do and do not prove.

## Stop condition before resuming implementation

Resume the unresolved model/method decision only after Ali can:

- explain the complete path without reading a prepared answer;
- predict representative accepted, rejected, unresolved, and request-failure outcomes;
- identify the owning layer for representative failures;
- run and interpret the narrow tests;
- complete the practical ownership task in the workbook with honest assistance notes.
