# PyPI release-index transport diagnosis

**Date:** November 6, 2026. **Status:** ACTIVE.
**Responsibility:** explain the acquisition path and distinguish the current failure boundary using bounded public transport controls; preserve the single native live attempt unchanged.
**Owners:** [live outcome](evidence/2026-11-06-native-normal-product-live-qualification/RESULTS.md), [implementation failure rules](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md#separately-frozen-native-product-attempt), [environment](../ENVIRONMENT.md#7-github-credential-and-proxy-caveat), [security](../SECURITY.md), [diagnostic contract](evidence/2026-11-06-pypi-transport-diagnosis/CONTRACT.md).
**Procedures:** `UP-SKILL:upgradepilot-build-implement`, `UP-SKILL:upgradepilot-learning-by-doing`, `UP-SKILL:upgradepilot-working-memory`.

```text
A0 — DONE: main/origin6800377d, saved receipts, source call chain, timeout/ledger/caching owners and environment reconciled.
A1 — DONE, CONTINUOUS CONTEXT: real capture partiality/recovery and missing selected pair already explained; user asks why and selects diagnosis.
A2 — DONE, COMPRESSED: acquisition chain and unknown DNS/TCP/TLS/header stage explained; bounded anonymous probes, no product retry or policy changes.
B — CURRENT: freeze diagnostic method; inspect current PyPI transport with product/independent controls and justified conditional contrasts.
Verification gate — PENDING: observed stages, exact control counts, source/attempt hashes, focused owner checks.
D — PENDING: explain actual failure location, why it affects HTTPX and what remains unknown.
E — PENDING: preserve decision and next responsibility without altering frozen attempt.
C — CONTINUOUS.
```

## Authorization and adaptation

Ali explicitly asks what/where the PyPI timeout belongs to, why it failed, and to proceed with the recommended bounded transport diagnostic. This admits public read-only network controls, not another PR/product attempt, credential read, retries, cap enlargement, global network/VPN/certificate changes, target execution or source-analysis changes. Existing coherent commit/push authorization applies. Keep private diagnostics outside the repository, expose only safe outcomes/hashes.

The preceding guided handoff and current source-chain explanation provide continuity and minimum upcoming orientation; compress repeated A1/A2 stop turns under the Smart Situational Override Rule while preserving actual proof/authorization. Independent learner mastery remains unassessed. If diagnosis exposes a consequential new repair/policy responsibility, reconcile its proper owner rather than silently implementing it.

Living map: imported distribution versus changed dependency; registry release-index metadata versus GitHub module text; sampled source versus installed version; domain resolution→TCP→TLS→HTTP headers→body→JSON/metadata admission; class-specific request exception versus reduced native reason; logical problem reuse versus physical dispatch; new diagnostic observations versus the earlier immutable failure.

## Source-first findings

Normal CLI constructs one AcquisitionSession, investigation publishes the input prefix, `collect_source_progress` creates AdapterSourceExplorer using that session, and `_acquire` consults a run-local package-index cache before `PyPIReleaseIndexClient.get_release_index`. The index client calls `PyPIJsonApiClient._get_response` with default3.05s connect/15s read timeouts, then validates a bounded JSON index. The shared AcquisitionSession enforces providers/GET/no redirects and shared limits, fully reads bounded response bytes and sets receipt.status immediately after headers arrive. Thus the saved two null-status/zero-byte receipts and typed timeout details place the old failure before a response was returned, with no finer retained DNS/TCP/TLS/header attribution.

FastAPI/pytest indices are selected by observed target imports and declarations. FastAPI's `TestClient` can lead through Starlette to the changed HTTPX source question; an index is version-selection metadata, not a package installation or import/runtime observation. Failed cached index observations can produce several logical problems without additional physical dispatches. The old run has two such physical failures, four logical problems, no retry/cap exhaustion and no dependency module receipts. No current evidence warrants a checker repair.
