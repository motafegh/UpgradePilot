# Targeted-Check Maintainer-Action Admission — Working Memory

**Date:** 2026-09-11  
**Session status:** CONTINUED  
**Primary mode:** Planning/Design orientation + Learning-by-Doing; Build not yet started  
**Selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Accepted semantics:** [`../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md)  
**Previous:** [`2026-09-11_synthesis-first-evaluator-build.md`](2026-09-11_synthesis-first-evaluator-build.md)  
**Continued by:** [`2026-09-11_ci-run-job-attempt-coherence-enhancement.md`](2026-09-11_ci-run-job-attempt-coherence-enhancement.md)

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

This is not yet a conclusion that new generic producer infrastructure is required. The accepted synthesis specification explicitly allows synthesis to derive an action-specific check from existing owned facts when every material premise and derivation is explicit and justified.

## A-phase producer mapping — first pass

### 1. Exact unresolved proposition — AVAILABLE in bounded mechanism paths

The current impact models already preserve proposition-level unresolved states rather than only generic uncertainty.

Examples:

- Python-support applicability can preserve `exact_target_python_declaration_established` or `declared_python_range_intersects_dropped_line` as unresolved;
- artifact serviceability can preserve `exact_target_wheel_compatibility_established`, `target_had_old_compatible_published_wheel`, and `target_lacks_proposed_compatible_published_wheel` as unresolved when exact target wheel compatibility is unavailable.

This means synthesis does not need to invent the *existence* of an unresolved technical proposition for these implemented mechanisms.

### 2. Concrete discriminating maintainer-performable check — NOT GENERICALLY AVAILABLE

The Python-support mechanism already has one concrete discriminating investigation selection: acquire the exact target Python declaration. But the normal application path executes that read itself when selected. Therefore this is evidence for the rule:

```text
useful check + UpgradePilot can/should execute it
→ investigation responsibility, not maintainer targeted-check permission
```

Artifact serviceability exposes a sharper current gap. The Target artifact-environment interpreter intentionally stops at partial static facts such as runner, setup-Python version, and dependency installation declaration. It explicitly leaves exact wheel compatibility `unresolved` and does not infer exact wheel tags or execute a target environment.

Current product state therefore contains an unresolved proposition, but it does **not** yet contain a producer-grounded concrete maintainer check for obtaining exact wheel compatibility. Merely knowing that UpgradePilot lacks this capability is not enough to manufacture one downstream.

### 3. Outcome interpretation / stopping logic — PARTLY AVAILABLE, but not yet attached to a maintainer check

The artifact applicability evaluator already knows how exact target wheel-tag evidence would affect its propositions:

- intersection with old published wheel tags can establish the old compatible path;
- intersection with proposed published wheel tags can refute proposed-wheel absence;
- no old-wheel intersection can refute the old compatible-path proposition.

So there is deterministic proposition reevaluation logic *if* exact target compatibility evidence exists.

What is not yet established is the complete maintainer-facing check contract that says how the maintainer should obtain admissible exact target evidence, what observations are accepted, and when that bounded check should stop.

S006 demonstrates the desired shape—freeze the exact check and map plausible outcomes before execution—but its Pydantic behavior-path check is non-controlling simulation evidence and is not a current implemented mechanism producer.

### 4. No justified UpgradePilot-executable investigation first — NOT YET ESTABLISHED GENERICALLY

The Product Decision Model requires three boundaries to remain separate:

```text
epistemically useful
!= UpgradePilot-executable
!= maintainer-recommendable
```

Python-support currently proves the importance of this distinction because its selected exact-file investigation is executed by UpgradePilot itself.

For artifact exact wheel compatibility, current source shows that UpgradePilot does not yet perform the missing exact environment evidence acquisition. But **lack of implemented capability is not proof that outsourcing to the maintainer is justified**. We still need an explicit, evidence-grounded reason that no admitted/worthwhile UpgradePilot investigation should do the same work first.

Conversation-C pressure evidence reinforces that `no further check` must preserve why: resolved, path-pruned, or unresolved-with-no-supported-investigation are different states.

### 5. No broader adaptive inquiry needed — NOT YET PROVEN for a current runtime targeted-check path

S006 is strong pressure that one exact behavioral question can sometimes be represented by one stable bounded differential check.

However, current `PublicPullRequestInvestigation` does not generically state that the remaining material uncertainty is fully captured by one stable check set rather than a broader inquiry whose next step depends on intermediate findings. This must be established for the specific candidate/action path rather than assumed from `unresolved` alone.

### 6. No independently established block condition — must remain an explicit action-relative gate

The absence of an implemented `block` runtime branch does not mean a block condition is semantically impossible. Targeted-check permission therefore must not become available merely because current code cannot emit block. Any admitted targeted-check path must establish that no independently proven hold already determines the current proposal disposition.

## Current A-phase conclusion

The first pass does **not** justify implementing `run targeted checks` as a simple new branch over existing `PublicPullRequestInvestigation` fields.

What is already strong:

```text
exact unresolved technical propositions
+ proposition reevaluation semantics
+ real S006 evidence for what a good discriminating bounded check looks like
```

What still needs to be earned for a real runtime targeted-check action:

```text
producer-grounded concrete maintainer-performable check
+ accepted observation/evidence contract
+ explicit reason UpgradePilot should not perform the same investigation first
+ proof that the remaining actionable uncertainty fits a stable bounded check set
+ no independent block condition
```

This means A-phase should continue one level deeper before Build. The next discriminating design question is whether these missing pieces can be **derived narrowly from current owned artifact/Python facts** or whether the first real missing responsibility belongs upstream in investigation/Target rather than in synthesis.

## Current A-phase route

1. **DONE — first pass:** map each accepted targeted-check permission premise to current typed investigation evidence/producers;
2. **DONE — first pass:** pressure the mapping against S006 and Conversation-C without treating historical action labels as ground truth;
3. **CURRENT:** decide whether the missing maintainer-check/outsource facts are narrowly derivable from current owned evidence or require an upstream investigation/Target responsibility;
4. identify the smallest justified next action without weakening targeted-check semantics;
5. make that design understandable before asking for a B-phase implementation decision.

No source/test implementation is authorized by this A-phase record itself.

## Learning-by-Doing state

```text
Slice: targeted-check maintainer-action admission

A — CURRENT:
    first producer mapping is complete; the key remaining question is whether a real maintainer-check/outsource contract can be derived from current owned facts or requires upstream capability/handoff work.

B — NOT STARTED:
    only after A closes, implement the smallest producer-grounded increment actually justified by the mapping; do not force the final action branch if an upstream responsibility is the real missing owner.

C — NOT STARTED:
    progressively preserve implementation/proof evolution if B begins.

D — NOT STARTED:
    inspect real behavior/tests and transfer ownership of the implemented permission boundary.

E — NOT STARTED:
    repair gaps and choose the next slice only after this action's bounded proof is understood.
```

## A-phase stopping conclusion and upstream handoff

Further inspection resolved the remaining design fork: the current artifact path can represent exact wheel-compatibility uncertainty and can reevaluate applicability when exact compatibility evidence exists, but current Target/CI producers do not yet establish a trustworthy exact target wheel-compatibility observation or a justified maintainer-outsource contract.

The safest smaller baseline is to ask whether already-produced CI execution evidence can supply a positive compatibility witness before considering target-environment reconstruction. That route exposed a prerequisite reliability defect already recorded by the separate correctness investigation:

```text
WorkflowRun preserves run_attempt
+
job acquisition requests filter="latest"
+
WorkflowJob does not preserve attempt identity
→ run metadata and jobs are not proven to belong to the same rerun attempt
```

Because stronger CI execution/log evidence would rely on that identity, targeted-check synthesis must not build on it yet. The user therefore selected a bounded re-entry into the existing CI investigation/acquisition responsibility rather than implementing `run targeted checks` prematurely.

Time-scoped continuation:

```text
targeted-check synthesis A
→ PAUSED after identifying upstream evidence/reliability dependency
→ CI run/job attempt-coherence enhancement cycle
→ reassess whether a trustworthy read-only CI execution/wheel witness is justified
→ return here with the resulting producer boundary
```

No targeted-check runtime branch has been implemented. This record remains the rationale/provenance for why the synthesis slice paused and what proof is needed before re-entry.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
