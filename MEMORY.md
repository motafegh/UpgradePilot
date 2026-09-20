# UpgradePilot Current Memory

**Last updated:** 2026-09-20  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position — main product workstream STARTED

- **Current responsibility:** **AUDIT-008-F4 — CI consuming-job identity → Target artifact-environment composition; A DONE, B source/test implementation DONE, C executable validation NEXT, D/E PENDING**. Normal application integration and test migration are committed and patch-reviewed; **no F4 tests or hosted validation have yet been observed**. Do not mark F4 or any non-abstention maintainer action complete.
- **Primary operation:** bounded Build/Implement + canonical A → B → C → D → E Learning-by-Doing. Source/test implementation was explicitly authorized by Ali after the preceding action-relative comparison. Learning-note artifacts remain out of scope unless explicitly requested.
- **Active working-memory detail:** `working-memory/2026-09-20_f4-ci-consuming-job-target-composition.md`. Completed selection/learning handoff: `working-memory/2026-09-20_action-relative-producer-reachability-comparison.md`. Earlier closed F11/F9/F3 detail remains in the existing dated working memories linked below.
- **Selected plan:** `plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md`; parent `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`. Audit input: `audits/2026-09-19_AUDIT-008_current-system-evidence-to-action-readiness.md` (non-controlling evidence). Accepted action semantics: `docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md`.
- **Route:** `main` unless Ali explicitly changes it. No new maintainer-action permission, external-target mutation, agentic checkpoint activation or unrelated product change is authorized by F4.
- **Parallel learning:** `working-memory/2026-09-19_cycle3-integrated-learning-review.md` continues independently in another conversation. Its exercises do not block the main workstream and must not be marked complete by this one.
- **Completed prior cycles:** Cycle 1 CLOSED; Cycle 2 CLOSED; Cycle 3 CLOSED; F3, F9 and F11 CLOSED at their bounded proof/learning horizons. Do not reopen without concrete contradiction/regression.

## Immediate F4 continuation and exact proof status

**Product issue and bounded change:** `ci/consumption.py::StaticDependencyConsumptionEvidence` already carries a `job_key` for a supported static dependency-consuming CI job. Previously the application lost that key at Target composition, so the conservative Target one-job rule reported ambiguity for a multi-job workflow. F4 now passes the exact supported consuming-job key, verifies workflow/source/revision/repository relationship, and deduplicates by job instead of collapsing distinct supported consuming environments. Target selects the exact matching static job or preserves an explicit problem; direct callers without a selected job keep the previous single-job-only behavior. These changes establish partial *declared* target context only, not exact wheel tags, package installation, behavioral compatibility or permission to merge/block.

**Committed F4 source and test scope:** Target selected-job API `src/upgradepilot/target/artifact_environment.py` commit `a6f0ede6d89eed8d60c979f23a282e43f896819c`; focused Target cases `tests/test_target_selected_consuming_job.py` commit `0d3f32396288a4572b4b2632d0ddc1e2e9af78ee`; normal application composition `src/upgradepilot/investigation.py` commit `9938f2cf8f6499cea309e32c30f9a471df611b34`; migrated normal two-job investigation test `tests/test_investigation.py` commit `687c95b6face49e34190d41b9a74b93d045e019b`; distinct job-specific-dedup/mismatch tests `tests/test_f4_target_job_composition.py` commit `0d246f2c85980fdc9e52c4a1c6fd82ad58043d99`. Source and migration patches were inspected; old test now expects relevant `test` environment rather than obsolete ambiguity. Dated F4 working record owns exact details, limitations and proof checklist.

**Immediate proof gate:** run the focused Target, composition and normal-investigation tests, then deterministic product regression on the updated F4 revision; inspect exact run SHA, installed product checks and test results before recording any pass. `.github/workflows/product-verification.yml` is manually dispatched and includes focused investigation and full deterministic suite. No GitHub Actions dispatch capability is exposed to this session, and the local container cannot resolve GitHub to clone the repository; **the historical F9 hosted green run is not F4 test evidence**. If a new test fails, diagnose/fix it before closure. F4 D must teach the actual code/data flow and one meaningful changed case after observed proof, not infer ownership from source written by AI.

## Prior closed milestones and proof limits

### F3 — CLOSED

[Product verification run #6](https://github.com/motafegh/UpgradePilot/actions/runs/35465839476), attempt 1, succeeded on exact checkout `08a3f70b5717255d7ed5f96ff3ec3ef67bfe4942`: Python 3.12.14, fresh install/pip check/installed CLI PASS, focused investigation 15/15, deterministic product regression 608/608. Bounded synthesis returns explained abstention; F3 is not proof of any non-abstention action. Detailed work: `working-memory/2026-09-19_f3-hosted-verification-and-f9-handoff.md` and `working-memory/2026-09-19_1825_parent-synthesis-evidence-path-reaudit.md`.

### F9 — CLOSED

Ordinary public-PR CLI calls default to anonymous GitHub access despite ambient `GITHUB_TOKEN`; `--github-auth token-env` deliberately opts into token use, with missing/empty-token rejection. GitHub-owned Requests session excludes unintended `.netrc` auth; proxy handling is separate. [Product verification run #7](https://github.com/motafegh/UpgradePilot/actions/runs/35516933780), attempt 1, succeeded on exact F9 checkout `2afc566a4ce2139f3439d6a4c3cf9596896b3841`: fresh install, installed CLI checks, focused 15/15 and regression 616/616 including 8/8 F9 tests. Ali correctly reasoned default-token behavior. This is not a live public-PR/real-token/proxy acceptance claim. Detail: `working-memory/2026-09-20_f9-public-github-authentication-phase-a.md`.

### F11 — CLOSED

Stale AUDIT-005 ACTIVE index entry moved to SCHEDULED with actual B2/X1 plan link and explicit non-skippable handoff once the current evidence-to-action journey finishes or is explicitly stopped/replanned; AUDIT-008 remains sole active audit input. No agentic model evaluation/adoption, product-code change or repository-wide stale-file scan occurred. Detail: `working-memory/2026-09-20_f11-audit-lifecycle-reconciliation.md`. Scheduled index: `audits/scheduled/README.md`.

### Cycles 1–3 — CLOSED

Retain proven exact CI run/job attempt identity, frozen-revision dependency source provenance, ADR-0009 parser-backed static workflow command analysis, one shared command traversal feeding dependency/environment/invocation observers, and bounded source-occurrence ↔ runtime-step correlation. Historical Cycle-3 hosted proof: GitHub Actions run `35448172928`, fresh installation and CLI PASS, focused investigation 15/15, Cycle-3 focused 76/76, full deterministic regression 604/604; earlier Cycle-2 regression 587/587 is a distinct proof horizon. S001 sole ordinary top-level and S002 first sequential Bash command are admitted positive execution-position families; S004 `&&` short-circuit remains unresolved/deferred.

**Proof boundaries:** Static presence/order is not actual execution/order. A supported, exact correlated completed/successful runtime step establishes `supported_runtime_correlated` at bounded step/occurrence strength; not exact installed version/artifact, direct inner-command success, compatibility, update safety, or maintainer-action permission. An ambiguous/ineligible occurrence does not gain runtime strengthening; known runtime non-success remains a fact without forcing a broader coverage conclusion. Preserve unresolved states rather than making positive assumptions. Dated details: `working-memory/2026-09-17_cycle3-runtime-strengthening-phase-a-orientation.md`, `working-memory/2026-09-18_cycle3-runtime-strengthening-build.md`, `working-memory/2026-09-19_cycle3-integrated-learning-review.md`.

## Parent synthesis authority and next-step guard

`PROJECT_CHARTER.md` owns the outcome family; accepted synthesis specification owns action-specific positive permission and abstention; current `src/upgradepilot/maintainer_action.py` admits only `abstain`. Accepted semantics do not mean normal producers make other actions reachable. F4 is a correct-source/job composition precursor for an eventual target-specific evidence path. The artifact candidate and published wheel inventories do not prove exact target wheel compatibility or source-build failure; CI green does not prove compatibility or merge permission.

**After actual F4 completion,** reassess which one decision-critical producer/normal composition premise is still missing according to the active plan. F5 target wheel-tag observation, F6 exact runtime dependency/artifact witness, F7 bounded favorable discovery/context and new genuinely demonstrated gaps remain unselected candidates, not a feature queue. Preserve AUDIT-005's scheduled checkpoint at the explicit route handoff.

For historical detail not repeated here, the previous complete live-state record is preserved in Git history at `0d3f32396288a4572b4b2632d0ddc1e2e9af78ee:MEMORY.md`, and all dated working-memory/plan/specification owners remain in place. Do not treat the dated records as competing live-state owners.
