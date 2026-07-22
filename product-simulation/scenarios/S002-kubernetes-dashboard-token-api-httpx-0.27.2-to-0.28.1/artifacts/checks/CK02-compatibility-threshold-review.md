# CK02 — FastAPI/Starlette/HTTPX compatibility threshold

**Scenario:** S002  
**Run:** `s002-retrofit-2026-07-22-r1`

## Compared evidence

- HTTPX 0.28.1 tagged changelog;
- FastAPI 0.115.2 tagged `pyproject.toml`;
- Starlette 0.36.3 and 0.37.2 tagged `TestClient` source.

## Direct comparison

- HTTPX 0.28.0 removed the deprecated `app` argument.
- Starlette 0.36.3 passes `app=self.app` to `httpx.Client`.
- Starlette 0.37.2 does not pass `app=`.
- FastAPI 0.115.2 requires `starlette>=0.37.2,<0.41.0` and its standard extra includes `httpx>=0.23.0`.

## Conclusion

An older Starlette branch would be incompatible with HTTPX 0.28.x. A FastAPI 0.115.2-era resolution would select a fixed Starlette branch. The target's exact historical resolution is not preserved, so compatibility is likely but not behaviorally proven.
