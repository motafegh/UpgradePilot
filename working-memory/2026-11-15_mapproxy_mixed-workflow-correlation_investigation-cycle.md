# MapProxy mixed-workflow correlation investigation

**Evidence date:** 2026-11-15
**Decision:** Determine whether correlating an ordinary job next to a matrix can deliver useful evidence under existing command-execution rules. [S018 case](../product-simulation/scenarios/S018-mapproxy-soupsieve-matrix-coverage/README.md) · [Maintainer-task decision](../plans/PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md#task-first-reassessment-after-delivered-reports)

## Cycle status

- **A0 — DONE.** Local and remote main matched at `b8b9ccaa`. Checked server-nexe closeout, S018 retained inputs and the active correlation and command-execution owners.
- **A1/A2 — DONE at the engineering orientation scope.** The previous turn presented the step-versus-command distinction and the proposed offline comparison before Ali asked to proceed.
- **B — DONE.** Reviewed the whole attempt and isolated the ordinary job, step and command decisions with retained evidence.
- **Verification — DONE for the diagnostic.** Current CI result and component controls reproduced in a network-isolated checkout process, using five input digests from the public manifest.
- **D — DONE at the result walkthrough scope.** Ownership response deferred. The coverage job and the lint/typechecking jobs illustrate different remaining proof gaps.
- **E — CLOSED.** Select the ordinary-job identity design checkpoint. No product Build proposition is qualified yet.
- **C — DONE.** Retained the diagnostic, limits and handoff in this record.

### Scope and phase adaptation

The planned comparison was presented before the instruction to proceed. This is a read-only discriminating check on retained evidence with no product or external action. Separate A1/A2 stops would have repeated that orientation and delayed the check, so both were compressed for this diagnostic. Independent learner understanding is unassessed. A successor implementation must establish provider identity, ambiguity refusal and compatible report and recovery boundaries.

## Observations and controls

| Path | Result and scope |
| --- | --- |
| Existing product CI assessment | `supported_not_correlated / static_job_strategy_unsupported` on the eight-job frozen attempt `43457921398`, attempt 1. The CI-only view preserves this answer. |
| Ordinary coverage job `131996881258` | Its YAML key is `coverage` with no explicit display name. Given the candidate job association, the production step matcher links the install script to successful step 6 and tests to successful step 7. The inner `pip install -r requirements-tests.txt` remains unresolved under `runtime_strengthening_positive_structure_not_established`. |
| Ordinary lint `131996881382` and typechecking `131996881059` | Both declare the changed requirements install as a sole command. GitHub recorded their Install requirements step 4 succeeding. Given each candidate job association, the existing command-execution evaluator returns `exact_command_execution_supported`. Full-workflow production results remain unresolved. |
| Missing or repeated evidence | Removing the coverage install summary gives `runtime_step_match_missing`. Repeating its display name with distinct ordered step numbers gives `runtime_step_match_ambiguous`. The lint name was unique in the frozen job list. Missing and duplicated names give zero and two candidates. A substituted runtime row can still look unique by name, so uniqueness needs an independent origin rule. |

The first inspection expected all candidates to share the multiline problem. The static evaluator showed the separate lint and typechecking candidates. The first private probe also assumed a shared display label and stopped; the corrected diagnostic used each source step index and its matched runtime step. The final private receipt SHA-256 is `5ff30bc0668d8e692e15d84cac712718a78fc61447e12ddb1178e364782a0e8e`. This was a component check with assumed identities supplied explicitly and an actual current CI-only projection. It was neither fresh acquisition nor an end-to-end product result for the proposed behavior.

## Disposition and next proof

Prioritize an **ordinary-job identity design for mixed workflows**. If the design can establish the lint/typechecking associations, the current execution owner can tell a maintainer that those install commands ran successfully. This is a smaller improvement than general matrix expansion or multiline execution analysis. It leaves the matrix test observations and the coverage script's inner command separately bounded. The retained provider job shape exposes a display name and numeric ID, but did not supply a separate YAML job key. The current ordinary matcher also requires an explicit static name.

First establish a provider-backed default-name rule for ordinary jobs and a reliable way to exclude competing origins from matrix, dynamic or reusable jobs. Check complete attempt acquisition and reject an unmatched, duplicated or conflicting origin, including an unsupported sibling whose possible name cannot be ruled out. Prove missing and ambiguous steps still fail closed. If no such identity rule can be admitted, retain the case's output and stop at the missing association. Compare the proposed consumer view with the current CI-only view for a real maintainer task. A later Build would need to retain job origins, identify unsupported siblings in the report and preserve offline recovery without recomputation.

The supported proposition would be successful consumption in the explicitly identified jobs. Actual installed or imported Soup Sieve, selector exercise, compatibility, non-abstention permission and independent usefulness remain open. General matrix expansion and command-position semantics have distinct proof obligations.

Provenance: `UP-SKILL:upgradepilot-planning-design`, `UP-SKILL:upgradepilot-learning-by-doing`, `UP-SKILL:upgradepilot-working-memory`.
