# Qualification subprocess supervisor — process-group timeout cleanup repair

**Date:** 2026-11-13. **Scope:** Local execution-control safety mechanism, **not** an UpgradePilot product dependency-analysis algorithm.
**Source:** A parallel read-only project audit identified a concrete missed process-group cleanup scenario. The untracked parallel audit artifact and unrelated work were not modified or absorbed into this change.

## Observed failure class

The pre-repair [qualification supervisor](../../../tools/run_qualification_cli.py) used `start_new_session=True` and sent `SIGTERM` to the child's process group on timeout. It then waited for **the leader process** and escalated to `SIGKILL` only if that leader did not exit. A descendant could **ignore `SIGTERM`** while the leader exited quickly; the supervisor would report `deadline_exceeded` and return 124 **without killing the surviving process-group member**. The earlier plain descendant test did not cover this mismatch.

This is a **verified supervisor safety defect** in the timeout/cleanup policy, not evidence of a defect in Q1 — CARLA/OpenCV: Normal Dependency and Artifact Investigation or Q2 — Pydantic/Soup Sieve: Normal Investigation with Conditional Local Language Model. Both actual product invocations exited normally without the timeout branch.

## Narrow implementation change

The supervisor's `_stop_group` now sends group-wide `SIGTERM`, gives a short **0.4-second** grace period, then **always attempts process-group `SIGKILL` before reaping the leader**. This means a leader's early termination cannot suppress a last-resort group termination. If the group no longer exists, the code tolerates `ProcessLookupError`. The leader is not reaped before final group signaling, avoiding premature process-group identity recycling. No HTTP routing, provider request, Python dependency analysis, report content or local model behavior was changed.

The guarantee is scoped to descendants **remaining in the launched process group** under normal Linux process permissions. It cannot claim cleanup of independent processes intentionally detached into another session/group or tasks unkillable by the OS.

## Controlled regression proof

An additional offline regression starts a child that installs a signal-ignoring (`SIGTERM`) handler and creates a ready marker. The parent becomes idle. After the 0.35-second deadline, the parent leader exits on `SIGTERM`, but the stubborn descendant would later write an `escaped` marker if left running. The amended supervisor escalates to group `SIGKILL`, returns 124 with `deadline_exceeded`, and the expected escape marker remains absent after a delayed check. This specifically closes the previously missing risk rather than only testing a well-behaved child.

The eight focused [supervisor tests](../../../tests/test_run_qualification_cli.py) passed, including this new adversarial descendant and the prior private files, exit code, deadline and refusal cases. The four focused [model telemetry observer tests](../../../tests/test_qualification_model_observer.py) also passed in controlled offline mode. The final **full installed-interpreter regression** passed: **1,126 tests, OK** in the runner's recorded **237.375 seconds**. Private final test-log SHA-256 `2151542ae8bdcc5876b2f12cc7b1852412770749b6e60cc6ec3982a774d38ae5`.

**Repair status:** targeted change and the adversarial control tested; **all 8 supervisor tests plus 4 model-observer tests and 1,126 full-suite tests passed**. No live target PR or local-model invocation was rerun to repair this timeout control.
