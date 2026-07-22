# S002 — HTTPX 0.27.2 → 0.28.1

**Repository:** `Aidan-Wallace/kubernetes-dashboard-token-api`  
**Public event:** PR `#20`  
**Frozen head:** `391508134b083b8f54461c0b576e8f7985c6ecb4`  
**Narrative status:** Complete  
**Artifact-lifecycle status:** Complete retrospective reconstruction  
**Ali review:** Pending  
**Manual outcome:** Run targeted checks; merge only if exact-head Python checks pass under a captured dependency resolution

## Records

- [`CASE.md`](CASE.md) — complete human-auditable investigation, retrofit disclosure, baseline comparison, decision construction, review state, and completion audit.
- [`artifacts/RUN_MANIFEST.json`](artifacts/RUN_MANIFEST.json) — run index, reconstruction status, artifact inventory, preservation limits, and validation result.
- [`artifacts/`](artifacts/) — machine-state, evidence, findings, decision, reports, follow-up, raw captures, and checks.

## Key result

HTTPX reaches the repository through FastAPI/Starlette `TestClient`. HTTPX 0.28 removed the `app` argument used by old Starlette versions, while Starlette 0.37.2 and FastAPI 0.115.2 establish that a fixed branch existed.

The public green workflow built the image and installed dependencies only. The Python workflow containing Ruff and pytest excluded `requirements.txt`, so the relevant tests did not run. Historical job logs now return HTTP 410, leaving the exact resolved FastAPI/Starlette environment unavailable.

## Required follow-up

In a trusted isolated checkout of the frozen head:

1. preserve the resolved package set;
2. run `ruff check .`;
3. run `pytest --cov`.

Pass → merge after normal review. Relevant failure → investigate/block. Unavailable or inconclusive → retain targeted-check/defer state. Changed head or resolution → create a new run or comparison.

## Retrofit boundary

The artifact bundle was created after the original investigation. It does not claim that historical JSON artifacts or progressive artifact commits existed at that time. Missing operation timestamps, expired logs, and the unavailable historical resolver state remain explicit.
