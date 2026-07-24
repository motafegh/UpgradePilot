# Active Test Suite

The pre-B2 M2 tests remain historical and are not current coverage.

The active deterministic suite contains:

- `test_github_client.py` — PR identity, changed-file validation, pagination, and reconciliation;
- `test_dependency_change.py` — supported exact pins and explicit unsupported patch states;
- `test_github_actions.py` — exact-head workflow runs, jobs, steps, pagination, and identity binding;
- `test_github_repository.py` — run-specific workflow path, exact-head file retrieval, base64 decoding, and unavailable files;
- `test_ci_authority.py` — sufficient direct exercise, tox and multi-job unresolved states, unavailable definitions, and unsuccessful CI.

Run from the repository root:

```bash
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
```

## Validation history

Ali observed the previous 18-test suite passing in WSL2 and validated live exact-head Actions acquisition for `googlefonts/glyphsLib#1145`.

The new CI-authority source adds 8 test methods, bringing the suite to 26 methods. That count is structural only until Ali runs the suite.

The tests prove bounded deterministic behavior. They do not prove broad YAML support, indirect tox/script authority, complete CI coverage, upgrade safety, or a correct maintainer recommendation.
