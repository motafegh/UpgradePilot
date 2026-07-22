# S004 Candidate Screening — Baseline-Sufficient Control

**Status:** Selected and complete
**Date:** 2026-07-23
**Purpose:** Select a deliberately simple real public Python Dependabot update capable of testing whether the transparent baseline is already sufficient and whether the full simulation stops before unnecessary conditional work.

## Selection criteria

A qualifying S004 candidate must provide:

- an exact public repository, PR, base, head, dependency, and patch identity;
- a patch or ordinary minor update with known directness;
- a passing current CI conclusion;
- CI that consumes the changed pinned or locked dependency and exercises its owning responsibility;
- complete enough upstream primary information to avoid speculative interpretation;
- no active evidence conflict, missing critical check, or causal failure problem;
- a credible point where additional investigation can be declared unnecessary;
- a public-safe bounded investigation surface.

A green status alone is insufficient.

## Screened candidates

### Rejected — `tkoyama010/pyvista-wasm#340`

Update: tox `4.56.3` → `4.56.4`.

Why it initially looked suitable:

- patch-level development dependency;
- one lockfile changed;
- broad test matrix passed;
- tests and lint were launched through tox.

Why it was rejected:

- the workflow installed `tox` and `tox-uv` directly from the package index without consuming the changed `uv.lock` for the tox executable;
- the passing workflow therefore did not establish which tox version was executed;
- accepting it as the control would repeat the CI-authority error exposed by S002.

### Rejected — `hsahovic/poke-env#942`

Update: websockets `16.1` → `16.1.1`.

Reason:

- the available public interface did not expose enough current check detail to prove that the changed dependency and relevant repository behavior were exercised.

### Rejected — `eugen-goebel/bi-data-analyst#40`

Update: pandas `3.0.3` → `3.0.5`.

Reason:

- the broader runtime surface and unavailable check detail made the case unsuitable for a clean sufficiency control.

## Selected candidate

### `googlefonts/glyphsLib#1145`

Update: pytest `9.0.2` → `9.0.3`.

Frozen identity:

- repository: `googlefonts/glyphsLib`;
- PR: `#1145`;
- base SHA: `044f19e4b1437bfc4343592486f4e3c6040306d9`;
- head SHA: `f3cda8a94600e58d27f1bc17c99b7693718b6350`;
- merge commit: `a007710184f634557e6524b7e3b115bf74c91b73`;
- changed file: `requirements-dev.txt`;
- exact mutation: `pytest==9.0.2` → `pytest==9.0.3`.

Why it qualifies:

- pytest is directly declared in the development requirements input and pinned in `requirements-dev.txt`;
- tox environments install `requirements-dev.txt`, so the proposed exact pytest version belongs to the exercised dependency path;
- the `Test + Deploy` workflow ran the test suite on Python 3.10 and 3.14 across Ubuntu and Windows and passed;
- the same workflow's lint job installed the development requirements through tox and passed;
- the separate regression workflow reinstalled the proposed `requirements-dev.txt` and invoked pytest directly for regression tests; it passed;
- official pytest release material describes 9.0.3 as a bug-fix release and drop-in replacement;
- no caution keyword is present under transparent baseline v0.1, while passing CI, direct dependency, and patch category select `merge_after_normal_review` through rule B05;
- no current evidence activates advisory exploitability analysis, adapter analysis, failure attribution, environment comparison, dynamic reproduction, or targeted-check design.

## Question S004 will answer

> Can UpgradePilot recognize that the transparent baseline is sufficient, confirm only the authority-critical facts, stop early, and avoid constructing unnecessary investigation stages or artifacts?

## Prospective rule

The scenario identity and baseline must be frozen before the full sufficiency confirmation. The complete scenario must preserve which conditional stages remained inactive, the cost added beyond the baseline, and the exact stopping rule.
