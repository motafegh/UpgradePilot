# Broader LLM agency — local technical feasibility evidence

This dated record preserves two known-development cases across Gemma and Qwen, followed by one generic interface clarification. **Disposition: inconclusive; repair the experiment before comparing broader agency.** No protected evaluation, product architecture choice or operational authority was established.

[Reviewed results and identities](reviewed-results.json) contain every assigned trial, configuration/source hashes, measured counters and bounded reviewer diagnoses. The [protocol](../../../plans/BROADER_LLM_AGENCY_COMPARATIVE_EVALUATION_PROTOCOL.md) owns the comparison design; the [cycle record](../../2026-10-05_2052_broader-llm-agency-research.md) preserves its evolution. Live continuation belongs only to [MEMORY.md](../../../MEMORY.md).

## What actually ran

Both arms used identical frozen source maps and tools. F received scheduled investigation stages; A chose its next operation and stopping time. This prototype F had no conditional stage skipping, and its models did not reliably perform the intended stages. It is not evidence about the strongest fixed workflow.

- Original pass: eight assigned trials, 47 case inference calls; seven action-wrapper failures and one missing terminal report.
- Clarified pass: eight additional known-case diagnostic trials, 70 case inference calls; four Gemma JSON failures and four Qwen report-contract failures.
- Combined: **16 trials, 117 case calls, 174,191 input / 8,496 generated tokens, 101 dispatched tool operations, 325.918 seconds of trial time**. All ten harmless setup/execution probes are additional: total inference was **127 calls, 174,675 input / 8,640 generated tokens**. These figures exclude public source acquisition, file hashing, loading, review and publication.

| Version | Model | Case | F terminal outcome / calls | A terminal outcome / calls |
|---|---|---|---|---|
| Original | Gemma | HTTPX | Wrapper / 1 | Wrapper / 7 |
| Original | Gemma | glyphsLib | Wrapper / 1 | Wrapper / 2 |
| Original | Qwen | HTTPX | Wrapper / 7 | Wrapper / 7 |
| Original | Qwen | glyphsLib | No final report / 16 | Wrapper / 6 |
| Clarified | Gemma | HTTPX | Extra closing brace / 1 | Extra closing brace / 1 |
| Clarified | Gemma | glyphsLib | Extra closing brace / 1 | Extra closing brace / 3 |
| Clarified | Qwen | HTTPX | Report wrapper / 16 | Report wrapper / 16 |
| Clarified | Qwen | glyphsLib | Report field types / 16 | Report wrapper / 16 |

No final report passed the common contract. Earlier failures were preserved; no response was stripped, repaired, retried or promoted. The clarification changed only generic action-format/search/completion guidance in the source-access module. The two case source-map hashes stayed identical; the overall bundle digest changed because acquisition reuse receipts changed. Model order was Gemma→Qwen originally and Qwen→Gemma for clarification; Gemma was reloaded. There was one run per configuration and no controlled seed, so the prompt contrast is formative, not an independent causal experiment.

## Transport and capacity versus investigation quality

Every retained native HTTP response returned 200, input usage remained below the declared SDK-template allowance, and reported reasoning usage was zero. No trial ended on input capacity, output truncation or the time guard. Gemma's measured-input margin was 64 tokens; Qwen's was 62. Both used 16,384 loaded context, temperature 0.2 and native stateless chat with **text JSON actions**. Native function calling was not tested. [Native API request and usage fields](https://lmstudio.ai/docs/developer/rest/chat).

Actual GGUF files were hashed before loading. SDK `lmstudio==1.5.0` was reused from the existing ignored optional runtime, without changing dependencies or main. GPU ratio 1.0/Flash Attention/GPU KV settings were requested and echoed; actual per-layer device placement and CPU contribution were not independently inspected. The RTX 3070 Laptop GPU reports 8192 MiB; dated loaded-memory observations were 4737 MiB for Gemma and 6218 MiB for Qwen. Provider-reported decode rates are in the JSON, but incomplete trajectories cannot forecast a full investigation batch. Backend version, parallel capacity and prefix-cache effects were not independently characterized.

The generic clarification enabled Qwen to dispatch all 60 pre-report actions in its four trials. Its final candidates still omitted wrapper fields or used wrong report types; one also used a singular citation field. Gemma appended an extra closing brace in each terminal reply. These are interface failures, not successful semantic reports.

Qwen's clarified notebook was empty on **48/60** dispatched actions. Repeated path listings/source reads and missing relevant evidence remained. Source inspection shows an additional design weakness: the next request supplies the latest result but omits the immediately preceding action; list/search results do not consistently carry their request scope. With an empty notebook, the model loses some immediate provenance. That is an identified host-design limitation; its causal contribution has not been isolated by a separate intervention. The original Qwen trace also used regex-looking queries in literal search and generalized zero hits beyond their scope.

## Assisted source review

Review expectations were saved before output and never exposed through tools. The reviewer is the same AI, sees model/arm identities and knows the historical cases. This is formative diagnosis, with no independent protected label or learner-mastery claim.

For HTTPX, the source supports actual removal of `app`/`proxies` plus other changes; target tests use FastAPI's TestClient. The old/new Starlette reference source differs in forwarding `app`, but the target's unpinned FastAPI requirement does not establish its installed Starlette version. Its Python workflow excludes a requirements-only change; a Docker build does not execute those application tests. Rejected Qwen reports missed these obligations, concentrating on a pin or one application file. [HTTPX changes](https://github.com/encode/httpx/blob/26d48e0634e6ee9cdc0533996db289ce4b430177/CHANGELOG.md), [target tests](https://github.com/Aidan-Wallace/kubernetes-dashboard-token-api/blob/391508134b083b8f54461c0b576e8f7985c6ecb4/tests/test_routes.py), [workflow scope](https://github.com/Aidan-Wallace/kubernetes-dashboard-token-api/blob/391508134b083b8f54461c0b576e8f7985c6ecb4/.github/workflows/python.yml).

For glyphsLib, the proposed development requirements explicitly pin pytest 9.0.3, tox installs that file and invokes pytest, and the regression workflow separately installs the proposed requirements before testing. The bounded historical capture reports successful exact-head jobs across Python 3.10/3.14 and Ubuntu/Windows; this is not freshly reacquired full-log evidence. The upstream release describes a bug-fix replacement, with changes that still require relevance assessment. The rejected agent candidate missed the explicit dev pin; the fixed candidate read a partial CI page without tracing the requirements/test connection or release changes. [Development pin](https://github.com/googlefonts/glyphsLib/blob/f3cda8a94600e58d27f1bc17c99b7693718b6350/requirements-dev.txt), [tox flow](https://github.com/googlefonts/glyphsLib/blob/f3cda8a94600e58d27f1bc17c99b7693718b6350/tox.ini), [release scope](https://github.com/pytest-dev/pytest/blob/a7d58d7a21b78581e636bbbdea13c66ad1657c1e/doc/en/changelog.rst).

Some rejected candidates contain correct local observations or provisional advice. They remain rejected outputs and incomplete investigations; they cannot become clean negatives, accepted recommendations or paired success scores. No agency win/regression statistic is justified.

## Acquisition, proof and retention

HTTPX's case contains 2628 retained documents; glyphsLib's contains 1372, including three total historical CI records. Large binary/font fixtures and two oversized glyph XML files are omitted explicitly. The archive-first route failed on binary expansion, then was interrupted after a complete tree inspection showed a predictable member-count failure. Seven completed captures were preserved. The alternate complete-tree/raw-text route verifies Git blob identities and avoids downloading excluded binaries; it retained 113 target files per revision. All source revisions, omission counts and acquisition digests are in the reviewed JSON.

Engineering proof: 16 new meaningful harness/transport/composition tests plus 23 nearest existing model/planner tests pass **39/39**; touched Ruff/format, CLI help and staged/full-diff checks are recorded separately in the cycle. Controlled checks prove mechanics, not the local models' investigation competence. Product source/tests are unchanged and full product/installed/hosted suites were not rerun.

Raw sources, assembled prompts, model replies/actions, provider frames and trial traces remain under ignored `.tmp/broader-agency-pilot/` and `.tmp/broader-agency-model-identities/`. Public JSON contains identities, counters and bounded review diagnoses, without raw model content. Both owned model instances were unloaded; the final loaded-model inventory was empty. Main's independent work was inspected read-only and never merged, copied, stashed or edited.

Reproduction uses the experiment CLI with `--prepare --tree-repository googlefonts/glyphsLib`, followed by `--execute --model <owned-instance> --model-identity <precomputed-GGUF-identity.json> --sdk-site <optional-sdk-site>`. Each run needs a new name, qualified local deployment and saved corpus/code identities. The original prompt implementation is available at `55bafb39`; clarification is the later committed tool guide. Ignored source captures and local model files are not part of a fresh clone.

The justified follow-up is an experiment-design revision for complete tool-observation provenance, usable conversation memory, model-visible bounded error recovery and verified tool/report interfaces, with reasoning configuration evaluated separately. A credible fixed baseline must actually perform its intended responsibilities. More cases or a framework would not repair the identified comparison weaknesses by themselves.
