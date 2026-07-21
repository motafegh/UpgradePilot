# UpgradePilot Current Memory

**Last updated:** 2026-07-22  
**Purpose:** Authoritative concise project-local continuation pointer. Source, tests, commands, outputs, and the current environment remain the authority for actual implementation behavior.

## Current responsibility

M2-S02 — known-text semantic extraction under [`plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md`](plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md).

The current working session is [`working-memory/2026-07-22_M2-S02_llm-extraction-session.md`](working-memory/2026-07-22_M2-S02_llm-extraction-session.md).

Ali accepted M2-S01 as the completed trusted-contract foundation and activated M2-S02 on 2026-07-21. M2-S01 remains historical foundation evidence; it is no longer the current plan.

## Relevant accepted controls and decisions

- Project operation: `OPERATING_GUIDE.md`.
- Minimum useful generality: `docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`.
- Stable core requirements: `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`.
- Source/package boundary: `docs/architecture/ADR-0001-initial-python-source-layout.md`.
- Runtime-contract method: `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md`.
- Pydantic v2 remains the accepted method for strict trusted application contracts.
- Raw source text, LLM candidate meaning, trusted facts, and decision results remain distinct.
- Manual fixtures may test validation but must not substitute for activated semantic extraction.
- A bounded local model may extract candidate meaning while deterministic Python code controls trust and the existing policy controls recommendation.

## Completed foundation

M2-S01 established:

```text
manual eight-field case input
→ build_initial_case_record(...)
→ InitialCaseRecord
```

Existing source also provides:

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

The current decision path still requires callers or tests to manually create `PythonSupportChange`.

M2-S02 must replace that manual boundary with:

```text
accepted release-note evidence
→ local LM Studio model
→ untrusted structured candidate facts
→ deterministic validation and grounding
→ trusted facts or explicit unresolved/rejected result
→ existing deterministic decision rule
```

The first supported semantic category is Python runtime-support additions and removals in dependency release-note text.

## Accepted session method direction

Reuse the proven Sentinel LM Studio connection pattern in a smaller UpgradePilot-specific form:

- LM Studio local OpenAI-compatible endpoint;
- environment-backed base URL, model ID, timeout, and output limit;
- one bounded instruct/chat model;
- temperature zero or effectively deterministic;
- structured candidate output;
- deterministic validation before trust;
- no LangChain, LangGraph, agents, RAG, embeddings, or broad model-routing framework.

Initial credible existing-model candidates include `gemma-4-e2b-it` and `qwen2.5-coder-7b-instruct`, but no model is selected until the actual LM Studio `/v1/models` response and a small discriminating comparison are recorded.

## Immediate continuation

Follow `working-memory/2026-07-22_M2-S02_llm-extraction-session.md`:

1. inspect current source, tests, dependencies, and the manual semantic boundary;
2. rerun the current repository checks before changing behavior;
3. verify the reachable LM Studio endpoint and list exact available model IDs;
4. freeze the first candidate-output contract;
5. implement and test deterministic validation using candidate fixtures;
6. implement the smallest direct LM Studio client;
7. compare credible existing local models on the bounded proof set;
8. add orchestration and connect trusted extracted facts to `evaluate_decision(...)`;
9. run the real Soup Sieve text through the path without caller-created semantic facts;
10. record commands, outputs, failures, repairs, model choice, assistance, and limitations.

## Evidence and uncertainty

The session plan is accepted, but no LM Studio endpoint, available model list, extraction dependency, selected model, candidate contract, validator, or real model call has yet been verified in the UpgradePilot runtime.

Earlier work reported test results, but the complete current suite has not been rerun during this session-planning task. Do not claim current checks pass until commands are rerun in the actual environment.

## Ownership boundary

- Ali identified that manually supplied semantic facts do not satisfy the real product responsibility under ordinary wording variation.
- Ali directed the minimum-useful-generality correction, accepted M2-S01 as the contract foundation, activated M2-S02, and selected the local LM Studio direction for the first implementation session.
- The current session plan and continuation update are substantially AI-generated under Ali direction.
- LM Studio integration, structured extraction, deterministic validation, testing, and end-to-end ownership remain to be demonstrated through explanation, modification, execution, and diagnosis.

## Career boundary

Do not update Career for ordinary project progress, tests, commits, sub-gates, or continuation changes.

Ali explicitly initiates a Career review when he wants Career to inspect UpgradePilot and update coarse project state, capability assessment, workload/capacity, career role, strategy, or durable program commitments.

## Detailed evidence

Use:

- current source and tests;
- `plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md`;
- `working-memory/2026-07-22_M2-S02_llm-extraction-session.md`;
- completed foundation plan `plans/M2_S01_INITIAL_TRUSTED_CASE_PLAN.md`;
- applicable specifications and ADRs;
- Git history and actual command output.

Do not copy this continuation into README, `AGENTS.md`, specifications, ADRs, or Career.
