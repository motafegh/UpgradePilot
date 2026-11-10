# OmniMatch CI report evidence trace

Ali selected the follow-up to the [cross-case qualification](2026-11-09_targeted-check_cross-case-qualification_cycle.md#distinct-positive-check-candidate-on-omnimatch) and asked for progressive recording and teaching. Reconciled main and origin/main at `8983b089`. The current question is where the literal old pin goes from workflow acquisition to the maintainer report. Use the [maintainer utility plan](../plans/PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md#task-first-reassessment-after-delivered-reports). Use the prior explanation and Ali's continuation as the orientation for this read-only diagnostic. A substantive design or repair would be a separate responsibility.

UP-SKILL:upgradepilot-repository-audit. UP-SKILL:upgradepilot-working-memory. UP-SKILL:upgradepilot-learning-by-doing.

## Proof route

Freeze OmniMatch PR 20 to base `db5576e5b38053a7b46d89ff51e1175eb61ab9c2` and head `22fc7709642599feca7b9527fe4f44874d04e520`. Try one bounded anonymous dependency/CI Workspace preparation through shared product owners. Trace workflow acquisition, static interpretation, capture, cold reconstruction, and the report mapping used by both product views. Keep a raw command, a structured fact about that command, and actual package identity in pytest separate. Preserve a provider stop if encountered. No target execution or product changes.

## Live acquisition and rendered result

The guarded anonymous attempt made 13 GitHub API GETs, all HTTP 200. The earlier 403 remains part of the previous attempt's history. The [rendered CI view](evidence/2026-11-10-omnimatch-ci-report-trace/ci-view.txt) is 9,195 bytes with SHA-256 `b427848aeae6c4707e78c3fb9af562ad4865070ff06d644037ff4f4a9345ab8a`. It is the direct product renderer output from a model-free Workspace, with the diagnostic request and inspection lines removed.

| Exact-head PR run | Attempt | Acquired jobs |
| --- | --- | --- |
| 42574105663, Code security analysis | 1 | JavaScript/TypeScript and Python jobs successful |
| 42574105536, Backend verification | 1 | `signatures` successful |
| 42574105631, Real local transformer verification | 1 | `cpu-models` successful |

The two latter workflow definitions contain the literal `httpx==0.27.0` in their install commands. The admitted dependency result remains HTTPX 0.27.0 → 0.28.1 in `backend/requirements.txt`. The report shows the old version in that identity section, but does not connect it to either green workflow. It prints `dependency_consumption_not_established` for aggregate coverage and `no_admitted_runtime_dependency_state_candidate` for runtime state. Both workflow files appear as exact-revision references. The acquired run/job/step metadata does not attest the package loaded inside the named pytest test. This attempt did not read logs, artifacts, or external test reports.

## Where the explanation stops

1. **Acquisition and native capture.** [`prepare_ci_evidence`](../src/upgradepilot/investigation_inputs.py#L83) reads attempt-bound jobs and exact-head workflow definitions. [`capture_ci`](../src/upgradepilot/workspace/native_capture.py#L150) records both the inputs and producer results. The [codec](../src/upgradepilot/ci/native_codec.py#L690) retains the workflow definition in the input. [Reconstruction](../src/upgradepilot/workspace/native_projection.py#L664) decodes it and validates run/job/head and definition scope. The old pin is still available in the workflow text at this boundary.
2. **Static CI analysis.** [`_inspect_steps_job_evidence`](../src/upgradepilot/ci/workflow_commands.py#L323) analyzes a run step and derives the supported consumption and invocation families. For direct requirements it asks whether the command consumes the changed file. The inline old pin does not establish that relationship. Both old-pin jobs therefore correctly lack a consumption fact. This owner emits no separate package/version request fact for these commands.
3. **Report projection.** [`_project_ci`](../src/upgradepilot/report_projection.py#L450) receives workflow execution records and producer results. It builds a source link and projects command text for admitted consumption or runtime assessment records. The full and partial reports share this mapping. Since no structured fact about the inline old pin enters those results, the renderer has no such fact to display. The report alone preserves the workflow link as reference only. The original definition remains available in the native CI input.

This is a confirmed explanatory gap for the selected case, with an accurate coverage classification. The workflow text survives acquisition and reconstruction. The missing piece is a structured declaration in the CI analysis result. The useful general distinction is between a package version **requested by a command**, what actually **completed in a job**, and a version **loaded in the named test process**. A future declarative fact should carry exact workflow, job, step, command location, package and requested version, with any limitations explicit. Compare a focused inspection surface against a concise report explanation before choosing how much to expose. Derive the fact at a CI analysis boundary if justified, then project it without upgrading the meaning to installed or tested. The proposed-version OmniMatch observation remains independently open.

The probe used the product's model-free preparation and native decode/reconstruction in process. It did not open a persisted checkpoint in a new process or produce a full investigation report. The full report's CI mapping was verified by source inspection. The saved report is the exact partial view of recorded CI evidence.

## Verification and handoff

The exact rendered view was checked for both workflow locators, the unresolved reason and absence of a workflow-linked old-pin command. Ninety-eight focused tests passed across CI coverage and state, parser-backed command evidence, normal orchestration, native reconstruction and report delivery. Governance doctor passed. The product code and test suite were unchanged. The next design decision is whether a workflow-scoped requested-version fact would improve the normal maintainer view or whether bounded source inspection is sufficient. Runtime-State Cycle 2 and automated action output remain separate.

```text
A0/A1/A2 — Reconciled current main and carried forward the prior explanation and selected diagnostic.
B — Acquired exact provider inputs and traced native capture, reconstruction, and report output.
Verification — Three runs and both old-pin definitions retained, rendered report compared, 98 focused tests passed.
D/E — Identify structured interpretation as the earliest missing fact. Separate static declaration from runtime evidence.
C — Acquisition, report, trace, limits, verification, and design handoff preserved.
```
