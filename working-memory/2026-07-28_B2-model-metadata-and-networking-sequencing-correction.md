# B2 Model Metadata and Networking Sequencing Correction

**Date:** 2026-07-28  
**Operation:** Correct the localhost/networking interpretation, preserve detailed LM Studio model metadata, and freeze the next memory-estimation candidates  
**Parent re-evaluation plan:** [`../plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md`](../plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md)  
**Deferred learning plan:** [`../plans/B2_LM_STUDIO_NETWORK_BOUNDARY_LEARNING_PLAN.md`](../plans/B2_LM_STUDIO_NETWORK_BOUNDARY_LEARNING_PLAN.md)  
**Supersedes only the overbroad networking interpretation in:** [`2026-07-28_B2-local-model-inventory-and-candidate-shortlist.md`](2026-07-28_B2-local-model-inventory-and-candidate-shortlist.md)  
**Result classification:** Detailed metadata captured; network learning preserved and sequenced after the first semantic baseline; candidate shortlist refined; memory estimates pending

## 1. Correction

The prior statement:

> No gateway URL, CORS change, or non-loopback bind is currently required.

is correct only for the first Python/WSL2 localhost baseline.

It must not be interpreted as:

```text
gateway networking is unnecessary
bind-address learning is unnecessary
firewall/authentication learning is unnecessary
CORS learning is unnecessary
```

Correct project interpretation:

```text
localhost is the first controlled transport
→ reduce variables during model-quality evaluation
→ preserve its result as the control
→ then run a separate controlled network-boundary learning slice
```

The sequencing decision postpones those topics; it does not defer them out of the learning journey.

## 2. Environment evidence now established

```text
LM Studio CLI commit: 71bd99c
server running: true
server port: 12345
just-in-time model loading: active
WSL2 localhost /v1/models: successful
Python: 3.12.3
Python executable: /home/motafeq/projects/UpgradePilot/.venv/bin/python3
GPU: NVIDIA GeForce RTX 3070 Laptop GPU
GPU driver: 610.74
VRAM total: 8192 MiB
VRAM used before model load: 1435 MiB
VRAM free before model load: 6584 MiB
loaded model instances in native inventory: none
```

The generated `lmstudio-models.json` and `lmstudio-loaded.json` files were created on Ali's Windows system. Their contents have not yet been supplied; the native `/api/v1/models` response provides sufficient model metadata for initial candidate estimation, while `lms ps` remains useful confirmation of runtime load configuration.

## 3. Detailed candidate metadata

### Candidate A — `qwen3.5-9b-ud`

```text
publisher: lmstudio-community
architecture: qwen35
parameters: 9B
quantization: Q4_K_XL, 4 bits/weight
file size: 5,966,095,584 bytes
file size: approximately 5.556 GiB
maximum context: 262,144
vision: false
tool-use trained: true
reasoning default: on
loaded instances: none
```

Interpretation:

- remains the primary general-language candidate;
- model weights alone consume most of the measured 6.43 GiB free-VRAM budget;
- complete GPU offload may fit only with limited context/KV use and runtime overhead, or may require partial CPU placement;
- exact `lms load --estimate-only` evidence is mandatory.

### Candidate B — `gemma-4-e4b-it-ud`

```text
publisher: lmstudio-community
architecture: gemma4
parameters: 7.5B
quantization: Q4_K_XL, 4 bits/weight
file size: 5,101,713,792 bytes
file size: approximately 4.751 GiB
maximum context: 131,072
vision: false
tool-use trained: true
reasoning default: on
loaded instances: none
```

Interpretation:

- remains the primary architecture-diverse candidate;
- has approximately 0.805 GiB less weight storage than the Qwen 9B candidate;
- appears more likely to permit full or near-full GPU offload at a bounded context, subject to runtime estimate;
- should be estimated at the same context and cache settings for a fair deployment comparison.

### Candidate C — `gemma-4-12b-it-qat`

```text
publisher: lmstudio-community
architecture: gemma4
parameters: 12B
quantization: Q4_0, 4 bits/weight
file size: 6,975,878,560 bytes
file size: approximately 6.497 GiB
maximum context: 262,144
vision: false
tool-use trained: true
reasoning default: on
loaded instances: none
```

Interpretation:

- remains a stretch quality candidate;
- weight storage alone slightly exceeds the measured 6.43 GiB free-VRAM baseline;
- full GPU offload is not expected under the observed desktop load;
- partial CPU offload may still be operational, but latency and thermal/resource behavior must justify its inclusion.

### Secondary — `qwen3-8b-thinking-2507`

```text
architecture: qwen3vl
parameters: 8B
quantization: Q4_K_M
file size: approximately 4.682 GiB
maximum context: 262,144
vision capability reported: false
loaded instances: none
```

Retain as a secondary comparison only. Its thinking behavior can consume output budget and complicate latency/structured-output measurement.

### Optional coder control — `qwen2.5-coder-7b-instruct`

```text
architecture: qwen2
parameters: 7B
quantization: Q3_K_M
file size: approximately 3.547 GiB
maximum context: 32,768
trained_for_tool_use: false
loaded instances: none
```

Retain only as an optional specialization control. Its lower-bit quantization and code specialization make it a weaker clean comparison for natural-language release semantics.

## 4. Models excluded from first-round estimation

- `google/gemma-4-12b`: Q4_K_M, approximately 7.038 GiB, vision enabled; worse memory fit than the non-vision QAT candidate.
- `qwen3.6-35b-a3b-ud`: IQ2_M but approximately 10.731 GiB of weights; unsuitable as a clean 8 GB-GPU first candidate.
- `qwen3.5-27b-claude-4.6-opus-reasoning-distilled.i1`: approximately 11.255 GiB and community-distilled; exclude.
- `qwen3.5-4b-uncensored-hauhaucs-aggressive`: exclude because the specialization is misaligned with controlled evidence extraction.
- `gemma-4-e2b-it` and `qwen3-4b-instruct-2507`: historical rejected controls, not adoption candidates.
- embedding models: wrong model type.

## 5. Download decision

Do not download another model before measuring these existing candidates.

The inventory already gives a valid comparison ladder:

```text
Gemma E4B — best expected hardware fit
Qwen 3.5 9B — strongest likely general semantic candidate
Gemma 12B QAT — stretch quality candidate with partial-offload risk
```

A new model download becomes justified only after a named gap is observed, such as:

- all three fail the structured-output admission gate;
- the two feasible models fail the semantic corpus materially;
- a current candidate's community template or quantization proves defective;
- a specific official/reputable model provides a materially stronger fit under measured hardware limits.

## 6. Exact next commands

Run from Windows PowerShell and preserve each complete output.

### Qwen 3.5 9B

```powershell
lms load --estimate-only qwen3.5-9b-ud --context-length 4096 --gpu max
lms load --estimate-only qwen3.5-9b-ud --context-length 8192 --gpu max
```

### Gemma 4 E4B

```powershell
lms load --estimate-only gemma-4-e4b-it-ud --context-length 4096 --gpu max
lms load --estimate-only gemma-4-e4b-it-ud --context-length 8192 --gpu max
```

### Gemma 4 12B QAT

```powershell
lms load --estimate-only gemma-4-12b-it-qat --context-length 4096 --gpu max
lms load --estimate-only gemma-4-12b-it-qat --context-length 8192 --gpu max
```

If the CLI rejects `--gpu max`, preserve the exact help/error output rather than guessing another form:

```powershell
lms load --help
```

Do not actually load models concurrently. Estimation is read-only sizing evidence.

## 7. After estimation

Use the estimates to freeze:

```text
candidate
context length
gpu offload
KV-cache placement
flash-attention state
reasoning mode
model TTL/JIT behavior
```

First deployment preference should be selected by evidence, not model size alone:

```text
fits safely
+ enough context
+ stable JSON Schema response
+ acceptable latency
+ strongest semantic results
```

After one localhost model completes the structured-output smoke test and at least one initial scored semantic result, activate the separate network-boundary learning plan.

## 8. Memory update timing

The selected route and plan have not changed. The existing `MEMORY.md` continuation already proceeds from inventory to memory estimation and smoke proof. Update `MEMORY.md` after the estimate outputs freeze the first actual deployment configuration, at which point the live blocker and exact continuation materially narrow.
