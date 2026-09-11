# Investigate vs Block — Existing-Evidence Research Report

**Date:** 2026-09-11  
**Status:** Completed bounded product-simulation research/evaluation report; non-controlling  
**Scope:** Maintainer-facing `investigate` without `block` evidence discrimination  
**Authority:** Supporting discovery/evaluation evidence only  
**Main synthesis owner:** `../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md` and its active working-memory chain

## 1. Research question

The bounded question was whether the existing product-simulation corpus or previously screened real cases already support a clean maintainer-facing distinction of this form:

```text
material concern exists
+
broader investigation is genuinely justified
+
no single bounded targeted check is sufficient
+
current evidence is not yet strong enough to recommend blocking normal progression
```

The requested reuse order was:

1. existing real/preserved cases or screening evidence;
2. compact cross-case evaluation;
3. real-derived one-variable contrast;
4. only if genuinely necessary, a new case.

This report does **not** freeze product semantics, change the Charter, modify the product-decision specification, define runtime action enums, or authorize implementation.

## 2. Governance and evidence boundary

This work follows the product-simulation rule that existing evidence should be reused before admitting a new case and that simulation findings remain supporting evidence until a controlling owner adopts them.

The Charter-supported output family remains:

```text
merge after normal review
run targeted checks
investigate or block
defer
abstain
```

Historical simulation or planner labels are not treated as current product truth.

The comparison anchors required for this research are:

- **S006** — strong targeted-check shape;
- **S003** — strong block-like shape;
- **Conversation-C / Buildtest-OpenSSL and related unresolved controls** — honest unresolved state where stronger maintainer action is not automatically justified.

## 3. Evidence classes used

| Evidence | Evidence class | Role in this report |
|---|---|---|
| S003 — event-handler-loader / TypeScript 7 | real public preserved case | block-like anchor |
| S006 — qldebugger / Pydantic validator coverage gap | real-derived controlled variant anchored in real public evidence | targeted-check anchor |
| Cactus-Network/cactus-blockchain #198 / cryptography 48→49 | real public screening evidence | strongest investigate-side anchor |
| Buildtest/OpenSSL candidate | real public screening evidence | unresolved / insufficient stronger-action contrast |
| S010 / podcast-script | real public preserved case | broader discovery and multi-mechanism pressure |
| S009 / publication reproducibility context | real public preserved case | context evidence that can matter without proving technical block |

No synthetic control is required to establish the primary distinction in this report.

## 4. Result

### 4.1 Existing evidence is sufficient for a design-level investigate-vs-block distinction

The existing corpus is sufficient to support the distinction at the **design-pressure / evidence-transfer** level.

The strongest investigate-side evidence is not a numbered scenario. It is the preserved real-public screening evidence for:

```text
Cactus-Network/cactus-blockchain #198
cryptography 48.0.0 → 49.0.0
```

That screened transition produced materially different candidate states in one proposal:

```text
A. x86_64 macOS wheel removal
   target builds an Intel-macOS installer
   → material artifact/serviceability relationship established
   → fallback/source-build failure not established

B. ChaCha20 semantic change
   target uses ChaCha20Poly1305 rather than the changed lower-level primitive
   → superficially related mechanism pruned

C. stricter X.509 certificate loading
   target genuinely loads X.509 certificates and may consume private CA material
   → real target relationship established
   → exact narrow malformed ECDSA/DSA activation condition unresolved
```

This creates a useful middle state:

```text
material concern exists
+
important decision-relevant questions remain unresolved
+
there is more than one non-dominated investigation branch
+
no one bounded check closes the relevant proposal-level uncertainty
+
no currently established fact independently proves that normal progression must be blocked
```

The evidence therefore supports a genuine `investigate` shape rather than merely another label.

### 4.2 Why Cactus is not S006-shaped targeted-check evidence

S006 has a much tighter structure:

```text
one exact upstream behavior change
+
one exact target branch
+
one visible coverage gap
+
one controlled differential check whose outcomes discriminate the material question
```

That is a strong `run targeted checks` shape.

Cactus differs because the meaningful unresolved space is not one proposition with one discriminating observation. It contains distinct mechanism branches whose useful evidence paths are different:

```text
Intel-macOS artifact/serviceability branch
!=
X.509 malformed-certificate activation branch
```

An installation/serviceability check cannot settle the X.509 question, and an X.509-focused check cannot settle artifact availability/serviceability.

Therefore:

```text
multiple concrete concerns
+
multiple materially different evidence responsibilities
+
adaptive pruning/reevaluation required
```

is stronger pressure for broader investigation than for one maintainer-facing targeted check.

### 4.3 Why Cactus is not S003-shaped block evidence

S003 already had proposal-level evidence strong enough to withhold normal progression:

```text
public CI failed during npm ci
+
TypeScript 7.0.2 sat outside the retained TypeScript-ESLint peer-support range
+
same-base comparison evidence strengthened attribution
```

The important distinction is not that S003 had "more evidence" in the abstract.

The distinguishing condition is:

> S003 already crossed the permission boundary for withholding the present proposal as-is. Further investigation could improve explanation or identify remediation, but it was no longer required to decide whether the current proposal should proceed normally.

Cactus does not cross that boundary from the preserved evidence alone.

## 5. Provisional evidence conditions

### 5.1 Investigate-side conditions

The current corpus supports this evidence shape:

```text
material target-relevant concern is grounded
+
one or more decision-relevant propositions remain unresolved/conflicted
+
there are concrete admissible investigation paths that could materially change the evidence state
+
those paths are not reducible to one bounded discriminating check for the relevant overall concern
+
broader inquiry has a concrete scope and stopping/pruning logic
+
no currently established condition independently justifies blocking normal progression
```

The key requirement is **grounded broader inquiry**, not generic uncertainty.

### 5.2 Block-side conditions

The current corpus supports this contrasting shape:

```text
at least one material proposal-level problem is established
at sufficient exact-target / exact-proposal proof strength
+
that established condition independently justifies withholding normal progression as-is
```

Additional investigation may remain useful for:

- causal refinement;
- remediation;
- coordinated-version selection;
- confirmation;
- discovering additional concerns.

But it is no longer necessary to establish the hold itself.

## 6. What `investigate` must not mean

`Investigate` must **not** become any of the following shortcuts:

```text
some uncertainty remains
→ investigate
```

```text
CI evidence is missing
→ investigate
```

```text
a major dependency update looks risky
→ investigate
```

```text
candidate discovery is incomplete
→ investigate indefinitely
```

```text
one exact unknown remains and one bounded discriminating check exists
→ investigate
```

```text
no stronger action is supportable but no useful inquiry is grounded
→ investigate
```

The evidence instead supports these neighboring boundaries:

```text
one exact decision-critical unknown
+ one bounded discriminating check
→ targeted-check shape
```

```text
established material proposal-level blocker
→ block-like shape
```

```text
material uncertainty remains
+ no grounded useful investigation remains
+ no stronger action is justified
→ abstain/unresolved pressure
```

```text
material question remains
+ useful next responsibility is specifically known
+ responsibility lies outside the current admitted capability/ownership boundary
+ concrete reassessment trigger exists
→ defer-like pressure
```

## 7. State transitions from investigate

### 7.1 Investigate → block

Transition when broader inquiry produces evidence that establishes a material proposal-level condition strongly enough to justify withholding normal progression.

Representative evidence additions include:

- exact-context install/build/runtime failure attributable to the proposal;
- authoritative compatibility/support constraint intersecting the exact proposed environment;
- exact target activation plus sufficiently established material consequence;
- another proposal-level contradiction whose proof no longer depends on unresolved investigation branches.

S003 is the primary block-like reference.

### 7.2 Investigate → targeted check

Transition when broader inquiry prunes the uncertainty space until:

```text
one decision-critical proposition remains
+
one bounded observation/check can materially discriminate its outcomes
```

The check should identify:

- the exact unresolved proposition;
- the activation condition/path;
- the controlled observation;
- materially different plausible outcomes;
- what each outcome changes in the recommendation state.

S006 is the primary targeted-check reference.

### 7.3 Investigate → abstain

Transition when the remaining concern cannot be resolved by any grounded, admissible, sufficiently discriminating inquiry and no stronger bounded action is supportable.

This must preserve uncertainty rather than fabricate an active-sounding next step.

### 7.4 Investigate → defer

Transition when a concrete useful evidence responsibility remains but it belongs outside the current supported capability/authority/time horizon and there is a grounded re-entry condition.

`Defer` should not be used as a synonym for insufficient evidence.

## 8. Boundary with broad discovery

S010 and the candidate-discovery pressure work add an important guard:

```text
more than one possible mechanism exists
!=
automatic investigate recommendation
```

Broader candidate discovery is itself conclusion-relative.

An `investigate` recommendation needs an already grounded material concern and a justified inquiry program whose expected evidence can change the maintainer-facing decision state. The mere possibility that more mechanisms could exist is not enough.

Likewise:

```text
all currently known candidates resolved
!=
discovery proven complete
```

so a favorable action cannot be inferred solely from candidate-local closure without an adequate broader sufficiency argument.

## 9. Remaining uncertainty

The corpus still lacks a **frozen numbered scenario whose evaluation oracle is specifically a maintainer-facing `investigate` recommendation**.

That absence matters for future benchmark/evaluation claims, but it does not currently justify creating a new case because the research question here is whether the semantic/evidence distinction can be supported strongly enough for main synthesis design.

The remaining finer ambiguity is:

> When should several individually bounded maintainer-performable checks remain represented as `run targeted checks`, and when does their interaction/adaptive sequencing become broad enough that `investigate` is the more faithful maintainer-facing recommendation?

The current evidence suggests that the distinction should depend on **evidence/inquiry structure**, not simply the number of checks:

```text
independent bounded checks with a stable finite decision partition
may still be targeted checks

whereas

multi-branch inquiry whose next step depends materially on intermediate findings,
mechanism refinement, candidate pruning, or newly exposed uncertainty
is stronger investigate pressure
```

This remains supporting design evidence, not accepted runtime semantics.

## 10. Is new simulation work required?

**No new numbered simulation case is required now.**

In particular:

```text
S013 solely to obtain an `investigate` label
→ not justified
```

The least-artificial next step, only if main synthesis still cannot decide the finer targeted-check-vs-investigate boundary, is:

```text
compact cross-case evaluation
Cactus #198
vs S006
vs S003
vs abstention/unresolved control
```

If exact isolation is still needed after that, use a **real-derived one-variable Cactus contrast** that changes one evidence condition, for example:

```text
current Cactus state
→ no proposal-level blocker established

controlled contrast
→ add one exact observed Intel-macOS installation failure attributable to the proposed artifact path

question
→ does the recommendation boundary move from investigate pressure to block pressure?
```

Only if such a compact contrast cannot answer the remaining design question should a new numbered case be considered.

## 11. Main-synthesis handoff

```text
finding
Existing real/preserved evidence is sufficient to support a defensible
investigate-vs-block distinction at the synthesis-design pressure level.
The strongest investigate-side evidence is screening-level rather than a
frozen numbered maintainer-action oracle.

best evidence/case
Cactus-Network/cactus-blockchain #198, cryptography 48.0.0 → 49.0.0
(real public preserved screening evidence), contrasted with:
S006 (real-derived targeted-check anchor),
S003 (real-public block anchor),
and Buildtest/OpenSSL / unresolved controls.

investigate-side conditions
Material concern grounded;
decision-relevant uncertainty remains;
multiple/non-dominated investigation branches exist;
useful inquiry is concrete and bounded enough to justify doing;
no single check closes the relevant overall uncertainty;
no currently established condition independently justifies blocking.

block-side conditions
A material exact proposal-level problem is already sufficiently established
to withhold normal progression as-is.
Further investigation may improve explanation/remediation but is not required
to justify the hold.

remaining uncertainty
No frozen numbered maintainer-action oracle exists specifically for `investigate`.
The finer boundary between several targeted checks and broader/adaptive
investigation remains a synthesis-design question.

whether new simulation work is needed
No new numbered case now.
Reuse Cactus + S006 + S003 first.
Use a compact real-derived contrast only if the finer boundary remains unresolved.

recommended next step for main
Consume this as non-controlling evidence in the overall synthesis design.
Define `investigate` by evidence/inquiry structure and permission boundary,
not by generic uncertainty, severity language, missing CI, or number of checks.
Do not freeze runtime semantics from this report alone.
```

## 12. Stop line

This product-simulation research responsibility is complete when it has answered:

1. whether existing evidence supports a clean investigate-vs-block distinction;
2. what evidence conditions separate investigate from block;
3. how investigate differs from targeted-check and abstention/defer pressure;
4. what evidence transitions can change the action family;
5. whether a new case is required.

Those questions are answered at the present evidence horizon.

Do not from this report alone:

- change `PROJECT_CHARTER.md`;
- change stable specifications;
- change the selected synthesis plan;
- update `MEMORY.md` or active main working memory;
- implement source/tests;
- create S013;
- treat `investigate` as a finalized runtime enum or universal severity level.
