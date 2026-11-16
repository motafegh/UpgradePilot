# Exact-attempt CI step report Build

2026-11-16 · [Design cycle](2026-11-15_exact-attempt-ci-step-report_design-cycle.md) · [Report plan](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#inspect-github-reported-steps-from-an-exact-attempt)

- **A0 — DONE.** Main and origin agree at `7536e428`. Reopened the report plan, current projection, encoder, CLI and nearest tests. The frozen MapProxy and ApplyPilot material is available locally.
- **A1/A2 — DONE for the Build scope.** The prior design walkthrough showed where steps disappear, what the offline inspector will expose, and which outcomes remain unresolved. Ali selected that implementation.
- **B — DONE.** The shared CI projection retains reported step facts and the ordinary saved-facts command groups them by job.
- **Verification — GREEN.** All 1,133 product tests passed. Focused tests, frozen CLI comparisons and the existing CI presentation consumer also passed.
- **D — DONE at the walkthrough scope.** Compared MapProxy's successful step, its missing-step control and ApplyPilot's failure and unavailable-list control. Independent learner ownership remains open.
- **E — CLOSED.** Recorded the report boundary and the next maintainer-task assessment.
- **C — DONE.** Preserved scope, implementation choices, raw-input replay and regression proof.

The continuity and implementation orientation were compressed because this is the immediately selected successor to the demonstrated report design and the authorization refers directly to it. Repeating the stops would repeat the already presented provider/interpretation distinction and proposed behavior. No learner pass is inferred. A material change to delivery or proof scope would reopen orientation before the changed work.

Trace exact-attempt `WorkflowJob` and `WorkflowStep` records into selected facts in the shared CI projection, then through ordinary CLI save and offline reopen. Preserve a captured failure, an unavailable list, an empty list and an unreported conclusion. Check the additive byte budget and the absence of any promotion into dependency assessment or maintainer action.

## Implementation and scope

The shared projection appends a grouped step fact for each numeric job in the existing `workflow_execution` source. It uses the existing job identity facts and keeps each step's number and quoted provider name, status and conclusion in captured order. Field quoting keeps embedded newlines and terminal controls inside the same observation. The report projection rejects repeated job IDs before publishing an ambiguous source, and the ordinary CLI surfaces that projection error. Distinct IDs carrying the same display name remain distinct. [CI report projection](../src/upgradepilot/report_projection.py) · [CLI](../src/upgradepilot/cli.py)

The version-1 report codec measures the incremental UTF-8 size of each added identity fact with the same object shape and indentation as the file. The 128 KiB shared allowance applies to optional step details. A whole attempt that exceeds the remaining allowance keeps its inventory and an omission reason, leaving the remaining budget available to later attempts. The new report generator is version 3. The version 5 renderer shows a per-source cue in the normal report and expands only the selected attempt in `--show-facts`. A legacy source still displays saved job counts and states that individual step outcomes were absent from its saved record. [Codec](../src/upgradepilot/report_file.py) · [Renderer](../src/upgradepilot/report.py)

## Verification results

The 49 focused CLI, report, report-file and PR-description tests passed. Controls cover conflicting IDs, same-name distinct IDs, skipped and pending outcomes, missing versus empty steps, control characters, legacy counts, a run with no job rows, encoded-byte accounting and whole-attempt admission under a shared budget. Seven separate CI presentation experiment regressions passed.

The retained-input replay used the ordinary investigation and CLI save route with hash-checked source and provider payloads. It used the production Actions parser and attempt-scoped request method through a local response stub, checked the exact attempted URL and PR head query, and stubbed the unrelated PyPI branch. Fresh CLI processes reopened all four output reports in an isolated network namespace. The selected fact views matched every saved job and step field shown below. The ordinary reopen matched the generated substantive output. The earlier MapProxy report also reopened with its historical counts and an explicit absent-details note, and the retained PR text source remained inspectable.

| Replay | Selected run and attempt | Offline fact result |
| --- | --- | --- |
| MapProxy #1559 | 43457921398, attempt 1 | Eight jobs and 79 step rows. Successful steps 6 and 7 in all four displayed matrix variants. Successful step 4 in lint and typechecking. Added detail was 5,127 bytes. |
| MapProxy missing-step control | Same run and attempt | Eight jobs and 78 rows. The successful 3.12 job's removed step 6 has an unknown outcome from this capture. |
| ApplyPilot #8 | 43073710410, attempt 1 | Two jobs and 19 step rows in the selected CI run source. API job 130708096164's install step 4 displays failure. |
| ApplyPilot unavailable-list control | Same run and attempt | That API job explicitly reports unavailable step details. The selected source retains both jobs and the other job's 10 step rows. |

All four reports had the same assessments, findings, unknowns and maintainer action as the pre-change projection of the same typed investigation. The private receipts, output reports and commands are retained under the local UpgradePilot evidence store. Verification receipt SHA-256 `95d329c22077561ff66758f3392031b111c275a83727d7089b98aacc3dcd1802`. This proof used checkout Python. It establishes recorded report fidelity. Package installation, parsed matrix coordinates, compatibility, a new publication and independent maintainer usefulness remain outside the result.

Full checkout suite passed **1,133 tests** in 251.792 seconds. Test log SHA-256 `572d68b07ccf5401d4bfa2f006b0b633826600af78c9be5a19379c7198899db3`.

## Walkthrough and handoff

In the MapProxy control, the 3.12 job still has a successful job conclusion. Without the reported install row, the reader has no outcome for step 6. In the original ApplyPilot attempt, the exact install step is present and reports failure. Removing its entire step list produces a third case, where the source retains the job and reports the missing detail explicitly. This is the planned distinction carried across the report file and read back without a refresh. Establishing which command executed inside one step would require a separate observation and proof rule. The independent reconstruction exercise is deferred, with no learner pass inferred.

The next bounded question is whether the attempt cue and single source inspection let a maintainer find the reported outcomes and identify the remaining evidence gap without reading raw JSON. Review the saved cases under the existing report task procedure before qualifying usefulness or selecting a separate matrix-coordinate or command-evidence increment.

Provenance: `UP-SKILL:upgradepilot-build-implement`, `UP-SKILL:upgradepilot-learning-by-doing`, `UP-SKILL:upgradepilot-working-memory`.
