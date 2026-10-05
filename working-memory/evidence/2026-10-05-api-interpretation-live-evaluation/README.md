# Source-only interpreter — measured first real-model development pass

Date: 2026-10-05. Outcome: **FAIL / REVISE**, with no semantic admission or product promotion. The requested checks were executed; negative results are preserved rather than rescued. [Reviewed per-case evidence](reviewed-results.json) contains bounded outcomes, token counts, deployment/settings and pre-inference source/code/request identities. Raw requests, replies and rejected frames remain in ignored `.tmp/api-interpretation-live/live-development-v1/`.

The maintained `gemma-4-e4b-it-ud` Gemma4/Q4_K_XL deployment was explicitly loaded before measurement. Its existing defaults selected **4,096** context tokens; neither that number nor the advertised 131,072 maximum was assumed to prove fit. The actual loaded instance, SDK chat template and tokenizer measured all 18 nonempty inputs before inference. Calls used temperature 0, seed 0 and the frozen **1,536-token completion ceiling**, serially, once per case. The nineteenth empty input did not infer. No context/model/prompt/schema/input/limit change or corrective retry occurred after output.

## Capacity, provider and contract results

All 18 requests fit measured input + schema allowance + reserved output. Full HTTPX: 1,816 chat-template tokens + 668 schema allowance + 1,536 output reserve = 4,020, leaving 76 tokens under the conservative accounting. Schema allowance is SDK tokenization of the complete response-format JSON, not a claim about the exact OpenAI handler's schema accounting. Every provider-reported prompt count was the SDK chat count + 1 and remained below the allowance. The full HTTPX actual prompt was 1,817 tokens.

All 18 HTTP calls returned 200. Sixteen completed outputs passed the frozen JSON-schema shape checks, demonstrating bounded operational schema execution on this deployment; this does not attest how the provider internally enforced the schema. Two larger cases, I001 full HTTPX and I017 partial HTTPX, stopped at the completion ceiling. Their usage receipts report 1,536 completion tokens, including respectively 845 and 1,406 reasoning tokens. Thus **input context fit passed; output-budget adequacy failed**. A larger context alone would not remove a fixed completion ceiling.

Three completed shape-valid responses (I003/I007/I011) supplied null subjects without the required nonblank explanations. This conditional requirement is in the frozen prompt and decoder, rather than encoded in schema shape. I018 used `S1`/`S2` where real line IDs were required in its unassessed entry. The decoder correctly rejected all four. No partial proposals were salvaged. Twelve responses were admitted structurally and by source reference: eleven with 14 observations altogether, one with no observations. Ten observations had null subjects; this is allowed with explanation, but unnecessary subject omission limits future structured consumption.

Summed case latency was 226.162 seconds, excluding model loading and tokenization/preparation. Provider receipts total 18,522 prompt and 16,117 completion tokens. There was no usage-accounting mismatch, hidden retry or no-inference-control HTTP frame.

## Assisted meaning and omission review

The separate frozen expectations were consulted only for review. This is AI-assisted known-development review, not independent accuracy or a protected-set score. Cases are assessed by propositions, not exact output wording or object count.

- **Critical semantic failure, I014:** ambiguous option cleanup became an affirmed current removal. Real quotation recovery does not establish this meaning. A null subject and explanation did not make the claimed removal uncertain.
- **Additional classification issue, I005:** current deprecation and planned removal were correctly separated, but replacement guidance was also emitted as a current behavior change unsupported by the passage.
- **Representation caution, I009:** the summary preserved non-removal and did not affirm removal, satisfying the frozen negation proposition. Its `behavior_change`/`affirmed` fields are nevertheless a weak encoding of a negated removal and cannot justify a downstream negated-removal classifier.
- **Useful controls:** supported removals, paraphrase, future timing, historical timing, changed subject, acknowledgments and instruction-shaped source had useful reviewed outcomes. The two Retry options shared one supported observation; this was not scored as an omission.
- **Six unavailable semantic outcomes:** I001/I003/I007/I011/I017/I018 supplied no admitted proposals. Their positive and coverage obligations remain unproved. Rejected/truncated fragments are not semantic passes, clean negatives, or an exhaustive omission count. In particular, the full-window other-change coverage requirement remains unproved.

The set fails development acceptance because useful controls do not offset a critical wrong meaning, missing usable full-window output or rejected required positives. Protected evaluation, a second ordinary real target/PR case, independent usefulness, target exposure and product admission remain outside this proof.

## Preservation and engineering proof

The full HTTPX input uses the normal source producer over the retained ordinary acquisition packet; it is historical acquisition plus fresh real inference, not a fresh PR/network acquisition. urllib3 excerpts and constructed/partial controls retain their weaker calibration scope. Independent target and adapter branches remain available despite interpretation failure.

The failed I001 packet saved and reopened exactly. A separate offline CLI subprocess also returned the same packet. Its exit **1** honestly reflects the preserved `provider_problem/output_truncated`; recovery itself succeeded. The packet is below the existing 8 MiB bound. Digests prove consistency relationships, not source authenticity.

Final reviewed experiment tree: **128/128 active API-trial tests**, including eight added evaluator/observer tests over the 120-test baseline. Focused new/interacting checks previously passed 39/39. Touched Ruff check/format checks pass. All nine preparation artifacts and four pre-inference source identities remain unchanged. Product source, active product tests, project dependencies and hosted workflows were not changed; full product/installed and unrelated experiment suites were not rerun. Existing unrelated governance/broader experiment debt remains outside this result.

## Reproduce and compare

Use an already loaded maintained LM Studio instance at the configured loopback endpoint. Optional `lmstudio==1.5.0` is isolated evaluation tooling; it was installed under ignored `.tmp/api-eval-sdk`, not added to project dependencies. [Official tokenizer/template documentation](https://lmstudio.ai/docs/python/tokenization) and [native load documentation](https://lmstudio.ai/docs/developer/rest/load) describe the public measurement/loading interfaces. The measured settings and limitations above, rather than documentation alone, establish this run's evidence.

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest \
  experiments.tests.test_api_change_source_acquisition \
  experiments.tests.test_api_target_context \
  experiments.tests.test_api_python_bindings \
  experiments.tests.test_api_adapter_exploration \
  experiments.tests.test_api_public_pr_context \
  experiments.tests.test_api_change_interpretation \
  experiments.tests.test_api_change_interpretation_evaluation

# Preparation only; must choose a new name. Existing runs cannot be overwritten.
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m experiments.api_change_interpretation_evaluation \
  --sdk-site .tmp/api-eval-sdk/lib/python3.12/site-packages --name NEW_NAME
# Add --execute only for an explicitly selected new real-model pass.
```

The next design question is how to budget full-window reasoning/output and improve semantic uncertainty/subject representation in a separately frozen revision. Larger loaded context may be necessary to reserve more output; it does not repair meaning by itself. Any revised run must retain this failed baseline and compare equivalent inputs without weakening accepted guards or answer-selected source reduction. This record recommends that question; it does not authorize a changed role or perform a revised pass.
