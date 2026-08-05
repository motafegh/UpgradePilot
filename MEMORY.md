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
- **Selected product increment:** **Step 7E — conditional application orchestration**.

Steps 7A changelog discovery, 7B deterministic crossed-release source windows, 7C product local semantic adapter, and 7D upstream support-drop composition have passed their bounded proof gates. Step 7E application/CLI implementation is now present on `main`; its focused and full regression gates remain pending.

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
- product/local-proof LM Studio transport disables ambient proxy inheritance with `requests.Session.trust_env = False`;
- corrected real S001 Step 7C live proof: **passed**;
- live Gemma inference returned one candidate for **Python 3.8 support dropped in Soup Sieve 2.8**, reconstructed exact quote offsets `729:770`, and `validate_support_drop_candidates(...)` grounded the claim;
- observed live inference latency for that proof: approximately **20.68 seconds**;
- Step 7D focused upstream-composition regression and full active product regression: **reported green in WSL** on implementation head `3ccd5464692d200e026248e2acc4989fac5e3836`;
- Step 7E implementation currently reaches head `206be14c2dc248189c0e07c87436d8558d24fe94` and awaits WSL validation.

Primary recent evidence:

- [`working-memory/2026-08-05_B2-step-7d-upstream-composition-validation.md`](working-memory/2026-08-05_B2-step-7d-upstream-composition-validation.md)
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

## Step 7E implementation now present

`src/upgradepilot/investigation.py` now coordinates:

```text
DependencyVersionChange
├── existing CI dependency-exercise branch
└── exact package release
    → trusted upstream repository
    → PyPI release index / crossed-release selection
    → canonical proposed-version Git tag (`<version>` then `v<version>` only if unavailable)
    → exact-commit changelog discovery and acquisition
    → authoritative interval composition
    → Step 7D support-drop evaluation
    → grounded claim?
        ├── no  → target pyproject.toml is not acquired
        └── yes → exact-head pyproject.toml
                  → target declaration
                  → target-Python relevance
```

The investigation result preserves intermediate upstream states so source/interval stops remain distinguishable from semantic no-claim results. `cli.py` renders these typed states and no longer assumes target-Python evidence exists for every supported dependency.

## Exact continuation

Validate Step 7E in WSL. Required immediate gates:

```bash
python -m unittest discover -s tests -p 'test_investigation.py' -v
python -m unittest discover -s tests -p 'test_cli.py' -v
python -m unittest discover -s tests -p 'test_source_topology.py' -v
python -m unittest discover -s tests -v
```

If green, record Step 7E as passed and continue to **Step 7F — controlled and live end-to-end proof**. Do not bypass failed sequencing tests by weakening the conditional target-activation rule.

## Material blockers and caveats

No known product blocker currently prevents Step 7E validation.

The reusable local deployment and ambient-proxy caveat are in `ENVIRONMENT.md`; stable local-inference transport and untrusted-source controls are in `SECURITY.md`. A provider/model/deployment-contract change is a reassessment event rather than a silent substitution.

## Learning state

Current demonstrated depth is best described as **substantial implementation exposure with repeated evidence-driven debugging; no formal mastery assessment**.

Recent learning exposure includes:

- deterministic evidence authority versus model semantic candidate generation;
- exact source-line/offset reconstruction and trust admission;
- upstream-domain composition versus application orchestration;
- conditional evidence activation instead of eager collection;
- CI as an independent evidence branch;
- preserving intermediate typed problems without collapsing them into one generic failure;
- product regression versus live-model proof;
- loopback destination intent versus actual proxy-mediated HTTP routing.

Record stronger ownership only after Ali demonstrates it through explanation, modification, testing, diagnosis, or transfer to changed cases.
