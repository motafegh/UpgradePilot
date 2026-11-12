# Cross-profile real-PR end-to-end qualification — execution plan

**Status:** Execution-ready *plan*, not executed. A0 design/current-state alignment done; execution begins only after A1/A2 owner onboarding, preflight/freeze, and explicit admission of the individual live cases. **Do not infer pass from this document.**

**Product owner:** [Evidence-Derived Learning and Building Plan, B2–B5](UPGRADEPILOT_90_DAY_PLAN.md#conditional-cross-profile-live-qualification-before-a-new-feature). **Live selection:** [MEMORY.md](../MEMORY.md). **Detailed source/design predecessor:** [2026-11-12 cross-profile design cycle](../working-memory/2026-11-12_cross-profile_real-pr_e2e_qualification_design-cycle.md). **Prior accepted work:** [AV-Tracer exact combined qualification](../working-memory/evidence/2026-11-12-av-tracer-native-ci/qualification.json), [OpenCV prior normal capture](../working-memory/evidence/2026-10-22-opencv-matched-report-source-capture/REVIEW.md), [Soup Sieve successful model-backed and rate-limited attempts](../working-memory/evidence/2026-10-03-report-model-recovery/README.md).

**Date written:** 2026-11-12. Freeze the *execution-time* code commit, installed command/module identity, external evidence/PR revisions, current model/server state, and network route. The plan does not impose a historical commit as a fresh-run truth.

## 1. Problem, objective, and exact claim boundary

**Problem:** Historical successful runs each covered a **different** execution profile/commit/date. HTTPX and OpenCV normal-path captures saved reports without upstream model activation; a distinct October 3 Pydantic/Soup Sieve run reached the real local model and grounded its support-drop candidate; the newer AV-Tracer combined source/selected-CI run saved JSON + a native SQLite Workspace without a model. None is a current-baseline, across-profile integration qualification. The ordinary CLI can conditionally invoke a model, but a valid report / exit 0 does not establish it was called. The existing HTTP source-capture tool explicitly refuses non-GET/model POST.

**Objective:** Examine current actual public product entry points, stage activation, evidence fidelity, failure semantics, cost and saved/reopened artifacts on **two new, bounded normal-path runs**, and reconcile them with the **already accepted** AV-Tracer combined-path reference. Determine the earliest material product gap that prevents a maintainer from answering a concrete dependency-upgrade question, or record that no new Build is justified.

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

**Source-revision rule:** Existing base/head SHAs are *historical comparison anchors*, not claims about current GitHub PR heads. The **normal** public CLI has no `--expected-base/--expected-head` flags: freeze via separate read-only preflight and **verify the saved report's exact identity after the run**; recheck if drift is plausible. If actual revision differs, preserve the observed result and decide whether to stop/reselect. Never edit a prior report or silently label a new head as the October sample. The combined caller-signature route has its own explicit expected SHA validation.

## 3. Governance and prerequisites — A0/A1/A2 before live work

**A0 — baseline reconciliation:** confirm live `MEMORY.md`, this plan, roadmap, governance `AGENTS.md`/Security/Environment, last AV-Tracer D/E, clean local versus remote `main`, active parallel work, installed Python and UpgradePilot provenance. Preserve unrelated untracked files; do not silently merge/overwrite parallel changes. Create/continue the **single execution cycle working-memory record** when activating B, linking these frozen plans; do not create per-command planning ceremonies.

**A1 — continuity:** explain to Ali the critical distinctions: public normal vs opt-in profile; `exit 0` vs complete observation; model activation vs not reached; PyPI wheel availability vs target suitability; saved JSON vs native SQLite and source retention; CI green vs proposed-version execution; installed package vs loaded code. Stop at A1 if these remain material misunderstandings; not a requirement to memorize every file.

**A2 — bounded execution readiness:** confirm why Q1/Q2/Q3 together are a route matrix, not a single all-features run; describe budgets, actual failure states, exact source proof, privacy/credentials, expected outputs, conditional Q4 and stop rules. Explicit owner go-ahead before network/model execution, with previous material D/E cycles closed or recorded as separate pending learning obligations.

### Immutable run freeze — one private manifest before the first normal CLI invocation

For each fresh Q1/Q2 case record:
- UTC time, UpgradePilot Git commit (full SHA), branch, checkout changes, invoked entry point, version and resolved installed `upgradepilot` module location; if using a **non-editable installed CLI**, verify its code matches that commit or reinstall it **before freezing**, then record the installation step separately. No dynamic source selection after results.
- Python/venv version, OS/WSL boundary, enabled package dependencies, relevant proxy routing **names only** (never secrets).
- Exact PR `repo/number`, declared dependency package/old/proposed versions, base/head, changed-file path/scope, open/merged state and API observed timestamp. Source-based expectation is a hypothesis, not the oracle.
- Planned auth (`anonymous` or explicit `token-env`), current GitHub rate-limit status without leaking token, PyPI route availability, per-case request/byte/time limits, single-attempt count.
- For Q2, LM Studio localhost endpoint, model key/version/quantization/context/parallelism when observable, service readiness and hardware/loaded-model state **without substituting models or weakening trust boundaries**.
- Explicit file output directory name/permissions, report destination, source viewer command and desired per-case claim to check. All new filenames must be unique.

**Stop/preflight refusal:** unsupported PR structure, changed identity, missing installed-source parity, inaccessible required network, missing expected model key when Q2 is selected, unreasonable quotas, unsafe/unreviewed capture method, or lack of writable owner-private output should produce a **preflight problem receipt**, not an improvised case substitution or a false product failure.

## 4. Budget, routing, observability and safety controls

**Suggested ceilings to approve in A2 (hard enforcement must be demonstrated before calling a limit enforced):**

| Variable | Q1 OpenCV | Q2 Soup Sieve | Q3 existing reference |
| --- | --- | --- | --- |
| Live application invocations | 1 | 1 | 0 new |
| External HTTP GET budget | 32 total (prior bounded contract) | Proposal: up to 56 GitHub GETs + 16 PyPI GETs, and **only** eligible known hosts; tune downward using actual preflight/quota | 0 new |
| Local-model POST budget | 0 expected; unexpected attempt is an **activation finding**, not silent success | 1 source-gated product request; provider timeout 180 seconds; at most 1,024 configured completion tokens | 0 |
| Per decoded HTTP body / total | Proposed 8 MiB / 32 MiB | Proposed 8 MiB / 32 MiB excluding separately bounded inference payload; record actual request/response sizes when observable | Already recorded |
| Startup-inclusive external deadline | 150 seconds (120s prior capture action budget + overhead) | 300 seconds including model 180s timeout; stop on real deadline, not arbitrarily after expected output | Private/offline reopen only |
| Retries/alternate credentials/model substitutions | None automatically; explicitly record permission and a new attempt horizon if necessary | Same; no forced direct semantic call to fill coverage | N/A |

These are **proposed experiment controls**, not claims that the current normal CLI enforces request or body budgets. The historical `tools/capture_report_sources.py` supports bounded *anonymous GET* capture but **rejects model POST**. It can be used with Q1 after checking actual route/eligibility, but **must not** be used unchanged for Q2. For Q2 select the smallest auditable observation method **before** the run (trusted LM Studio request/event receipt, or one reviewed test-only/scope-only wrapper that invokes the actual public CLI/adapter and records metadata only). Do not add a general intercepting proxy, silently mock model output or transform the product into a different code path for convenience. If trustworthy model-call telemetry and enforceable budgets are not possible, record the *unmeasured* fields as unknown, narrow the claim, or stop; never print guessed call counts or silently allow unlimited activity.

**Observe separately:** GitHub/PyPI physical HTTP GETs including redirects and refusals; response status and decoded consumed bytes vs complete bytes; actual model `/v1/chat/completions` POST attempt/status/elapsed/model ID and response usage if supplied; acquisition/preflight time vs CLI wall time vs offline read time. Distinguish zero measured, not observed, missing, blocked, and non-activation. A report's field existence is **not proof of model execution**. Guard against a model response arriving after external timeout; retain no false complete report.

**Credentials/proxies:** product defaults to anonymous even with ambient token. Use `--github-auth token-env` only when **explicitly** selected and the existing owner-only token file has been verified; scope it to the child process, never command arguments/reports. GitHub direct routing and PyPI through the previously qualified split proxy are **separate** policies; do not disable/change machine VPN/proxy globally. LM Studio traffic stays on loopback `127.0.0.1:18080` with ambient proxies ignored by its own session. No `0.0.0.0`, remote model API, replacement model or hidden fallback. Provider errors may remain unresolved legitimately. Avoid raw prompt/response publication or signed-URL retention.

**Safety of source content:** retrieved PR/release/changelog/job text is untrusted, may contain instructions, personal data or copyrighted third-party content. Never execute it, obey embedded instructions, expose private tokens or commit raw external bodies without an explicit retention/legal/sensitivity review. Public summaries and receipts use bounded excerpts and attributed links; Ali's approval of the existing reviewed AV-Tracer archive is not blanket approval for all new raw captures.

## 5. Execution procedure and evidence obligations

### P0 — reconcile and freeze (no product invocation)

1. Check `git status`, local/remote `main`, preexisting test suite status, executable/package origin and PR metadata. Verify the exact selected dependency/version pair.
2. For Q2 inspect `src/upgradepilot/upstream/support_drop_extractor.py` and `ENVIRONMENT.md`: current endpoint `http://127.0.0.1:18080`, key `gemma-4-e4b-it-ud`, timeout 180s, max source window 4096 characters. README port already corrected. Confirm the model exists and loopback route works; a standalone service probe is **not product model-call coverage**. Historical observed parallelism 4 differed from adopted 1; record actual running configuration, do not silently change it.
3. Freeze invocation, budgets, observer, auth and output paths in a new private case manifest. Run no live analysis before freeze. An optional focused regression/smoke test of current product does not substitute for a real case.

### P1 — Q1: normal CARLA/OpenCV artifact route

1. Obtain independent public PR preflight and freeze exact identity; distinguish preflight GETs from normal application GETs. Confirm supported changed-file/dependency representation; if unsupported, retain that result and stop the case.
2. Execute the **actual normal public CLI** (`upgradepilot carla-simulator/scenario_runner 1111 --save-report /private/unique/report.json` or equivalently `python -m upgradepilot` after code parity check). Use a newly frozen invocation, auth and monitored limits; one admitted attempt.
3. Retain stdout/stderr/exit/timing and source capture where available. Check the report's exact PR base/head and package transition against preflight; a mismatched current revision is not comparable to the October output.
4. Strictly decode saved JSON, recompute SHA-256/size, reopen with `--open-report` without credentials/network, inspect one actual `--show-facts SOURCE_ID` for artifact tags/distributions and one actual `--show-source SOURCE_ID` where original text is retained. **Reference-only** sources should explicitly refuse original-text viewing without downloading it. Record renderer/report consistency.
5. Independently check the consequential artifact claim against original PyPI distribution filenames/tags and source distribution, and check one CI/runtime/environment absence or unresolved claim. Wheel-tag disappearance is not a proven failing target environment or a universal incompatibility. Record `abstain` and source strength honestly.

**Q1 pass for route fidelity:** a supported exact-input report is delivered, its artifact facts correspond to original evidence, saved JSON reopens, source views respect retention, and any unknowns are appropriately classified. If an earlier stage fails, score **partial/blocked with owner** rather than awarding a route pass for printing a report.

### P2 — Q2: normal Pydantic/Soup Sieve *conditional* LLM route

1. Freeze PR head/base, dependency, source-path eligibility, rate-limit and **actual current model readiness**. Prior October result is only a comparison, not a requirement that today's source window or model behavior be identical.
2. Execute the *unchanged public normal CLI* (`upgradepilot pydantic/pydantic 13432 --save-report /private/unique/report.json`) with process-scoped routing and reviewed observer. **Do not** call the extractor directly or inject a candidate just to make the LLM branch run.
3. Trace the activation chain in order: exact upstream repository and proposed release index → crossed-release and tag/changelog authority → bounded `CrossedReleaseSourceWindow` → actual `LocalSupportDropExtractor` request → response/proposed candidate → deterministic citation/line/version grounding or rejection → target Python declaration and impact/relevance. Mark the *first stop/limitation*. If the model is not reached, preserve `not_reached` and the earlier reason, not `model failed`. If called, distinguish request transport/status failure, invalid JSON/schema, candidate `unresolved`, rejected proposal, grounded result, and target applicability.
4. Record the actual LM Studio POST **metadata-only**, source-window/source ID linkage, model ID and observed settings, HTTP status, latency and token usage *only if returned*; no raw prompts or hallucinated cost figures. A 200 response is not automatic semantic correctness.
5. Reopen the private JSON offline with current CLI and inspect the admitted upstream quote and target Python declaration using real source IDs. Independently compare exact tagged upstream text against the grounded interpretation and the target's declared `requires-python` range, distinguishing a candidate support drop from target applicability and overall upgrade safety.
6. If upstream acquisition or source eligibility fails before model activation, mark the route **partial** and the **current model activation qualification open**. Do not secretly retry or substitute a different PR/model. A separately approved single alternative source-eligible PR could later be considered; it needs its own freeze and explicit rationale.

**Q2 conditional positive proof:** only if the real product actually invoked the adopted model under an admitted source window and the resulting grounded/unresolved/rejected state is faithfully and durably represented. Grounding itself must be assessed from the original tagged source, not from the model's self-report. A legitimate non-activation is a valid product outcome but does not meet model-*activation* coverage.

### P3 — Q3: AV-Tracer retained reference, no fresh external acquisition

1. Verify SHA-256 and documented file list of the existing [public example archive](../examples/av-tracer/README.md). Extract to an owner-private temporary directory with `0700` directories/`0600` files; the Workspace refuses overly permissive extraction.
2. Open source-only and combined saved JSON and exact SQLite revisions **offline**. Show the actual combined selected error `source-48` / saved excerpt where present; verify PR/run/attempt/job/source/digest from the [qualification receipt](../working-memory/evidence/2026-11-12-av-tracer-native-ci/qualification.json).
3. Assert old source-only report remains byte-identical and lacks the CI-log assessment. Verify the combined report contains a selected `ci-job-log` observation but full normal CI coverage and runtime state stay `not_evaluated` and action `abstain`.
4. Separate the observed `app=` traceback and same-job `httpx-0.28.1` install token from unproven same-process import identity and counterfactual causality. Do not claim ordinary upstream model behavior was exercised by this profile.
5. Record this as **reused November 12 reference proof at an earlier code commit**, not a fresh run under the current baseline. If product code changed meaningfully, qualify its continued offline compatibility separately before claiming current parity.

### P4 — cross-case verification and independent evidence review

- Construct an **actual-activation matrix** for PR identity; CI workflow/YAML, runtime command-completion state, PyPI releases/artifacts, upstream publisher authority, semantic model attempt/grounding, target Python applicability, source/signature, selected exact CI log, JSON save, native SQLite Workspace, offline source/facts inspection, action synthesis. Cells are `completed_supported`, `completed_unresolved`, `not_evaluated_by_profile`, `not_activated_prerequisite`, `blocked_unavailable`, `unsupported_input`, `failed_implementation`, `not_measured`—no blank cell means “pass.”
- Read the saved report *and* corresponding primary evidence for at least **one material finding and one material unknown per fresh case** (and the known historical CI excerpt in Q3). Check source identity/time/version roles, what is actually retained versus reference-only, package/environment applicability, quote equality, and no invented runtime/method/action. A syntactically valid report is not a semantic correctness oracle.
- Exercise offline open in a fresh process with network/credentials/model calls disabled or guarded; record exact rejection/error when referenced source text was not retained. A JSON integrity digest establishes bytes, not factual truth.
- Record exit code, activation/status, API GET/redirect/body costs when observed, model POST/latency/usage when observed, wall time, saved report/excerpt counts, bytes/hashes, private file paths **only in private receipts**, and independent evidence review result. Separate startup/preflight/proxy/model-load and product runtime. Treat **unobserved** as unknown, not zero.
- Compare with October historical reports and November AV-Tracer only **by scope/horizon**. A fresh contradiction may indicate changed upstream availability or model/runtime, not necessarily product regression.
- A read-only independent second-pass review by the assistant may identify mistakes but does **not** count as blinded independent-human utility. Record conflicts and repair owner.

## 6. Failure taxonomy, stop lines, and minimal repair policy

| Observed situation | Required label and response | No unsupported substitution |
| --- | --- | --- |
| PR head/base drift, unsupported dependency or missing input | `input_identity_drift` / `unsupported`; preserve preflight, stop this candidate | Do not rebrand a different revision as the same case |
| GitHub 403/429, stale token, proxy/TLS, PyPI failure | `source_unavailable` / `auth` / `transport`; preserve partial results and exact retry/credential policy | No silent token fallback, unlimited retry, or fabricated zero evidence |
| Upstream tag/source-window missing | `prerequisite_not_met`; no model call expected | Do not call model directly and count it as normal product |
| Local model unavailable, POST unsuccessful, schema invalid or unsupported model | `model_provider_problem` / `model_output_unresolved` with request existence explicitly shown | Do not substitute stronger model, change prompt/validator or fake candidate |
| Multiple/contradictory sources or ungrounded semantic candidate | `unresolved`/rejected with source-specific reason | No semantic promotion from model confidence or repeated text |
| Report opens but cited original source is not retained | `reference_only` / `retention_gap` with exact source and consumer need | Do not claim full offline source preservation |
| Exit 0 but required stage never activated | `delivered_partial`; report valid, **coverage open** | Do not count route/LLM activation as passed |
| Unexpected exception, corrupt report, false fact or broken recovery | `implementation_failure`; preserve safe trace, stop downstream inference | Do not hide it behind `abstain` or rerun until green |
| Claims about target installation/runtime, CI job correlation, or source applicability missing proof | `not_established` / `not_evaluated` | Do not infer from wheel listing/green CI/installed-package summary |
| Repeated or late requests beyond frozen budget | `budget_exceeded` and preserve attempted result | No further automatic acquisition |

**Repair rule:** within this qualification B-stage, fix only a blocker necessary for a faithful selected route if independently diagnosed and authorized; record both original failure and subsequent new attempt separately, rerun relevant regressions, refreeze code/inputs. Defer broader capabilities (job discovery, full native normal persistence, generalized source parsing, AI agents, new targeted-check permission) to a separate decision after the review. No “repair” solely to make a planned case appear green.

## 7. Deliverables, acceptance, and final decision

**Private evidence root** outside Git: `~/.local/share/upgradepilot/<unique-cross-profile-qualification-run>/` with an owner-only manifest and `Q1/`, `Q2/` directories, each containing actual invocation/exit/UTC time, report JSON when produced, stdout/stderr sanitized as needed, observed request/model ledger and external response observations, hashes, reopened view proof and brief reviewed claims. Reused Q3 may link to the existing reviewed example archive rather than duplicate its bytes.

**Reviewed, public-safe artifacts** under a new dated `working-memory/evidence/` directory only after sanitization: `RESULTS.md` (overall scope and decision), `coverage-matrix.md`, a concise `qualification-receipt.json` per selected case or one combined index, one source-verified claim/unknown assessment per fresh case, failures/retention/authorization/cost/stop register, and paths to accepted private inputs without embedding home names, signed URLs, tokens, unreviewed raw CI logs, prompts or third-party bodies. Preserve every real attempt, including failed preflight and no-model branches. No unreviewed raw sources get pushed automatically.

**Acceptance is a two-dimensional result:**
1. **Route-level:** Q1 current ordinary artifact investigation is truthfully delivered and reopened or records a diagnosed scope-specific failure; Q2 conditional model path is **actually observed and qualified** if prerequisites permit, otherwise explicitly remains open; Q3 prior combined reference remains independently recoverable and scope-qualified. Any failed live route is an **observed qualification outcome**, not a pass.
2. **Study-level:** every attempted case has frozen identities, method, artifacts or exact stop state, actual coverage matrix, calibrated resource measurements, one primary-source claim review, unresolved/retention states and clear attribution of the earliest missing owner. No “overall system passed 100%” result. Decide **`no_build`**, **`bounded_build:<owner/problem>`**, or **`more_evidence:<exact_missing_condition>`** from the evidence. A completed batch can be valuable even if some routes fail; it must not falsely mark those routes qualified.

**Decision priorities:** If model is blocked by GitHub acquisition, the upstream source owner/routing is first; if a successful candidate is ungrounded, the source-window/validator boundary is first; if correct evidence is hidden, report/consumer is first; if exact failed CI job selection is burdensome, the job-candidate owner is next; if evidence is ready but no justified next check can be admitted, examine the explicit positive action permission rather than add prose; if no decision-relevant gap is found, do not build. The previously selected **decision-focused contrasting maintainer task review follows this qualification**, using actual new case evidence—not a predetermined action or feature.

**Deferred randomized cohort:** only after the deterministic batch and a meaningful unanswered prevalence/robustness question. Define the eligible PR sampling frame, exclusions, frozen list/seed, time horizon, attempts/denominator and interpretation limits before any seeded selection. Do not start broad random testing, independent reviewer comparison or model-evaluation benchmark by default.

## 8. Execution-ready handoff and learning ownership

Before activation, the operator produces a short **Preflight Freeze** with exact case revisions, commit/installed code, accepted source capture/LLM observer, model/credential route, numeric budgets and new private output destinations. The owner then admits **Q1**; after its recorded verification and D learning, proceeds to **Q2** without silently modifying the method; Q3 reuses known proof and any needed offline verification. Preserve A0→A1→A2→B→Verification→D→E and C across the work proportionately, including legitimate stop/deferral paths.

**Learning checks:** (i) How can CLI exit 0 while the model never ran? (ii) Why does `Successfully installed X` differ from actually imported module identity? (iii) What source inspection can distinguish wheel inventory from target viability? (iv) What is lost if only a report JSON survives, versus native Workspace plus retained original excerpt? (v) How do different model/PR/code horizons affect meaningful latency and correctness comparisons? Record owner understanding, not assumed mastery.

**End condition:** Complete and review the matrix and resource/claim checks; close the qualification cycle with honest partials and a specific next product responsibility or no-Build disposition. Update `MEMORY.md` and accepted owners to reflect the *actual* results. This plan makes no claim that the live cases have already been run.
