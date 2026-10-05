# API interpreter readiness — preparation before cycle selection

Date/time: 2026-10-05 19:36 Asia/Tehran.
Session status: ACTIVE — readiness checks completed; joint cycle-selection discussion pending; formal Build cycle not opened.
Primary responsibility: bounded Planning/Design preparation and non-destructive operational verification.
Owner: [API-change/target-exposure feasibility plan](../plans/UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md).
Previous: [closed interpretation preparation cycle](2026-10-05_1617_api-change-interpretation-preparation_lbd-cycle.md).
Skills: `UP-SKILL:upgradepilot-planning-design`, `UP-SKILL:upgradepilot-working-memory`.

## Session anchor and authorization

Ali requested recording the prerequisites discussed during re-entry, executing them immediately, and preserving their results before jointly deciding whether/how to start the next cycle. This authorizes the readiness record, relevant live-state reconciliation and bounded read-only checks. It does not open interpreter Build or semantic evaluation.

Initial main/origin horizon: `a9d34fd7c1c628e96a9658bdbee67813b51571e9`, aligned after the preceding fetch. The unrelated untracked `2026-10-03_broad-project-and-future-plans-audit_lbd-cycle.md` is preserved outside scope. The preceding preparation cycle remains CLOSED with D explicitly deferred; actual whole-design learner ownership remains unestablished.

## Selected checks and status

1. DONE — reconciled acquisition → source representation → adapter recovery and the separate product support-drop role. New interpreter implementation is still absent.
2. GREEN — nine frozen files, 19 input/case pairs, 20 sections, 75 lines and 734 contiguous spans checked; schema valid, evaluator fields excluded, all review statuses still `not_run`.
3. GREEN for reachability/inventory — three model metadata endpoints HTTP 200 through direct loopback without credentials/proxy. Maintained model present, currently unloaded; effective deployment unverified.
4. DONE as readiness diagnosis, exact fit UNESTABLISHED — no frozen executable renderer, loaded model or local tokenizer/SDK available. Metadata maximum context is not the effective context. Actual fit remains a before-inference obligation.
5. GREEN for focused trial/runtime baseline — five API trial modules pass 100/100; `pip check` passes. Governance doctor FAILED on a pre-existing unrelated documentation marker; not hidden by the focused pass.
6. DONE — evidence and proposed boundary consolidated below; joint decision and formal cycle entry remain pending.

## Proportional procedure adaptation

Circumstance: Ali explicitly requested immediate pre-cycle prerequisite checks after current-state onboarding and before deciding to open a formal cycle. Normal substantive work uses a new canonical cycle with A1/A2 gates. Applying another full cycle here would duplicate the orientation and prematurely imply that the proposed Build was selected. Chosen route: one dated preparatory session record, bounded checks and a decision handoff; no formal Build phase status or learner mastery claim. Effect: source behavior, semantic role and product authority remain unchanged; actual proof gaps are retained. Required reconciliation: `MEMORY.md` points to this preparation while retaining the closed cycle/learning debt; an agreed later cycle initializes its own A0/A1/A2 and single cycle record.

## Proof boundaries and exclusions

No model inference, target execution, model/server replacement, automatic retry, dependency installation, source/test implementation or product adoption is selected. Read-only provider metadata does not prove structured-output support or exact context fit. Existing controlled-provider tests do not prove real-model API meaning. Frozen expectations remain evaluator-only; raw prompts/responses and rejected archives remain local. Runtime configuration changes require a separately justified decision.

## Progressive findings

Initial source inspection confirms `api_target_context_smoke.py` is an acquisition/static-context entry with no model interpretation. Existing support-drop inference has a separately admitted domain contract; only its public loopback session factory is a candidate for fitting transport reuse. The new API prompt, decoder, grounding and results remain experiment-local. The proposed complete engineering path is acquisition → model proposal → source/reference validation → saved recovery, preserving independent context on inference failure.

### Frozen input and baseline checks

[Artifact readiness evidence](evidence/2026-10-05-api-interpreter-readiness/artifact-readiness.json) records fresh local integrity/representation checks. All nine file hashes/sizes match the frozen preparation. The 19 input IDs pair with unique evaluator cases and all case reviews remain `not_run`. Exact line reconstruction and every contiguous span within each section pass; expected/forbidden/review fields do not occur in producer inputs. JSON Schema metaschema validation used already-installed system `python3`/`jsonschema`, not a new project dependency. This does not implement a runtime decoder or semantic evaluator.

The retained ordinary packet SHA-256 remains `1e79f2b75abd1cbaf79a7deb61fec1d8f4b9ee68cbd9834c586443ac6976a5dc`, and all six saved producer-code hashes match current experiment source. This establishes dated acquisition integrity, not a fresh ordinary external run. The known ordinary HTTPX window contains 1,367 source characters; the schema is 3,814 bytes and template artifact 3,530 bytes. These measurements are deliberately not token estimates; the template artifact includes explanatory Markdown and is not the exact runtime request.

Fresh baseline command: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest experiments.tests.test_api_change_source_acquisition experiments.tests.test_api_target_context experiments.tests.test_api_python_bindings experiments.tests.test_api_adapter_exploration experiments.tests.test_api_public_pr_context` — **100/100 PASS**. `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pip check` — **PASS**. No executable code was changed; no full product, unrelated experiment suite, fresh installation or live PR acquisition was run. The prior broader experiment-suite failures remain historical disclosed debt rather than being relabeled fixed by this trial pass.

### Provider and capacity findings

[Provider metadata](evidence/2026-10-05-api-interpreter-readiness/provider-metadata.json) records HTTP 200 from `/v1/models`, `/api/v1/models` and `/api/v0/models` at `http://127.0.0.1:18080`, with `requests.Session.trust_env=False`, no credentials and redirects disabled. Only the maintained pilot metadata is retained; unrelated model inventory is omitted. `gemma-4-e4b-it-ud`, `gemma4`, `Q4_K_XL` is listed; native v1 has no loaded instances and v0 says `not-loaded`. The advertised 131,072-token maximum does not prove an actual loaded context, memory capacity, effective template, parallelism or schema support. The earlier 4,096-context baseline remains historical rather than current measurement. The dated report proof also observed parallelism 4, whereas the environment reference lists the older baseline 1; no active instance exists to resolve the present configuration. Serial trial calls remain the plan's execution requirement.

No WSL `lms` CLI or project-environment `lmstudio`, `llama_cpp`, `transformers`, `tokenizers` or `jsonschema` package is available. The system `jsonschema` is usable for artifact checks. No packages were installed and no model/server state was changed. Official [LM Studio tokenization guidance](https://lmstudio.ai/docs/python/tokenization) describes applying the loaded model's prompt template, tokenizing the formatted conversation and comparing with its loaded context. The [native REST endpoint inventory](https://lmstudio.ai/docs/developer/rest) does not list an equivalent tokenize/template endpoint. These are documented routes, not executed SDK proof.

Correction to the initial ordering assumption: provider reachability/inventory can be checked before Build; exact final request fit cannot be established before the exact renderer exists, and presently cannot be measured against an unloaded deployment. Do not invent a provisional renderer here or call a model merely to finish a checklist. Implement/freeze the normal renderer, then establish exact model/template/tokenizer/schema accounting plus the 1,536-token completion reserve before the first live semantic request. If fit cannot be established, keep live evaluation at its capacity gate; controlled-provider integration can still be verified. Schema compatibility and output truncation behavior likewise require their own later executed checks.

### Governance checker observation

`PYTHONDONTWRITEBYTECODE=1 .venv/bin/python tools/agent-governance/governance_doctor.py` — **FAIL**, sole reported error: `AGENTS.md responsibility map is missing owner marker examples/`. Neither `AGENTS.md` nor the checker differs from the starting committed tree. This is a reproduced pre-existing documentation/checker mismatch, not a new API trial failure. Its corrective owner is the root responsibility map/checker governance responsibility; correction is outside this readiness pass. It does not supply evidence against interpreter semantics or controlled-provider test readiness. The overall governance check is not claimed green.

## Decision handoff

As of this session's handoff, the engineering baseline and frozen preparation support opening a bounded experiment-local interpreter Build cycle. There is no observed acquisition/test/package-consistency blocker for that proposed work. Formal entry still requires Ali's joint selection; the previous whole-design understanding debt remains deferred and must inform the later cycle's minimum-complete A2.

Recommended next responsibility: implement one cohesive API interpreter plus explicit opt-in ordinary PR integration and controlled-provider source-to-proposal-to-saved-recovery proof. Verify input maps, partial/ambiguous scope, shape/reference adversaries, uncertainty/identity retention, provider failures and truncation; run focused new tests then the relevant active trial regression. Keep the ordinary acquisition-only entry and product report/support-drop/action semantics intact. If a shared product provider change becomes necessary, admit and prove that change separately.

The two selection options remain: (1) implementation and controlled-provider proof, followed immediately by a separate live-model evaluation checkpoint; (2) the same engineering responsibility plus bounded live-model development evaluation in one larger cycle, with separate engineering and semantic gates. Option 1 remains recommended because failures have distinct diagnosis/proof owners. It incurs explicit unaccepted-model-quality debt, not a useful-interpreter claim; the immediate later evaluation must not disappear behind infrastructure work.

Live evaluation prerequisites: explicit operational entry with the actual maintained deployment, exact renderer/method identity and token fit, provider schema/truncation proof, equivalent frozen inputs and separately reviewed semantic/omission outcomes. No package/server/model substitution or silent input shortening is selected. A second ordinary real target-PR variation is still required before broader semantic claims; supplied urllib3 RST excerpts are calibration, not normal RST acquisition support. Target-impact composition, product adoption and independent usefulness retain the parent plan's later gates.

No formal cycle, inference, interpreter implementation, semantic acceptance or learner mastery is recorded. This active preparation record is the dated discussion anchor; `MEMORY.md` alone selects the live continuation.
