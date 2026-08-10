# UpgradePilot Current Memory

**Last updated:** 2026-08-10  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Completed bounded responsibility:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md).
- **Completed Step 7 integration plan:** [`plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`](plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md).
- **Accepted semantic extractor method:** [`docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`](docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md).
- **Accepted source organization:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).
- **Selected next B2 responsibility:** [`plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md), approved bounded plan at commit `d3bf15e62cee8b20188b032f87c8a5c4556245e4`.
- **Implementation status:** intentionally paused before Step 1 while Ali completes a bounded prerequisite-learning phase; no source/module selection or implementation work is currently authorized by live continuation.
- **Current focused learning artifact:** [`learning/2026-08-10-seven-concept-foundation-pre-a-c-implementation.md`](learning/2026-08-10-seven-concept-foundation-pre-a-c-implementation.md), covering the minimum seven concepts required for implementation-adjacent A→C reasoning.
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

Complete the bounded **seven-concept prerequisite study phase** before returning to Step 1 of the selected approved plan.

Primary study artifact:

[`learning/2026-08-10-seven-concept-foundation-pre-a-c-implementation.md`](learning/2026-08-10-seven-concept-foundation-pre-a-c-implementation.md)

The seven study targets are:

1. evidence vs inference vs authority;
2. open-world reasoning and completeness;
3. necessary/sufficient conditions and AND/OR paths;
4. impact candidate — mechanism / exposure / activation / consequence;
5. applicability — established / refuted / unresolved / conflicted;
6. discriminating target and investigation selection;
7. deterministic vs semantic responsibility and LLM authority.

The target is operational understanding with guidance, not repetition of every A/B/C discussion and not a mastery certification.

Do **not** continue source implementation, create another implementation plan, open Conversation D, or alter the approved B2 plan during this study phase merely to create activity. Use the repository/cases as teaching material only unless learning exposes a concrete factual contradiction or unsafe instruction.

After the bounded study phase, reassess readiness together. If sufficiently understood, the planned implementation continuation remains **Step 1 of the selected plan: inspect current source/tests and freeze the implementation baseline before selecting concrete source/module changes**.

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

Minimum composition behavior must explicitly test established/refuted/unresolved/conflicted path combinations, including mixed unresolved/conflicted alternatives, without automatically creating a universal Boolean/rule engine.

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

Conceptually:

```text
authoritative upstream Python-support drop
+
exact target declared Python range
→ mechanism-specific candidate
→ candidate propositions/applicability
→ when target evidence is unresolved/conflicted:
   discriminating target + bounded read-only investigation
```

S001 is an implementation anchor, not product scope or a known-answer hardcode.

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

The last accepted implementation proof state remains the completed Target-Python relevance slice. No fresh source/test regression was run during A–C reconciliation, learning consolidation, AUDIT-003 review, plan creation/comparison, final plan corrections, authority transition, or creation of the seven-concept study guide.

Recorded verification includes:

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

The bounded S001 conclusion means only that the grounded Python-3.8 support-drop concern does not intersect the target's declared Python installation range. It does not establish update safety, universal compatibility, sufficient testing, or a merge recommendation.

## Material blockers / caveats

- No blocker remains for the completed Target-Python Support Relevance responsibility.
- The prior plan-authority-transition blocker is **resolved**; the approved A–C foundation plan is selected.
- Implementation is intentionally paused for the bounded seven-concept learning phase; this is a deliberate learning handoff, not a source failure or design blocker.
- Conversation D remains deliberately unopened until bounded A–C implementation evidence exposes a concrete need for D-level overall sufficiency/policy/action semantics.
- Security/non-mutation boundaries remain controlled by `SECURITY.md`; public read-only inspection never authorizes arbitrary target code execution or dependency installation.
- LM Studio loopback/proxy caveats remain owned by `ENVIRONMENT.md`; provider/model/deployment-contract changes remain reassessment events rather than silent substitutions.

## Learning state

Current demonstrated depth remains **substantial implementation exposure with repeated evidence-driven debugging and substantial guided product-model reasoning; no formal mastery assessment**.

The new seven-concept study guide is the focused prerequisite artifact for the current learning phase. The broader frozen A→C mastery note remains available for deeper reconstruction but should not be treated as mandatory rereading. Stronger ownership should be recorded only after demonstrated explanation, prediction, modification, testing, diagnosis, or transfer on changed cases.
