# UpgradePilot Current Memory

**Last updated:** 2026-08-11  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Completed bounded responsibility:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md).
- **Completed Step 7 integration plan:** [`plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`](plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md).
- **Accepted semantic extractor method:** [`docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`](docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md).
- **Accepted source organization:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).
- **Selected next B2 responsibility:** [`plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md), approved bounded plan at commit `d3bf15e62cee8b20188b032f87c8a5c4556245e4`.
- **Implementation status:** Step 1 baseline inspection is complete. The first bounded A→B domain foundation was implemented at commit `fa75caa70c578daf436580fe1151e163455a36f0`, wired into `PublicPullRequestInvestigation` at `9110a514311b1f66dcf54928290a8842731cfe05`, and focused orchestration tests were added at `cf8529f3053b5e56e2b005cad811fb84ab3df837`. Fresh installed-project/full regression is still pending before this slice is treated as fully verified.
- **Current A→B implementation record:** [`working-memory/2026-08-11_B2-first-a-b-impact-applicability-implementation.md`](working-memory/2026-08-11_B2-first-a-b-impact-applicability-implementation.md).
- **Current focused learning artifact:** [`learning/2026-08-10-seven-concept-foundation-pre-a-c-implementation.md`](learning/2026-08-10-seven-concept-foundation-pre-a-c-implementation.md), covering the minimum seven concepts required for implementation-adjacent A→C reasoning. Study it progressively and reinforce its concepts through the implementation/testing work that naturally exercises them.
- **Superseded historical plan:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md), superseded in place at commit `64f273655c43c5a1ec44aa69ae68e96de92f0062`; historical/non-controlling pre-reconciliation and future-D source material only, explicitly not an accepted Conversation-D plan.
- **Old-vs-new plan reconciliation:** [`working-memory/2026-08-10_B2-new-decision-foundation-plan-reconciliation.md`](working-memory/2026-08-10_B2-new-decision-foundation-plan-reconciliation.md); comparison passed and authority transition was subsequently applied.
- **Single product-model reconciliation record:** [`working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md), post-AUDIT-003 consolidated at commit `4923ca94fc241e4675751c3f251b730f324d11d8`.
- **External critical review:** [`audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`](audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md) was audited finding-by-finding; substantive findings were accepted with bounded refinements and incorporated into the reconciliation/model and approved plan.
- **Conversation A:** CLOSED 2026-08-08 — mechanism-specific technical impact-candidate model.
- **Conversation B:** CLOSED 2026-08-09 — candidate-specific applicability, evidence/coverage, negative-inference, and model-authority model.
- **Conversation C:** CLOSED 2026-08-10 — discriminating-target / investigation-selection / stopping model, after C01 and C203 pressure tests and closure review.
- **Conversation D:** **not yet opened**.
- **Frozen cumulative learning snapshot:** [`learning/2026-08-10-product-decision-model-a-b-c-mastery-note.md`](learning/2026-08-10-product-decision-model-a-b-c-mastery-note.md). It represents the original A→C closure state and must not be silently rewritten to include later audit/plan amendments.

## Immediate project action

Complete **verification of the integrated first A→B slice**, then begin the first bounded Step 5 / Conversation-C activation only if the integration is green.

Verification sequence:

- run `tests/test_impact_applicability.py`;
- run `tests/test_python_support_impact.py`;
- run `tests/test_investigation.py` and the nearest Target-Python/orchestration regressions;
- run the full active product deterministic suite in the normal project WSL/Python environment;
- run the installed/import smoke required by the existing proof discipline;
- diagnose/fix any integration defect before expanding semantics.

If those checks are green, the next source responsibility is the first real C activation around the exact target Python declaration. Preserve the distinction between:

```text
grounded A candidate
+
exact target declaration evidence not yet acquired
→ unresolved B proposition
→ discriminating target = exact authoritative target declaration
→ existing read-only exact-head acquisition may be selected
```

and:

```text
same exact acquisition already attempted
+
failed / unavailable
→ do not select the identical investigation again
   without concrete retry justification
```

The second state must instead preserve the unresolved proposition and either select a materially different justified investigation or represent no further executable investigation.

The seven-concept study note remains a **parallel companion** during this work. The current implementation already exercises evidence-vs-inference, open-world/completeness, necessary/sufficient conditions, A candidate formulation, and B applicability semantics.

Do **not** create another implementation plan, open Conversation D, or add a generic investigation/rule/scoring framework merely to create activity.

## Why the selected plan exists

The superseded Transparent Decision plan mixed two responsibilities that the A–C reconciliation has now separated:

```text
PRE-D FOUNDATION
A — technical impact candidate
↓
B — candidate-specific applicability/evidence/composition
↓
C — uncertainty/conflict-driven investigation selection and stopping
```

and:

```text
LATER D
final overall evidence sufficiency
+ repository-policy/residual-risk relationship
+ final maintainer-facing action/synthesis
```

The selected approved plan owns only the first implementable responsibility and explicitly hands off before D. Its creation therefore represents a justified responsibility split rather than duplicate planning.

The old-vs-new reconciliation verified that useful old-plan material was either:

- retained in the approved plan;
- already completed by intervening Target-Python/upstream implementation;
- or explicitly preserved as later D/final-action source material.

## Continuation-critical decision-model guards

Detailed reasoning remains in the reconciliation record. The next implementation must preserve these boundaries.

### A — impact candidate

```text
upstream change mechanism
+ target-relevant exposure/path
+ activation condition(s)
+ possible target-relevant consequence
= mechanism-specific impact candidate
```

Candidate formulation does **not** establish its own exposure, activation, or other component truth. Preserve independently justified versus hypothetical component status.

The implemented `PythonSupportDropImpactCandidate` therefore marks the grounded upstream mechanism as established, target exposure/activation as requiring evaluation, and the consequence as possible rather than established. Exact dependency-transition and target-head identity are retained, and a mismatched upstream interval is rejected.

### B — applicability / coverage

Applicability remains proposition-based for one candidate and exact target/revision/context.

Conceptual states:

```text
established applicable
established not applicable
unresolved
conflicted
```

Preserve:

```text
missing evidence != not applicable
not observed != absent without justified completeness
one established complete path can establish applicability
```

An unqualified `established not applicable` candidate state requires **both**:

```text
every represented viable applicability path sufficiently eliminated
+
path-model coverage sufficiently justified for the candidate-level non-applicability claim
```

Therefore, all represented paths being refuted while path-model coverage remains unresolved/insufficient does **not** justify unqualified `established not applicable`; preserve the path refutations and the coverage limitation.

Keep distinct:

```text
EVIDENCE COVERAGE
PATH-MODEL COVERAGE
CANDIDATE-DISCOVERY COVERAGE
```

Therefore all discovered candidates being non-applicable does not prove transition-level absence of impact without independently justified discovery coverage.

The first A→B implementation explicitly represents proposition evidence coverage and path-model coverage. It intentionally does not implement candidate-discovery completeness or transition-level absence claims.

For the first Python-support candidate, the existing deterministic Target-Python relevance result is decomposed into explicit upstream-mechanism, exact-target-declaration, and range-intersection/activation propositions. Path-level information is preserved when candidate state is composed.

### C — investigation selection

C starts from:

```text
material unresolved OR genuinely conflicted proposition
+
uncertainty/conflict location or reason
```

then derives discriminating target(s) and candidate investigations.

Keep three boundaries distinct:

```text
EPISTEMIC INVESTIGATION VALUE
!= UPGRADEPILOT EXECUTION ADMISSIBILITY
!= MAINTAINER-FACING RECOMMENDABILITY
```

C may produce:

```text
selected next investigation / small conditional sequence
OR no further justified investigation
OR multiple admissible non-dominated alternatives requiring later policy/maintainer context
```

Do not invent numerical VoI or universal cost utility. Observation meaning remains limited by identity/context/temporal/contrast/reconstruction fidelity.

For the first Target-Python C case, distinguish evidence **not yet acquired** from an acquisition **already attempted and failed/unavailable**. The existing exact-head read-only acquisition may be selected in the first case; the identical failed investigation must not be selected again without concrete retry justification in the second. Otherwise select a materially different justified investigation or preserve `no further executable investigation` with unresolved/conflicted state.

Candidate refinement is conditional in the first slice: whenever it occurs, preserve minimum `V1 → triggering observation → V2/refined candidate` lineage, but do not manufacture a refinement case merely to satisfy the plan.

```text
C investigation stop
!= D overall evidence sufficiency
!= final maintainer action
```

## First implementation anchor

The selected plan intentionally reuses the completed Target-Python support-drop path as the first A–C architecture anchor rather than adding a new ecosystem mechanism.

The implemented and now wired A→B path is:

```text
authoritative upstream Python-support drop
↓
PythonSupportDropImpactCandidate
↓
exact target declaration acquisition/interpretation
↓
existing TargetPythonRelevanceResult
↓
explicit upstream / target-declaration / activation propositions
↓
declared-installation-range applicability path
↓
CandidateApplicabilityAssessment
↓
PublicPullRequestInvestigation.python_support_drop_impact_result
```

A grounded non-overlap is intended to produce bounded `established_not_applicable`; overlap produces `established_applicable`; target/comparison uncertainty produces `unresolved`; no grounded upstream claim produces no A candidate.

This does **not** yet implement C because target acquisition still occurs in the pre-existing order. The next semantic refactor must make pre-acquisition unresolved state and investigation selection explicit rather than relabeling the current acquisition as C after the fact.

S001 remains an implementation anchor, not product scope or a known-answer hardcode.

Kedro/Pluggy, pip-audit/CacheControl/urllib3, C01 grpcio-tools, and C203 Buildtest/OpenSSL remain transfer/adversarial cases used to test whether the first-slice design overclaims generality; they do not automatically activate graph, plugin, differential-execution, or historical-reconstruction infrastructure.

## B2 proportionality boundary

The first pre-D implementation/evaluation slice must **not** automatically introduce:

- universal impact-candidate generation;
- arbitrary dependency graph infrastructure;
- universal plugin/framework analysis;
- generic investigation planner/decision tree;
- numerical VoI/ranking;
- generic differential-test executor;
- universal historical-environment reconstruction;
- autonomous target-repository execution;
- complete investigation/exposure taxonomy;
- final D-level sufficiency formula;
- final five-action recommendation engine.

No Charter change is currently justified.

## Latest material verification

The last accepted full implementation proof state remains the completed Target-Python relevance slice. No fresh installed-project/full active product regression has yet been run after the A→B source/integration commits.

Recorded prior verification includes:

- pre-Step-7B active product regression: **323 tests passed**;
- completed Step 6 experiment regression: **27 tests passed**;
- Step 7A exact-commit changelog-path discovery live proof: passed;
- Step 7B–7F focused/full regressions: reported green in WSL at their recorded steps;
- corrected Step 7C local Gemma proof grounded **Python 3.8 support dropped in Soup Sieve 2.8**, exact quote offsets `729:770`;
- final S001 normal-path CLI proof: passed;
- exact target Pydantic head: `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a`;
- exact target declaration: `requires-python >=3.10`;
- final bounded target-Python relevance: `outside_declared_python_range`;
- CI dependency exercise remained honestly `unresolved / dependency_exercise_not_proven`;
- observed final CLI wall-clock duration: approximately **36.546 seconds**.

New first-A→B-session validation:

- isolated applicability-composition harness: **9 tests passed**;
- isolated Python-support candidate/adapter harness: **7 tests passed**;
- combined isolated new-domain-logic proof: **16 tests passed** under Python 3.13.5;
- modified `investigation.py` and focused orchestration-test file: syntax-compiled locally before GitHub write;
- focused orchestration tests are present in the repository but have **not** executed against the installed project in this assistant environment;
- repository GitHub commit-status/CI checks for the first implementation commit returned no configured statuses;
- the assistant local container could not clone GitHub because outbound DNS/network access failed, so no full repository regression is claimed from this session.

The bounded S001 conclusion still means only that the grounded Python-3.8 support-drop concern does not intersect the target's declared Python installation range. It does not establish update safety, universal compatibility, sufficient testing, or a merge recommendation.

## Material blockers / caveats

- No blocker remains for the completed Target-Python Support Relevance responsibility.
- The prior plan-authority-transition blocker is **resolved**; the approved A–C foundation plan is selected.
- Step 1 baseline inspection and the first A→B source/integration work are complete.
- Fresh installed-project/full regression is now the immediate verification gate before expanding into C semantics. The isolated new-domain harness and syntax checks are useful evidence but must not be represented as the full active product suite.
- The seven-concept learning phase is **not an implementation blocker**. It continues alongside building and should be reinforced through the source/test work rather than treated as a prerequisite completion gate.
- Conversation D remains deliberately unopened until bounded A–C implementation evidence exposes a concrete need for D-level overall sufficiency/policy/action semantics.
- Security/non-mutation boundaries remain controlled by `SECURITY.md`; public read-only inspection never authorizes arbitrary target code execution or dependency installation.
- LM Studio loopback/proxy caveats remain owned by `ENVIRONMENT.md`; provider/model/deployment-contract changes remain reassessment events rather than silent substitutions.

## Learning state

Current demonstrated depth remains **substantial implementation exposure with repeated evidence-driven debugging and substantial guided product-model reasoning; no formal mastery assessment**.

The first A→B implementation/integration session directly reinforced evidence-vs-inference, open-world/completeness, necessary/sufficient conditions and AND/OR path reasoning, mechanism-specific candidate formulation, and candidate-specific applicability. It also exposed an important distinction between **evidence missing** and **evidence present but the accepted deterministic method cannot decide**. The seven-concept study guide remains the focused parallel learning companion. Stronger ownership should continue to be built and recorded through explanation, prediction, implementation-adjacent reading, modification, testing, diagnosis, and transfer on changed cases.