# Targeted-Check Maintainer-Action Admission — Working Memory

**Date:** 2026-09-11  
**Session status:** ACTIVE  
**Primary mode:** Planning/Design orientation + Learning-by-Doing; Build not yet started  
**Selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Accepted semantics:** [`../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md)  
**Previous:** [`2026-09-11_synthesis-first-evaluator-build.md`](2026-09-11_synthesis-first-evaluator-build.md)

## Session anchor

The first deterministic maintainer-action evaluator is locally proven at its admitted boundary: it consumes `PublicPullRequestInvestigation`, returns explained `abstain`, preserves the source investigation/reasons/uncertainty/limits, passes its 2 focused tests, and passes the 530-test repository unit suite.

The next bounded responsibility selected through the prior slice's E-phase is to evaluate **`run targeted checks`** as the first candidate non-abstention action. Selection is based on evidence/readiness, not a severity ladder. No targeted-check runtime branch is admitted or implemented yet.

## A-phase responsibility

Before any source mutation, determine whether the accepted `run targeted checks` semantics can be mapped truthfully onto current investigation producers and real evidence.

Accepted permission requires all of the following together:

- one or a small stable set of exact decision-critical unresolved propositions;
- concrete bounded maintainer-performable checks whose plausible observations materially discriminate those propositions;
- enough interpretation/stopping logic to explain how the observations would change the decision state;
- no justified UpgradePilot-executable investigation that should perform the same work first;
- no material concern requiring broader/adaptive inquiry instead of the bounded check set;
- no independently established block condition.

Generic uncertainty or vague `test more` advice is insufficient.

## Initial real-evidence anchor — S006

S006 is a completed **real-derived controlled variant** around qldebugger / Pydantic validator behavior. It is useful design-pressure evidence, not a semantic owner or current runtime fixture.

Its technical chain is:

```text
Pydantic V2 TypeError validator semantic
→ proposed range permits Pydantic 2.x
→ exact qldebugger validator branch deliberately raises TypeError on non-string input
→ visible controlled evidence exercises nearby paths but not that exact branch
→ exact observable behavior across V1/V2 remains unresolved
→ narrow two-version differential reproduction selected
```

The selected check holds the frozen qldebugger revision and `handler = 1` constant, compares Pydantic `1.10.9` with `2.0.0`, and observes the top-level exception class/message. The recommendation records how each plausible result changes the remaining question and explicitly limits what the check cannot prove.

Crucially, S006 deliberately stopped before a final maintainer action. It therefore establishes strong **targeted-check design/traceability pressure**, not by itself permission for the Charter action `run targeted checks`.

This is exactly the distinction this slice must resolve:

```text
useful discriminating technical check exists
!=
maintainer should be asked to run that check
```

## Current producer/handoff observation

`PublicPullRequestInvestigation` currently preserves rich typed technical evidence such as dependency identity/result, CI coverage, package/upstream evidence, Python-support investigation selection/results, and artifact-serviceability results.

At first inspection it does **not** expose an obvious generic final-synthesis object that directly states all targeted-check permission premises, such as a maintainer-performable check plus its outcome interpretation and proof that no equivalent UpgradePilot-executable investigation remains.

This is not yet a conclusion that new generic producer infrastructure is required. The accepted synthesis specification explicitly allows synthesis to derive an action-specific check from existing owned facts when every material premise and derivation is explicit and justified. A-phase must therefore map each targeted-check premise to:

```text
already directly available
OR derivable without inventing stronger meaning
OR genuinely missing from the normal producer path
OR unreachable because an earlier responsibility should act first
```

## Current A-phase route

1. map each accepted targeted-check permission premise to current typed investigation evidence/producers;
2. pressure the mapping against S006 without treating its historical `run_targeted_checks` comparator as ground truth;
3. verify the boundary between an UpgradePilot-executable investigation and a maintainer-performable check;
4. identify the smallest missing fact/representation, if any;
5. make the action-admission design understandable before asking for a B-phase implementation decision.

No source/test implementation is authorized by this A-phase record itself.

## Learning-by-Doing state

```text
Slice: targeted-check maintainer-action admission

A — CURRENT:
    orient the accepted permission, current producer boundary, and S006 design pressure; determine what facts are actually available versus missing before implementation.

B — NOT STARTED:
    only after A closes, implement the smallest producer-grounded targeted-check permission/result increment if justified.

C — NOT STARTED:
    progressively preserve implementation/proof evolution if B begins.

D — NOT STARTED:
    inspect real behavior/tests and transfer ownership of the implemented permission boundary.

E — NOT STARTED:
    repair gaps and choose the next slice only after this action's bounded proof is understood.
```

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
