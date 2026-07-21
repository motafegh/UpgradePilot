# M2-S02 LLM Extraction Session

**Status:** Current working session  
**Date:** 2026-07-22  
**Owner:** Ali Rajabi  
**Controlling plan:** `../plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md`

## Session outcome

Establish the first real known-text semantic-extraction path for Python runtime-support changes using Ali's existing LM Studio setup, while preserving a deterministic trusted boundary and the existing deterministic recommendation policy.

The intended path is:

```text
accepted release-note evidence
→ local LM Studio model
→ untrusted structured candidate facts
→ deterministic validation and grounding
→ trusted Python-support facts or explicit unresolved/rejected result
→ existing deterministic decision rule
```

This session does not need to complete all of M2-S02. It should stop when the first honest implementation increment is working, tested, and understood.

## Accepted method direction

Use the Sentinel-proven local connection pattern in a smaller UpgradePilot-specific form:

- LM Studio provides the local OpenAI-compatible endpoint;
- configuration comes from environment variables rather than hardcoded host or model values;
- one bounded chat/instruct model performs natural-language extraction;
- temperature is zero or effectively deterministic;
- timeout and output-token limits are explicit;
- model output remains untrusted until deterministic validation succeeds;
- the LLM does not make the final recommendation;
- no LangChain, LangGraph, agents, RAG, embeddings, or model-routing framework is added for this responsibility.

Initial model candidates should come from Ali's existing local models. `gemma-4-e2b-it` and `qwen2.5-coder-7b-instruct` are credible first candidates based on Sentinel history, but no model is selected until the local server reports the currently available models and a small extraction comparison is run.

## Required understanding for this session

Ali should be able to explain, at the depth needed for implementation:

1. why raw evidence text, LLM candidate output, trusted extracted facts, and final decisions are separate states;
2. why the supporting quote is returned by the model and checked against the original evidence;
3. what JSON Schema or another structured-output constraint can guarantee and what it cannot;
4. why schema validity does not prove semantic correctness;
5. why timeout, model identity, base URL, and output limit are runtime configuration;
6. why the local model may extract candidate meaning while Python code controls trust and the existing policy controls recommendation.

## Execution sequence

### 1. Inspect current truth

- inspect `pyproject.toml`, `src/upgradepilot/evidence.py`, `src/upgradepilot/decision.py`, existing tests, and the active M2-S02 plan;
- confirm the current manual `PythonSupportChange` boundary that the new normal flow must replace;
- rerun the current repository tests before changing behavior.

### 2. Verify the local LM Studio boundary

- start or confirm the LM Studio local server;
- determine the reachable base URL from the actual UpgradePilot runtime environment, including WSL/Windows networking if applicable;
- query `/v1/models` and record the exact available model IDs;
- make one minimal health request with an explicit timeout;
- do not download another model until the existing models are inspected.

### 3. Freeze the first candidate contract

The first supported candidate fact remains bounded to:

```text
change: added | dropped
python_version: explicit major.minor value
source_quote: exact supporting text copied from the supplied evidence
```

The extraction response must also represent no supported fact and relevant-but-unresolved meaning without inventing a version or change.

### 4. Implement the deterministic validator first

Using manually constructed candidate outputs only as validator fixtures, implement and test:

- accepted upstream-release-note evidence requirement;
- strict candidate schema;
- allowed change values;
- explicit Python major.minor value;
- source quote exists in original evidence text;
- claimed Python version appears in the supporting quote;
- evidence identity is attached by trusted application code, not selected by the model;
- duplicate or contradictory candidates remain rejected or unresolved;
- malformed or ungrounded output cannot become a trusted fact.

Manual candidates are allowed here because they test the validator. They must not be presented as completing semantic extraction.

### 5. Implement the smallest LM Studio client

Add one provider boundary that:

- reads base URL, model ID, timeout, and optional output limit from environment-backed configuration;
- calls the LM Studio OpenAI-compatible endpoint directly through the smallest justified client dependency;
- requests the frozen structured candidate response;
- returns model output as untrusted candidate data;
- exposes connection, timeout, malformed response, and unavailable-model failures explicitly.

Prefer the ordinary OpenAI-compatible Python client over Sentinel's LangChain stack unless direct client evidence shows a blocking limitation.

### 6. Compare existing local models

Run the smallest discriminating proof set against credible existing models:

- same meaning with different wording;
- added versus dropped support;
- different Python version;
- continued support;
- deprecation;
- possible future removal;
- ambiguous support change;
- irrelevant text;
- multiple explicit facts;
- embedded instruction attempting to invent a fact.

Record correctness, false facts, unresolved behavior, structured-output success, latency, and material runtime constraints. Select one model for the first implementation based on evidence rather than model reputation alone.

### 7. Add orchestration and decision integration

Implement the smallest path that:

```text
EvidenceItem
→ LLM candidate extraction
→ deterministic validator
→ trusted PythonSupportChange-compatible fact
→ existing evaluate_decision(...)
```

The normal executable example must not require a caller to manually construct the semantic support-change fact.

### 8. Validate and stop

Run narrow tests first, then the complete current suite and applicable compile/package checks. Stop this session when:

- one real model produces candidate output from known text;
- invalid or hallucinated output is blocked by deterministic validation;
- at least the real Soup Sieve evidence reaches the existing decision path without manual fact construction;
- representative changed-meaning cases do not collapse into the target fact;
- actual commands, outputs, model identity, latency, failures, assistance, and remaining limitations are recorded;
- Ali can locate and explain the client, candidate contract, validator, trusted fact, orchestration, decision integration, and tests.

## Likely source shape

Use the fewest readable modules. The current likely responsibilities are:

```text
extraction.py
  candidate/trusted extraction contracts and orchestration

llm_extractor.py
  LM Studio configuration and model call

extraction_validation.py
  deterministic grounding and trust checks
```

This is a working hypothesis, not a requirement to create three files. Combine responsibilities when that produces a clearer, smaller implementation without mixing provider code, trust validation, and recommendation policy.

## Forbidden expansion

Do not add during this session merely for architectural appearance:

- LangChain or LangGraph;
- autonomous agents or tool-selection loops;
- RAG, embeddings, vector databases, or graphs;
- live GitHub, PyPI, or web acquisition;
- model fine-tuning or a training corpus;
- multiple-provider abstraction;
- cloud deployment, persistence, queues, services, or workflow engines;
- LLM-controlled final recommendations;
- broad semantic routing across every release-note category;
- a universal compatibility ontology.

## Evidence discipline

Update this record with material implementation evidence only:

- exact model IDs exposed by LM Studio;
- selected base URL shape without secrets;
- commands and relevant outputs;
- method comparison results;
- source/test commits;
- observed failures and repairs;
- Ali-directed decisions and explanations;
- assistance and remaining limitations.

Do not turn this file into a second specification, general progress tracker, or repeated narrative of routine edits.
