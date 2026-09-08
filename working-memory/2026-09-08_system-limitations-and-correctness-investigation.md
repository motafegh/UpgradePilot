# System limitations and correctness investigation

**Recorded:** 2026-09-08
**Session responsibility:** Separate supporting investigation; planning checkpoint.
**Plan:** [System limitations and correctness investigation](../plans/SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md).
**Authority:** Dated progression and handoff only; [MEMORY.md](../MEMORY.md) owns canonical project continuation.

## User request and boundary

Ali requested our own investigation process, plan and working memory, with progressive records of discoveries before deciding subsequent work. The immediate instruction was to write the plan first. This authorizes the two artifacts here, not product fixes or expansion. Product integration continues separately; do not replace its plan, live memory, working record or deferred proof obligations.

## Starting evidence and corrections

The preceding chat review traced acquisition, dependency/CI, upstream/model, Target/artifact and CLI boundaries against source and plans at `09d9eaa`, with remote documentation then advancing to `a2876bc`. It identified seed concerns about shell-comment recognition, PR revision correspondence, run-attempt binding, CI branch failure and hidden CLI diagnostics. These were source-traced, not executable reproductions or proven public incidents.

During this planning checkpoint the shared checkout advanced to `9fe57f721afe3ab8ea6fdc050124d8ce0c2610e1`, matching origin at inspection. Compared with the earlier review, product changes were in `src/upgradepilot/cli.py` and `tests/test_cli.py`; live memory selected cross-responsibility/end-to-end proof after the human-facing explanation cycle.

**Correction:** “artifact output missing” is no longer an accurate implementation finding at that snapshot. The CLI now has artifact, Target-environment and applicability rendering. Its new behavior still needs the main task's recorded executable proof. Other intermediate diagnostic omissions remain questions for fresh rendering inspection, not a blanket claim that the CLI lacks explanation.

The recorded user constraint still defers executable proof. No product tests, live acquisition, model invocation or hosted workflow was run in this planning checkpoint. Tool access alone does not close that debt.

## Seed register — revalidate before concluding

| Question | Starting evidence | Disposition at this checkpoint |
|---|---|---|
| Shell comments/quoted data become install evidence | `dependency/direct_install.py` scans segments for requirement flags; CI consumes observed declarations | Source-traced hypothesis; controlled positive/negative and composition checks pending |
| PR patch/revision mismatch | PR identity and mutable files endpoint are separate reads; source contexts use the initial head | Snapshot-consistency hypothesis; stable/changed-head sequence needed |
| Workflow attempt mismatch | Run stores attempt, jobs request `latest` | Attempt-binding hypothesis; stable/rerun sequence needed |
| CI errors stop independent branches | Actions calls precede package acquisition; exceptions reach CLI | Source-traced degradation behavior; classify prerequisite versus independent failure |
| Diagnostic detail lost in CLI | Returned index/tag/changelog outcomes are richer than earlier renderer | Refresh against changed CLI; artifact-output absence superseded |
| Deliberate coverage limits | Static/runtime separation, Target single-job/direct-requirements gate, strict source/semantic bounds | Assess value and real-case pressure; no expansion selected |
| Persistence and evaluation gaps | Existing focused storage proposal and development-only report evaluation | Classify dependencies; do not duplicate their design or claim measured quality |

Source links and discriminating checks are owned by the linked plan and will be made exact for each evaluated snapshot. Earlier source inspection is evidence to test, not authority to keep a finding.

## Planning decisions

Use one bounded investigation plan and one progressively maintained record. Prioritize potential false evidence and identity mixing before wider coverage. Keep source diagnosis separate from executable reproduction, and both separate from prevalence or product acceptance. Reuse real preserved cases with exposure/comparability disclosed; do not create an aggregate “accuracy” from heterogeneous unsupported cases.

The plan sets revision checks, permitted evidence work, coordination boundaries, completion criteria and a decision gate. It deliberately leaves repair designs open until the finding is established. Existing main-task proof should be reused only when it matches the exact proposition and revision.

## Planning validation and learning cycle

Local Markdown targets, fence balance, whitespace and governance doctor all passed. These checks validate the documentation, not the suspected defects or current product behavior. Publication is limited to the two new artifacts; unrelated checkout changes remain with their owners.

A — DONE: explained independent investigation, evidence classifications and parallel-work boundaries.
B — DONE: wrote the position-neutral investigation plan and this record; no diagnostics or fixes implemented.
C — DONE: preserved user scope, seed hypotheses and the material CLI/state correction.
D — explanation supplied with handoff; learner response pending. Ownership question for the investigation: what evidence would distinguish a safe unsupported-command abstention from an incorrect positive CI finding?
E — pending response/continuation; first proposed investigation checkpoint is baseline reconciliation followed by the command-recognition contrast, subject to the applicable execution constraints.

## Time-scoped handoff

At this planning stop, no seed hypothesis has gained executable proof. Resume by reading the then-current main state and source diff, then follow the first investigation checkpoint. Continue this record with evidence, corrections and dispositions at meaningful points. Do not launch the main task's proof campaign, write fixes, or expand Target/CI merely because this plan now exists.

Provenance: `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-working-memory`.
