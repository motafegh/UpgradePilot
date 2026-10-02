# Retargeting semantics — real-world reality check

**Date:** 2026-09-22
**Kind:** Non-controlling Product Simulation breadth/control research.

## Question

Are pip retargeting semantics such as `--target`, `--user`, and `--prefix` merely theoretical edge cases, or do they occur materially in public CI? And do they already intersect the exact dependency-update consumption paths UpgradePilot cares about?

## Discovery snapshot

GitHub workflow-file discovery searches produced large file-level co-occurrence sets:

- `pip install` + `--target`: 20,896 matching files;
- `pip install` + `--user`: 27,072;
- `pip install` + `--prefix`: 10,848.

By contrast, exact `PIP_TARGET` environment-variable search under workflow paths produced only 9 matches.

These counts are not prevalence estimates and can include scripts/templates or unrelated occurrences in the same file. They establish only that CLI retargeting is a real and broadly visible CI pattern rather than a synthetic-only concern.

## Concrete current example — Equinor reusable Python workflow

`equinor/ops-actions/.github/workflows/python.yml` accepts a `pip_target_dir` workflow input and executes `pip install -r "$REQUIREMENTS" --target "$PIP_TARGET_DIR"` or `pip install "$REQUIREMENTS" --target "$PIP_TARGET_DIR"`.

This validates the design intuition that destination relation can matter. The destination itself is not inherently invalid; whether it supports later execution depends on how that directory is incorporated into the resulting artifact/runtime.

## Dependency-update controls — retargeted command can be irrelevant

### Elastic Rally #2189

Dependabot updates `soupsieve 2.8.4 → 2.9` in `uv.lock` (head `5ef63308eae9f51756e4b4b1aa3a107cf5cc5654`). The relevant unit-test path creates a uv project environment and runs `uv sync --locked --extra=develop` through the Makefile.

The same workflow also has an `install-with-pyenv` job using `pip install --user` for pip and published `esrally`, but that job does not consume the changed `uv.lock` source. Its retargeting semantics must not contaminate the changed-dependency Target inference.

### sqlalchemy-cockroachdb #308

Dependabot proposes `cryptography 48.0.0 → 50.0.0` (head `39541a7f0fc2bc04d9c91f67a2f02df091d3dc24`). CI uses `pip install --user tox==...` to install the test runner. Again, the retargeted command is tooling setup, not direct evidence that the changed cryptography source was installed into the relevant test environment.

## Finding

Retargeting is **real enough to justify a semantic class**, so it should not be dismissed as hypothetical.

But the stronger UpgradePilot question is relational:

`exact changed-dependency consumer is retargeted` + `target destination relation to later exercise is known?`

The first recent Dependabot controls inspected do not satisfy that stronger shape. They instead expose an over-broad-analysis risk: noticing any `--user` or `--target` command in the workflow and assigning its semantics to the proposal would be wrong.

## Current priority

Keep retargeting as a real but **not yet high-pressure supported-update gap** until a case is found where the exact changed dependency consumer itself is retargeted. The current evidence does not justify a broad environment-location resolver solely from these controls.