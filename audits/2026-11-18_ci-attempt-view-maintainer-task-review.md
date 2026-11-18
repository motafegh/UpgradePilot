# CI attempt view maintainer-task review

Reviewed 2026-11-18 at `d05f7db0`, followed by a bounded report-label repair. [Cycle and proof](../working-memory/2026-11-18_ci-attempt-view_maintainer-task-review-cycle.md) · [Report responsibility](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#inspect-github-reported-steps-from-an-exact-attempt)

The question was whether a reader can locate the exact attempt, recover reported install and test outcomes, and identify missing evidence by inspecting one selected source. This is an author-exposed development review. The assistant had previously implemented the feature and read the cases. Independent reader performance and usefulness were unmeasured.

## Recorded outcomes

The four November 16 Build reports matched the retained verification manifest. Fresh CLI opens in a network namespace reproduced their saved output exactly. Their job and step facts answered the questions below without raw JSON inspection.

| Saved case | Answer from the selected source | Remaining uncertainty |
| --- | --- | --- |
| MapProxy #1559 | Eight jobs, 79 step rows. Each of the four displayed variants records successful install step 6 and test step 7. | The display label and broader step result leave the embedded dependency command and installed Soup Sieve state open. |
| MapProxy missing-step control | The 3.12 job remains successful and its captured steps omit step 6. The view explicitly leaves outcomes of absent rows unknown. | Whether that install step ran is unknown from this capture. |
| ApplyPilot #8 | API job 130708096164 records install step 4 as failed and Tests step 6 as skipped. | The failure cause is unavailable. Successful Web jobs cannot supply the API job's missing positive premise. |
| ApplyPilot unavailable-list control | The API job remains present with its reported job outcome and an explicit unavailable step list. | The install step outcome is unavailable. |

MapProxy's older counts-only source cannot answer the step-outcome question. Its new offline rendering discloses that the individual outcomes were absent from the saved record. This baseline is the retained November 15 report, with its own production context. The comparison establishes added evidence access, without measuring a reader's speed or preference.

## Finding and resolution

**A workflow-name task could require two source inspections.** ApplyPilot's full report has two failed execution sources with the same head and attempt number. At the reviewed revision, both source inventories omit their workflow names even though the producer's `WorkflowRun` already retains them. Given an exact run ID, one inspection succeeds. Given only the workflow name `CI` and API job question, the first displayed source leads to Security, followed by the remaining CI source. The deterministic first-candidate route required two opens. This is an observed source-selection limitation, without a claim about how an independent reader would behave.

The repair copies `WorkflowRun.name` into the existing execution source's identity facts as `workflow_name`. The existing inventory and inspector both render it. New reports record generator 4. Source IDs, captured step rows and CI/action assessment meanings stay compatible with the selected report task. Original report bytes are preserved, and opening them retains their historical evidence limits.

The new frozen replays select the source from the printed workflow name before opening its facts. Each case needs one source inspection. ApplyPilot now distinguishes Security from CI in the source inventory. All fields in the four selected job/step views were checked, and the new projection's assessments, findings, unknowns and action matched the pre-repair projection on the same typed investigations. The complete focused CLI/report/report-file/PR-description suite passed 50 tests, including a two-workflow regression. No additional provider acquisition was needed.

Private review receipt SHA-256 `645602a70bfb2439fdf418904d6410e27894d4f065d2ee82686717db5a6f68df`. Workflow-selection receipt SHA-256 `83734680124806afd6aac014aef7d92c2c89daab9bb6e7e4a32a2cebbdfc303d`. Reopened field-validation receipt SHA-256 `c01313905047f6b30bfaf933fbe03830a5c4d60626bf6fd0e8667ce004f08f53`. [Projection owner](../src/upgradepilot/report_projection.py) · [Regression](../tests/test_report.py)

## Disposition

Retain the saved attempt inspector for the demonstrated observation task. The repaired navigation meets the scoped one-source criterion in these cases. MapProxy's cue first appears at line 379 of a 517-line full report, and its inspector has 146 lines. Those measured lengths justify monitoring navigation if later reader evidence exposes search friction. They do not independently justify another presentation redesign.

The next engineering question concerns MapProxy's dependency evidence. Its report records both unsupported matrix correlation and unresolved shell analysis for a command containing `matrix.pillow-version`. The existing view exposes provider outcomes while those semantic gaps remain. A successor design should establish the proposition to be answered, how literal matrix inputs are specialized before shell analysis, and the association evidence needed to connect the resulting job/step interpretation. Preserve the full four-combination responsibility and explicitly handle unresolved cases. The earlier graph and display-swap evidence remains relevant to the chosen claim strength. [Earlier matrix design](../working-memory/2026-11-15_mapproxy_job-and-matrix-identity_design-cycle.md) · [Provider-origin check](../working-memory/2026-11-15_mapproxy_provider-origin_investigation-cycle.md)

Provenance: `UP-SKILL:upgradepilot-repository-audit`, `UP-SKILL:upgradepilot-build-implement`, `UP-SKILL:upgradepilot-working-memory`.
