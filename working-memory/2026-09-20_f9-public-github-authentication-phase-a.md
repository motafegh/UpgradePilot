# AUDIT-008-F9 — public GitHub authentication boundary (2026-09-20)

**Role:** Closed dated F9 working record; `MEMORY.md` alone owns live selection. F3 remains closed; F11 is the next selected responsibility.

## Responsibility and learner orientation

Make ordinary public-PR investigation anonymous by default without requiring the user to remember `env -u GITHUB_TOKEN`; retain deliberately selected authenticated use. `ENVIRONMENT.md` §7 documented the observed stale-token → public GitHub HTTP 401 failure and the process-local `env -u GITHUB_TOKEN` workaround. It separately documents proxy/TLS problems; F9 does **not** fix or reconfigure proxies.

**Learning correction:** the initial technical Phase A explanation assumed familiarity with HTTP, `.netrc` and redirects. Ali explicitly said he did not understand F9. We re-explained it using the existing `env -u GITHUB_TOKEN` public integration command and distinguished token vs proxy issues. Ali recognized that existing workaround, confirmed F9's bounded authentication responsibility, and authorized implementation. Technical preflight or a green CI run alone is not learner-ownership evidence.

## A — DONE: source and design preflight

Before F9, `cli.py::main` unconditionally passed `os.getenv("GITHUB_TOKEN")`; `investigate_public_pull_request` propagated the token to GitHub clients; `GitHubApiClient` added a bearer header and otherwise constructed a regular Requests session. Requests can also add ambient `.netrc` credentials during initial preparation and redirects even with no CLI token. A separate Requests 2.32.5 simulation showed why both initial and redirected requests matter; that experiment was design evidence, not product proof.

Accepted bounded contract: normal CLI anonymous; `--github-auth token-env` explicitly reads `GITHUB_TOKEN`, rejects missing/empty before acquisition, and does not print or accept token values as command-line arguments. Default GitHub Requests session suppresses implicit `.netrc` initially and on redirects, retains cross-origin credential stripping and ordinary environment proxy handling; caller-injected sessions remain caller-owned. Keep 401/404/timeout distinctions; no general credential manager, proxy redesign, changed evidence semantics, or external-target mutation.

## B — DONE: implementation and exact-revision executable proof

- `src/upgradepilot/cli.py`: `--github-auth {anonymous,token-env}`, anonymous default; reads the variable only in explicit mode; missing/empty token returns exit 2 before investigation without disclosing the secret.
- `src/upgradepilot/github/auth_session.py` (new): `GitHubPublicSession` uses no-op `AuthBase` against initial `.netrc` insertion and avoids redirect re-insertion; strips supplied bearer when origin changes, retains `trust_env=True`.
- `src/upgradepilot/github/api.py`: default session is `GitHubPublicSession`, preserving explicitly injected sessions and existing HTTP error handling. A transient omission of `import requests` and unrelated array-error wording was corrected at `b2644040e1958927a2cb84c410dc1e08f3c45be4` before validation.
- `tests/test_github_authentication.py` (new): eight focused tests spanning default anonymity, explicit token, missing/empty token, help/non-disclosure, Requests prepared/redirected request under synthetic `.netrc`, bearer preservation/stripping, injected session, and 401/404/timeout distinctions.
- `README.md`: quickstart documents anonymous default and explicit token opt-in. No proxy, investigation or maintainer-action logic changed.

**Scope review:** pre-F9 `fcdbc4a200d17958571dd2438311c1ab84ee1ec1` to implementation/docs `8e7a589e48805624ae445ecc7f116be6d99cedf3` changes only README, CLI, GitHub API, new auth session and new tests; work committed to `main`.

**Exact hosted proof:** Ali dispatched [Product verification run #7](https://github.com/motafegh/UpgradePilot/actions/runs/35516933780), ID `35516933780`, attempt 1, `workflow_dispatch`, success on 2026-09-20. Checkout and logged HEAD `2afc566a4ce2139f3439d6a4c3cf9596896b3841` contain F9 source/tests and README. Ubuntu 24.04.5, Python 3.12.14, installed Requests 2.34.2; fresh package install, `pip check` and both installed CLI help entry points PASS; focused investigation **15/15 PASS**; full deterministic product suite **616/616 PASS**, including the **8/8 F9 authentication cases**. F3's prior 608/608 run tested a different revision.

**Proof limits:** controlled authentication/request/redirect evidence does not prove a live public PR, real token or rate-limit outcome, arbitrary proxy environment, model quality, or any new maintainer-action permission. No additional F9 code repair is indicated at the selected bounded proof horizon.

## C — DONE: progress preservation

Exact source revisions, test outcome, environment and proof limits are retained above; `MEMORY.md` updated at the implementation, verification and closure milestones.

## D — DONE: post-implementation learning and ownership check

Teaching began from Ali's familiar `env -u GITHUB_TOKEN` workaround: the old ordinary command could automatically use an expired shell token; the new ordinary command selects anonymous GitHub access, with `--github-auth token-env` as the deliberate opt-in. In a changed-case check, Ali was asked whether an expired ambient `GITHUB_TOKEN` would be used by `upgradepilot pydantic/pydantic 13432` without the option, and why. He correctly answered that it would **not** be used unless explicitly requested. This establishes the bounded user-facing configuration distinction, not detailed independent ownership of Requests redirect internals; those remain lookup-level until required by future work.

## E — DONE: closure and next-slice orientation

No material gap appeared in the selected ownership check, and the installed-product deterministic proof passed. **F9 CLOSED for its bounded authentication contract and learning slice.** No live GitHub/proxy success or broader action claim is inferred. The next plan slice is **AUDIT-008-F11 — audit/live-state lifecycle reconciliation**: align AUDIT-005's lifecycle classification and audit indexes with the current project route, preserving its valid evidence without treating it as a competing active engineering responsibility. F11 does not authorize new product source changes or revive agentic orchestration.
