# Investigator deployment/interface — final study and D reconciliation guide

**Date:** October 17, 2026
**Branch:** `learning/deployment-interface-d-prep-2026-10-17`
**Main evidence horizon:** `c414a6e9bacd572d2d04c38ca54b313f73e83846`
**Status:** final reconciled study reference for this learning branch. The older consolidated guide is historical at its publication horizon; use this file for current study and D reconciliation.

## 1. Responsibility and final state

The completed engineering responsibility was not “find the best LLM.” It was to determine whether exact local model deployments can operate UpgradePilot's bounded Investigator interface with measurable runtime/configuration correspondence, strict evidence/reference authority, retained failures and reproducible qualification evidence.

Build and bounded Verification are complete and GREEN. Canonical D is current and E remains pending.

Current CUDA llama.cpp 2.60.0 qualification points:

| Candidate | Exact-point interface result |
| --- | --- |
| Gemma 4 12B | 4/4 canary-qualified |
| Qwen3.8-27B UD-Q4_K_M | 4/4 canary-qualified |
| Gemma 4 E4B | 4/4 canary-qualified |
| Qwen3.5-9B | 4/4 canary-qualified |
| Gemma 4 E2B | 2/4, WITHHELD |
| MiMo-V2.6-Distill-Qwen-9B | 2/4, WITHHELD |

The two withheld results are completed negative qualification results, not unfinished jobs. The four 4/4 results establish bounded interface operation at those exact deployment points, not semantic correctness or product acceptance.

## 2. Core execution model

The concrete path is:

`UpgradePilot request -> chat template -> tokenizer/token IDs -> BOS/EOS/special-token handling -> context admission -> LM Studio -> llama.cpp/backend -> CPU/GPU/KV execution -> generation/sampling/thinking -> streamed fragments/usage/config receipt -> SDK -> strict Investigator adapter/assessor`

Important distinctions:

- LM Studio orchestrates serving/configuration; llama.cpp performs the lower-level inference.
- Tokenization is model-specific.
- A generation reserve is possible output capacity, not actual generated output.
- Model weights and KV cache are different memory responsibilities.
- Requested GPU offload/configuration is not proof of actual runtime state.

The earlier 1817-measured versus 1818-runtime prompt discrepancy was important because it exposed incomplete correspondence between what we measured and what the backend consumed. The final current-runtime cohort has zero fully rendered prompt-token mismatches across all 119 calls.

## 3. Requested versus observed

The strongest engineering lesson is:

> **Declared/requested/intended is not evidence of what actually happened.**

For every consequential runtime property we prefer observed evidence:

- actual template/rendering;
- actual tokenizer count;
- actual backend/runtime identity;
- actual requested/applied prediction configuration correspondence;
- actual weight-layer flags and KV configuration;
- actual visible output fragments;
- actual usage/stop/error metadata.

Across the final current-runtime calls there were zero prediction-setting mismatches, zero native load/identity mismatches and zero rendered prompt-count mismatches. That is what makes these exact deployment points scientifically usable.

It still does not establish global optimality. Flash auto-kernel choice, physical tensor residency and other unexposed implementation details remain bounded unknowns.

## 4. Context and generation

`input tokens + reserved generation + explicit margin <= context`

establishes mathematical capacity admission only.

It does not prove:

- full reserve will be used;
- correct completion;
- semantic quality;
- acceptable latency;
- no repetition;
- valid JSON;
- real-case report adequacy.

The synthetic current-runtime large-model canaries used a 2048 generated-token cap, while the planned real-case protocol allows 8192. Preflight demonstrated that an 8192 reserve fits inspected request shapes inside 32768 context, but actual real-case 8192-token adequacy has not been demonstrated.

## 5. Sampling and thinking

Temperature controls sampling concentration/variation. Top-k limits sampling to the k highest-probability token candidates. Top-p retains the highest-probability candidates until cumulative probability reaches p.

Thinking mode can alter generation path, usage, latency and output behavior. A model passing under a later thinking-on/native-sampler deployment after failing under an earlier thinking-off deployment establishes the later exact deployment only.

It does not establish that thinking alone caused the change when backend, sampler, generation allowance or other runtime controls also changed.

Gemma 4 E4B is the clearest example: an earlier materially different point failed its qualification cohort, while the current native thinking-on point qualifies 4/4. Preserve both facts.

## 6. Stateless history

The current boundary is explicitly stateless at the inference-server conversation level. UpgradePilot/Workspace owns durable state; each model call explicitly reconstructs the information the model is allowed to rely on.

A complete interaction event requires:

`previous model-authored request + returned observation`

The request preserves intent/history. The observation preserves what the system returned.

Earlier history that retained observations but omitted exact request arguments was incomplete. A model repeating an operation under that condition could not fairly be blamed without repairing the interface first.

After the repair, repeated behavior can more cleanly be attributed to the tested deployment when the necessary history is actually present.

## 7. Evidence/reference authority

Keep these separate:

- model request = intent;
- Workspace/tool observation = delivered data;
- delivered typed evidence reference = possible citation authority;
- internal record/delivery/catalog ID = implementation identity, not automatically a citation;
- final citation = model use of an eligible delivered reference.

A prior model request grants zero evidence authority. A model cannot mint authority by inventing an ID and then seeing its own invented ID again in later explicit history.

Only references actually delivered as eligible in included observations can authorize final citations.

### Visible observation versus citable reference

A final review correction sharpened this rule: an observation/problem can be visible to the model while carrying `evidence=[]` and therefore no typed citation reference.

So:

`visible to model != citable`

Do not accuse a model of citation failure for an observation the interface made uncitable, and never encourage invention of a reference.

Similarly, an empty tool menu in the final report phase after procedural finish does not establish that the entire source universe is exhausted.

These reviewer-side corrections are part of D: evaluation itself must remain evidence-bound.

## 8. Canonical accounting versus readable presentation

Canonical packed bytes own deterministic admission/accounting/omission/reference identity. The model may see a more readable fixed-first representation with chronological request/result pairs.

Different serialization is acceptable only if the same admitted information is represented faithfully. The presentation must not silently add, remove or mutate evidence, IDs, requests, observations or authority.

## 9. Candidate versus deployment versus qualification

Model candidate = underlying model asset.

Deployment = model asset plus exact material runtime conditions, including template/tokenizer/context/sampling/thinking/placement/cache/transport/backend state.

Preflight = identity/configuration/fit preparation before live qualification.

Canary = controlled live synthetic interface test.

Semantic case = later real dependency-update investigation.

Therefore:

`candidate -> exact deployment -> preflight/freeze -> canary qualification -> real semantic case`

Passing one level does not establish the next.

## 10. Raw/Structured and short/near-envelope

Raw primarily exposes bounded source navigation.

Structured additionally exposes product-owned native evidence representations/pages.

These are treatment differences, not simply two prompt styles.

Short sequences test easier interaction/context conditions. Near-envelope sequences exercise larger history, more evidence, omission/packing pressure and late/final report behavior.

A Raw-short pass does not qualify a whole deployment. Required Raw/Structured and short/long conditions must satisfy the frozen gate before the deployment is treated as interface-qualified for the intended comparison.

## 11. Failure ownership

Use the strongest justified class before changing anything:

- interface/experiment defect;
- runtime/configuration correspondence problem;
- interruption/incomplete evidence;
- model interaction/instruction-following failure;
- reference/citation-use failure;
- generation/resource limit;
- semantic-quality problem.

If our interface omitted needed state, repair the interface before blaming the model.

If the interface is correct and the deployment still fails, preserve that negative result.

Do not repeatedly modify settings until a particular canary passes and then pool everything as one stable experiment. That is evaluation overfitting. Legitimate changes are hypothesis-driven, bounded and separately versioned.

## 12. Interface success versus semantics

This is the most important downstream boundary.

A model can:

- use allowed tools;
- follow sequence mechanics;
- cite eligible references;
- produce valid JSON;
- complete procedural finish;

and still make an unsupported conclusion.

Qwen3.5-9B's Raw-long canary is the clearest example: the interface result qualifies, but the report recommends proceeding with the dependency update based on a synthetic interface marker that establishes neither compatibility nor permission.

So:

`valid interface behavior != semantic entailment != maintainer usefulness/action permission`

A valid citation proves provenance/reference validity. It does not prove that the cited evidence entails the claim.

## 13. Final per-model interpretation

### Gemma 4 12B

Current exact point qualifies 4/4. Short reports remained well scoped; longer reports exposed readiness overstatement/informativeness limits. No semantic acceptance follows.

### Qwen3.8-27B

Current exact point qualifies 4/4. Final reports showed careful reference/scoping behavior, including correct treatment of `not_evaluated/null` and uncitable failed reads. It is materially slower/costlier in the observed current cohort: roughly 2702 client seconds across 20 calls, with one call around 669 seconds. This is a planning cost, not an intrinsic global ranking.

### Gemma 4 E4B

Current native thinking-on point qualifies 4/4. Earlier failures under a materially different deployment remain historical evidence. This makes E4B a legitimate future candidate, but not an automatic additional arm in the already planned real-case comparison.

### Qwen3.5-9B

Current exact point qualifies 4/4 and is much faster in the observed current cohort than Qwen27, but the unsupported proceed inference is a clear semantic warning. That makes it informative for later semantic work, not product-approved.

### Gemma 4 E2B

Current point is 2/4 and WITHHELD. Preserve the negative result rather than automatically sweeping more settings.

### MiMo-V2.6-Distill-Qwen-9B

Current point is 2/4 and WITHHELD, including long-report reference failures after correction. Preserve the negative result.

## 14. What is established

Established at this horizon:

- real local stateless model transport works;
- complete request/result history works;
- current-request reference authority works;
- Raw/Structured access works mechanically;
- source/native references can be delivered and guarded;
- actual prompt/runtime/configuration correspondence is measurable and matched for the current cohort;
- four exact deployments satisfy the bounded synthetic interface gate;
- two exact deployments are honestly withheld;
- streamed visible-fragment retention/reasoning filtering work;
- failures/configuration revisions can be retained without silent salvage/pooling.

## 15. What is not established

Not established:

- real dependency-update semantic correctness;
- autonomous discovery quality;
- autonomous stopping adequacy;
- maintainer usefulness;
- action permission;
- generalization beyond known development cases;
- actual real-case 8192-output adequacy;
- globally optimal context/offload/sampler/runtime settings;
- intrinsic model ranking;
- stateful transport superiority;
- multi-agent need/benefit.

## 16. Next experimental responsibility

After canonical D and E close this cycle, the next candidate responsibility is the real paired comparison freeze and semantic review under the existing integration plan.

The current baseline remains:

`2 real cases x 2 treatments x 2 deployments = 8 assignments`

The planned deployment pair remains Gemma 4 12B + Qwen3.8-27B unless explicitly revised before inference.

Before real-case activation, freeze at least:

- exact case inputs/evidence identities;
- selected deployment identities/configurations;
- assignment IDs/order;
- budgets/output allowance;
- Raw/Structured treatment correspondence;
- prompts/tool/reference contract;
- source obligations and semantic review dimensions;
- review process/assistance/effort measurement;
- actual prior spend and activation boundary.

A passing small model does not silently become a third arm. Adding or substituting E4B/Qwen9 materially changes the comparison design and must be an explicit pre-run decision.

## 17. Product-source migration boundary

Do not copy experiment files wholesale into `src/upgradepilot` merely because interface qualification succeeded.

The real semantic comparison should first determine which mechanisms actually earn adoption.

Likely eventual product-owned responsibilities, if supported, include:

- Investigator session/interface contract;
- strict tool and reference authority policy;
- exact history/omission rules;
- product-facing Workspace consumer seam;
- clean local-model runtime abstraction;
- durable regression tests for authority/configuration invariants.

Experiment-owned concerns should remain experiments:

- synthetic canaries;
- model cohorts/qualification harness;
- comparison assignment ordering;
- performance sweeps;
- experimental budgets/manifests;
- offline development semantic review.

Dependency direction should remain:

`experiments -> product code`

and never:

`product runtime -> experiments`

## 18. Deferred runtime research

Useful but not D blockers unless product need makes them decision-critical:

- stateful LM Studio continuation versus explicit stateless requests;
- REST SSE versus current SDK streaming;
- detailed batch/micro-batch benchmarking;
- Flash Attention actual-kernel characterization;
- KV placement/quantization benchmarking;
- speculative decoding;
- mmap/load behavior;
- concurrency/unified-KV behavior;
- RoPE/context-extension work.

## 19. Final D ownership checks

Canonical main deliberately leaves learner ownership unverified until Ali answers these in his own words:

1. Why can Qwen3.5-9B pass all four interface sequences while its “proceed with update” recommendation is still unsupported? What source-to-conclusion review remains necessary?
2. If Gemma 4 E4B were selected for the real comparison, why can we not simply add it to the existing comparison now? What design/configuration/budget/review elements must be explicitly revised and frozen before affected inference?

After these answers are owned, reconcile them into canonical D, identify any genuine learning gap, then perform E repair/defer/closure. Only after canonical closure should the temporary learning branch receive a merge/disposition decision.
