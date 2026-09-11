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

## Action-family pressure — targeted check, block, investigate, abstain

### Existing real anchors are strong for targeted check and block

**S006** supplies a clean targeted-check shape. Authoritative upstream Pydantic behavior evidence intersects an exact target validator branch, visible evidence does not exercise the exact TypeError path, and one bounded old/new differential reproduction can discriminate the remaining behavior question. The case explicitly did not establish merge/block/defer or safety semantics.

Transferable shape:

```text
one exact decision-relevant question remains
+
one concrete bounded check instantiates the activation condition
+
its plausible observations materially discriminate the question
→ strong targeted-check evidence shape
```

This remains subject to the current investigation boundary: a maintainer-facing check is only plausible after no justified UpgradePilot-executable investigation should perform that same work first.

**S003** supplies a clean block-like shape. Public CI failed at installation before the named downstream lint responsibility, the proposed TypeScript version was outside the retained TypeScript-ESLint peer-support range, and a same-base adjacent PR supplied useful comparison evidence. The historical synthesis concluded that the present proposal should not merge as generated while explicitly avoiding the stronger claim that TypeScript 7 can never be supported.

Transferable shape:

```text
current proposal has an established material failure/constraint conflict
+
evidence is sufficient to tie the concern to the proposal at the owned proof strength
→ normal progression can be withheld until the proposal/evidence condition changes
```

The historical `investigate_or_block` label is not imported as the current runtime rule; the evidence makes S003 specifically useful as a **block-like** anchor.

### Existing corpus does not cleanly isolate investigate-without-block

The remaining corpus was checked before declaring a gap:

- **Conversation-C / Buildtest-OpenSSL** supplies `unresolved + no sufficiently authoritative supported investigation remains`, but explicitly stops before maintainer-facing action semantics. It does not establish that broader maintainer investigation is preferable to abstention or block.
- **S010** supplies multiple distinct mechanisms, different target handling, context and bounded discovery coverage. It strongly shows that broader inquiry may be needed for a broader-coverage claim, but its owned question is discovery breadth rather than a maintainer-facing `investigate` disposition.
- **S007** resolves its owned contradiction and prunes deeper investigation, so it is a stopping anchor rather than an investigate-only anchor.
- **S008/S011** intentionally stop at narrower settled questions while deeper propositions remain separate.
- **S012** identifies a specific outside responsibility, making it stronger pressure for defer/targeted handoff than for open-ended investigation.
- the historical planner conflicted control supports honest unresolved state with no fabricated handoff, not a real maintainer-facing investigate action.

Therefore the current corpus adequately pressures:

```text
targeted check
block-like hold
local stopping
known outside responsibility / defer-like handoff
honest unresolved / possible abstention
```

but does **not** yet cleanly discriminate:

```text
broader maintainer investigation is justified
AND
current evidence is not yet sufficient to recommend block
AND
no single bounded targeted check adequately resolves the decision
```

This is now a **genuine evidence gap**, not an assumed need for more cases.

## Bounded product-simulation request specification — investigate versus block

This request specification is prepared under the active synthesis plan and the product-simulation case-selection framework. It does **not** authorize or launch new simulation work by itself.

### Named question

What evidence boundary should distinguish these two operational meanings inside the Charter-facing `investigate or block` family?

```text
INVESTIGATE
material decision-relevant concern/uncertainty justifies broader inquiry,
but current evidence is not yet sufficient to recommend withholding normal progression
solely on the established technical state

BLOCK
current evidence is already sufficient to recommend withholding normal progression
until a stated condition/proposal/evidence state changes
```

The investigation should also test whether that distinction is materially useful at the product-output level or whether one Charter-facing action plus structured reasons/sub-disposition can represent both cleanly.

### Existing evidence checked

Use at minimum:

- S003 as the block-like anchor;
- S006 as the single concrete targeted-check anchor;
- S007 and Conversation-C pressure for stopping/pruning;
- S008/S011 for settled-question versus deeper-uncertainty boundaries;
- S010 for broader discovery/multiple-mechanism pressure;
- S012/no-tool transfer for specific outside responsibility versus honest unresolved state.

Do not recreate these cases merely to relabel their historical actions.

### Missing discrimination

We still lack one realistic evidence state where all of the following hold together:

```text
material concern is grounded enough that simple favorable continuation is too weak or at least seriously questionable
+
the concern is not yet established strongly enough to justify a block-like hold from the current evidence alone
+
no single bounded check adequately closes the overall decision
+
broader inquiry has a concrete scope/reason rather than generic "investigate more"
```

The evidence should make it possible to contrast that state with S003-like block permission.

### Preferred least-artificial form

Do **not** assume S013.

Preferred order:

1. first search existing screened real cases / preserved challenge evidence for a natural investigate-without-block shape;
2. if one exists, perform a compact **cross-case transfer evaluation** against S003 rather than a full numbered scenario;
3. if one realistic host almost fits, use a **real-derived controlled variant** changing one material evidence condition;
4. use a synthetic control only if exact isolation cannot be achieved credibly with existing real structure.

A new full numbered scenario is justified only if the smaller forms cannot answer the question.

### Expected decision consequence

The result should tell main synthesis design whether:

- `investigate` and `block` need explicit sub-disposition semantics;
- structured reasons/checks are enough under one Charter-facing action;
- one of the interpretations should be unavailable in V1 because a defensible positive permission boundary cannot be established;
- or the Charter/stable synthesis owner eventually needs refinement.

It should also clarify the boundary with `abstain`: broader investigation must be grounded enough to be useful, not merely a more active-sounding response to uncertainty.

### Claim limits

The simulation may establish a discriminating semantic/evaluation contrast. It must not by itself:

- change the Charter;
- define accepted runtime enums/classes;
- prove prevalence across public dependency PRs;
- authorize source implementation;
- establish universal severity ordering among Charter actions;
- treat historical simulation action labels as ground truth.

### Stop condition

Stop when existing or minimally derived evidence can answer both:

1. what concrete fact(s) make broader investigation justified while block remains too strong;
2. what additional evidence/state transition converts that same general concern into a defensible block-like hold, or demonstrates that the distinction is not operationally useful.

If existing screened evidence already answers both, record that and do not create a new case.

## Learning-by-Doing state

```text
Slice: S011/S012/no-tool transfer and action-family evidence-gap detection

A — DONE:
    oriented the difference among settled owned questions, known outside responsibility, honest unresolved state, targeted-check and block-like outcomes.

B — DONE:
    inspected S011, S012, the no-tool transfer, S006, S003, S005, Conversation-C pressure, workspace coverage and the case-selection framework; transferred the underlying semantics without importing historical action labels as current product rules.

C — DONE:
    preserved the transfer maps, targeted-check/block anchors, the surviving investigate-without-block evidence gap, and the bounded simulation request specification here.

D — DONE at guided depth:
    established from concrete cases why `some uncertainty remains` is insufficient for defer/investigate/check, why S006 is check-shaped, and why S003 is block-shaped.

E — WAITING FOR AUTHORIZATION:
    the next external/supporting action is bounded product-simulation work against the request specification above. Do not launch a new case by default; the separate simulation arm should first seek the least-artificial existing-case/cross-case answer.
```

## Immediate continuation

The main synthesis design has now reached a real evidence dependency:

```text
existing corpus
→ targeted-check boundary well pressured
→ block-like boundary well pressured
→ investigate-without-block boundary still materially underdetermined
```

Next options under the selected plan are:

1. Ali authorizes the product-simulation arm to execute the bounded request above; main later consumes its result as non-controlling evidence; or
2. main explicitly leaves investigate-vs-block unresolved and withholds any first-version semantics that depend on that distinction while continuing only independent design work.

Do not create S013, change stable synthesis specifications, or begin product source/test implementation merely because the gap is now documented.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
