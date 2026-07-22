# M2-S02 Learning Path — Closed Extraction Experiment

**Status:** M2-S02 is closed with a negative local-model adoption result.

**Purpose:** Build implementation-level understanding and ownership of the contracts that survived, the experiments that failed, the design reversals that followed, and the evidence used to reject both tested local extractors for normal runtime use.

**Implementation snapshot:** current `main` after the attributed-claim and authority correction.

This package is educational material. Source, tests, JSON artifacts, the closed plan, and working memory remain the authority for actual behavior and historical evidence.

## What changed from the earlier learning package

The earlier package described a mandatory pre-extraction risk detector and a semantic validator that rejected instruction-like and category-specific wording. That description is now obsolete for the normal path.

The final M2-S02 architecture is:

```text
accepted release-note EvidenceItem
→ untrusted candidate attributed claims
→ mechanical source grounding
→ application-assigned model_derived authority
→ deterministic bounded decision effect
```

Important final dispositions:

- both tested local model deployments were rejected for normal semantic extraction;
- the mandatory second-model risk gate was removed from normal orchestration;
- instruction/output and Python-support category regexes were removed from product grounding;
- the detector, models, evaluators, tests, and JSON outputs remain as negative experiment evidence;
- M2 continues without requiring an LLM.

## What this learning path should produce

After completing the lessons and exercises, Ali should be able to:

1. trace a release-note statement from `EvidenceItem` to an attributed decision claim and deterministic outcome;
2. distinguish source eligibility, literal grounding, independent corroboration, authority, and decision effect;
3. explain why a grounded claim is not a trusted fact or independently confirmed truth;
4. locate where `model_derived` authority and `transformation_id` are assigned and preserved;
5. explain why the risk detector and semantic regexes were first added and later rejected from normal runtime;
6. distinguish transport failures, schema failures, semantic model errors, grounding errors, authority violations, and decision-effect errors;
7. interpret the final model-evaluation metrics and intentional non-zero exit codes;
8. explain why negative evidence and design reversal are legitimate project progress;
9. make one bounded prediction-driven test change without erasing the current trust boundary.

## Depth language

| Depth | Meaning |
|---|---|
| **Introduced** | You recognize the term and its role. |
| **Operational** | You can locate and use it correctly in this repository. |
| **Implementation** | You can explain the mechanism from source/tests and diagnose representative failures. |
| **Ownership practice** | You can predict, modify, test, and defend the bounded behavior with decreasing assistance. |

This package targets **implementation depth** and begins **ownership practice**. It does not claim general natural-language understanding, production-grade model evaluation, model safety, or broad evidence corroboration.

## Study order

Do one lesson at a time. The process-history lesson is mandatory because the final architecture cannot be understood accurately by reading only the current code.

| Order | Lesson | Main outcome |
|---:|---|---|
| 1 | [`01_PIPELINE_AND_TRUST_BOUNDARIES.md`](01_PIPELINE_AND_TRUST_BOUNDARIES.md) | Trace the final attributed-claim and authority-limited path. |
| 2 | [`02_CONTRACTS_PYDANTIC_AND_ORCHESTRATION.md`](02_CONTRACTS_PYDANTIC_AND_ORCHESTRATION.md) | Understand the claim contracts, Pydantic controls, provenance, and orchestration. |
| 3 | [`03_PROCESS_FAILURES_AND_DESIGN_REVERSALS.md`](03_PROCESS_FAILURES_AND_DESIGN_REVERSALS.md) | Learn the experiment sequence, misleading intermediate results, failures, and architectural corrections. |
| 4 | [`04_LM_STUDIO_STRUCTURED_OUTPUT_AND_DIAGNOSTICS.md`](04_LM_STUDIO_STRUCTURED_OUTPUT_AND_DIAGNOSTICS.md) | Understand the retained experimental transport and why structured output did not justify adoption. |
| 5 | [`05_MECHANICAL_GROUNDING_AND_ATTRIBUTED_CLAIMS.md`](05_MECHANICAL_GROUNDING_AND_ATTRIBUTED_CLAIMS.md) | Understand what grounding proves, what it deliberately does not prove, and why semantic regexes were removed. |
| 6 | [`06_TESTING_MODEL_EVALUATION_AND_DIAGNOSIS.md`](06_TESTING_MODEL_EVALUATION_AND_DIAGNOSIS.md) | Interpret deterministic tests, model metrics, repeated failures, decision effects, and negative exits. |
| 7 | [`07_OWNERSHIP_WORKBOOK.md`](07_OWNERSHIP_WORKBOOK.md) | Demonstrate recall, prediction, diagnosis, design reasoning, and readiness for M2-S03. |

## Current source map

| Responsibility | Source |
|---|---|
| Evidence contracts | [`../../src/upgradepilot/evidence.py`](../../src/upgradepilot/evidence.py) |
| Candidate, grounded, and orchestration contracts | [`../../src/upgradepilot/extraction.py`](../../src/upgradepilot/extraction.py) |
| Mechanical grounding | [`../../src/upgradepilot/extraction_validation.py`](../../src/upgradepilot/extraction_validation.py) |
| Attributed decision claims and authority-limited policy | [`../../src/upgradepilot/decision.py`](../../src/upgradepilot/decision.py) |
| Experimental LM Studio extractor | [`../../src/upgradepilot/llm_extractor.py`](../../src/upgradepilot/llm_extractor.py) |
| Retained input-risk experiment | [`../../src/upgradepilot/input_risk.py`](../../src/upgradepilot/input_risk.py) and [`../../src/upgradepilot/llm_input_risk_detector.py`](../../src/upgradepilot/llm_input_risk_detector.py) |
| Grounding tests | [`../../tests/test_extraction_validation.py`](../../tests/test_extraction_validation.py) |
| Orchestration/decision integration | [`../../tests/test_extraction_service.py`](../../tests/test_extraction_service.py) |
| Authority and decision policy | [`../../tests/test_decision.py`](../../tests/test_decision.py) |
| Experimental transport tests | [`../../tests/test_llm_extractor.py`](../../tests/test_llm_extractor.py) and [`../../tests/test_llm_input_risk_detector.py`](../../tests/test_llm_input_risk_detector.py) |
| Decision-effect evaluator | [`../../scripts/evaluate_python_support_models.py`](../../scripts/evaluate_python_support_models.py) |
| Input-risk experiment evaluator | [`../../scripts/evaluate_input_risk_models.py`](../../scripts/evaluate_input_risk_models.py) |

## Final live evidence

Complete 14-case run:

| Deployment | Candidate/grounded correct | Decision-effect correct | Disposition |
|---|---:|---:|---|
| `gemma-4-e2b-it` | 9/14 | 11/14 | Rejected for normal extraction |
| `qwen3-4b-instruct-2507` | 8/14 | 10/14 | Rejected for normal extraction |

Focused repeated failures:

| Deployment | Clean repetitions | Decision-effect correct |
|---|---:|---:|
| `gemma-4-e2b-it` | 3/12 | 6/12 |
| `qwen3-4b-instruct-2507` | 0/12 | 4/12 |

Artifacts:

- [`../../m2-s02-attributed-claim-decision-effects.json`](../../m2-s02-attributed-claim-decision-effects.json)
- [`../../m2-s02-attributed-claim-repeated-failures.json`](../../m2-s02-attributed-claim-repeated-failures.json)
- [`../../m2-s02-input-risk-expanded-results.json`](../../m2-s02-input-risk-expanded-results.json)
- [`../../m2-s02-input-risk-qwen-failures.json`](../../m2-s02-input-risk-qwen-failures.json)

## Supporting records

- Closed responsibility: [`../../plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md`](../../plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md)
- Detailed chronological record: [`../../working-memory/2026-07-22_M2-S02_llm-extraction-session.md`](../../working-memory/2026-07-22_M2-S02_llm-extraction-session.md)
- Core claim/authority requirements: [`../../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)
- Current continuation: [`../../MEMORY.md`](../../MEMORY.md)
- Current next plan: [`../../plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md`](../../plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md)

## Useful commands

```bash
python -m unittest discover -s tests -p 'test_extraction_validation.py'
python -m unittest discover -s tests -p 'test_extraction_service.py'
python -m unittest discover -s tests -p 'test_decision.py'
python -m unittest discover -s tests
```

The live evaluators require LM Studio and are historical/experimental tools. A non-zero exit is expected when scored model cases fail; inspect the saved artifact rather than calling the run itself broken.

## Completion condition

This learning package is complete at ownership-practice entry when Ali can explain:

- why `GroundedPythonSupportClaim` is grounded but not corroborated;
- why authority is application-assigned and cannot be supplied by model JSON;
- why false favorable claims and false dropped claims have different decision effects;
- why the detector and semantic regexes were removed without deleting their evidence;
- why both local deployments were rejected despite valid JSON and some correct cases;
- how M2-S03 can proceed without an adopted model.
