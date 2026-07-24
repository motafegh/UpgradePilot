# Active Test Suite

The pre-B2 M2 tests were removed from the active test path under
[`ADR-0003`](../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md).
Their exact historical versions remain available at commit
`e7425dcfc20f093ac10c9a903f1c4ae50a8b2638` and are not current coverage.

The active suite now begins with `test_github_client.py`, which verifies the first read-only
GitHub acquisition behavior:

- a successful response is converted into exact pull-request identity;
- the request uses explicit connect/read timeouts;
- authentication is optional and not invented when absent;
- a GitHub `404` remains `not_found_or_inaccessible` rather than being overstated as proof
  that the pull request does not exist.

Run the active suite from the repository root after installation:

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
```

## Observed WSL validation

Ali ran the suite on 2026-07-24 in the actual WSL development environment using Python 3.12.
Both tests passed:

```text
Ran 2 tests in 0.000s
OK
```

Ali also ran the separate live-network smoke command:

```bash
upgradepilot googlefonts/glyphsLib 1145
```

It successfully returned the expected public PR identity and exact base/head SHAs. The live
command is complementary evidence, not part of the deterministic unit suite.

An initial run before reinstalling the editable package failed because the existing virtual
environment did not yet contain the newly declared `requests` dependency. Running
`python -m pip install -e .` synchronized the environment with `pyproject.toml` and resolved
the failure.

These tests and the live smoke establish only the behavior they execute. They do not yet
prove changed-file retrieval, dependency extraction, CI authority, recommendation,
production readiness, or independent ownership.