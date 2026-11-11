# AV-Tracer signature first-view precision — Build / Learning-by-Doing cycle

Date: 2026-11-11
Selected responsibility: improve the deterministic saved-report first view for native caller/signature results, using existing recorded violation/keyword facts, with no new source analysis, execution, provider calls, model inference or public schema change.
Control owners: [MEMORY](../MEMORY.md); [review/evidence decision](2026-11-11_av-tracer-combined-evidence-runtime-applicability-and-ai-checkpoint_cycle.md); [learning readiness](2026-11-11_av-tracer-maintainer-ownership-learning_followup.md); `src/upgradepilot/report.py::_signature_overview`; `tests/test_caller_signature_delivery.py`.

UP-SKILL:upgradepilot-build-implement. UP-SKILL:upgradepilot-learning-by-doing. UP-SKILL:upgradepilot-working-memory.

## Cycle status
- A0 — DONE: reconciled GitHub main `58e4f2f82f28477f0444dff22bd177041eec3bca`; local `main` was fast-forwarded non-destructively from `af92c23f`. Unrelated untracked `working-memory/2026-10-03_broad-project-and-future-plans-audit_lbd-cycle.md` remains untouched. No branch per Ali's explicit preference.
- A1 — DONE (continuing dialogue): actual saved AV-Tracer first-view, causal-vs-static limits, and prior learning exercise already discussed and acknowledged; no new onboarding uncertainty introduced by this bounded renderer task.
- A2 — DONE (continuity-compressed): renderer reads existing typed `ReportAssessment.facts`, displays old/proposed outcomes, must not infer runtime execution, and must refuse invented named violations for conflicting/missing witnesses. Ali explicitly activated the next Build after the learning checkpoint; previous conceptual explanation and exercise satisfy the task-level pre-B gate.
- B — DONE: evidence-grounded rejected-keyword summary implemented in the existing renderer; tests cover alternative keyword, missing evidence, contradictory witnesses, and other violation reasons. No schema or producer changes.
- Verification — GREEN: final complete suite **1,100/1,100** (`PYTHONPATH=src .venv/bin/python -m unittest discover -s tests -p 'test_*.py'`, exit 0), report-projection suite 14/14, repaired controlled delivery test, exact offline AV-Tracer report with original SHA-256 unchanged, `git diff --check` clean. The first failed 29-test attempt is separately retained below.
- D — CURRENT: review the actual source/test changes with Ali, and check whether he can distinguish supported single-witness detail from conflicting/missing detail. No independent learner ownership claim yet.
- E — PENDING: close with actual evidence and handoff.
- C — CONTINUOUS: note meaningful change/failure/correction without raw copied third-party sources.

## Build question and expected proof
Can the human first view immediately identify an exact `unexpected_keyword` from existing native witness facts when those facts are unambiguous, without attributing it to the historical pytest failure or manufacturing a reason from absent data? Preserve original deep witness display and honest CI/runtime `not_evaluated`. The tests must distinguish one supported rejection, non-`app` keyword, contradictory witnesses, missing violations, and original source-only cold report. No source schema, parser, provider or model change.

## Recorded outcomes
- Implemented a deterministic first-view addition in `_signature_overview`: read the proposed rejected witness's saved `violation_*` facts and print `Rejected keyword: <parameter>` only when the reason is an unambiguous `unexpected_keyword`. For other recorded reasons, print `Recorded violation`; for missing details, say not recorded; for disagreeing same-state witnesses, withhold the precise result and give an explicit conflict. The original detailed report, source references, action status, and `not_evaluated` labels remain unchanged.
- Added regression controls in `tests/test_caller_signature_delivery.py` for a non-AV-Tracer `option` rejection, renamed `proxies` case, missing violation, conflicting witnesses, and another violation reason. Existing guards against missing pairs, mismatched roots and contradictory outcome states remain.
- **Meaningful failure and correction:** The first version of the controlled delivery assertion expected `app` by analogy with AV-Tracer. It failed because the controlled case actually rejects `option`. The product rendered the correct value `option`; the test, not the renderer, was wrongly hardcoded. Repaired the test to demand `option` and reject `app`. The rerun of the exact previously failed test passed (1/1); the new cases passed their dedicated targeted run (1/1). The initial 29-test suite run therefore failed 1/29 due to this test assertion; it is not presented as a green run.
- **Saved-report validation:** Original AV-Tracer `report.json` digest `85fd07790ebb0e44eecda9b1f6688251e1d0dec7dc2d340dc66beb9105d69bd3` was unchanged before/after offline reopening. The exact first view printed `Proposed 0.28.1: arguments rejected`, `Rejected keyword: app`, conditional source assumptions, CI `not evaluated` and runtime `not evaluated`.
- **Report projection tests:** 14/14 passed in `tests/test_report.py`.
- **Broader regression:** Full `PYTHONPATH=src .venv/bin/python -m unittest discover -s tests -p 'test_*.py'` completed **1,100 tests, OK, exit 0**, observed in `.tmp/av-tracer-firstview/full-suite.log` and its terminal process completion (duration recorded as 200.143 seconds by unittest). This is the final passing run, separate from the earlier failed focused attempt.
- **Source review:** `git diff --check` passed, only the intended product/test files and cycle record were edited; Ali's pre-existing untracked October file remains untouched.
