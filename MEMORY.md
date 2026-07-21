# UpgradePilot Current Memory

**Last updated:** 2026-07-21  
**Purpose:** Authoritative concise project-local continuation pointer. Source, tests, commands, outputs, and the current environment remain the authority for actual implementation behavior.

## Current responsibility

M2 transition review — reconcile the existing M2 trusted-case, evidence, and deterministic-decision foundation with the newly accepted minimum-useful-generality requirements, then decide whether M2-S01 is sufficiently closed or should be explicitly redirected into the prepared M2-S02 semantic-extraction responsibility.

`plans/M2_S01_INITIAL_TRUSTED_CASE_PLAN.md` remains the active plan until that decision is made. `plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md` is prepared next work and is not yet active.

## Relevant accepted controls and decisions

- Project operation: `OPERATING_GUIDE.md`.
- Minimum useful generality: `docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`.
- Stable core requirements: `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`.
- Source/package boundary: `docs/architecture/ADR-0001-initial-python-source-layout.md`.
- Runtime-contract method: `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md`.
- Pydantic v2 remains the accepted method for strict trusted application contracts.
- Raw source data remains separate from trusted normalized structures.
- Manual fixtures and adapters may support tests or explicit supplied-data transformations, but they must not substitute for an activated automated semantic responsibility.
- A bounded model may perform activated natural-language extraction when deterministic validation protects the trusted boundary and recommendation control remains separate.

## Current implemented structure

Inspected repository history shows these source responsibilities exist:

```text
manual eight-field case input
→ build_initial_case_record(...)
→ InitialCaseRecord

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
- `src/upgradepilot/decision.py` — structured Python-support facts, deterministic decision input/result contracts, one targeted-check rule, and abstention fallback;
- corresponding tests under `tests/`.

## Material limitation now exposed

The current decision path does **not** extract semantic facts from evidence text. The normal test/application construction still manually creates `PythonSupportChange`, including `change="dropped"` and `python_version="3.8"`.

Therefore:

- the current code demonstrates evidence and deterministic-decision contracts;
- it does not yet demonstrate automated natural-language semantic extraction;
- it must not be presented as a complete source-text-to-decision flow;
- exact fixture success does not satisfy the new generality specification;
- the prepared M2-S02 responsibility exists to replace this manual semantic boundary in the normal flow.

## Newly accepted generality correction

UpgradePilot now requires:

```text
bound the supported domain, not the known fixture
```

For variable-input automated behavior, acceptance requires the real input form and representative evidence for same-meaning variation, changed meaning, negation, ambiguity, irrelevant input, untrusted embedded instructions, malformed generated output, and source traceability where applicable.

Known-answer hardcoding, exact-sentence matching, dependency/version constants, or caller-supplied interpretation are not credible semantic-extraction baselines.

## Reported implementation evidence and uncertainty

Repository commits show:

- initial evidence contracts and tests were added;
- the first deterministic decision rule and tests were added;
- the minimum-useful-generality guardrail and controlling specification were added;
- the M2-S02 known-text semantic-extraction plan was prepared.

Earlier work reported 26 passing tests before the decision tests were added. Seven decision tests were subsequently committed, implying 33 discovered tests if all are collected, but this combined count has not been reverified during the present documentation-alignment task.

Do not claim current checks pass until the relevant commands are rerun in the actual environment.

## Immediate continuation

1. Inspect the current source, tests, environment, and relevant working evidence.
2. Rerun the narrow and full checks required by M2-S01.
3. Assess M2-S01 against its actual pass condition, separating completed contract work from later evidence/decision additions.
4. Decide explicitly:
   - close M2-S01 and activate M2-S02; or
   - redirect current M2 work into M2-S02 while recording any unfinished M2-S01 obligations.
5. Before implementing Task A, finalize its semantic contract and compare only credible extraction methods: the simplest real deterministic baseline and one bounded schema-constrained LLM method.
6. Ensure the resulting normal flow derives structured meaning from known source text rather than requiring caller-created semantic facts.

## Ownership boundary

- Ali identified that the manually supplied semantic fact does not satisfy the real product responsibility and would fail under ordinary wording changes.
- Ali directed the minimum-useful-generality correction and the preparation of a real semantic-extraction responsibility.
- The recent guardrail, specification, plan, and this memory update are substantially AI-generated under Ali direction.
- Evidence, decision, LLM extraction, Pydantic, testing, and end-to-end system ownership remain limited and must be demonstrated through later explanation, modification, testing, and diagnosis.

## Career boundary

Do not update Career for ordinary project progress, tests, commits, sub-gates, or continuation changes.

Ali explicitly initiates a Career review when he wants Career to inspect UpgradePilot and update:

- coarse project state;
- capability assessment;
- workload/capacity decision;
- career role or strategy;
- durable program commitments.

## Detailed evidence

Use:

- current source and tests;
- `plans/M2_S01_INITIAL_TRUSTED_CASE_PLAN.md`;
- `plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md`;
- applicable specifications and ADRs;
- current records under `working-memory/`;
- Git history and actual command output.

Do not copy this continuation into README, `AGENTS.md`, specifications, ADRs, or Career.