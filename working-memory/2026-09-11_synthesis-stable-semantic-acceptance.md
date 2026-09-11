# Synthesis Stable Semantic Acceptance — Working Memory

**Date:** 2026-09-11  
**Session status:** ACTIVE  
**Primary mode:** Planning/Design + Learning-by-Doing  
**Selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-11_synthesis-producer-reachability-and-correctness.md`](2026-09-11_synthesis-producer-reachability-and-correctness.md)  
**New stable owner:** [`../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md)

## Session anchor

The preceding design work established both a coherent action-permission matrix and a current-source producer/reachability map. This slice promotes only the stable reusable synthesis semantics to their proper durable owner and pressure-tests that complete contract once before implementation is admitted.

No product source or tests are changed in this slice.

## Owner decision

The stable synthesis semantics do **not** belong inside the existing Product Decision Model specification.

Reason:

```text
PRODUCT DECISION MODEL
→ technical candidate/applicability/investigation/stopping
→ explicitly stops at the boundary to later maintainer-facing synthesis

MAINTAINER ACTION SYNTHESIS
→ overall action-relative sufficiency
→ final maintainer-facing action permission/projection
→ residual uncertainty, defer, abstention, claim limits
```

The documentation-promotion rules say a new specification is justified only when a distinct durable framework-independent semantic responsibility genuinely lacks an owner. This condition is satisfied here.

Therefore the accepted stable owner is:

`docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md`

The Charter remains the owner of the five broad outcome classes. The new specification does not add another public action.

## Accepted contract shape

The specification accepts these core rules:

```text
1. evidence sufficiency is action-relative;
2. every emitted action requires positive permission;
3. actions are not a severity ladder;
4. missing/unsupported/correctness-limited evidence cannot satisfy permission;
5. semantic availability and current producer reachability are separate;
6. merge-after-normal-review requires positive bounded coverage/context closure;
7. targeted checks require concrete bounded discriminating maintainer checks;
8. investigate requires a grounded broader/adaptive inquiry;
9. block requires an independently established current-proposal hold condition;
10. defer requires a specific useful outside/future responsibility + re-entry trigger;
11. abstain is the honest result when no other action is positively justified;
12. the first synthesis method must remain deterministic and transparent.
```

The Charter's combined `investigate or block` action now has one required internal distinction:

```text
public action = investigate or block
+
disposition = investigate | block
```

This preserves the Charter outcome family while retaining the materially different next-step semantics established by the evidence.

## Whole-contract pressure pass

### Favorable — S004 / S005

The accepted favorable permission survives the real favorable/control evidence:

```text
exact identity
+ bounded evidence/coverage authority
+ target-specific upstream mapping
+ no decision-critical contradiction/gap inside the owned horizon
→ merge after normal review
```

The specification correctly rejects the weaker shortcut:

```text
nothing bad found
→ merge
```

S009/S010 remain the counter-pressure preventing that shortcut because technical closure is not generic repository-context or candidate-discovery completeness.

### Targeted check — S006

S006 remains compatible with:

```text
one exact decision-critical unknown
+ one bounded discriminating check
+ interpretable outcomes
→ run targeted checks
```

The stable rule additionally preserves the accepted execution boundary: a useful UpgradePilot-executable investigation should not be unnecessarily outsourced to the maintainer.

### Investigate — Cactus screening evidence

The real preserved Cactus evidence remains compatible with:

```text
material concern grounded
+ several materially different evidence directions
+ intermediate findings can prune/refine the next action
+ no established current-proposal blocker
→ investigate disposition
```

The specification does not convert every multi-check situation into investigate; the discriminator is broader/adaptive inquiry rather than check count alone.

### Block — S003

S003 remains compatible with:

```text
current proposal failure/constraint conflict sufficiently established
+ no further inquiry required to justify withholding current proposal as-is
→ block disposition
```

The specification correctly preserves that block is proposal-relative and does not mean permanent dependency incompatibility.

### Defer — S012 / no-tool transfer

The accepted defer rule survives the outside-responsibility evidence:

```text
decision-critical unknown
+ no justified current UpgradePilot investigation
+ specific useful outside/future evidence responsibility
+ concrete re-entry trigger
→ defer
```

The specification rejects `missing capability → defer`.

### Abstain — honest unresolved/no-tool control

The accepted abstain rule survives:

```text
material insufficiency remains
+ no block
+ no concrete targeted check
+ no grounded broader inquiry
+ no specific outside/future responsibility
→ abstain
```

This prevents fake activity from replacing honest uncertainty.

## Producer/reachability pressure

The stable semantics also survive today's implementation boundary without being weakened to fit it.

Current normal producers still imply approximately:

```text
merge after normal review
→ generally unreachable because positive generic discovery/context coverage is absent

run targeted checks
→ semantic permission exists, but no generic maintainer-check producer

investigate
→ semantic permission exists, but no generic broader-inquiry producer

block
→ potentially reachable in narrow trusted producer-grounded cases

defer
→ semantic permission exists, but no generic outside/re-entry producer

abstain
→ projectable when synthesis has valid input and no other permission is established
```

This is accepted behavior of the **semantic contract**: current reachability must not weaken the meaning of an action.

## Correctness pressure

The specification deliberately promotes only the stable trust rule:

```text
known identity/provenance/interpretation weakness
→ evidence may be preserved
→ but it cannot satisfy a permission above its trustworthy proof strength
```

The current patch/revision defect, static command-recognition false positives, and workflow-attempt mixing remain implementation/evidence facts owned by their existing investigation/repair responsibility. They are not frozen as permanent synthesis semantics.

This separation prevents the stable specification from becoming a bug log while still ensuring Build cannot ignore those defects.

## Acceptance decision

**Accepted.**

The complete contract survives the present real/real-derived evidence anchors, current producer reachability, and known correctness restrictions without case-specific action rules, opaque scoring, generic planner state, or framework-specific machinery.

No ADR is required yet because no consequential implementation/structural mechanism has been selected. The accepted method remains a transparent deterministic baseline; ordinary Python is sufficient as the starting implementation assumption unless Build discovers a consequential method decision that requires separate ADR treatment.

## Build handoff boundary

Stable semantic acceptance is complete enough to pass the design gate.

The next substantive responsibility is **Build/Implement**, not more synthesis research.

Build must begin from the smallest implementation responsibility that can satisfy the accepted contract at the **currently reachable producer boundary**. It must not fabricate unreachable actions just to exercise every semantic branch.

The first implementation plan should therefore distinguish:

```text
SEMANTICALLY ACCEPTED ACTION
vs
CURRENTLY PRODUCER-REACHABLE ACTION
```

and protect the trust restrictions already established by current evidence.

Exact source type/module shape remains a Build design/implementation decision. The specification intentionally does not freeze Python class names or a package layout.

## Learning-by-Doing state

```text
Slice: stable maintainer-action synthesis semantic acceptance

A — DONE:
    Re-anchored the canonical AGENTS.md A→B→C→D→E loop and oriented the responsibility: choose the durable owner and accept only framework-independent semantics.

B — DONE:
    Created the distinct maintainer-action synthesis specification, pressure-tested the full action family against favorable/targeted/investigate/block/defer/abstain evidence plus producer/correctness constraints, and registered the owner in the docs/specification maps.

C — DONE:
    Preserved this acceptance record and will advance MEMORY.md to the Build handoff after the stable contract passed.

D — CURRENT:
    Post-action teaching/ownership check belongs in the conversation: Ali should understand why the new synthesis specification is separate from the Product Decision Model, why action permission is positive rather than fallback-based, and why accepted semantics may remain unreachable in the current implementation.

E — PENDING ALI RESPONSE:
    Repair any important ownership gap, then orient the first Build slice. Do not silently begin Build before D/E close unless Ali explicitly redirects.
```

## Immediate handoff

```text
stable synthesis semantics accepted
→ post-action ownership check
→ repair learning gap if any
→ activate Build/Implement procedure
→ design/implement the smallest deterministic synthesis result + evaluator at current producer reachability
→ focused tests
→ normal application/CLI integration only after core synthesis behavior is proven
```

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`
