# UpgradePilot Current Memory

**Last updated:** 2026-08-05  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md).
- **Selected bounded plan:** [`plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`](plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md).
- **Accepted semantic method:** [`docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`](docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md).
- **Accepted source organization:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).
- **Selected product increment:** **Step 7C — product local semantic adapter**.

Step 7A changelog discovery and Step 7B deterministic crossed-release source-window construction have passed their bounded proof gates. Step 7's remaining proof and stop boundaries still control continuation.

## Latest material verification

The accepted product baseline now includes:

- post-reconciliation active product regression: **323 tests passed** before Step 7B;
- completed Step 6 experiment regression: **27 tests passed**;
- module and installed CLI entry points: **passed**;
- Step 7A exact-commit changelog-path discovery live proof: **passed**;
- Step 5 interval/changelog live proof after credential-contamination diagnosis: **passed**;
- Step 7B focused source-window, GitHub changelog-discovery, source-topology, and full active product regressions: **passed in WSL** on implementation head `ec80105cabca9515c74a89549119f40415df6c0d`.

Primary recent evidence:

- [`working-memory/2026-08-05_B2-step-7b-crossed-release-source-window-validation.md`](working-memory/2026-08-05_B2-step-7b-crossed-release-source-window-validation.md)
- [`working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md`](working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md)
- [`working-memory/2026-08-04_REPO-GOV_post-reconciliation-artifact-routing-alignment.md`](working-memory/2026-08-04_REPO-GOV_post-reconciliation-artifact-routing-alignment.md)

Detailed source topology, migration history, test output, experiment scores, and incident narratives belong to their dated evidence records, source/tests, and accepted ADRs rather than this live continuation file.

## Retained Step 6 decision fact

The bounded local extractor was adopted for one narrow responsibility after the frozen evaluation gate:

```text
admitted crossed-release source text
→ bounded local candidate extraction
→ deterministic exact-source reconstruction
→ validate_support_drop_candidates(...)
→ grounded support-drop claim or explicit problem
```

Deployment identity and evaluation evidence remain controlled by ADR-0006, `ENVIRONMENT.md`, and the Step 6 working/evaluation records.

## Exact continuation

Resume with **Step 7C — product local semantic adapter**.

Required responsibility:

```text
CrossedReleaseSourceWindow
→ accepted LM Studio localhost request using gemma-4-e4b-it-ud
→ strict contract-v2 structured selection
→ deterministic exact source-line recovery
→ CandidateUpstreamClaimResult
or explicit unresolved candidate result on provider/HTTP/JSON/schema/runtime failure
```

Reuse the accepted ADR-0006 method exactly: direct `requests`, temperature `0`, seed `0`, no automatic retries, strict JSON Schema, no cloud/fallback provider, no experiment imports, and no model ownership of source authority or downstream decisions.

Do not begin Step 7D upstream composition until Step 7C focused deterministic product tests pass. Ordinary product tests must not require live model inference.

## Material blockers and caveats

No product blocker currently prevents Step 7C.

The reusable local deployment baseline is in `ENVIRONMENT.md`; stable untrusted-source/provider security controls are in `SECURITY.md`. A provider/model/deployment-contract change is a reassessment event rather than a silent substitution.

## Learning state

Current demonstrated depth is best described as **substantial implementation exposure with repeated evidence-driven debugging; no formal mastery assessment**.

Recent learning exposure includes:

- responsibility boundaries versus import wiring;
- provider/domain/application/interface ownership;
- deterministic source identity and structural windowing versus semantic interpretation;
- global source-line/character provenance preservation;
- product regression versus experiment regression versus live proof;
- explicit unresolved states instead of hidden truncation or heuristic recovery;
- distinguishing environment/provider failures from product evidence failures.

Record stronger ownership only after Ali demonstrates it through explanation, modification, testing, diagnosis, or transfer to changed cases.
