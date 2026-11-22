# GitHub JSON response size limit

- **Starting revision:** `70daed013ccbb4e56afdc0a60997d80acc61c9b1`
- [AUDIT-016 F3](../audits/2026-11-21_AUDIT-016_whole-project-product-and-design.md#audit-016-f3--medium-ordinary-acquisition-has-uneven-resource-enforcement)
- UP-SKILL:upgradepilot-build-implement
- UP-SKILL:upgradepilot-working-memory

Ali authorized measuring the 8 MiB candidate and implementing the shared GitHub JSON response guard if the evidence supports it. Learning remains in the separate workstream per Ali's direction. This record carries the engineering decisions and verification. The increment owns one decoded response body. Aggregate investigation accounting remains a separate decision.

## Selected limit and implementation

The shared GitHub JSON transport owns the **8 MiB decoded-body ceiling**. The admission samples for four public cases ranged from 635 to 27,249 bytes across 16 responses. The complete retained MapProxy, OpenCV, and HTTPX ledgers supplied 11, four, and four successful GitHub response bodies with maxima of 45,796, 24,077, and 29,496 bytes. A separate exact pandas Git tree response was 729,960 bytes with `truncated=false` and SHA-256 `cc7ca366268b8abe3fd91c4477a4b24b7150e8a4f6add0564c137f0dae9b9c04`. These retained examples show compatibility at their measured sizes. They supply no global workload distribution.

An admitted 1,000,000-byte repository text file needs about 1.33 MB of base64 before JSON envelope overhead. The 8 MiB ceiling matches existing inventory and caller/signature per-response ceilings and passes a full synthetic changed-file page with roughly 4.8 MB of patch text. A shared limit at this layer avoids guessing endpoint-specific ceilings from sparse cases. File-size, page-count, identity, and higher-level evidence contracts still supply independently required checks. [Exact-file support contract](../docs/architecture/ADR-0004-dependency-version-change-evidence.md#5-exact-structured-file-acquisition) · [Shared transport](../src/upgradepilot/github/api.py)

The reader requests a streamed response, caps decoded chunk accumulation, closes the response on success or failure, and parses only after the complete body fits. It reports `response_size_limit` on overflow and `body_incomplete` on interrupted transport. A complete invalid JSON document keeps the distinct response-error path. The limit relies on observed decoded bytes, including when a length header is absent or describes compressed bytes.

Requests can buffer redirect bodies while resolving a redirect or preparing an unfollowed next request. The response hook closes that unused body and preserves the status and headers before Requests performs its redirect handling. The implementation retains the existing relative URL resolution, credential stripping, and explicit repository-move observation behavior. Only the small hook depends on Requests' response cache fields, with controlled adapter coverage for both redirect routes. Existing GitHub product fixtures now supply serialized bytes to the streaming reader.

## Verification progression

- **173 focused tests passed.** Cases include an exact 8 MiB decoded compressed response, one byte over, early closure before the tail and before JSON parsing, interrupted transport, malformed complete JSON, followed and observed redirects, a full large changed-file page, and the maximum supported repository text with base64 line wrapping.
- **56 affected experiment and diagnostic tests passed**, alongside the experiment dependency boundary check.
- The candidate wheel was built and installed offline using cached build and dependency wheels. `pip check` passed and all 120 installed product modules matched the candidate. The first local build attempt used the editable environment without an available build backend. The isolated cached-wheel build supplied the backend. The first network-namespace invocation needed retained namespace setup capabilities to enable loopback. The corrected invocation initialized loopback and then dropped capabilities before testing as the ordinary user.
- The installed MapProxy ordinary CLI replay consumed the same 16 frozen responses, with request and body identities checked by the existing transport. The full report rendered identically after excluding the newly generated report ID and generated/acquisition timestamps. Stable render SHA-256 `7dfc45e1dc3282c628e7d54fc55ec1b5b0dbfa43980dbce1c863b85558411e83`. The installed CLI separately rejected a synthetic oversized initial response with exit 3 and `response_size_limit` after one attempt and produced no saved report. [Reference replay](evidence/2026-11-21-matrix-final-acceptance/RESULTS.md)
- The installed reader also accepted the retained 729,960-byte pandas tree through the normal Requests adapter seam and returned the complete decoded object.
- **All 1,191 product tests passed with zero skips** on the clean installed wheel in 249.196 seconds, from the private candidate checkout with only loopback, normal user identity and dropped capabilities. Installed module and console help matched. Full regression log SHA-256 `49f0a5afab1837c5dcad3119ec5c510574b147cb1178d12468d7391e3bafb052`.
- Candidate product/test patch SHA-256 `4849543b8b81d86d02bdf3a6f0c134399de435a63f280991bd41e9ee6188d1b5`. Installed wheel SHA-256 `c73bbdc13f186bffc0808ccaca8e14d444ab92cbf2d34d12c9435f54e4f4607c`.

The local checks qualify one decoded response, existing supported inputs, and the tested report and transport paths. Aggregate request count, cumulative bytes, end-to-end runtime, and live provider observations remain separate.
