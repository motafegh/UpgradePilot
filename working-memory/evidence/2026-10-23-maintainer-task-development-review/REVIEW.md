# Maintainer task review: useful narrow facts, missing acquired change context

Recorded October23,2026. Starting source horizon `d3e0abe1`; executable source remains unchanged. [Cycle](../../2026-10-23_maintainer-benefit-review-and-milestone_cycle.md). Ali explicitly requested the assistant perform the review. This is **exposed AI-assisted development review by the implementer**, with prior case/answer exposure. It supplies prioritization evidence, not independent maintainer usefulness, a blinded baseline, time-saving measurements or semantic acceptance.

## Question and comparison basis

Can a reviewer identify the exact update, recover a material supported change/finding, distinguish its missing applicability premise and locate the relevant source without inventing compatibility or a maintainer action?

Inspect the same frozen normal-source packet with and without the actual normal report. The source-only answers below are analyst reconstructions after prior report exposure; they are not observed untreated reviewer outcomes. No live browsing, native evaluation, model trial, target execution or new case was performed. Missing evidence is not silently supplemented from older simulations.

The [inspection recipe](inspect_retained_cases.py) and [receipt](inspection.json) verify all21 retained normal HTTP observations/189,977 decoded bytes:12 complete bodies and9 unconsumed status-only404 responses. Both report/source-index/capture public copies equal private originals; each capture's96 product-source hashes match current source. Strict report decoding passes. A zero-length unconsumed file is not an empty server response. Both captures retain equal first/final PR body text, without establishing atomicity or historic decision-time content.

## HTTPX: diagnostic explanation, little help with the visible change mechanism

Source packet: [original capture](../2026-10-22-matched-report-source-capture/REVIEW.md), [unchanged report](../2026-10-22-matched-report-source-capture/report.txt), [index](../2026-10-22-matched-report-source-capture/source-index.json).

| Task | Source-only reconstruction | What the actual report adds / omits |
| --- | --- | --- |
| Exact update | PR/diff establish HTTPX0.27.2→0.28.1 in requirements.txt at base b065646e4b7b894964567950f9ad770b02c136c2/head391508134b083b8f54461c0b576e8f7985c6ecb4 | Consolidates exact identity; does not claim installation or compatibility |
| Material change context | PR JSON `body` includes copied release/changelog sections. They describe `app`/`proxies` removal, distinct `cert`/string-`verify` deprecations and other changes | The report omits this context. It does not establish target exposure or any API-impact finding |
| CI strength | The captured exact-head/event query returns zero runs | Names the scoped query limitation and no admitted runtime candidate. Neither means CI never existed |
| Package artifacts | Both releases list a universal wheel and source distribution; explicit filename tag sets are equal | Reports no candidate inside the bounded published-wheel-loss horizon. That narrower negative is useful, not complete absence of impact |
| Missing premise | No target usage/caller/framework resolution evidence is in this packet. Copied prose is not independently verified upstream code or authority | Correctly withholds runtime/compatibility/action claims, but repeats upstream prerequisites without exposing available copied context |
| Next evidence | Relevant target use and exact source/adapter relationship would be discriminating if acquired under an admitted method; their actual outcome is unknown | Does not supply a specific admitted check/action. This review's diagnostic question is not a product-generated permission |

The PR body is9,348 characters. [Receipt](inspection.json) locates the first `app` removal at decoded-body character offsets1387–1449 and the `cert` deprecation at966–1014, with hashes; each appears twice in copied sections. Two copies are not independent corroboration. Release prose attribution supports saying what the PR description reports, not asserting that an exact target will break. The visible changed-file patch contains a ranged FastAPI declaration, which does not establish an installed Starlette version or forwarded argument.

**Development judgment:** retain the report's identity, narrow artifact-negative and proof-strength explanation. For the main task of understanding the visible update mechanism, it is incomplete: the ordinary input contains material attributed context the report lacks. No independent task benefit or action improvement is established.

## OpenCV: real inventory summarization, unresolved target effect

Source packet: [original capture](../2026-10-22-opencv-matched-report-source-capture/REVIEW.md), [unchanged report](../2026-10-22-opencv-matched-report-source-capture/report.txt), [index](../2026-10-22-opencv-matched-report-source-capture/source-index.json).

| Task | Source-only reconstruction | What the actual report adds / omits |
| --- | --- | --- |
| Exact update | PR/diff establish opencv-python4.2.0.32→4.8.1.78 at base7758d066080f180f8296887ed89b7c723a54706a/headf32ad2d23a9abee47c566dfbed2b822d953a09e2 | Consolidates exact identity and requirements.txt transition |
| Material artifact finding | Old registry inventory has27 wheels/no sdist; proposed has6 wheels/one sdist. Explicit compressed filename-tag expansion yields27 removed/8 added exact tags | Adds a computed inventory distinction and explicitly withholds target installation failure. The receipt checks full tag sets using direct filename-field expansion, without the production owner or packaging wheel parser |
| Material copied context | The PR body includes a Python3.6 support-drop statement under its4.7.0.68 section and other changes. The release excerpt explicitly says it is truncated | Context/coverage limitation is absent from the report. The copied statement is not the accepted grounded support-drop contract |
| Missing premise | Target Python/platform/ABI, selected installer behavior and source-build outcome are not established by these bodies | Correctly retains no target associations, unresolved applicability and unknown source-build success |
| CI/action | Zero runs returned by the captured exact-head query; no target execution witness | Retains no runtime candidate and explained abstention. Neither exact tag loss nor sdist availability earns an action |
| Next evidence | A justified exact target environment/usage observation could distinguish compatible wheel versus fallback paths; source-build success would remain separate | Reports the source-build unknown; no executable target check is selected or performed |

The PR body is5,900 characters. Support statement offsets2839–2866 and truncation marker3360–3375 refer to decoded JSON `body`, with source hashes in the receipt. They are not line references into an independently retrieved upstream file. No manual Python3.6 target conclusion from the older simulation entered this review. The proposed `cp37-abi3` inventory cannot be reduced to27 broken environments: exact tag disappearance and compatible target tag alternatives are different propositions.

**Development judgment:** the artifact inventory calculation is a concrete narrower contribution beyond a PR prose summary. Its practical task benefit remains unmeasured, and target relevance stays unresolved. It also omits already acquired copied support context, so neither report length nor artifact detail makes this a complete update explanation.

## Cross-case findings and earliest owner

1. **Material context is acquired but not carried into product knowledge.** `GitHubPullRequestClient.get_pull_request` receives the full PR JSON and `_parse_pull_request` constructs identity fields only; `PullRequestIdentity` has no description. `AcquiredDependencyInputs`, normal native capture and report projection receive that reduced boundary. A renderer cannot faithfully recover missing body text from identity or a URL. [Provider](../../../src/upgradepilot/github/pull_request.py), [integration](../../../src/upgradepilot/investigation_inputs.py), [native capture](../../../src/upgradepilot/workspace/native_capture.py), [report](../../../src/upgradepilot/report_projection.py).
2. **This is a supported capability/retention gap, not a reproduced violation of the existing identity-parser contract.** A selected new source consumer can justify retention at the earliest producer seam. It cannot justify bypassing publisher provenance, upgrading copied text into authoritative release evidence, or injecting model conclusions. PR descriptions are mutable observation-time content, not immutable head-commit files.
3. **Meaning and observation must stay separate.** The copied statements make a source-aware development question possible. They neither establish complete release coverage nor automatically admit a Python-support/API semantic result, target applicability, package execution or action.
4. **Presentation has useful scope discipline and substantial repetition.** HTTPX contains273 lines/1,518 whitespace-separated words,9 unknowns and17 source entries; OpenCV286 lines/1,664 words,10 unknowns and18 sources. Several sections repeat the same missing upstream prerequisite and generic consequence. These counts describe output, not measured cognitive burden. Simplification is plausible, but compressing prose alone would not restore absent context.
5. **A third live capture is not needed to establish this missing transfer.** A positive support-drop case may later provide regression/contrast evidence. It cannot repair loss of the description in these two existing inputs. Keep its source/model budget and the independent three-pressure pilot separate.

## Investment disposition

Prefer a bounded design of **normal PR-description preservation and inspectable, attributed change context** before another capture or broader interpreter. The selected user outcome is the ability to recover the material context already supplied by the PR and distinguish it from evaluated findings. Retention is an enabling step, not a usefulness result.

The design should settle the minimal producer-owned observation record, content/mutability/size states, transfer through native/application/report consumers, saved-report compatibility and a usable source-inspection route. Existing `ReportSource` supports retained text for `pull_request`, but the current renderer only lists source metadata. Simply adding content to JSON does not prove human access. Avoid automatically dumping long raw HTML, semantic keyword extraction or a parallel acquisition graph. Independent usefulness, automated semantic interpretation and broader target discovery retain separate owners/gates.

Strongest counterargument: a maintainer can already open the PR description; retaining it might merely duplicate accessible material. Therefore require a concrete offline/source-inspection or downstream-consumer obligation and a useful bounded display before Build; if these cannot be demonstrated proportionately, stop/narrow that design rather than build a storage feature to call it progress. The supported milestone is access and attribution, not broad change understanding or a positive recommendation.

This review does not justify a new model run, a semantic judge, positive maintainer action, general runtime expansion or rewriting existing publisher/correlation owners. It also does not establish independent reviewers unavailable; Ali selected self-review for this responsibility. Independent usefulness remains unestablished.

UP-SKILL:upgradepilot-repository-audit
