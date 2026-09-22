# S016 Candidate Screening — Thumbor uv selector scope

**Date:** 2026-09-22
**Status:** ADMITTED for bounded real-case simulation
**Form:** untouched real public Dependabot proposal + exact positive/negative selector controls

## Candidate identity

- Repository: `thumbor/thumbor`
- PR: `#1867` — Dependabot `coverage 7.14.1 → 7.15.4`
- Base: `b46e940867efc287a04131194c0a437bbc8e7696`
- Head: `ea7c44f1830fa4cd0df1ceeab17a01d20ccad38f`
- Observed PR runtime checkout: synthetic merge `8ff9e8b64668c22706cf29c202b0356375c9bf8d`
- Changed file: `uv.lock` only

## Q — Named question

> Does a successful uv operation against the changed lock establish the changed package state merely because the package exists in `uv.lock`, or must the exact selected extras/groups reach that package?

## G — Existing-evidence gap

S013 covers earlier sync followed by later no-sync exercise. S014 covers already-satisfied versus freshly installed state. S015 covers marker applicability in requirements files.

No retained scenario yet validates the current uv design boundary:

`lock transition != selected-root reachability != command-completion package state`.

## C — Consequence

Without selector-aware reachability, an unrelated successful uv operation could be borrowed as positive evidence for a changed lock package it never selected.

That would create a false B5 P2/P7 composition.

## E — Evidence feasibility

Exact public evidence is available.

The lock records `coverage==7.15.4` and the Thumbor workspace package places `coverage` under optional extra `tests`.

Positive direct workflow occurrence:

`uv sync --locked --extra tests`

in lint/formatter job `black` (`95054923808`) succeeds and runtime output explicitly includes:

`+ coverage==7.15.4`.

Negative direct workflow control:

`uv run --locked --only-group release --only-group build python -m build --sdist --no-isolation`

in release job `build_sdist` (`95054923612`) succeeds, creates a fresh `.venv`, installs 36 packages, and does not include coverage.

The exact lock root structure shows:

- optional extra `tests` contains `coverage`;
- group `build` contains `setuptools`, `wheel`;
- group `release` contains `build`, `twine`.

An additional docs control successfully builds a docs-only environment without coverage, but it expands through the Makefile and is secondary evidence because current static workflow analysis does not expand Make targets.

## S — Safe boundary

All evidence is public/read-only. No rerun, mutation, credential, or private data is required.

## N — Negative-result value

If release/build roots reached coverage transitively, that would challenge our assumed selector separation. If the positive tests selector did not reach coverage, it would challenge current selected-root modeling. Either result is useful.

## L — Claim limit

S016 may establish selector-specific reachability and observed runtime package-state differences for this exact proposal.

It must not establish:

- that coverage is absent globally or from every preexisting environment;
- uv selector prevalence;
- later package persistence;
- behavioral compatibility or update safety;
- a required implementation architecture.

## T — Stop condition

Stop when the exact lock transition, root ownership, positive tests-extra path, negative release/build path, runtime checkout identity, and current-product projection are preserved.

## F — Case form

Untouched real public evidence is ideal because one proposal naturally contains both a positive selected-root witness and a successful unrelated scoped uv control.

## Current-product projection

Current UpgradePilot already separates these responsibilities:

- `dependency/uv_lock.py`: exact textual lock transition only;
- `dependency/environment.py`: lock context does not imply reachability;
- `dependency/environment_selection.py`: parses uv extras/groups and `only` selectors;
- `dependency/uv_reachability.py`: evaluates changed-package reachability from selected roots.

The PR patch is compatible with the current lock-transition boundary: after artifact-only sdist/wheel churn is ignored, the meaningful package transition is coverage `7.14.1 → 7.15.4` with unchanged registry source.

## Admission decision

**PASS.** S016 is a real outcome-level validation of an existing UpgradePilot decomposition and a direct B5 P2 pressure case.

Primary evaluation roles:

- `integration_reality_check`
- `property_invariant`
- `method_comparison`
- `stopping_sufficiency`