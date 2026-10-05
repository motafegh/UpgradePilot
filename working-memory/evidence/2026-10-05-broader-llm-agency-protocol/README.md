# Broader-agency protocol — dated feasibility evidence

This directory preserves read-only observations supporting the [local comparison protocol](../../../plans/BROADER_LLM_AGENCY_COMPARATIVE_EVALUATION_PROTOCOL.md). It contains no model trial result, chosen product architecture or live project position.

## Observation and scope

[The snapshot](local-model-and-reference-snapshot.json) records a successful direct loopback GET to `http://127.0.0.1:18080/api/v1/models`, using Python urllib with `ProxyHandler({})`. Both native and compatible model-list endpoints were inspected successfully; the retained snapshot uses the native response and includes only five candidates relevant to the protocol. The full inventory was not copied into project memory. The observation timestamp is in the JSON.

Gemma `gemma-4-e4b-it-ud` was loaded at context 4096, with parallel 4, Flash Attention and GPU KV offload reported. The candidate Qwen and larger Gemma records were unloaded. Model sizes, quantization and capability flags are provider metadata. No tokenization, inference, tool-call probe, model load/unload, GPU measurement or third-party execution occurred. File sizes do not establish runtime memory fit. ENVIRONMENT's historically validated parallelism 1 differs from this dated observation; no reusable environment owner was changed on this basis alone.

The same snapshot identifies committed main revision `08e364615b011a11defc85c2d357fa2d0e26ccdb` and SHA-256 hashes for four source/test files read from that revision. The research worktree does not contain main's two later interpreter modules; inspect them by commit rather than inventing local file links:

```bash
git show 08e364615b011a11defc85c2d357fa2d0e26ccdb:experiments/api_change_interpretation.py
git show 08e364615b011a11defc85c2d357fa2d0e26ccdb:experiments/api_change_interpretation_trial.py
git show 08e364615b011a11defc85c2d357fa2d0e26ccdb:working-memory/2026-10-05_1950_api-change-interpretation-implementation_lbd-cycle.md
```

The pinned record reports 31 focused and 120 active API-trial tests, controlled-provider interpretation/recovery, and exact offline CLI packet equality. This is **inspected historical engineering evidence**, not a rerun, local real-model result or product admission. Main's uncommitted MEMORY/source/evaluator record showed a same-cycle real-model evaluation extension underway; those changing files were not adopted as verified source.

The committed product `src/` and `tests/` trees are unchanged between the research fork `7f1bd0ec29d13d32cc8a805d948b4dc422394d96` and this reference. The research branch was not merged/rebased, and main's work was not edited, stashed or copied. Subsequent execution must refresh/pin source and reconcile local runtime availability separately.

## Primary-source follow-up

Read selected methods/limitations rather than only overview leads:

- [DepRepair](https://arxiv.org/html/2607.17957v1), benchmark construction, approach, controlled generation/oracle and discussion/threats. Its breakage-selected corpus and post-generation testing motivate additional negative/unresolved cases and a separate execution-feedback experiment. Results remain the authors' claims, not reproduced here.
- [Agent-evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), definitions, research-agent grading, environment isolation, grader/trajectory limitations and transcript review. Used as design guidance, not empirical validation of our rubric.
- [LM Studio model-list API](https://lmstudio.ai/docs/developer/rest/list), [tool-use flow and template/parser support](https://lmstudio.ai/docs/developer/openai-compat/tools), [Python tokenization](https://lmstudio.ai/docs/python/tokenization). Documentation support does not prove the installed deployment's behavior; plain-text tokenization is not an exact rendered-request measurement.
- [Qwen3.5-9B official model card](https://huggingface.co/Qwen/Qwen3.5-9B), serving/context caveats, thinking controls, agent usage and sampling/output best practices. Official family guidance is not validation of the available GGUF's lineage or performance in our smaller local configuration.

These sources deepen the first dossier's P03/P11/P17 leads and add a concrete local model-family option. All protocol-specific budgets, corpus sizes, triage thresholds and experiment sequencing are our proposed engineering judgments.
