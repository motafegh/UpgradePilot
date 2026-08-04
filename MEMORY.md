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
- **Selected product increment:** **Step 7D — support-drop runtime evaluation / upstream composition**.

Step 7A changelog discovery, Step 7B deterministic crossed-release source windows, and Step 7C product local semantic adapter have passed their bounded proof gates.

## Latest material verification

The accepted product baseline now includes:

- post-reconciliation active product regression: **323 tests passed** before Step 7B;
- completed Step 6 experiment regression: **27 tests passed**;
- module and installed CLI entry points: **passed**;
- Step 7A exact-commit changelog-path discovery live proof: **passed**;
- Step 5 interval/changelog live proof after credential-contamination diagnosis: **passed**;
- Step 7B focused source-window, GitHub changelog-discovery, source-topology, and full active product regressions: **passed in WSL** on implementation head `ec80105cabca9515c74a89549119f40415df6c0d`;
- Step 7C focused semantic-adapter and full active product regressions: **passed in WSL**;
- Step 7C first live attempt exposed ambient proxy contamination: loopback HTTP was routed through Privoxy on `127.0.0.1:8080` despite the shell's wildcard-style `NO_PROXY` entries;
- direct no-proxy control reached LM Studio at `127.0.0.1:12345` with HTTP 200;
- product/local-proof LM Studio transport now disables ambient proxy inheritance with `requests.Session.trust_env = False`;
- corrected real S001 Step 7C live proof: **passed**;
- live Gemma inference returned one candidate for **Python 3.8 support dropped in Soup Sieve 2.8**, reconstructed exact quote offsets `729:770`, and `validate_support_drop_candidates(...)` grounded the claim;
- observed live inference latency for that proof: approximately **20.68 seconds**.

Primary recent evidence:

- [`working-memory/2026-08-05_B2-step-7c-live-semantic-extractor-proof.md`](working-memory/2026-08-05_B2-step-7c-live-semantic-extractor-proof.md)
- [`working-memory/2026-08-05_B2-step-7c-lm-studio-proxy-contamination-diagnosis.md`](working-memory/2026-08-05_B2-step-7c-lm-studio-proxy-contamination-diagnosis.md)
- [`working-memory/2026-08-05_B2-step-7b-crossed-release-source-window-validation.md`](working-memory/2026-08-05_B2-step-7b-crossed-release-source-window-validation.md)

Detailed source topology, experiment scores, historical incident narratives, and full test output belong to their dated evidence records, source/tests, accepted ADRs, `ENVIRONMENT.md`, and `SECURITY.md` rather than this live continuation file.

## Retained semantic trust boundary

The accepted and now live-proven bounded path is:

```text
admitted crossed-release source text
→ bounded local candidate extraction
→ deterministic exact-source reconstruction
→ validate_support_drop_candidates(...)
→ grounded support-drop claim or explicit problem
```

The model does not own source authority, package/version identity, exact source text/offsets, target relevance, compatibility, safety, or maintainer action.

## Exact continuation

Resume with **Step 7D — support-drop runtime evaluation**.

Required responsibility:

```text
AuthoritativeUpstreamIntervalEvidence
→ complete Step 7B source-window construction
→ Step 7C LocalSupportDropExtractor
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
→ UpstreamSupportDropClaimResult
```

Implement the smallest clear upstream-domain composition. The deterministic validator remains the only trust-admission owner. Window/provider/candidate failures must remain explicit unresolved problems and may not synthesize a grounded claim.

Do **not** activate target `pyproject.toml` acquisition or target-Python relevance during Step 7D. That application sequencing belongs to Step 7E in `src/upgradepilot/investigation.py`.

## Material blockers and caveats

No known product blocker currently prevents Step 7D.

The reusable local deployment and ambient-proxy caveat are in `ENVIRONMENT.md`; stable local-inference transport and untrusted-source controls are in `SECURITY.md`. A provider/model/deployment-contract change is a reassessment event rather than a silent substitution.

## Learning state

Current demonstrated depth is best described as **substantial implementation exposure with repeated evidence-driven debugging; no formal mastery assessment**.

Recent learning exposure includes:

- deterministic evidence authority versus model semantic candidate generation;
- exact source-line/offset reconstruction and trust admission;
- product regression versus live-model proof;
- loopback destination intent versus actual proxy-mediated HTTP routing;
- responsibility separation between upstream composition and later application orchestration.

Record stronger ownership only after Ali demonstrates it through explanation, modification, testing, diagnosis, or transfer to changed cases.
