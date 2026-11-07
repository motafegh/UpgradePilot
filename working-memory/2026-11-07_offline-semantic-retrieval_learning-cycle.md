# Offline semantic retrieval comparison

November 7, 2026. Ali selected the next offline retrieval comparison after the [lexical and rewrite exercise](2026-11-07_offline-evidence-retrieval_learning-cycle.md#guided-opencv-query-rewrite). The [AI plan](../plans/EVIDENCE_GROUNDED_MAINTAINER_EXPLANATION_COMPARISON_PLAN.md#tool-and-learning-comparisons) separates retrieval quality from explanation and product entry. Scope is one cached local embedding model on CPU and the existing exposed HTTPX/OpenCV passages. Independent learner practice remains separate.

```text
A0 — DONE: reconciled f10ec5f7, saved sources, local model assets and interpreter imports.
A1/A2 — CONTINUOUS CONTEXT: explained lexical misses, identity filters and the three-way comparison.
B — CURRENT: freeze the comparison, then run locally.
Verification — PENDING: check matched inputs, retrieval outcomes and negative controls.
D/E — PENDING: interpret the results and preserve the handoff.
C — CONTINUOUS: preserve prerequisites, methods, failures and results.
```

The separate A1/A2 stops are compressed for the directly selected, reversible continuation of the saved-evidence exercise. The prior explanation established the mechanism and this turn scoped the three arms before writing the freeze. The model consumes only local case passages and queries. The project virtual environment lacks the embedding dependencies. The existing CPU interpreter in the Sentinel agents environment imports them, and the existing Hugging Face snapshot provides safetensors weights. An LM Studio inventory read found other local embedding candidates. The cached CPU route avoids shared model loading, GPU activity, downloads and dependency changes. No product code or other project's environment is modified.

Compare the original seven lexical queries and their corresponding plain-language inputs, plus three new phrasings on the same exposed cases. These are new query strings, not unseen-case evidence. A fixed two-entry rewrite baseline has prior knowledge of the original misses. Freeze the evidence, model assets, packages, queries, expected passage IDs and ranking rule before embedding. Use the same target and role eligibility and top-two result limit in all arms. Score passage hits and first rank. A separate absent-evidence probe measures whether rank can be mistaken for proof. Leave the historical lexical result and the deferred explanation pilot intact.

Pre-freeze corrections. The embedding interpreter imports the model stack but the first freeze attempt failed before reading the report because it lacked `tree_sitter_bash`. Added UpgradePilot's existing package directory at the end of the runner's import search path to supply the report decoder's dependencies without installing or modifying either environment. Tokenizer-only inspection found that four selected passages exceed the embedding snapshot's default 128-token limit, with a maximum of 361 tokens. The tokenizer advertises 512 and the model has 514 positions. Freeze an explicit 384-token cap so the embedding arm sees the same full passages as lexical search. The fit check refuses any silent truncation. Neither correction used a model result.

The first activation at `63bc0998` loaded local weights and stopped at `assert SEQUENCE_LIMIT <= model.tokenizer.model_max_length`. The SentenceTransformers wrapper sets the tokenizer's limit from the snapshot's 128-token sentence config. The preflight had read the underlying tokenizer's 512-token declaration. Zero encoding calls or scores occurred in that attempt. Keep `freeze.json` and the first runner at their Git horizon. Bind a successor that checks the raw tokenizer and positional limit independently, sets the already planned 384 cap, and then checks the effective wrapper setting and every actual input length. The cases, expected IDs, ranking rules and model stay as frozen. This is a fit-control correction before output exposure, with one separately identifiable successor attempt.
