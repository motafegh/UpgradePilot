# B2 Gemma E4B Memory Estimate

**Date:** 2026-07-28  
**Operation:** Preserve LM Studio load estimates for the first hardware-fit candidate and determine whether the deployment can be frozen  
**Parent plan:** [`../plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md`](../plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md)  
**Candidate metadata record:** [`2026-07-28_B2-model-metadata-and-networking-sequencing-correction.md`](2026-07-28_B2-model-metadata-and-networking-sequencing-correction.md)  
**Result classification:** Full-offload estimate is provisionally feasible at 4K and 8K, but estimator confidence is low and the identical estimates do not justify freezing 8K without an observed load/smoke result

## 1. Candidate

```text
model key: gemma-4-e4b-it-ud
architecture: gemma4
parameters: 7.5B
quantization: Q4_K_XL
weight file size: approximately 4.751 GiB
measured free VRAM before model load: approximately 6.43 GiB
```

## 2. LM Studio estimates supplied by Ali

### 4,096-token context

```text
Model: gemma-4-e4b-it-ud
Context Length: 4,096
GPU Offload: 100%
Estimated GPU Memory:   4.75 GiB
Estimated Total Memory: 4.75 GiB
Confidence: LOW

Estimate: This model may be loaded based on your resource guardrails settings.
```

### 8,192-token context

```text
Model: gemma-4-e4b-it-ud
Context Length: 8,192
GPU Offload: 100%
Estimated GPU Memory:   4.75 GiB
Estimated Total Memory: 4.75 GiB
Confidence: LOW

Estimate: This model may be loaded based on your resource guardrails settings.
```

## 3. Interpretation

Established:

- LM Studio does not reject full GPU offload for this candidate at either requested context;
- the candidate is the strongest current hardware-fit option for the first observed load;
- the weight estimate leaves roughly 1.68 GiB between the estimated model memory and the measured pre-load free-VRAM baseline.

Not established:

- that 8K is as safe as 4K;
- that KV cache, runtime buffers, compute graph, or Windows GPU contention are fully represented;
- that the model will actually load without guardrail reduction or partial offload;
- that inference will remain stable under a JSON-Schema request;
- that semantic quality is acceptable.

The identical 4K and 8K estimates, combined with `Confidence: LOW`, indicate that this estimator output is not sufficiently discriminating for context-dependent memory. It is likely dominated by weight storage or lacks reliable architecture-specific cache estimation. This is an inference from the supplied outputs, not a claim about LM Studio's internal implementation.

Therefore:

```text
estimate says may load
≠ observed load succeeded
≠ 8K proven safe
≠ structured inference succeeded
```

## 4. CLI capability evidence

Ali also supplied `lms load --help`, establishing:

- `--gpu off|max|0..1` controls GPU offload ratio;
- `--context-length` controls the loaded context window;
- `--parallel` controls concurrent predictions;
- `--ttl` can automatically unload an idle model;
- `--identifier` can assign a stable API model identifier;
- `--estimate-only` performs sizing without loading;
- speculative decoding options exist but are not needed for the first semantic baseline.

The supplied CLI help does not expose explicit KV-cache placement, flash-attention, or reasoning-mode switches. Those settings must be inspected through LM Studio load metadata/UI/API rather than assumed.

## 5. Current deployment disposition

Do not freeze 8K merely because its estimate equals 4K.

Current leading first observed-load configuration:

```text
candidate: gemma-4-e4b-it-ud
context: 4,096
GPU offload: 100%
parallel: 1
speculative decoding: off
stable identifier: upgradepilot-gemma-e4b-smoke
TTL: bounded for experiment convenience
```

This remains provisional until the other candidate estimates are gathered. Starting at 4K is the conservative baseline because the admitted release-text experiment does not yet require 8K and 4K reduces unmeasured cache/runtime risk.

## 6. Remaining estimate sequence

Run and preserve:

```powershell
lms load --estimate-only qwen3.5-9b-ud --context-length 4096 --gpu max
lms load --estimate-only qwen3.5-9b-ud --context-length 8192 --gpu max

lms load --estimate-only gemma-4-12b-it-qat --context-length 4096 --gpu max
lms load --estimate-only gemma-4-12b-it-qat --context-length 8192 --gpu max
```

If the 12B full-offload estimate is rejected or exceeds guardrails, do not load it. Preserve the result; partial-offload estimates can then be tested deliberately with named ratios such as `--gpu 0.75` only after the full-offload evidence is reviewed.

## 7. Next gate

After all three estimate sets are available:

1. compare operational headroom and confidence;
2. freeze the first candidate and load configuration;
3. explicitly load one model rather than relying on just-in-time defaults;
4. capture `lms ps --json` and `nvidia-smi` after load;
5. run one strict non-streaming JSON-Schema smoke request;
6. unload or allow the bounded TTL to expire;
7. only then proceed to Instructor/direct-adapter comparison and semantic scoring.

No product source, dependency, semantic method, or decision behavior is changed by this record.
