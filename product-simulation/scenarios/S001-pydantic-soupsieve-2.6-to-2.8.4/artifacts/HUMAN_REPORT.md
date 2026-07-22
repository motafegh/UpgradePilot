# UpgradePilot manual report — Pydantic PR #13432

**Repository:** `pydantic/pydantic`  
**Head revision:** `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a`  
**Update:** Soup Sieve `2.6` → `2.8.4`  
**Exact change:** one `uv.lock` package record  
**Recommended action:** **Merge after normal maintainer review**

## Why

Soup Sieve is transitive documentation tooling rather than a published Pydantic
runtime dependency. The relevant path is:

```text
docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve
```

The interpreter change is compatible with declared support: Pydantic requires
Python `>=3.10`; Soup Sieve 2.8.4 requires Python `>=3.9`.

Two reviewed high-severity denial-of-service advisories affect Soup Sieve 2.6
and identify 2.8.4 as patched. The inspected Pydantic plugin uses Beautiful Soup
for HTML parsing and tree traversal but did not directly call `.select()`,
`.select_one()`, or `soupsieve.compile()` in the bounded inspected path. That
limits the exploitability claim but does not prove complete non-exposure.

The proposed lock hashes align with the official PyPI 2.8.4 release. Exact-head
documentation CI installed the `docs` group containing Soup Sieve and completed
the MkDocs build successfully.

## Important limitations

- Exact Dependabot trigger is unresolved.
- Complete indirect selector use and private production inputs were not proven.
- Credentialed post-merge Algolia upload result was not retrieved.
- No independent local target execution was performed.
- This retrospective reconstruction cannot recover every original raw connector
  payload or per-operation timestamp.

## Maintainer action

Perform normal human review and merge unless repository knowledge reveals an
undocumented interpreter, deployment, or selector-input constraint.

A changed head SHA or materially new evidence requires a new run.

## Provenance

- PR: https://github.com/pydantic/pydantic/pull/13432
- `artifacts/CASE_IDENTITY.json`
- `artifacts/EVIDENCE_ITEMS.jsonl`
- `artifacts/FINDINGS.json`
- `artifacts/DECISION.json`
- `artifacts/RUN_MANIFEST.json`

This report does not claim objective safety, non-exploitability, or production
proof.
