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
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
```

## Observed WSL validation

Ali ran the expanded suite on 2026-07-24 in the actual WSL2 development environment using
Python 3.12:

```text
Ran 12 tests in 0.002s
OK
```

Ali also ran the live-network proof:

```bash
python3 -m upgradepilot googlefonts/glyphsLib 1145
```

The command returned:

```text
Changed-file records: 1
Changed file: requirements-dev.txt (modified)
Dependency change: supported
Source file: requirements-dev.txt
Package: pytest
Old version: 9.0.2
Proposed version: 9.0.3
```

This establishes that the current changed-file acquisition and exact pinned-dependency
extraction work against the real public S004 PR in Ali's environment.

The deterministic suite proves only the implemented mocked boundaries, while the live run
proves one real public path. Neither establishes CI authority, dependency exercise by CI,
upgrade safety, recommendation correctness, broader dependency syntax support, production
readiness, or independent ownership.

The immediate ownership exercise is one Ali-authored test for equivalent normalized package
spellings before work advances to exact-head workflow evidence.
