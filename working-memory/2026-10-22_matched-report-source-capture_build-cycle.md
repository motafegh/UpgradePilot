# Matched normal report/source capture — Build cycle

Primary operation: Build/Implement under [report usefulness §5](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#5-independent-usefulness-evaluation).
Previous: [readiness engineering cycle](2026-10-22_maintainer-utility-readiness_engineering-cycle.md).

A0 — DONE: fetched origin; entry main242cf32d and origin/main agree. Readiness receipts establish3 historical candidates but0 qualified matched packets in inspected retention. Current normal application, Requests GitHub/PyPI clients, old GitHub-only preparation recorder, report codec/CLI/tests and source/trust owners inspected. Unrelated untracked October3 audit preserved.
A1/A2 — Teaching DEFERRED by Ali; engineering responsibility established from the preceding handoff and "Go on". Understanding unassessed; no teaching gate in this session.
B — CURRENT: diagnostic recording of normal HTTP inputs plus the normal report; controlled composition/failure proof, then bounded live proof if admissible.
Verification gate — PENDING.
D — DEFERRED elsewhere; learning topics retained below.
E — PENDING engineering handoff.
C — CONTINUOUS.

## Selected responsibility and local design

Build one developer diagnostic under tools/, with its distinct proof in experiments/tests/. No product runtime imports tools/tests. No new product schema, acquisition engine, dependency, semantic evaluator or generic evaluation platform. The normal application and report projection remain owners of meaning/action. Source HTTP recording earns its place because a matched ordinary-review packet cannot be recovered from the existing report's derived/partial source entries.

Trace: normal application → existing GitHub/PyPI Requests clients → HTTP adapter and producer-consumed response bytes → private source packet + normal report. A scoped HTTPAdapter.send observer and response iterator/close observation preserve existing streamed and non-streamed consumer behavior. Do not eagerly drain PyPI streams: doing so could move a partial-body failure into the request stage and change the domain error. Preserve original byte chunks/exception types; budgets stop the diagnostic without fabricating a product provider failure. Record decoded HTTP bytes, not wire compression or target execution.

Allow anonymous HTTPS GETs only to api.github.com and pypi.org. Refuse auth/cookie headers and other destinations before transmission. Suppress ambient netrc/proxies for this tool process, not machine configuration. Capture source bytes only in a new0700 directory outside Git with0600 files. Retain timestamps/request URL/status and only response headers actually relevant to client/body interpretation; never request credential values or record session headers. Keep transport/body partial/failure and status-only unconsumed responses explicit.

No model inference selected. The same GET/endpoint guard stops any model POST before transmission using diagnostic control-flow that ordinary provider exception handlers cannot convert into semantic uncertainty. Preserve partial inputs and no completed normal-report artifact. Exact expected PR/base/head/dependency transition are independent capture-to-report coherence checks; a mismatch is not_comparable, not a silent new case. Report/source packet identity and body hashes prove retention/equality, not source truth or usefulness.

Proof: exercise actual Requests responses and normal clients through recorded/unrecorded transports, including streamed body failure, malformed JSON/status-only closure, redirect/auth/destination refusal, byte/request/deadline limits and model refusal; compare native result/report semantics with only existing generated-ID/time normalization. Publish tool/tests proof before any live acquisition. Any live selection gets an immutable operational manifest first, separate from an unready independent study protocol. Prefer one HTTPX normal-path mechanical proof, not3-case study activation; a current model branch or identity drift remains an honest stopped/unavailable outcome.

Learning elsewhere: why observing a stream differs from eager buffering; decoded-byte versus wire retention; request-stage versus body-stage failures; capture stopping versus provider uncertainty/abstention; raw source packet versus derived report; source access parity versus independent utility; operational freeze versus study freeze; exact identity/horizon and private/public evidence boundaries.

UP-SKILL:upgradepilot-build-implement
UP-SKILL:upgradepilot-working-memory

## Implementation, proof and live preparation

Implemented tools/capture_report_sources.py and9 distinct diagnostic tests. The synchronous adapter/iterator/close observer tees bytes without eager PyPI reads and preserves native report meanings. Controlled actual application/report parity passes with report ID/time normalization only; compressed-body, stream failure, HTTP/malformed closure, destination/auth/model refusal, identity drift and caps/private retention are exercised.79 inclusive nearest tests pass in1.224s; after final index wording,9 focused tests pass again. Existing JobHunter Ruff binary check/format passes; no installation or product source mutation. Removed speculative cached-response handling after JUST review; normal HTTPAdapter returns unread responses. Initial lint issues corrected, terminal/provider broad catches explicitly justified, no test failure or real-case result was hidden.

[Operational proof packet](evidence/2026-10-22-matched-report-source-capture/PRE_EXECUTION.md) and100-member freeze bind all96 product files plus tool/test/plan/contract. One newly dated HTTPX exact-normal acquisition is selected for mechanical proof, not a three-case utility study.32 GET/8MiB-body/32MiB-total/120s action/150s external/public5MiB caps; zero inference/GPU/target execution/installs; model-required/identity drift/transport/cap failures preserve incomplete evidence without fabricated semantic results. The fresh private output path does not yet exist. Publish this coherent increment before the one live attempt.

## One fresh normal capture — outputs preserved before paired review

Code/proof/operational freeze published asb925b382 before execution. The one HTTPX capture completed normally:8 anonymous GETs,77,977 retained decoded bytes,4.183781s internal and4.502642s startup-inclusive, process exit0. Exact frozen repository/PR/base/head/HTTPX transition match. New full normal report, source index and receipt are retained; source body bytes remain private in the frozen new path. All private files inspected are0600. No model request or target execution occurred. Raw output completion is not yet source-mapping or utility acceptance.

Source shape:6 completed response bodies;2 PyPI provenance404 responses were closed without consumption, retained explicitly as body_not_consumed with only header/status evidence. PR identities were acquired twice around changed-file acquisition; no-run query is a new October22 observation. The dependency change uses the retained changed-file patch; no full requirements.txt input was acquired, so the report's head-file reference must not be labelled retained full-file content. Preserve these limits in paired review. No normal producer/parser/correlation/runtime semantic owner changed, and no original report/capture was modified or rerun.
