# UpgradePilot Current Memory

**Last updated:** 2026-08-12  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Controlling route plan:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).
- **B2 parent plan:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md).
- **Selected B2 responsibility:** [`plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md), revised for responsibility-shaped generality and continued end-to-end convergence.
- **Planning correction:** [`working-memory/2026-08-12_B2-responsibility-shaped-expansion-decision.md`](working-memory/2026-08-12_B2-responsibility-shaped-expansion-decision.md).
- **Current learning/build record:** [`working-memory/2026-08-12_B2-learning-by-building-first-c-session.md`](working-memory/2026-08-12_B2-learning-by-building-first-c-session.md).
- **Fresh runtime-loop verification:** [`working-memory/2026-08-12_B2-first-runtime-investigation-local-verification.md`](working-memory/2026-08-12_B2-first-runtime-investigation-local-verification.md), recorded at `89c13a85031478f571938b951719147d59e48328`.
- **Accepted source organization:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).
- **Superseded historical decision plan:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md), still non-controlling.

## Current implementation truth

The first Python-support **technical impact candidate → candidate-specific applicability → discriminating investigation → observation feedback → reevaluation** runtime loop is now implemented and fresh local verification is green.

Implemented source/test changes:

- `56450616d6c16438afbf2fa094bff08c0d9c8d25` — focused selector/no-repeat tests;
- `85d28f57697d861a55aeaa595fb30670dcc7c340` — mechanism-specific `PythonSupportDropInvestigationSelection` and selector;
- `9c806a98c5da61ab853fcc26fde43462eac52739` — orchestration tests for observable pre-state → selection → post-state;
- `1c7f7a79f7f2b56a572e6c460cdb7f11b7f654d4` — runtime orchestration wired through the selected exact-head target-declaration read.

Verified runtime shape:

```text
grounded Python-support-drop claim
→ build PythonSupportDropImpactCandidate
→ evaluate before target evidence
→ applicability unresolved because exact target declaration is not yet acquired
→ select exact target-declaration acquisition
→ execute existing read-only exact-head repository read
→ interpret target declaration
→ evaluate Target-Python relevance
→ reevaluate the same candidate
→ preserve post-observation applicability
```

`PublicPullRequestInvestigation` now preserves separately:

1. `python_support_drop_pre_investigation_result` — why the candidate was unresolved before acquisition;
2. `python_support_drop_investigation_selection` — what exact read was selected and why;
3. `python_support_drop_impact_result` — the post-observation reevaluated state.

The selector remains intentionally Python-support-specific. It selects the exact target declaration only for the genuine pre-acquisition gap and does not automatically reselect the same acquisition once target relevance/evidence already exists, including target-declaration problem states.

## Latest material verification

Fresh 2026-08-12 local verification was performed after pulling the latest `main` changes in the normal UpgradePilot environment.

Reported result:

```text
focused runtime-investigation tests: GREEN
nearest relevant regressions: GREEN
full active test suite: GREEN
```

No exact fresh count/timing transcript was captured in the repository record, so do not invent one. The earlier 2026-08-11 proof remains historical evidence for the previous implementation state; the new dated verification record owns the fresh runtime-loop claim.

## Planning/execution rule now in force

```text
BOUND THE SUPPORTED DOMAIN
NOT THE KNOWN FIXTURE

broad responsibility horizon
+
small implementation/learning increments
+
materially different real-case pressure
+
evidence-earned abstraction
+
continued end-to-end convergence
```

Product-simulation cases are transfer/adversarial evidence, not a sequential implementation backlog. One successful Python-support specimen is not enough to freeze the architecture.

## Immediate project action

The first runtime investigation loop verification gate is **cleared**.

Begin the implementation-grounded **architecture/transfer checkpoint** against the already-identified materially different cases:

```text
S006 → static evidence can remain insufficient; targeted behavior observation can be discriminating
S007 → authoritative static evidence can resolve/prune execution; selected checks can become stale
S008 → artifact-serviceability / installation-mode mechanism is materially different from Python-support reasoning
S009 → repository reproducibility/provenance context is decision-relevant but must remain separate from technical applicability
```

The checkpoint should inspect only the evidence needed to answer concrete source/architecture questions:

- what in the current candidate/applicability representation is genuinely reusable;
- what remains Python-support-specific;
- whether `PublicPullRequestInvestigation` is beginning to grow one field/branch per mechanism;
- what investigation/result concepts are likely shared versus mechanism-specific;
- whether any abstraction is now actually earned;
- what minimum shape a second technical mechanism needs to reconnect to the real application path.

Do **not** refactor preemptively during the checkpoint. Compare first; change only when concrete pressure appears.

## Expected next implementation breadth

Unless the transfer checkpoint exposes a stronger lower-cost contrast, the next technical mechanism is an **S008-style artifact-serviceability / installation-mode mechanism**.

Its first useful responsibility should distinguish, when supported by real evidence:

```text
package/interpreter admissibility
!= compatible binary artifact availability
!= source fallback availability
!= source fallback success
```

It must consume real admitted evidence, preserve exact package/version/target/revision/provenance identity, stay mechanism-specific where semantics differ, reuse shared applicability composition only where it actually fits, prefer authoritative static evidence and justified stopping, avoid arbitrary target execution, and integrate through the real application path.

## Continuation-critical guards

- candidate formulation does not manufacture exposure/activation/completeness/consequence truth;
- missing evidence is not negative evidence;
- candidate-level non-applicability requires represented-path elimination plus sufficient path-model coverage;
- evidence coverage, path-model coverage, and candidate-discovery coverage remain distinct;
- identical failed/unavailable investigation is not blindly retried;
- a selected investigation may need revalidation/pruning if new evidence removes its discriminating value;
- successful execution is not automatically valid evidence;
- investigation stopping is not overall evidence sufficiency or final maintainer action;
- do not introduce a universal impact engine, generic planner, generic rules framework, arbitrary dependency graph, plugin system, opaque scalar score, persistence/service/queue infrastructure, or target mutation without demonstrated need.

## Learning state

Current demonstrated depth remains **substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment**.

The next learning emphasis is practical architecture through contrast: compare the verified Python-support mechanism against materially different evidence/mechanism shapes, identify genuine commonality versus mechanism-specific semantics, and learn when duplication is healthier than abstraction and when a shared contract is actually earned.
