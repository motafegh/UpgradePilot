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

Steps 7A changelog discovery, 7B deterministic crossed-release source windows, 7C product local semantic adapter, 7D upstream support-drop composition, and 7E conditional application orchestration have passed their bounded implementation/regression gates. Step 7F controlled integration and full product regressions have been reported green; the selected normal-path live proof remains open because it exposed one bounded upstream repository-resolution generality gap before LM Studio invocation.

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
- Step 7E focused application/CLI/topology tests and full active product regression: **reported green in WSL** on implementation head `0aa54602e86dc5eacc8c30718ad87fb04528dde0`;
- Step 7F controlled end-to-end test and full active product regression: **reported green in WSL**;
- first normal-path S001 CLI run established the exact PR/dependency/CI/package evidence but stopped before semantic inference at `Upstream repository: unsupported_source` because Soup Sieve's exact PyPI metadata exposes its canonical GitHub repository through the `Homepage` project-URL label rather than one of the resolver's previously admitted Source-style labels;
- exact PyPI Soup Sieve 2.8.4 metadata was verified to contain `Homepage: https://github.com/facelessuser/soupsieve`;
- the resolver now admits canonical GitHub `Homepage` repository-association candidates only under the existing exact-file PyPI provenance and repository-agreement trust rule; focused regression and normal-path live rerun remain pending for this correction.

Primary recent evidence:

- [`working-memory/2026-08-05_B2-step-7f-live-upstream-repository-generality-gap.md`](working-memory/2026-08-05_B2-step-7f-live-upstream-repository-generality-gap.md)
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

Continue **Step 7F** from the repository-resolution correction.

1. Validate the provenance-backed `Homepage` repository-association correction:

```bash
python -m unittest discover -s tests -p 'test_upstream_source.py' -v
python -m unittest discover -s tests -v
```

2. Rerun the selected normal-path S001 proof:

```bash
time env -u GITHUB_TOKEN python -m upgradepilot pydantic/pydantic 13432
```

Expected continuation if exact Soup Sieve provenance corroborates the Homepage candidate:

```text
trusted upstream repository: facelessuser/soupsieve
→ crossed releases 2.7 .. 2.8.4
→ exact proposed-version tag/commit
→ exact discovered tagged changelog
→ real local Gemma extraction
→ deterministic grounded Python 3.8 support-drop claim in 2.8
→ exact-head Pydantic pyproject.toml
→ requires-python >=3.10
→ outside_declared_python_range
```

If the live run stops again, preserve and diagnose the smallest newly exposed evidence/provider boundary. Do not hardcode S001 repository identity or bypass provenance/source authority to force the expected answer.

If the normal-path live result reaches the expected bounded relevance state and the active deterministic product regression remains green, record Step 7 as complete and evaluate the parent Target-Python plan completion condition before advancing to the next B2 responsibility.

## Material blockers and caveats

The active Step 7F blocker is **validation of the repository-association generality correction and the resulting normal-path S001 rerun**. No semantic-model change is authorized or currently indicated.

The reusable local deployment and ambient-proxy caveat are in `ENVIRONMENT.md`; stable local-inference transport and untrusted-source controls are in `SECURITY.md`. A provider/model/deployment-contract change is a reassessment event rather than a silent substitution.

## Learning state

Current demonstrated depth is best described as **substantial implementation exposure with repeated evidence-driven debugging; no formal mastery assessment**.

Recent learning exposure includes deterministic authority versus semantic interpretation, source provenance, conditional activation, domain composition versus application orchestration, independent CI evidence, typed unresolved states, local-network/proxy trust boundaries, and the difference between a scenario-specific acquisition proof and generic product repository resolution.
