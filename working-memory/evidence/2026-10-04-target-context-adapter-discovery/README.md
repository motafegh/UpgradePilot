# Exact target context and adapter exploration — partial live proof

Date: 2026-10-04 (Asia/Tehran). This increment has local deterministic proof plus an initial ordinary PR run and a later component replay. A corrected full ordinary run is still pending. No model, target installation, actual resolution, compatibility, maintainer utility or product adoption is established.

Reproduce the full acquisition when capacity/authentication permits:

```sh
PYTHONPATH=src .venv/bin/python -m experiments.api_target_context_smoke Aidan-Wallace/kubernetes-dashboard-token-api 20
# Only with explicitly configured, valid GITHUB_TOKEN:
PYTHONPATH=src .venv/bin/python -m experiments.api_target_context_smoke Aidan-Wallace/kubernetes-dashboard-token-api 20 --github-auth token-env
```

The runner accepts repository/PR identity, not target paths, adapter names, versions or interpretations. All default providers share one per-run 50-request cap. Exact target requirements/calls precede generic adapter exploration. Latest stable satisfying constraints is a labelled exploration choice, never resolved target state. No ambient authentication is inherited in anonymous mode.

## Retained attempts

- `live-initial.json`: anonymous ordinary PR execution, 37 GitHub requests. Base/head match the archived development case. The target tree independently supplied 12 eligible files, including the TestClient call. Raw `fastapi[standard]`, exact changed HTTPX declaration and other requirements are retained. Both HTTPX crossed sections were acquired. Initial adapter samples reached FastAPI's Starlette re-export, then a combined product-resolver metadata-link result was incorrectly used as a pure publisher verdict. This run predates the corrected independent provenance inspection and refined release/file budgets; it is not a final acceptance run.
- `live-corrected.json`: explicit token-env attempt failed on the first PR request with HTTP 401. It contains no token value. Anonymous access was subsequently confirmed; configured authentication failure is separate from source absence. No `gh` executable or repository `.env` was available for an already-configured profile fallback; no credential was replaced or exposed.
- `live-adapter-replay.json`: fresh anonymous adapter reads, seeded only by producer facts from `live-initial.json`, whose hash is recorded. This is a **component replay**, not a fresh full PR path. It independently acquired FastAPI re-export modules and Starlette's TestClient module from exact sampled versions/commits. Conditional `httpx`/`httpx2` imports remain unresolved lexical bindings. Some later dependency reads encountered rate-limit/forbidden results; omitted candidates and errors remain visible. Sample versions are not the historical target's installed versions. The source/probe code hashes identify that attempt; later input-byte-bound, inventory-stream-bound and diagnostic-only changes are tested locally but not retrospectively claimed as freshly live-verified.

A replay can be reproduced from the retained target record, with its proof class kept distinct:

```sh
PYTHONPATH=src .venv/bin/python -m experiments.api_adapter_context_replay working-memory/evidence/2026-10-04-target-context-adapter-discovery/live-initial.json
```

Records contain source locations, method/input identities, hashes and static observations rather than complete raw archives. Public source is recoverable by immutable commit/path where available. Registry metadata remains mutable; its scoped declarations and response identity do not attest historical build origin. Complete third-party source files are not redistributed; retained static records include short import/reference expressions and dependency declarations.

## Local proof and outstanding gate

The focused active trial suite passes 37 tests: source/window/provenance/auth boundaries, inventory/AST/declarations, adapter constraints/caching/budgets, ordinary PR composition and replay source correspondence. Full checkout product regression passes 743 tests; product source/tests remain unchanged. Ruff/format and pip check pass. Historical unrelated experiment suites were not repaired or claimed green; no new fresh-installed wheel/model test was run for this isolated experiment increment.

The corrected full ordinary run must be executed after valid explicit authentication or anonymous quota recovery. Fresh comparison must preserve these failed/partial attempts rather than overwrite them. Acquisition evidence is not semantic API-impact or utility acceptance. `verification.json` records final local source/test hashes and the proof debt.
