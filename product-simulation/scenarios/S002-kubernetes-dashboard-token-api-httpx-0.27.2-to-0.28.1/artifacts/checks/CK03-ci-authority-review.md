# CK03 — CI authority review

**Scenario:** S002  
**Run:** `s002-retrofit-2026-07-22-r1`  
**Frozen head:** `391508134b083b8f54461c0b576e8f7985c6ecb4`

## Docker workflow

- triggers for pull requests to `main`;
- builds the repository Dockerfile;
- the Dockerfile installs `requirements.txt`;
- no test or application-start command is present;
- run `15940060582` and job `44966848674` succeeded.

## Python workflow

- contains `ruff check .`;
- contains `pytest --cov`;
- pull-request path filters include only `app/**`, `static/**`, `templates/**`, and `tests/**`;
- `requirements.txt` is excluded;
- no Python workflow run was observed for the frozen head.

## Log retention

Job-log retrieval for job `44966848674` returned HTTP 410.

## Conclusion

The green Docker result proves that one dependency resolution installed and the image built. It does not prove `TestClient` initialization or route-test behavior. The relevant Python checks were skipped by trigger configuration, and the exact tested dependency environment is no longer recoverable.
