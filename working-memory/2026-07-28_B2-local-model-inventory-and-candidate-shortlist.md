# B2 Local Model Inventory and Candidate Shortlist

**Date:** 2026-07-28  
**Operation:** Record WSL2 reachability, Python/GPU environment, available LM Studio model identifiers, and the first bounded candidate shortlist  
**Parent plan:** [`../plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md`](../plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md)  
**Related server/Instructor assessment:** [`2026-07-28_B2-lm-studio-server-and-instructor-assessment.md`](2026-07-28_B2-lm-studio-server-and-instructor-assessment.md)  
**Result classification:** Transport and core hardware inventory established; provisional shortlist selected; exact quantizations/load estimates still required; no model or adapter adopted

## 1. Environment evidence supplied by Ali

### WSL2 transport

The active UpgradePilot WSL2 environment successfully reached:

```text
http://127.0.0.1:12345/v1/models
```

The endpoint returned a valid OpenAI-compatible model list. Therefore Windows-to-WSL2 localhost transport is established for the current LM Studio desktop server. No gateway URL, CORS change, or non-loopback bind is currently required.

### Python environment

```text
Python 3.12.3
/home/motafeq/projects/UpgradePilot/.venv/bin/python3
```

### GPU snapshot

```text
NVIDIA GeForce RTX 3070 Laptop GPU
Driver: 610.74
Total VRAM: 8192 MiB
Used before model load: 1435 MiB
Free before model load: 6584 MiB
Temperature: 46 C
GPU utilization: 1%
```

The desktop compositor, LM Studio, ChatGPT, browsers, VS Code, and other GUI processes were active during the snapshot. The free-VRAM value is therefore the relevant initial operating budget, not the nominal 8192 MiB total.

## 2. Model identifiers exposed by LM Studio

### General/instruction or reasoning candidates

```text
qwen3.5-9b-ud
gemma-4-e4b-it-ud
gemma-4-12b-it-qat
google/gemma-4-12b
qwen3-8b-thinking-2507
qwen3.6-35b-a3b-ud
qwen3.5-27b-claude-4.6-opus-reasoning-distilled.i1
ministral-3-3b-instruct-2512
```

### Coder-specialized or community-specialized candidates

```text
qwopus3.5-9b-coder-mtp
qwen2.5-coder-7b-instruct
qwen2.5-coder-0.5b-instruct
```

### Previously rejected or deliberately weak controls

```text
gemma-4-e2b-it
qwen3-4b-instruct-2507
qwen3-4b-thinking-2507
qwen2.5-0.5b-instruct
qwen3.5-4b-uncensored-hauhaucs-aggressive
```

### Embedding models — excluded from semantic extraction

```text
text-embedding-nomic-embed-text-v1.5
text-embedding-mxbai-embed-large-v1
```

The `/v1/models` response establishes API identifiers only. It does not establish exact local file paths, quantizations, disk sizes, architecture metadata, or load configuration.

## 3. Provisional first-round shortlist

### Candidate A — `qwen3.5-9b-ud`

**Role:** Primary general-language candidate.

Reasons:

- materially larger and newer than the previously rejected Qwen3 4B deployment;
- general conversational/instruction model rather than code-only specialization;
- size class is plausible for a 4-bit deployment on an 8 GB GPU, subject to exact quantization and LM Studio estimation;
- likely strongest existing balance of semantic capability and operational feasibility.

Open questions:

- exact quantization and file size;
- whether the local chat template/thinking behavior is stable under JSON Schema;
- GPU memory estimate at 4096 and 8192 context;
- first-pass semantic reliability.

### Candidate B — `gemma-4-e4b-it-ud`

**Role:** Primary architecture-diverse alternative.

Reasons:

- newer and materially stronger than the previously rejected Gemma E2B deployment;
- instruction-tuned general model;
- effective 4.5B decoder class with larger total embedding footprint, designed for on-device use;
- provides a different model family for comparison without adding a second semantic decision system.

Open questions:

- exact UD quantization and local file size;
- whether multimodal support adds avoidable memory overhead in the LM Studio load;
- structured-output quality and thinking-mode behavior;
- memory estimate at the frozen context.

### Candidate C — `gemma-4-12b-it-qat`

**Role:** Stretch quality candidate, not default.

Reasons:

- materially larger 12B instruction model;
- QAT 4-bit checkpoint may preserve more quality than ordinary low-bit post-training quantization;
- useful to test whether a stronger model materially improves semantic and decision-effect accuracy.

Constraint:

- the official Q4_0 GGUF weights alone are approximately 6.98 GB, before KV cache, runtime buffers, and other GPU use;
- Ali currently has approximately 6.43 GiB free VRAM before model load;
- full GPU offload is therefore unlikely at useful context without reducing other GPU use, offloading KV cache to CPU, or partial CPU inference.

This candidate enters only if `lms load --estimate-only` shows an operationally acceptable configuration.

## 4. Secondary candidates and exclusions

### `qwen3-8b-thinking-2507`

Retain as a secondary candidate only. It may reason well, but persistent thinking can consume output budget, latency, and structured-output headroom. It should not displace the general 9B and Gemma E4B candidates before smoke evidence.

### `qwen2.5-coder-7b-instruct`

Retain as an optional specialization control. It is a 7.61B code-focused instruction model with broad competencies, but release-note semantic extraction is not primarily a coding task.

### `qwopus3.5-9b-coder-mtp`

Do not select for the first semantic round. It is a community coder-oriented derivative and adds provenance/chat-template/MTP variables that are unnecessary before the clean general models are measured.

### `qwen3.6-35b-a3b-ud`

Exclude from the first round. Although only approximately 3B parameters are activated per token, the model contains 35B total parameters and still requires the complete quantized weight set in memory or system RAM. It is not a clean fit for an 8 GB laptop-GPU first experiment.

### `qwen3.5-27b-claude-4.6-opus-reasoning-distilled.i1`

Exclude because of size, community distillation variables, and likely heavy CPU offload.

### Previously rejected 2B/4B deployments

Do not treat as new candidates. One may be retained only as a historical control after the new proof set is frozen.

## 5. Download decision

Do not download another model yet.

The current inventory already contains:

```text
one plausible 9B general candidate
+ one plausible Gemma E4B candidate
+ one 12B QAT stretch candidate
+ optional 8B reasoning and 7B coder controls
```

A new download is justified only if:

- exact local metadata shows the current candidate quantization is unsuitable;
- the model file/chat template is a modified or unreliable community variant;
- structured-output smoke testing fails for model/runtime reasons;
- a specific official quantization provides a clearly better fit and a memory estimate supports it.

Prefer official instruction-tuned checkpoints or reputable direct quantizations of them. Avoid uncensored/aggressive, roleplay, or opaque reasoning-distilled variants for this evidence-extraction responsibility.

## 6. Required metadata capture before loading

From Windows PowerShell:

```powershell
lms --version
lms server status --json --quiet
lms ls --llm --json | Out-File -Encoding utf8 lmstudio-models.json
lms ps --json | Out-File -Encoding utf8 lmstudio-loaded.json
```

From WSL2, the LM Studio native endpoint can also provide detailed model metadata:

```bash
curl -fsS http://127.0.0.1:12345/api/v1/models \
  | python3 -m json.tool \
  > lmstudio-native-models.json
```

Return or inspect the entries for:

```text
qwen3.5-9b-ud
gemma-4-e4b-it-ud
gemma-4-12b-it-qat
qwen3-8b-thinking-2507
```

Required fields include model key/path, architecture, parameter count, quantization, file size, maximum context, capabilities, and any loaded instances.

## 7. Memory-estimation sequence

After exact model keys are known, run from Windows PowerShell, serially:

```powershell
lms load --estimate-only <QWEN35_9B_MODEL_KEY> --context-length 4096 --gpu max
lms load --estimate-only <QWEN35_9B_MODEL_KEY> --context-length 8192 --gpu max

lms load --estimate-only <GEMMA4_E4B_MODEL_KEY> --context-length 4096 --gpu max
lms load --estimate-only <GEMMA4_E4B_MODEL_KEY> --context-length 8192 --gpu max

lms load --estimate-only <GEMMA4_12B_QAT_MODEL_KEY> --context-length 4096 --gpu max
lms load --estimate-only <GEMMA4_12B_QAT_MODEL_KEY> --context-length 8192 --gpu max
```

Do not load the three models concurrently. Do not use just-in-time defaults for scored experiments; the final candidate must be explicitly loaded with a frozen context, GPU offload, flash-attention, and KV-cache configuration.

## 8. Current conclusion

Established:

```text
LM Studio server reachable from WSL2 localhost
OpenAI-compatible model listing works
Python 3.12.3 project venv identified
RTX 3070 Laptop GPU and free-memory baseline captured
existing inventory contains credible first-round candidates
```

Still required:

```text
LM Studio/CLI version
native detailed model metadata
exact quantizations and file sizes
currently loaded instances
memory estimates at 4K and 8K context
frozen candidate/load configuration
JSON-Schema smoke results
```

The immediate continuation is metadata capture and memory estimation. No new download, dependency, product model, or semantic adapter is selected by this record.
