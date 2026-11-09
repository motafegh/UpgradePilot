# Target wheel applicability evidence qualification

Ali selected a one-case evidence qualification after the [saved-fact inspection Build](2026-11-08_saved-report-selected-facts_planning-cycle.md#build-continuation). The maintainer question is whether an exact dependency update removes a compatible published wheel for a target environment the project uses. Keep the [artifact integration plan](../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md#slice-3--target-artifact-environment-and-applicability-composition) and [evaluator](../src/upgradepilot/impact/artifact_serviceability.py) as the normal responsibility owners.

```text
A0 — DONE: reconciled main at 1dea42c5, existing target/impact owners and retained case discovery.
A1/A2 — DONE IN CONTINUOUS CONTEXT: prior onboarding and selected qualification explain exact tags, target association, and stop rules.
B — CURRENT: check OpenCV and one retained contrast, using public identity/metadata only to resolve that case.
Verification — PENDING: inspect exact boundaries and exercise existing controls.
D/E — PENDING: report disposition and re-entry condition.
C — CONTINUOUS: preserve case selection, evidence limits and results.
```

Use OpenCV as the publication-positive, target-unresolved control. Select TileDB-Py PR #2308 as the single witness-positive candidate before comparing compatibility. The [retained search](../product-simulation/2026-09-22_G4_EXACT_WHEEL_TAG_WITNESS_FEASIBILITY.md) identifies an exact-head workflow and three different matrix-job examples, making it the strongest observed installer-witness lead. Its separate historical dependency-update examples lacked the witness at their own heads. Require one exact admitted dependency change, exact old/proposed inventories, and a complete target-owned tag list tied to the same revision and applicable installer environment. Case selection does not depend on whether the comparison would report wheel loss or continuity. Stop if either required side is missing. No target execution, credentials, log-archive acquisition or product changes are part of this qualification. UP-SKILL:upgradepilot-repository-audit. UP-SKILL:upgradepilot-working-memory.

## Qualification result

- **OpenCV control.** Reopened the exact [saved report](evidence/2026-10-22-opencv-matched-report-source-capture/report.json) through the current CLI. It shows the 27 removed tags, eight added tags and available proposed source distribution. The record has no established target environment or compatible-tag set. Target applicability and the source-build outcome remain unresolved.
- **TileDB-Py contrast.** The retained note records tag counts and samples for three matrix jobs. The [exact-head workflow](https://github.com/TileDB-Inc/TileDB-Py/blob/395cbff79cb9690e5350216a4d570fad52a07671/.github/workflows/ci.yml#L69-L83) places the installer diagnostic after Python setup. The [Ubuntu job](https://github.com/TileDB-Inc/TileDB-Py/actions/runs/28433363033/job/84253268965) currently marks its logs expired. No complete tag list was found in the inspected retained inputs. The reported samples support feasibility and cannot establish absence of a compatible wheel.
- **Dependency admission.** Two bounded anonymous GitHub JSON reads returned PR metadata and all 11 changed files. Base `ea5016dc639208d54de0526c44261bbd794e288a` and head `395cbff79cb9690e5350216a4d570fad52a07671`. The [PR diff](https://github.com/TileDB-Inc/TileDB-Py/pull/2308/files) changes a NumPy test matrix and source/test code. Current `analyze_dependency_change`, run against these file records with an offline repository client, returned `no_supported_dependency_file` with zero downstream file requests. The changes therefore supply no admitted exact old-to-proposed dependency candidate for this evaluator.

## Evaluator and normal-workflow boundary

Current [artifact evaluation](../src/upgradepilot/impact/artifact_serviceability.py) checks repository and revision equality, then intersects the target's full supported tags with both published wheel inventories. A disappeared tag alone does not establish loss when a different proposed wheel still fits. The [normal orchestration](../src/upgradepilot/investigation.py) supplies the publication candidate to the evaluator without a positive exact-tag observation. Its separate static workflow-environment composition is not an installer-tag producer. This is an unimplemented evidence bridge. Neither screened case shows that admissible evidence was dropped or mishandled.

All 27 artifact and investigation tests passed, including controlled loss, replacement compatibility, missing evidence and wrong revision. The real contrast stopped before applicability evaluation. No historical data was combined across PRs or matrix rows. A source-build outcome would require its own evidence even after a wheel-loss finding.

Disposition is to defer product changes for this case. Re-enter on one exact supported update with both release inventories and a complete target-owned installer observation tied to the relevant repository, revision, matrix job and install environment. A target-produced structured artifact or a scoped retained diagnostic can qualify if it preserves that binding and completeness. This screening neither authorizes target instrumentation nor demonstrates how common such evidence is.

```text
B — DONE: screened one real contrast and preserved the stop reason.
Verification — GREEN FOR SCREENING: exact identity, admission refusal, offline baseline and 27 owner tests.
D/E — GUIDED HANDOFF: distinguish witness feasibility, applicable evidence and source-build proof. Qualification attempt closed with the positive case still missing.
C — DONE: preserved scoped observations, proof limits and re-entry condition.
```
