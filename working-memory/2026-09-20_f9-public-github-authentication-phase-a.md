# AUDIT-008-F9 — public GitHub authentication boundary, Phase A (2026-09-20)

**Role:** Active bounded F9 working record; `MEMORY.md` alone owns current live selection. Supersedes the F9 handoff portion of `working-memory/2026-09-19_f3-hosted-verification-and-f9-handoff.md`; does not reopen F3.

## Responsibility and limits

Make anonymous public GitHub acquisition deliberate and reproducible while preserving explicitly selected authenticated public access. No new maintainer action, unrelated producer/synthesis change, proxy/networking redesign, general credential manager, or external-target mutation. The current F3 hosted proof is historical for F9; F9 has not been implemented or executable-proven.

## A — pre-implementation orientation and source-supported findings

- `src/upgradepilot/cli.py::main`: `token=os.getenv("GITHUB_TOKEN")` is passed unconditionally to `investigate_public_pull_request(...)`. The CLI currently exposes no explicit auth-mode selection.
- `src/upgradepilot/investigation.py`: the optional token is passed to the GitHub pull-request, actions, and repository clients (inspect remaining GitHub client construction during B preflight).
- `src/upgradepilot/github/api.py::GitHubApiClient`: supplies `Authorization: Bearer ...` whenever a token is provided; otherwise supplies no explicit Authorization header. Requests `Session` handles outgoing calls. Its current HTTP classification maps 404 to `not_found_or_inaccessible`, 403/429 to `forbidden_or_rate_limited`, 401 to `http_error` with status 401, and timeouts to `timeout`.
- `audits/2026-09-19_AUDIT-008_current-system-evidence-to-action-readiness.md` F9 and `ENVIRONMENT.md` §7 document an observed ambient stale/invalid `GITHUB_TOKEN` → authenticated public request → HTTP 401 failure, separate from ambient proxy/TLS trouble.
- Existing `tests/test_github_client.py` exercises no-Authorization-header at the mocked session boundary, but that alone does not prove the actual prepared request is anonymous. `tests/test_cli.py` currently covers rendering/exit behavior rather than deliberate auth selection.
- Requests documentation describes `~/.netrc` / `NETRC` as another ambient authentication source when `Session.trust_env` is enabled, potentially overriding an Authorization header; `trust_env=False` also changes proxy/environment handling. Reference: https://requests.readthedocs.io/en/latest/user/authentication/ and https://requests.readthedocs.io/en/stable/api/. Do not conflate token selection with proof of outgoing anonymity or solve this by casually disabling all ambient networking.

## Proposed smallest contract for B preflight

Default CLI: `upgradepilot owner/repo 123` selects public anonymous mode; explicit `--github-auth token-env` selects use of `GITHUB_TOKEN` only for that invocation and must reject a missing/empty token before acquisition. Never accept the secret value as a command-line argument or display it in help/output/errors. Implement auth selection at CLI plus actual GitHub HTTP request preparation; check `.netrc`/session injection/redirect behavior proportionately while preserving existing proxy handling and explicit authenticated use. The exact requests-layer implementation remains to be confirmed against source and focused tests before mutation; no general credential or transport redesign is authorized.

## Proof and next action

Expected focused tests: default CLI ignores ambient `GITHUB_TOKEN`; explicit token-env loads it; missing explicit token fails without network/secret exposure; real Requests prepared/request-boundary checks reject ambient `.netrc` in anonymous mode and preserve deliberate bearer auth; 401 stays distinguishable from 404 and timeout; existing GitHub/investigation/CLI tests and deterministic suite pass. Hosted manual CI is available for a later exact-revision closure if local executable testing is unavailable. No tests for F9 have run yet.

**Canonical cycle:** A — ACTIVE (core orientation delivered; finish exact session/redirect/adapter and design preflight before B). B — PENDING; C — started by this record, ongoing; D — PENDING; E — PENDING.

**Stop line:** no F9 source/test edit or technical-closure claim during this Phase-A checkpoint; choose bounded implementation only once outgoing anonymous/authenticated request semantics are explicit. F11 remains downstream.
