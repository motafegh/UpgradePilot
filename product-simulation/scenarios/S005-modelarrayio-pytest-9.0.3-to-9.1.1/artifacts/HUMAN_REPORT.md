# S005 Maintainer Report

## Recommendation

**Merge after normal maintainer review.**

This changes the transparent baseline's `run_targeted_checks` action.

## Why the baseline was too cautious

Baseline v0.1 saw literal `breaking` and `deprecation` language in pytest 9.1 and correctly treated it as a coarse warning. It could not determine whether those upstream surfaces applied to ModelArrayIO.

The full evidence shows:

- PR #85 changes only pytest 9.0.3 → 9.1.1 in `uv.lock`;
- the latest tox environments consume that lock through `uv-venv-lock-runner`;
- exact-head pytest 9.1.1 jobs passed on Python 3.11, 3.12, 3.13, and 3.14;
- the Python 3.12 latest job also included downloaded-data tests;
- the upstream breaking behavior requires `--doctest-modules`, which the repository does not use;
- the listed deprecated private APIs, hook markers, pastebin, console entry point, yield fixture, teardown fixture request, and class-scoped instance-fixture patterns were not found;
- all discovered parametrization values are concrete lists or tuples.

No remaining pytest 9.1 question identifies a useful additional check.

## Residual limits

- Network S3 tests were excluded.
- External pytest plugin internals were not independently audited.
- Negative source search is bounded.
- This is decision support, not proof that the update is safe.

## Transition

Reopen the decision in a new run if the head, lock resolution, workflow command, test selection, or repository usage changes, or if new evidence identifies a relevant pytest 9.1 warning or failure.

No target repository action was performed by UpgradePilot.