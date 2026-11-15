# MapProxy GitHub job-origin investigation

2026-11-15 · [Previous design diagnostic](2026-11-15_mapproxy_job-and-matrix-identity_design-cycle.md) · [S018 evidence](../product-simulation/scenarios/S018-mapproxy-soupsieve-matrix-coverage/README.md)

## Cycle status

- **A0 — DONE.** Local and remote main agreed at `44736fcb`. Reopened the selected continuation, the mixed-workflow design result and S018's exact saved workflow and jobs.
- **A1/A2 — DONE for the provider check.** The preceding discussion distinguished the existing YAML-to-run bridge, the narrower ordinary-job route and the requested coverage of all four combinations. Ali then authorized the exact-attempt follow-up.
- **B — DONE.** Read the exact-attempt GitHub jobs and checks records, visualization and matrix fragment. Reconciled them with the frozen case.
- **Verification — DONE.** The map covers eight of eight job IDs. Eight synthetic inconsistencies were rejected. A coherent substitution of matrix display fields survived and establishes the remaining proof limit.
- **D — DONE for the assistant walkthrough.** The verification distinguishes YAML job origin, displayed combination, observed step outcome and package state. Ali's independent ownership response remains open.
- **E — CLOSED.** Preserved the evidence and report design decision. Provider markup remains a qualification candidate.
- **C — DONE.** Retained the initial failures, successful graph expansion, identity check, negative controls and proof boundary.

The interactive stops were compressed for this read-only follow-up. The prior orientation already posed this exact evidence question, and Ali chose to proceed after challenging the narrower ordinary-only scope. The result carries no independent learner verification or Build authorization.

The orientation map was to rebind repository, head, workflow, run and attempt first, then inspect which provider fields tie a numeric ID to YAML origin and matrix values. Missing, competing or display-only matches preserve uncertainty at their respective claim level.

## Evidence from the exact attempt

The live attempt was `mapproxy/mapproxy`, PR #1559, head `ac01b8901935bfc16a0195277b4aec1c43275897`, event `pull_request`, `.github/workflows/test.yml`, run `43457921398`, attempt 1, check suite `117676308842`. The attempt referenced no reusable workflows. The exact-attempt REST jobs body was byte-identical to the frozen S018 body. The pinned YAML and frozen jobs matched the S018 manifest hashes. [Exact attempt visualization](https://github.com/mapproxy/mapproxy/actions/runs/43457921398/attempts/1) · [Exact-attempt jobs API](https://docs.github.com/en/rest/actions/workflow-jobs#list-jobs-for-a-workflow-run-attempt)

The run graph contains a structural YAML key on each ordinary job element and a link with its numeric job ID. The collapsed `test` group exposes its attempt-scoped expansion URL. A direct GET of that fragment returned HTTP 404. The same route with GitHub's page-request headers returned HTTP 200 and four children under that group. Each child exposes the structural YAML key `test`, a same-run numerical job link and an opaque external ID. All eight job links and external IDs matched their exact-attempt REST job and corresponding GitHub Actions check records. The graph and fragment both bind to attempt 1. GitHub documents the graph as a human interface. Its markup and fragment request shape have no machine contract in the documentation reviewed. [Visualization graph](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-the-visualization-graph) · [Check runs API](https://docs.github.com/en/rest/checks/runs#get-a-check-run)

| YAML key in graph | GitHub job ID | GitHub job display name | Selected reported step outcomes |
| --- | ---: | --- | --- |
| `coverage` | 131996881258 | coverage | 6 and 7 successful |
| `doc` | 131996881440 | doc | Outside this case's install/test readout |
| `lint` | 131996881382 | lint | 4 successful |
| `typechecking` | 131996881059 | typechecking | 4 successful |
| `test` | 131996881880 | test (3.12, 13.0.0) | 6 and 7 successful |
| `test` | 131996881564 | test (3.13, 13.0.0) | 6 and 7 successful |
| `test` | 131996881411 | test (3.14, 13.0.0) | 6 and 7 successful |
| `test` | 131996881633 | test (3.15, 13.0.0) | 6 and 7 successful |

The frozen YAML declares four Python values and a singleton Pillow value of `13.0.0`. The latter is consequently a fixed **declared input** for this matrix. The expanded graph, job and check records each show matching combination labels. The step 5 labels also agree with each displayed Python value. No separate per-child coordinate field was found in these responses. The graph establishes **which YAML job owns each ID** here. A separately evidenced **assignment of a specific Python coordinate to an ID**, and observation of a running Python or installed Pillow version, remain open. [Matrix definition and expansion](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations#adding-a-matrix-strategy-to-your-workflow-job) · [Runner contexts](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts)

The public log attempts remain visible in the receipt. Two job-log requests returned HTTP 403. The selected public step fragment returned HTTP 404, as in the earlier capture. The run-level artifact inventory listed a single artifact named `coverage-report` with no job-level coordinate metadata. Its content was outside this check and was left unopened. [Artifact inventory API](https://docs.github.com/en/rest/actions/artifacts#list-workflow-run-artifacts)

## Verification and decision

The offline diagnostic checked hashes, exact attempt and workflow scope, complete ID sets, graph parent and child relationships, matching check suite and external IDs, and the observed step results. It refused a missing row, duplicate row, different fragment attempt, different run link, mismatched external ID, mismatched YAML key, mismatched matrix parent, and a REST-only exchange of two matrix names and step lists. When the same substitution was applied coherently to the graph and Checks display labels as well, the diagnostics still accepted the swapped labels. The numeric IDs remained under `test`. This synthetic result shows why additional copies of the display fields corroborate the provider's display but cannot independently attest the axes. No provider data mix-up was observed.

Private raw bodies, fetch manifests, offline diagnostic and structured receipt are in the local UpgradePilot evidence store. Key hashes are `cb2b1361da178a44936bf731476a4a4aacdc0f53eb515885fc64574da3b33c8b` for exact-attempt jobs, `204942f5223b8d88840e3157061c3a36381bd415422263cea456c0d7929319b1` for the graph page, `465e29607af5c217fd8833e48e62ec2171956c037caf731733fe0eb1b7344722` for the expanded fragment, and `4651c7b2b49e0b0a13ed2b49c45ec3f3f1a801728e6ce5919bba2a6812b46d6a` for the verification receipt.

The next responsibility is report design for **GitHub-reported steps from an exact attempt**. Start with the existing attempt-scoped job records. Show all four reported matrix labels and the selected install and test step outcomes against the current unresolved baseline. Preserve missing and failed outcomes, distinguish display labels from YAML-correlated execution, and check that a maintainer can answer which jobs GitHub reported as reaching which steps. The report design can be evaluated without making HTML a product dependency. A later decision to consume the graph for ordinary-job or job-group origin would need evidence of acquisition and parser stability, rerun and partial-response controls, and a saved-report recovery path. Matrix coordinate attestation would still require a suitable source.

The ordinary `lint` and `typechecking` single-command installs remain correlation candidates given admitted job origin. The successful matrix and coverage step 6 summaries do not give separate command proof for their embedded `pip install -r requirements-tests.txt`. Installed Soup Sieve version, import, test-path exercise, compatibility and upgrade advice remain outside the evidence. Product source and tests were untouched, and no workflow was rerun.

Provenance: `UP-SKILL:upgradepilot-planning-design`, `UP-SKILL:upgradepilot-learning-by-doing`, `UP-SKILL:upgradepilot-working-memory`.
