# Bounded PyPI pre-response timeout recovery

Evidence: first capture FastAPI release timeout; S005 proposed HTTPX provenance timeout; S006 Starlette release timeout. D001 later obtained the exact first endpoint. These are real pre-response timeouts, not token/quota, adverse provenance, malformed JSON or missing source. Network-level root cause remains unknown. Current per-run failure cache correctly avoids hidden retries but forces expensive whole acquisitions after one transient event.

## Explicit successor-only profile

Keep default/frozen no-retry behavior and policy receipt v1 unchanged. Add opt-in PyPI-only HTTPS GET timeout recovery at the existing TrialPublicSession owner, with a separately frozen contract field:

- At most1 retry for one logical request, at most2 retry decisions for the entire acquisition.
- Only requests.exceptions.Timeout before response status/body exists; never retry an HTTP status (including401/403/404/429), body/JSON/integrity errors, policy refusal/deadline, credential failure, GitHub request or non-GET/new host.
- Every physical attempt uses the existing charged request/body/time owner and the same counters; no reset, extra allowance or whole-attempt retry. A retry may itself be refused by the existing global limits.
- Retain failed request and retry-decision linkage, including selected-but-not-dispatched decisions. Event/decision history is not discarded when the final response succeeds.
- No semantic reinterpretation of unknown provenance as absent/adverse or vice versa. Providers validate the eventual response exactly as before; observation times may differ and do not establish an atomic provider snapshot.

Emit version2 transport receipts only for opted-in sessions, with exact retry policy and decisions in addition to existing fields/events. Keep v1 cold admission unchanged and qualify fixed v2 relation/cap admission. The ordinary experiment contract reader admits only this exact recovery profile; automatic_retry=false continues to prohibit whole-attempt retry and is explicitly scoped in the new successor's lifecycle text. No old contract is edited.

## Proof before live

Controlled timeout→success and timeout→timeout must charge both attempts and retain first failure. Global2 retry ceiling; shared provider/time limit can prevent dispatch. GitHub timeout, HTTP responses and body/JSON/policy failure must not retry. Normal ordinary actual-client composition must retain/read the v2 profile and reject corrupted retry links without reanalysis. Qualify API/architecture/historical regressions and old/first/S002–S006 cold bundles, freeze new method/profile, then perform a fresh S007. No response/capture backfill, auth broadening, cap increase or target/model execution.
