# Bounded PyPI transport diagnostic contract

November 6, 2026. [Cycle](../../2026-11-06_pypi-transport-diagnosis_cycle.md). Freeze before dispatch. This is a separate developer diagnostic; it does not repair, retry, regrade or append material to the native product attempt.

## Question and fixed sequence

Why can the current environment fail to obtain the two PyPI indices required by source acquisition? The original capture proves two timeouts with no status/body; it does not identify a network substage or establish that the same condition still exists.

1. **Baseline, at most3 HTTP dispatches:** one real installed `PyPIReleaseIndexClient` call for `fastapi`, one for `pytest`, both through a fresh anonymous `AcquisitionSession` with unchanged product policy/default timeouts/retry disabled; then one independent Linux curl GET for the same FastAPI URL using HTTP/1.1. Observe existing product DNS/TCP/TLS/header calls with passive wrappers. Preserve exception classes/chains privately, native receipts, accepted/rejected index state and bytes. No PR/GitHub/acquisition producer/analysis run or personal-token access.
2. **Address-family contrast, at most2 HTTP dispatches, conditional:** only if baseline receives no HTTP response and observed DNS resolves address families, run one Linux curl FastAPI GET per available IPv4/IPv6 family. Do not rerun a family or change DNS/routes. A DNS failure alone does not justify forced-family retries.
3. **Host contrast, at most1 HTTP dispatch, conditional:** only if WSL baseline/family controls still cannot reach HTTP despite successful resolution, compare one direct Windows-system-curl FastAPI GET if the executable exists. This is the specific WSL/host network-boundary question; no Windows configuration changes. An absent executable means unperformed, not failure or permission to install tools.

Stop after those fixed controls, on a source/method integrity failure, or if the discriminating question is answered earlier. Max6 HTTP dispatches total, no automatic retries/replacements. Success now is current reachability evidence, not an explanation or repair of the earlier timeout. Failure may establish only a narrower stage/platform boundary; preserve remaining uncertainty.

## Transport, resource and timing scope

Only HTTPS GET to `https://pypi.org/pypi/fastapi/json` and `/pypi/pytest/json`; redirects off, no credentials, explicit direct/no-proxy child environment. Product uses its existing verified certificate behavior and shared50/100 policy,180s cooperative deadline,8MiB response/32MiB aggregate limits and3.05/15s socket defaults. Actual diagnostic HTTP dispatches are capped by this fixed method, not by exhausting that policy. Index JSON admission retains its existing stricter1,000,000-byte provider cap; a transport success plus size/metadata refusal is a separate outcome.

Curl disables user configuration (`-q` first), credentials/netrc are not selected, `--noproxy '*'`, HTTP/1.1, no redirects, retry0,3.05s connection timeout,20s whole-call ceiling,8MiB maximum response, body discarded. Keep status, exit/error category, DNS/TCP/TLS/first-byte/total timing and public remote-address metadata; no headers/cookies/certificate bypass or body archive. Curl and Requests use their own normal trust implementations; they are independent controls, not identical TLS clients.

Qualified Windows QPC supervises each phase as a labelled outer process envelope:100host seconds baseline,60family,40host contrast. Inner Python raw-monotonic and curl timing values are stage counters, not interchangeable physical/active durations. Observe gaps using the existing qualified watcher; retain timeouts and incomplete controls without repetition. Every phase uses a new owner-private output directory. Total phase ceilings200host seconds plus bounded startup/cleanup; no tool wait over60seconds. No global settings or product clocks change.

Freeze method copies/digests, selected installed source/dependency identity, actual binary digests, endpoints/phase/control limits and input live-result/receipt hashes before each phase. Preserve failed diagnostics and any correction as separately labelled successors; do not modify an executed method snapshot. Public projection excludes raw environment values, credentials, private routing details, arbitrary exception text and response bodies.

## Decision boundary

Classify the strongest observed boundary (resolution, TCP, TLS, pre-header wait, body, JSON/admission, platform/client contrast), distinguish current versus historical proof, and identify the smallest justified next responsibility. No product repair or new live capture is selected by a successful diagnostic. A material transport/policy/observability change needs its owning design/authorization and qualification; a transient outcome does not justify infrastructure or limit changes.
