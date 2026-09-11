# UpgradePilot Current Memory

**Last updated:** 2026-09-11  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** complete the Learning-by-Doing ownership check for the newly accepted maintainer-action synthesis semantics, then enter the first bounded Build/Implement slice for the deterministic synthesis layer.
- **Mode:** Planning/Design + Learning-by-Doing is closing at the semantic-acceptance gate. Product source/test implementation has **not started yet**; Build/Implement is the next admitted operation after the current LbD D/E handoff closes.
- **Selected plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Accepted stable synthesis owner:** `docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md`.
- **Active working memory:** `working-memory/2026-09-11_synthesis-stable-semantic-acceptance.md`.
- **Previous working memory:** `working-memory/2026-09-11_synthesis-producer-reachability-and-correctness.md`.
- **Supporting simulation evidence:** `product-simulation/INVESTIGATE_VS_BLOCK_EXISTING_EVIDENCE_REPORT_2026-09-11.md` plus the referenced real/real-derived case corpus.
- **Parent plan:** `plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`.
- **Repository route:** continue directly on `main` unless Ali later asks for a separate branch.
- **Framework status:** ordinary-Python / LangGraph / LangChain comparison remains closed; the accepted synthesis contract requires a transparent deterministic baseline and does not justify framework re-entry.

## Semantic acceptance checkpoint

The overall evidence-sufficiency / maintainer-action responsibility now has a controlling stable specification distinct from the Product Decision Model.

Boundary:

```text
PRODUCT DECISION MODEL
→ technical candidate/applicability/investigation/stopping semantics

MAINTAINER ACTION SYNTHESIS
→ overall action-relative evidence sufficiency
→ one Charter action
→ decisive reasons / residual uncertainty / follow-up / claim limits
```

The Product Decision Model remains the upstream technical-decision owner. The new synthesis specification begins only after that responsibility's current evidence/investigation state exists.

The accepted action semantics are:

```text
MERGE AFTER NORMAL REVIEW
positive bounded evidence/context/coverage closure established
+ no material non-favorable condition remains

RUN TARGETED CHECKS
one or a small stable set of exact decision-critical unknowns
+ bounded discriminating maintainer-performable checks
+ no justified UpgradePilot-executable investigation should do the same work first

INVESTIGATE OR BLOCK — investigate disposition
material concern grounded
+ concrete broader/adaptive inquiry
+ not reducible to one stable bounded check set
+ no independent block condition established

INVESTIGATE OR BLOCK — block disposition
material exact current-proposal hold condition already established strongly enough
that the proposal should not progress as-is

DEFER
specific useful outside/future responsibility or condition
+ concrete reassessment/re-entry trigger

ABSTAIN
no other Charter action positively justified at current proof strength
```

These actions are different evidence/responsibility shapes, not a severity ladder.

## Accepted synthesis rules

- evidence sufficiency is **action-relative**, not one global sufficient/insufficient boolean;
- every emitted action requires **positive permission**;
- missing evidence is not negative evidence and cannot create favorable permission;
- `merge after normal review` is bounded return-to-ordinary-review permission, not a safety claim;
- the Charter's combined `investigate or block` outcome must preserve an internal `investigate` versus `block` disposition;
- `run targeted checks` requires actual discriminating maintainer checks, not generic uncertainty;
- `investigate` requires grounded broader/adaptive inquiry, not merely “more research”;
- `block` is proposal-relative and does not imply permanent incompatibility;
- `defer` requires a named outside/future responsibility plus re-entry trigger;
- `abstain` is the honest fallback when no other action is positively justified;
- semantic action availability is separate from current runtime producer reachability;
- known identity/provenance/interpretation weakness prevents affected evidence from satisfying permissions above its trustworthy proof strength;
- the first synthesis method must be transparent and deterministic; no LLM/planner/graph/opaque score owns final action authority.

## Whole-contract pressure result

The accepted contract survived one complete pressure pass without case-specific exceptions:

- S004/S005 → favorable permission;
- S006 → targeted-check shape;
- preserved Cactus screening evidence → broader/adaptive investigate shape;
- S003 → block shape;
- S012/no-tool transfer → defer shape;
- honest unresolved/no-tool control → abstain shape;
- S009/S010 → counter-pressure preventing `nothing bad found → merge`;
- current producer map → confirms unreachable actions must remain unavailable rather than semantically weakened;
- current correctness findings → confirm trust restrictions belong before permission, while the concrete bugs remain implementation/evidence facts rather than stable semantic clauses.

No new simulation case or ADR is required before Build.

## Current producer reachability remains narrower than the specification

Current normal `PublicPullRequestInvestigation` already preserves most mechanism-specific truth, but not every final-action prerequisite.

At the present boundary:

```text
MERGE AFTER NORMAL REVIEW
→ not generally reachable; generic positive candidate-discovery/repository-context coverage is not produced

RUN TARGETED CHECKS
→ semantic permission accepted; no generic maintainer-check producer yet

INVESTIGATE
→ semantic permission accepted; no generic broader-inquiry producer yet

BLOCK
→ potentially reachable in narrow trusted cases, especially validated Python support-drop overlap

DEFER
→ semantic permission accepted; no generic outside/re-entry producer yet

ABSTAIN
→ projectable when synthesis has a valid input and no other permission is established
```

Do not fabricate unreachable branches merely to exercise the complete semantic action family in V1.

## Current trust restrictions still relevant to Build

The separate correctness investigation remains the owner of the concrete defects, but Build must not ignore their evidence-strength consequences:

1. **Patch/revision correspondence:** requirements/constraints patch text is not proven to belong to the initially frozen PR head; exact-file `uv.lock` and admitted pyproject paths are not implicated by that exact finding.
2. **Static command-recognition false positives:** unsupported shell comments/quoted separator data can earn positive direct-requirements evidence.
3. **Workflow run/job attempt mixing:** run/head identity does not currently prove same-attempt coherence.

The accepted synthesis rule is general:

```text
preserve affected evidence at its actual strength
+
do not let it satisfy a permission requiring stronger trust
```

## Remaining upstream capability gaps

These remain outside the first synthesis implementation rather than being patched with invented synthesis state:

- unresolved Python post-attempt continuation needs a narrow handoff if another justified product investigation or specific outside responsibility is to be asserted;
- artifact exact target wheel compatibility has a typed evidence contract but no normal producer/selector;
- generic candidate-discovery completeness and generic repository-purpose/context discovery are not current product capabilities;
- generic maintainer targeted-check / broader-investigation / defer-reentry producers do not yet exist.

## Immediate continuation

Canonical Learning-by-Doing loop is active:

```text
A — DONE: stable-owner/contract slice oriented.
B — DONE: stable synthesis specification written and whole contract pressure-tested.
C — DONE: accepted contract, navigation, working memory, and this live handoff preserved.
D — CURRENT: post-action teaching + Ali ownership check.
E — NEXT: repair any important understanding gap, then orient Build.
```

After D/E close, activate the Build/Implement procedure for the smallest deterministic synthesis implementation at **current producer reachability**:

```text
accepted synthesis specification
→ choose smallest core synthesis result/evaluator representation
→ implement only producer-grounded action paths + honest abstention
→ focused unit tests for permission/trust boundaries
→ then integrate with PublicPullRequestInvestigation / CLI only after the core behavior is proven
```

Do not introduce an LLM, graph, generic planner, risk score, new simulation case, or unrelated producer expansion as part of the first Build slice.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`
