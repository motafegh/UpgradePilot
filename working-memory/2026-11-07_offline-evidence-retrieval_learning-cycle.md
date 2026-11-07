# Offline evidence retrieval exercise

November 7, 2026. Starts from `852dd20b` and the [HTTPX and OpenCV baseline reviews](2026-11-07_evidence-grounded-maintainer-explanation_planning-cycle.md#httpx-concise-baseline-check). Ali selected the [offline retrieval exercise](../plans/EVIDENCE_GROUNDED_MAINTAINER_EXPLANATION_COMPARISON_PLAN.md#tool-and-learning-comparisons) after both tasks were answered by a concise source-backed baseline. The separate explanation pilot remains deferred for those tasks.

```text
A0 — DONE: reconciled the selected handoff, report identities and available local FTS5.
A1 — CONTINUOUS CONTEXT: the preceding walkthroughs established the source roles and expected evidence.
A2 — COMPRESSED: compare exact source selection with lexical ranking and explicit identity filters.
B — DONE: ran the isolated known-address and lexical comparison.
Verification — GREEN FOR THE EXERCISE: 5/7 retrieval hits, two retained misses and identity controls verified.
D — GUIDED HANDOFF: explain the difference between query coverage and evidence eligibility.
E — HANDOFF: try a simple query rewrite before selecting a semantic retrieval comparison.
C — DONE FOR THIS INCREMENT: inputs, misses, proof limits and handoff preserved.
```

The ordinary separate onboarding and pre-action stops are compressed for this directly selected, reversible local exercise. Its material, methods and task were previewed in the prior handoff. The exercise has an in-memory index, read-only saved inputs and no model or external effects. The learning map covers a passage's exact address, target identity versus package version role, word matching versus BM25 ranking, and evidence selection versus answer quality. Independent practice remains separately assessable.

Freeze the selected spans and query/expected-passage pairs in the local replay before inspecting ranked output. Both cases are exposed, and the index is deliberately small. Compare direct lookup by known address with literal queries, paraphrases, wrong-version exposure and a synthetic wrong-head control. Preserve genuine misses under the original query; a later query change is a labelled development observation. This exercise measures retrieval only.

## Results and reasoning

The [replay](evidence/2026-11-07-offline-evidence-retrieval/replay.py) verified the saved report hashes and exact repository/PR/base/head identity, then indexed five HTTPX source windows and four OpenCV saved report passages in an in-memory SQLite FTS5 table. One synthetic control copied an HTTPX window with a deliberately invalid head. Report excerpts and source excerpts keep their distinct provenance. The HTTPX replay needs the original owner-retained report at the bound local location. Nothing in the index is canonical Workspace evidence. BM25 ranks text matches using corpus statistics. The SQL metadata predicates govern eligibility before the result limit. Ranking does not grant evidence authority.

| Query | Expected passage | Result within two |
| --- | --- | --- |
| `ModuleNotFoundError` and `httpx2` | HTTPX fallback | Hit, 248 bytes |
| `backup client` | HTTPX fallback | Empty |
| `follow_redirects` and `cookies`, old role and version | Old HTTPX constructor | Hit, 1,036 bytes |
| `follow_redirects` and `cookies`, proposed role and version | Proposed HTTPX constructor | Hit, 946 bytes |
| `wheel-tag capabilities` | OpenCV artifact inventory | Hit, 462 bytes |
| `target source-build outcome` | OpenCV source-build unknown | Hit, 320 bytes |
| `compile` and `from source` | OpenCV source-build unknown | Empty |

Known-address selection recovered all seven requested passages because their addresses were supplied. It is a reference for checking retrieval, not an equally automated search competitor. FTS5 hit five of seven, with all five literal queries successful and both selected paraphrases empty. The two passages exist in the admitted corpus. The query vocabulary failed to match, so increasing the top-k limit could not help those queries. Unscoped keyword search returned both HTTPX versions and the forwarding call. The exact role/version pair restricted the result to the requested version, and a deliberately inconsistent pair returned nothing. The wrong-head copy matched without the target filter and was excluded with exact identity filtering. Two additional replays under socket and subprocess guards produced identical results. SQLite version 3.45.1.

The technical result is confined to selected windows and seven exposed queries. No generation, general search-quality estimate, measured maintainer effort or production integration follows. The explanation pilot on the two exposed tasks remains deferred. The next useful learning exercise is to predict and test a plain query rewrite against one miss, then compare a semantic selector only under a separately chosen corpus and scoring contract. The original misses remain in this record. Independent learner practice is pending.

### Guided HTTPX query rewrite

Continued with a worked example so the OpenCV miss remains available for Ali's own attempt. Used the unchanged replay inputs and search function under socket and subprocess guards, with the same nine retained passages, synthetic wrong-head control and top-two limit. The original `"backup client"` still returned no rows. Both `httpx2` and `"import httpx" AND httpx2` returned only `httpx-fallback` under exact PR identity. Without that filter both returned the wrong-head control first and the valid passage second. The useful rewrite changes the terms supplied to the matcher. Exact identity still owns eligibility. The narrow result came from prior knowledge of this case and leaves the original five-of-seven score intact. No general rewrite method was evaluated. OpenCV query selection and independent learner practice remain pending.

### Guided OpenCV query rewrite

Ali asked for the search mechanism and purpose to be explained before proceeding, then selected continuation. The assistant demonstrated the OpenCV rewrite using the original replay corpus and search function, exact OpenCV target and top-two limit under socket/subprocess guards. `compile AND "from source"` remained empty. `"source distribution"` returned the build-outcome and artifact-availability passages, in that order. Both `"source-build outcome"` and `"source build outcome"` returned just the build-outcome passage (`report.txt` L155–158). The broad phrase is useful for finding context. The narrower phrase distinguishes the missing build observation from publication availability. In this index the hyphen is treated as a token separator. Neither phrase creates a build result.

Both original misses now have guided, source-aware rewrites. This is a development observation and the frozen 5/7 baseline remains the comparison result. Independent learner practice remains unassessed. A semantic retrieval experiment would need its own approved local model and frozen passages, query set, expected answers, identity eligibility and scoring. Include a simple lexical rewrite comparator so the semantic treatment must improve on a credible simpler method. No new inference, generation or production retrieval selected.
