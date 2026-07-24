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
python -m unittest discover -s tests -v
```

These tests establish only the behavior they execute. They do not yet prove live-network
acquisition, changed-file retrieval, CI authority, dependency extraction, recommendation,
or production readiness.
