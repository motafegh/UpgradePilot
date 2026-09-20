# F4 — CI consuming-job to Target composition (2026-09-20)

**Role:** Dated bounded Build/Implement + Learning-by-Doing record. `MEMORY.md` is the sole live-state owner. **Authorized:** Ali explicitly chose to proceed with F4 after the action-relative comparison. No maintainer-action admission, new CI command analysis, runtime install claim or external-target mutation is in scope.

## A — orientation and preflight: DONE

**Product problem:** CI already identifies the static job which consumes the changed dependency. Target interprets an entire workflow and currently insists it contain exactly one job, losing a useful existing job association in the multi-job case. `test` and `lint` are example job *names*, not new test commands or test-execution functionality. Earlier confusion was clarified before entry; detailed source/data flow may be learned during this F4 slice.

**Normal flow:** `StaticDependencyConsumptionEvidence` (`ci/consumption.py`) has `workflow_path`, `workflow_revision`, `job_key`, `source_path`, `state`. `investigation.py::_compose_target_artifact_environments` validates supported direct-requirements source/revision/path but currently drops `job_key` in deduplication and in the `interpret_target_artifact_environment(...)` call. `target/artifact_environment.py::_select_target_job` requires exactly one workflow job. Existing application regression `test_multi_job_target_ambiguity_is_preserved_despite_ci_job_relevance` establishes the conservative unresolved state for a workflow where only `test` consumes the dependency. Provider static workflow IR preserves job keys, including problem/reusable shapes; the selected job must be validated against the exact workflow definition, not inferred from a job's human-friendly name.

**Bounded outcome:** pass the already-supported CI consuming-job key (with exact source/workflow/revision association) to Target; interpret only that exact selected job, reject absent/mismatched/unsupported identity without guessing, preserve job-specific deduplication and existing direct single-job use. Keep static declaration proof static; do not infer runtime execution, exact wheel tags, installed version, compatibility, block or merge permission. A future exact target observation remains separate.

**Preflight proof:** focused Target selected-job positive/negative tests, normal application two-job positive and job-specific/mismatch negatives, existing single-job/unsupported regression, then broader deterministic suite on the exact changed revision. No green F9 CI run proves F4 changes. GitHub connector supports file-replacement writes but no patch or workflow dispatch; local container has no GitHub DNS access, so executable verification must be recorded as pending unless actual F4 tests are observed by a supported route.

## B — bounded implementation: NEXT

Make the smallest source/test changes at Target and application composition. Preserve existing meanings and stop at F4.

## C — progressive state: OPEN

Record exact commits, changed-file diff, actual tests and any proof debt; update `MEMORY.md` only for live selection or material milestone.

## D — actual-code learning: PENDING

After implementation, trace the exact job key from CI consumption through application association to Target result; distinguish declared environment from runtime compatibility; use one changed-case reasoning check if useful.

## E — closure and next step: PENDING

Repair a material misunderstanding if any; close only at achieved proof horizon, otherwise hand off concrete unfinished build/verification state. Reassess next action-specific evidence producer only after F4 is genuinely proven.
