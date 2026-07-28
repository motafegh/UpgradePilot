# B2 LM Studio Server and Instructor Assessment

**Date:** 2026-07-28  
**Operation:** Record current LM Studio server evidence and assess Instructor as a bounded structured-extraction adapter  
**Parent plan:** [`../plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md`](../plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md)  
**Main re-evaluation record:** [`2026-07-28_B2-local-lm-studio-semantic-reevaluation.md`](2026-07-28_B2-local-lm-studio-semantic-reevaluation.md)  
**Result classification:** Server endpoint partially inventoried; Instructor admitted as an experiment candidate, not selected or added to the active package

## 1. User-provided LM Studio server evidence

At `2026-07-28 21:10:46`, the LM Studio desktop application reported:

- HTTP server started successfully;
- listening port: `12345`;
- just-in-time model loading active;
- LM Studio native model and chat endpoints available;
- OpenAI-compatible endpoints available, including:
  - `GET /v1/models`;
  - `POST /v1/responses`;
  - `POST /v1/chat/completions`;
  - `POST /v1/completions`;
  - `POST /v1/embeddings`;
- server logs stored under `C:\Users\lenovo\.cache\lm-studio\server-logs`.

This establishes that the required OpenAI-compatible chat-completion route is enabled on the Windows host.

It does not yet establish:

- the LM Studio application or CLI version;
- whether the server is loopback-only or exposed on another interface;
- whether authentication is enabled;
- which GGUF models are downloaded;
- which model, if any, is currently loaded;
- model quantizations, sizes, context limits, or load configuration;
- GPU free memory and competing processes;
- WSL2 reachability through `127.0.0.1` or the Windows gateway;
- structured-output behavior for any candidate deployment.

## 2. Instructor definition

Instructor is a Python structured-output library built around Pydantic models. For this experiment it could wrap an OpenAI-compatible client pointed at LM Studio and use native JSON-Schema mode.

Potential responsibilities:

```text
Pydantic response model
→ JSON Schema request construction
→ LM Studio /v1/chat/completions
→ typed Pydantic parsing and validation
→ optional validation context
→ optional retries and hooks
```

Instructor is not the model, inference server, semantic evaluator, grounding authority, or decision engine.

## 3. What Instructor can contribute

Instructor may reduce custom adapter code by providing:

- Pydantic-model-to-schema generation;
- typed parsed results;
- strict field and model validation;
- validation context for mechanical source-span or exact-quote checks;
- access to raw completion responses;
- hooks for request, response, parse-error, and retry diagnostics;
- configurable re-asking when validation fails.

For LM Studio, the relevant candidate configuration is conceptually:

```text
OpenAI-compatible client(base_url=http://<host>:12345/v1)
+ Instructor JSON_SCHEMA mode
+ Pydantic UpstreamClaimResult
```

The exact API and package versions must be pinned only after a smoke experiment proves compatibility with the installed LM Studio deployment.

## 4. What Instructor cannot establish

Instructor does not solve the historical UpgradePilot failure by itself.

The previous experiment already used:

```text
native JSON Schema
+ Pydantic validation
+ source quotation/grounding
+ deterministic authority limits
```

and still observed schema-valid, grounded-looking, semantically wrong claims that changed downstream actions.

Therefore:

```text
Pydantic-valid output
≠ semantically correct attributed claim

quote exists in source
≠ quote was interpreted in the correct speech-act context

retry succeeded
≠ first attempt was reliable

Instructor returned a model
≠ product adoption is justified
```

The model deployment and evaluation evidence remain decisive.

## 5. Retry policy for the scored experiment

Instructor can re-ask the model after a Pydantic validation failure by adding validation feedback to the next prompt. That may be useful operationally later, but it changes the inference attempt and can conceal first-attempt reliability.

For the initial scored experiment:

- use `max_retries=0`;
- record the first raw completion and validation result;
- classify transport, schema, grounding, and semantic failures separately;
- do not allow a corrected retry to overwrite the failed first attempt;
- consider retries only as a separate measured recovery experiment after first-pass scoring.

A later retry experiment must record:

- every attempt;
- validation feedback sent back to the model;
- added latency and tokens;
- whether the retry corrected structure only or changed semantic meaning;
- final downstream decision effect.

## 6. Grounding policy

Pydantic validation context may mechanically verify that a quote or span belongs to the exact release body. This is useful but insufficient.

UpgradePilot must preserve two separate checks:

1. **mechanical grounding** — the referenced span exists in the admitted source;
2. **semantic correctness** — the normalized claim accurately represents what the source says in context.

Instructor can assist with the first. The frozen semantic corpus and scored oracle are required for the second.

## 7. Dependency and architecture disposition

Instructor is admitted as a credible experiment candidate alongside:

- direct `requests` plus explicit JSON Schema and application validation;
- OpenAI Python client plus explicit Pydantic validation;
- LM Studio Python SDK.

Current disposition:

- do not add Instructor, Pydantic, or OpenAI-client dependencies to the active package yet;
- prototype only after model inventory and WSL2 transport are confirmed;
- compare adapter code, diagnostics, dependency cost, retry behavior, and failure transparency;
- reject LangChain/agent orchestration for this bounded extraction responsibility;
- select an adapter only after the smoke proof and before the frozen scored run;
- treat adapter selection as separate from model adoption.

The leading hypothesis is that Instructor may be useful for the experiment harness and possibly the final bounded adapter, but it cannot improve a weak model's semantic accuracy merely by validating its output.

## 8. Remaining environment commands

Run from Windows PowerShell:

```powershell
lms --version
lms server status --json --quiet
lms ls --llm --json | Out-File -Encoding utf8 lmstudio-models.json
lms ps --json | Out-File -Encoding utf8 lmstudio-loaded.json
nvidia-smi --query-gpu=name,driver_version,memory.total,memory.used,memory.free --format=csv
nvidia-smi
```

Run from WSL2:

```bash
ip route show default
cat /etc/resolv.conf | grep '^nameserver'

curl -fsS http://127.0.0.1:12345/v1/models \
  | python3 -m json.tool

# Only if localhost fails:
WINDOWS_HOST="$(ip route show default | awk '/default/ {print $3; exit}')"
curl -fsS "http://${WINDOWS_HOST}:12345/v1/models" \
  | python3 -m json.tool

python3 --version
python3 -c 'import sys; print(sys.executable)'
```

Do not enable CORS for this path. Preserve the exact connection error before changing server bind settings.

## 9. Exact continuation

After the remaining inventory is supplied:

1. classify downloaded models;
2. identify at most three eligible general instruct candidates;
3. run memory estimates before loading;
4. choose one candidate and one stable load configuration;
5. compare a minimal direct adapter with an Instructor `JSON_SCHEMA` adapter in a smoke harness;
6. keep retries disabled for first-pass measurement;
7. freeze the broader semantic corpus and expected decision effects before scored runs.

No product semantic code, decision behavior, or runtime dependency is approved by this record.
