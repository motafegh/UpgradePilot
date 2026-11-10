# Integrate static dependency requests into CI reports

Ali selected the integration continuation after the [extraction milestone](2026-11-10_ci-version-request-extraction_build-cycle.md). Main and origin/main reconciled at `81aeab4c`. Carry forward the distinction between a recorded request, coverage and runtime. The [selected plan](../plans/CI_REQUESTED_DEPENDENCY_VERSION_REPORT_PLAN.md#persistence-and-report-integration) calls for an explicit coverage codec version and shared report projection. The previous onboarding established the producer and the handoff, and the current continuation authorizes this implementation scope.

UP-SKILL:upgradepilot-build-implement. UP-SKILL:upgradepilot-learning-by-doing. UP-SKILL:upgradepilot-working-memory.

The source proof must survive even if runtime correlation is absent. Preserve the producer's parsed job/step basis and bind it to the exact retained workflow, then verify command bytes at recovery without rerunning workflow, shell, or dependency analysis. Historical coverage layout and report behavior remain part of the proof.

The first live diagnostic reached the exact PR inputs with three HTTP 200 responses and stopped before CI acquisition. The harness used the native-only default schema 1 for a lifecycle host, which correctly refused publication. The successor explicitly creates an isolated schema-2 store, as required by the existing host contract. No product storage default or existing Workspace was changed.

## Implementation and live proof

The normal CI coverage result now carries the extracted static requests and one retained parsed job per affected job key. The producer binds requests to the exact retained workflow digest. Reconstruction checks package/workflow identity, retained job and step membership, byte and line/column coordinates, command text and the literal argument source against the recorded run text. This uses the historical static basis even when runtime matching is unresolved. It does not re-establish package semantics or claim authenticity from the digest.

Only the CI coverage native family adds codec version 2. The version-1 layout is intact and decodes without a request result. The version-2 layout distinguishes an empty evaluated tuple from unavailable request evidence. Explicit version-1 encoding refuses to discard newly recorded request evidence. The shared report mapping uses ordinary workflow-scoped facts and the existing exact workflow source links. The saved report schema and coverage/runtime/action semantics stay the same.

The fresh schema-2 successor made 13 anonymous API GETs, all HTTP 200, on the same frozen OmniMatch base and head. It saved Workspace revision `c41dda7352e04e5eac7367ec0931779a`, digest `c57bdc86bb666234d8c30866b23dc15d8991e8ea31d2d656846bf50d14d937a6`. A fresh process reopened that SQLite revision read-only and reproduced the live report with network and analysis entry points guarded. The [saved CI view](evidence/2026-11-10-omnimatch-version-request-report/ci-view.txt) has SHA-256 `3b85183b29c71ad0c7ae9a0a143e19157978d34cf0eab357c304e138576c8895`.

The [previous CI view](evidence/2026-11-10-omnimatch-ci-report-trace/ci-view.txt) differs only by two added static-request lines, in `signatures` and `cpu-models`. They identify the requested old pin and exact command scope. `dependency_consumption_not_established` and `no_admitted_candidate` stay in force. A version-1 control from the equivalent retained inputs rendered the previous view byte for byte. The live qualification used CI preparation and durable recovery. Full-investigation rendering and saved-report reopen were exercised with controlled inputs. No target execution or proposed-version runtime proof.

An independent backward-compatibility control ran the actual `81aeab4c` source in an isolated directory to produce a version-1 native boundary and its report. Current source read that older boundary, retained historical unknown request status, and reproduced the report byte for byte. Controlled corruption checks refused mismatched workflow digests, job and step identities, command text, and literal argument source even when the payload digest was recomputed.

## Verification and handoff

All 1,088 product tests passed. The focused request, codec and report controls also passed after final source-binding cleanup. Governance doctor and diff checks passed. In the live capture, the CI coverage payload grew from 5,326 bytes in the equivalent v1 control to 28,994 bytes in v2, including one parsed job basis for each of the two affected jobs. That is the measured cost for this case, with no general size or latency claim.

The planned report path is connected. The remaining OmniMatch question concerns the HTTPX version loaded by the named test and would need a distinct target-owned observation. Before investing in broader CI interpretation or runtime state, review this completed report against the maintainer task.

```text
A0/A1/A2 — Reconciled current main and carried forward the extraction milestone and agreed integration.
B — Connected coverage, versioned native capture, validated recovery, and report projection.
Verification — Exact live/cold parity, actual older codec parity, corruption controls, and 1,088 product tests.
D/E — Explain why a static pin survives the restart without granting runtime credit.
C — Preserved the harness refusal, corrected qualification, report evidence, cost, and handoff.
```
