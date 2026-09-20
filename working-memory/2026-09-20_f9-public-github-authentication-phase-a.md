# AUDIT-008-F9 — public GitHub authentication boundary (2026-09-20)

**Role:** Active dated F9 working memory; `MEMORY.md` alone owns live selection. F3 remains closed; F11 remains downstream.

## Responsibility and learner orientation

Make ordinary public-PR investigation anonymous by default without requiring the user to remember `env -u GITHUB_TOKEN`; retain deliberate authenticated use. `ENVIRONMENT.md` §7 documented the observed stale-token → public GitHub HTTP 401 failure and the process-local `env -u GITHUB_TOKEN` workaround. It separately documents proxy/TLS problems; F9 does **not** fix or reconfigure proxies.

**Learning correction:** the initial technical Phase A explanation assumed familiarity with HTTP, `.netrc` and redirects. Ali explicitly said he did not understand F9. We re-explained it using the existing `env -u GITHUB_TOKEN` public integration command and distinguished token vs proxy issues. Ali recognized the concrete existing workaround, confirmed that F9 is only fixing this authentication behavior, and authorized implementation. Technical preflight does not establish learner ownership; D must begin with the actual simple CLI change before introducing internal details.

## A — DONE: source and design preflight

Prior implementation: `cli.py::main` unconditionally passed `os.getenv("GITHUB_TOKEN")`; `investigate_public_pull_request` propagated explicit token to GitHub clients; `GitHubApiClient` added bearer header and otherwise constructed a regular Requests session. Requests can also add ambient `.netrc` credentials during initial preparation and redirects, even if no CLI token was passed. An isolated Requests 2.32.5 experiment established that no-op session auth prevents initial `.netrc` use but redirect auth must also be controlled. A narrowly scoped session preserving cross-host bearer stripping and `trust_env=True` passed the isolated experiment. That experiment was design evidence, not UpgradePilot product proof.

Chosen contract: normal CLI is anonymous; `--github-auth token-env` explicitly reads `GITHUB_TOKEN`, rejects missing/empty before acquisition, never prints or accepts secret as a command-line argument. Default GitHub Requests session suppresses implicit `.netrc` on initial and redirected requests, retains cross-origin credential stripping and ordinary proxy/environment transport. Explicitly injected custom sessions remain caller-owned test seams. Retain existing 401/404/timeout classification; no action semantics, unrelated evidence producers, general credential manager, or proxy redesign.

## B — DONE: implementation and exact-revision executable proof

- `src/upgradepilot/cli.py`: added `--github-auth {anonymous,token-env}`, default anonymous; read `GITHUB_TOKEN` only in explicit mode; missing/empty token returns exit 2 before investigation without secret disclosure.
- `src/upgradepilot/github/auth_session.py` (new): `GitHubPublicSession` uses a no-op `AuthBase` to prevent implicit `.netrc` during initial request preparation; redirect handling strips existing bearer on origin change without reloading `.netrc`. `trust_env=True` remains unchanged.
- `src/upgradepilot/github/api.py`: default session construction changes to `GitHubPublicSession`; caller-injected sessions and HTTP error categories remain. A transient edit accidentally omitted `import requests` and altered one array-error word; both were corrected in commit `b2644040e1958927a2cb84c410dc1e08f3c45be4` before validation.
- `tests/test_github_authentication.py` (new): eight focused tests for default token ignorance, deliberate token selection, missing/empty token/no acquisition, help contract, Requests prepared/redirected request with synthetic `.netrc`, bearer preservation/stripping, default-vs-injected session, and 401/404/timeout distinction.
- `README.md`: quickstart and CLI contract show anonymous default and explicit token-env opt-in. No proxy or investigation logic changed.

**Scope review:** comparison of pre-F9 `fcdbc4a200d17958571dd2438311c1ab84ee1ec1` and implementation/docs `8e7a589e48805624ae445ecc7f116be6d99cedf3` shows only README, CLI, GitHub API, new auth session, and new tests changed. All updates are on `main`.

**Exact hosted proof:** Ali dispatched the existing manual `Product verification` workflow. [Run #7](https://github.com/motafegh/UpgradePilot/actions/runs/35516933780), ID `35516933780`, attempt 1, `workflow_dispatch`, completed **success** on 2026-09-20. Checkout and logged `git rev-parse HEAD` equal `2afc566a4ce2139f3439d6a4c3cf9596896b3841`, containing the F9 source/tests and README. Ubuntu 24.04.5, Python 3.12.14; installed `requests==2.34.2` (the prototype used 2.32.5). Fresh package install and `pip check` PASS, both installed CLI help entry points PASS (help shows anonymous default and token-env opt-in), focused investigation **15/15 PASS**, full deterministic product suite **616/616 PASS**. The eight F9 tests in `test_github_authentication.py` each show `ok` in the full-suite job log. No failure or repair was indicated. The prior F3 run `35465839476` tested a different revision and is not this proof.

**Proof limits:** the eight F9 cases use controlled ambient-credential/request/redirect conditions; the workflow does not conduct a live public-PR acquisition, real-token acceptance, a live proxy diagnosis, or a model evaluation. Green deterministic tests support the bounded F9 implementation contract on this installed revision, not universal network success or new maintainer-action permissions. This validated source does not require a further F9 code change on current evidence.

## C / D / E

C — DONE for source and hosted proof: exact revision, workflow run, environment, tests, limitations and design/proof distinction preserved above. Update `MEMORY.md` with verified F9 and D/E remaining.

D — NEXT: teach Ali the actual implemented flow beginning with the familiar `env -u GITHUB_TOKEN` workaround and new CLI choice, then only if useful the HTTP-session behavior. Ask one concrete changed-case reasoning question; green tests do not prove learner ownership.

E — PENDING: repair the material learning gap if any, then close F9 at its bounded proof horizon and orient F11 audit lifecycle reconciliation. Do not infer other action permissions or proxy correctness from this CI run.

**Stop line:** F9 implementation and deterministic hosted verification are complete; learning/ownership D/E remain before overall F9 closure and F11. No general credential/proxy redesign, unrelated product change, or external-target mutation.