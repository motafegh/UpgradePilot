# HTTPX caller/signature evidence report

Publication summary of saved UpgradePilot report `4eea103d-dbb6-4fa2-89e4-5d28a1a47ea3`. Evidence IDs refer to the saved report. The links below identify the pinned inputs. This summary provides findings and source links. The rehearsal folder has no original-text attachments for this case.

## Pull request and change

- Repository `Aidan-Wallace/kubernetes-dashboard-token-api`, PR #20.
- Base `b065646e4b7b894964567950f9ad770b02c136c2`.
- Head `391508134b083b8f54461c0b576e8f7985c6ecb4`.
- Declared dependency change `httpx` 0.27.2 → 0.28.1. See the [PR](https://github.com/Aidan-Wallace/kubernetes-dashboard-token-api/pull/20) and [head requirements](https://github.com/Aidan-Wallace/kubernetes-dashboard-token-api/blob/391508134b083b8f54461c0b576e8f7985c6ecb4/requirements.txt) for the declaration (`source-1`, `source-25`).

## Target call and adapter

The target test constructs a client with `TestClient(app)` (`source-27`). The retained FastAPI sample re-exports Starlette's test client (`source-37`). On that source path, the target call fits the sampled Starlette initializer (`source-43`, a conditional source assessment). The sample establishes a path to inspect. Installed adapter selection and effective import binding remain unknown.

[Target test at the exact head](https://github.com/Aidan-Wallace/kubernetes-dashboard-token-api/blob/391508134b083b8f54461c0b576e8f7985c6ecb4/tests/test_routes.py#L7) · [FastAPI re-export](https://github.com/fastapi/fastapi/blob/8e3db5153ec314d6e7775cd0ea39a46e95bfddb0/fastapi/testclient.py#L1) · [Sampled Starlette initializer](https://github.com/Kludex/starlette/blob/8aa828ceaff764a2e57932fb42fdf105a47c4c83/starlette/testclient.py#L445)

## Forwarded call and dependency signatures

The sampled Starlette initializer forwards five keyword arguments at `super().__init__` (`source-39`). The conditional comparison checks `base_url`, `headers`, `transport`, `follow_redirects`, and `cookies` against the selected HTTPX initializers. All five bind to named parameters in the old 0.27.2 signature (`source-49`, based on `source-35`) and in the proposed 0.28.1 signature (`source-47`, based on `source-31`). The comparison assumes the sampled forwarding path and the recorded receiver and dispatch premises.

[Starlette forwarding call](https://github.com/Kludex/starlette/blob/8aa828ceaff764a2e57932fb42fdf105a47c4c83/starlette/testclient.py#L477) · [HTTPX 0.27.2 initializer](https://github.com/encode/httpx/blob/609df7ecc0f7cb10a1c998aa9c269bba77337c5f/httpx/_client.py#L628) · [HTTPX 0.28.1 initializer](https://github.com/encode/httpx/blob/26d48e0634e6ee9cdc0533996db289ce4b430177/httpx/_client.py#L639)

## Limits and recorded action

The saved investigation used the caller/signature profile. Installed versions and bindings, effective class resolution, branch activation, and the callee that actually receives the call remain unobserved. This profile did not evaluate CI or runtime behavior. The report records maintainer abstention.
