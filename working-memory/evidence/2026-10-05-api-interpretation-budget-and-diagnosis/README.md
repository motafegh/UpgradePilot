# Completed output-budget repair and causal diagnosis

Started 2026-10-05; reviewed handoff completed 2026-10-06. Ali authorized increasing capacity enough to obtain the larger answers and investigating why the model produced null subjects, bad references and wrong meanings. The [first failed pass](../2026-10-05-api-interpretation-live-evaluation/README.md) remains unchanged. [Budget comparison](budget-comparison.json), [frozen diagnostic protocol](diagnostic-protocol.json) and [assisted causal review](causal-review.json) preserve the separate proof classes. Raw requests/replies, model reasoning and rejected frames remain ignored local evidence.

## Budget repair — verified on all frozen inputs

Explicitly reloaded the same maintained Gemma deployment at **16,384 context**, following the native load/echo-config pattern verified in JobHunter's current runtime source. Native receipt and SDK independently confirm the applied context. The experiment now defaults to **8,192 completion tokens**, and its evaluator exposes an explicit recorded budget. Capacity accounting derives the reserve from the actual request. Historical saved packets re-render using their recorded budget, preserving both the original failed 1,536-token packet and new packets without weakening source/request consistency.

All 18 nonempty requests were measured and frozen before their responses. Only `max_tokens` changed in the request bodies; source inputs, prompt/schema, model, temperature 0 and seed 0 remain the same. Calls were serial. Full-window accounting: 2,484 input tokens including conservative schema allowance + 8,192 reserve = 10,676 within 16,384. Native loading changes deployment identity/configuration, so this is one capacity intervention rather than an isolated experiment on each setting.

**All 18 HTTP calls finished with `stop`; zero truncations.** Full HTTPX finished with 11 observations at **2,672 completion tokens**, partial HTTPX with 10 at **3,067**. Those exceed the old ceiling and demonstrate the immediate truncation mechanism. Required removal and other-change propositions are now recoverable within their complete/partial scope. The new full packet opens through the real offline CLI with exit 0 and exact equality; the historical failed packet still opens identically with its honest failure state. Saved new packet: 708,945 bytes, below 8 MiB.

The sixteen previously completed final replies are byte-identical to the first pass. Their three missing-explanation failures, one invalid-reference failure and critical cleanup/removal error persist. New totals: 14 structurally/source-admitted responses, 13 with 35 observations; 31 observations have null subjects. This closes the selected output-budget debt, **not semantic admission**. Summed case latency is 261.5 seconds, excluding loading/preparation, with 18,784 completion tokens. No source shortening, model substitution, correction loop or hidden retry occurred.

## Why the other failures happened — discriminating evidence

Manual inspection first established that source names appeared in summaries despite null subjects. The full ordinary HTTPX input also has null subjects despite a supplied target dependency interval, so missing calibration context cannot explain them all. Sixteen separately frozen diagnostic calls then changed one generic instruction block or schema visibility/generation condition. Two further frozen plain-language comprehension calls tested the task outside its fixed taxonomy. None supplied expected answers or promoted a revised role.

| Contrast | Observed outcome | Supported diagnosis |
| --- | --- | --- |
| Clarify source-named subject versus fully known owner | Named subjects recovered in 4/4 selected cases | Subject granularity and instruction interpretation contribute; missing source facts are not the explanation for these nulls |
| Include the exact schema in readable instructions | Subjects recovered in 3/3 selected subject cases; conflicting-source references still failed | Missing explicit readable structure contributes but does not explain every failure |
| Repeat the conditional explanation rule alone | Null subject/null reason still failed in I003 | Cross-field compliance is unreliable; a stronger reminder alone is insufficient |
| Clarify exact line IDs in both arrays | I018 references passed; typed negation remained weak | Section/global limitation references were confused with required line-level citations |
| Clarify kind/assertion/ambiguity semantics | I009 became removal/negated; I014 still asserted removal; I005 regressed | Some field mapping is instruction-sensitive; tested clarification is not a reliable general repair |
| Readable schema without output constraints | Three replies contained Markdown JSON fences and failed strict JSON admission | Removing constraints changes failure behavior; it is not an accepted fix |
| Plain-language source comprehension | I005 correctly separated current deprecation, future removal and advice; I014 repeated cleanup without asserting removal, but did not explain operational ambiguity | Useful comprehension is available, while translating it into the taxonomy remains unreliable; ambiguity mastery is unproved |

The original instructions discussed subjects near prohibitions on invented owners/qualified symbols. Clarifying that a source-described argument/function/method can be a subject even without full owner knowledge recovered real names without adding source facts. This supports a prompt/contract interpretation contributor; it does not uniquely prove which wording or internal model mechanism caused each null. Some repaired subjects still name `Factory.build()` while leaving the added parameter only in the summary, so structured precision remains a review obligation.

Our authored baseline messages contained prose rules but no literal schema. The primary [llama.cpp grammar documentation](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md) distinguishes schema output constraints from a schema shown in the prompt. Actual prompt receipts match SDK-rendered messages plus one token, consistent with this separation; the readable-schema contrasts supply further behavioral evidence. The installed server's internal implementation was not inspected. We do not claim a nullable-grammar bug: the unchanged schema can emit source-named strings after a generic subject clarification.

I003's null-subject/null-reason pair exposes unreliable conditional compliance. The schema allows each null independently; the decoder correctly owns the additional relationship. Elsewhere the model can supply explanations for null subjects, so the evidence does not establish an absolute backend inability. Fixing unnecessary nulls avoids those three specific rejections but does not prove correct treatment of genuinely unspecified subjects.

For I018, the model tried citing whole-section/global limitations through strings that do not identify actual supplied lines. Explicit identifier granularity corrected this example; showing the schema alone did not. Source membership validation remains necessary. The corrected references did not repair the meaning fields.

For meaning, budget-only reproduces the original failures exactly. The cleanup passage remains definite removal even under a generic ambiguity instruction. The I005 semantic clarification retained deprecations but demoted its explicitly planned removal to unassessed material, still classified guidance as a behavior change, and emitted one literal `"null"` subject string. These regressions disprove a simple “add stronger instructions and call it solved” approach. Plain I005 comprehension demonstrates that the source facts are accessible; reliable mapping to kind, assertion, timing and subject is the missing behavior. The exact training/quantization/logit causes remain undiagnosed, and a changed task cannot establish original-role acceptance.

## Engineering and handoff boundaries

Final active API-trial regression: **130/130**, from 128 baseline plus two meaningful budget/compatibility tests. Focused interacting proof: 41/41. Touched Ruff check/format and CLI help pass. One initial new recovery assertion compared in-memory tuples against JSON lists; the test was corrected to compare the existing canonical packet hashes, not by changing behavior. All nine semantic preparation assets and four inference-source identities remain unchanged after freeze. No product/shared source, project dependency or hosted workflow changed; broader product/installed/unrelated experiment suites were not run.

Reproduce budget preparation/execution with an already loaded, verified maintained instance and a new run name:

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m experiments.api_change_interpretation_evaluation \
  --sdk-site .tmp/api-eval-sdk/lib/python3.12/site-packages \
  --name NEW_NAME --max-output-tokens 8192
# Add --execute for a selected new pass after preparation; existing names cannot be overwritten.
```

The public diagnostic protocol records selected cases, generic instruction text, exact transformations, capacities and request hashes. Reconstruct a contrast from `prepare_request(calibration_source_input(...))`, append the recorded generic system block (or exact sorted schema), measure/freeze, call the same bounded provider, and apply the original decoder. The unconstrained arm removes `response_format` while retaining conservative schema allowance in measurement. The plain-comprehension protocol is retained in the causal review. One-run scripts and full request bodies remain local; this is assisted known-development diagnosis, not a reusable accepted semantic oracle.

Recommended next responsibility: design a separately versioned source-only contract/prompt that makes structure readable, clarifies subject granularity and line references, and addresses jointly reliable kind/polarity/timing/uncertainty plus supplied-material-only limitations. Compare the entire frozen set and a newly frozen independent case rather than accepting isolated repaired examples. **Budget repair is verified; the semantic role remains FAILED / REVISE.**
