# Exact-release advisory visibility Build

- **Base revision** `08e3699d53d8f0e6adc202b1609ea00e16372e70`
- [Bounded design](2026-11-24_exact-release-advisory-visibility-design.md)
- [Implementation and proof requirements](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#preserve-advisory-observations-for-an-exact-release)
- UP-SKILL:upgradepilot-build-implement
- UP-SKILL:upgradepilot-working-memory

Ali selected the ordinary CLI build following the design and asked for a walkthrough after the work. The accepted design and the immediately preceding plan discussion supplied the implementation scope and proof requirements. The walkthrough follows verification under that agreed cadence.

## Built behavior

The ordinary caller opts into typed advisory retention in the exact-version PyPI release parser after package identity checks. An advisory problem leaves the validated release metadata and file inventory available. The parser bounds entries and IDs, preserves first-seen order and withdrawal state, and explicitly refuses malformed, contradictory or over-limit lists. It carries no free-form provider content forward. An attempted but unadmitted release produces a package-source status. An unattempted old release retains its existing assessment and produces no advisory source.

The first candidate added the observation to the shared release dataclass. Focused checks passed, then the full installed run reported 28 failures and six errors, traced to the fixed caller/signature source layout and its lossless round-trip guard. The repaired build carries the observation on an optional producer variant used by the ordinary path. The default release client still produces the original base record for caller/signature and its established SQLite format. This keeps report-only evidence outside the historical source contract and avoids a migration with no admitted consumer.

Ordinary generator 5 projects these observations into the existing package metadata sources. Renderer 8 shows the compact status, with IDs and their states available through the existing offline facts view. The source already carries its locator and observation time. There is no report schema change. The normal workflow makes no extra requests and the report action remains the original synthesis result. Workspace and model paths were outside this increment.

## Installed evidence

Passed 24 PyPI tests, 28 report tests and eight PR-description tests in the focused checkout runs. The experiment boundaries and seven CI presentation experiment tests passed separately. Built an offline wheel from a clean checkout with the candidate product and test patch applied. The fresh installation passed dependency consistency, and all 120 installed product modules matched the candidate source byte for byte.

- Candidate patch SHA-256 `068c85aaa32d797cf47b1a115639da4ba9a25912c1704ecb204a667c11016d56`
- Installed wheel SHA-256 `719f217151f8675feccd85b92f0dcb8809181265d6c39c94feda364fec0de0ea`
- Private final proof directory `~/.local/share/upgradepilot/release-advisory-build-final-20261124.Ukv6KUXA/`

The installed ordinary CLI ran against [three frozen response ledgers](2026-11-23_f4-development-acceptance.md#direct-checks) under a network guard. It matched the 37 methods and normalized request URLs in order and preserved the nine status-only 404 observations. All six exact old/proposed package sources opened through `--show-facts`, with three reported IDs and four explicit empty lists. Historical report bytes and views remained stable on four prior inputs. The full view comparison normalizes the current renderer version in its header. All prior package fact views matched byte for byte.

| Case | Release observations in the new saved report | Saved report SHA-256 |
|---|---|---|
| OpenCV #1111 | Old `4.2.0.32` at `source-8` has two reported IDs. Proposed `4.8.1.78` at `source-6` has an explicit empty list. | `2671becf0378b69d4558a3c40fb7e68b1697fbbfeca45d6129079f50a6ace5cd` |
| MapProxy #1559 | Old Soup Sieve `3.0.4` at `source-33` has `GHSA-mmhr-3c5m-f64f`, reported. Proposed `4.0` at `source-31` has an explicit empty list. | `40d12c4383352b4e374cf4f567a28dc4872d6bc74385005ff2ebcf72c805400d` |
| Dashboard API HTTPX #20 | Old `0.27.2` at `source-8` and proposed `0.28.1` at `source-6` both have explicit empty lists. | `def2b5553386a21e3916e968e203bb8c028c952900259fcbc8988db9c5e27ffb` |

The replay generated new observation and report times while using the original captured response bodies. It supplied no new provider observations. Structured findings, unknowns, assessments and action matched the previous frozen reports. The ordinary console comparison matched renderer 7 after accounting for the new advisory lines and scope, method versions and generated times, identifier and save path. All three kept `abstain`.

Six separate controlled HTTPX replays passed on the same installed wheel. Replacing only the old response's advisory field with missing, malformed, conflicting or over-limit data preserved the other assessments and action. Two identical withdrawn entries produced one retained ID marked withdrawn. A response bound to the wrong proposed release stopped after the proposed lookup, with an unavailable advisory status and the old release unattempted. The timestamp validator accepts timezone-bearing calendar timestamps with ordinary clock seconds. It refuses unrepresentable timestamp forms such as leap seconds at the advisory field boundary, preserving the rest of the package evidence.

Both published [AV-Tracer captures](../examples/av-tracer/README.md) passed archive SHA-256 verification. A fresh process reopened each saved report and SQLite Workspace revision, then read the exact retained source. All six outputs matched the prior installed CLI after normalizing the full report renderer header.

After the compatibility repair, the 35 caller/signature delivery tests, 43 native reconstruction tests, and 25 source-acquisition tests passed in focused runs. The full isolated installed suite passed **1,198 tests with zero skips** in 253.920 seconds. The `full-installed.log` SHA-256 is `c99dc877202afc5f889540d5c42eadc372ad7376c1ff422c3068a60d6e88c9f2`.

In MapProxy, the record now answers what PyPI reported for each exact release in the frozen responses. The CI source can independently answer what command GitHub reported successful. Installed version, execution of affected behavior and mitigation still require separate target evidence. Data from a later lookup requires a new observation.
