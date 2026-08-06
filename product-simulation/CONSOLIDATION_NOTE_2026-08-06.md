# Product-Simulation Branch Consolidation — 2026-08-06

This short note records a branch-handling correction only.

## Canonical working branch for current product-simulation research

`agent/product-simulation-case-screening-01`

The product-simulation recalibration, subsequent candidate screening, S006 admission, and future case work should continue on this branch unless Ali explicitly requests another branch for a concrete reason.

## Obsolete side branches

The following branches are retained only as historical Git references and should not receive further work:

- `agent/product-simulation-case-program-proposal`
- `agent/product-simulation-s006-qldebugger-coverage-gap`

The proposal branch contains earlier design material whose useful concepts were selectively carried into the recalibrated framework. It must not be merged wholesale into the calibrated branch.

The S006 branch was created unnecessarily. Its S006 commits are being incorporated into the calibrated branch without rewriting their prospective history.

## Rule going forward

Do not create a new branch per simulation case by default.

Use the calibrated product-simulation branch for sequential discovery, screening, case admission, and scenario work. Create another branch only when parallel/conflicting experimental work, destructive risk, or Ali's explicit instruction gives a concrete reason.

This note does not change project live state, simulation governance, product architecture, or `MEMORY.md`.