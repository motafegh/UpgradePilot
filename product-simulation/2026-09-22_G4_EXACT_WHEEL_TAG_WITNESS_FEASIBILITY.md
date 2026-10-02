# G4 — Exact target wheel-tag witness feasibility

**Date:** 2026-09-22
**Kind:** Non-controlling Product Simulation mechanism/reality research.

## Question

Does real public CI expose a target-owned runtime witness for the exact compatible wheel tags of a particular OS/Python environment?

## Discovery

A bounded GitHub code search for `pip debug` under `.github/workflows` returned 76 matching workflow files. This is discovery evidence only, not prevalence.

## TileDB-Py exact witness

- Repository: `TileDB-Inc/TileDB-Py`
- Reference PR: `#2308`, `Support NumPy 2.5.0`
- Head: `395cbff79cb9690e5350216a4d570fad52a07671`
- Head-associated run: `28433363033`, `TileDB Python CI`, success

The exact-head `.github/workflows/ci.yml` runs a matrix over OS and Python versions and, after `actions/setup-python`, executes `pip debug --verbose` in a dedicated `Print pip debug info` step.

That command executes inside the selected runtime environment rather than inferring compatibility from runner labels.

## Runtime evidence

Successful job `84253268965` (Ubuntu/Python 3.12) logs `Compatible tags: 1068`, beginning with `cp312-cp312-manylinux_2_39_x86_64`, `cp312-cp312-manylinux_2_38_x86_64`, etc.

Successful job `84253268987` (Windows/Python 3.12) logs `Compatible tags: 42`, beginning with `cp312-cp312-win_amd64`, `cp312-abi3-win_amd64`, `cp312-none-win_amd64`, etc.

Successful job `84253268940` (macOS Intel/Python 3.12) logs `Compatible tags: 2931`, beginning with `cp312-cp312-macosx_15_0_x86_64`, `cp312-cp312-macosx_15_0_intel`, and `cp312-cp312-macosx_15_0_universal2` among the early entries.

## Finding

The G4 witness-feasibility question has a clear positive answer: real public CI can emit the exact runtime-compatible tag set for a selected target using a target-owned command such as `pip debug --verbose`.

`runner label + setup-python declaration` is not equivalent to exact compatible tags. A successful `pip debug --verbose` in the selected runtime is a much stronger witness.

Matrix identity remains essential because Linux, Windows, and macOS rows produce materially different tag sets. A static job key cannot stand in for every runtime row.

## Product boundary

This establishes feasibility, not current UpgradePilot capability and not authorization for generic log ingestion. The Target/wheel-evidence owner can separately consider a structured tag artifact/output, bounded parsing of an explicit target-owned command, another runtime witness, or continued explicit non-support when no witness exists.

The next high-value question is whether an UpgradePilot-supported dependency-update case naturally exposes such a witness without requiring new repository instrumentation.
## Supported-update bridge screening

A bounded follow-up checked whether the strongest `pip debug --verbose` witness could already be tied to a clean UpgradePilot-style Python Dependabot update.

TileDB-Py has historical Python Dependabot PRs, including `#865` (`numpy 1.19.4 → 1.21.0` in `misc/requirements_wheel.txt`, head `17031ec1...`). However, the exact workflow at that proposal head did **not** yet contain `pip debug --verbose`; it printed Python/pip versions and ran installs/tests, but not exact compatible-tag output.

epics-base/p4p `#81` is another historical NumPy Dependabot proposal, but its exact-head workflow likewise did not contain the current-style `pip debug` witness.

Therefore the current result remains:

`real exact-tag witness mechanism exists` + `real Python Dependabot cases exist` != `one verified case currently composes both`.

This is a bounded acquisition gap, not evidence that the bridge does not exist. Do not force an end-to-end case from mismatched historical revisions.