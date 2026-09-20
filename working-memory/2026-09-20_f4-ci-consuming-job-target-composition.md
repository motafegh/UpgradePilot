# F4 — CI consuming-job to Target composition (2026-09-20)

**Role:** Dated bounded Build/Implement + Learning-by-Doing record. `MEMORY.md` is the sole live-state owner. **Authorized:** Ali explicitly chose to proceed with F4 after the action-relative comparison. No maintainer-action admission, new CI command analysis, runtime install claim or external-target mutation is in scope.

## A — orientation and preflight: DONE

**Product problem:** CI already identifies the static job which consumes the changed dependency. Target currently interprets an entire workflow and insists it contain exactly one job; in a two-job workflow it loses the available job selection and safely reports ambiguity. `test` and `lint` are example job *names*, not new test commands or test-execution functionality. Ali clarified this distinction and chose to learn deeper code flow during the build.

**Normal flow:** `StaticDependencyConsumptionEvidence` (`ci/consumption.py`) has `workflow_path`, `workflow_revision`, `job_key`, `source_path`, `state`. `investigation.py::_compose_target_artifact_environments` validates supported direct-requirements source/revision/path but drops `job_key` in deduplication and in the `interpret_target_artifact_environment(...)` call. The existing application regression `test_multi_job_target_ambiguity_is_preserved_despite_ci_job_relevance` establishes the current conservative unresolved state. The provider static workflow IR preserves job keys; Target must never guess a job or use its human-friendly display name as identity.

**Bounded outcome:** carry exact workflow/revision/source + already-supported CI consuming-job key to Target; interpret that job alone; refuse missing/mismatched/unsupported identity; keep deduplication job-specific and preserve single-job direct callers. Static declaration evidence is not runtime execution, wheel tags, installed version, compatibility or permission to merge/block.

## B — implementation: PARTIAL (Target API only; normal application integration still pending)

**Committed:** `src/upgradepilot/target/artifact_environment.py` now accepts optional `consuming_job_key`, selects the exact matching static workflow job, rejects an absent selected job with `selected_target_job_not_found`, preserves unsupported/reusable-job problems, and retains the old one-job-only behavior for callers that do not supply a key. Commit `a6f0ede6d89eed8d60c979f23a282e43f896819c`.

**Focused test source committed:** `tests/test_target_selected_consuming_job.py` covers positive two-job selected `test` versus unrelated `lint`, missing selected key, selected reusable job, and empty key; also checks unchanged direct-call ambiguity and exact-wheel-compatibility remaining unresolved. Commit `0d3f32396288a4572b4b2632d0ddc1e2e9af78ee`.

**NOT YET IMPLEMENTED:** `src/upgradepilot/investigation.py::_compose_target_artifact_environments` must pass `consumption.job_key`, preserve that key in the deduplication relation, check exact definition/dependency-source repository and revision coherence, and ensure the selected Target result refers to the same job. Update existing `tests/test_investigation.py::test_multi_job_target_ambiguity_is_preserved_despite_ci_job_relevance` to prove the now-expected positive result; add only distinct missing/identity and two-consuming-job normal-path integration cases. Do not leave the old test asserting ambiguity when the normal application behavior changes. No new action or wheel evidence is authorized by this work.

## C — preservation and proof: PARTIAL

GitHub compare `a27067e208a49c8eda5238e3784a2aedc0cf0777..0d3f32396288a4572b4b2632d0ddc1e2e9af78ee` shows only the Target source, one new focused test file, the closed comparison working memory and this F4 working memory. **No F4 tests or broad regression have been executed.** Local clone remains unavailable because the container cannot resolve `github.com`; GitHub connector supports full-file replacements but no text-patch action or workflow dispatch. Do not infer test pass from code review or historical F9 CI. F4 remains open pending normal-path integration, focused and wider test results and D/E.

## D — actual-code learning: PENDING

After full normal application implementation, trace the exact job key from CI consumption through application association into Target result; distinguish job declaration facts from actual installed package/runtime compatibility; offer one changed-case reasoning exercise after showing the actual code.

## E — closure and next step: PENDING

Repair material understanding gaps and close only at observed F4 proof horizon; do not move to another product responsibility or claim an action became reachable while normal integration/proof is missing.
