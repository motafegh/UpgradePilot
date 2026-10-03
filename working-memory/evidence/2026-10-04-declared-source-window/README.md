# Declared source-window acquisition — bounded evidence

Date: 2026-10-04 (Asia/Tehran). This proves the first trial source component, not ordinary PR-to-target exposure, API meaning, compatibility or action permission.

Reproduce from repository root:

```sh
PYTHONPATH=src .venv/bin/python -m experiments.api_change_source_smoke httpx 0.27.2 0.28.1
PYTHONPATH=src .venv/bin/python -m unittest experiments.tests.test_api_change_source_acquisition -q
PYTHONPATH=src .venv/bin/python -m unittest discover -s tests -q
```

- `live-result-initial.json`: initial exact-heading-only selection failed on dated HTTPX headings after five GitHub requests. Source acquisition reached the actual file; no window was accepted. It used the pre-existing installed providers.
- `live-result-installed-provider.json`: corrected calendar-date grammar acquired both sections, still using the old installed provider tree. Retained separately after the installed-versus-checkout discrepancy was found.
- `live-result.json`: final acquisition with explicit checkout imports and component SHA256, exact source URLs/commit/path, UTF-8 hashes, character offsets/line numbers and limits. Anonymous reads, no token, model or target execution. Section text is exactly recoverable from the pinned source if retrieval remains available; no claim of offline raw replay. Existing retained planning excerpts/license are available in [earlier evidence](../2026-10-03-api-impact-design/README.md).

Declared repository basis remains weaker than publisher provenance. PyPI exact-release metadata is mutable; retained URLs/time/results scope this observation rather than cryptographically attesting its history. Tag source identity is pinned after resolution. The result discloses its exact-heading/calendar-date grammar and ignored release keys; it does not cover arbitrary release-document formats.

Checks: 11 focused trial tests (with adversarial subcases), 743 current-checkout product tests, touched Ruff checks/format and diff whitespace. The initial default-interpreter product run tested an old installed package and failed seven subcases plus one error in the already repaired marker family; this was an installation freshness problem, not a checkout regression. Local installed package refresh/checks are recorded in the cycle. Full historical experiment regression is not claimed; its previously recorded unrelated failures remain outside this component.
