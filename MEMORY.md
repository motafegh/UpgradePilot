# UpgradePilot Current Memory

**Last updated:** 2026-08-08  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Completed bounded responsibility:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md).
- **Completed Step 7 integration plan:** [`plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`](plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md).
- **Accepted semantic method:** [`docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`](docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md).
- **Accepted source organization:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).
- **Selected next B2 responsibility:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md), with implementation intentionally paused pending whole-product decision-model reconciliation.
- **Active reconciliation record:** [`working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md).
- **Conversation A:** closed on 2026-08-08 after explicit impact-model closure review.
- **Active conversation:** Conversation B — applicability and investigation activation.
- **Immediate session action:** define what it means for one impact candidate to be applicable, not applicable, unresolved, or conflicted for one exact target/revision/context before freezing runtime states or implementation structures.

Steps 7A through 7F are complete. The parent Target Python Support Relevance responsibility is behavior-valid for its admitted bounded question. No compatibility, safety, merge/defer, or maintainer recommendation is activated by this completion.

The previously requested end-to-end learning walkthrough of the completed implementation remains planned, but Ali explicitly chose to first explore and reconcile the future whole-product decision model so that learning and later implementation proceed against the best current conceptual direction.

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
- observed wall-clock duration for the complete final normal CLI proof: approximately **36.546 seconds**;
- whole-product document audit before the next decision layer found that stable evidence/authority/conditional-stopping principles remain strong, while the historical five-action framing and July decision-contract draft require reconciliation against the current evidence engine before implementation;
- Conversation A accepted the domain relation `upstream change + exposure relationship/path + activation condition(s) + possible consequence = impact candidate`, with `impact candidate` representing the complete proposition rather than a separate intermediate event;
- Conversation A closure review found no remaining foundational ambiguity that would make Conversation B's applicability model fundamentally wrong; runtime classes/enums/schema and complete impact/exposure taxonomies remain deliberately uncommitted.

Primary recent evidence:

- [`working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md)
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

### 1. Whole-product decision-model reconciliation

Use [`working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md) as the progressive dated record for the current discussion.

Proceed through four whole-product conversations:

```text
A. dependency-update impact/problem model                  — CLOSED
B. target applicability and investigation activation      — ACTIVE
C. best next investigation / targeted-check selection
D. evidence sufficiency, stopping, and maintainer-facing result
```

Do not use B2/B3/B4 stage boundaries to prevent whole-product reasoning during this reconciliation. Do not implement the current transparent-decision draft or modify the charter/action vocabulary until the discussion has established whether those concepts remain correct.

Historical simulation outcomes and the July decision-contract draft are evidence, not current machine labels. The non-controlling product-ambition proposal may provide candidate ideas but must be independently evaluated rather than inherited.

Conversation A closed with this accepted domain structure:

```text
upstream change
+ exposure relationship/path
+ activation condition(s)
+ possible target-relevant consequence
= impact candidate
```

`Impact candidate` is the complete proposition, not a separate event between change and exposure. This is a domain decision, not yet a runtime class/schema decision.

The active Conversation-B question is:

> For one specific impact candidate and one exact target/revision/context, what proposition is UpgradePilot trying to establish when it says that candidate is applicable, not applicable, unresolved, or conflicted?

Conversation B should first establish the semantics and boundaries of applicability before choosing runtime state vocabularies, repository-inspection techniques, or implementation structures.

### 2. Repository changes after conceptual closure

Once the reconciliation reaches accepted decisions, use its final decision/repository-change register to determine which stable owners actually require change, potentially including the charter, README, route, transparent-decision plan, specifications, and an ADR if a consequential decision architecture is accepted.

Do not create those changes merely because the working record lists them as candidates.

### 3. End-to-end implementation learning remains required

Ali still wants a complete end-to-end learning walkthrough of the implemented system using real S001 and S004 inputs/cases. After the forward product-model discussion reaches a useful stopping point, return to that learning work before or alongside the next substantial implementation as appropriate.

Learning progress must distinguish introduction/exposure from demonstrated mastery.

## Material blockers and caveats

No blocker remains for the completed Target-Python relevance responsibility.

The next decision/recommendation implementation is intentionally paused until the whole-product impact/investigation/decision model is reconciled sufficiently to avoid encoding stale or misleading assumptions.

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
- live end-to-end proof as a mechanism for discovering integration assumptions that component tests missed;
- product-level distinction among evidence collection, impact/applicability reasoning, investigation planning, sufficiency/stopping, repository policy, and maintainer-facing action;
- Conversation-A domain modeling of upstream change, exposure, activation, consequence, impact candidates, technical-impact boundaries, and neighboring non-impact decision context.

Record stronger ownership only after Ali demonstrates it through explanation, modification, testing, diagnosis, or transfer to changed cases.