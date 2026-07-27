# Test Suite

This directory contains deterministic tests for the product source under `src/upgradepilot/`.
Historical pre-reset tests are not part of this suite.

Test responsibilities include:

- `test_github_client.py` — PR identity, changed-file validation, pagination, and reconciliation;
- `test_dependency_change.py` — supported exact pins and explicit unsupported patch states;
- `test_github_actions.py` — exact-head workflow runs, jobs, steps, pagination, and identity binding;
- `test_github_repository.py` — run-specific workflow path, exact-head file retrieval, base64 decoding, and unavailable files;
- `test_workflow_commands.py` — bounded workflow command extraction;
- `test_ci_authority.py` — sufficient, insufficient, and unresolved CI-authority behavior.

Run from the repository root:

```bash
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
```

Observed validation belongs in a dated evidence record and the live continuation belongs only
in `MEMORY.md`; this index does not record pass counts or latest results.

The tests prove only their bounded deterministic claims. They do not prove broad YAML
support, indirect tox/script authority, complete CI coverage, upgrade safety, or a correct
maintainer recommendation.