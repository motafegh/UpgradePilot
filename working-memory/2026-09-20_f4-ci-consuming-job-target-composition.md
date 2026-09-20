# F4 — CI consuming-job to Target composition (2026-09-20)

**Role:** Dated bounded Build/Implement + Learning-by-Doing record; `MEMORY.md` alone owns live selection. Ali authorized F4 following the action-relative comparison and chose to learn the detailed code flow at the appropriate time. No maintainer-action admission, new CI command analysis, runtime install claim, external-target mutation or unrelated feature is in scope.

## A — orientation / preflight: DONE

**Problem:** CI already establishes an exact static `job_key` for a supported job that consumes the changed dependency. The previous application called Target without this key, so Target correctly reported ambiguity for a workflow with several jobs rather than independently guessing the relevant environment. `test` and `lint` are example job IDs, not missing CI test-command analysis.

**Owned flow:** `ci/consumption.py::StaticDependencyConsumptionEvidence` provides `workflow_path`, `workflow_revision`, `job_key`, `source_path` and static `state`. Application composition binds those facts to an exact workflow definition and dependency source. `target/artifact_environment.py` interprets the selected job's *declared* environment. Identity and source-context mismatches must not silently yield Target evidence. Static declarations do not prove execution, installed version/artifact, wheel compatibility, update safety or any maintainer-action permission.

**Proof target:** selected job in a two-job normal investigation, preservation of separate supported consuming jobs, wrong/missing/reusable identity conservatism, single-job legacy behavior and full regression without changing unrelated product responsibilities.

## B — bounded implementation and test sources: DONE; executable proof pending

- Target API: `src/upgradepilot/target/artifact_environment.py` accepts optional `consuming_job_key` and selects the exact matching static job; missing key in workflow becomes `selected_target_job_not_found`, reusable/unsupported shapes remain explicit problems, and a direct caller without a key retains the one-job-only rule. Commit `a6f0ede6d89eed8d60c979f23a282e43f896819c`.
- Focused Target tests: `tests/test_target_selected_consuming_job.py`, commit `0d3f32396288a4572b4b2632d0ddc1e2e9af78ee`: positive selected job vs unrelated job, missing selected job, reusable job, empty explicit key, unchanged no-key ambiguity and no invented wheel compatibility.
- Application composition: `src/upgradepilot/investigation.py::_compose_target_artifact_environments` now requires a nonempty supported job key, binds the source repository/revision and workflow path/revision, carries the job key into Target, checks Target returns the same key, and includes job identity in result deduplication. Commit `9938f2cf8f6499cea309e32c30f9a471df611b34`. Inspected commit patch: edits confined to this composition function.
- Normal application integration test: migrated `tests/test_investigation.py` from obsolete expected two-job ambiguity to CI-identified `test` selection, including contrasting `test` (Ubuntu/Python 3.9) and `lint` (Windows/Python 3.12), while keeping artifact applicability unresolved. Commit `687c95b6face49e34190d41b9a74b93d045e019b`. Inspected patch: intended test migration plus a small unrelated whitespace-only formatting change in the `_package` helper, not a behavior change.
- Additional distinct composition tests: `tests/test_f4_target_job_composition.py`, commit `0d246f2c85980fdc9e52c4a1c6fd82ad58043d99`. Two supported consuming jobs retain distinct environments instead of being deduplicated; duplicate observations for one job remain one environment; selected missing job returns explicit problem; mismatched source revision/repository fails cross-branch binding. These focused tests exercise the composition seam with controlled CI containers; the existing `test_investigation.py` is the normal application path proof asset.

**Current claim:** source and regression-test changes are committed and reviewed at patch level. They have **not yet been executed or proven green**. No F4 non-abstention action is admitted. Do not interpret the F9 hosted green run as F4 evidence.

## C — progressive preservation and executable verification: ACTIVE

Review exact current diff and verify implementation/test syntax by executing `python -m unittest discover -s tests -p 'test_target_selected_consuming_job.py' -v`, `python -m unittest discover -s tests -p 'test_f4_target_job_composition.py' -v`, and `python -m unittest discover -s tests -p 'test_investigation.py' -v`, then broader `python -m unittest discover -s tests -v` on the **same updated revision**. The repository's `.github/workflows/product-verification.yml` is manually dispatched and includes fresh package install, CLI checks, focused investigation and complete deterministic suite; a green run must be matched to the F4 code/test SHA and its actual logs before recording hosted proof. The connected GitHub actions here do not offer a workflow-dispatch mutation; the container cannot resolve GitHub for a local clone. Until genuine executable results are available, validation is open debt, not a pass.

## D — post-implementation learning / ownership: PENDING

Trace one concrete job ID through `StaticDependencyConsumptionEvidence.job_key` → `investigation._compose_target_artifact_environments` → `interpret_target_artifact_environment(..., consuming_job_key=...)` → `TargetArtifactEnvironmentEvidence.job`. Explain job key versus human-readable job name, job-specific result identity, and proof/non-proof. Ask one changed-case question after executable results or explain honestly which parts remain unverified.

## E — gap repair / next-slice orientation: PENDING

Repair only material misunderstanding and close F4 at its observed proof horizon; otherwise retain exact remaining validation/learning debt. Do not advance to F5/F6/F7 or claim action permission without independent source-backed selection.
