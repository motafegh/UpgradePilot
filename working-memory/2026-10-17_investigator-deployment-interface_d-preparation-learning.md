# Investigator deployment/interface — D preparation learning companion

**Branch:** `learning/deployment-interface-d-prep-2026-10-17`
**Original base:** `main@a95c2369c71fcb8e8824f11181c04b1bb7042ac1`
**Final evidence horizon reconciled:** `main@c414a6e9bacd572d2d04c38ca54b313f73e83846`
**Date:** October 17, 2026
**Status:** RECONCILED LEARNING COMPANION — core learning owned through the final qualification evidence; two canonical-D ownership checks remain for Ali. This file is not the canonical D owner and does not close D/E by itself.

## Purpose and boundary

This companion records learner-owned understanding for the deployment/model-interface qualification responsibility. It was created while main Build/Verification was still active, then reconciled after the bounded qualification work completed.

It does not own model dispositions, experiment evidence, live MEMORY, semantic acceptance, usefulness, product migration, or later case activation. Final engineering truth remains on `main` in the deployment-cycle record and retained evidence.

Ali requested that teaching avoid opaque experiment labels such as revision numbers unless their meaning is explained. This reconciliation therefore uses descriptive experimental horizons rather than requiring revision-label memorization.

## Final main state used for reconciliation

The bounded deployment/interface engineering responsibility is complete and Verification is GREEN. All six candidates now have actual current CUDA llama.cpp 2.60.0 observations under frozen deployment points:

- Gemma 4 12B — 4/4 canary-qualified.
- Qwen3.8-27B UD-Q4_K_M — 4/4 canary-qualified.
- Gemma 4 E4B — 4/4 canary-qualified.
- Qwen3.5-9B — 4/4 canary-qualified.
- Gemma 4 E2B — 2/4, WITHHELD.
- MiMo-V2.6-Distill-Qwen-9B — 2/4, WITHHELD.

Across the current-runtime cohorts, 119 prediction calls have zero requested/applied prediction-setting mismatches, zero native-load/identity mismatches, and zero fully rendered prompt-token mismatches. The qualification work therefore established a strong measured correspondence between the frozen requests/configurations and the observed runtime for these exact deployment points.

The real HTTPX/glyphsLib semantic comparison remains unactivated. Interface qualification does not establish semantic correctness, autonomous discovery/stopping adequacy, maintainer usefulness, action permission, generalization, or globally optimal deployment settings.

## Learner-owned block 1 — request to runtime/model output

Ali owns the concrete path at the current required depth:

`UpgradePilot request -> model chat-template rendering -> tokenizer/token IDs -> special-token handling -> context admission -> LM Studio orchestration -> llama.cpp/backend inference -> CPU/GPU/KV placement -> generation/sampling/thinking -> streamed fragments/usage -> SDK -> strict UpgradePilot adapter/assessor`

Stable learner-owned conclusions:

- A token is a tokenizer-specific vocabulary unit represented by an ID; it is not necessarily a word.
- BOS/EOS are Beginning/End Of Sequence markers.
- The earlier `1817 measured / 1818 runtime` discrepancy mattered because it exposed incomplete measurement/runtime correspondence, not because one token materially threatened capacity.
- Context is total sequence capacity; input occupies part of it and generation reserve is intentionally retained possible output capacity. `input + reserve + margin <= context` proves fit only, not correctness, speed, full-reserve use, or semantic adequacy.
- Model weights are persistent trained parameters; KV cache is temporary Key/Value attention state for already processed sequence tokens.
- Requested GPU offload is an intention. Actual observed placement is stronger evidence; a nominal `ratio=1.0` did not itself prove physical placement.
- Temperature changes sampling concentration/variation. Top-k restricts next-token candidates to the k highest-probability options. Top-p retains the smallest high-probability set reaching cumulative probability p.
- Thinking mode and sampler/runtime differences can materially change a deployment. A later configuration succeeding after an earlier one fails establishes that exact later operating point, not that one changed parameter caused the improvement or that it is globally correct/optimal.
- Runtime controls such as batching, Flash Attention, KV quantization/placement, mmap, concurrency/unified KV, speculative decoding and RoPE remain understood at role level; detailed optimization is deferred until a real performance/context/concurrency responsibility requires it.

**Block 1 status: OWNED.**

## Learner-owned block 2 — stateless history and evidence/reference authority

Stable learner-owned conclusions:

- Stateless means no trusted hidden server conversation. Everything the model is allowed to rely on for the current call must be explicit in that call.
- Complete interaction history requires both the prior model-authored request and the returned system observation. The request preserves what was attempted; the observation preserves what the system actually returned.
- A previous model request has zero evidence authority. It is intent/history, not evidence.
- A Workspace/tool observation is delivered data, but still has bounded provenance/scope and is not automatically broad semantic truth.
- Only a typed evidence reference actually delivered as eligible by the system can authorize a report citation.
- Internal record/delivery/catalog IDs are not automatically citation references.
- A model-manufactured reference remains invalid even if the next stateless request shows the model its own earlier text containing that ID.
- Canonical packed/accounting representation and model-readable presentation may differ in format if they preserve the same admitted information faithfully; accounting one history while showing materially different history would be invalid.
- Omitted evidence cannot silently remain authoritative; it must be reread/redelivered when needed.

Final-main refinement now incorporated:

- **visible observation != citable typed reference.** A failed read/problem may be visible to the model while the interface supplies `evidence=[]`. Review must not punish the model for failing to cite an unavailable reference or encourage invented citations.
- A report-phase empty tool menu after procedural finish is not proof that the source universe itself is exhausted.

**Block 2 status: OWNED.**

## Learner-owned block 3 — qualification design

Stable learner-owned conclusions:

- Model candidate = underlying model asset under consideration.
- Deployment = exact model plus material runtime/template/tokenizer/context/sampler/thinking/placement/transport conditions.
- Preflight establishes identity/readiness/fit before live qualification; it is not a canary result.
- Canary qualification actually exercises the model against the bounded Investigator interface and establishes interface operability only.
- Real semantic case assignments later ask whether a qualified deployment can interpret real dependency-update evidence correctly and usefully.
- Raw and Structured are different evidence-access treatments; a Raw pass does not establish Structured capability.
- Short and near-envelope sequences exercise different context/history pressure; a short pass does not establish realistic longer interaction behavior.
- One passing sequence cannot qualify an entire deployment. Required conditions must be satisfied before the deployment is admitted to the intended paired comparison.
- Material changes to history handling, runtime/backend, thinking, sampling, generation allowance, transport or other consequential controls create separately versioned experimental/deployment conditions. Old and new results remain evidence about their own conditions rather than being blindly pooled.

**Block 3 status: OWNED.**

## Learner-owned block 4 — failure diagnosis and repair discipline

Stable learner-owned conclusions:

- If our stateless representation omits exact previous request information, resulting repetition is primarily an interface defect; after repairing the history, equivalent repetition can become evidence about the tested deployment.
- A completed interface-valid report can still be semantically wrong or unsupported. Interface validation and semantic evaluation answer different questions.
- Configuration tuning is legitimate when hypothesis-driven, bounded and separately versioned. Repeatedly changing settings until a specific canary passes risks evaluation overfitting and weakens generalization evidence.
- Interruption/incomplete usage should be retained as incomplete evidence rather than relabeled as a semantic model failure.
- Requested-versus-observed runtime mismatches must be resolved before assigning model blame.
- Citation/reference failure, model interaction failure, generation/resource exhaustion and semantic-quality failure are distinct classes and should not be collapsed into one generic “model failed” label.

Final-main reviewer-side lesson now incorporated:

- Failure diagnosis applies to our review too. Earlier criticisms were corrected after tracing actual phase state and citation visibility. We should not infer model internals or fault the model for information/authority the interface did not provide.

**Block 4 status: OWNED.**

## Learner-owned block 5 — final evidence synthesis

Ali's final synthesis, reconciled against completed main evidence:

- Interface qualification is not semantic validation. A model can satisfy tools/schema/reference/procedural requirements and still make a claim that the cited evidence does not entail.
- A later deployment succeeding after an earlier deployment fails cannot be attributed to a single parameter when multiple runtime/sampling/thinking controls changed.
- Qualification belongs to the runtime/configuration where it was observed. A material backend change requires current-runtime evidence rather than silently inheriting old passes.
- Across different models/methods/scenarios we must verify that the runtime actually applied the elements and parameters we believe we are testing and keep materially different conditions separate.

Final candidate-state synthesis:

- Gemma 4 12B: exact current point is 4/4 interface-qualified. Semantic/report review still found overstatement/informativeness limits; no semantic acceptance.
- Qwen3.8-27B: exact current point is 4/4 interface-qualified. Final reports show careful scope/reference handling; practical latency/cost is significant. No intrinsic superiority or semantic acceptance.
- Gemma 4 E4B: exact native thinking-on point is 4/4 interface-qualified. Earlier failure under a materially different deployment remains valid historical evidence and is not erased. Current success does not establish which changed factor caused improvement.
- Qwen3.5-9B: exact current point is 4/4 interface-qualified, while one Raw-long report still gives a clear example of a validly cited but unsupported “proceed” inference. This is the strongest concrete demonstration of interface success != semantic correctness.
- Gemma 4 E2B: current point is 2/4 and WITHHELD with completed negative qualification evidence.
- MiMo-V2.6-Distill-Qwen-9B: current point is 2/4 and WITHHELD with completed negative qualification evidence.

What remains deliberately unestablished: real dependency-update semantics, autonomous discovery/stopping adequacy, maintainer usefulness, generalization, action permission, real-case 8192-output adequacy, globally optimal configuration and any intrinsic model ranking.

**Block 5 conceptual synthesis status: OWNED. Formal canonical-D ownership still requires Ali's two final responses below.**

## Formal-D ownership checks still required

Main's canonical D packet asks Ali to answer these in his own words. This companion must not fabricate ownership.

1. Why can Qwen3.5-9B pass all four interface sequences while its “proceed with update” recommendation still lack support? What additional source-to-conclusion review remains necessary?
2. If Gemma 4 E4B were selected for the later real comparison, why can its qualification not silently create a third deployment arm? What must be explicitly decided and frozen before affected inference?

These are the only meaningful learner-ownership checks still open for this cycle at the current depth.

## Remaining debt / explicitly deferred learning

Not blockers for D unless a later responsibility makes them decision-critical:

- detailed batch/micro-batch optimization;
- actual Flash Attention kernel characterization;
- KV-placement/quantization benchmarks;
- speculative-decoding evaluation;
- mmap/load benchmarking;
- concurrent prediction/unified-KV study;
- RoPE/context-extension tuning;
- stateful LM Studio versus explicit stateless transport comparison;
- REST SSE versus current SDK streaming observability comparison.

The following final-main limitations remain engineering/project debt rather than learner confusion:

- one historical terminated-call usage remains unknown;
- retained run roots are local-only, not off-machine backup/full runtime-binary archives;
- current settings are qualified operating points, not global optima;
- real-case comparison requires its own case/configuration/order/budget/review freeze before inference.

## Formal-D reuse criteria

After Ali answers the two ownership checks:

1. record those answers here as learner-owned conclusions;
2. compare them with main's D packet without importing stale revision-label summaries;
3. identify any actual contradiction or missing concept;
4. if none, update canonical D on `main` with the supported learner-owned conclusions;
5. perform E repair/defer/closure truthfully;
6. only then decide which learning-branch records are worth merging, rather than merging the temporary branch wholesale.

## Progress

- [x] L1 request-to-model pipeline owned
- [x] L2 stateless history/reference authority owned
- [x] L3 qualification mechanics owned
- [x] L4 failure diagnosis/repair discipline owned
- [x] L5 conceptual per-model/current-state synthesis owned
- [x] Q1-Q5 answered/reviewed at required depth
- [x] Q6-Q9 answered/reviewed at required depth
- [x] Q10-Q13 answered/reviewed at required depth
- [x] Q14-Q16 answered/reviewed at required depth
- [x] Reconciled against completed B/Verification evidence
- [ ] Final canonical-D ownership check 1 answered by Ali
- [ ] Final canonical-D ownership check 2 answered by Ali
- [ ] Folded into formal canonical D
- [ ] E repair/defer/closure completed
- [ ] Temporary learning-branch merge/disposition decided
