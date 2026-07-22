# CK01 — Static relevance review

**Scenario:** S002  
**Run:** `s002-retrofit-2026-07-22-r1`  
**Frozen head:** `391508134b083b8f54461c0b576e8f7985c6ecb4`  
**Execution:** Retrospective manual comparison of re-acquired exact-head files.

## Inputs

- `requirements.txt` at base and head;
- `tests/test_routes.py` at head;
- repository-wide GitHub code search for `httpx`;
- `readme.md`;
- `Dockerfile`.

## Direct results

- HTTPX is directly pinned in `requirements.txt`.
- `fastapi[standard]` is unpinned in the same file.
- `tests/test_routes.py` imports FastAPI `TestClient` and constructs `TestClient(app)`.
- The code search returned only `requirements.txt`; no direct application-source HTTPX import was observed.
- The Dockerfile installs the shared requirements file into the production image.
- The README explicitly notes that pytest and Ruff should not be installed in the container.

## Conclusion

HTTPX has multiple simultaneous roles:

1. directly declared;
2. functionally reached through the test framework;
3. not directly observed in application source;
4. installed in the production image.

This is static evidence. It does not prove complete dynamic absence from application behavior.
