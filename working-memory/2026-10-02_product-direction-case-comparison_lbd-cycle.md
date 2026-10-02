# Product Direction Case Comparison — LbD Cycle

Date: 2026-10-02 (Asia/Tehran).
Primary operation: Planning/Design investigation.
Plan: [Product direction and maintainer utility](../plans/PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md).
Previous: [Planning preparation](2026-10-02_product-direction-and-report-planning.md).
Procedures: UP-SKILL:upgradepilot-planning-design; UP-SKILL:upgradepilot-working-memory.

## Authorization and progression

Ali explicitly requested the next step after discussing that no additional plan is necessary. Authorized responsibility: execute the prepared comparison and reconcile its direction decision; product implementation remains separate. Standing authorization covers coherent validated commits/pushes.

A0 — DONE: fetched origin/main, reconciled plan/live handoff, current source and selected case records; initialized this cycle and learning map.
A1 — DONE for the continuity opportunity: Ali challenged the unclear explanation; research integration was reconciled and the product/worked-example distinction re-explained concretely. Detailed mastery remains unassessed.
A2 — CURRENT: case walkthrough explains the upcoming comparison; pre-B understanding remains unassessed.
B — PENDING: no alternative has been evaluated or selected in this cycle.
Verification gate — PENDING: comparison traceability, common rubric, counterevidence and owner reconciliation not yet established.
D — PENDING: evidence-backed learning after the comparison.
E — PENDING: ownership gaps and closure.
C — CONTINUOUS: initialization and evidence distinctions preserved here.

## A0 reconciliation

Starting head: f5ec89034e97aa8ed6ba44f5e8300b6bc8d0bf8c; clean main. Fetch found no remote commits ahead. The three latest commits publish review evidence, prepared plans and the inspectable rubric. They do not implement a new product direction. Executable paths src/, tests/, experiments/ and pyproject.toml remain unchanged from 860f1e36; prior test results remain dated proof and were not rerun for orientation.

Current source inspection confirms maintainer_action.py admits only explained abstention; cli.py calls the investigation and does not import/call action synthesis or project runtime_dependency_state_result. investigation.py includes runtime-state composition. This is the present delivery boundary, not permanent retention/scope authority. Do not confuse normally available typed evidence with a field actually delivered to the CLI user.

Selected case inputs for orientation, not evaluation results:

| Case | Exact identity / input | Proof class and pressure |
| --- | --- | --- |
| S001 Pydantic/Soup Sieve | Preserved 2026-10-02 [CLI log](evidence/2026-10-02-unbounded-review/live-s001-cli.log); head aa2dc024d33f61cdef50bf1973ab5adf0a974f5a | Ordinary live acquisition recorded earlier: semantic-provider failure with unresolved output; no successful model-quality or merge proof |
| S002 HTTPX | [Retrospective case](../product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md); head 391508134b083b8f54461c0b576e8f7985c6ecb4; run s002-retrofit-2026-07-22-r1 | Manual curated reconstruction: Docker workflow versus Python test coverage; historical resolver state unavailable; external behavioral confirmation absent |
| S008 CARLA/OpenCV | [Frozen case identity](../product-simulation/scenarios/S008-carla-opencv-python36-artifact-fallback/artifacts/CASE_IDENTITY.json); base 7758d066080f180f8296887ed89b7c723a54706a; head f32ad2d23a9abee47c566dfbed2b822d953a09e2 | Manual bounded artifact analysis: missing CPython-3.6 binary path with source fallback; source-build success/failure and maintainer action unproven |

Input SHA256 anchors: S001 log 7f921ffddb5f4b29f7f5c10a7891f20102db6acc771a976612bb070bfb8627aa; S002 RUN_MANIFEST.json 39c7d83ba90ad7945f9ccbd5a30d1918523662745a89b6a0de7db78b79ab1459; S008 CASE_IDENTITY.json 7c322afb141145d6941b980ee43e05a663454cc42dcd5127d86f52659ab8da94. These bind the inspected local records, not fresh external acquisition or full-bundle validation.

## Living A-phase learning map

### A1 correction after research integration and explicit understanding gap

Ali reported merging the real-case research and said the earlier question was not understandable. The explanation used normal-producer/action-permission terminology before establishing a concrete example; this is an orientation gap, not a failed learner assessment. No A1/A2 understanding or comparison result is inferred.

Fetched and fast-forwarded clean main from 2440ba92 to fe135063. PR #34 preserves the complete 61-commit simulation-research history through dd974c95; S013–S016 and their research handoffs are now local on main. The imported delta has 45 changed files and no src/, tests/, experiments/ or pyproject.toml changes. The direction plan and MEMORY.md already acknowledge integration; preserve that reconciliation. The dated September handoff's original not-merged label is historical, not the current integration state.

Simpler teaching model: a real-case investigation is a worked example of what useful assistance could discover; product source is the reusable program that must acquire and reason about the evidence when given a PR. Merging the worked examples supplies the project with those records, while this merge did not add their reasoning to product code. The HTTPX packet records that Docker succeeded but relevant Python tests did not run; its proposed follow-up was to capture resolved versions and run those tests. Comparison must distinguish presenting that archived finding from automatically establishing it for a new PR. Both are valuable evidence, but establish different capabilities.

Refine A1/A2 to explain product versus research through this example before using producer reachability or action-permission vocabulary. Retain S013–S016 as available further controls where they materially discriminate a delivery choice; do not add cases merely to increase the matrix size. Reconciliation and explanation are this increment; comparative judgments remain pending.

A1 bridge: prepared plans are execution coordination; source still has bounded findings and abstention. Preserved ordinary CLI evidence and richer manual packets establish different claims. Main ownership target: distinguish a useful manual insight from an insight the normal product can produce.

A2 topics: compare the three delivery sequences with the same nine rubric dimensions; trace each proposed useful output through normal producers; label unavailable evidence and untested utility; preserve adverse cases rather than average labels. Expected result is a justified trial or one practical discriminating check. This will not establish independent usefulness, expand action permissions or implement a report.

Meaningful unresolved states: a curated conclusion may require an absent producer; honest output may still provide little utility; alternatives may remain indistinguishable. Hybrid is a hypothesis and can lose. No numeric scoring, speculative action promotion, target execution or research merge is needed for this orientation.

## Dated handoff and validation

### Case walkthrough after Ali requested to see the examples

Ali requested a practical walkthrough after the simplified HTTPX explanation. Refreshed origin/main; no newer remote changes. Read S013–S016 post-case syntheses, S008 synthesis and the preserved S001 CLI details. These are archived case observations, not new external acquisitions. Their historical references to implementation stages remain dated; do not adopt their then-current product projections as verified present behavior.

The walkthrough uses the following concrete lessons:

| Case | Archived finding | Useful assistance to examine, not a claim of implemented output |
| --- | --- | --- |
| S001 | Model request failed; CI consumption was supported but not correlated to runtime execution | Explain which questions remain unanswered and why green CI does not close them |
| S002 | Docker success did not establish relevant Python tests; resolved framework versions were unavailable | Explain the testing gap and justify capturing versions plus running the relevant tests |
| S008 | CPython-3.6 binary wheel path disappeared while source fallback remained | Explain installation-mode change without claiming installation failure |
| S013 | Earlier explicit uv sync formed package state before later no-sync tests; runtime used a PR merge revision | Follow the sequence and exact execution identity rather than judging a later command in isolation |
| S014 | The PR command found the requested pip version already satisfied; base command actually installed a different version | Report package state without falsely attributing a fresh installation |
| S015 | The changed pytest requirement applied on Python 3.8 and was ignored on Python 3.9 | Avoid borrowing a successful sibling environment as evidence for the changed requirement |
| S016 | Tests-extra selection included coverage; separate release/build selection excluded it | Identify which selected environment actually includes the changed dependency |

A2 delivery-sequence model: action-led first earns a justified disposition; advisor-led first delivers useful evidence/explanation; hybrid delivers that explanation while independently allowing a disposition only when its evidence is sufficient. Next B will compare these using the plan's nine dimensions and current producer traces; neither this walkthrough nor the case authors' recommendations selects a winner or measures utility. Learner understanding remains open; avoid another unexplained quiz.

Walkthrough increment: only this cycle record and MEMORY.md changed; whitespace and local-reference checks pass. No executable changes or product test claim. Preserve the earlier dated handoff below as the state before this walkthrough.

Continuity gate remains open under OPERATING_GUIDE.md §2.2. Resume A2 after Ali has a meaningful opportunity to challenge/correct the current-state model. Do not interpret authorization to proceed as proof of learner mastery. Prior planning-cycle D/E ownership assessment is explicitly deferred; its preparation result remains complete and this record owns the separate comparison cycle.

Orientation increment validation: local Markdown references resolve; whitespace check passes; changes are confined to this record, a prior-record continuation link and MEMORY.md. No product, experiment, independent evaluation or fresh external-source proof is claimed. Existing experiment failures and the governance-doctor baseline mismatch remain recorded in the earlier evidence; they were not repaired by initialization.
