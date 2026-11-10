# Targeted-check feasibility on an open HTTPX upgrade

Ali selected the [Aruba handoff](2026-11-09_aruba-maintainer-decision_comparison-cycle.md#next-responsibility-and-stop-line) to review one exact-version case. Reconciled `main` and `origin/main` at `3f105401`. The [maintainer utility plan](../plans/PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md#task-first-reassessment-after-delivered-reports) owns the task-first sequence. The [action specification](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md#72-run-targeted-checks) requires a specific feasible check whose result would change the next step. The [qldebugger simulation](../product-simulation/scenarios/S006-qldebugger-pydantic-validator-coverage-gap/README.md) illustrates how a same-input old/proposed comparison could discriminate. Its range update and controlled omission limit what it proves about normal product admission.

UP-SKILL:upgradepilot-repository-audit. UP-SKILL:upgradepilot-working-memory.

## Candidate selection

Prefer an open PR with a single exact change that the product admits, an upstream behavior change with a concrete failure mechanism, and a target call plus a relevant test entry. Historical qldebugger, Cactus and Freqtrade material did not supply that combination. Public GitHub title searches were discovery only. The initial Dependabot-author queries yielded no candidates, so the broader search used open PR titles and exact upgrade terms. Focused on HTTPX 0.28 because upstream identifies a precise removed argument, and prioritized visible FastAPI test paths over title-only matches. This was a small purposive screen, with no estimate of how common the mechanism is.

| Candidate | Selection or exclusion |
| --- | --- |
| [pedido-service #10](https://github.com/cauerkarsten/pedido-service/pull/10) | Selected for one current-owner CI probe. A single `requirements-dev.txt` pin change, an exact-head workflow that directly installs that file, and a visible `TestClient(app)` in a pytest module give the clearest connection between the change and a possible check. |
| [mlops-iris #11](https://github.com/sanskrutishah14/mlops-iris/pull/11) | Reserve screen. The same exact pin change and a `TestClient(app)` call are visible, while CI installs `requirements-dev.txt` and the changed pin lives in `requirements.txt`. The declared FastAPI 0.115.4 separately requires [Starlette `>=0.40.0,<0.42.0`](https://github.com/fastapi/fastapi/blob/0.115.4/pyproject.toml#L42). No second product CI probe. |
| [fastapi-realworld-practice #7](https://github.com/AndreiPiterbarg/fastapi-realworld-practice/pull/7) | Screened out. The changed declaration is a Poetry caret range with a lockfile, outside the selected single exact-pin admission. |

Seven raw GitHub file requests failed during TLS. Exact-revision Contents API reads recovered those same files without changing transport settings or using credentials. Historical discovery and reserve screening are separate from the product probe below.

## Exact selected case and existing owner result

- Repository and PR `cauerkarsten/pedido-service#10`, open at observation. Base `dbb134f810d7eeab70fa9209bf66d3d05badd29a`. Head `4dbfdac075d4c13889f39fae44432593e6b4c78a`.
- `acquire_dependency_inputs` required both revisions and admitted `httpx 0.27.2 → 0.28.1` in `requirements-dev.txt`, the sole changed file. The GitHub files response SHA-256 was `0aef359a70b7321ff8afa0099993d7bedc755ac58da1e18e067743cd4a03feca`.
- `prepare_ci_evidence` bound [run `41820605942`, attempt `1`](https://github.com/cauerkarsten/pedido-service/actions/runs/41820605942/attempts/1) to that head. The exact workflow source and runtime job steps yielded `supported_runtime_correlated`. Static job `testes`, step index 2, command `pip install -r requirements-dev.txt`, correlated with successful runtime step 4. The attempt jobs response SHA-256 was `c752c8915aa17088292a9b66cbd0a778ee6b2c3d4fc55b6c7be7850a1b4dd1e8`.
- The product CI projection and renderer preserved `runtime direct exercise correlation: not_established`. The observed job conclusion was `success`. The YAML declares pytest, and the coverage owner did not establish a direct HTTPX invocation. The command-completion package-state owner evaluated one candidate and returned `unresolved` at `manager_environment`. The result establishes successful execution of the install command. Effective package state, test-level execution, and actual dispatch remain separate questions.
- The probe made seven anonymous GitHub API GETs, all HTTP 200, under an eight-request local cap. It called the current dependency and CI preparation owners and the shared CI projection/renderer directly. Raw API responses were not retained. This was a read-only owner probe, with no full Workspace investigation or target-code execution.

## Does this case warrant a focused check?

The [target test](https://github.com/cauerkarsten/pedido-service/blob/4dbfdac075d4c13889f39fae44432593e6b4c78a/tests/test_pedido.py#L36) instantiates `TestClient(app)` through FastAPI. The [workflow](https://github.com/cauerkarsten/pedido-service/blob/4dbfdac075d4c13889f39fae44432593e6b4c78a/.github/workflows/ci.yml#L30) installs `requirements-dev.txt`, which [includes `requirements.txt`](https://github.com/cauerkarsten/pedido-service/blob/4dbfdac075d4c13889f39fae44432593e6b4c78a/requirements-dev.txt). The [target requirement](https://github.com/cauerkarsten/pedido-service/blob/4dbfdac075d4c13889f39fae44432593e6b4c78a/requirements.txt#L1) pins FastAPI 0.115.0.

[HTTPX 0.28.0](https://github.com/encode/httpx/releases/tag/0.28.0) removed its deprecated `app=` argument. For the proposed mechanism to affect the target's `TestClient(app)` call, the selected adapter would have to forward that argument to `httpx.Client`. [FastAPI 0.115.0's dependency metadata](https://github.com/fastapi/fastapi/blob/0.115.0/pyproject.toml#L42) declares `starlette>=0.37.2,<0.39.0`. [Starlette 0.37.2](https://github.com/Kludex/starlette/releases/tag/0.37.2) removed the forwarding at the admitted floor. [The tagged constructor](https://github.com/Kludex/starlette/blob/0.37.2/starlette/testclient.py#L422) passes a transport. The target can still pass an app to its adapter without that adapter passing `app=` to HTTPX. With the declared pins respected and that adapter path selected, the screened forwarding mechanism is ruled out by source and dependency metadata. The observed green run alone could never establish that explanation.

A narrow counterfactual check would compare `TestClient(app)` in the same target setup under old and proposed HTTPX pins, recording the resolved adapter and callable. If the old version constructs the client and the proposed version fails at a forwarded `app=` with the same adapter, investigate the adapter constraint or revise the upgrade. If both constructions succeed on that path, clear that specific concern. The selected evidence provides no reason to expect the implicated forwarding under normal declared resolution. The generic missing manager-environment observation supplies no contrary exposure. This case therefore serves as a negative control for recommending a check from a release note plus a superficially similar call. Installed versions and behavior outside the screened path remain open.

## Disposition

Stop the bounded screen here. Keep targeted-check output and Runtime-State Cycle 2 deferred. A suitable follow-up candidate would expose a direct `httpx.Client` or `AsyncClient` call with `app=` on a relevant target path, or admit an adapter version that still forwards it. Require an exact supported transition, a pending decision, and an observation whose outcomes lead to distinct actions. Use existing source and CI owners first. This screen supplies no product synthesis, runtime compatibility verdict, or maintainer usefulness result.

```text
A0/A1/A2 — Prior Aruba handoff and user selection carried forward for this bounded read-only screen.
B — Selected one exact-pin target, traced the suspected mechanism, and exercised existing CI owners.
Verification — Exact source and upstream declarations, guarded dependency admission, exact-attempt CI result.
D/E — Distinguish the adapter input from the downstream keyword. Close the negative control with positive qualification deferred.
C — Selection rationale, transport recovery, producer result, and action criteria preserved here.
```
