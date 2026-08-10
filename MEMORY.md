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
- **Selected next B2 responsibility:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md).
- **Implementation status for that responsibility:** intentionally paused; the selected plan is materially stale against accepted A–C semantics and must be reconciled before generic decision-layer source work begins.
- **Single reconciliation record:** [`working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md), post-AUDIT-003 consolidated at commit `4923ca94fc241e4675751c3f251b730f324d11d8`.
- **External critical review:** [`audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`](audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md) was independently audited; its substantive findings were accepted with bounded refinements and incorporated into the reconciliation record. The audit remains non-controlling historical evidence.
- **Conversation A:** CLOSED 2026-08-08 — mechanism-specific technical impact-candidate model.
- **Conversation B:** CLOSED 2026-08-09 — candidate-specific applicability, proposition/evidence, negative-inference, and model-authority model.
- **Conversation C:** CLOSED 2026-08-10 — discriminating-target / investigation-selection / stopping model, after C01 and C203 pressure tests and closure review.
- **Post-C audit disposition:** does not reopen A/B/C; adds implementation guards and plan-reconciliation obligations.
- **Conversation D:** **not yet opened**.
- **Frozen cumulative learning snapshot:** [`learning/2026-08-10-product-decision-model-a-b-c-mastery-note.md`](learning/2026-08-10-product-decision-model-a-b-c-mastery-note.md). It represents the original A→C closure state and must not be silently rewritten to retroactively include post-closure audit amendments.

## Immediate project action

**Reconcile the existing `B2_TRANSPARENT_DECISION_METHOD_PLAN.md` against accepted A–C semantics plus the post-C AUDIT-003 amendments before any new generic decision-layer implementation.**

The plan update should preserve B2 scope and add only the responsibilities/proof obligations needed for the first credible pre-D A–C implementation/evaluation slice.

After the plan is reconciled:

```text
select smallest credible B2 A–C implementation/evaluation slice
↓
implement + test + inspect real behavior
↓
use the resulting evidence to decide whether a concrete Conversation-D dependency exists
```

Do **not** open broad Conversation D merely because C is closed. Do **not** implement a final recommendation engine under another name before D-level overall sufficiency/policy/maintainer-action semantics are actually needed and accepted.

## Continuation-critical decision-model guards

Detailed reasoning and decision history live in the reconciliation record. Keep only these guards in standing memory because they materially control the next plan/implementation step.

### A — impact candidate

```text
upstream change mechanism
+ target-relevant exposure/path
+ activation condition(s)
+ possible target-relevant consequence
= mechanism-specific impact candidate
```

Candidate formulation does **not** establish its own exposure, activation, or other component truth. Candidate construction must preserve independently justified versus hypothetical component status.

### B — applicability / coverage

Applicability is proposition-based for one candidate and exact target/revision/context.

Conceptual knowledge states remain:

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

Before negative or transition-level conclusions, keep three coverage questions distinct:

```text
EVIDENCE COVERAGE
Did evidence sufficiently cover proposition P?

PATH-MODEL COVERAGE
Did this candidate represent the material alternative applicability routes?

CANDIDATE-DISCOVERY COVERAGE
Were enough mechanism-specific candidates discovered to support any transition-level absence claim?
```

Therefore:

```text
all discovered candidates not applicable
!= transition proven to have no material target impact
```

without independently justified discovery coverage.

Minimum generic composition code must explicitly test proposition/path combinations involving `established`, `refuted`, `unresolved`, and `conflicted`, including mixed unresolved/conflicted alternative paths. Do not assume one scalar four-state precedence is automatically lossless; do not build a universal Boolean/rule engine merely to satisfy this obligation.

### C — investigation selection

C starts from a material **non-final** proposition state:

```text
unresolved OR genuine conflict
+
uncertainty/conflict location or reason
```

then identifies a discriminating target and candidate investigations.

Preserve three distinct boundaries:

```text
EPISTEMIC INVESTIGATION VALUE
Would the check, if correctly obtained, materially discriminate the proposition?

UPGRADEPILOT EXECUTION ADMISSIBILITY
May UpgradePilot itself execute it under capability/security/authorization/environment boundaries?

MAINTAINER-FACING RECOMMENDABILITY
Should the maintainer later be asked to run it given policy/risk/budget/output semantics?
```

The third crosses into later D/output reasoning. A useful check can be non-executable by UpgradePilot yet still potentially recommendable to a maintainer.

C valid outcomes include:

```text
selected next investigation / small conditional sequence
OR
no further justified investigation
OR
multiple admissible non-dominated alternatives whose residual preference depends on policy/maintainer/later decision context
```

Do not invent fake numerical VoI or universal cost utility. Hard configured boundaries may reject a check; genuine cost/value trade-offs among admissible alternatives should remain explicit.

Investigation result meaning is limited by identity/context/temporal/contrast/reconstruction fidelity. Successful execution does not automatically create valid evidence. Proxy evidence may narrow without exact-context authority. Candidate refinement must preserve minimal V1 → observation → V2 supersession/refinement lineage rather than silently mutating the original hypothesis.

```text
C investigation stop
!= D overall evidence sufficiency
!= final maintainer action
```

## B2 proportionality boundary

Whole-product A–C reasoning is broader than what B2 should implement now.

The first pre-D implementation/evaluation slice must **not** automatically introduce:

- a universal impact-candidate generator;
- arbitrary dependency graph infrastructure;
- universal plugin/framework analysis;
- a generic investigation planner/decision tree;
- numerical VoI/ranking;
- a generic differential-test executor;
- universal historical-environment reconstruction;
- autonomous target-repository execution;
- a complete investigation/exposure taxonomy.

B2 should implement only the thinnest credible manifestation needed to test accepted semantics through the real public-PR vertical slice and obtain architecture/evidence feedback.

No Charter change is currently justified.

## Latest material verification

The last accepted implementation proof state remains the completed Target-Python relevance slice; no fresh source/test regression was run during A–C reconciliation, learning consolidation, AUDIT-003 review, or the post-audit working-memory update.

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
- **Current implementation blocker:** `B2_TRANSPARENT_DECISION_METHOD_PLAN.md` must be reconciled before new generic decision-layer implementation; this is a method/proof-plan mismatch, not a source failure.
- Conversation D remains deliberately unopened unless plan reconciliation or bounded implementation exposes a concrete need for D-level overall sufficiency/policy/action semantics.
- Security/non-mutation boundaries remain controlled by `SECURITY.md`; public read-only inspection never authorizes arbitrary target code execution or dependency installation.
- LM Studio loopback/proxy caveats remain owned by `ENVIRONMENT.md`; provider/model/deployment-contract changes remain reassessment events rather than silent substitutions.

## Learning state

Current demonstrated depth remains **substantial implementation exposure with repeated evidence-driven debugging and substantial guided product-model reasoning; no formal mastery assessment**.

The frozen A→C mastery note is the primary relearning artifact. Post-C audit amendments are currently implementation/reconciliation guards rather than a reason to rewrite that historical learning snapshot. Stronger ownership should be recorded only after demonstrated explanation, modification, testing, diagnosis, or transfer on changed cases.
