# UpgradePilot Current Memory

**Last updated:** 2026-08-10  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Completed bounded responsibility:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md).
- **Completed Step 7 integration plan:** [`plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`](plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md).
- **Accepted semantic method:** [`docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`](docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md).
- **Accepted source organization:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).
- **Selected next B2 responsibility:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md), with implementation intentionally paused pending whole-product decision-model reconciliation.
- **Single active reconciliation record:** [`working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md). Conversations A→D remain in this one progressive record.
- **Conversation A:** closed on 2026-08-08 after explicit impact-model closure review.
- **Conversation B:** closed on 2026-08-09 after proposition/evidence/model-authority reconciliation, semantic-heavy Kedro/Pluggy pressure test, and explicit closure review.
- **Active conversation:** Conversation C — best next investigation/check.
- **Immediate session action:** run Conversation-C Pressure Test 2 using C203 Buildtest/OpenSSL. Test the opposite pressure from C01: the ideal historical discriminating observation may be unavailable, reconstruction may become progressively less authoritative/more costly, and the correct result may be `unresolved + no further justified investigation`.

Steps 7A through 7F are complete. The parent Target Python Support Relevance responsibility is behavior-valid for its admitted bounded question. No compatibility, safety, merge/defer, or maintainer recommendation is activated by this completion.

The end-to-end learning walkthrough of the completed implementation remains planned, but forward whole-product decision-model reconciliation currently continues through Conversation C so later implementation is based on the best current product semantics rather than stale decision labels.

## Latest material verification

The accepted baseline includes:

- post-reconciliation active product regression: **323 tests passed** before Step 7B;
- completed Step 6 experiment regression: **27 tests passed**;
- Step 7A exact-commit changelog-path discovery live proof: **passed**;
- Step 7B focused and full active product regressions: **passed in WSL**;
- Step 7C focused/full regressions and corrected real S001 local-model proof: **passed**;
- real Step 7C Gemma inference grounded **Python 3.8 support dropped in Soup Sieve 2.8**, with exact quote offsets `729:770`;
- Step 7D focused upstream-composition regression and full active product regression: **reported green in WSL**;
- Step 7E focused application/CLI/topology tests and full active product regression: **reported green in WSL**;
- Step 7F controlled end-to-end test and complete active product regression: **reported green in WSL**;
- Step 7F live proof exposed and corrected the PyPI upstream-repository generality gap: Soup Sieve publishes its canonical GitHub repository under PyPI `Homepage`; the resolver now accepts canonical GitHub Homepage as a repository-association candidate only when exact-file PyPI provenance independently corroborates the same repository;
- Step 7F live proof exposed and corrected an orchestration/interface defect: `PyPIReleaseClient` was incorrectly used for package-wide release-index acquisition; the application now uses separate `PyPIReleaseClient` and `PyPIReleaseIndexClient` responsibilities, with spec-constrained mocks protecting the boundary;
- final normal-path S001 CLI proof: **passed**;
- normal application established `facelessuser/soupsieve` with **2 of 2** exact distribution files covered by PyPI provenance;
- complete crossed-release interval: **2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4**;
- live normal-path semantic result: **grounded Python 3.8 support drop introduced in Soup Sieve 2.8**;
- exact-head Pydantic target source: `pyproject.toml` at `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a`, blob `8271997ab85caa1af522954812a2749784432dc7`;
- exact target declaration: **`requires-python >=3.10`**;
- final bounded relevance: **`outside_declared_python_range`**;
- CI dependency exercise remained honestly **unresolved / dependency_exercise_not_proven** and was not promoted into compatibility or safety;
- observed wall-clock duration for the complete final normal CLI proof: approximately **36.546 seconds**;
- whole-product document audit found stable evidence/authority/conditional-stopping principles strong while historical five-action framing and the July decision-contract draft require reconciliation against the current evidence engine;
- Conversation A accepted `upstream change + exposure relationship/path + activation condition(s) + possible consequence = impact candidate`, with `impact candidate` as the complete proposition;
- Conversation A closure found no foundational ambiguity threatening Conversation B; runtime classes/enums/schema and complete exposure taxonomy remain deliberately uncommitted;
- Conversation B accepted proposition-based applicability per mechanism-specific candidate, candidate-specific necessary/alternative propositions, and `established applicable`, `established not applicable`, `unresolved`, `conflicted` as evidence-justification semantics rather than runtime enum commitments;
- Conversation B accepted open-world default reasoning, proposition-local closed-world boundaries, bounded negative evidence, universe-of-discourse discipline, and the requirement that completeness itself be justified;
- Conversation B accepted the deterministic-shell / bounded-semantic-responsibility direction: identity/authority/coverage are separately justified, deterministic decision procedures preferred where reliable, semantic output attributed/grounded, and candidate composition mechanical once proposition states/logic are explicit;
- Kedro/Pluggy pressure testing preserved `uses dependency != participates in affected mechanism != relies on specific changed property`, with insufficiently grounded semantic alignment remaining `unresolved` rather than becoming an opaque model verdict;
- explicit Conversation-B closure review **passed** across S001, Buildtest/OpenSSL, pip-audit multi-hop, Kedro/Pluggy dynamic/semantic behavior, and the build/codegen comparator;
- Conversation C distinguishes evidence source, investigation/check, observation, uncertainty location/reason, and discriminating target; distinguishes relevant evidence from discriminating evidence and information gain from decision-relevant information gain; distinguishes resolution from useful uncertainty reduction; and separates hard admissibility from softer preference;
- Conversation C has a provisional comparison/sequencing model covering proposition-relative dominance/Pareto reasoning, candidate-logic/shared-gate pruning leverage, complementary versus redundant/corroborating evidence, earned observation-driven escalation, non-compensatory hard constraints, qualitative comparison instead of fake scoring, conditional/adaptive investigation policies, state-space-explosion risk, and bounded lookahead/re-evaluation;
- **Conversation-C Pressure Test 1 (C01 code generation) passed with refinements:** a non-cheapest targeted differential regeneration can rationally be the first substantive investigation when it directly targets a decisive high-pruning gate; static→semantic→dynamic is not a universal ordering; admissibility must include a minimal experiment pre-flight; and post-execution results still require evidence validation;
- Pressure Test 1 exposed two new provisional refinements: **contrast validity** (the old/new comparison must represent the proposition being asked, with confounders controlled or accounted for) and **investigation-to-candidate feedback** (an observation that reveals a different mechanism may require candidate refinement/new candidate formulation rather than only updating an existing proposition);
- these Conversation-C principles remain provisional pending at least the complementary Buildtest/OpenSSL pressure test.

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

Use only [`working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md) as the progressive A→D reconciliation record.

Proceed through:

```text
A. dependency-update impact/problem model                  — CLOSED 2026-08-08
B. target applicability and investigation activation      — CLOSED 2026-08-09
C. best next investigation / targeted-check selection     — ACTIVE
D. evidence sufficiency, stopping, and maintainer-facing result
```

Do not use B2/B3/B4 stage boundaries to prevent whole-product reasoning. Historical simulation outcomes and the July decision-contract draft remain evidence, not current machine labels. Do not implement the old transparent-decision draft or modify charter/action vocabulary until reconciliation establishes what remains correct.

Conversation A closed with:

```text
upstream change
+ exposure relationship/path
+ activation condition(s)
+ possible target-relevant consequence
= impact candidate
```

Conversation B closed with proposition-based applicability and evidence/model-authority semantics capable of preserving precise unresolved propositions without forcing LLM verdicts or converting missing evidence to non-applicability.

Conversation-C Pressure Test 1 has passed with two refinements but has not yet closed C.

The active Conversation-C action is:

> **Run Pressure Test 2 on C203 Buildtest/OpenSSL: when the ideal exact historical observation may no longer be available, determine how UpgradePilot should compare weaker evidence, historical reconstruction, narrowing, and stopping without converting imperfect evidence into false resolution or escalating indefinitely.**

Pressure-test specifically:

- feasibility versus theoretical discrimination;
- historical identity/time authority;
- reconstruction fidelity and evidential status;
- dominance/qualitative comparison when the ideal check is infeasible;
- useful uncertainty reduction versus resolution;
- escalation stopping and disproportionate reconstruction;
- justified `unresolved + no further supported investigation`;
- whether contrast validity generalizes usefully beyond code generation;
- whether C can own investigation stopping enough to select no-further-check while leaving final evidence sufficiency/maintainer synthesis to D.

After Pressure Test 2, explicitly review which C principles can be promoted, which remain provisional, and whether one more structurally distinct test is necessary before C closure.

Do not yet freeze a numerical Value-of-Information score, universal ranking/planner schema, fixed investigation taxonomy/checklist, or autonomous executor.

### 2. Repository changes after conceptual closure

Once reconciliation reaches accepted decisions, use its repository-change register to determine which stable owners actually require change, potentially including the charter, README, route, transparent-decision plan, specifications, and an ADR if consequential architecture/method is accepted.

Do not create those changes merely because they are candidates.

### 3. End-to-end implementation learning remains required

A complete end-to-end learning walkthrough of the implemented system using real S001 and S004 remains required. After the forward product-model discussion reaches a useful stopping point, return to that learning work before or alongside the next substantial implementation as appropriate.

Learning progress must distinguish introduction/exposure from demonstrated mastery.

## Material blockers and caveats

No blocker remains for the completed Target-Python relevance responsibility.

The next general decision/recommendation implementation remains intentionally paused while Conversation C resolves the immediate missing semantic link between unresolved applicability and useful investigation selection. This does not require completing all of C/D before implementation; re-run the implementation-handoff check at C closure.

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
- deterministic Markdown extraction versus semantic interpretation;
- bounded LLM candidate generation versus deterministic trust admission;
- exact source-line/offset reconstruction;
- conditional target evidence activation;
- Python specifier/line relevance without compatibility overclaiming;
- ambient proxy contamination of loopback inference traffic;
- scenario-specific proof versus generic product behavior;
- unrestricted mocks hiding concrete-interface integration defects;
- live end-to-end proof as a mechanism for finding integration assumptions component tests missed;
- product-level distinction among evidence collection, impact/applicability reasoning, investigation planning, sufficiency/stopping, repository policy, and maintainer-facing action;
- Conversation-A impact/exposure/activation/consequence modeling;
- Conversation-B proposition-based applicability, necessary/sufficient conditions, alternative paths, negative evidence, open/closed-world reasoning, universe-of-discourse, conflict normalization, deterministic/semantic boundaries, and applicability-versus-maintainer authority;
- Kedro/Pluggy semantic-heavy pressure testing and `uses dependency != participates in affected mechanism != relies on specific changed property`;
- Conversation-C discrimination, uncertainty-location/discriminating-target reasoning, resolution versus reduction, admissibility versus preference, dominance/Pareto comparison, logical pruning/shared-gate leverage, complementarity/corroboration, earned escalation, non-compensatory hard constraints, adaptive conditional policies, bounded lookahead, differential-test contrast validity, post-execution evidence validation, and investigation-result feedback into candidate refinement.

Record stronger ownership only after demonstrated explanation, modification, testing, diagnosis, or transfer to changed cases.
