# UpgradePilot Current Memory

**Last updated:** 2026-08-05  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Completed bounded responsibility:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md).
- **Completed Step 7 integration plan:** [`plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`](plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md).
- **Accepted semantic method:** [`docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`](docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md).
- **Accepted source organization:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).
- **Selected next B2 responsibility:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md).
- **Immediate session action:** perform Ali's requested end-to-end learning walkthrough of the completed Target-Python Support Relevance milestone before implementing the next decision responsibility.

Steps 7A through 7F are complete. The parent Target Python Support Relevance responsibility is behavior-valid for its admitted bounded question. No compatibility, safety, merge/defer, or maintainer recommendation is activated by this completion.

## Latest material verification

The accepted baseline now includes:

- post-reconciliation active product regression: **323 tests passed** before Step 7B;
- completed Step 6 experiment regression: **27 tests passed**;
- Step 7A exact-commit changelog-path discovery live proof: **passed**;
- Step 7B focused and full active product regressions: **passed in WSL**;
- Step 7C focused/full regressions and corrected real S001 local-model proof: **passed**;
- real Step 7C Gemma inference grounded **Python 3.8 support dropped in Soup Sieve 2.8**, with exact quote offsets `729:770`;
- Step 7D focused upstream-composition regression and full active product regression: **reported green in WSL**;
- Step 7E focused application/CLI/topology tests and full active product regression: **reported green in WSL**;
- Step 7F controlled end-to-end test and complete active product regression: **reported green in WSL**;
- Step 7F live proof first exposed a real upstream-repository generality gap: Soup Sieve publishes its canonical GitHub repository under PyPI `Homepage`; the resolver now accepts canonical GitHub Homepage as a repository-association candidate only when exact-file PyPI provenance independently corroborates the same repository;
- Step 7F live proof then exposed a real orchestration/interface defect: `PyPIReleaseClient` was incorrectly used for package-wide release-index acquisition; the application now uses separate `PyPIReleaseClient` and `PyPIReleaseIndexClient` responsibilities, and spec-constrained test mocks protect that boundary;
- final normal-path S001 CLI proof: **passed**;
- normal application established `facelessuser/soupsieve` with **2 of 2** exact distribution files covered by PyPI provenance;
- complete crossed-release interval: **2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4**;
- live normal-path semantic result: **grounded Python 3.8 support drop introduced in Soup Sieve 2.8**;
- exact-head Pydantic target source: `pyproject.toml` at `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a`, blob `8271997ab85caa1af522954812a2749784432dc7`;
- exact target declaration: **`requires-python >=3.10`**;
- final bounded relevance: **`outside_declared_python_range`**;
- CI dependency exercise remained honestly **unresolved / dependency_exercise_not_proven** and was not promoted into a compatibility or safety claim;
- observed wall-clock duration for the complete final normal CLI proof: approximately **36.546 seconds**.

Primary recent evidence:

- [`working-memory/2026-08-05_B2-step-7f-normal-path-live-s001-proof.md`](working-memory/2026-08-05_B2-step-7f-normal-path-live-s001-proof.md)
- [`working-memory/2026-08-05_B2-step-7f-release-index-client-integration-defect.md`](working-memory/2026-08-05_B2-step-7f-release-index-client-integration-defect.md)
- [`working-memory/2026-08-05_B2-step-7f-live-upstream-repository-generality-gap.md`](working-memory/2026-08-05_B2-step-7f-live-upstream-repository-generality-gap.md)
- [`working-memory/2026-08-05_B2-step-7e-conditional-orchestration-validation.md`](working-memory/2026-08-05_B2-step-7e-conditional-orchestration-validation.md)
- [`working-memory/2026-08-05_B2-step-7d-upstream-composition-validation.md`](working-memory/2026-08-05_B2-step-7d-upstream-composition-validation.md)
- [`working-memory/2026-08-05_B2-step-7c-live-semantic-extractor-proof.md`](working-memory/2026-08-05_B2-step-7c-live-semantic-extractor-proof.md)

## Behavior-valid Target-Python relevance path

```text
public repository + PR number
→ exact PR identity and complete changed-file evidence
→ trusted DependencyVersionChange
├── independent bounded CI dependency-exercise branch
└── upstream/target relevance branch
    → exact PyPI proposed release via PyPIReleaseClient
    → trusted upstream GitHub repository from project-link candidate + exact-file provenance agreement
    → package-wide PyPI release index via PyPIReleaseIndexClient
    → complete old-exclusive/proposed-inclusive crossed-release interval
    → canonical exact proposed-version Git tag
    → exact-commit changelog discovery and acquisition
    → authoritative tagged-changelog interval evidence
    → complete deterministic crossed-release Markdown source window
    → bounded local Gemma candidate extraction
    → deterministic exact-source reconstruction
    → validate_support_drop_candidates(...)
    → GroundedPythonSupportDropClaim?
        ├── no  → target Python remains inactive / explicit unresolved state
        └── yes → exact-head target pyproject.toml
                  → [project].requires-python
                  → deterministic target-Python relevance
```

The model does not own source authority, package/version identity, release ordering, exact source text/offsets, target relevance, compatibility, safety, or maintainer action.

## Completed bounded conclusion for S001

```text
Soup Sieve 2.6 -> 2.8.4
→ crossed release 2.8 explicitly drops Python 3.8 support
→ deterministic validation grounds that upstream claim
→ Pydantic exact PR head declares requires-python >=3.10
→ no stable Python 3.8.Z version is admitted by the target declaration
→ outside_declared_python_range
```

This means only that the grounded upstream Python 3.8 support-drop concern does not intersect the target's declared Python installation range under the accepted method. It does not mean the update is safe, universally compatible, sufficiently tested, or recommended for merge.

## Exact continuation

### 1. Learning before new implementation

Ali requested a complete end-to-end learning session after this milestone. Before implementing the next decision responsibility, walk the completed real S001 path from CLI input through the actual owners, important source types/functions, trust boundaries, inputs/outputs, conditional activation, live-model role, deterministic grounding, target comparison, and the Step 7F debugging lessons.

Learning progress must distinguish introduction/exposure from demonstrated mastery.

### 2. Resume B2 Transparent Decision Method after the walkthrough

Use:

- [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md) as the position-neutral controlling plan;
- [`working-memory/2026-07-28_B2-transparent-decision-method.md`](working-memory/2026-07-28_B2-transparent-decision-method.md) as historical/design context, not live authority.

That working record predates the current responsibility-based source topology and the now-completed Target-Python relevance branch. Reconcile its evidence assumptions against the current product before freezing a decision contract or implementing recommendation policy.

The next consequential decision/recommendation method still requires concrete explanation and Ali approval under the existing plan. Do not silently convert target non-overlap, green CI, source authority, or a model result into `merge`, `safe`, or `compatible`.

## Material blockers and caveats

No blocker remains for the completed Target-Python relevance responsibility.

The next B2 decision responsibility remains intentionally unimplemented until its current evidence contract, sufficiency/stopping rules, action meanings, semantic needs, and proof plan are reconciled and approved.

The reusable LM Studio loopback/proxy caveat remains in `ENVIRONMENT.md`; stable local-inference and untrusted-source controls remain in `SECURITY.md`. Provider/model/deployment-contract changes remain reassessment events rather than silent substitutions.

## Learning state

Current demonstrated depth is best described as **substantial implementation exposure with repeated evidence-driven debugging; no formal mastery assessment**.

Recent learning exposure includes:

- exact PR/base/head evidence and representation-specific dependency extraction;
- domain evidence types versus application orchestration;
- independent CI and upstream investigation branches;
- PyPI exact-release identity versus package-wide release-index identity;
- project-link discovery candidates versus independently corroborating publisher provenance;
- crossed-release authority and exact immutable tag/changelog binding;
- deterministic Markdown structure extraction versus model semantic interpretation;
- bounded LLM candidate generation versus deterministic trust admission;
- exact source-line/offset reconstruction;
- conditional target evidence activation;
- Python specifier/line relevance without compatibility overclaiming;
- ambient proxy contamination of loopback inference traffic;
- scenario-specific proof versus generic product behavior;
- unrestricted mocks hiding concrete-interface integration defects;
- live end-to-end proof as a mechanism for discovering integration assumptions that component tests missed.

Record stronger ownership only after Ali demonstrates it through explanation, modification, testing, diagnosis, or transfer to changed cases.
