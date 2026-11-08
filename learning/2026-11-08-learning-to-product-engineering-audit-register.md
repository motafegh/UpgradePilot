# Learning-to-product engineering audit register

**Created:** 2026-11-08 · **Compared main:** `b56ad634e421fb3d639141054da52260e83c7410` · **Learning branch:** `learning/current-caller-signature-mastery-roadmap-2026-11-02`  
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
| LPA-004 · OpenCV selected-facts inspection | F2/F3 | Documented scoped limitation | Task-gated, bounded typed-fact access, not a repair of original-text source command |
| LPA-005 · First-view independent usefulness | F3 | Pending product gate | Reviewer packet prepared; authorized participant outcomes still absent |

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

### LPA-004 — Saved OpenCV artifact tag facts versus original-text CLI access

**Observed:** the [first-view implementation review](../working-memory/2026-11-08_maintainer-report-first-view_build-cycle.md) confirms `source-13` has exact OpenCV wheel-tag facts in saved `selected_facts` JSON, while `--show-source` refuses because that command displays only *retained original text*. This is **not data loss**. Overview counts remain correct (27 removed, eight added).

**Potential improvement:** when an exact-tag maintainer task is selected, compare direct JSON inspection with a bounded typed-fact viewer; preserve `--show-source` refusal for non-original-text records.

**Required before action:** concrete user task and evidence/field identity, cost, CLI naming, bounded errors, focused tests and authorization. **Status:** `documented_limit`; already recognized by main, not an independently selected fix.

### LPA-005 — Verify first-view usefulness independently before adoption claims

**Observed:** [report renderer Build](../working-memory/2026-11-08_maintainer-report-first-view_build-cycle.md) passed 61 focused and 1,078 product tests. The [revision-3 reviewer technical recheck](../working-memory/2026-11-08_maintainer-first-view-review-readiness_planning-cycle.md) resolved task/rubric ambiguity. The [GitHub rehearsal summary](../working-memory/evidence/2026-11-08-maintainer-first-view-review/remote-rehearsal/README.md) is derivative and does not supply all owner-local original-text access.

**Required before usefulness claim:** eligible independent participants, equivalent authorized evidence access, frozen tasks/rubric/timing, recorded outcomes and failures. This is managed by the existing [maintainer usefulness plan](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md), not an independent duplicate experiment.

**Status:** `pending_product_gate`; no new bug, no measured human benefit.

## Current audit disposition

No verified product defect is admitted from the present learning discussion. LPA-001/002 are research/design candidates, LPA-003/005 are already-gated product responsibilities, and LPA-004 is a bounded user-facing access opportunity. Do not implement or merge any entry without comparing current main and selecting a specific acceptance proof.

**Current learning:** C2 remains in progress (10/14 guided slices taught). Next tasks are exact source-ID reconstruction, saved report/cold-opening and result-decoder refusal. This file is a tracking aid, **not an extra learning module**.
