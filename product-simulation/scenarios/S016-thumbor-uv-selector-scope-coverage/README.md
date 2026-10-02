# S016 — Thumbor coverage: uv selector scope controls package-state proof

**Date:** 2026-09-22
**Status:** Complete at admitted simulation depth
**Form:** untouched real Dependabot proposal + exact selector/runtime controls

## Case identity

Target: `thumbor/thumbor#1867`

Dependency transition:

`coverage 7.14.1 → 7.15.4` in `uv.lock`.

Frozen proposal revisions:

- base: `b46e940867efc287a04131194c0a437bbc8e7696`
- head: `ea7c44f1830fa4cd0df1ceeab17a01d20ccad38f`
- observed PR CI checkout: synthetic merge `8ff9e8b64668c22706cf29c202b0356375c9bf8d`

Only `uv.lock` changes in the proposal.

## Owned question

> When several successful uv commands use the same changed lock, which ones may support a positive state claim for the changed package?

## Lock/root structure

The exact-head lock contains `coverage==7.15.4`.

The root Thumbor package places coverage in optional extra `tests`.

The independent dependency groups are:

- `build`: setuptools, wheel
- `docs`: sphinx-reload, sphinx-rtd-theme
- `release`: build, twine

Coverage is not a root of those groups.

## Positive selected-root path

Exact workflow occurrence in `.github/workflows/lint.yml`:

`uv sync --locked --extra tests`

Observed job:

- lint/formatter run `31902346443`
- job `95054923808` (`black`)
- conclusion: success
- Python 3.14.7

Runtime output reports:

- resolved 135 packages;
- installed 67 packages;
- `+ coverage==7.15.4`.

The selected `tests` extra reaches the changed package and the runtime state observation agrees.

## Negative scoped control

Exact workflow occurrence in `.github/workflows/release.yml`:

`uv run --locked --only-group release --only-group build python -m build --sdist --no-isolation`

Observed job:

- release run `31902346382`
- job `95054923612` (`build_sdist`)
- conclusion: success
- Python 3.10.20

The command creates a fresh `.venv`, installs 36 packages, successfully builds the sdist, and does not include coverage in the selected installed set.

This is a successful uv operation against the same changed lock, but its exact selector surface is release+build rather than tests.

Therefore it cannot be used as positive evidence that the changed coverage version was satisfied for this operation.

## Secondary docs control

The docs job expands `make setup_docs build_docs` to a docs-only uv environment. Runtime output installs 39 packages and contains no coverage.

This confirms the same real scope behavior, but it is secondary because current static workflow analysis does not expand Makefile targets.

## Core distinction

`changed package exists in uv.lock + uv command succeeds`

is not enough.

The useful relation is:

`exact changed lock + exact selected roots + changed package reachable from those roots + admitted operation semantics + exact runtime success`

before a command-derived B5 state proposition may be considered.

## Current UpgradePilot projection

The existing decomposition is aligned with this real case:

- `uv_lock.py` owns exact textual lock transition;
- `environment.py` explicitly rejects lock-membership-as-universal-reachability;
- `environment_selection.py` owns uv selector parsing;
- `uv_reachability.py` owns selected-root reachability.

The PR lock diff is compatible with the current transition boundary: the semantic package transition is coverage `7.14.1 → 7.15.4`; registry source is unchanged; sdist/wheel inventory churn is artifact metadata rather than a second dependency transition.

S016 therefore validates an existing architecture decision rather than demanding a new generalized resolver.

## What S016 establishes

- real Dependabot uv-lock updates can be exercised through multiple different selector scopes;
- successful uv operation does not imply every package in the lock is in the selected environment;
- positive state evidence must compose with selected-root reachability;
- current separation of lock transition, environment selection, and reachability has real empirical value;
- direct runtime output can act as a useful evaluation witness for the selected scope.

## What S016 does not establish

Do not infer:

- coverage is globally absent from the release runner;
- package absence outside the fresh selected environment;
- state persists after later mutation;
- behavioral compatibility;
- update safety;
- a requirement to ingest uv logs in product code;
- a universal claim about every uv selector.

## Evidence bundle

1. `artifacts/CASE_IDENTITY_AND_LOCK_TRANSITION.json`
2. `artifacts/TESTS_EXTRA_POSITIVE_RUNTIME.json`
3. `artifacts/RELEASE_GROUP_NEGATIVE_CONTROL.json`
4. `artifacts/CURRENT_PRODUCT_PROJECTION_AND_STOP.json`

Supporting analysis:

- `../../S016_CANDIDATE_SCREENING.md`
- `../../S016_POST_CASE_SYNTHESIS.md`

## Stop

S016 stops at selector-specific command-completion state applicability. Reopen only for implementation transfer, selector parsing regressions, selected-root reachability changes, or later-state continuity.