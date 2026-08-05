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
- **Selected product increment:** **Step 7F — controlled and live end-to-end proof**.

Steps 7A changelog discovery, 7B deterministic crossed-release source windows, 7C product local semantic adapter, 7D upstream support-drop composition, and 7E conditional application orchestration have passed their bounded implementation/regression gates.

## Latest material verification

The accepted baseline now includes:

- post-reconciliation active product regression: **323 tests passed** before Step 7B;
- completed Step 6 experiment regression: **27 tests passed**;
- Step 7A exact-commit changelog-path discovery live proof: **passed**;
- Step 7B focused and full active product regressions: **passed in WSL**;
- Step 7C focused/full regressions and corrected real S001 local-model proof: **passed**;
- real Step 7C Gemma inference grounded **Python 3.8 support dropped in Soup Sieve 2.8**, with exact quote offsets `729:770`;
- the first Step 7C live attempt exposed ambient Privoxy contamination; the product LM Studio loopback transport now disables ambient proxy inheritance with `requests.Session.trust_env = False`;
- Step 7D focused upstream-composition regression and full active product regression: **reported green in WSL**;
- Step 7E focused application/CLI/topology tests and full active product regression: **reported green in WSL** on implementation head `0aa54602e86dc5eacc8c30718ad87fb04528dde0`.

Primary recent evidence:

- [`working-memory/2026-08-05_B2-step-7e-conditional-orchestration-validation.md`](working-memory/2026-08-05_B2-step-7e-conditional-orchestration-validation.md)
- [`working-memory/2026-08-05_B2-step-7d-upstream-composition-validation.md`](working-memory/2026-08-05_B2-step-7d-upstream-composition-validation.md)
- [`working-memory/2026-08-05_B2-step-7c-live-semantic-extractor-proof.md`](working-memory/2026-08-05_B2-step-7c-live-semantic-extractor-proof.md)
- [`working-memory/2026-08-05_B2-step-7c-lm-studio-proxy-contamination-diagnosis.md`](working-memory/2026-08-05_B2-step-7c-lm-studio-proxy-contamination-diagnosis.md)
- [`working-memory/2026-08-05_B2-step-7b-crossed-release-source-window-validation.md`](working-memory/2026-08-05_B2-step-7b-crossed-release-source-window-validation.md)

## Current normal application flow

```text
DependencyVersionChange
├── independent CI dependency-exercise branch
└── upstream branch
    → exact PyPI release
    → trusted upstream repository
    → PyPI release index / complete crossed-release selection
    → canonical proposed-version Git tag (`<version>` then `v<version>` only when explicitly unavailable)
    → exact-commit changelog discovery + acquisition
    → authoritative interval composition
    → deterministic crossed-release source window
    → adopted local Gemma candidate extraction
    → deterministic exact-source reconstruction
    → validate_support_drop_candidates(...)
    → grounded support-drop claim?
        ├── no  → target pyproject.toml remains inactive
        └── yes → exact-head pyproject.toml
                  → TargetPythonDeclaration
                  → target-Python relevance
```

The model does not own source authority, package/version identity, exact source text/offsets, target relevance, compatibility, safety, or maintainer action.

## Exact continuation

Complete **Step 7F**.

1. Add one controlled integration proof that uses fake/captured provider/source responses but the real Step 7B source-window, Step 7C adapter/reconstruction, Step 7D trust admission, and Step 7E conditional application path. It must prove both activation and non-activation without live model inference.
2. Run the selected normal-path live proof against S001:

```text
pydantic/pydantic PR #13432
soupsieve 2.6 → 2.8.4
expected grounded upstream claim: Python 3.8 support dropped in 2.8
historical target declaration: requires-python >=3.10
expected bounded relevance: outside_declared_python_range
```

Use the normal CLI/application path, not the special Step 7C semantic proof tool. For public read-only proof, avoid accidental ambient GitHub authentication if the local `GITHUB_TOKEN` is not intentionally part of the proof.

If controlled tests, full active product regression, and the normal-path live S001 proof pass, record Step 7 as complete and advance to the parent plan's next authorized increment. Do not extend Step 7 into compatibility, safety, merge/defer recommendation, general release summarization, new semantic categories, or repository mutation.

## Material blockers and caveats

No known product blocker currently prevents Step 7F.

The reusable local deployment and ambient-proxy caveat are in `ENVIRONMENT.md`; stable local-inference transport and untrusted-source controls are in `SECURITY.md`. A provider/model/deployment-contract change is a reassessment event rather than a silent substitution.

## Learning state

Current demonstrated depth is best described as **substantial implementation exposure with repeated evidence-driven debugging; no formal mastery assessment**.

Recent learning exposure includes deterministic authority versus semantic interpretation, source provenance, conditional activation, domain composition versus application orchestration, independent CI evidence, typed unresolved states, and local-network/proxy trust boundaries.
