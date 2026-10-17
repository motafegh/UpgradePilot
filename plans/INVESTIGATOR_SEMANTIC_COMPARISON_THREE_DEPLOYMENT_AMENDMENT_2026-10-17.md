# Investigator semantic comparison — three-deployment amendment

**Date:** October 17, 2026
**Status:** admitted planning amendment; no semantic inference is activated by this file.
**Owner:** `plans/INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md` remains the controlling integration/comparison plan except where this amendment explicitly revises the deployment-count/assignment baseline.
**Reason for revision:** after completion of current-runtime model-interface qualification, Ali explicitly selected Gemma 4 E4B for inclusion in the real semantic comparison because its exact current deployment is 4/4 canary-qualified and provides a materially smaller qualified operating point worth comparing against the two larger baselines.

## 1. Decision

The planned real semantic comparison is revised from:

`2 development cases × 2 evidence treatments × 2 deployments = 8 assignments`

to:

`2 development cases × 2 evidence treatments × 3 deployments = 12 assignments`.

The intended deployment set is:

1. Gemma 4 12B — exact current-runtime deployment identity to be frozen for the real-case batch;
2. Qwen3.8-27B UD-Q4_K_M — exact current-runtime deployment identity to be frozen for the real-case batch;
3. Gemma 4 E4B — exact qualified native thinking-on deployment identity to be frozen for the real-case batch.

This is an explicit expansion of the semantic-comparison question. It is not an automatic consequence of a canary pass, not an implicit third arm, and not a replacement of retained qualification history.

Qwen3.5-9B remains a qualified available candidate but is **not** added by this amendment. Gemma 4 E2B and MiMo-V2.6-Distill-Qwen-9B remain withheld at their current measured points. Any further deployment addition/substitution requires another explicit pre-inference revision.

## 2. Scientific question after the amendment

The comparison now asks two related bounded questions over the same two exposed development cases:

1. Does Structured native evidence access improve evidence use, interpretation, uncertainty handling, stopping and recommendation quality relative to Raw-oriented navigation?
2. Can a substantially smaller but interface-qualified local deployment (Gemma 4 E4B) achieve useful real semantic evidence use relative to the two larger qualified baselines, and what resource/cost trade-off accompanies that result?

The second question does not create an intrinsic model ranking. One sample per case/treatment/deployment cannot estimate stochastic reliability or general superiority.

## 3. Assignment and fairness consequences

The next semantic-comparison cycle must freeze all 12 assignment IDs and their serial execution order before inference.

The existing Raw/Structured fairness rules remain controlling:

- all three deployments use the same underlying case/source/native evidence freeze;
- Raw and Structured differ only by the admitted treatment capability boundary;
- no case-specific solved path, protected answer, reviewer label or outcome-derived hint enters model input;
- each assignment gets fresh model/context/Workspace state as required by the controlling plan;
- treatment order must be balanced as far as possible across deployments/cases and frozen before outputs exist;
- no failure-selective retry, output salvage or post-outcome configuration tuning is allowed.

Because three deployments cannot produce a perfectly pairwise-symmetric two-treatment order across every case by simple duplication, the next-cycle manifest must explicitly state the chosen balancing rule and order before inference rather than silently inheriting the prior two-deployment schedule.

## 4. Budget consequence

Unless the next-cycle pre-run freeze explicitly justifies a different bounded ceiling, retain the existing **per-assignment** semantic ceilings from the controlling plan:

- 16 model calls maximum;
- 524,288 input tokens maximum;
- 131,072 generated tokens maximum including reported reasoning where applicable;
- 48 charged operations maximum;
- 8 MiB delivered observations maximum;
- 14,400 seconds maximum;
- 8,192 generated-token per-call/final reserve target subject to exact deployment fit and pre-run correspondence.

With 12 assignments, the corresponding conservative aggregate maxima become:

- 192 model calls;
- 6,291,456 input tokens;
- 1,572,864 generated tokens;
- 576 charged operations;
- 96 MiB delivered observations;
- 172,800 seconds.

These are ceilings, not spending targets. The next-cycle freeze must record exact prior spend separately and may lower ceilings if measured evidence supports doing so. It must not increase or selectively vary limits after seeing semantic outcomes.

## 5. Deployment/configuration freeze requirements

Before any affected real-case inference, freeze and verify for all three deployments:

- exact local asset filename/parts, byte size and SHA256 identity;
- runtime/backend and SDK identity;
- actual prompt/chat-template identity and tokenizer/special-token policy;
- reasoning/thinking mode and sampler settings;
- context and generation allowance;
- requested and observed weight placement/offload;
- KV placement/quantization, batching and other material exposed runtime controls;
- actual rendered request fit for the real-case shapes;
- requested-versus-applied configuration correspondence;
- assignment IDs/order and model/treatment mapping.

The qualification evidence establishes current synthetic interface operating points. It does not by itself establish real-case 8,192-token report adequacy. Gemma 12B/Qwen27 synthetic current-runtime canaries used a 2,048 generated-token cap; the controlling plan's 8,192 real-case allowance therefore still requires an explicit real-case configuration/fit freeze before activation. Gemma E4B's qualification used an 8,192 allowance, but its exact real-case request shapes/configuration must still be frozen rather than inferred from the canary run.

Any material configuration change from the qualified point is versioned and must receive the bounded correspondence/qualification proof required by the controlling plan before its semantic assignments are admitted.

## 6. Review protocol consequence

The same nine semantic-review dimensions remain controlling:

- relevant evidence coverage;
- interpretation correctness;
- unsupported claims;
- scoped negative evidence;
- unresolved quality;
- stopping quality;
- recommendation usefulness;
- reviewer effort;
- resource cost.

Review obligations must be frozen before outputs. Review every material assertion, including summaries/recommendations. Valid citation shape does not establish entailment. Preserve immutable model outputs separately from reviewer corrections.

The three-deployment amendment makes resource/cost comparison more decision-relevant, but cost alone does not decide semantic quality and semantic quality alone does not erase operational cost.

## 7. Qualification and non-adoption boundary

Current interface qualification supports admission of the exact qualified deployment points into pre-run semantic planning:

- Gemma 4 12B: 4/4 canary-qualified exact point;
- Qwen3.8-27B: 4/4 canary-qualified exact point;
- Gemma 4 E4B: 4/4 canary-qualified exact point.

This amendment does **not** establish:

- semantic correctness;
- autonomous discovery/stopping adequacy;
- maintainer usefulness;
- production adoption;
- action permission;
- protected-case generalization;
- global model/configuration superiority.

The real semantic comparison remains a development experiment. A later retain/reject/inconclusive disposition is required.

## 8. Required next-cycle pre-inference outputs

Before semantic inference is activated, the selected successor cycle must publish/freeze:

1. exact qualified/refreshed three-deployment configuration catalog;
2. exact common case/input/source/native identities and availability check;
3. 12 assignment IDs and balanced serial order;
4. exact prompts, tools, reference policy, packing/omission policy and report schema;
5. per-assignment and aggregate budgets/accounting rules;
6. real-case rendered-token/context/output fit evidence;
7. review obligations, masking/order/assistance procedure and source-check method;
8. stop/refuse/failure/no-rerun rules;
9. owner-only retention destinations and public-safe evidence paths;
10. explicit activation record showing the current deployment/interface cycle has closed through D/E.

No inference is authorized merely by creating this amendment.
