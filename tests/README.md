# Active Test Suite

The pre-B2 M2 tests were removed from the active test path under
[`ADR-0003`](../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md).
Their exact historical versions remain available at commit
`e7425dcfc20f093ac10c9a903f1c4ae50a8b2638` and are not current coverage.

The active deterministic suite contains:

- `test_github_client.py` — pull-request identity, ambiguous `404`, changed-file pagination,
  changed-file response validation, and exact record-count reconciliation;
- `test_dependency_change.py` — one supported exact pinned Python dependency update plus
  explicit unsupported results for missing, incomplete, non-pinned, mismatched, and ambiguous
  patch evidence;
- `test_github_actions.py` — exact-head `pull_request` workflow-run acquisition, explicit empty
  evidence, pagination, job/run/SHA binding, and bounded step-summary validation.

Run the active suite from the repository root after installation:

```bash
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
```

## Validation history

Ali previously observed 12 tests passing in WSL2 and validated the live public path through
`pytest 9.0.2 → 9.0.3` extraction for `googlefonts/glyphsLib#1145`.

For the exact-head Actions increment, the assistant ran the source directly with Python 3.13:

```text
Ran 18 tests
OK
syntax compilation passed
```

The assistant environment could not perform editable installation because its package index was
unavailable. Ali's WSL2 editable-install, deterministic suite, and live S004 command are the next
authoritative proof.

The Actions tests prove only controlled acquisition and validation behavior. They do not prove
that real CI installed or exercised the changed dependency, that the update is safe, or that any
maintainer recommendation is correct.
