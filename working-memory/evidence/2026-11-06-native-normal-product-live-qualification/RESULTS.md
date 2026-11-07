# Single normal-product live qualification: partial, positive adoption deferred

November 6, 2026. [Cycle](../../2026-11-06_native-normal-product-live-qualification_cycle.md), [frozen execution review](../2026-11-06-native-product-execution-readiness/REVIEW.md), [actual observation](attempt-results.json), [task review](TASK_REVIEW.md), [task/native receipts](task-results.json), [verification](verification.json).

## Actual invocation and preserved result

One real invocation used the bound noneditable installation and normal `python -m upgradepilot` caller/signature profile, explicit personal-token mode and exact repo/PR/base/head guards. No authored HTTP adapter, historical source injection, experiment runner, provider prefetch, second attempt or target execution. The launcher used the credential only for the activated child; no credential value or Authorization header is retained in public artifacts.

| Observation | Actual result |
|---|---|
| Repo / PR | `Aidan-Wallace/kubernetes-dashboard-token-api` /20 |
| Base | `b065646e4b7b894964567950f9ad770b02c136c2` |
| Head | `391508134b083b8f54461c0b576e8f7985c6ecb4` |
| Observed dependency transition | HTTPX0.27.2→0.28.1 |
| Process / acquisition / analysis | Exit0 / partial / completed |
| Confirmed and cold-verified revision | `70aa4c795ef54b46ad5f411acb3e5631` |
| Qualified outer invocation |43.8622811host seconds; UTC43.8611023s;160 observations/max gap0.2798909s, no quality problems |
| Physical requests |17 GitHub/19 total;94,625 decoded body bytes |
| Retained source |12 target files; no dependency-source scopes or module receipts |
| Static work |72 facts,3 local target comparisons,76 discovery gaps; no omitted gap diagnostics |
| Selected TestClient / HTTPX witnesses |0 |
| Maintainer action |`abstain`; CI/runtime explicitly `not_evaluated` |

The command's exit0 means it delivered an admitted partial result, not that the requested paired upgrade question was answered. The three comparisons concern local `get_token()` calls; they do not compare HTTPX versions. Fixed projection checks preserve all three witnesses' ordered paths, roles, versions, local outcomes and premises faithfully. The selected `TestClient(app)` call has a retained `callable_relationship_unresolved` gap at tests/test_routes.py L7.

## Why the paired evidence is missing

All17 GitHub requests received200. The only PyPI physical requests were `/pypi/fastapi/json` and `/pypi/pytest/json`; both have no response/status, zero received body bytes and `transport_error`. Typed acquisition problems identify release-index timeouts. Four logical problem entries reuse those two failed index observations; they are not four physical requests. Retry policy is `none`, retry decisions and stop records are empty, and no request allowance is exhausted.

The retained evidence establishes the failure boundary and timeout category. It does **not** establish DNS, TCP/TLS, routing, provider outage, account quota or a specific machine cause. Successful GitHub acquisition does not prove the separate PyPI route works. No retry, fallback auth, larger allowance or lower analyzer repair is justified by this capture alone.

## Recovery, retention and scope

The frozen cold method opens this exact selected revision in a fresh process outside the checkout, with product origins in the bound installation and experiments unavailable. Six forbidden-operation probes discriminate guards against credentials/AST/acquisition/analysis/discovery/synthesis; network is blocked. Exact saved report SHA-256 is `9932eb24aedcbfcc4090cbc252db0884a8e55cf6e19c82bdab9f0c2c03c9c744`. The original selected target source is `source-27`, SHA-256 `54ce091cd5e7ec03d53606f59b713e87ff64a1d6d5922f61be23d97b049393f2`. Recovery does not reconstruct missing library text or rerun producers.

Private intent, exact manifest, stdout/stderr, host observations, SQLite store, report and task/source responses remain below the reserved case root in `product-attempt-01` and `task-review-01`. The public packet carries sanitized outcomes/hashes and native request receipts without headers. All377 frozen execution bindings and121 installed file digests still match after execution; prior packets remain unchanged. Qualified timing encloses this invocation's launch/acquisition/analysis/publication/render/save/exit; it is not human review time, a stage decomposition or a speed comparison with the unrelated raw60-page route. The completed40-minute raw-access limitation remains deferred under AUDIT-015.

## Disposition and next responsibility

**Defer positive native-adoption qualification.** A normal real product invocation, honest partial delivery and exact report/source recovery are demonstrated. The selected useful old/proposed HTTPX pair is absent, so the positive task/adoption gate does not pass. No independent usefulness, untouched transfer, installed/import/dispatch/exercise behavior, compatibility or merge permission is established. Product source/budgets/semantics remain unchanged; previous full-suite results are historical unchanged-source evidence, not fresh test runs.

The justified next responsibility is a bounded PyPI transport diagnosis, starting from these retained failures and the existing environment/transport owners. Freeze any proposed network controls separately before use, then decide whether a separately labelled successor product attempt is justified. Do not rerun this attempt, mutate its grade, enable retries or expand syntax/representation as a substitute for missing acquisition. Runtime/combined-evidence and AI checkpoints keep their existing owners and follow-up gates.
