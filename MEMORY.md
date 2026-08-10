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
- **Legacy selected next B2 plan:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md). New generic decision-layer implementation remains paused; this older plan is materially pre-reconciliation and is awaiting an explicit supersession/archive decision rather than source implementation.
- **New candidate bounded plan:** [`plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md), final candidate content commit `2c25f08f5056dc27c2af345dd04eea76c1a87edd`.
- **Old-vs-new plan reconciliation:** [`working-memory/2026-08-10_B2-new-decision-foundation-plan-reconciliation.md`](working-memory/2026-08-10_B2-new-decision-foundation-plan-reconciliation.md), commit `b84b1baa5e38da4871f1b9db00dce6ea4de274a5`; verdict **PASS — candidate ready for explicit promotion decision**.
- **Single product-model reconciliation record:** [`working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md), post-AUDIT-003 consolidated at commit `4923ca94fc241e4675751c3f251b730f324d11d8`.
- **External critical review:** [`audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`](audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md) was audited finding-by-finding; substantive findings were accepted with bounded refinements and incorporated into the reconciliation/model and new-plan design.
- **Conversation A:** CLOSED 2026-08-08 — mechanism-specific technical impact-candidate model.
- **Conversation B:** CLOSED 2026-08-09 — candidate-specific applicability, evidence/coverage, negative-inference, and model-authority model.
- **Conversation C:** CLOSED 2026-08-10 — discriminating-target / investigation-selection / stopping model, after C01 and C203 pressure tests and closure review.
- **Conversation D:** **not yet opened**.
- **Frozen cumulative learning snapshot:** [`learning/2026-08-10-product-decision-model-a-b-c-mastery-note.md`](learning/2026-08-10-product-decision-model-a-b-c-mastery-note.md). It represents the original A→C closure state and must not be silently rewritten to include later audit/plan amendments.

## Immediate project action

Perform the **authority transition decision** for the B2 decision responsibility:

1. decide whether to promote [`plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md) as the selected next bounded B2 responsibility;
2. if promoted, ensure [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md) no longer remains a competing active implementation owner;
3. preserve the older plan through Git history and preferably archive/supersede it as pre-reconciliation historical material rather than silently deleting it;
4. do **not** rename the old plan into a Conversation-D plan without revalidating its final-action assumptions after A–C implementation feedback;
5. after promotion, begin Step 1 of the new plan: inspect current source/tests and freeze the implementation baseline before choosing concrete source/module changes.

No additional roadmap, generic planner plan, schema plan, or child implementation plan is justified before Step 1 source inspection exposes a concrete responsibility that needs one.

## Why the new candidate plan exists

The older Transparent Decision plan mixed two responsibilities that the A–C reconciliation has now separated:

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

The new candidate plan owns only the first implementable responsibility and explicitly hands off before D. Its creation therefore represents a justified responsibility split rather than duplicate planning.

The old-vs-new reconciliation verified that useful old-plan material was either:

- retained in the new plan;
- already completed by intervening Target-Python/upstream implementation;
- or explicitly preserved as later D/final-action material.

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
non-applicability requires closure of every represented viable path
```

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

Do not invent numerical VoI or universal cost utility. Observation meaning remains limited by identity/context/temporal/contrast/reconstruction fidelity. Candidate refinement must preserve minimum V1 → observation → V2 lineage.

```text
C investigation stop
!= D overall evidence sufficiency
!= final maintainer action
```

## First implementation anchor after promotion

The candidate plan intentionally reuses the completed Target-Python support-drop path as the first A–C architecture anchor rather than adding a new ecosystem mechanism.

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

The last accepted implementation proof state remains the completed Target-Python relevance slice. No fresh source/test regression was run during A–C reconciliation, learning consolidation, AUDIT-003 review, new-plan creation, or old-vs-new plan comparison.

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
- **Current implementation blocker:** authority transition between the legacy selected Transparent Decision plan and the reconciled candidate A–C foundation plan has not yet been explicitly completed.
- Conversation D remains deliberately unopened until bounded A–C implementation evidence exposes a concrete need for D-level overall sufficiency/policy/action semantics.
- Security/non-mutation boundaries remain controlled by `SECURITY.md`; public read-only inspection never authorizes arbitrary target code execution or dependency installation.
- LM Studio loopback/proxy caveats remain owned by `ENVIRONMENT.md`; provider/model/deployment-contract changes remain reassessment events rather than silent substitutions.

## Learning state

Current demonstrated depth remains **substantial implementation exposure with repeated evidence-driven debugging and substantial guided product-model reasoning; no formal mastery assessment**.

The frozen A→C mastery note remains the primary relearning artifact. Stronger ownership should be recorded only after demonstrated explanation, prediction, modification, testing, diagnosis, or transfer on changed cases.
