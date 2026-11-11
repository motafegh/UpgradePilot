# Qualify the AV-Tracer conflict through the caller/signature product path

Ali selected one product-path qualification after reviewing the OmniMatch result and the AI sequence. Main and origin/main reconciled at `c8b59cfb`. Prior orientation established the expected source conflict, normal-path requirement and the separate runtime/AI questions. Carry that orientation forward for this bounded audit and provider observation. UP-SKILL:upgradepilot-repository-audit. UP-SKILL:upgradepilot-working-memory.

Use AV-Tracer PR 11, base `527a004918c0f825e97c3583404242605fd58ec2`, head `25e7205f39103456e7efbc4e9f503f3debc7b5d8`, and expected HTTPX 0.25.2 → 0.28.1. The [manual baseline](2026-11-09_targeted-check_cross-case-qualification_cycle.md#positive-source-conflict-on-two-independent-target-repositories) identifies `backend/tests/test_app.py` → FastAPI re-export → Starlette 0.27.0 forwarding `app=` → old HTTPX accepts it, proposed HTTPX rejects it. A pass needs the normal report to recover that pairing and its scope with inspectable evidence. A failed GitHub job is separate, and its cause is unverified.

Run one anonymous normal caller/signature CLI from current source with exact base/head guards, new private store/report and existing policy. Use process-local direct provider routing, which succeeded for the previous public acquisition and PyPI wheel reads. Keep default 50 GitHub/100 total request limits, 32 MiB aggregate and 180-second acquisition ceiling, with a 270-second process guard. Use no manual source injection, model, target code execution or automatic retry. Recover the exact saved revision and identify the earliest gap before choosing any further work. The [caller/signature checkpoint](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md#16-combined-evidence-and-runtime-applicability-design-checkpoint) and [AI checkpoint](../plans/UPGRADEPILOT_90_DAY_PLAN.md#evidence-grounded-ai-design-checkpoint) own the subsequent decision.

## Actual result and first missing evidence

The CLI exited 0 in about 45 seconds and saved a report and Workspace revision `fe8628f1d8814be9931f5bd201135244`. The exact transition was admitted. Acquisition retained 12 target files, including `backend/tests/test_app.py` and both requirements files. The retained declarations include FastAPI 0.104.1, and the target import candidate for `fastapi.testclient` is present. A cold original-source view reopened `source-27` and showed `client = TestClient(app)`. The independent saved-report and exact Workspace reopen gave the same view.

The required conflict **did not reach the normal report**. The capture is partial. Native receipts identify a FastAPI release-index body transport failure after HTTP 200, reuse of that failed index result for another candidate, and a separate pytest release timeout. The invocation spent 17 GitHub and 20 total provider requests, with 582,820 decoded body bytes and no completed module-source receipts or adapter samples. The analyzer completed with 49 witnesses across 36 target roots, all involving repository-local callees. A green CLI exit and those counts establish delivery and limited local analysis. They supply no old/proposed HTTPX witness for the selected path.

The first missing evidence is library-source acquisition, before source correspondence or model explanation could be evaluated for this path. The underlying source record preserves the transport problems. The top-level coverage view says partial without listing those specific failures. Record that explanation gap as a separate possible presentation task if it becomes materially important. CI and runtime were unevaluated by this source-only profile. The failed GitHub test job from the previous review remains separately scoped.

## Route controls and disposition

Two separately labeled public read-only controls succeeded. Direct `/pypi/fastapi/0.104.1/json` produced an admitted exact release. The existing unauthenticated loopback proxy delivered and admitted `/pypi/fastapi/json`, the index required by the current adapter sampling path. The current owner requests the index even for this literal pin. The exact-release control is diagnostic evidence, not a verified index bypass or justification for dropping the existing index admission rules. Neither response was mixed into the frozen Workspace.

The next focused qualification would use one separately bound successor with PyPI through the verified loopback route, direct anonymous GitHub, unchanged acquisition/analysis limits and the same pass condition. This first run had no retry. Keep the case out of the fixed-evidence LLM comparison until the source chain is available. If a successor acquires the chain but the report still misses it, trace the actual remaining correspondence or presentation boundary before choosing an AI task. This is a defer disposition for the AV-Tracer AI candidate based on missing library evidence.

The [public qualification receipt](evidence/2026-11-10-av-tracer-caller-signature-product-qualification/qualification.json) binds identity, result counts, transport, revision and hashes. The [report excerpt](evidence/2026-11-10-av-tracer-caller-signature-product-qualification/report-excerpt.txt) preserves the coverage and analysis sections. The full source-bearing report and SQLite Workspace are in the private owner-only retention directory. Governance and diff checks passed. No source/test changes, model invocation or target execution.

```text
A0/A1/A2 — Current main, exact target and expected manual baseline reconciled in continuous context.
B — One normal invocation, saved and cold report/source inspection, and two route-only controls.
Verification — Delivery and cold parity pass. The exact source-conflict task is blocked by library acquisition.
D/E — Separate local analysis completion, relevant source evidence and later explanation quality.
C — Preserved the frozen result, narrower diagnostics, route controls and handoff.
```
