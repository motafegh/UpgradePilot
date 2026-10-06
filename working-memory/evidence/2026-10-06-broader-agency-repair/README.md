# Broader agency repair — reviewed local development evidence

Recorded 2026-10-06. Experiment execution and assisted source review; no product acceptance.

The repaired tool/history/report path supports actual multi-step investigations, visible correction, packed history and paid replay. It does **not** yet produce an advice-ready decision path on either known case. These results justify more investigation of interface and source-selection design; they do not select a winner or greater product authority.

## What was executed

Three already-local GGUF deployments: Gemma 4 E4B UD Q4_K_XL, Qwen3.5 9B UD Q4_K_XL and MiMo V2.6 Distill Qwen 9B Q4_K_L. Serial LM Studio execution used 16384 context, temperature 0.2, full GPU ratio/strict VRAM cap/KV offload/flash attention on the existing RTX 3070 laptop GPU. The final compatible-tools profile reports server-default reasoning; it is separately identified from the earlier native/off profile. No undocumented thinking flag, hosted call, model download or target execution was used.

Final executable freeze: `a83de8f3`, following implementation `73dec92d` and SDK schema repair `bc8ed7a5`. [The protocol](../../../plans/BROADER_LLM_AGENCY_COMPARATIVE_EVALUATION_PROTOCOL.md) sections 16.7–16.9 own configuration and the MiMo diagnostic exception. [The progression record](../../2026-10-05_2052_broader-llm-agency-research.md) section 11 explains implementation, failures and adaptations.

All **12/12** selected known-case assignments were executed once and source-reviewed. Gemma/Qwen entered after two fresh canaries passed. MiMo's canary performed multi-scope reads, later follow-up, notes and a valid source-linked report, but searched “canary” instead of the explicitly supplied ABSENT_CANARY_TERM and incorrectly said the token was absent. Qualification remains failed; its second sequence was withheld. Its four cases were explicitly selected before execution as unqualified diagnostics under protocol 16.9, without changing the ordinary gate, prompt, validator, sources or budgets.

| Model | Final interface qualification | Mechanically complete reports | Case calls | Case tool operations |
|---|---|---:|---:|---:|
| gemma | Two fresh sequences passed | 1/4 | 54 | 33 |
| qwen | Two fresh sequences passed | 3/4 | 51 | 106 |
| mimo | Failed exact zero-hit search; cases diagnostic only | 2/4 | 60 | 84 |

“Mechanically complete” means admitted shape and existing retained source-line references, including visible recovery where labelled. It does not mean supported claims or an acceptable recommendation. All final/partial candidates were examined, including mechanically rejected candidates. **No candidate was assessed advice-ready** in this assisted formative review.

## Assigned outcomes

| Model | Case | Policy | Saved outcome | Calls | Complete/all F artifacts |
|---|---|---|---|---:|---:|
| gemma | HTTPX | agent | report_contract_problem | 16 | 0/0 |
| gemma | HTTPX | fixed | report_contract_problem | 12 | 0/5 |
| gemma | pytest | agent | report_contract_problem | 16 | 0/0 |
| gemma | pytest | fixed | completed_ungraded | 10 | 5/5 |
| mimo | HTTPX | agent | completed_ungraded | 15 | 0/0 |
| mimo | HTTPX | fixed | report_contract_problem | 15 | 0/5 |
| mimo | pytest | agent | report_contract_problem | 16 | 0/0 |
| mimo | pytest | fixed | completed_after_recovery_ungraded | 14 | 5/5 |
| qwen | HTTPX | agent | completed_after_recovery_ungraded | 16 | 0/0 |
| qwen | HTTPX | fixed | completed_after_recovery_ungraded | 14 | 4/5 |
| qwen | pytest | agent | completed_after_recovery_ungraded | 12 | 0/0 |
| qwen | pytest | fixed | provider_or_capacity_problem | 9 | 2/2 |

F follows upstream → consumer → conditions/CI → synthesis → challenge; A chooses its order and stopping. Both share source tools, observation scope, history/replay, report interface and per-trial ceilings: 16 calls, 245760 input, 32768 generated tokens, 48 operations, 8 MiB observations, 1200 seconds; 1024 ordinary/4096 report output reserve. A complete artifact establishes that a structured work product exists, not that the stage investigated the right evidence. Arm order is F/A on HTTPX and A/F on pytest, fresh trial state throughout.

## Source review: what the mechanics missed

HTTPX 0.27.2→0.28.1 requires checking the 0.28.0 `app`/`proxies` removals, the target's indirect FastAPI/TestClient exposure, reference Starlette client forwarding, actual installed-version uncertainty and CI activation. The target's requirements-only change is excluded by the Python workflow's path filter. Reference old/new Starlette sources are comparisons, not evidence of the target's resolved runtime.

Gemma produced useful target clues but did not trace that chain. Qwen's fixed report recognized indirect exposure while leaving the upstream check unperformed. Qwen's agent examined more source and used two paid event replays, yet called the 0.28.1 SSL fix a deprecation and attributed a 0.23.2 RawURL reversion to 0.28.1. Exact frozen anchors: `httpx-new:CHANGELOG.md:L9` is the SSL fix; L19 preserves standard verify=True/False behavior; L28/L29 remove proxies/app; L164 is under the 0.23.2 header at L154. Its inspected Python trigger did not reach the report. The fixed TestClient claim cited target test line 1 (`import pytest`), although TestClient is line 2.

pytest 9.0.2→9.0.3 requires pin/input-constraint interpretation, installation into the executed test environment, ordinary matrix/head results, regression reinstall/run and release materiality. Frozen anchors: `requirements-dev.in:L5` is pytest>=2.8; L6/L7 directly declare pytest-randomly/pytest-xdist; `tox.ini:L10/L11` consume both requirement files; ordinary CI L27/L28 specifies Python 3.14/3.10 and Ubuntu/Windows; regression workflow L43/L46 reinstalls and runs regression tests. The available release-9.0.3 announcement calls this a bug-fix drop-in replacement. A permissive constraint and patch number alone cannot establish that chain.

Gemma's fixed pytest report had valid pin and regression-command references but missed installation, upstream and full CI obligations. Qwen's agent called directly declared plugins transitive and stopped without the test path/release check. Qwen's fixed trial had two partial artifacts and a 60-second HTTP read timeout during call nine; no final report exists. Partial CI/fixture clues are retained, but it never located the actual upstream release file or inspected the test installation configuration. Its plugin-absence language exceeded the examined page.

MiMo's HTTPX agent identified removals/deprecations relevant to the update interval, but assigned the 0.28.0 changes to 0.28.1 and the 0.27.1 zstd addition to 0.27.2. It read and replayed the target Python workflow yet reported it unexamined, and did not trace TestClient/Starlette or the trigger exclusion. Its fixed HTTPX candidate claimed low-risk standard direct Client usage without establishing that path, and never read the available changelogs. Bare-path references failed the contract.

MiMo's pytest agent read tox, fixture source, all CI capture pages and the release material. It recovered correct bug-fix clues, but assigned the 9.0.2 terminal-progress change to 9.0.1 (`pytest-old:doc/en/changelog.rst:L34/L40`), gave the wrong 9.0.3 date (the retained header at new L34 is 2026-04-07), and invented a Python 3.12/Windows regression-job binding absent from the capture. Regex-like alternatives were searched literally; their zero hits cannot establish absent fixture use, particularly after actual fixture lines were delivered. Its fixed pytest artifacts correctly identified direct plugins and the bug-fix/drop-in announcement, yet cited pygments at requirements-dev.txt L63 for the pytest pin and repeated stale claims that upstream/CI had not been read. Five complete artifacts did not establish five adequately performed investigations. [Individual reviews and coverage](reviewed-results.json) preserve these useful clues, failures and the model's failed qualification separately.

## Harness failures, interface limitations and costs

The first preferred probes used zero inference calls because the SDK rejected aliased Python containers in tool schemas as cycles. JSON roundtripping at the SDK boundary preserved schema values and removed alias identities. The next preferred attempt used one call/model, then exposed the SDK's required `toolCallRequest` history wrapper. Both were harness failures, preserved under their own freezes, rather than model incapability. Actual SDK source and discriminating checks drove each repair. Neutral stage turns and native call IDs now survive SDK/wire history.

Separately selected native/off probes used ten responses and failed the first sequence: Gemma appended a tool marker to follow-up JSON; Qwen emitted undeclared singular `note`; MiMo emitted prose/XML-style calls. Two visible corrections were included, with no decoding salvage. That alternative was not repeated. Final compatible/default-accounted qualification used eight calls each for Gemma/Qwen and five for MiMo, plus the preceding one actual preferred call/model; each remains within the twelve-call preferred qualification ceiling.

All current-increment probes, failed attempts and cases total **199 attempted inference calls / 198 accounted responses**, **1,610,630 known input tokens**, **88,294 known generated tokens**, including **47,271 reasoning tokens**, and **260 tool operations**. These token totals are **lower bounds** because Qwen's ninth pytest F attempt has no response usage; it is not counted as zero cost. The eight preceding responses in that trial account for 70144 input/3050 generated/1427 reasoning tokens. Its timed-out request measured 15210 input tokens with 1024 output reserve, but a measured request is not actual provider usage. [The JSON](reviewed-results.json) includes per-trial counters, completeness flags, receipt reconciliation and artifact hashes. Earlier v0.1 pilot costs remain in their own evidence.

Current interface limitations matter to interpretation: the guide no longer gives an exact citation-format example; genuine diff-packet/zero-hit/event evidence has no admitted final-reference form; source-text search does not locate a path merely because the filename exists; numeric tool schemas omit page bounds enforced in the guide/host. Several candidates failed references to packet/events even when the underlying pin fact was real. F's seven nominal retrieval calls plus batching and light stage instructions are not established as a strongest fixed baseline. These are design debts, not permission to salvage failed output or infer that every rejected statement is false.

## Verification and limits

Focused mechanics/composition proof: **50/50** (27 harness/transport/history/recovery/source checks plus 23 nearest planner/extractor checks), using the existing main venv with this research tree on PYTHONPATH. Focused Ruff/format and diff checks pass. Live receipts demonstrate same-instance binding, retained tool IDs, measured fit, counted correction and actual packed/replayed history. Code and corpus hashes are unchanged throughout the final batch. Existing optional SDK runtime is lmstudio 1.5.0/Python 3.12.3; this was not a fresh accepted product installation. All research-owned models were unloaded at execution closure.

Frozen cases: HTTPX target base b065646e4b7b894964567950f9ad770b02c136c2 / head 391508134b083b8f54461c0b576e8f7985c6ecb4, corpus 6e4ab534a86aaf9d3ebc23f66391f0976faa11c5e1602ba4f12b97b25dd0abe0; glyphsLib base 044f19e4b1437bfc4343592486f4e3c6040306d9 / head f3cda8a94600e58d27f1bc17c99b7693718b6350, corpus 8c8ef1a31b2c009d83803b8c94ce9a33af201de4ae49513e0a978f186d237101. Broad retained text excludes declared binary/oversized material; CI captures are bounded historical observations, not fresh full logs or installed environments. No reviewer reference entered model requests.

This is a known-case, assisted development review by the same AI with visible model/arm labels. It is neither independent protected adjudication nor a reliability estimate. The combined interface/history/recovery/budget/reasoning redesign cannot isolate an agency or memory effect. No full product/experiment regression, target execution, independent usefulness assessment, repeated-run reliability, protected batch, adoption or learner-mastery proof is claimed.

The evidence supports a next design responsibility around evidence references, source orientation/search semantics and fixed-stage sufficiency, with an unchanged whole-set retest and independent new cases before any substantive architecture/authority decision. It does not authorize that implementation or select broader/protected execution by itself. Raw requests, source corpus, full candidates and provider reasoning remain under ignored .tmp; this public evidence contains reviewed facts, operation scope, costs and hashes only.
