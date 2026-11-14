# CI aggregate explanation Build cycle

**Opened:** 2026-11-14
**Scope:** Correct the ordinary CI summary after the [ApplyPilot/pyee qualification](evidence/2026-11-14-cross-profile-q4-applypilot/ANALYSIS.md#maintainer-walkthrough-and-qualification-disposition). Ali authorized the selected Build and requested progressive Learning-by-Doing. [Prior qualification cycle](2026-11-12_cross-profile_e2e_qualification_execution_lbd-cycle.md) · [Execution plan disposition](../plans/CROSS_PROFILE_REAL_PR_END_TO_END_QUALIFICATION_EXECUTION_PLAN.md#fifth-gate--practical-maintainer-task-and-qualification-disposition)

## Cycle status

- **A0 — DONE.** Fetched origin. Local and remote main agreed at `525de3b2`. The latest delta from qualification closeout records deferred peer-constraint research and changes no source or tests. Rechecked the exact saved report digest, relevant evaluator and report projection, and existing CI controls. Initialized this record.
- **A1 — DONE.** Ali identified the failed installation step as the observation the summary should preserve. Onboarding clarified that the step outcome and the cause of the pip error require different evidence.
- **A2 — DONE.** Ali explained that a missing runtime match leaves whether the install ran unknown. That distinction is part of the regression acceptance.
- **B — DONE.** The aggregate surfaces a recorded non-successful dependency step and distinguishes supported declarations from unresolved execution.
- **Verification — GREEN.** Full checkout suite 1,127 tests passed after the test-environment correction. Both retained-input report cases reopened offline.
- **D — DONE at the reviewed scope.** Before/after teaching was delivered. Ali’s A2 answer demonstrated the missing-step distinction before Build. The additional post-build ownership response was deferred at closure.
- **E — CLOSED.** Ali requested closure and continuation. See the closure rationale and next-cycle link below.
- **C — DONE.** The engineering progression, validation and remaining ownership debt are preserved.

## Orientation map

**A1 — What the real case established.** The retained ApplyPilot #8 report is the original pre-fix capture, SHA-256 `c21710d1a1cda54c77781b72c5d83f0b7151e3f3991e1d2ad4cc6e3f772c1f25`. Both exact-head workflows failed. In the CI workflow, the API job's lockfile install matched runtime step 4 and failed, while its Web sibling succeeded. The workflow assessment records static consumption and the failed runtime step. The aggregate sees a successful job and emits a generic explanation that obscures both the observed failure and the supported static declaration. The prior local component check reproduced that summary with the CI workflow alone and either order of the two inputs. The original pip error is unavailable in the capture, so the exit cause is unknown. The manual Playwright constraint conflict is independently established. [Run results](evidence/2026-11-14-cross-profile-q4-applypilot/RESULTS.md)

**A2 — What we need to reason about before code.** Trace the exact attempt step through the per-workflow assessment, the aggregate CI evaluator and the ordinary report. Decide which existing evidence the aggregate can surface without promoting successful-consumption credit or claiming a failure cause. Work through an ApplyPilot-shaped regression and two controls, a genuinely successful consuming step and an unavailable correlation. Check the report as generated and after offline reopen, keeping the pre-fix capture as historical evidence. Peer-pin metadata acquisition and standalone job-fact inspection are separate responsibilities. [CI evaluator](../src/upgradepilot/ci/dependency_exercise.py#L158) · [Report projection](../src/upgradepilot/report_projection.py#L503) · [Focused CI tests](../tests/test_ci_runtime_correlated_dependency_coverage.py)

## A2 pre-B orientation

The workflow evaluator populates `runtime_consumption_reason` and `runtime_consumption_detail` before assigning its overall workflow outcome. ApplyPilot’s aggregate checks for a successful job and then relies on workflow-level reasons, so it misses the failed step preserved in those narrower fields. The report projection displays the aggregate explanation. Build will keep the repair in the evaluator and use the existing evidence to lead with the failed consuming step when supported. Controls cover a genuinely successful match and an unavailable match, with successful-consumption and maintainer-action boundaries preserved. Ali reasoned that a missing match leaves whether the API install ran unknown even when a sibling job passed.

## Build and focused proof

The ApplyPilot-shaped regression reproduced the previous generic reason before source changes. The evaluator now surfaces the workflow's existing non-successful step observation in the top-level result. The negative job/step shape keeps its prior aggregate state with or without a successful sibling. With a declared command and missing runtime match, the aggregate keeps the declaration and explicitly leaves whether the command ran unknown. The existing positive workflow and successful matched-step precedence remains in place. No report schema change was needed.

The checkout interpreter passed 64 CI tests and 14 report tests after the source change. A network-isolated replay used the retained ApplyPilot PR/patch, attempt-scoped job records and exact workflow text as local provider inputs to the ordinary investigation and CLI projection. PyPI acquisition was stubbed to keep unrelated branches out of this CI proof. The new saved JSON reported the CI workflow's step 4 failure, unresolved successful consumption and action `abstain`. It reopened in a fresh process with the same substantive output. The original report reopened with its historical summary and the same original render digest. A counterfactual replay removed only the API job's step summaries. Its top-level view kept the declared consumption and successful job and reported that whether the declared command ran is unknown. Both final reports reopened with substantive parity. The private report SHA-256 values are `502f3074e2d50e89f88b1dad2c6103af58e4879f7d9d11b329eae18566102666` (failed-step replay) and `5480924f5a55e3845e95bef2a63b46a070a9b6de15575ab65799792366c7eaf5` (missing-step control). This is retained-input replay through checkout code, with no new live run or fresh packaged-install claim.

The first full suite completed 1,127 tests with one Workspace permission-fixture failure. The proof directory was correctly private, but the test subprocess inherited the proof shell's `umask 077`. That changed the fixture's requested mode `0755` to `0700` before the store checked it. The run under the same private umask was interrupted after the cause was identified. The final full run used the normal `022` umask inside the private output directory. The targeted Workspace suite passed 40 tests, and the final checkout suite passed **1,127 tests** in 217.652 seconds. Private full log SHA-256 `e35d54c5a6fb8123d6b4bd11b4eb51cacc6ccc47f3548dcde6215e66174d45e0`.

## D — Evidence-backed learning

The code took the route discussed in A2. Keep the workflow’s matched-step observation through aggregation, then use the ordinary projection and reader. Verification also demonstrated that preserving uncertainty matters with or without a successful sibling. The before/after pair isolates the changed evidence question by removing only the API job’s step summaries in the replay. The additional ownership check asked whether an overall API job failure can supply the missing result for the install step when step summaries are absent.

## E — Closure

Closed on November 14 at Ali's request after the implementation and full verification. The exact failed step and unknown step-execution control are independently represented in the repaired checkout replay. Ali previously identified the uncertainty correctly in A2. The additional D response remains deferred, with no post-build learner pass inferred. The conclusion to carry forward is that the overall job result gives the job outcome, while an exact step observation is needed to locate the install outcome. The pip error is separate evidence for attribution. The retained proof covers checkout code and offline reports. Independent maintainer usefulness remains unmeasured.

Continued into the [server-nexe investigation](2026-11-14_server-nexe_job-correlation_design-cycle.md), which asks whether evidence about the relevant step survives a skipped sibling job.

Provenance: `UP-SKILL:upgradepilot-build-implement`, `UP-SKILL:upgradepilot-learning-by-doing`, `UP-SKILL:upgradepilot-working-memory`.
