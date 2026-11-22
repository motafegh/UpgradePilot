# Ordinary investigation aggregate acquisition review

- **Inspected product:** `f3e5b4fdce762baea46bfdae8851ac8a70bcee70`
- [AUDIT-016 F3](../audits/2026-11-21_AUDIT-016_whole-project-product-and-design.md#audit-016-f3--medium-ordinary-acquisition-has-uneven-resource-enforcement)
- UP-SKILL:upgradepilot-repository-audit
- UP-SKILL:upgradepilot-working-memory

Ali selected a short offline aggregate-cost review followed immediately by maintainer-usefulness preparation. Learning stays in its parallel workstream. This review closes the selected measurement and budget decision. The previously delivered [8 MiB GitHub body guard](2026-11-22_github-json-response-size-build.md) bounds one response.

## Retained normal-run observations

Each row counts ordered GET attempts across both providers and totals only the decoded bytes actually retained. Verified all 37 request records and body hashes offline. The measurement uses ordered normal-run ledgers from the MapProxy replay and October 22 captures. It excludes separate preflights and partial snapshots. The selected cases have intact ledgers and different acquisition paths.

| Case and horizon | GitHub GETs / bytes | PyPI GETs / bytes | Total GETs / bytes | Timing |
|---|---:|---:|---:|---|
| MapProxy #1559, frozen November transport replay | 11 / 199,004 | 5 / 145,044 | **16 / 344,048** | Retained transport, no comparable live duration |
| CARLA/OpenCV #1111, October 22 live capture | 4 / 48,900 | 9 / 63,100 | **13 / 112,000** | 7.479 s capture-internal |
| Dashboard API/HTTPX #20, October 22 live capture | 4 / 59,749 | 4 / 18,228 | **8 / 77,977** | 4.184 s capture-internal |

OpenCV's seven and HTTPX's two provenance HTTP 404 outcomes count as attempts. Their bodies were unconsumed and contribute zero **retained** bytes. Wire bytes, retries outside these observed runs, and representative workload percentiles remain unknown. MapProxy consumed all 16 ledger responses and keeps its replay horizon. [MapProxy proof](evidence/2026-11-21-matrix-final-acceptance/RESULTS.md) · [OpenCV capture](evidence/2026-10-22-opencv-matched-report-source-capture/REVIEW.md) · [HTTPX capture](evidence/2026-10-22-matched-report-source-capture/REVIEW.md)

Ledger SHA-256 values in table order are `0e39c5935f6ca4d296cf802e57a7eec44ca4c72d7ca185213e1c53def6580a29`, `8a62a31c0c8ceefa34dc0bfd270d23ce94d2da3c4db72e996ad6e42eafbe8b43`, and `34fb9393349bf001b4a83bc34e53de0542e1f4d3295f6490412b86e954c9cda2`.

## Measured amplification and decision

- **CI multiplies across runs.** Changed files page at 100 and admit up to 3,000 records. Run listings and per-run jobs page at 100 and admit up to 1,000 each. CI obtains the jobs, then normally reads run details and one exact workflow file per run. A complete, fully populated CI branch could make 10 run-list GETs plus up to 12 requests per run before accounting for other producers. This is a source-derived branch envelope, conditional on complete admissible data and reachable workflow definitions. Provider quotas, transport, and inconsistent shapes can stop earlier. [PR reader](../src/upgradepilot/github/pull_request.py) · [Actions paging](../src/upgradepilot/github/actions.py) · [CI composition](../src/upgradepilot/investigation_inputs.py#L84)
- **Controlled execution confirms the multiplication.** The current input and CI producers consumed the retained MapProxy PR and changed-file identities followed by synthetic CI evidence with 20 runs of 201 jobs each, each referring to the same head and workflow path. The path completed **104 GETs and 729,665 decoded bytes** with 4,020 job records. Requests were two PR reads, one changed-file page, one run page, 60 job pages, 20 run-detail reads and 20 workflow-file reads. The GitHub session was injected and networking isolated. This is execution evidence for request fan-out. Frequency and live performance are unmeasured.
- **Provenance multiplies across artifacts.** A proposed release can request one PyPI provenance endpoint per distribution file. OpenCV demonstrates seven requests with no usable provenance, and HTTPX demonstrates two. Stopping at the first positive witness could miss contradictory publisher evidence because the resolver checks agreement across the available set. [Provenance resolver](../src/upgradepilot/upstream/repository.py#L75)

**Disposition:** preserve the per-response guard and defer selecting a shared ordinary budget. The retained cases fit comfortably, while the stress run shows why a per-response limit cannot bound aggregate work. Copying the explicit caller/signature profile's 50 GitHub and 100 total request defaults would stop the synthetic ordinary CI case even though every collection is individually admitted. The test establishes that a limit would be a product coverage decision, and the sample gives no acceptable stop threshold. Revisit when a representative high-fan-out ordinary case shows unacceptable bytes, waiting, rate-limit use or duplicate exact reads. At that point compare producer-scoped reduction with an end-to-end budget and preserve truthful outcomes on every interrupted evidence branch. [Separate source-profile policy](../src/upgradepilot/caller_signature/acquisition.py#L30)
