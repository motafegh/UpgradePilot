# Overall Evidence Sufficiency and Maintainer Action Synthesis — Orientation Working Memory

**Date:** 2026-09-08  
**Session status:** ACTIVE — synthesis responsibility admitted; semantic contract/design is the next bounded action  
**Primary mode:** Planning/Design + Learning-by-Doing  
**Selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-08_artifact-serviceability-integration-proof.md`](2026-09-08_artifact-serviceability-integration-proof.md)

## Why this responsibility is now earned

The prior artifact-serviceability integration plan is closed with deterministic WSL proof. The normal application path now carries two materially different technical mechanism families:

```text
Python-support-drop
+
artifact-serviceability
→ heterogeneous mechanism-specific evidence/applicability state
```

The parent B2 foundation explicitly says to stop deepening those mechanisms once credible heterogeneous technical state exists and identify the concrete synthesis/output blocker.

The B2 vertical-slice owner names the next responsibility as:

```text
technical candidate results
+ CI/evidence authority
+ relevant repository/context evidence
+ residual uncertainty
→ overall sufficiency assessment
→ bounded recommendation or abstention
```

## Stable owners recovered

### Charter

`PROJECT_CHARTER.md` fixes the broad supported action family:

```text
merge after normal review
run targeted checks
investigate or block
defer
abstain
```

It also prohibits objective-safety claims, repository mutation, and replacement of maintainer judgment.

### Product Decision Model

`UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md` owns technical-candidate/applicability/investigation semantics and explicitly stops before mature synthesis/policy.

Its boundary is:

```text
INVESTIGATION
Should we acquire more evidence, what next check is worth pursuing,
and has worthwhile investigation stopped?

LATER SYNTHESIS / POLICY
Given all candidates, repository context, observations, failures, and remaining uncertainty,
is the overall evidence state sufficient for a maintainer-facing output and how do policy/
residual-risk considerations affect that output?
```

The specification says that mature synthesis contract is intentionally outside its current accepted scope until separately admitted and accepted.

### Current implementation

`PublicPullRequestInvestigation` currently returns detailed typed evidence/results, including:

- dependency result;
- CI coverage;
- package/upstream evidence and problem states;
- Python-support impact/investigation/relevance state;
- artifact candidate/Target/applicability state.

It does not contain an overall sufficiency or maintainer-action result.

The CLI renders the evidence at its typed proof strength and deliberately does not manufacture an overall recommendation.

There is no current top-level synthesis/decision module in `src/upgradepilot/`.

## Historical source material

`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md` remains superseded and non-controlling, but it contains useful earlier pressure around:

- action-relative sufficiency;
- explicit unresolved/conflicting states;
- reasons/checks/claim limits;
- preserving acquisition problems;
- avoiding a generic safety score;
- controlled contrasts before a live proof.

Those ideas must be re-evaluated against the now-richer real implementation rather than copied as accepted semantics.

## Planning conclusion

A new consequential plan is justified because:

1. this is a new B2 responsibility with several semantic and implementation decisions;
2. the stable synthesis contract is not yet accepted anywhere;
3. wrong action semantics could cause overclaiming at the product boundary;
4. the current heterogeneous evidence finally provides enough real pressure to design the method from implementation truth rather than one fixture.

Created plan:

`plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`

## Current unresolved design questions

The immediate design responsibility is **not** source code. It is to define and pressure the smallest synthesis contract around the actual current typed states.

We must resolve:

1. What exact typed result should represent one Charter action or abstention, sufficiency/readiness, decisive reasons, residual uncertainty, required targeted checks, and claim limits?
2. What is the minimum sufficiency-state model that does not collapse actionable gaps, unresolved/conflicted state, and unsupported cases?
3. What are the permission/stop boundaries for the five Charter outcomes?
4. Which repository/context evidence is genuinely needed now, if any, beyond the current investigation result?
5. How should multiple mechanism results combine without an opaque score, double counting, or false candidate-discovery completeness?
6. Should accepted synthesis semantics extend the current Product Decision Model specification or live in a separate focused synthesis specification?

## Simplest credible baseline

Start with deterministic transparent composition over typed state:

```text
owned typed evidence/result state
→ explicit sufficiency/action conditions
→ bounded action or abstention
→ decisive reasons + unresolved limits/checks
```

Do not start with an LLM, graph, generic policy engine, numeric score, or agent planner.

## Next bounded action

Pressure the synthesis contract against the real current state families before deciding field names or source layout.

Start with these contrasts:

```text
1. no material established technical concern + adequate evidence
2. established applicable material concern
3. artifact candidate but exact applicability unresolved
4. complete artifact comparison with no candidate
5. CI authority insufficient/unresolved
6. provider/acquisition problem
7. unsupported dependency transition
8. heterogeneous results with different finality strengths
9. unresolved candidate with no further UpgradePilot-executable investigation
10. one concrete maintainer-facing targeted check
```

The goal is to derive the smallest coherent outcome/sufficiency semantics, not one rule per fixture.

Do not implement until those semantics are accepted and promoted to the correct stable owner.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
