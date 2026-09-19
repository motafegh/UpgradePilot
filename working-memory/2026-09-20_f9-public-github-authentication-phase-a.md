# AUDIT-008-F9 — public GitHub authentication boundary (2026-09-20)

**Role:** Active bounded F9 working record; `MEMORY.md` alone owns current live selection. Supersedes the F9 handoff portion of `working-memory/2026-09-19_f3-hosted-verification-and-f9-handoff.md`; does not reopen F3.

## Responsibility and limits

Make anonymous public GitHub acquisition deliberate and reproducible while preserving explicitly selected authenticated public access. No new maintainer action, unrelated producer/synthesis change, proxy/networking redesign, general credential manager, or external-target mutation. The F3 hosted proof is historical for F9; F9 has not been implemented or executable-proven.

## A — pre-implementation orientation and verified design findings: DONE

- `src/upgradepilot/cli.py::main` currently passes `token=os.getenv("GITHUB_TOKEN")` unconditionally. No CLI auth selector exists. `investigate_public_pull_request` passes its optional token into GitHub pull-request, actions, repository and other relevant GitHub client creation; the shared `GitHubApiClient` adds `Authorization: Bearer ...` if supplied. `GitHubApiClient` currently constructs an ordinary Requests `Session` unless a session is injected.
- F9 audit and `ENVIRONMENT.md` §7 document actual stale ambient token → authenticated public request → HTTP 401; ambient proxy/TLS failures are separate. Current 401 has `http_error` reason and 401 status, while 404 is `not_found_or_inaccessible`, 403/429 are `forbidden_or_rate_limited`, and timeout is `timeout`.
- Default Requests sessions can read `.netrc`/`NETRC` and apply authorization even without an explicit token. The basic first-request check `session.auth = NoOpAuth()` suppresses that injection at `Session.prepare_request`, but **does not prevent `Session.rebuild_auth` from inserting `.netrc` authorization on redirects** while `trust_env=True`. Inspectable sources: Requests `Session.prepare_request` and `Session.rebuild_auth` in the installed Requests 2.32.5 source, and https://requests.readthedocs.io/en/latest/user/authentication/. This is a real design issue rather than proof that current public cases actually redirected.
- An isolated local Requests 2.32.5 prototype, with simulated ambient credentials and no network, confirmed the initial/redirect issue; a narrowly scoped `Session` variant with no-op auth and redirect re-auth prevention preserved anonymous initial and redirected requests, retained explicit bearer headers, stripped bearer auth on cross-host redirects, and left `trust_env=True`. **These prototype checks are not UpgradePilot implementation or executable product proof**. Recheck exact behavior under the installed product dependency version.
- `tests/test_github_client.py` currently checks no Authorization passed as mocked `Session.get` header but cannot establish the true prepared-request boundary. `tests/test_cli.py` covers presentation/error exits, not explicit CLI auth choice. `SECURITY.md` requires deliberate credential use and no secret disclosure.

## Selected bounded design for implementation preflight

- CLI default is anonymous; an explicit `--github-auth token-env` opts in to `GITHUB_TOKEN` for that invocation only. Missing/empty explicit token must be rejected before acquisition; never put the secret on the command line, in help, outputs, or errors. Avoid reading the ambient token in default mode.
- Outgoing GitHub requests must not inherit `.netrc` auth during initial preparation or redirects. Prefer a narrowly scoped GitHub-owned Requests-session boundary: a no-op `AuthBase` to prevent initial ambient `.netrc`, plus redirect-auth handling that **retains Requests cross-host credential stripping** but does not reintroduce `.netrc`. Preserve `trust_env=True` and existing proxy/environment transport behavior rather than using `trust_env=False` as a blanket fix. The default production GitHub client must use this controlled session; an explicitly injected custom/mock session remains an explicit caller/test seam, not evidence about default production transport.
- Keep `investigate_public_pull_request`'s existing explicit `token` injection path and domain/evidence semantics. Retain 401 as an operational HTTP acquisition error distinct from 404/missing evidence and timeout; evaluate a more specific reason only if needed for clarity, without treating authentication failure as semantic abstention. Redirect behavior outside credential safety must not be broadened without evidence.

## B / C / D / E and proof

B — NEXT: implement the selected CLI selection and GitHub-owned session boundary, add focused tests for anonymous-with-ambient-token, explicit token-env/missing-token, genuine Requests prepared request and redirect behavior, bearer preservation/credential stripping, non-disclosure and failure classification. Inspect exact source and diff before mutation; test narrow-to-broad. If the exact Requests version or GitHub session injection contract exposes a contradiction, return to the relevant design owner before expanding scope.

C — ACTIVE: preserve implementation revisions, tests and any execution blocker here. Update `MEMORY.md` when the live phase/milestone changes. Manual `Product verification` CI is available for exact-revision hosted installed-product closure when needed; historical 608/608 is F3 proof only.

D — PENDING: teach the actual implemented source/control flow, planned versus observed behavior, proof limits; perform a small ownership check with Ali.

E — PENDING: repair relevant gaps, close F9 only on sufficient proof, orient F11 audit lifecycle reconciliation next.

**Stop line:** no F9 product mutation or test pass is claimed in this Phase-A record. No proxy redesign, credential manager, CLI synthesis action, or external target mutation. F11 remains downstream.
