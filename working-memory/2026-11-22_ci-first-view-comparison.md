# CI first-view comparison

- **Repository baseline:** `7a95a9bbbb1357a4e87794b2e63a80ec0266b1fe`
- [F4 development results](evidence/2026-11-22-maintainer-usefulness-preparation/REVIEW_RESULTS.md#disposition)
- [First-view comparison method](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#first-view-comparison-on-saved-reports)
- UP-SKILL:upgradepilot-planning-design
- UP-SKILL:upgradepilot-repository-audit
- UP-SKILL:upgradepilot-working-memory

Ali selected the offline design comparison and the resulting Build decision. Learning stays in its parallel workstream. This comparison uses saved product reports at their recorded horizons and edits no product code.

## Frozen comparison

| Input | Saved report SHA-256 | Assigned role |
|---|---|---|
| MapProxy #1559, F4 assisted report | `3214f53ecfbf9c2b15d937363d0b97056438402d5e343ebfe6e5a656382b2706` | Main case for repeated scoped CI evidence |
| ApplyPilot #8, corrected November 21 ordinary CI replay | `189313e90a01814a5569c34de3f57c1ac68057c0d7955342efed3045f2a3320e` | Failed-install control with successful sibling jobs |

View A is the ordinary saved-report rendering. View B starts with a concise excerpt and provides the same detailed report and selected-facts reader. For each, locate the exact changed pin, determine successful, failed, or unresolved consumption, recover the supporting run, attempt, job, and step, identify what remains unknown, and retain the recorded action. Compare the number of report sections and source inspections needed by an explicit navigation path. Line locations are descriptive. No elapsed time or independent user behavior is inferred.

For a Build recommendation, require a compact view justified by structured saved evidence, correct outcomes and proof boundaries, a direct route to relevant retained facts, and a specific improvement over the baseline. Inspect ApplyPilot's source binding before admitting a generalized failure summary. An exposed author can demonstrate this design and its structural properties. Maintainer usefulness needs its own evaluation.

## View B sketches

These are author-written excerpts for comparison. Both sit above the full original report, which remains available for detail and source inspection.

### MapProxy

```text
MapProxy #1559 · soupsieve 3.0.4 → 4.0
Base a6507dd0dba671e48d303a74f7a5575dadf7fd76 · head ac01b8901935bfc16a0195277b4aec1c43275897
CI run 43457921398, attempt 1 · 7 successful scoped executions of pip install -r requirements-tests.txt
Step 6 · Python 3.12 (job 131996881880), 3.13 (131996881564), 3.14 (131996881411), 3.15 (131996881633), and coverage (131996881258).
Step 4 · lint (job 131996881382) and typechecking (131996881059).
The doc job has no supported observation for this requirements command.
Installed version unresolved in all seven observations. The recorded invocation leaves pip's effective environment unknown.
Evidence · upgradepilot --open-report PATH --show-facts source-4
Maintainer action · abstain
```

### ApplyPilot control

```text
ApplyPilot #8 · pyee 14.0.0 → 16.0.1
Base 4996efaa87cb93289d2da899f306d779a84687f0 · head 3009f89f0d4f58fcc588647a5c33f3a8e95bf05f
CI run 43073710410, attempt 1 · API lint and tests, job 130708096164, step 4 failed.
The failed step was configured to run python -m pip install -r requirements-lock.txt ruff==0.17.4 from services/api.
The failed step leaves successful dependency consumption unestablished. Its cause and installed version are unresolved.
Evidence · upgradepilot --open-report PATH --show-facts source-5
Maintainer action · abstain
```

The ApplyPilot excerpt is an analyst reconstruction from the existing CI assessment, static command, and selected run facts. Its source facts and conclusion are checkable. Its exact join is unavailable in the saved command assessment, so the excerpt does not qualify as an automatic renderer result.

## Offline verification

Reopened both exact reports and rendered the full and selected-facts views with networking isolated. MapProxy's normal F4 capture and ApplyPilot's corrected CI replay retain their original observation horizons. [F4 packet receipt](evidence/2026-11-22-maintainer-usefulness-preparation/PACKET_RECEIPT.json) · [Matrix acceptance and ApplyPilot replay](evidence/2026-11-21-matrix-final-acceptance/RESULTS.md)

| Navigation task | A. Existing saved rendering | B. Proposed first view |
|---|---|---|
| MapProxy identity and CI scope | Dependency assessment starts at line 18 and overall CI assessment at line 30. The overall verdict gives the scope without listing the exact commands. | Update, exact revisions, successful command, result count and named jobs are together at the start. |
| MapProxy exact job, step and package-state limit | The first reported job ID is at line 52. The first command-completion assessment begins at line 364. The recorded action is on line 721 of a 1,140-line saved view. The original F4 console capture had 1,141 lines including the terminal blank line. | A nine-line excerpt puts job, step, common limit and action together and points to one saved-facts command. The reader can reopen the same per-job observations. |
| ApplyPilot exact failed step | The 397-line saved view states the failure in the CI assessment at line 30. The exact numeric job is recoverable in the saved facts for `source-5`. | The seven-line analyst excerpt is faithful and supplies the same source directly. Existing typed command facts do not support generating the exact numeric join automatically. |

MapProxy's seven `runtime-command-*` assessments joined to eight associated job instances through run ID, attempt, source job index, instance kind and expansion slot. The retained byte spans isolated the requirements command inside each script. Source order distinguished five second commands from two sole commands. Every reported step matched the same-attempt `source-4` facts. All seven package-state assessments returned the same manager-environment stop, so the sketch can state it once without merging their job and step identities. The `doc` context had no admitted command observation. Both reports retained `abstain`.

ApplyPilot's `ci` assessment correctly states that the consuming step failed. The saved `runtime-command-1` has the workflow, changed command and static step but carries no structured run, attempt, runtime job ID or exact runtime step number. The selected `source-5` facts independently retain the named failed step and successful sibling evidence. Automated association by display label, report prose, or first nearby successful job would extend beyond the saved binding.

Two additional saved MapProxy controls checked an entry guard requiring complete structured scopes and successful command outcomes. The [matrix controls](evidence/2026-11-21-matrix-final-acceptance/RESULTS.md) supplied the explicit-skip report SHA-256 `d45405158edea0df9afc8540415d69741c017ee3b011a94584a0af3c44a94da5` and missing-install report SHA-256 `98d47a24cdfde56970116b3643932b0975790c48da7ac8c3a95740dcf99341ce`. The guard withheld the homogeneous success overview for both. In particular, the missing-install control's overall CI state is still `supported_runtime_correlated` because other jobs qualify. Its first command is unresolved. A guard based solely on the overall verdict would miss this difference.

## Build decision

Recommend one bounded presentation increment in the existing report first view, using the typed saved record. A qualified report can summarize successful, individually bound command observations and consolidate a truly shared unresolved reason. Retain the full report, all existing source IDs, changed-version limits and action. Require sufficient exact linkage across the candidate set before emitting a homogeneous overview. Leave cases with unbound, failed, skipped or mixed observations on their existing detailed path for this increment. ApplyPilot demonstrates why a generalized failed-step summary needs its own typed association before automatic rendering.

The concrete improvement is the placement of the answer and its source together, supported by the exact saved MapProxy fields and successful refusal controls. Next implementation proof should cover ordinary and saved rendering, historical schema compatibility, different job and step identities, source inspection, mixed and missing evidence, and preservation of ApplyPilot's existing failure finding. This comparison does not measure reviewer performance or claim that a general summary is already implemented.
