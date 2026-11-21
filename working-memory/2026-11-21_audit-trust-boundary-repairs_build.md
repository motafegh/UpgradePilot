# Audit trust boundary repairs

Ali selected the two [AUDIT-016 trust repairs](../audits/2026-11-21_AUDIT-016_whole-project-product-and-design.md#findings-and-dispositions). The Build started at `3285b3b0`. The [Charter](../PROJECT_CHARTER.md), [trust rules](../SECURITY.md) and [local-model ADR](../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md#security-and-transport-boundary) already own the accepted boundaries. Engineering execution and evidence recording are in scope, with learning handled separately.

## Implementation

- The [shared PR reader](../src/upgradepilot/github/pull_request.py) requires a case-insensitive match for the returned base repository and affirmative public visibility with `private=false`. Missing or contradictory metadata fails before PR description retention. The same guard runs on the identity re-read after changed-file acquisition. A public base may have a different head fork. The existing public CLI error path reports refusal.
- The [default local-model POST](../src/upgradepilot/upstream/support_drop_extractor.py) keeps ambient proxy settings disabled and explicitly disables redirects. A redirect response is handled through the existing unresolved result. The reusable HTTP session constructor and injected test/alternative POST interfaces retain their prior scope.
- The existing product fixtures now include explicit public metadata. The first affected research regression exposed a shared synthetic PR response that omitted it. That one fixture was updated to match the admitted provider contract. A separate report-capture test initially missed the existing product test helpers and passed with the expected `PYTHONPATH=tests` invocation.

## Verification progression

- 78 focused product tests passed. Controlled cases covered private, internal, missing, inconsistent, and mismatched base metadata, a case variant with a fork head, a final identity re-read that no longer confirms public visibility, redirect refusal, and a direct model response.
- In the installed CLI, ordinary, caller/signature and combined caller/signature configurations rejected a synthetic nonpublic target with exit 4 before changed-file acquisition, stdout description emission or report creation. Original retained provider JSON for MapProxy, ApplyPilot and Pydantic passed the new shared admission guard.
- All 127 affected experiment and diagnostic tests passed after fixture and invocation corrections. The experiment dependency boundary checker passed. Both installed entry points, MapProxy attempt facts, and the exact AV-Tracer Workspace source reopened offline.
- The offline wheel was built from a private checkout with audited baseline plus the exact candidate patch, and installed using cached local wheels. All 120 installed product modules matched the candidate. `pip check` passed. Candidate product/README/test diff SHA-256 `81ee36b02ef2130042fa78ce9520acce06f197fa3300815363717dde624c5538`. Wheel SHA-256 `7b034fed4b39f9143e77a1efb3a5d3517d133940cb0ea4ca85a60cf9fd2d4393`.
- The full suite passed **1,186 tests with zero skips** on the clean installed wheel. It ran from the private checkout with only loopback, normal user identity and dropped namespace capabilities. The runner reported 230.450 seconds. Retained full regression log SHA-256 `e60ba33695a5418d939225699126d0e618c72e42c87d03836a2c9141ca003514`.

The two audit findings are resolved at their tested boundaries. Verification used controlled responses and retained public inputs. Fresh provider behavior and live model execution remain outside this proof. The broader product priorities and AI opportunities stay with AUDIT-016 and the live handoff.

UP-SKILL:upgradepilot-build-implement
