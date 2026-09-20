# Action-relative producer/reachability comparison — 2026-09-20

**Role:** Dated analysis/design and Learning-by-Doing record for the selected responsibility after closed F3/F9/F11. `MEMORY.md` alone owns live selection. The comparison does not authorize source/test Build, alter accepted action semantics, or make a non-abstention action currently reachable.

## A — orientation: DONE

Ali requested immediate continuation with canonical A → B → C → D → E and progressive preservation. The comparison distinguished **positive action permission** (what evidence is required) from **normal producer reachability** (what the application really establishes). Current action semantics come from `docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md`; current `src/upgradepilot/maintainer_action.py` remains abstention-only. Historical September 11 reachability notes were treated as questions, not current source truth.

**Initial main revision before this record:** `e2cf430b54be64e077f0ff2e8faa2409fce22398`. No product source, tests, stable specifications or execution plans were edited in this comparison.

## B — action-relative comparison: DONE (analysis, not new runtime proof)

| Action and existing case pressure | Positive requirement and normal-path gap | Why not first |
| --- | --- | --- |
| `merge after normal review` (S004/S005/S009/S010) | Positive bounded candidate/repository-context discovery and closure, beyond merely no detected problem. | F7 requires a separately justified coverage horizon and multiple independent premises. |
| `run targeted checks` (S006) | Exact unresolved material proposition, a concrete discriminating maintainer check with meaningful outcomes, and no better admitted UpgradePilot-owned investigation. Python's current selector chooses a product-owned read-only source acquisition, **not** a maintainer check. | No such general check is yet produced on the normal Python/artifact path. F4 may supply target-context identity, but it does not authorize a check. |
| `investigate` (Cactus #198 screening) | Grounded material concern, concrete broader/adaptive inquiry and stopping/pruning, no independent current block. | Current normal producer does not derive that broader inquiry; no reason to add a generic planner before needed evidence. |
| `block` (S003 mechanism-specific pressure) | Exact proposal-level hold, sufficient proof. Python-support declared hold needs affected supported-environment obligation and dependency required there, not mere `requires-python` overlap. Wheel-path loss with possible source fallback is not installation failure. | S003's TypeScript/npm result is not proof of a current Python normal-path block. F4 does not unlock block. |
| `defer` (S012) | Specific useful outside/future responsibility and concrete re-entry trigger; missing capability alone is insufficient. | Current path does not normally establish this obligation. |

**F4 selected over F5/F6/F7 as one bounded next composition repair:** `src/upgradepilot/ci/consumption.py::StaticDependencyConsumptionEvidence` preserves exact `workflow_path`, `workflow_revision`, `source_path` and `job_key`. `src/upgradepilot/investigation.py::_compose_target_artifact_environments` currently drops `job_key` from its deduplication identity and does not pass it into `target.artifact_environment::interpret_target_artifact_environment`. Target then requires `len(definition.jobs) == 1`; a real two-job workflow can have one exact consuming job and still produce `ambiguous_target_job_selection`. `tests/test_investigation.py::test_multi_job_target_ambiguity_is_preserved_despite_ci_job_relevance` protects this current conservative state. Preserve that existing test as a regression target to update after the admitted behavior changes.

**F5** exact target wheel tags still need target-owned observation; runner/Python labels are insufficient. **F6** exact resolved runtime package/artifact is needed only for a selected proposition; a correlated successful CI step does not establish it. **F7** favorable bounded discovery/context horizon remains larger and separately justified. F4 alone will not produce wheel compatibility, runtime version, safety, or a new action.

**Selected F4 entry contract:** exact workflow/revision/dependency-source identity + supported consumption `job_key` must reach Target. Keep dedup job-specific; reject absent/ambiguous/unsupported/mismatched job identities; preserve legacy direct single-job callers unless a better admitted contract is proved. Prove the normal application positive two-job path, negative identity and unsupported paths, and unchanged declared-only strength. Do not broaden matrix/reusable workflow semantics or install-version interpretation.

## C — progressive preservation: DONE for comparison

The comparison was committed to `main` with `MEMORY.md` as its sole live-state owner. No product changes or new tests were performed for this comparison. This final status entry records the learner handoff; F4 must use a separate dated working memory and normal Build proof route.

## D — practical ownership explanation: DONE at bounded conceptual depth

Ali initially understood "test" as a new test-command-analysis capability. We corrected that: `test` was only the *example name* of a job CI already inspected and identified as consuming the changed dependency. Target currently sees two jobs and returns ambiguity, not an incorrect positive for the unrelated `lint` job. F4 passes the **existing** relevant job association across the composition boundary. Ali subsequently restated the intended use of the CI-identified test job to find the Target environment and explicitly elected to proceed to F4, learning deeper code details during implementation. This shows bounded conceptual orientation, not independent mastery of the code or proof boundary.

## E — handoff: DONE

Comparison closed at its analysis/selection/teaching horizon. Ali authorized proceeding with F4 on 2026-09-20. New F4 Build slice owns exact source/test inspection, design of selected-job binding, implementation, verification and its separate D/E learning check. No non-abstention maintainer action is authorized by this handoff.
