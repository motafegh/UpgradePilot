# CI aggregate explanation Build cycle

**Opened:** 2026-11-14
**Scope:** Correct the ordinary CI summary after the [ApplyPilot/pyee qualification](evidence/2026-11-14-cross-profile-q4-applypilot/ANALYSIS.md#maintainer-walkthrough-and-qualification-disposition). Ali authorized the selected Build and requested progressive Learning-by-Doing. [Prior qualification cycle](2026-11-12_cross-profile_e2e_qualification_execution_lbd-cycle.md) · [Execution plan disposition](../plans/CROSS_PROFILE_REAL_PR_END_TO_END_QUALIFICATION_EXECUTION_PLAN.md#fifth-gate--practical-maintainer-task-and-qualification-disposition)

## Cycle status

- **A0 — DONE.** Fetched origin. Local and remote main agreed at `525de3b2`. The latest delta from qualification closeout records deferred peer-constraint research and changes no source or tests. Rechecked the exact saved report digest, relevant evaluator and report projection, and existing CI controls. Initialized this record.
- **A1 — DONE.** Ali identified the failed installation step as the observation the summary should preserve. Onboarding clarified that the step outcome and the cause of the pip error require different evidence.
- **A2 — CURRENT.** Oriented the repair and proof through the evaluator and report projection. The pre-B reasoning check is pending.
- **B — PENDING.** Build is authorized for the selected correction.
- **Verification — PENDING.** Use local tests and a freshly generated saved report with an offline reader check.
- **D — PENDING.** Teach the actual repair and reasoning from before/after evidence.
- **E — PENDING.** Reconcile gaps and close after the verified result and learning review.
- **C — CONTINUOUS.** Preserve meaningful decisions, evidence and ownership progress here.

## Orientation map

**A1 — What the real case established.** The retained ApplyPilot #8 report is the original pre-fix capture, SHA-256 `c21710d1a1cda54c77781b72c5d83f0b7151e3f3991e1d2ad4cc6e3f772c1f25`. Both exact-head workflows failed. In the CI workflow, the API job's lockfile install matched runtime step 4 and failed, while its Web sibling succeeded. The workflow assessment records static consumption and the failed runtime step. The aggregate sees a successful job and emits a generic explanation that obscures both the observed failure and the supported static declaration. The prior local component check reproduced that summary with the CI workflow alone and either order of the two inputs. The original pip error is unavailable in the capture, so the exit cause is unknown. The manual Playwright constraint conflict is independently established. [Run results](evidence/2026-11-14-cross-profile-q4-applypilot/RESULTS.md)

**A2 — What we need to reason about before code.** Trace the exact attempt step through the per-workflow assessment, the aggregate CI evaluator and the ordinary report. Decide which existing evidence the aggregate can surface without promoting successful-consumption credit or claiming a failure cause. Work through an ApplyPilot-shaped regression and two controls, a genuinely successful consuming step and an unavailable correlation. Check the report as generated and after offline reopen, keeping the pre-fix capture as historical evidence. Peer-pin metadata acquisition and standalone job-fact inspection are separate responsibilities. [CI evaluator](../src/upgradepilot/ci/dependency_exercise.py#L158) · [Report projection](../src/upgradepilot/report_projection.py#L503) · [Focused CI tests](../tests/test_ci_runtime_correlated_dependency_coverage.py)

## A2 pre-B orientation

The workflow evaluator populates `runtime_consumption_reason` and `runtime_consumption_detail` before assigning its overall workflow outcome. ApplyPilot’s aggregate checks for a successful job and then relies on workflow-level reasons, so it misses the failed step preserved in those narrower fields. The report projection displays the aggregate explanation. Build will keep the repair in the evaluator and use the existing evidence to lead with the failed consuming step when supported. Controls cover a genuinely successful match and an unavailable match, with successful-consumption and maintainer-action boundaries preserved. The reasoning check asks what the summary may say when the Web job passed but the API install can no longer be matched to a runtime step.

Provenance: `UP-SKILL:upgradepilot-build-implement`, `UP-SKILL:upgradepilot-learning-by-doing`, `UP-SKILL:upgradepilot-working-memory`.
