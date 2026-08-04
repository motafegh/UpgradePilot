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

Step 7A changelog discovery and Step 7B deterministic crossed-release source-window construction have passed their bounded proof gates. Step 7C deterministic product tests have also passed; the remaining Step 7C gate is the corrected live local-model proof.

## Latest material verification

The accepted product baseline now includes:

- post-reconciliation active product regression: **323 tests passed** before Step 7B;
- completed Step 6 experiment regression: **27 tests passed**;
- module and installed CLI entry points: **passed**;
- Step 7A exact-commit changelog-path discovery live proof: **passed**;
- Step 5 interval/changelog live proof after credential-contamination diagnosis: **passed**;
- Step 7B focused source-window, GitHub changelog-discovery, source-topology, and full active product regressions: **passed in WSL** on implementation head `ec80105cabca9515c74a89549119f40415df6c0d`;
- Step 7C focused semantic-adapter and full active product regressions: **passed in WSL** before live inference;
- first Step 7C live attempt reacquired the complete real S001 source window successfully but provider preflight returned HTTP 500 because ambient proxy variables routed the loopback request through Privoxy on `127.0.0.1:8080`;
- explicit `curl --noproxy '*'` reached LM Studio directly at `127.0.0.1:12345`, returned HTTP 200, and showed the adopted `gemma-4-e4b-it-ud` model as available;
- product and live-proof LM Studio transport now use a `requests.Session` with `trust_env = False` so loopback inference does not inherit ambient proxy configuration.

Primary recent evidence:

- [`working-memory/2026-08-05_B2-step-7c-lm-studio-proxy-contamination-diagnosis.md`](working-memory/2026-08-05_B2-step-7c-lm-studio-proxy-contamination-diagnosis.md)
- [`working-memory/2026-08-05_B2-step-7b-crossed-release-source-window-validation.md`](working-memory/2026-08-05_B2-step-7b-crossed-release-source-window-validation.md)
- [`working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md`](working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md)

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

Resume by rerunning the **Step 7C real S001 live semantic proof** after the proxy-independent loopback transport correction.

Expected live flow:

```text
real S001 upstream evidence
→ Step 7B CrossedReleaseSourceWindow
→ proxy-independent LM Studio loopback session
→ gemma-4-e4b-it-ud contract-v2 selection
→ deterministic exact source-line recovery
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
→ grounded Python 3.8 support-drop claim or explicit safe problem
```

If the live proof grounds the expected S001 claim, close Step 7C and continue immediately to **Step 7D — upstream composition and deterministic trust admission**. If it fails, diagnose the smallest provider/model/contract boundary exposed by the live output; do not change source authority or target-Python logic to compensate.

Reuse the accepted ADR-0006 method exactly: direct `requests`, temperature `0`, seed `0`, no automatic retries, strict JSON Schema, no cloud/fallback provider, no experiment imports, and no model ownership of source authority or downstream decisions.

## Material blockers and caveats

No known product blocker currently prevents the corrected Step 7C live proof.

The reusable local deployment and ambient-proxy caveat are in `ENVIRONMENT.md`; stable local-inference transport and untrusted-source controls are in `SECURITY.md`. A provider/model/deployment-contract change is a reassessment event rather than a silent substitution.

## Learning state

Current demonstrated depth is best described as **substantial implementation exposure with repeated evidence-driven debugging; no formal mastery assessment**.

Recent learning exposure includes:

- responsibility boundaries versus import wiring;
- deterministic source identity and structural windowing versus semantic interpretation;
- global source-line/character provenance preservation;
- product regression versus experiment regression versus live proof;
- explicit unresolved states instead of hidden truncation or heuristic recovery;
- distinguishing environment/provider failures from product evidence failures;
- distinguishing loopback destination intent from actual HTTP transport routing under ambient proxy configuration.

Record stronger ownership only after Ali demonstrates it through explanation, modification, testing, diagnosis, or transfer to changed cases.
