# B2 Local LM Studio Semantic Re-evaluation Working Record

**Date opened:** 2026-07-28  
**Operation:** Gather current local-model, LM Studio, historical, hardware, transport, and evaluation evidence before any B2 semantic implementation  
**Controlling parent plan:** [`../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md)  
**Bounded re-evaluation plan:** [`../plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md`](../plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md)  
**Semantic boundary proposal:** [`2026-07-28_B2-upstream-semantic-boundary.md`](2026-07-28_B2-upstream-semantic-boundary.md)  
**Starting repository revision:** `001a0ef746130878aee4be64d83a456fa7c09c26`  
**Local result classification:** Investigation opened; prior negative evidence and current method constraints gathered; environment inventory pending; no product method approved or implemented

## Objective

Preserve the evidence needed to decide whether Ali's current LM Studio and local GGUF environment can support UpgradePilot's first bounded upstream-claim extractor.

This record must separate:

```text
local endpoint works
≠ JSON Schema works
≠ semantic claims are correct
≠ source grounding is valid
≠ downstream decision effects are acceptable
≠ product adoption is justified
```

## Current user environment known before capture

User-reported facts:

- LM Studio is installed on the user's system;
- local GGUF models are already downloaded;
- hardware includes an NVIDIA RTX 3070 Laptop GPU with 8 GB VRAM;
- prior Sentinel work used LM Studio from the `agents` module;
- the active UpgradePilot development environment is WSL2/Python 3.12.

Exact current LM Studio version, server port/bind, downloaded model inventory, quantizations, loaded configuration, free VRAM, and WSL2 base URL remain to be captured.

## Existing UpgradePilot evidence that controls this re-evaluation

### Historical experiment

At immutable revision `e7425dcfc20f093ac10c9a903f1c4ae50a8b2638`, UpgradePilot already implemented and evaluated a local LM Studio extractor using:

```text
OpenAI-compatible /v1/chat/completions
+ response_format=json_schema
+ temperature=0
+ seed=0
+ bounded timeout and max_tokens
+ strict Pydantic parsing
+ source quotation and grounding
+ model-derived authority
+ deterministic decision-effect evaluation
```

Observed deployments:

| Deployment | Quantization | Clean candidate/grounded | Correct decision effect | Average latency |
|---|---|---:|---:|---:|
| `gemma-4-e2b-it` | Q4_K_M | 9/14 | 11/14 | 3.163 s |
| `qwen3-4b-instruct-2507` | Q6_K | 8/14 | 10/14 | 0.749 s |

Both produced repeated material false dropped-support claims. The semantic failures persisted after transport, token-budget, schema, and grounding behavior were separated and diagnosed. Both deployments were rejected for normal extraction.

### Durable lessons retained

- JSON Schema controls representation, not meaning.
- `finish_reason="stop"` rules out output truncation for that response but not semantic error.
- literal source quotation does not prove correct interpretation of the source's speech act.
- phrase- and fixture-shaped regex repairs are not an accepted semantic architecture.
- a second local-model input-risk gate added latency and still produced false positives and false negatives.
- model-derived claims must have bounded downstream effects.
- absence of an extracted caution must not become evidence of safety.
- negative model evaluation is a valid engineering result.

## Sentinel comparison inspected

Sentinel's `agents/src/llm/client.py` provides useful operational patterns:

- environment-configured `LM_STUDIO_BASE_URL` rather than a hardcoded WSL2 gateway;
- non-empty placeholder API key for OpenAI-compatible clients;
- explicit request timeout to avoid indefinite hangs during load/OOM conditions;
- centralized model identifiers and task routing;
- temperature `0.0` for deterministic-style security tasks;
- measured token-cap tuning and latency observations on the same RTX 3070 class;
- direct connection smoke checks.

Sentinel also exposes patterns that UpgradePilot should not copy as its trusted semantic boundary:

- prompting for JSON without an enforced JSON Schema in the inspected debate path;
- stripping markdown fences after the response;
- permissive `json.loads` and value fallback;
- silent rule-based fallback after semantic/parse failure;
- multi-role debate and LangChain orchestration unnecessary for one bounded extraction task.

Sentinel is therefore an operational reference, not an architecture authority for UpgradePilot.

## Current official LM Studio capabilities gathered

Current LM Studio documentation establishes:

- OpenAI-compatible `/v1/chat/completions` accepts `response_format` with a JSON Schema;
- for GGUF models, structured output uses llama.cpp grammar-based sampling;
- the JSON object is returned as a string in `choices[0].message.content` and still requires parsing and application validation;
- not all models are capable of reliable structured output, especially models below approximately 7B parameters;
- `GET /v1/models` lists models visible to the server;
- `lms ls --json` lists downloaded models;
- `lms ps --json` lists loaded models;
- `lms load --estimate-only`, `--context-length`, and `--gpu` support deployment sizing;
- `lms log stream --source model --filter input,output --json` exposes model I/O for diagnosis;
- `lms log stream --source model --filter output --stats` exposes performance statistics;
- server binding beyond `127.0.0.1` and enabling CORS expand exposure and should not be enabled without need and protection.

## Current method conclusion

Using an LLM is approved as an experiment direction, not yet as adopted product behavior.

The leading semantic architecture remains:

```text
exact authoritative GitHub Release body
→ local bounded structured extraction
→ deterministic schema validation
→ deterministic source-span grounding
→ model-derived attributed claims
→ deterministic evidence sufficiency
→ deterministic maintainer action
```

The current transport preference for the experiment is direct HTTP with the active `requests` dependency unless comparison shows that the OpenAI client or LM Studio SDK provides necessary value. LangChain and agent frameworks are not justified for this responsibility.

## Environment capture requested from Ali

Run the following from **Windows PowerShell**, with LM Studio open. These commands are read-only.

```powershell
# 1. CLI and server identity
lms --version
lms server status --json --quiet

# 2. Downloaded and loaded model inventories
lms ls --llm --json | Out-File -Encoding utf8 lmstudio-models.json
lms ps --json | Out-File -Encoding utf8 lmstudio-loaded.json

# 3. GPU identity and current memory/process state
nvidia-smi --query-gpu=name,driver_version,memory.total,memory.used,memory.free --format=csv
nvidia-smi
```

If `lms --version` is unsupported, run:

```powershell
lms
```

and preserve the first lines containing the CLI version.

Run the following from **WSL2**, replacing `<PORT>` with the port reported by `lms server status`:

```bash
# 4. Record the Windows host/gateway visible from WSL2
ip route show default
cat /etc/resolv.conf | grep '^nameserver'

# 5. Test localhost first; this may work with mirrored networking
curl -fsS http://127.0.0.1:<PORT>/v1/models | python3 -m json.tool

# 6. If localhost fails, test the WSL2 default gateway
WINDOWS_HOST="$(ip route show default | awk '/default/ {print $3; exit}')"
curl -fsS "http://${WINDOWS_HOST}:<PORT>/v1/models" | python3 -m json.tool

# 7. Record the active project runtime
python3 --version
python3 -c 'import sys; print(sys.executable)'
```

Do not enable CORS for this Python/WSL2 path. If WSL2 cannot reach the server, record the failure before changing LM Studio bind settings. Any bind to `0.0.0.0` must be treated as network exposure and reviewed with authentication/firewall settings.

Artifacts to return or upload:

- `lmstudio-models.json`;
- `lmstudio-loaded.json`;
- PowerShell `nvidia-smi` output;
- WSL2 `/v1/models` output or exact connection error;
- LM Studio server port and whether localhost or the gateway worked.

Do not include API tokens or unrelated private prompts.

## Candidate selection after inventory

After the inventory is captured:

1. exclude embedding-only and vision-only models;
2. identify the strongest general instruct/chat models that can plausibly fit 8 GB VRAM;
3. prefer 7B–8B-class GGUF deployments over the previously rejected 2B/4B deployments when available;
4. use `lms load --estimate-only <model-key> --context-length <N> --gpu max` before loading;
5. select at most three candidates;
6. assign stable identifiers for the experiment;
7. load and test models serially, not concurrently;
8. preserve one historical rejected deployment only if it adds comparison value.

No model download should occur without Ali's explicit approval after reviewing the existing inventory.

## First smoke proof after candidate selection

For each eligible candidate, the first proof will be one non-streaming JSON-Schema request that tests:

- endpoint reachability;
- exact model identifier;
- valid structured JSON;
- explicit `resolved` or `no_decision_relevant_claim` state;
- source-span grounding;
- finish reason and token diagnostics;
- latency and LM Studio logs;
- no tool use or action fields.

The smoke proof is only a transport/schema admission gate. It is not semantic adoption evidence.

## Experiment corpus direction

The new corpus must be broader than the historical Python-support set and include:

- fix/remediation;
- compatibility assurance;
- interface/behavior change;
- support-boundary change;
- deprecation versus removal;
- current versus future;
- added versus dropped;
- explicit negation;
- multiple claims;
- no relevant claim;
- ambiguity;
- conflict;
- instruction-shaped text;
- legitimate quoted instruction-like text;
- historical S001/S002/S004 excerpts;
- one realistic longer GitHub Release body.

Expected claims and decision effects must be frozen before candidate scoring.

## Decisions deferred

Not yet selected:

- candidate model(s);
- quantization(s);
- context length;
- GPU offload;
- complete-body limit versus deterministic chunking;
- direct `requests` versus OpenAI client versus LM Studio SDK;
- Pydantic versus manual/dataclass contract validation;
- exact claim enums and source-span representation;
- acceptance of local LLM extraction into the product;
- ADR content;
- product source/module boundaries.

## Dated progress log

### 2026-07-28 — Re-evaluation opened

**Observation**

Ali approved proceeding with an LLM direction and reported an existing LM Studio/GGUF environment on an RTX 3070 Laptop GPU with 8 GB VRAM. Sentinel's agents module and UpgradePilot's archived M2 experiment were inspected. Current official LM Studio structured-output and model-management capabilities were checked.

**Interpretation**

The main risk is not basic connectivity or JSON formatting. The prior UpgradePilot experiment already solved those mechanics and still rejected two local deployments because semantically wrong but schema-valid claims changed downstream actions. The current experiment must therefore test stronger deployments and the broader four-category B2 claim contract with decision-effect scoring.

**Decision**

Create a bounded local-LM re-evaluation plan. Do not restore archived M2 source, adopt Sentinel's LangChain/agent architecture, add dependencies, or implement product semantics until the environment inventory and scored method evidence exist.

**Effect**

The next action is environment capture and candidate selection. Product source, active tests, dependencies, decision rules, and CLI behavior remain unchanged.

**References**

- `../plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md`;
- `../plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md`;
- `../learning/m2-s02/03_PROCESS_FAILURES_AND_DESIGN_REVERSALS.md`;
- `../learning/m2-s02/04_LM_STUDIO_STRUCTURED_OUTPUT_AND_DIAGNOSTICS.md`;
- archived revision `e7425dcfc20f093ac10c9a903f1c4ae50a8b2638`;
- Sentinel `agents/README.md` and `agents/src/llm/client.py`.
