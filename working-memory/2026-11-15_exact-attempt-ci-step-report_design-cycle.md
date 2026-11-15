# Exact-attempt CI step report design

2026-11-15 · [MapProxy provider-origin investigation](2026-11-15_mapproxy_provider-origin_investigation-cycle.md) · [Maintainer-task route](../plans/PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md#task-first-reassessment-after-delivered-reports)

- **A0 — DONE.** Main and origin agree at `fbb4aca3`. The selected delivery question is how to expose reported steps for the exact attempt when dependency command correlation remains unresolved.
- **A1/A2 — DONE at Planning/Design scope.** The preceding exchange already identified what GitHub exposes, distinguished job origin from matrix coordinates and step outcomes from command proof, and selected report design. Ali chose to proceed.
- **B — DONE.** Traced acquisition through the report reader and compared the current report with a selected-facts sketch from the same attempt.
- **Verification — DONE for design.** Reproduced the missing user-visible steps with the ordinary investigation and offline reader. Reconstructed the native CI values and checked the sketch's fidelity, failure wording and serialization fit.
- **D — DONE at the assistant walkthrough scope.** The report projection omits step fields the process already has. The new view can answer a question about the recorded attempt while leaving the dependency question unresolved. Independent learner ownership remains open.
- **E — CLOSED.** Wrote the Build candidate and proof obligations in the existing report plan. Independent maintainer usefulness remains unmeasured.
- **C — DONE.** Preserved the evidence, probe corrections, cost comparison and stop conditions.

The read-only product design is a direct continuation of the prior orientation, so the interactive stops are compressed. This records design consent without inferring product implementation consent or learner verification.

The orientation map is exact-attempt acquisition → native CI inputs → report projection → CLI and saved-result readers. Verify what was acquired, what is still present, and what the reader can see. Distinguish provider-declared display names and step states, missing observational evidence, and existing dependency reasoning. Use the full frozen MapProxy job list to test the proposed responsibility.

## Producer and consumer trace

1. `GitHubActionsClient.get_workflow_jobs` requests the captured attempt and binds the returned rows to the run and head. `WorkflowStep` already retains number, name, status and optional conclusion. `WorkflowJob.steps` distinguishes an unavailable list from an explicit empty list. [Provider owner](../src/upgradepilot/github/actions.py#L270)
2. `prepare_ci_evidence` supplies the paired run and jobs to the ordinary investigation as well as native CI input capture. A reconstruction of the ordinary investigation's selected in-memory native boundary recovered the complete typed pairs, including every step. That was a reconstruction check over retained material. [CI preparation](../src/upgradepilot/investigation_inputs.py#L83) · [Native CI reconstruction](../src/upgradepilot/workspace/native_projection.py#L823)
3. `_project_ci` creates a `workflow_execution` source with run identity, job names, states and step counts. It omits the individual steps from both full and CI-only reports. The default source renderer filters out job facts, and today the saved-report `--show-facts` selector refuses this source kind. The earliest missing transfer is in report projection. [Projection](../src/upgradepilot/report_projection.py#L456) · [Saved-fact renderer](../src/upgradepilot/report.py#L400)

## Frozen comparison

The checkout's ordinary investigation ran in an isolated network namespace on hash-checked MapProxy #1559 PR, changed files, run, jobs and workflow captures. The unrelated package provider returned a controlled unavailable result. The native reconstruction recovered eight jobs and 79 steps for run `43457921398`, attempt 1. The actual CI assessment remained `supported_not_correlated` and its workflow correlation reason remained `static_job_strategy_unsupported`. The baseline saved report encoded, decoded and reopened through the CLI in a separate process. It contained the eight job names and step counts. The default output hid all four matrix display names, and `--show-facts` for the attempt source returned exit 7. The CI-only projection also hid those names. [S018 case](../product-simulation/scenarios/S018-mapproxy-soupsieve-matrix-coverage/README.md)

The private design sketch grouped the same 79 step rows by all eight numeric job IDs. Each `test (3.12, 13.0.0)` through `test (3.15, 13.0.0)` displayed successful steps 6 and 7. `coverage` also displayed successful steps 6 and 7, and `lint` and `typechecking` displayed successful step 4. ApplyPilot's exact run `43073710410`, attempt 1, job `130708096164` rendered its recorded API install step 4 as failed. Removing its step list in a control resulted in unavailable step details. Additional sketch controls distinguished unavailable and empty lists, an absent selected step, and a pending step with no conclusion. The untrusted multiline-name control stayed within one display row. [ApplyPilot retained outcome](2026-11-14_ci-aggregate-explanation_build-cycle.md#build-and-focused-proof)

The additional draft facts added 5,275 serialized bytes and decoded under the existing report schema with identical assessment and action records. A size-only synthetic batch of 1,000 job blocks of comparable detail added 685,893 bytes. Those measurements justify an initial small shared detail budget and attempt-level completeness checks instead of an unbounded dump. Private comparison receipt SHA-256 `fdd9620a1927b1940ce50b605e99e92bf61be6404cc68356b60b8be07927eee1`. The first harness lacked the capability-bound provider member and then read the wrong native projection attribute. The corrected harness binds a fail-fast provider stub and reads `workflow_inputs`. The draft remained a private diagnostic using the existing schema, outside the product renderer and projector.

## Decision

| Alternative | Maintainer task and trade-off |
| --- | --- |
| Expose the existing job facts as-is | Identifies variants and outcomes at job level. A step count still leaves the install and test outcomes unavailable. |
| Put all step rows in the default report | Answers the step question immediately in MapProxy. Seventy-nine additional rows obscure the default review, and larger captured attempts amplify the cost. Guessing a subset from step names would silently omit arbitrary workflow steps. |
| Extend the attempt source and existing saved-facts inspection | Answers the task by following the exact attempt's cue to grouped step details. Reuses the existing source, offline reader and recorded identity. The reader saves a report and uses one extra command to see details. |
| Extend correlation or consume the visualization graph | Could address YAML origin and command evidence with additional qualification. The whole-matrix coordinate and multiline command gaps remain, and the task about reported steps already has a typed producer. |

Choose the exact-attempt source and saved-facts view for a bounded Build candidate. Use whole attempts within a 128 KiB report-wide ceiling for the additional optional detail, with explicit omissions. The target is all four displayed variants in the frozen case, exact provenance and failure/unknown fidelity with zero added requests. Reassess if the result does not let a maintainer answer the scoped task with one source inspection. Evidence from a later Build must cover the ordinary save/reopen route, legacy input, budget exhaustion and public report correctness. It cannot establish separate package execution or semantic usefulness by itself.

The [report plan](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#inspect-github-reported-steps-from-an-exact-attempt) owns the proposed scope and proof. [Live selection](../MEMORY.md) remains separate. No source or product test files changed.

Provenance: `UP-SKILL:upgradepilot-planning-design`, `UP-SKILL:upgradepilot-learning-by-doing`, `UP-SKILL:upgradepilot-working-memory`.
