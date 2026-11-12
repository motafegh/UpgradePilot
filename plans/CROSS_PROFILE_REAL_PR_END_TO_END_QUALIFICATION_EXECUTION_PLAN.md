# Cross-profile real-PR end-to-end qualification — execution plan

**Status:** Revised after the A2 owner challenge. **Qualify a properly installed current UpgradePilot using the real public CLI first.** Reuse existing product input/provider guards; a new general HTTP-intercepting launcher is **not** a prerequisite. Required: verified installation, frozen case identity, a tested parent deadline and private outcome receipt, and explicit per-case admission. Additional observation is scoped to a concrete missing proof, especially actual model dispatch. The [earlier plan audit](../audits/2026-11-12_cross-profile-e2e-execution-plan-review.md) records the superseded stricter launcher proposal. No live qualification has been performed.

**Product owner:** [Evidence-Derived Learning and Building Plan, B2–B5](UPGRADEPILOT_90_DAY_PLAN.md#conditional-cross-profile-live-qualification-before-a-new-feature). **Live selection:** [MEMORY.md](../MEMORY.md). **Detailed source/design predecessor:** [2026-11-12 cross-profile design cycle](../working-memory/2026-11-12_cross-profile_real-pr_e2e_qualification_design-cycle.md). **Prior accepted work:** [AV-Tracer exact combined qualification](../working-memory/evidence/2026-11-12-av-tracer-native-ci/qualification.json), [OpenCV prior normal capture](../working-memory/evidence/2026-10-22-opencv-matched-report-source-capture/REVIEW.md), [Soup Sieve successful model-backed and rate-limited attempts](../working-memory/evidence/2026-10-03-report-model-recovery/README.md).

**Date written:** 2026-11-12. Freeze the *execution-time* code commit, installed command/module identity, external evidence/PR revisions, current model/server state, and network route. The plan does not impose a historical commit as a fresh-run truth.

## 1. Problem, objective, and exact claim boundary

**Problem:** Historical successful runs each covered a **different** execution profile/commit/date. HTTPX and OpenCV normal-path captures saved reports without upstream model activation; a distinct October 3 Pydantic/Soup Sieve run reached the real local model and grounded its support-drop candidate; the newer AV-Tracer combined source/selected-CI run saved JSON + a native SQLite Workspace without a model. None is a current-baseline, across-profile integration qualification. The ordinary CLI can conditionally invoke a model, but a valid report / exit 0 does not establish it was called. The existing HTTP source-capture tool explicitly refuses non-GET/model POST.

**Objective:** Install and exercise the **current distributable UpgradePilot** through its public CLI, then examine stage activation, evidence fidelity, failures, cost and saved/reopened artifacts on **two new bounded ordinary runs**. Reconcile them with the accepted AV-Tracer combined-profile reference. Any separate instrumented run is explicitly labeled and must not stand in for a public-product run. Select the next Build only from an observed decision-critical gap.

**Claim target:**
- Which supported route completed from PR input to available report/file/reopen on **this frozen baseline**?
- Which evidence families actually activated, were inapplicable/not evaluated, failed or stopped, and **why**?
- Were original facts and provenance represented faithfully and retained/inspectable to the claimed degree?
- Was the adopted LM Studio provider **actually called**, or did acquisition/source-window prerequisites prevent it?
- What wall time, API/model calls, bytes and file footprint were **actually measured**?
- Which material maintainer question remains unresolved and who owns its earliest evidence failure?

**Not a claim:** “100% of project code”, “one PR exercises all paths”, representative reliability/throughput, tested universal compatibility, independent human usefulness, model semantic accuracy generally, a causal upgrade proof, autonomous merge/fix authority, or success of every conditional stage. Report `abstain` can be correct. No target repository writes, target test execution, CI reruns, automatic reviewer experiment or new architecture feature as part of the qualification.

## 2. Intended routes, roles, inputs and non-activation

| ID | Role and public entry point | Historical anchor **only** (revalidate before B) | Expected discriminator | Durability |
| --- | --- | --- | --- | --- |
| **Q1** | Fresh *normal* `upgradepilot REPO PR --save-report PATH`; deterministic artifact/CI branch | `carla-simulator/scenario_runner#1111`; `opencv-python` `4.2.0.32→4.8.1.78`; October 22 base `7758d066080f180f8296887ed89b7c723a54706a`, head `f32ad2d23a9abee47c566dfbed2b822d953a09e2`. Prior 13 GETs / ~7.8s, no model. | Published artifacts and precise wheel tag changes, source distribution, static/CI evidence and *unproven target applicability*. Do not infer installation or runtime failure from removed tags. | Private saved JSON, source/facts viewer and report reopen. No SQLite promised by normal public route. |
| **Q2** | Fresh *normal* CLI with conditional `LocalSupportDropExtractor` and adopted LM Studio service | `pydantic/pydantic#13432`; Soup Sieve `2.6→2.8.4`; October 3 base `652a61ce4f9d7d76eaada31535807a485ece0e21`, head `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a`. Prior successful model call, plus *separate* earlier rate-limited/no-model attempt. | Source authority → bounded crossed-release window → **actual model request**, candidate → deterministic quote/line/version grounding → target Python declaration/relevance; distinguish `not_reached`, `failed`, `rejected`, `grounded`. | Private JSON and offline source viewer. No native caller-signature/CI-log evaluation in the normal route. |
| **Q3** | Previously *qualified* opt-in `caller-signature-ci` source and historical selected-job evidence | `ivaronkun-Ahey/AV-Tracer#11`; run `41416124208` attempt 1 / backend job `125180284415`, frozen base/head and [receipt](../working-memory/evidence/2026-11-12-av-tracer-native-ci/qualification.json) | Independent check of six conditional source witnesses, historical HTTPX `app=` error, exact job/source IDs, status limits, private report/Workspace recovery; no model branch. | Reuse reviewed [published ZIP](../examples/av-tracer/README.md) and receipts; no fresh run unless a specific new proof requires it. |
| **Q4, conditional only** | At most one additional supported contrasting normal PR | No case preselected; screen **up to three** leads with explicit criteria and retain all screens | Only if Q1/Q2 leave a **specific decision-critical CI/runtime ambiguity** whose behavior cannot be assessed from existing cases; prefer genuinely different mechanism/CI state over second Starlette-to-HTTPX copy | Same as chosen public route. Separate written approval for a live Q4 attempt. |

**Source-revision rule.** Revalidate historical SHA anchors through a separate read-only PR preflight; freeze the actual repository/PR/base/head and dependency transition. Existing normal product code checks coherence around changed-file acquisition; the internal `acquire_dependency_inputs(... expected_base, expected_head)` admits frozen SHAs, but the normal **public CLI does not expose those parameters**. Preflight plus after-save report identity comparison verifies **whether the delivered result is the selected case**; it does not prove the CLI refused an externally mismatching first PR observation *before* changed-file acquisition. If strict pre-acquisition external SHA admission is necessary for a particular claim, scope a **small explicitly tested CLI/input-owner integration** rather than an invisible test-only hook. Any mismatch invalidates that selected-case acceptance, even if the product's internal snapshot remained coherent. The combined source/CI profile has its own explicit expected-SHA interface.

## 3. Governance and prerequisites — A0/A1/A2 before live work

**A0 — baseline reconciliation.** Confirm live `MEMORY.md`, this plan, roadmap, governance `AGENTS.md`/Security/Environment, last AV-Tracer D/E, clean local versus remote `main`, active parallel work, installed Python and UpgradePilot provenance. Preserve unrelated untracked files and parallel changes. Create or continue the **single execution-cycle working-memory record in A0**, seed its orientation map, and maintain C through preflight, verification, learning and closure.

**A1 — continuity.** Explain the relevant differences between the ordinary and opt-in profiles, CLI success and branch coverage, published wheels and target suitability, JSON and Workspace retention, and installed package and loaded code. Stop for Ali to question or challenge the current-state model before A2.

**A2 — bounded execution readiness:** confirm why Q1/Q2/Q3 together are a route matrix, not a single all-features run; describe budgets, actual failure states, exact source proof, privacy/credentials, expected outputs, conditional Q4 and stop rules. Explicit owner go-ahead before network/model execution, with previous material D/E cycles closed or recorded as separate pending learning obligations.

### Installation baseline and private case freeze

**Primary execution route: install UpgradePilot correctly.** Prefer a dedicated qualification Python virtual environment, isolated from the existing WSL `.venv` and other parallel work. Build/install the project using its declared Python packaging and dependency metadata; record dependency resolution, installation and exact distribution metadata. Do not reinstall unrelated dependencies blindly. Existing `.venv` replacement is a separately reviewed fallback. `PYTHONPATH=src` is a **secondary source-code diagnostic**, not a substitute for an installed-application qualification.

**Before any live PR:** verify Git commit and unchanged checkout, build artifact and installed distribution provenance, actual `upgradepilot` executable, Python interpreter and resolved imported modules for CLI, investigation, report, GitHub/PyPI acquisition and semantic extractor. Confirm the selected installation is consistent with the frozen source commit rather than trusting only the package version `0.0.0` or a one-module hash. Run an offline CLI help/smoke check and existing controlled regression tests; installation or import failure is a **packaging/environment outcome**, not a target PR failure.

Freeze one shared installed-code/environment baseline and one separate private case card per new live run. Record UTC time, full Git SHA, build/install/entry-point provenance, Python/dependency versions, approved process-local networking/auth, public PR metadata and changed-file scope, exact command, deadline and output path. Recheck mutable source/model readiness before Q2 — Pydantic/Soup Sieve: conditional local-model investigation. Record the identity/control limitations of the normal CLI rather than claiming an unimplemented freeze gate.

For Q2 — Pydantic/Soup Sieve: conditional local-model investigation additionally record LM Studio endpoint, requested model key, observable loaded-model/configuration state, and an approved way to attribute a model POST to **this** product invocation. For Q1 — CARLA/OpenCV: normal artifact investigation record one primary artifact fact and one uncertainty to inspect. Use owner-private output directories (0700/0600), distinct receipts for preflight and product execution, and never copy token or raw prompt values to public records.

**Preflight stops:** mismatching/unsupported PR, packaging parity failure, unavailable safe network route or quota, private-output failure, or unavailable model needed to claim Q2 model integration. A missing **optional** metrics source narrows the measurement claim; a missing **essential safety control** stops execution. Preserve exact refusal rather than substituting another case.
 
## 4. Product-first operational boundaries and proportional observability

**Existing product guards — reuse, don't duplicate.** The installed version must be checked for repository/PR argument validation, exact-head changed-file and post-acquisition identity consistency, bounded GitHub and PyPI provider operations and error classification, Python Package Index streamed JSON response limit (currently 1,000,000 bytes by default), and the local semantic model's source-window/timeout/completion bounds. These are valuable correctness safeguards, **not** a shared whole-process physical-request/byte budget. The ordinary CLI does not currently expose the internal expected-base/head parameters.

**Minimal external run protection — required.** Launch the **real installed** `upgradepilot` public CLI in a fresh process. Use a tested subprocess/shell supervisor solely for a wall-clock deadline, exit/signal handling and safe private stdout/stderr/time receipt; no replacement producer, model stub or monkeypatched request behavior. The existing application makes actual GitHub/PyPI/conditional model calls; do not prevent a naturally eligible LLM branch merely because a historical Q1 run didn't invoke it. No target-repository code execution, GitHub writes, automatic retries or model substitutions. Use anonymous GitHub auth by default; explicit `--github-auth token-env` only if approved and process-scoped with verified owner-only token. Preserve known qualified GitHub/PyPI proxy split without changing global machine settings.

**Optional exact request/byte telemetry.** If needed, reuse existing provider measurements or a narrowly justified, independently tested observation seam. `tools/capture_report_sources.py` is **a separate internal-code diagnostic**, not the public CLI; its GET-only refusal means it cannot be used unchanged for the model-enabled case and it cannot be presented as same-invocation evidence for a different CLI run. Without a valid observer, physical GET counts, aggregate decoded bytes and precise transfer cost are `not_measured`, **not zero and not proven bounded**. Do not build a general intercepting launcher merely to fill blank spreadsheet cells.

**Actual local model dispatch is a special proof obligation for Q2 — Pydantic/Soup Sieve: conditional local-model investigation.** A trusted, uniquely attributed LM Studio server event from the same product process or a minimal metadata-only adapter observer can prove dispatch. Rehearse any observer with controlled inputs and show it doesn't alter prompt, source gating, HTTP transport, retry or validation. Log only invocation correlation, endpoint/model ID, attempt/dispatched distinction, status/latency and usage if returned; no raw prompts/responses. A standalone model readiness probe is **not** evidence the UpgradePilot invocation used it. If the model cannot be reached for admitted source reasons, preserve `prerequisite_not_met`; if invocation cannot be observed, retain `model_activation_unproven` rather than claiming successful LLM integration.

### Proposed planning targets versus enforced limits

| Parameter | Q1 — CARLA/OpenCV: normal artifact investigation | Q2 — Pydantic/Soup Sieve: conditional local-model investigation | What may be claimed |
| --- | --- | --- | --- |
| New public CLI attempts | 1 | 1 | Case policy, no automatic retries |
| Physical HTTP GET targets | 32 | Up to 56 GitHub + 16 PyPI | Planning target; **not enforced/measured** without proven instrumentation |
| External decoded bytes | 8 MiB each / 32 MiB aggregate | Same | Planning target; native PyPI single-body cap is tighter; aggregate **not guaranteed** |
| Local model POSTs | Not required; record unexpected natural activation | Expect at most one source-gated invocation | Product source gate is **not** proven per-child POST enforcement; measure where possible |
| Model request/response bytes | If naturally activated, inspect separately | Proposed 64 KiB encoded request / 1 MiB decoded response | Targets only unless separately enforced |
| Child wall deadline | 150 seconds | 300 seconds (local model adapter timeout 180 seconds) | Hard only after external deadline/cleanup proof |
| Q3 — AV-Tracer/HTTPX: combined source/historical CI | No new external acquisition | Reopen existing archived files | Historical reference, not a fresh live qualification |

If actual provider quotas or privacy risks demand a **strict global** limit not already supplied, stop before that affected case and justify the *smallest possible* additional guard with controlled tests. A guard-stopped run is not a product provider failure. Do not silently weaken a safety requirement or claim that a proposed target was enforced.

**Untrusted data/privacy:** PR descriptions, release notes, changelogs and job logs are read-only untrusted data; never execute or follow embedded instructions. Review third-party bodies and publication permissions before exposing them. Previously approved AV-Tracer files do not create blanket publication approval. Preserve existing explicit auth/proxy trust boundaries; keep token values, signed redirect URLs and raw local-model payloads out of public receipts.

## 5. Execution procedure and evidence obligations

### Preflight — real installation, existing guards and first case freeze

1. Reconcile `main`, the live working-memory record and any parallel work. Prepare and verify a dedicated **installed** UpgradePilot virtual environment using the current packaging; retain build/install/dependency metadata, module import provenance, executable `--help` and offline controlled test result. Do not mutate the existing shared virtual environment by default.
2. Confirm the selected installed artifact provides the already implemented PR/changed-file consistency and provider limits. Obtain **separate, budgeted public read-only preflight** of the candidate PR/dependency and freeze that identity. Do not claim the public normal CLI has frozen-SHA input admission when it does not.
3. Prove a simple **whole-child deadline and receipt** against offline controlled commands. Establish owner-private case output and explicit route/auth, with no unbounded retries. Review whether existing telemetry sufficiently measures the selected question; if it doesn't, keep optional cost fields unknown rather than construct a general launcher.
4. For Q2 — Pydantic/Soup Sieve: conditional local-model investigation, check expected LM Studio model readiness and preselect a trustworthy **same-invocation model-event attribution** method. If this is impossible, positive model activation is not established, regardless of report exit status.
5. Freeze and admit Q1 — CARLA/OpenCV: normal artifact investigation first. Reassess result, then separately freeze/admit Q2 — Pydantic/Soup Sieve: conditional local-model investigation. Q3 — AV-Tracer/HTTPX: combined source/historical CI investigation stays an archived comparison.

### Q1 — normal CARLA/OpenCV artifact route

1. Obtain independent public PR preflight and freeze exact identity; distinguish preflight GETs from normal application GETs. Confirm supported changed-file/dependency representation; if unsupported, retain that result and stop the case.
2. Execute the **actual installed ordinary CLI** with arguments `carla-simulator/scenario_runner 1111 --save-report /private/unique/report.json` under the tested parent deadline/receipt, with approved auth. Do **not** artificially disable naturally eligible product capabilities. One admitted attempt; if the report identity differs from the separately frozen PR, record an input mismatch rather than a qualifying result.
3. Retain stdout/stderr, exit and timing; include a same-invocation request ledger or raw PyPI bodies **only if truly observed and retained**. Otherwise label those metrics `not_measured` and use separately timestamped primary-source corroboration. Verify report base/head and dependency transition against preflight. Keep October evidence attributed to its historical horizon.
4. Strictly decode saved JSON, recompute SHA-256/size, reopen with `--open-report` without credentials/network, inspect one actual `--show-facts SOURCE_ID` for artifact tags/distributions and one actual `--show-source SOURCE_ID` where original text is retained. **Reference-only** sources should explicitly refuse original-text viewing without downloading it. Record renderer/report consistency.
5. Independently derive the old/proposed wheel-tag sets and source-distribution presence from the exact release inventories. Compare with the rendered facts and check one material CI/runtime/environment unknown against its evidence. Prefer the same-invocation bodies. A separate later release lookup can corroborate the result when identities and scope match, with its own timestamp and receipt. Classify any material unverified claim as open. Wheel-tag changes describe published artifacts. Target installation and applicability require their own evidence.

**Q1 pass for route fidelity:** a supported exact-input report is delivered, its artifact facts correspond to original evidence, saved JSON reopens, source views respect retention, and any unknowns are appropriately classified. If an earlier stage fails, score **partial/blocked with owner** rather than awarding a route pass for printing a report.

### Q2 — normal Pydantic/Soup Sieve conditional model route

1. Freeze PR head/base, dependency, source-path eligibility, rate-limit and **actual current model readiness**. Prior October result is only a comparison, not a requirement that today's source window or model behavior be identical.
2. Execute the **actual installed ordinary CLI** with arguments `pydantic/pydantic 13432 --save-report /private/unique/report.json` under the tested parent deadline/receipt. The model can activate only through the product's normal source prerequisites. Attribute positive model dispatch to the same product run using the preselected trusted event/metadata-only observer; if evidence is missing, call it `unproven`, not successfully exercised.
3. Record each model-related stage in the coverage matrix and name the first stop. Use actual product outcomes and supporting evidence:

   | Stage | Evidence and interpretation |
   | --- | --- |
   | Upstream eligibility | Exact repository, release interval, tag/changelog and bounded source window, or the prerequisite that stopped the route. |
   | Actual model dispatch | A request tied to the admitted source and this invocation. Distinguish not reached, refused before transport, and dispatched. |
   | Provider response | Distinguish transport/status failure, unusable JSON/schema and usable response. Record returned model ID and usage only if available. |
   | Deterministic grounding | Distinguish no candidate, unresolved selection, a rejected proposal and a grounded result. Check any grounded quote/line and version against the tagged changelog. |
   | Target evaluation | Record whether target evaluation was reached, the target declaration and the supported relevance/impact outcome. Distinguish a missing declaration from a supported applicability conclusion. |

4. Reopen the private JSON offline. Open the tagged changelog and grounded quote by saved source ID if retained. Inspect the saved target Python fact and its exact-head locator. The ordinary report's target-declaration source is reference-only, so verify the actual `requires-python` text against the exact-head file retained during the run or a separately attributed exact-head read. Expect original-text refusal for reference-only entries. Compare the declared range with the grounded claim and keep the conclusion at the scope of that support drop.
5. Preserve the first stop if the upstream prerequisites fail or the invocation is refused. Model activation remains open when the POST never dispatched. A dispatched request can qualify invocation and failure handling even if the provider response fails or the candidate is rejected. A different PR requires its own approved freeze and rationale.

**Q2 positive grounded-route proof** requires observed dispatch to the adopted provider, a usable response, a source-verified grounded claim, completed downstream target evaluation with its primary evidence checked, and faithful saved/offline delivery. Record invocation, response and rejection coverage separately when this stronger result is absent. A correct unresolved outcome can qualify the handling of that state.

### Q3 — AV-Tracer retained reference and offline recovery

1. Verify SHA-256 and documented file list of the existing [public example archive](../examples/av-tracer/README.md). Extract to an owner-private temporary directory with `0700` directories/`0600` files; the Workspace refuses overly permissive extraction.
2. Open source-only and combined saved JSON and exact SQLite revisions **offline**. Show the actual combined selected error `source-48` / saved excerpt where present; verify PR/run/attempt/job/source/digest from the [qualification receipt](../working-memory/evidence/2026-11-12-av-tracer-native-ci/qualification.json).
3. Assert old source-only report remains byte-identical and lacks the CI-log assessment. Verify the combined report contains a selected `ci-job-log` observation but full normal CI coverage and runtime state stay `not_evaluated` and action `abstain`.
4. Separate the observed `app=` traceback and same-job `httpx-0.28.1` install token from unproven same-process import identity and counterfactual causality. Do not claim ordinary upstream model behavior was exercised by this profile.
5. Record historical live proof at its original commit and current offline compatibility at the frozen reader baseline. Reuse an earlier offline check only if it covers the same archive and reader baseline.

### Cross-case verification and evidence review

- Construct an **actual-activation matrix** for PR identity, CI workflow/YAML, runtime command-completion state, PyPI releases/artifacts, the five separate Q2 stages, source/signature, selected exact CI log, JSON save, native SQLite Workspace, offline source/facts inspection and action synthesis. Fill each cell with its actual state, reason and evidence. Distinguish completed, unresolved, outside the profile, prerequisite missing, refused before dispatch, unavailable, unsupported, failed and not measured. Keep Q3 historical live and current reader proof distinct.
- Read the saved report and corresponding primary evidence for at least **one material finding and one material unknown per fresh case where available**, and the known historical CI excerpt in Q3. Verify source identity, time/version roles, retention, applicability and quote equality. For a stopped case, verify the actual stop against the receipt and retain the missing proof explicitly.
- Exercise offline open in a fresh process with network/credentials/model calls disabled or guarded; record exact rejection/error when referenced source text was not retained. A JSON integrity digest establishes bytes, not factual truth.
- Record exit code, activation/status, API GET/redirect/body costs when observed, model POST/latency/usage when observed, wall time, saved report/excerpt counts, bytes/hashes, private file paths **only in private receipts**, and independent evidence review result. Separate startup/preflight/proxy/model-load and product runtime. Treat **unobserved** as unknown, not zero.
- Compare with October historical reports and November AV-Tracer only **by scope/horizon**. A fresh contradiction may indicate changed upstream availability or model/runtime, not necessarily product regression.
- A read-only independent second-pass review by the assistant may identify mistakes but does **not** count as blinded independent-human utility. Record conflicts and repair owner.

## 6. Failure taxonomy, stop lines, and minimal repair policy

| Observed situation | Required label and response | No unsupported substitution |
| --- | --- | --- |
| PR head/base drift, unexpected transition, unsupported dependency or missing input | `input_identity_drift` / `unsupported`; preserve expected and observed identity and stop before downstream work | Do not rebrand a different revision as the same case |
| GitHub 403/429, stale token, proxy/TLS, PyPI failure | `source_unavailable` / `auth` / `transport`; preserve partial results and exact retry/credential policy | No silent token fallback, unlimited retry, or fabricated zero evidence |
| Upstream tag/source-window missing | `prerequisite_not_met`; no model call expected | Do not call model directly and count it as normal product |
| Model dispatch denied by the launcher | `refused_before_dispatch`; preserve the denied attempt and actual count of admitted POSTs separately | Do not classify the denied request as a provider failure or model coverage |
| Local model unavailable, dispatched POST unsuccessful, schema invalid or unsupported model | Record `model_provider_problem` / `model_output_unresolved` with the dispatch and response states | Do not substitute stronger model, change prompt/validator or fake candidate |
| Multiple/contradictory sources or ungrounded semantic candidate | `unresolved`/rejected with source-specific reason | No semantic promotion from model confidence or repeated text |
| Report opens but cited original source is not retained | `reference_only` / `retention_gap` with exact source and consumer need | Do not claim full offline source preservation |
| Exit 0 but required stage never activated | `delivered_partial`; report valid, **coverage open** | Do not count route/LLM activation as passed |
| Unexpected exception, corrupt report, false fact or broken recovery | `implementation_failure`; preserve safe trace, stop downstream inference | Do not hide it behind `abstain` or rerun until green |
| Claims about target installation/runtime, CI job correlation, or source applicability missing proof | `not_established` / `not_evaluated` | Do not infer from wheel listing/green CI/installed-package summary |
| Request, byte or elapsed-time ceiling reached | `budget_exceeded`; preserve the refused operation, partial evidence and any independently verified cleanup | No further automatic acquisition |

**Repair rule:** within this qualification B-stage, fix only a blocker necessary for a faithful selected route if independently diagnosed and authorized; record both original failure and subsequent new attempt separately, rerun relevant regressions, refreeze code/inputs. Defer broader capabilities (job discovery, full native normal persistence, generalized source parsing, AI agents, new targeted-check permission) to a separate decision after the review. No “repair” solely to make a planned case appear green.

## 7. Deliverables, acceptance, and final decision

**Private evidence root** outside Git: `~/.local/share/upgradepilot/<unique-cross-profile-qualification-run>/` with an owner-only manifest and `Q1/`, `Q2/` directories, each containing actual invocation/exit/UTC time, report JSON when produced, stdout/stderr sanitized as needed, observed request/model ledger and external response observations, hashes, reopened view proof and brief reviewed claims. Reused Q3 may link to the existing reviewed example archive rather than duplicate its bytes.

**Reviewed public artifacts.** Preserve the exact originals locally. Publish a results summary, coverage matrix, compact receipt, and a source-verified claim/unknown review or exact stop for each fresh case. Record evidence IDs and hashes without home paths or credentials. Apply the [artifact publication rule](../docs/README.md#publishing-project-artifacts) to share a reviewed exact report or other files needed for offline reproduction, or a reviewed counterpart with its limits when originals cannot be shared. Preserve every attempt, including failed preflight and model non-activation.

**Route acceptance.** Q1 passes its artifact claim only with exact-input fidelity, zero model dispatches, verified release facts and successful offline delivery. Q2 reports invocation coverage, provider/validation behavior and the positive grounded route separately using the five stages above. Q3 reports historical live qualification and compatibility with the frozen offline reader. Keep partial, refused and failed cases in the results with their own disposition.

**Batch completion.** Every attempted case has its admitted identity and method or exact preflight stop, actual stage coverage, measured resource use and explicit unknowns, saved artifacts or failure evidence, and the earliest owner of any material gap. Review a primary-source claim and unknown where the route produced them. Decide **`no_build`**, **`bounded_build:<owner/problem>`**, or **`more_evidence:<exact_missing_condition>`** from the recorded outcomes. Batch completion includes honest partial results. Route passes are scored individually.

**Decision priorities.** Trace a model non-activation to its first missing input or source gate. If a proposal is ungrounded, determine whether source selection, model interpretation or validation explains the outcome. A correct rejection may require no repair. If correct evidence is hidden, examine the report consumer. If exact CI job selection is the demonstrated burden, examine that owner. Consider positive action admission only when the evidence earns it. The **decision-focused contrasting maintainer task review follows this qualification** and uses the actual case evidence to choose the next product question.

**Deferred randomized cohort:** only after the deterministic batch and a meaningful unanswered prevalence/robustness question. Define the eligible PR sampling frame, exclusions, frozen list/seed, time horizon, attempts/denominator and interpretation limits before any seeded selection. Do not start broad random testing, independent reviewer comparison or model-evaluation benchmark by default.

## 8. Launch handoff and learning ownership

After A0 and A1, use A2 to agree the scope, control proof and proof limits. Seal the private Q1 run card before Ali admits that invocation. Review Q1's actual outcome before sealing and admitting Q2, with its separate model and credential scope. A failure in a shared launcher control blocks reuse until that control is verified. A case-specific source stop remains an outcome of that case. Q3 uses the verified archive and current-reader check. Keep the single cycle record current across both cases, then use D and E for evidence-backed ownership and closure.

**Learning checks:** (i) How can CLI exit 0 while the model never ran? (ii) Why does `Successfully installed X` differ from actually imported module identity? (iii) What source inspection can distinguish wheel inventory from target viability? (iv) What is lost if only a report JSON survives, versus native Workspace plus retained original excerpt? (v) How do different model/PR/code horizons affect meaningful latency and correctness comparisons? Record owner understanding, not assumed mastery.

**End condition:** Complete and review the matrix and resource/claim checks; close the qualification cycle with honest partials and a specific next product responsibility or no-Build disposition. Update `MEMORY.md` and accepted owners to reflect the *actual* results. This plan makes no claim that the live cases have already been run.
