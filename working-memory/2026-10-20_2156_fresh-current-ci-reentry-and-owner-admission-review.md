# Main re-entry: fresh current CI cohort and existing-owner admission

Date: 2026-10-20. Reviewed main at e3e5a736 after fast-forward from c381c02a.
Primary responsibility: read-only project re-entry plus bounded source/evidence review. Ali requested reassessment of the new fresh-CI cohort and current owners before selecting main continuation. Standing instruction authorizes progressive records/commits/pushes. No product, test, cohort raw, plan, specification or ADR change is part of this review.

Previous: [retained CI comparison cycle](2026-10-20_1924_retained-native-ci-baseline-comparison_build_lbd-cycle.md). Parallel completed evidence: [corrected cohort cycle](2026-10-20_2010_fresh-current-ci-diagnostic-cohort_build_lbd-cycle.md).

## Re-entry and procedure boundary

A0 — DONE: refreshed remote main; inspected the 28-commit delta, controlling route/product boundaries, cohort/corrections/manifests/verifier, active source/tests and relevant runtime/Investigator plans. No product/test/plan/spec/ADR/MEMORY changes occurred in the incoming cohort delta. Existing unrelated October 3 untracked audit is preserved.
A1 — CURRENT: current-state/continuity packet and recommendation delivered for Ali's challenge. Learner understanding not assessed.
A2 — PENDING for a selected follow-on diagnostic.
B — NOT ACTIVATED for a new FCI correlation/runtime/full-product run or repair.
Verification — GREEN for the narrow review: corrected bundle verifier passes; 20 existing acquisition/correlation unit tests pass; retained-input representation probes reproduce job-admission gaps. These are not completed three-case correlation results.
D/E — NOT claimed closed for a new main cycle; predecessor ownership debt remains separate.
C — preserve material re-entry evidence here; MEMORY.md alone owns live continuation.

Procedure adaptation: Ali first requests orientation/critical reassessment before choosing the next responsibility. Standalone re-entry plus bounded audit is used; A0 includes source checks and non-destructive parser probes needed to distinguish readiness from a product defect. Opening an implementation cycle or repeating the old proposed A2 would prematurely select the work. This record preserves the A0/A1 boundary; follow-on A2/pre-B gates remain intact. No substantive product/experiment implementation is inferred from this review.

## Verified change since our last handoff

Incoming work creates an exposed three-case fresh-current-CI cohort with immutable provider/source data, candidate decisions, readiness matrix, verifier, final report and closed cohort cycle. No source owner changed. The sole live MEMORY had not incorporated the cohort, so its presentation-first recommendation was stale as a continuation choice, despite remaining valid historical reasoning.

The [cohort README](../product-simulation/fresh-current-ci-diagnostic-2026-10-20/README.md), [corrections](../product-simulation/fresh-current-ci-diagnostic-2026-10-20/RETENTION_CORRECTIONS.md), [readiness matrix](../product-simulation/fresh-current-ci-diagnostic-2026-10-20/READINESS_MATRIX.md), [verification record](../product-simulation/fresh-current-ci-diagnostic-2026-10-20/REPLAY_VERIFICATION.md) and [final report](../product-simulation/fresh-current-ci-diagnostic-2026-10-20/FINAL_REPORT.md) are read together, not at their earlier superseded closure.

Two retention defect classes were repaired additively: reconstructed PR-diff whitespace for openai-agents/PasarGuard, and omitted final newlines in the first openai-agents workflow and mdformat workflow/base/head requirements copies. Flawed raw objects remain immutable/non-authoritative. Manifests now select exact diff/source overlays; seven source artifacts bind recorded frozen upstream Git blob IDs. Local re-verification passes 21 declared artifacts (including preserved flawed copies) across 5/9/7 per case. These checks bind retained bytes to recorded identities; no live upstream reauthentication or HTTP-wire archive is claimed.

FCI002's expected first refusal was corrected from a generic matrix description to static_job_name_missing for pre-commit. Current correlator iterates jobs in YAML order, checking strategy and then literal name within each job. The first ordinary pre-commit job lacks a name; the later tests matrix is a secondary independent unsupported shape. The bundle verifier checks that declared expectation, not execution of the correlator.

Historical glyphsLib's empty captured step arrays remain true for that freeze, and a job-name fallback still would not supply missing steps. Current rich step captures disprove treating that observation as a universal provider limitation. They do not retrospectively repair the old capture, explain why it was empty, or change prior model overclaim/inadequacy judgments.

## What the cases can and cannot test

| Case | Retained evidence/current contract pressure | Stronger result not earned |
| --- | --- | --- |
| FCI001: openai agents/mcp, run 39372679381 attempt 1 | One literal named ordinary job, four runtime steps including two skipped user steps. Expected positive identity correlation; useful skipped-status preservation control | No mcp installation/exercise/compatibility witness. uv/lock shape and skipped user steps do not enter the admitted direct-requirements/pip state family |
| FCI002: mdformat-footnote/tox, run 36798375619 attempt 1 | Thirteen jobs: eleven non-empty step arrays and two null skipped publish-job step fields. Expected first static_job_name_missing; later matrix remains unsupported | No tox exercise: workflow uses flit/pytest/pre-commit/build, not the changed requirements file/tox route. Null is unavailable, not an observed empty list |
| FCI003: PasarGuard/FastAPI, run 39445488948 attempt 1 | Five rich step arrays and non-matrix static jobs lacking display names. Expected static_job_name_missing. Preserve reported empty run pull_requests relation | Make-target success is not exact FastAPI installation/exercise. No inferred PR-array entry or YAML-key/display-name fallback |

These are correlation-shape/input diagnostics, not a complete retained public-PR investigation, dependency-state positive cohort, protected evaluation, semantic comparison, usefulness study or action-permission proof. Selected-run evidence does not retain every workflow/source/dependency input used by the complete normal acquisition/investigation route.

## Confirmed retained-input admission gap

Source chain: [GitHubActionsClient](../src/upgradepilot/github/actions.py) owns exact-head run and exact-attempt job acquisition plus field/identity parsing; [prepare_ci_evidence](../src/upgradepilot/investigation_inputs.py) orchestrates it; [correlate_workflow_runtime](../src/upgradepilot/ci/workflow_runtime_correlation.py) relates admitted typed static/runtime evidence; [dependency state](../src/upgradepilot/ci/dependency_state.py) composes a stronger, separate proposition; report/Investigator and maintainer synthesis consume those facts at their own boundaries.

All three selected_run objects omit workflow_id, but each exact_head_runs list retains a unique matching id/workflow_id. Explicitly joining those records recovers a run field without guessing. All 19 job records omit head_sha, required by the normal job parser. No equivalent job-level head field was found in the declared cohort artifacts. Do not copy the PR/run head into each job and present it as a retained provider observation.

Read-only discriminating probes used the real existing representation parsers: selected-run dict joined to retained workflow_id; a minimal identity object carrying only the frozen head required by the parser; no fabricated full PR. Result: three joined runs parse, but every raw job fails with “GitHub workflow-job item is missing required field: head_sha.” Case counts 1/13/5. This is not a public transport/pagination replay, correlation result, native producer run or model call.

Additional admission limits: exact-head run-list captures are reduced records rather than complete normal parser responses; total_count/page envelopes are not retained, and only selected-run jobs/workflow sources are included. jobs_attempt provenance declares run/attempt identity in text but does not itself retain a literal attempts/{n}/jobs request/response archive. The cohort's recorded attempt association is preserved; exact-attempt endpoint behavior is separately protected by current product unit tests, not independently proved by these reduced captures.

Classification: a concrete input-completeness/readiness gap for faithful existing-acquisition-parser replay, **not a demonstrated defect in product acquisition**. The existing refusal is correct for missing required input. Cohort byte/source-fidelity verification remains valid within its declared proof class. A narrowly scoped correlation adapter would need explicit derived/missing field provenance and its claims could not include acquisition correctness. Do not weaken a product contract merely to make a diagnostic run.

## Fresh checks and proof limits

- python3 product-simulation/fresh-current-ci-diagnostic-2026-10-20/verify_bundle.py: PASS; job counts 1/13/5; source-upstream binding counts 1/3/3; FCI002 null/non-empty preserved.
- Existing parser probes: three selected runs parse after a declared exact-ID join; all 19 job records refuse missing head_sha. No data filled or rewritten.
- PYTHONPATH=src:tests:. .venv/bin/python3 -m unittest test_github_actions test_workflow_runtime_correlation -v: 20 tests pass in 0.011 seconds. They protect exact attempts, job/run heads, step preservation, names, matrices, ordered matching and unresolved cases. They do not run these three new FCI cases through the complete owners.
- No fresh cohort correlation/runtime-state/full-investigation run, provider/model prediction, new target evidence acquisition, target code execution or install occurred. Git metadata fetch is separate from target evidence.

## Reassessed main continuation

Recommendation supersedes the old presentation-first recommendation as the immediate main priority: **retained-input admission followed by a bounded existing-owner current-CI diagnostic**.

1. Freeze authoritative manifest-selected sources and declare the exact proof seam. Recover missing normal-parser fields/request identities from original retained capture evidence if actually available; otherwise preserve input-unavailable. Any new live acquisition is a separately labelled observation, never a hidden repair of the October freeze. Run workflow_id may be joined by exact retained run ID; job head must not be invented.
2. Separate a faithful selected-run provider/representation diagnostic from a deliberately narrower correlation-only projection. Do not call either a complete public-PR replay. If an adapter derives scope metadata, expose that premise and exclude the corresponding independent acquisition claim.
3. On admitted inputs, exercise FCI001's ordinary-job identity path while retaining skipped statuses; FCI002's first missing-name refusal and null-step availability; FCI003's missing-name refusal. No requirement to broaden named/matrix support or produce a positive runtime-state witness.
4. If retained evidence contradicts admitted supported behavior, preserve the minimal reproducer and fix the earliest responsible owner under Build authorization. If data is missing, repair the capture/retention/readiness boundary; if unsupported by design, preserve the refusal. No automatic lower-level feature expansion.
5. Use those results to decide whether Investigator/report presentation should be next. Existing unresolved-state promotion remains a real separate interpretation problem; richer current provider evidence does not erase it. No new model arm, multi-role architecture or positive action is selected.

Why this is product-connected: it checks whether the admitted evidence chain survives realistic current input before spending on presentation or broadening semantics. It is temporary component proof, not a replacement for Charter's PR-to-useful-report responsibility. Re-enter runtime-state capability with an actual admitted environment/command/state case or an explicit design decision; re-enter independent usefulness/protected evaluation under their own gates.

Broader owner reconciliation: the project route admits evidence-gated X1 and reports before positive action without waiving B2–B5 duties. Runtime-state Cycle 1 is closed; matrix/unnamed/uv/environment/direct-observation expansions and Cycle 2 remain conditional. ADR-0010 keeps correlation, exact command execution and requirement state separate. Maintainer synthesis is still abstain-only; no fresh CI observation changes action prerequisites. Completed Investigator comparisons remain negative/limited and cannot be silently rerun or pooled. No stable plan/spec/ADR change is justified merely by this cohort review.

Ownership reactivation: explain why correlated skipped steps are a valid identity control but no installation proof, and why a missing provider job head is a different issue from an intentionally unnamed YAML job. Ali has the re-entry packet for challenge; no mastery/next Build authorization is inferred.

UP-SKILL:upgradepilot-project-reentry-orientation
UP-SKILL:upgradepilot-repository-audit
UP-SKILL:upgradepilot-working-memory

Review-record validation: two Markdown owners/58 local references resolve; fences/newlines and git diff --check pass. Current origin/main rechecked at e3e5a736 before publication. Cohort, product source/tests, plans, specs/ADRs and governance remain unchanged from that horizon. This preserves the reassessment under Ali's standing recording/publication instruction, not a new executable responsibility.
