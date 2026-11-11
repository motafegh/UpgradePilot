# Learning-to-product engineering audit register

**Created:** 2026-11-08 · **Last reconciled main:** `f84da7f90a1d0c74ccb21e4569d63407bd47b9b9` (2026-11-11) · **Learning branch:** `learning/current-caller-signature-mastery-roadmap-2026-11-02`
**Related:** [learning roadmap](2026-11-02-caller-signature-native-pipeline-mastery-roadmap.md) · [source and engineering-history map](2026-11-06-caller-signature-module-reference-map.md)

This document preserves engineering observations surfaced during learning for eventual **evidence-based, selective product triage**. It is **not an approved bug list, product roadmap, implementation authorization, or automatic merge instruction**.

## How to maintain and eventually hand off

For each new item, record: stable ID, module, source horizon, **observed fact**, **hypothesis or possible improvement**, what a current product owner already handles, evidence needed to validate/change, and decision status. Do not convert an unanswered question or a known limitation into a defect. Reconcile with updated `main` before modifying an item's state. Preserve historical evidence, rejected attempts and superseded ideas.

Allowed dispositions: `documented_limit`, `hypothesis`, `pending_product_gate`, `verified_defect`, `ruled_out`, `implemented_verified`. After learning completion, review current evidence and send **only accepted, still relevant candidates** for separate product plans/changes. No bulk merge or automatic fixing. Learning work does not modify production source, tests or evidence.

## Candidate register

| ID | Module | Classification | Product disposition |
| --- | --- | --- | --- |
| LPA-001 · Starlette sample versus installed version | C2/E3/G1 | Documented limit + hypothesis | Preserve sampled record; only investigate an admitted exact target-version basis |
| LPA-002 · Traceable resolution of witness premises | C2/D2/F2 | Hypothesis | First test whether existing report evidence actually leaves a maintainer question unanswered |
| LPA-003 · Actual affected-call runtime observation | G1 | Pending product gate | Historical merged HTTPX case explicitly deferred by main |
| LPA-004 · OpenCV selected-facts inspection | F2/F3 | **Implemented/verified** | Bounded `--show-facts` now supports artifact and package metadata saved facts; original-text view unchanged |
| LPA-005 · First-view independent usefulness | F3 | Pending product gate | Two exposed AI slots answered 30/30; independent human/time utility still unmeasured |
| LPA-006 · Multiline CI fact rendering | F2/F3 | **Verified defect → implemented/verified** | Six/seven real saved commands diagnosed and corrected in shared renderer; no new runtime proof |
| LPA-007 · Verified public GitHub repository moves | D1/E3 | **Implemented/verified** | One-hop, public ID/name/tag verification with canonical source identity and v1/v2 retention |
| LPA-008 · Exact changed-version source priority | D1/E2/F3 | **Implemented/verified** | Earlier AV-Tracer capture omitted proposed HTTPX after incidental exploration; successor acquired both definitions within an explicit 56-call allowance |

### LPA-001 — Exact adapter-version authority, not replacing a historical sample

**Observed:** [`select_exploration_version`](../src/upgradepilot/caller_signature/source_acquisition.py) picks the newest stable release satisfying a visible declared specifier and labels it `constraint_sample`. The [November 7 HTTPX witness](../working-memory/evidence/2026-11-07-native-proxy-successor/RESULTS.md) uses sampled Starlette 1.10.0. That is **not proof that the target installed Starlette 1.10.0**. Exact HTTPX 0.27.2/0.28.1 declaration evidence answers a different question.

**Hypothesis:** For a future decision-relevant case with qualified actual target-version data, capture a separate version/source basis and analyze the applicable adapter path. Do **not** silently substitute that version for the old sampled witness or infer loaded module identity from a bare version string.

**Required before action:** identify exact lock/install/runtime source and environment identity, distinguish declaration from resolved install and loaded file, check current source association and budget owners, design a paired/branch-preserving outcome test.

**Status:** `documented_limit` + `hypothesis`; not a verified defect or selected new detector. Revisit under E3/G1 only if actual evidence resolves the decision.

### LPA-002 — Premise traceability if actual maintainer tasks require it

**Observed:** [live witness premises](../working-memory/evidence/2026-11-07-native-proxy-successor/results.json) preserve conditional fallback, re-export, class/MRO, receiver and target-installed-runtime assumptions. The new [maintainer first view](../working-memory/2026-11-08_maintainer-report-first-view_build-cycle.md) already renders conditionality and points to detailed source/witness records.

**Hypothesis:** A bounded premise → proposition → owner/observation → evidence/horizon interface might reduce navigation or enable evidence-specific resolution. It is not justified merely because the existing reason strings look incomplete.

**Required before action:** a real unanswered/slow maintainer task, existing saved-field inventory, comparison of report-only improvements against new producer logic, no invented proof. **Status:** `hypothesis`, defer.

### LPA-003 — Exact test-call runtime observation remains a separately gated responsibility

**Observed:** the [HTTPX CI/runtime checkpoint](../working-memory/2026-11-07_httpx-ci-runtime-applicability_cycle.md) retained July's bounded Docker CI, October's zero exact-head workflow runs and November's conditional static source evidence as **distinct horizons**. None witnessed the target's `TestClient(app)` invocation or loaded callable identity. Main explicitly deferred a new combined/runtime producer for the already-merged PR.

**Possible later scope:** in an actionable new case, start from target-owned evidence of exact process/run/checkout/interpreter, reached call, dispatch branch, loaded callable/file and installed artifact; only then decide if extra instrumentation is necessary, proportionate and authorized.

**Status:** `pending_product_gate`; current behavior is correct abstention, **not** a defective CI parser.

### LPA-004 — Saved selected-facts inspection implemented for admitted kinds

**Original limitation:** OpenCV source-13's exact wheel-tag changes were saved under `selected_facts`, but original-text-only `--show-source` rightly refused. This was a navigation/access issue, **not source data loss**.

**Verified selected Build:** [November 8 design/implementation and real-source proof](../working-memory/2026-11-08_saved-report-selected-facts_planning-cycle.md) adds [`--show-facts`](../src/upgradepilot/cli.py) for saved artifact capabilities and package metadata, checks the report and source identity, and displays provenance plus every exact keyed value. Real OpenCV 37 and Soup Sieve 12 field comparisons match; the ordinary report/HTTPX original text views are byte-identical; 1,080 product tests passed. Unknown, empty or unsupported selected sources still refuse and original-text access stays restricted.

**Disposition:** `implemented_verified` for these two selected types only. Full CI job inventories, general Workspace fact search, target wheel compatibility and independent usefulness were not implemented or established. Do not re-open without a new concrete task.

### LPA-005 — Verify first-view usefulness independently before adoption claims

**Observed:** [report renderer Build](../working-memory/2026-11-08_maintainer-report-first-view_build-cycle.md) passed 61 focused and 1,078 product tests. The [revision-3 reviewer technical recheck](../working-memory/2026-11-08_maintainer-first-view-review-readiness_planning-cycle.md) resolved task/rubric ambiguity. The [GitHub rehearsal summary](../working-memory/evidence/2026-11-08-maintainer-first-view-review/remote-rehearsal/README.md) is derivative and does not supply all owner-local original-text access.

**Required before usefulness claim:** eligible independent participants, equivalent authorized evidence access, frozen tasks/rubric/timing, recorded outcomes and failures. This is managed by the existing [maintainer usefulness plan](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md), not an independent duplicate experiment.

**Newer evidence:** the [exposed two-slot AI rehearsal](../working-memory/2026-11-08_maintainer-first-view-review-readiness_planning-cycle.md#ai-rehearsal-result) recovered three cases per slot (30/30 combined answers) but used a derivative HTTPX summary, without independent human comparison or equal timed access. The gate remains open.

**Status:** `pending_product_gate`; no new bug, no measured human benefit.


**Latest November 11 exposed-task evidence:** [Strict one-Workspace-revision comparison](../working-memory/2026-11-11_av-tracer-same-evidence-first-view-comparison_lbd-cycle.md) verified one inserted rejected-keyword line at the first view without changing report SHA/source citations, but was performed by a case-familiar analyst, not independent reviewers. The final D/E learning closure recommends **only a readiness assessment** for a multi-case, independent, equal-evidence reviewer pilot; at least three distinct cases and two reviewers with frozen oracle/tasks, actual navigations, answers and time. Neither a pilot nor a human utility pass has occurred. LPA-005 remains `pending_product_gate`.
### LPA-006 — CI multiline command rendering: verified defect repaired

**Actual incident:** [Real glyphsLib CI-only and Soup Sieve full-report walkthrough](../working-memory/2026-11-09_ci-dependency-exercise_report-walkthrough-cycle.md) showed command-valued assessment facts retained embedded LF, while shared rendering removed those controls and joined distinct commands. The *display* was incorrect, while typed evidence and CI states were intact.

**Implemented repair:** [Shared renderer](../src/upgradepilot/report.py) splits command/fact values on LF and prefixes continuation rows before terminal safety filtering. Red/green tests also prevent label-shaped text/control escape from impersonating a separate finding. Six real glyphsLib and seven real Soup Sieve facts, 70 focused product, seven experimental and 1,081 full product tests passed. Display version 4 is not saved schema or evidence owner migration.

**Disposition:** `implemented_verified`. Retain as a genuine diagnosis/repair example for F2/F3; no open product repair.

### LPA-007 — GitHub repository moves: original source admission obstacle now resolved

**Observed:** The [AV-Tracer split-route capture](../working-memory/2026-11-10_av-tracer-split-route-qualification_cycle.md) stopped on a GitHub 301 tag lookup for the declared FastAPI source. Blind redirect would risk a foreign provenance claim; unconditional refusal prevented examining the actual renamed public source.

**Verified repair:** [Repository-move Build](../working-memory/2026-11-11_caller-signature-repository-move_build-cycle.md) verifies one-hop public GitHub repository ID and canonical name plus exact tag and content under the same request ledger; real FastAPI and Starlette moves succeeded. Typed source-family codec2 preserves declared versus canonical identities, refusal states and historical v1 support. 1,096 tests passed at this milestone.

**Disposition:** implemented_verified. Not an open defect, general redirect permission or proof of installation.

### LPA-008 — Exact source-version selection and limited-budget allocation

**Observed:** [First verified-move AV-Tracer run](../working-memory/2026-11-11_caller-signature-repository-move_build-cycle.md) spent all four library release slots on FastAPI, Starlette, incidental pytest and old HTTPX; proposed HTTPX 0.28.1 was not queried. Source-pair comparison was impossible although the relevant target call and old source were retained.

**Verified repair:** [Exact-version allocation Build](../working-memory/2026-11-11_caller-signature-exact-version-allocation_build-cycle.md) prioritizes the known old/proposed dependency after a relevant indirect adapter path is found, and uses member-guided source closure. A separately approved successor acquired defining files on GitHub calls 44 and 45, retained old bound/proposed rejected app= with partiality, and used 51 of the explicitly selected 56 GitHub calls. 1,099 product tests passed.

**Disposition:** implemented_verified for this case, not a universal completeness claim and not a global default-policy increase. Revisit only for a new decision-relevant case demonstrating a remaining selection failure.

## Current audit disposition

No **open** verified product defect is admitted from this learning discussion. LPA-001/002 are still hypotheses; LPA-003/005 remain existing evidence/usefulness gates; LPA-004, LPA-006, LPA-007 and LPA-008 are now implemented/verified at their bounded scopes. The new AV-Tracer exact source pair does not settle LPA-001: the upstream adapter is still sampled, not observed as installed/loaded in that target process. The isolated OmniMatch named-test comparison is a separate developer process and does not close the target-owned G1 runtime observation gate. The [OpenCV/TileDB screening](../working-memory/2026-11-08_target-wheel-applicability_qualification-cycle.md) and [Aruba package-state/decision comparison](../working-memory/2026-11-09_aruba-maintainer-decision_comparison-cycle.md) remain under their current project owners, without separate selected product repairs. Do not bulk-merge speculative items.

**Learning-branch preservation incident — November 9:** This document was present at learning commit `08211717` but absent from the later `70511f28` branch tree when a newer sync was based on the main tree. Restored it from the original preserved commit and reconciled it here. The [learning main-sync protocol](2026-11-02-caller-signature-native-pipeline-mastery-roadmap.md) now requires an explicit three-document post-publication check so an earlier parent is not mistaken for current file retention.

**Current learning:** C2 remains in progress (11/15 guided slices taught). Next tasks are exact source-ID reconstruction, saved report/cold-opening and result-decoder refusal. This file is a tracking aid, **not an extra learning module**.
