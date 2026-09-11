# Synthesis Action-Permission Matrix — Working Memory

**Date:** 2026-09-11  
**Session status:** CONTINUED  
**Continued by:** [2026-09-11_synthesis-producer-reachability-and-correctness.md](2026-09-11_synthesis-producer-reachability-and-correctness.md)

**Lifecycle reconciliation (2026-09-11):** The conclusions and continuation below describe this dated checkpoint. Consult the successor and repository `MEMORY.md` for continuation; historical learning labels do not establish unrecorded learner ownership.

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
| `merge after normal review` | required admitted evidence/context coverage is positively adequate for this bounded decision; no established material concern defeats favorable permission; remaining uncertainty is not material to the favorable permission boundary | absence of a known concern is not enough; implemented mechanisms do not prove discovery completeness; missing evidence cannot become favorable evidence | S001/S004/S005 favorable shapes; S009/S010 coverage/context pressure |
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

## Favorable-permission pressure pass

The favorable side was pressure-tested against S001/S004/S005 and the S009/S010 counter-pressure.

### What the favorable cases actually had

S004 is the cleanest baseline-sufficient control. Its favorable action was not justified by `patch update + green CI`. It positively established:

```text
exact proposal/dependency identity
+
direct development dependency role
+
changed requirements consumed by the owning execution path
+
relevant exact-head ordinary and regression checks passed
+
primary upstream release information was coherent with the bounded target question
+
no contradictory or missing decision-critical evidence remained
```

S005 is the stronger action-revision control. The baseline initially asked for checks, but fuller evidence established:

```text
exact lock identity
+
actual lock-backed tox/test execution path
+
exact-head pytest 9.1.1 matrix results
+
upstream breaking statement decomposed to its activation condition
+
target configuration/source did not activate that condition
+
listed deprecations/patterns were absent or supported
+
no remaining target-specific uncertainty named a useful additional check
```

That evidence legitimately weakened the action back to ordinary review.

S001 supplies an older favorable shape where the full decision also remained `merge_after_normal_review`, but it does not override the later S009/S010 coverage lessons.

### What S009 and S010 prevent us from inferring

S009 establishes that a proposal may have a material repository-purpose/provenance inconsistency without proving technical incompatibility. Therefore:

```text
technical candidates look fine
!=
all decision-relevant repository context is fine
```

S010 establishes that one valid candidate can coexist with another materially distinct mechanism and that its discovered candidate set is intentionally non-exhaustive. Therefore:

```text
all currently discovered/evaluated candidates look fine
!=
discovery coverage proven adequate for a broad favorable conclusion
```

### Favorable action design hypothesis

`merge after normal review` should mean:

> Within an explicitly admitted and positively established evidence horizon, UpgradePilot found no decision-critical condition requiring a stronger action, the evidence relied upon is authoritative enough for that horizon, and remaining uncertainty does not defeat returning the proposal to ordinary maintainer review.

This is **bounded review permission**, not a safety claim and not proof that every possible mechanism was discovered.

A defensible positive permission requires all of the following classes of facts at the current design horizon:

```text
A. exact identity / trust
   proposal, revision, dependency/change identity are established;
   material evidence used by the decision is valid/trusted at its owned proof strength.

B. bounded coverage adequacy
   the decision declares/owns the evidence and mechanism/context horizon it is relying on;
   that horizon is positively covered rather than merely having produced no findings;
   known blind spots that could materially change the action remain explicit and defeat favorable permission when unresolved.

C. candidate / concern closure
   all decision-critical candidates actually admitted within that horizon are resolved or otherwise non-defeating for ordinary review;
   no established block, targeted-check, investigate, or defer condition remains material to the action.

D. evidence-authority closure
   when CI or another execution result is relied upon, it is tied to the changed dependency/proposal and the responsibility it is claimed to cover;
   missing/unreachable/unsupported evidence is not converted into favorable evidence.

E. context closure where admitted
   any material repository-context finding actually produced by an admitted context owner is incorporated;
   a missing generic context producer is not silently interpreted as `no context concern`.

F. residual-uncertainty limits
   remaining uncertainty is explicitly recorded and is not decision-critical to the favorable permission being issued.
```

### Current product-reachability consequence

The current normal product can evaluate specific implemented mechanism families, but it does not yet own a generic candidate-discovery completeness claim or a general repository-purpose/policy/provenance discovery responsibility.

Therefore the current product **cannot generally prove the positive bounded-coverage condition required for `merge after normal review` across arbitrary supported PRs** merely from the fact that its implemented mechanisms found no blocker.

The first synthesis implementation should therefore follow this conservative rule:

```text
if positive bounded coverage/context adequacy is not producer-grounded
→ `merge after normal review` permission is unavailable
→ choose another positively justified action when one exists
→ otherwise abstain
```

This does not mean favorable action is removed from the Charter or impossible forever. It means first-version runtime reachability must not outrun the evidence producers that justify it.

A later bounded discovery/context capability can make the favorable branch reachable without changing the underlying action meaning.

## Coherent matrix status after favorable pressure

The action family now has a complete design-level positive-permission shape:

```text
MERGE AFTER NORMAL REVIEW
positive bounded evidence/coverage closure established
+ no material stronger-action condition remains

RUN TARGETED CHECKS
exact decision-critical unknown
+ bounded discriminating maintainer check

INVESTIGATE
material concern
+ grounded broader/adaptive inquiry
+ no block yet established

BLOCK
material proposal-level hold condition already established

DEFER
specific useful outside/future responsibility
+ concrete reassessment trigger

ABSTAIN
no stronger action positively justified
+ no grounded useful next responsibility
```

This is now coherent enough to stop inventing more action examples and move to producer/reachability reconciliation and stable semantic acceptance work.

## What remains before stable acceptance

The remaining work is no longer "what do these actions basically mean?" It is:

1. reconcile each permission with actual normal producers/reachability, especially unresolved Python post-attempt state and artifact exact-compatibility evidence;
2. account for established affected-evidence correctness restrictions so unreliable evidence cannot authorize an action;
3. determine the stable specification owner and represent the accepted synthesis semantics there;
4. pressure the final matrix as one whole contract before Build authorization.

Do not add an LLM, graph, score, generic planner, or new simulation case to solve these producer/acceptance questions.

## Historical activity labels (not canonical learning-cycle completion)

```text
Slice: first coherent action-permission matrix + favorable permission

A — DONE:
    supporting investigate-vs-block evidence consumed; no S013 required.

B — DONE:
    first permission/prohibition matrix built from real anchors rather than a severity score.

C — DONE:
    escalation/uncertainty actions pressure-tested against S006, Cactus #198, S003, S012, and honest-unresolved/no-tool control.

D — DONE:
    favorable permission pressure-tested against S001/S004/S005 and S009/S010.

E — DESIGN CONCLUSION:
    favorable action requires positive bounded coverage/evidence closure; absence of known concern is insufficient. Current normal producers do not generally establish that coverage, so V1 must withhold favorable permission where the positive horizon is not producer-grounded.

F — NEXT:
    reconcile the matrix with actual producer reachability/correctness constraints, then move to stable semantic acceptance.
```

## Immediate continuation

Next real step under the selected plan:

```text
coherent semantic matrix
→ actual producer/reachability map for each permission
→ evidence-correctness restrictions
→ identify remaining genuinely missing state versus derivable state
→ stable specification owner / acceptance
→ only then Build/Implement
```

Do not begin Build, introduce an LLM/planner/graph, or create another simulation case from this working-memory matrix alone.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`
