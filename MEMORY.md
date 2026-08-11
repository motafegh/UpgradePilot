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
- **Implementation status:** Step 1 baseline inspection is complete. The first bounded technical impact-candidate and candidate-specific applicability foundation was implemented at `fa75caa70c578daf436580fe1151e163455a36f0`, wired into `PublicPullRequestInvestigation` at `9110a514311b1f66dcf54928290a8842731cfe05`, and focused orchestration tests were added at `cf8529f3053b5e56e2b005cad811fb84ab3df837`. The explicit pre-acquisition target-evidence state was added at `4bc5061c084640606435595c5d95978b8f7ea554` with its focused test at `0f57e7ab347a8d13c86991c44605178eac085570`. The integrated slice is now locally verified in the normal project environment: **384 tests passed** and installed/import smoke passed.
- **Current implementation record:** [`working-memory/2026-08-11_B2-first-a-b-impact-applicability-implementation.md`](working-memory/2026-08-11_B2-first-a-b-impact-applicability-implementation.md).
- **Current local verification record:** [`working-memory/2026-08-11_B2-impact-applicability-local-verification.md`](working-memory/2026-08-11_B2-impact-applicability-local-verification.md).
- **Current focused learning artifact:** [`learning/2026-08-10-seven-concept-foundation-pre-a-c-implementation.md`](learning/2026-08-10-seven-concept-foundation-pre-a-c-implementation.md), covering the minimum seven concepts required for implementation-adjacent reasoning. Study it progressively and reinforce its concepts through the implementation/testing work that naturally exercises them.
- **Superseded historical plan:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md), superseded in place at commit `64f273655c43c5a1ec44aa69ae68e96de92f0062`; historical/non-controlling pre-reconciliation and future-D source material only, explicitly not an accepted Conversation-D plan.
- **Old-vs-new plan reconciliation:** [`working-memory/2026-08-10_B2-new-decision-foundation-plan-reconciliation.md`](working-memory/2026-08-10_B2-new-decision-foundation-plan-reconciliation.md); comparison passed and authority transition was subsequently applied.
- **Single product-model reconciliation record:** [`working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md), post-AUDIT-003 consolidated at commit `4923ca94fc241e4675751c3f251b730f324d11d8`.
- **External critical review:** [`audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`](audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md) was audited finding-by-finding; substantive findings were accepted with bounded refinements and incorporated into the reconciliation/model and approved plan.
- **Conversation A — technical impact-candidate formulation:** CLOSED 2026-08-08.
- **Conversation B — candidate-specific applicability/proposition evaluation:** CLOSED 2026-08-09.
- **Conversation C — discriminating investigation selection/stopping:** CLOSED 2026-08-10 at the product-model level; runtime activation is not yet implemented.
- **Conversation D — overall evidence sufficiency / repository policy / residual risk / maintainer-facing synthesis:** **not yet opened**.
- **Frozen cumulative learning snapshot:** [`learning/2026-08-10-product-decision-model-a-b-c-mastery-note.md`](learning/2026-08-10-product-decision-model-a-b-c-mastery-note.md). It represents the original closure state and must not be silently rewritten to include later audit/plan amendments.

## Immediate project action

The verification gate for the first implemented technical impact-candidate and candidate-specific applicability slice is **cleared**.

Current continuation:

1. review/learn the just-verified implementation in small learning-by-building steps as needed;
2. then begin the first bounded runtime activation of **discriminating investigation selection** around the exact target Python declaration;
3. keep the first runtime activation narrow: unresolved candidate-specific applicability because target evidence has not yet been acquired → identify the exact target declaration as the discriminating target → select the existing read-only exact-head acquisition;
4. only after that bounded case is understood and implemented, handle the materially different already-attempted-and-failed/unavailable acquisition state.

Preserve the distinction:

```text
grounded technical impact candidate
+
exact target declaration evidence not yet acquired
→ unresolved candidate-specific proposition
→ discriminating target = exact authoritative target declaration
→ existing read-only exact-head acquisition may be selected
```

versus:

```text
same exact acquisition already attempted
+
failed / unavailable
→ do not select the identical investigation again
   without concrete retry justification
```

The second state must preserve unresolved applicability and either select a materially different justified investigation or represent no further executable investigation.

Do **not** create another implementation plan, open the overall-sufficiency/maintainer-action responsibility, or add a generic investigation/rule/scoring framework merely to create activity.

## Why the selected plan exists

The superseded Transparent Decision plan mixed responsibilities that the reconciliation has now separated:

```text
PRE-FINAL-ACTION FOUNDATION
technical impact-candidate formulation
↓
candidate-specific applicability/evidence/composition
↓
uncertainty/conflict-driven discriminating investigation selection and stopping
```

and:

```text
LATER RESPONSIBILITY
overall evidence sufficiency
+ repository-policy/residual-risk relationship
+ maintainer-facing action/synthesis
```

The selected approved plan owns only the first implementable responsibility and explicitly hands off before the later overall-sufficiency/action responsibility.

## Continuation-critical decision-model guards

### Technical impact-candidate formulation

```text
upstream change mechanism
+ target-relevant exposure/path
+ activation condition(s)
+ possible target-relevant consequence
= mechanism-specific impact candidate
```

Candidate formulation does **not** establish its own exposure, activation, or other component truth. Preserve independently justified versus hypothetical component status.

The implemented `PythonSupportDropImpactCandidate` marks the grounded upstream mechanism as established, target exposure/activation as requiring evaluation, and the consequence as possible rather than established. Exact dependency-transition and target-head identity are retained, and a mismatched upstream interval is rejected.

### Candidate-specific applicability / coverage

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

Therefore all represented paths being refuted while path-model coverage remains unresolved/insufficient does **not** justify unqualified `established not applicable`.

Keep distinct:

```text
EVIDENCE COVERAGE
PATH-MODEL COVERAGE
CANDIDATE-DISCOVERY COVERAGE
```

Therefore all discovered candidates being non-applicable does not prove transition-level absence of impact without independently justified discovery coverage.

The first implementation explicitly represents proposition evidence coverage and path-model coverage. It intentionally does not implement candidate-discovery completeness or transition-level absence claims.

For the first Python-support candidate, the existing deterministic Target-Python relevance result is decomposed into explicit upstream-mechanism, exact-target-declaration, and range-intersection/activation propositions. Path-level information is preserved when candidate state is composed.

The pre-acquisition extension now also represents:

```text
target_relevance = None
→ exact target declaration has not yet been acquired/evaluated
→ target-declaration proposition unresolved + evidence coverage insufficient
→ activation proposition unresolved
→ candidate applicability unresolved
```

This is intentionally distinct from an existing `TargetPythonDeclarationProblem`, which means acquisition/interpretation was attempted and produced a problem.

### Discriminating investigation selection/stopping

This responsibility starts from:

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

It may produce:

```text
selected next investigation / small conditional sequence
OR no further justified investigation
OR multiple admissible non-dominated alternatives requiring later policy/maintainer context
```

Do not invent numerical Value-of-Information or universal cost utility. Observation meaning remains limited by identity/context/temporal/contrast/reconstruction fidelity.

For the first Target-Python case, distinguish evidence **not yet acquired** from an acquisition **already attempted and failed/unavailable**. The existing exact-head read-only acquisition may be selected in the first case; the identical failed investigation must not be selected again without concrete retry justification in the second.

Candidate refinement is conditional in the first slice: whenever it occurs, preserve minimum `V1 → triggering observation → V2/refined candidate` lineage, but do not manufacture a refinement case merely to satisfy the plan.

```text
investigation stop
!= overall evidence sufficiency
!= final maintainer action
```

## First implementation anchor

The selected plan intentionally reuses the completed Target-Python support-drop path as the first architecture anchor rather than adding a new ecosystem mechanism.

The currently implemented orchestration path remains:

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

A grounded non-overlap produces bounded `established_not_applicable`; overlap produces `established_applicable`; target/comparison uncertainty produces `unresolved`; no grounded upstream claim produces no technical impact candidate.

The domain evaluator can now also represent candidate-specific applicability **before target evidence acquisition**, but the real application orchestration still acquires the target declaration in the pre-existing order. Therefore runtime discriminating-investigation selection is still not implemented.

S001 remains an implementation anchor, not product scope or a known-answer hardcode.

Kedro/Pluggy, pip-audit/CacheControl/urllib3, C01 grpcio-tools, and C203 Buildtest/OpenSSL remain transfer/adversarial cases used to test whether the first-slice design overclaims generality; they do not automatically activate graph, plugin, differential-execution, or historical-reconstruction infrastructure.

## B2 proportionality boundary

The first pre-final-action implementation/evaluation slice must **not** automatically introduce:

- universal impact-candidate generation;
- arbitrary dependency graph infrastructure;
- universal plugin/framework analysis;
- generic investigation planner/decision tree;
- numerical VoI/ranking;
- generic differential-test executor;
- universal historical-environment reconstruction;
- autonomous target-repository execution;
- complete investigation/exposure taxonomy;
- final overall-sufficiency formula;
- final recommendation engine.

No Charter change is currently justified.

## Latest material verification

Current accepted local implementation proof after the impact/applicability and pre-acquisition changes:

- focused applicability-composition tests: **9 passed**;
- focused Python-support impact tests: **9 passed**;
- focused `PublicPullRequestInvestigation` integration tests: **6 passed**;
- focused new implementation subtotal: **24 passed**;
- nearest existing Target-Python interpretation regression: passed;
- nearest existing Target-Python relevance regression: passed;
- full active product deterministic suite in normal WSL/Python environment: **384 tests passed in 0.068s**;
- installed/import smoke: **passed** (`installed imports: OK`);
- Python used: **3.12.3** at `/home/motafeq/projects/UpgradePilot/.venv/bin/python`;
- dated proof: [`working-memory/2026-08-11_B2-impact-applicability-local-verification.md`](working-memory/2026-08-11_B2-impact-applicability-local-verification.md).

Prior proof remains historical context, including the earlier 323-test Target-Python-era regression, Step 7 live proofs, and the S001 normal-path proof.

The bounded S001 conclusion still means only that the grounded Python-3.8 support-drop concern does not intersect the target's declared Python installation range. It does not establish update safety, universal compatibility, sufficient testing, or a merge recommendation.

## Material blockers / caveats

- No blocker remains for the completed Target-Python Support Relevance responsibility.
- The plan-authority-transition blocker is resolved.
- The first technical impact-candidate and candidate-specific applicability source/integration work is implemented and locally verified.
- The prior fresh-regression verification gate is **resolved** by the 384-test green suite and installed/import smoke.
- The seven-concept learning phase is **not an implementation blocker**. Learning continues alongside building and should be reinforced in small source/test steps rather than treated as a prerequisite completion gate.
- Runtime discriminating investigation selection/stopping is the next unimplemented source responsibility.
- The overall evidence-sufficiency / repository-policy / residual-risk / maintainer-facing synthesis responsibility remains deliberately unopened until bounded implementation evidence exposes a concrete need for it.
- Security/non-mutation boundaries remain controlled by `SECURITY.md`; public read-only inspection never authorizes arbitrary target code execution or dependency installation.
- LM Studio loopback/proxy caveats remain owned by `ENVIRONMENT.md`; provider/model/deployment-contract changes remain reassessment events rather than silent substitutions.

## Learning state

Current demonstrated depth remains **substantial implementation exposure with repeated evidence-driven debugging and substantial guided product-model reasoning; no formal mastery assessment**.

The first technical impact-candidate and candidate-specific applicability implementation/integration reinforced evidence-vs-inference, open-world/completeness, necessary/sufficient conditions and AND/OR path reasoning, mechanism-specific candidate formulation, and candidate-specific applicability. The pre-acquisition extension additionally reinforces the distinction between **not checked yet** and **checked/attempted but failed or unavailable**. Stronger ownership should continue through small explanation, prediction, implementation-adjacent reading, modification, testing, diagnosis, and transfer steps.