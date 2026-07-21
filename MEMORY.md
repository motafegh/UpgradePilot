# UpgradePilot Current Memory

**Last updated:** 2026-07-21  
**Purpose:** Authoritative concise project-local continuation pointer. Source, tests, commands, outputs, and the current environment remain the authority for actual implementation behavior.

## Current responsibility

M2-S02 — known-text semantic extraction under [`plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md`](plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md).

Ali accepted M2-S01 as the completed trusted-contract foundation and activated M2-S02 on 2026-07-21. M2-S01 remains historical foundation evidence; it is no longer the current plan. This transition does not claim that M2 is complete or that an extraction method has already been selected or implemented.

## Relevant accepted controls and decisions

- Project operation: `OPERATING_GUIDE.md`.
- Minimum useful generality: `docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`.
- Stable core requirements: `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`.
- Source/package boundary: `docs/architecture/ADR-0001-initial-python-source-layout.md`.
- Runtime-contract method: `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md`.
- Pydantic v2 remains the accepted method for strict trusted application contracts.
- Raw source text, candidate extracted meaning, trusted facts, and decision results must remain distinct.
- Manual fixtures and adapters may support tests or supplied-data transformations, but they must not substitute for activated semantic extraction.
- A bounded model may perform natural-language extraction when deterministic validation protects the trusted boundary and recommendation control remains separate.

## Completed foundation

M2-S01 established the accepted contract foundation:

```text
manual eight-field case input
→ build_initial_case_record(...)
→ InitialCaseRecord
```

Existing source responsibilities also include:

```text
InitialCaseRecord + normalized evidence items
→ EvidenceSet

EvidenceSet + caller-created PythonSupportChange facts
→ DecisionInput
→ evaluate_decision(...)
→ DecisionResult
```

Current modules include:

- `src/upgradepilot/case_identity.py` — trusted initial case transformation;
- `src/upgradepilot/evidence.py` — bounded accepted/missing evidence contracts;
- `src/upgradepilot/decision.py` — structured Python-support facts, deterministic decision contracts, one targeted-check rule, and abstention fallback;
- corresponding tests under `tests/`.

## Active semantic gap

The current decision path still requires callers or tests to manually create `PythonSupportChange`, including values such as `change="dropped"` and `python_version="3.8"`.

M2-S02 must replace that manual semantic boundary with:

```text
known release-note text
→ bounded semantic extraction
→ candidate structured facts
→ deterministic validation and grounding
→ accepted facts or explicit unresolved/rejected state
→ deterministic decision input
→ traceable decision result
```

The first supported semantic category is Python runtime-support change in dependency release-note text.

## Current method state

No extraction method is accepted yet.

The active plan requires a bounded comparison between:

1. the simplest credible deterministic extraction baseline;
2. one schema-constrained LLM extraction method;
3. a hybrid only if evidence demonstrates additional value.

Exact sentence matching, dependency/version hardcoding, encoded expected answers, and caller-supplied `PythonSupportChange` objects are not credible extraction baselines.

## Immediate continuation

1. Inspect the current source, tests, environment, and relevant working evidence.
2. Finalize Task A's semantic contract:
   - candidate output;
   - trusted output;
   - unresolved/rejected behavior;
   - source quote/span grounding;
   - transformation identity;
   - decision-layer boundary.
3. Define the smallest discriminating proof set for paraphrases, changed meaning, negation, ambiguity, irrelevant text, untrusted embedded instructions, and malformed output.
4. Compare the credible deterministic baseline with one bounded schema-constrained LLM method.
5. Select, reject, defer, or combine methods based on observed evidence.
6. Implement the smallest complete path from known source text to the existing deterministic decision layer.

## Evidence and uncertainty

Repository history shows that evidence contracts, deterministic decision code, tests, the minimum-useful-generality specification, and the M2-S02 plan exist.

Earlier work reported test results, but the complete current suite has not been rerun during this plan-activation task. Do not claim current checks pass until commands are rerun in the actual environment.

## Ownership boundary

- Ali identified that manually supplied semantic facts do not satisfy the real product responsibility under ordinary wording variation.
- Ali directed the minimum-useful-generality correction, accepted M2-S01 as the contract foundation, and activated M2-S02.
- The recent guardrail, specification, plans, and continuation updates are substantially AI-generated under Ali direction.
- Evidence, decision, LLM extraction, Pydantic, testing, and end-to-end system ownership remain limited and require later explanation, modification, testing, and diagnosis.

## Career boundary

Do not update Career for ordinary project progress, tests, commits, sub-gates, or continuation changes.

Ali explicitly initiates a Career review when he wants Career to inspect UpgradePilot and update coarse project state, capability assessment, workload/capacity, career role, strategy, or durable program commitments.

## Detailed evidence

Use:

- current source and tests;
- `plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md`;
- completed foundation plan `plans/M2_S01_INITIAL_TRUSTED_CASE_PLAN.md`;
- applicable specifications and ADRs;
- current records under `working-memory/`;
- Git history and actual command output.

Do not copy this continuation into README, `AGENTS.md`, specifications, ADRs, or Career.