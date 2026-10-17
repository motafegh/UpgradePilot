# Investigator deployment/interface — learner-owned D closure

**Date:** October 17, 2026
**Status:** learner-owned D conclusions consolidated from `learning/deployment-interface-d-prep-2026-10-17` and reconciled against completed main qualification evidence at `c414a6e9bacd572d2d04c38ca54b313f73e83846`.
**Boundary:** this file records learning ownership. Model/runtime dispositions remain owned by the retained qualification evidence and canonical cycle records.

## Owned execution model

Ali owns the request-to-output path at the required depth:

`UpgradePilot request -> chat template -> tokenizer/token IDs -> special-token handling -> context admission -> LM Studio orchestration -> llama.cpp/backend inference -> CPU/GPU/KV execution -> generation/sampling/thinking -> streamed output/usage/configuration -> SDK -> strict Investigator adapter/assessor`.

Stable conclusions:

- tokenization/template behavior is model/deployment specific;
- BOS/EOS and other transformations matter because measured input must correspond to actual runtime input;
- context fit establishes capacity only, not correctness, latency, semantic adequacy or full-reserve use;
- model weights and KV cache are distinct memory/runtime responsibilities;
- requested GPU/runtime configuration is not proof of actual applied state;
- temperature/top-k/top-p/thinking and material runtime differences can define a different deployment condition;
- a later configuration succeeding does not by itself identify which changed parameter caused the improvement.

## Owned state/evidence model

Ali owns the stateless-history and evidence-authority boundaries:

- complete stateless history requires both the prior model-authored request and the returned observation;
- prior model intent has zero evidence authority;
- observation is delivered data with bounded scope, not automatically broad semantic truth;
- only a typed evidence reference actually delivered by the system can authorize a report citation;
- internal record/delivery/catalog IDs do not become citation authority merely because the model sees them;
- canonical packed/accounting representation may differ from model-readable presentation only when admitted content is preserved faithfully;
- omitted evidence cannot silently remain authoritative;
- visible observation is distinct from citable typed reference: a model may see a problem for which `evidence=[]` supplies no citation ID.

## Owned qualification model

Ali owns the distinctions among candidate, deployment, preflight, canary and semantic case:

- candidate is the model asset under consideration;
- deployment is the candidate plus exact material runtime/template/context/sampler/thinking/placement/transport conditions;
- preflight prepares and verifies identities/fit before live qualification;
- canary qualification establishes bounded interface operability only;
- real semantic assignments later ask whether the qualified deployment interprets actual dependency-update evidence correctly and usefully;
- Raw versus Structured and short versus near-envelope exercise different treatment/interface pressures;
- one passing sequence cannot qualify an entire deployment;
- materially changed experimental conditions remain separate evidence rather than being pooled.

## Owned failure and review discipline

Ali owns the distinction among interface defects, runtime/configuration correspondence failures, incomplete/interrupted evidence, model interaction failures, reference failures, generation/resource limits and semantic-quality problems.

Repair is justified when our protocol/measurement/interface prevents a fair interpretation. Once the interface is sound/frozen, a model/deployment failure remains evidence rather than being tuned away. Repeatedly changing settings until a canary passes risks evaluation overfitting.

Reviewer-side errors are subject to the same discipline: criticism must be grounded in the actual phase, observations and references the model received. We corrected earlier criticisms where failed-read observations were visible but uncitable, and where a report-phase empty menu did not mean the entire source universe was exhausted.

## Final current-runtime synthesis

Current exact-point interface dispositions on CUDA llama.cpp 2.60.0 are:

- Gemma 4 12B — 4/4 canary-qualified;
- Qwen3.8-27B UD-Q4_K_M — 4/4 canary-qualified;
- Gemma 4 E4B — 4/4 canary-qualified;
- Qwen3.5-9B — 4/4 canary-qualified;
- Gemma 4 E2B — 2/4, WITHHELD;
- MiMo-V2.6-Distill-Qwen-9B — 2/4, WITHHELD.

Qualification belongs to the exact runtime/configuration in which it was observed. The four 4/4 results do not establish semantic correctness, autonomous investigation/stopping adequacy, maintainer usefulness, action permission, protected-case generalization or intrinsic model ranking.

## Canonical D ownership checks

Ali explicitly owns both final D consequences:

1. **Interface success is not semantic acceptance.** A report can use valid citations and satisfy the interface while making a conclusion that goes beyond what those citations support. The next semantic layer must review source-to-claim entailment, scope, uncertainty and applicability rather than treating citation validity as proof of meaning.
2. **E4B may be included, but only through an explicit experiment revision.** Ali selected Gemma 4 E4B for the real semantic comparison because its exact current deployment is 4/4 canary-qualified and shows useful potential. He also explicitly agreed that changing the comparison from two to three deployments changes assignment count, fairness/order, aggregate budget and the comparison question; those conditions must therefore be revised and frozen before affected semantic inference rather than adding untracked E4B calls afterward.

The controlling planning amendment is `plans/INVESTIGATOR_SEMANTIC_COMPARISON_THREE_DEPLOYMENT_AMENDMENT_2026-10-17.md`, revising the intended real comparison to:

`2 cases × 2 treatments × 3 deployments = 12 assignments`.

## Remaining non-blocking/deferred learning

Detailed batch/micro-batch optimization, Flash Attention kernel characterization, KV placement/quantization benchmarking, speculative decoding, mmap/loading, concurrent/unified-KV serving, RoPE/context extension, stateful LM Studio transport and REST-SSE comparisons remain future responsibilities when a product question makes them decision-critical. They are not blockers for closing this deployment/interface cycle.
