# Manual product verification workflow

**Date:** 2026-09-08
**Responsibility:** Repeatable installed-package and deterministic product verification, parallel to the main implementation.
**Status:** Workflow prepared and statically checked; first hosted execution pending.

## Design and ownership

Continued the supporting-work sequence after evaluation calibration and the installation quickstart. No `.github` workflow existed. Inspected package metadata, CLI entry points and controlled product test/provider seams. The main implementation explicitly retains deferred executable proof, so this first workflow uses manual dispatch only; publishing it does not execute that validation.

Added [the workflow](../.github/workflows/product-verification.yml), registered `.github/workflows/` as the hosted repository-verification owner in root agent guidance, and added README usage/claim limits. No product source, tests, dependency declarations, experiment machinery or live project selection changed.

The job uses Ubuntu 24.04 and Python 3.12, installs the product into a fresh virtual environment, checks dependency consistency and installed CLI startup outside the checkout, then runs focused investigation composition before the full deterministic product suite. No test/model/live-proof command from `experiments/` or `tools/` is invoked. Package installation still uses the network; this workflow is not a network isolation boundary. Dependencies remain resolved from project ranges rather than a lock, so interpreter/package versions and the exact selected commit are printed for diagnosis.

A manually selected branch supplies the checkout. Read-only contents permission, checkout credential non-persistence, immutable action revision pins and a 15-minute job limit keep this bounded. No workflow input is interpolated into shell code. No cache, publication, artifact service or multi-version matrix was introduced for speculative coverage.

## External reference verification

Consulted official [manual dispatch documentation](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow), [checkout](https://github.com/actions/checkout) and [setup-python](https://github.com/actions/setup-python). `git ls-remote` against those official repositories resolved:

- checkout `v7`: `3d3c42e5aac5ba805825da76410c181273ba90b1`;
- setup-python `v6`: `ece7cb06caefa5fff74198d8649806c4678c61a1`.

The workflow must be present on the default branch for the manual dispatch UI. No run was dispatched in this task.

## Validation and proof limits

Local validation parses YAML using the string-preserving BaseLoader, checks that manual dispatch is the only trigger, confirms the permission and immutable action pins, verifies the referenced focused test exists, and passes each run block to `bash -n`. Markdown/local links and governance doctor are checked before publication. These establish local configuration consistency, not GitHub acceptance or runner success. `actionlint` was not installed; no actionlint result is claimed.

The previous quickstart independently established clean local installation and CLI startup. It does not prove this hosted workflow or the newly added product tests. Product/experiment suites and live acquisition were not run here; their existing proof debt remains explicit. The first hosted run must be inspected before enabling automatic triggers or claiming CI is green.

## Learning cycle

A — DONE: separated repeatable test execution from live inference and from deferred proof closure.
B — DONE: implemented a minimal manual workflow with installed-package checks and focused-to-broad progression.
C — DONE: recorded workflow scope and validation limits; main project memory unchanged.
D — explanation supplied; learner review pending.
E — next evidence is a deliberately dispatched hosted run when selected; broader automation should follow that result.

Useful ownership distinction: a valid workflow file is a recipe for proof, not proof that the selected tests pass. The same distinction applies to the evaluation labels and product plans prepared in the preceding slices.

Provenance: `UP-SKILL:upgradepilot-build-implement`; `UP-SKILL:upgradepilot-working-memory`.
