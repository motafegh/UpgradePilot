# Overall Evidence Sufficiency and Maintainer Action Synthesis — Orientation Working Memory

**Date:** 2026-09-08  
**Session status:** ACTIVE — synthesis responsibility admitted; first semantic pressure pass recorded; acceptance gate remains open  
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

## First semantic pressure pass

The first pass suggests that the five Charter actions should be distinguished by **what the current evidence is sufficient to justify**, not by a generic risk score.

### Merge after normal review

Tentative meaning:

```text
current admitted evidence is sufficient to continue ordinary maintainer review
without a known decision-critical unresolved/conflicted/material established concern
inside the supported B2 reasoning boundary
```

This must remain a bounded recommendation, not a claim that the update is safe or that candidate discovery is globally complete.

A complete comparison with no artifact-serviceability candidate can support this action for that mechanism; it does not prove no other mechanism exists.

### Run targeted checks

Tentative meaning:

```text
a specific unresolved decision-relevant proposition remains
+
a concrete maintainer-facing check could materially discriminate it
+
that check is sufficiently specific and justified to recommend now
```

This must name the actual check/target. Generic “test more” or “investigate further” is not enough.

This action is distinct from UpgradePilot's own automated-investigation selection: the product may have reached its execution boundary while still having enough evidence to recommend a concrete maintainer check.

### Investigate or block

Tentative meaning:

```text
an established applicable material concern
OR a decision-critical conflict/uncertainty is strong enough that proceeding normally
would be too strong until resolved
```

This is stronger than `run targeted checks`: the current evidence justifies treating resolution as a gate/blocking concern rather than an optional additional check.

### Defer

Tentative meaning:

```text
the case is inside the admitted product domain
but a decision-critical condition is temporarily unavailable/pending/not yet mature enough
for a stronger action
+
a later rerun or external state change could reasonably improve the decision
```

Examples may include temporary provider unavailability or pending evidence, but this must be pressure-tested. `defer` should mean “not now; revisit when the blocking state changes,” not generic uncertainty.

### Abstain

Tentative meaning:

```text
the product cannot responsibly select another supported action at the current method boundary
```

Likely triggers include unsupported/out-of-domain input or a state where the method lacks a defensible action mapping and no more specific bounded recommendation is justified.

Abstention is not failure. It is the explicit product behavior when UpgradePilot lacks authority to decide more strongly.

## Sufficiency-model insight from the first pass

A separate global `sufficient/insufficient` boolean appears too weak because evidence can be:

```text
sufficient to recommend a targeted check
but insufficient to recommend normal review
```

or:

```text
sufficient to justify blocking
while still leaving technical uncertainty unresolved
```

Therefore **sufficiency is action-relative**.

Current hypothesis:

- the selected action itself should encode what the evidence is sufficient to justify;
- the result should preserve decisive reasons, residual uncertainty/conflict, required checks, and claim limits;
- a separate top-level sufficiency enum should be added only if pressure tests show it carries non-duplicative semantics.

Do not freeze this hypothesis yet.

## Pressure against current heterogeneous states

First-pass mapping to test further:

```text
no material established concern + adequate admitted evidence
→ possible merge-after-normal-review candidate

established applicable material concern
→ investigate-or-block candidate

artifact candidate + exact applicability unresolved
→ targeted-check / defer / block depends on whether a concrete discriminating check exists,
   whether the gap is temporary, and how decision-critical the candidate is

complete artifact comparison + no candidate
→ mechanism contributes no bounded artifact concern; does not establish global absence

CI supported_not_correlated
→ useful bounded CI evidence, but not runtime step correlation or safety proof

CI unresolved/no successful CI
→ may weaken normal-review permission; exact action depends on whether the gap is actionable,
   temporary, or method-limiting

provider/acquisition problem
→ likely defer if temporary/retryable and decision-critical; abstain if method cannot responsibly
   proceed or classify the case more specifically

unsupported dependency transition
→ abstain/unsupported rather than guess

heterogeneous results with different finality
→ strongest decision-critical unresolved/established concern may constrain action, but synthesis
   must not flatten everything into one score

unresolved candidate + no further UpgradePilot-executable investigation
→ does not become not-applicable; may still support targeted maintainer check, defer, block, or
   abstain depending on evidence/action semantics
```

## Remaining design pressure before acceptance

The first pass is coherent enough to continue but not yet stable enough for specification promotion.

Next design questions:

1. Define the boundary among `run targeted checks`, `investigate or block`, and `defer` using concrete current evidence states.
2. Decide whether `merge after normal review` can be justified without candidate-discovery completeness, and if so what explicit claim limit is mandatory.
3. Decide what repository/context evidence is minimally required before any favorable action can be emitted.
4. Decide the minimal typed result fields after action semantics stabilize.
5. Then choose the stable specification owner and promote accepted semantics before implementation.

Do not implement until those semantics are accepted and promoted to the correct stable owner.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
