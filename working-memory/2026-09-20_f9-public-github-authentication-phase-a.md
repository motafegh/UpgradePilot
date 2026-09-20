# AUDIT-008-F9 — public GitHub authentication boundary (2026-09-20)

**Role:** Active dated F9 working memory; `MEMORY.md` alone owns live selection. F3 remains closed; F11 remains downstream.

## Responsibility and learner orientation

Make ordinary public-PR investigation anonymous by default without requiring the user to remember `env -u GITHUB_TOKEN`; retain deliberate authenticated use. `ENVIRONMENT.md` §7 documented the concrete observed stale-token → public GitHub HTTP 401 failure and the process-local `env -u GITHUB_TOKEN` workaround. It separately documents proxy/TLS problems; F9 does **not** fix or reconfigure proxies.

**Learning correction:** the initial technical Phase A explanation assumed familiarity with HTTP, `.netrc` and redirects. Ali explicitly said he did not understand F9. We re-explained it using the existing `env -u GITHUB_TOKEN` public integration command and distinguished token vs proxy issues. Ali recognized the concrete existing workaround, confirmed that F9 is only fixing this authentication behavior, and authorized implementation. A technical source preflight alone does not establish learner understanding; D must start from the actual simple CLI change before discussing Requests internals.

## A — DONE: source and design preflight

Prior implementation: `cli.py::main` unconditionally passed `os.getenv("GITHUB_TOKEN")`; `investigate_public_pull_request` propagated explicit token to GitHub clients; `GitHubApiClient` added bearer header and otherwise constructed a regular Requests session. Requests can also add ambient `.netrc` credentials during initial preparation and redirects, even if no CLI token was passed. An isolated Requests 2.32.5 experiment showed that a no-op session auth prevents initial `.netrc` use but redirect auth must also be controlled. A narrowly scoped session preserving cross-host bearer stripping and `trust_env=True` passed the isolated experiment. This is not product execution proof.

Chosen contract: normal CLI is anonymous; `--github-auth token-env` explicitly reads `GITHUB_TOKEN`, rejects missing/empty before acquisition, never prints or accepts the secret as an argument. Default GitHub Requests session suppresses implicit `.netrc` on initial and redirected requests, retains cross-origin credential stripping and ordinary proxy/environment transport. Explicitly injected custom sessions remain caller-owned test seams. Retain existing 401/404/timeout classification; no action semantics, unrelated evidence producers, general credential manager, or proxy redesign.

## B — source/test implementation committed; executable proof pending

- `src/upgradepilot/cli.py`: added `--github-auth {anonymous,token-env}`, default anonymous; read `GITHUB_TOKEN` only in explicit mode; missing token returns exit 2 before investigation without secret disclosure.
- `src/upgradepilot/github/auth_session.py` (new): `GitHubPublicSession` uses a no-op `AuthBase` to prevent implicit `.netrc` during initial request preparation, and overrides redirect authentication to strip existing bearer on origin change without reloading `.netrc`. `trust_env=True` remains unchanged.
- `src/upgradepilot/github/api.py`: only default session construction changes to `GitHubPublicSession`; caller-injected sessions and existing HTTP error categories remain. A transient edit accidentally omitted `import requests` and altered one array-error word; both were corrected in commit `b2644040e1958927a2cb84c410dc1e08f3c45be4` before validation.
- `tests/test_github_authentication.py` (new): eight focused tests for default token ignorance, deliberate token selection, missing/empty token/no acquisition, help contract, real Requests prepared/redirected request with synthetic `.netrc`, explicit bearer preservation/stripping, default-vs-injected session, and 401/404/timeout distinction.
- `README.md`: quickstart and CLI contract now show anonymous default and explicit token-env opt-in. No proxy or investigation logic changed.

**Scope review:** GitHub commit comparison from pre-F9 `fcdbc4a200d17958571dd2438311c1ab84ee1ec1` to implementation/docs commit `8e7a589e48805624ae445ecc7f116be6d99cedf3` shows only README, CLI, GitHub API, new auth session, and new tests changed; the original large CLI/README bodies were retained. All source/test updates are on `main` as authorized.

**Proof status:** No UpgradePilot F9 repository test suite or manual CI run has been executed for this revision. A separate local Requests 2.32.5 simulation of the selected session behavior passed anonymous/explicit/same-origin/cross-origin checks with mocked ambient `.netrc`, but it is not an installed-product test. Prior F3 hosted 608/608 run predates F9 and cannot close it. GitHub connector cannot dispatch the `Product verification` workflow and this assistant container cannot clone GitHub (DNS unavailable). The next executable proof is a manual Product verification run on the exact current F9 `main` revision; inspect its checkout SHA, installed CLI, focused investigations and full deterministic suite. Repair demonstrated failures; do not label F9 technically closed on authored tests or a design prototype alone.

## C / D / E

C — ONGOING: source/test milestone and proof debt preserved here. Keep `MEMORY.md` consistent with B source-complete / executable-validation pending.

D — PENDING: teach from the actual code, beginning with the familiar `env -u GITHUB_TOKEN` workaround and the new CLI choice; then trace only necessary HTTP-session behavior and ask one concrete changed-case reasoning question. Separate source review from executable proof and learner ownership.

E — PENDING: repair any important learner or test gap, close F9 only after required exact-revision validation, then orient F11 audit lifecycle reconciliation.

**Stop line:** F9 remains implemented/source-reviewed but proof-pending. No general credential/proxy redesign, new maintainer-action permission, unrelated product change, or F11 implementation before the F9 closure conditions are satisfied.
