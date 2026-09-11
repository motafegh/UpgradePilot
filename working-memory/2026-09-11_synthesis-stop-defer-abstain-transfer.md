# Synthesis Stop / Defer / Abstain Transfer — Working Memory

**Date:** 2026-09-11  
**Session status:** ACTIVE  
**Primary mode:** Planning/Design + Learning-by-Doing  
**Selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-11_synthesis-artifact-and-cross-candidate-transfer.md`](2026-09-11_synthesis-artifact-and-cross-candidate-transfer.md)

## Session anchor

This record continues the real-case-first synthesis design route after the S007/Python and S008/artifact transfer work. Product source/tests and stable synthesis semantics remain unchanged; this is Planning/Design evidence only.

The immediate responsibility is to transfer the useful semantic distinctions from S011, S012, and the B2/X1 no-tool cross-case evaluation into the current overall-synthesis design without importing historical planner labels as current Charter actions.

The Charter-supported maintainer-facing outcomes remain:

```text
merge after normal review
run targeted checks
investigate or block
defer
abstain
```

The historical B2/X1 planner experiment used a different disposition vocabulary:

```text
choose_action
stop
defer
unresolved
```

Those labels are not equivalent one-for-one. Transfer only the evidence-backed underlying distinction.

## Evidence-transfer map 2 — S011: settled owned question with adjacent uncertainty

### Evidence basis

S011 is a preserved real public case around Dictare's optional `mlx` environment and a NumPy dependency update. Exact target/workflow evidence established that the inspected standard and macOS workflows installed `.[dev]`, not `.[mlx]`. Therefore the inspected workflows did not form the affected optional dependency environment.

Runtime compatibility of NumPy 2.4.6 inside a real MLX environment remained unresolved, but that was a different proposition from the owned coverage/environment-formation question.

### Transfer distinction

```text
owned question settled
+
adjacent/deeper proposition unresolved
!=
permission to continue investigating the deeper proposition
```

S011 therefore supplies strong real evidence against an `any unresolved fact -> continue/defer/check` heuristic.

### Current synthesis consequence

Overall synthesis is broader than S011's historical planning question, so S011's historical `stop` cannot be copied as a maintainer action. The transferable rule is narrower:

> A residual uncertainty should affect the selected maintainer action only when it is material to that action's permission boundary.

This supports action-relative sufficiency. A later synthesis result may preserve adjacent uncertainty as a claim limit or secondary concern without letting it automatically control the primary action.

What S011 does **not** establish:

- that NumPy 2.4.6 is compatible with the MLX stack;
- that deeper runtime compatibility is globally unimportant;
- that a favorable maintainer action is justified;
- that every unresolved adjacent proposition can be ignored.

The missing design work is to define, per candidate Charter action, which propositions are decision-critical and which may remain residual without making that action too strong.

## Evidence-transfer map 3 — S012: concrete unresolved applicability with a known outside capability

### Evidence basis

S012 is a preserved real case around Freqtrade/FreqAI persisted scikit-learn state. It establishes that current source/current environment may be insufficient when target behavior intentionally reuses persisted state produced under an earlier dependency environment.

The same underlying evidence supported two different historical questions:

```text
Question A:
Can historical producer provenance be a necessary applicability input?
→ yes, established by static evidence
→ historical simulation stopped at that bounded question

Question B:
Is this concrete selected persisted artifact actually an old-producer/new-consumer case?
→ producer version / exact reused artifact remain unresolved
→ deployment/artifact-history evidence would discriminate
```

### Transfer distinction

```text
material question remains unresolved
+
a specific evidence responsibility that could discriminate it is known
+
that responsibility is outside the current admitted product capability
```

is materially different from generic uncertainty.

The important fact is not merely `missing evidence`; it is the existence of a **named, decision-relevant outside responsibility** with a concrete reassessment path.

### Current synthesis consequence

S012 gives real pressure for a possible `defer` permission boundary, but does not by itself establish the stable Charter semantics.

A defensible defer hypothesis now needs at least:

```text
decision-critical proposition remains unresolved
+
no justified admitted UpgradePilot investigation can currently resolve it
+
a specific external/future responsibility or condition is grounded by the evidence
+
obtaining/changing that state could materially change the recommendation
+
a concrete reassessment/rerun trigger can be named
```

Do not use `defer` as a synonym for `insufficient evidence`.

What remains open:

- whether every outside-capability case should map to Charter `defer`;
- when a maintainer-performable concrete check should instead become `run targeted checks`;
- when the unresolved concern is already strong enough to support `investigate or block`;
- whether some outside responsibilities are outside the Charter's useful decision horizon and should instead contribute to abstention.

## Evidence-transfer map 4 — no grounded next responsibility

### Evidence basis

The B2/X1 no-tool disposition transfer evaluation compared preserved real cases and one synthetic conflicted control under a planner experiment contract. Its strongest reusable finding is relational:

```text
no-tool disposition
!= function(unresolved proposition alone)
```

The experiment's `unresolved` control represented:

```text
owned question remains materially insufficient/conflicted
+
no admitted useful action
+
no sufficiently grounded outside capability/responsibility
+
no justified closure/negative conclusion
```

The evaluation correctly refused to fabricate a handoff merely because no action was available.

### Current synthesis consequence

The historical label `unresolved` is **not** a Charter action and must not be copied into runtime synthesis.

The transferable rule is:

```text
no grounded next capability/responsibility
→ do not fabricate `defer`
→ do not fabricate `run targeted checks`
→ preserve the uncertainty honestly
```

Within the current Charter, `abstain` is a plausible candidate when no stronger bounded recommendation is supportable. However, that mapping is **not accepted yet**, because `investigate or block` may legitimately cover some materially unresolved states even when there is no single concrete check/capability to name.

Therefore the next design contrast must pressure:

```text
ABSTAIN CANDIDATE
method lacks a defensible stronger action and cannot ground a useful next responsibility

versus

INVESTIGATE CANDIDATE
material concern/uncertainty warrants broader inquiry even though no single bounded targeted check is sufficient

versus

BLOCK CANDIDATE
existing evidence already justifies withholding normal progression until a stated condition changes
```

## Important non-transfer from the historical planner experiment

The no-tool evaluation also contains `d-repeat-stop`, a synthetic control where the only admitted action had already been attempted and blind repetition was forbidden while the proposition remained unresolved.

That control remains useful for the already-recorded Python handoff problem, but its historical planner `stop` must not become a top-level maintainer action. It demonstrates only that:

```text
investigation can legitimately stop
while epistemic uncertainty remains
```

Later synthesis must still decide what maintainer-facing action, if any, that unresolved stopped state supports.

## Combined semantic map now supported by real/cross-case evidence

The transfer work now supports these distinctions without yet freezing Charter mappings:

| Situation | Evidence meaning | What must not be inferred automatically |
|---|---|---|
| owned proposition/question final | local investigation can stop for that question | overall PR sufficient / favorable action |
| owned question final, adjacent uncertainty remains | preserve residual uncertainty; do not reopen unrelated work automatically | defer/check/investigate solely because some uncertainty exists |
| question unresolved, justified UpgradePilot investigation remains | return to investigation owner | maintainer check/defer by default |
| question unresolved, no admitted product investigation, specific useful outside responsibility known | concrete handoff/reassessment path exists | generic uncertainty = defer |
| question unresolved, no admitted action, no grounded outside responsibility | uncertainty must remain explicit | fabricated defer or targeted check |
| established mechanism concern | technical conclusion exists | automatic top-level block |

This table is design evidence only, not a runtime decision table or accepted specification.

## Current design consequence for action-relative sufficiency

S011 and S012 strengthen the action-relative baseline:

```text
Evidence sufficiency is not:
"are all propositions resolved?"

It is closer to:
"is the decision-relevant state sufficient to justify this particular bounded action,
while honestly preserving the residual uncertainty that does not satisfy or defeat that permission?"
```

This does not yet prove that no separate sufficiency/readiness field is useful. It does show that a global `sufficient / insufficient` boolean would erase important distinctions.

## Learning-by-Doing state

```text
Slice: S011/S012/no-tool transfer for stop, defer and honest unresolved state

A — DONE:
    oriented the difference among settled owned questions, known outside responsibility, and unresolved state with no grounded next responsibility.

B — DONE:
    inspected S011, S012, the no-tool cross-case evaluation and the Charter outcome vocabulary; transferred the underlying semantics without importing experiment labels as product actions.

C — DONE:
    preserved the transfer maps and current non-rules in this working record.

D — DONE at guided depth:
    repaired the prior reasoning gap directly: final local proposition state can justify local stopping without a duplicate stop flag, while unresolved state requires explicit continuation/stop evidence rather than inference from absence.

E — ACTIVE:
    next pressure `investigate or block` versus abstain and targeted-check handoff using existing real cases before declaring any new simulation gap.
```

## Immediate continuation

Use existing real evidence first to pressure the remaining action-family seam:

```text
run targeted checks
vs
investigate or block
vs
abstain
```

Start with S006/S008/S012 for concrete discriminating checks/outside capabilities and S003/S007/S010 for established concerns / broader inquiry pressure. Determine whether the existing corpus already supplies a clean real contrast for `investigate` versus `block`.

Only if that distinction remains materially unresolved after the existing-corpus review should a bounded new product-simulation request be specified for Ali's authorization.

Do not modify stable synthesis specifications or product source/tests until the semantic acceptance gate is satisfied.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
