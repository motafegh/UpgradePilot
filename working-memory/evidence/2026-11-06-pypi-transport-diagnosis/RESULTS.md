# PyPI transport diagnosis

Executed November 7, 2026. [Frozen diagnostic contract](CONTRACT.md), [measured results and hashes](results.json), [cycle](../../2026-11-06_pypi-transport-diagnosis_cycle.md), [original live attempt](../2026-11-06-native-normal-product-live-qualification/RESULTS.md).

The installed client reproduced both index timeouts during the **TLS handshake**, after DNS resolution and IPv4 TCP connection. TLS establishes the encrypted HTTPS session. Both handshakes exceeded their timeout before HTTP header handling began. Requests exposed the error as `ReadTimeout`, with `urllib3.exceptions.ReadTimeoutError` and the underlying `TimeoutError` in its exception chain. The stage trace identifies where that broad exception occurred.

The original live ledger retains null status, zero response bytes and `transport_error` for both attempts. The release-index owner adds the timeout description. That older evidence localizes the failure to acquisition before a usable HTTP response. Its finer network stage remains unknown.

| Control | Observed outcome |
|---|---|
| Installed FastAPI index client | DNS resolved IPv4 and IPv6. IPv4 TCP connected. TLS timed out. |
| Installed pytest index client | Same observed sequence and timeout class. |
| Linux curl, default address selection | TCP connected. SSL connection timed out. |
| Linux curl, forced IPv4 | TCP connected. SSL connection timed out. |
| Linux curl, forced IPv6 | TCP connection failed. |
| Windows system curl | Connection timed out before an HTTP response. Its trace leaves the finer stage unresolved. |

All six public HTTPS attempts ended without an HTTP response. The Linux curl result independently reproduces the observed transport boundary. The Windows result also shows a failure outside the WSL client environment. The particular network component responsible remains unresolved. The three qualified host process envelopes were 10.391, 3.270 and 3.263 seconds. These cover the diagnostic processes and their overhead. The Python TLS stage counters are stored separately in the structured results.

## Where this sits in UpgradePilot

`collect_source_progress` gives `AdapterSourceExplorer` the shared acquisition session. The explorer pairs observed imports with declarations and asks `PyPIReleaseIndexClient.get_release_index` for available releases. It uses the visible constraint to choose a source exploration sample. Source acquisition then needs upstream repository and module evidence. This is the route toward the FastAPI `TestClient` definition and its possible Starlette and HTTPX relationships. The pytest index serves another observed import. [Source progress](../../../src/upgradepilot/caller_signature/source_progress.py#L100), [adapter exploration](../../../src/upgradepilot/caller_signature/source_acquisition.py#L826).

`PyPIJsonApiClient` uses the existing 3.05-second connection and 15-second read settings. `AcquisitionSession` records response status before reading the bounded body. The diagnostic traces end during TLS, so neither response-body reading nor index parsing was reached. The original partial capture therefore has target text and local comparisons while the selected downstream dependency path lacks source evidence. [PyPI request client](../../../src/upgradepilot/pypi/api.py#L64), [release-index client](../../../src/upgradepilot/pypi/release.py#L366), [transport ledger](../../../src/upgradepilot/caller_signature/acquisition.py#L204).

## Disposition

Defer another native product capture until a trusted route completes the required PyPI index reads. A bounded alternate-route comparison is the next discriminating check. It should record verified TLS, HTTP status and index admission separately. If that route yields usable indices, review a separately labelled successor invocation under the existing product policy. The original attempt retains its partial grade and its saved evidence.

The diagnostic used anonymous PyPI reads, separate owner-private outputs and the qualified installed product binding. Hash verification covers the original live artifacts, all 377 execution bindings, 121 installed files and each executed diagnostic method. The private probe counter named `dispatched_http_requests` counts attempted controls. At the observed failure boundary these are HTTPS attempts with zero HTTP responses. The public summary uses `attempted_https_controls` to make that scope explicit.
