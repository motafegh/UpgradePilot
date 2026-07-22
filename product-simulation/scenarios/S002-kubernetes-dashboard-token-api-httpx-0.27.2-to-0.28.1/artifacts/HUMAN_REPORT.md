# HTTPX 0.27.2 → 0.28.1

**Repository:** `Aidan-Wallace/kubernetes-dashboard-token-api`  
**Pull request:** `#20`  
**Frozen head:** `391508134b083b8f54461c0b576e8f7985c6ecb4`

## Recommendation

**Run the repository's Python checks on this exact PR head and capture the resolved dependency versions. Merge after normal review only if those checks pass.**

## Why

The repository directly pins HTTPX and its tests construct FastAPI's `TestClient`, which reaches HTTPX through Starlette.

HTTPX 0.28 removed the deprecated `app` constructor argument. Starlette 0.36.3 still passed that argument and would be incompatible. Starlette 0.37.2 removed the call, and FastAPI 0.115.2 requires Starlette 0.37.2 or newer. A then-current FastAPI resolution was therefore likely compatible, but the repository did not lock FastAPI or preserve its exact historical resolution.

The available green GitHub Actions result does not prove the relevant behavior. The successful workflow built the Docker image and installed the shared requirements. It did not run the route tests. The separate Python workflow contains Ruff and `pytest --cov`, but its pull-request path filter excludes `requirements.txt`, so the dependency-only PR did not trigger it.

The historical Docker job logs now return HTTP 410, so the exact installed FastAPI/Starlette versions cannot be recovered publicly.

## Targeted checks

In a trusted isolated checkout of the frozen head:

1. install the frozen requirements;
2. preserve the complete resolved package set;
3. run `ruff check .`;
4. run `pytest --cov`.

## Result transitions

- **Relevant checks pass:** merge after normal review.
- **TestClient initialization or route tests fail because of the HTTPX/Starlette interface:** investigate or block; upgrade FastAPI/Starlette to a fixed line or retain HTTPX below 0.28.
- **Checks are unavailable or inconclusive:** retain the targeted-check/defer state.
- **The head or resolved environment changes:** create a new run or comparison; do not silently reuse this conclusion.

## Limits

This report does not prove complete production safety. No public exact-head Python test result exists, the historical dependency resolution is missing, private maintainer checks are unknown, and static search cannot prove complete absence of dynamic HTTPX use.

## Provenance

Material evidence and lineage are preserved in:

- `EVIDENCE_ITEMS.jsonl`;
- `CLAIMS_AND_INTERPRETATIONS.jsonl`;
- `FINDINGS.json`;
- `DECISION.json`;
- `FOLLOW_UP_STATE.json`.
