# Synthesis Action-Permission Matrix — Working Memory

**Date:** 2026-09-11  
**Session status:** ACTIVE  
**Primary mode:** Planning/Design + Learning-by-Doing  
**Selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-11_synthesis-stop-defer-abstain-transfer.md`](2026-09-11_synthesis-stop-defer-abstain-transfer.md)  
**Supporting evidence:** [`../product-simulation/INVESTIGATE_VS_BLOCK_EXISTING_EVIDENCE_REPORT_2026-09-11.md`](../product-simulation/INVESTIGATE_VS_BLOCK_EXISTING_EVIDENCE_REPORT_2026-09-11.md)

## Session anchor

The bounded product-simulation dependency from the previous record has now been answered without creating S013. Existing preserved real screening evidence from Cactus #198, contrasted with S006, S003, and unresolved/no-tool controls, is sufficient to pressure a design-level `investigate` versus `block` distinction.

The responsibility now advances from action-family evidence gathering to the first coherent **action-permission matrix** for the Charter outcome family.

This record remains design evidence only. It does not freeze stable synthesis semantics, authorize source/test implementation, or introduce runtime enums/classes.

## Minimum mental model

The synthesis question is not:

```text
How risky is this PR?
```

It is:

```text
Given the evidence UpgradePilot actually owns,
what maintainer-facing action is positively justified,
and what stronger actions are not justified?
```

The first method should therefore use **positive permission conditions**, not a severity score or a generic `if unresolved -> investigate` ladder.

## First coherent action-permission matrix

| Charter action | Candidate positive permission | Important prohibition / boundary | Main pressure evidence |
|---|---|---|---|
| `merge after normal review` | required admitted evidence/context coverage is positively adequate for this bounded decision; no established material concern defeats favorable permission; remaining uncertainty is not material to the favorable permission boundary | absence of a known concern is not enough; implemented mechanisms do not prove discovery completeness; missing evidence cannot become favorable evidence | S001 historical favorable shape; S009/S010 coverage/context pressure |
| `run targeted checks` | one or a small stable set of exact decision-critical unresolved propositions remain; concrete bounded maintainer-performable checks materially discriminate them; no justified UpgradePilot-executable investigation should perform the same work first | generic uncertainty is not a check; a broad adaptive inquiry is not one targeted check; do not outsource work merely because product automation is missing | S006 |
| `investigate or block` — investigate sub-disposition | a material target-relevant concern is grounded; useful broader inquiry has concrete scope and stopping/pruning logic; the inquiry is not reducible to one stable bounded check/set; no established condition independently justifies withholding the current proposal as-is | uncertainty alone, missing CI, major-version severity, or incomplete discovery alone do not justify investigate; do not use investigate to avoid honest abstention | Cactus #198 screening evidence contrasted with S006/S003 |
| `investigate or block` — block sub-disposition | at least one material exact proposal-level problem/constraint/failure is established strongly enough that normal progression should be withheld for the current proposal as-is | block does not mean permanent incompatibility; additional investigation may help remediation/explanation but is not required to justify the hold itself | S003 |
| `defer` | a decision-critical question remains unresolved; no justified admitted UpgradePilot investigation can currently resolve it; a specific useful outside/future responsibility or condition is known; a concrete reassessment trigger can be named | generic insufficient evidence is not defer; if a concrete maintainer check is available now, targeted-check may fit better; if no grounded future/outside responsibility exists, do not fabricate one | S012 + no-tool transfer |
| `abstain` | no stronger bounded action is positively justified; no grounded useful targeted check, broader investigation program, or specific defer/re-entry responsibility can be supported at current proof strength | abstain is not a disguised negative conclusion; it must preserve uncertainty and claim limits | no-tool unresolved control / Conversation-C pressure |

## Why this is not a severity ladder

Do not model the actions as:

```text
merge < targeted check < investigate < block
```

That would collapse different responsibilities.

Examples:

- `defer` is not necessarily more or less severe than `investigate`; it means the useful next responsibility is outside the current supported boundary or time horizon.
- `abstain` is not the highest-risk outcome; it means the method cannot justify a stronger bounded recommendation.
- `run targeted checks` can be appropriate for a highly material issue if one bounded observation is the correct discriminating next step.
- `block` depends on proof sufficient to withhold the current proposal, not on a numeric severity score.

## Pressure pass against real cases

### S006 — targeted-check anchor

Observed shape:

```text
one exact target behavior question remains
+
one controlled old/new differential observation can discriminate it
```

Matrix result:

```text
run targeted checks
```

only if UpgradePilot itself has no justified executable investigation that should perform the same check first.

This pressures the product-vs-maintainer execution boundary without changing the check shape.

### Cactus #198 — investigate anchor

Observed real screening shape:

```text
material Intel-macOS artifact/serviceability relationship
+
real but unresolved X.509 activation relationship
+
pruned ChaCha20 false friend
+
multiple materially different evidence paths
+
no established proposal-level blocker yet
```

Matrix result:

```text
investigate pressure
```

because useful next inquiry is broader/adaptive: intermediate findings can prune/refine which branch deserves the next evidence action. This is materially different from one predeclared S006-style check.

Claim limit: Cactus remains preserved screening evidence, not a frozen numbered maintainer-action oracle.

### S003 — block anchor

Observed shape:

```text
proposal CI fails at install
+
proposed TypeScript version conflicts with retained TypeScript-ESLint peer support
+
same-base comparison strengthens attribution
```

Matrix result:

```text
block pressure
```

because further inquiry is not required to justify withholding the current proposal as generated.

The hold is proposal-relative, not a universal claim that TypeScript 7 can never be supported.

### S012 — defer pressure

Observed shape:

```text
concrete deployment/applicability question remains
+
artifact-history/provenance evidence could discriminate it
+
that exact evidence responsibility is outside the current product snapshot/capability
```

Matrix result:

```text
defer pressure
```

when the missing outside/future evidence is decision-critical and a concrete re-entry condition can be named.

If that same evidence can instead be obtained immediately through one maintainer-performable bounded check, the targeted-check family may be the better representation. This remains a boundary to pressure later rather than a reason to stop the current matrix.

### Honest unresolved / no-tool control — abstain pressure

Observed shape:

```text
material insufficiency/conflict remains
+
no admitted useful product action
+
no grounded outside responsibility
+
no justified stronger conclusion
```

Matrix result:

```text
abstain pressure
```

because synthesis must not invent a check, defer target, or active-sounding investigation merely to avoid saying that it cannot justify a stronger recommendation.

## First deterministic selection shape

The design should not begin with an opaque score. A simpler baseline is:

```text
1. consume owned typed evidence/results/context only;
2. identify which action permissions are positively satisfied;
3. apply explicit prohibitions/defeaters;
4. resolve only genuine overlaps using evidence structure and action meaning;
5. emit one Charter action or abstention;
6. include decisive reasons, unresolved questions/checks, claim limits, and provenance.
```

Important overlap rules now supported strongly enough for design use:

```text
established proposal-level hold condition
→ block can be justified even if further investigation would help remediation

one exact unresolved question + bounded discriminating check
→ targeted-check pressure, not generic investigate

broader grounded adaptive inquiry + no hold established
→ investigate pressure

specific useful outside/future responsibility + reassessment trigger
→ defer pressure

no stronger permission + no grounded useful next responsibility
→ abstain pressure
```

Do not infer a universal total ordering among all actions.

## The remaining major gap: favorable permission

The negative/escalation side is now much clearer than the favorable side.

A favorable recommendation cannot be:

```text
no known blocker
→ merge after normal review
```

because S009/S010 already show:

```text
all implemented mechanism results look non-concerning
!=
adequate discovery/context coverage established
```

The next design slice therefore needs to define the **positive bounded coverage/context prerequisites** for `merge after normal review`.

The question is not whether UpgradePilot can prove global safety. It cannot and should not claim that.

The question is:

> What bounded evidence horizon must the first synthesis method positively establish before it may return a proposal to ordinary maintainer review instead of withholding favorable permission?

This is now the most important unresolved action-permission question.

## Learning-by-Doing state

```text
Slice: first coherent action-permission matrix

A — DONE:
    supporting investigate-vs-block evidence consumed; no S013 required.

B — DONE:
    first permission/prohibition matrix built from real anchors rather than a severity score.

C — DONE:
    matrix pressure-tested against S006, Cactus #198, S003, S012, and honest-unresolved/no-tool control.

D — CURRENT OWNERSHIP POINT:
    understand why actions represent different responsibility/evidence shapes rather than one risk ladder.

E — NEXT:
    define the positive bounded evidence/coverage prerequisites for `merge after normal review`, then pressure the complete matrix before stable semantic acceptance.
```

## Immediate continuation

Next real step under the selected plan:

```text
favorable action permission
→ identify minimum positive evidence horizon
→ pressure against S001/S004/S005 plus S009/S010 coverage/context counter-pressure
→ decide whether V1 can safely emit `merge after normal review`
   or must initially withhold that action when coverage cannot be established
```

Do not begin Build, introduce an LLM/planner/graph, create another simulation case, or freeze runtime action types from this working-memory matrix alone.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`
