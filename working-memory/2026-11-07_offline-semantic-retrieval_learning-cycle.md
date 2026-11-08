# Offline semantic retrieval comparison

November 7, 2026. Ali selected the next offline retrieval comparison after the [lexical and rewrite exercise](2026-11-07_offline-evidence-retrieval_learning-cycle.md#guided-opencv-query-rewrite). The [AI plan](../plans/EVIDENCE_GROUNDED_MAINTAINER_EXPLANATION_COMPARISON_PLAN.md#tool-and-learning-comparisons) separates retrieval quality from explanation and product entry. Scope is one cached local embedding model on CPU and the existing exposed HTTPX/OpenCV passages. Independent learner practice remains separate.

```text
A0 — DONE: reconciled f10ec5f7, saved sources, local model assets and interpreter imports.
A1/A2 — CONTINUOUS CONTEXT: explained lexical misses, identity filters and the three-way comparison.
B — DONE: froze the comparison, preserved the failed activation and ran the fit-control successor locally.
Verification — GREEN FOR THE EXERCISE: matched inputs and hashes, score counts, eligibility and top-two bounds checked.
D — GUIDED HANDOFF: explain where word matching, known rewrites and embeddings helped.
E — HANDOFF: preserve an exposed learning result and leave independent practice and stronger retrieval qualification open.
C — DONE FOR THIS INCREMENT: prerequisites, failures, corrections, scores and proof limits preserved.
```

The separate A1/A2 stops are compressed for the directly selected, reversible continuation of the saved-evidence exercise. The prior explanation established the mechanism and this turn scoped the three arms before writing the freeze. The model consumes only local case passages and queries. The project virtual environment lacks the embedding dependencies. The existing CPU interpreter in the Sentinel agents environment imports them, and the existing Hugging Face snapshot provides safetensors weights. An LM Studio inventory read found other local embedding candidates. The cached CPU route avoids shared model loading, GPU activity, downloads and dependency changes. No product code or other project's environment is modified.

Compare the original seven lexical queries and their corresponding plain-language inputs, plus three new phrasings on the same exposed cases. These are new query strings, not unseen-case evidence. A fixed two-entry rewrite baseline has prior knowledge of the original misses. Freeze the evidence, model assets, packages, queries, expected passage IDs and ranking rule before embedding. Use the same target and role eligibility and top-two result limit in all arms. Score passage hits and first rank. A separate absent-evidence probe measures whether rank can be mistaken for proof. Leave the historical lexical result and the deferred explanation pilot intact.

Pre-freeze corrections. The embedding interpreter imports the model stack but the first freeze attempt failed before reading the report because it lacked `tree_sitter_bash`. Added UpgradePilot's existing package directory at the end of the runner's import search path to supply the report decoder's dependencies without installing or modifying either environment. Tokenizer-only inspection found that four selected passages exceed the embedding snapshot's default 128-token limit, with a maximum of 361 tokens. The tokenizer advertises 512 and the model has 514 positions. Freeze an explicit 384-token cap so the embedding arm sees the same full passages as lexical search. The fit check refuses any silent truncation. Neither correction used a model result.

The first activation at `63bc0998` loaded local weights and stopped at `assert SEQUENCE_LIMIT <= model.tokenizer.model_max_length`. The SentenceTransformers wrapper sets the tokenizer's limit from the snapshot's 128-token sentence config. The preflight had read the underlying tokenizer's 512-token declaration. Zero encoding calls or scores occurred in that attempt. Keep `freeze.json` and the first runner at their Git horizon. Bind a successor that checks the raw tokenizer and positional limit independently, sets the already planned 384 cap, and then checks the effective wrapper setting and every actual input length. The cases, expected IDs, ranking rules and model stay as frozen. This is a fit-control correction before output exposure, with one separately identifiable successor attempt.

## Verified result

The [successor freeze](evidence/2026-11-07-offline-semantic-retrieval/freeze-successor.json) at `772b67cb` completed one CPU run using `paraphrase-multilingual-mpnet-base-v2` and 768-dimensional normalized vectors. The longest input was 361 tokens under the effective 384-token cap, with all passage text admitted. The [results](evidence/2026-11-07-offline-semantic-retrieval/results.json) preserve every ranked ID and similarity score. File digests, first/successor input parity, row counts, rankings against the query labels, top-two limits and exclusion of the synthetic wrong head were checked without rerunning the model. This run recorded 2.179 seconds for model construction and 2.776 seconds for the encoding stage including the input-length check. These stage timings describe this small run, not user latency or a benchmark.

| Method | Original seven | Three new phrasings | Total hits within two |
| --- | --- | --- | --- |
| Keyword search | 5/7 | 0/3 | 5/10 |
| Keyword search with two known rewrites | 7/7 | 0/3 | 7/10 |
| Embedding similarity | 6/7 | 3/3 | 9/10 |

Every hit was at rank one. Embeddings found the OpenCV build-unknown passage for `compile from source` and all three new query strings. For `backup client`, embeddings ranked the two HTTPX constructors ahead of the fallback passage. The known `httpx2` rewrite found the fallback. The role-specific old and proposed constructor questions each had one eligible passage, so their hits primarily exercise metadata admission. The absent-evidence probe ranked HTTPX source passages even though the packet has no observation proving the target test loaded the fallback. This is a consequence of returning the nearest passages without an abstention rule. Similarity, relevance and evidence support are separate. A numeric cutoff was not fitted to this sample.

Both cases and all passages are previously exposed. The three new phrasings test query variation on that material. They are not a generalization cohort, and the rewrite arm covers two previously observed phrases only. These results support a learning comparison of lexical and semantic selection. A successor can test whether a hybrid helps on separately selected material and how it handles no admissible answer, with the same identity gates and a predeclared rule. This run qualifies neither a product retriever nor a generated answer. Independent learner practice is unassessed. The explanation pilot on these tasks remains deferred.
