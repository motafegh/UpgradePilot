# Active Test Suite

The pre-B2 M2 tests were removed from the active test path under
[`ADR-0003`](../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md).
Their exact historical versions remain available at commit
`e7425dcfc20f093ac10c9a903f1c4ae50a8b2638` and are not current coverage.

The active deterministic suite now contains:

- `test_github_client.py` — pull-request identity, ambiguous `404`, changed-file pagination,
  changed-file response validation, and exact record-count reconciliation;
- `test_dependency_change.py` — one supported exact pinned Python dependency update plus
  explicit unsupported results for missing, incomplete, non-pinned, mismatched, and ambiguous
  patch evidence.

Run the active suite from the repository root after installation:

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
```

## Current validation state

The 12-test source candidate passed in an isolated Python test layout before publication.
Ali's WSL2 validation remains required before the B2 checklist can mark this increment complete.

The previous observed WSL validation on 2026-07-24 applied to the original two-test identity
increment:

```text
Ran 2 tests in 0.000s
OK
```

Ali also ran the earlier live-network smoke command:

```bash
upgradepilot googlefonts/glyphsLib 1145
```

It successfully returned the expected public PR identity and exact base/head SHAs. The updated
live proof must additionally report:

```text
Changed file: requirements-dev.txt
Package: pytest
Old version: 9.0.2
Proposed version: 9.0.3
```

The deterministic suite proves only the implemented mocked boundaries. The pending live WSL
run must establish that current changed-file acquisition and extraction work against the real
public PR. Neither proof establishes CI authority, upgrade safety, recommendation correctness,
production readiness, or independent ownership.
