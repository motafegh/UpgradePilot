# Pre-B2 M2 Implementation Archive

**Status:** Historical, read-only, non-controlling  
**Archived:** 2026-07-23  
**Exact source commit:** `e7425dcfc20f093ac10c9a903f1c4ae50a8b2638`  
**Reset decision:** [`../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)

## Purpose

This record preserves the exact location and scope of the implementation removed from the
active product and test paths before B2 responsibility freezing.

The code itself is preserved by the immutable Git commit above. It is deliberately not
copied into another importable directory because duplicate source would remain visually
active, could be imported accidentally, and could confuse new learning and design work.

To inspect one historical file without restoring it:

```text
git show e7425dcfc20f093ac10c9a903f1c4ae50a8b2638:<path>
```

Do not restore the archived tree wholesale. A current responsibility must independently
justify any later mechanism.

## Archived package configuration

- `pyproject.toml`

The archived configuration declared Pydantic and OpenAI runtime dependencies. The active
clean package does not inherit those dependencies.

## Archived active source

- `src/upgradepilot/__init__.py`
- `src/upgradepilot/case_identity.py`
- `src/upgradepilot/decision.py`
- `src/upgradepilot/evidence.py`
- `src/upgradepilot/extraction.py`
- `src/upgradepilot/extraction_validation.py`
- `src/upgradepilot/input_risk.py`
- `src/upgradepilot/llm_extractor.py`
- `src/upgradepilot/llm_input_risk_detector.py`

## Archived active tests

- `tests/test_case_identity.py`
- `tests/test_decision.py`
- `tests/test_evidence.py`
- `tests/test_extraction_service.py`
- `tests/test_extraction_validation.py`
- `tests/test_input_risk.py`
- `tests/test_llm_extractor.py`
- `tests/test_llm_input_risk_detector.py`
- `tests/test_model_evaluator.py`

## Archived scripts

- `scripts/evaluate_input_risk_models.py`
- `scripts/evaluate_python_support_models.py`
- `scripts/run_screened_extraction_demo.py`

## Archived generated evaluation outputs

- `gemma-4-e2b-results.json`
- `m2-s02-attributed-claim-decision-effects.json`
- `m2-s02-attributed-claim-repeated-failures.json`
- `m2-s02-input-risk-expanded-results.json`
- `m2-s02-input-risk-gemma-768-diagnostic.json`
- `m2-s02-input-risk-gemma-diagnostic.json`
- `m2-s02-input-risk-qwen-failures.json`
- `m2-s02-input-risk-results.json`
- `m2-s02-seed-0-results.json`
- `qwen3-4b-results.json`
- `small-model-results.json`

## Related historical records retained in the active documentation tree

These remain available as learning and history, but they do not control new source:

- `plans/M2_S01_INITIAL_TRUSTED_CASE_PLAN.md`
- `plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md`
- `plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md`
- `working-memory/2026-07-20_M2-S01_case-identity-implementation-start.md`
- `working-memory/2026-07-20_M2-S01_case-identity-normalization.md`
- `working-memory/2026-07-22_M2-S02_llm-extraction-session.md`
- `learning/m2-s02/`
- `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md`

## Authority and reuse limits

This archive does not authorize:

- importing archived modules;
- copying old classes into B2;
- treating historical tests as current coverage;
- retaining Pydantic or OpenAI because the old code used them;
- restoring the old M2 decision rule;
- claiming that archived behavior remains supported.

It may be consulted only when a current task identifies a specific comparison question.
The active source, active tests, accepted B1 responsibility, and later B2 plan control all
new implementation work.