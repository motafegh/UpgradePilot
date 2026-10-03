# Learning Session — Product Direction, Hybrid Reporting, and Maintainer Utility

**Date/time:** 2026-10-03 19:19 Asia/Tehran
**Session status:** ACTIVE
**Primary responsibility/mode:** Learning/discussion only; no `main` mutation
**Branch:** `learning/product-direction-report-2026-10-03`
**Base:** `main@9b281229d8ac9094aec7c3315003267bdd8f6938`
**Related plan:** [Product Direction and Maintainer Utility Investigation](../plans/PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md)
**Current live owner remains:** [MEMORY.md](../MEMORY.md)
**Procedure:** UP-SKILL:upgradepilot-working-memory

## Session anchor

Ali explicitly asked to keep the ongoing `main` work untouched and use this separate branch for learning, discussion, discovery, and durable notes that may be useful later.

This record is deliberately non-controlling. It may preserve hypotheses, questions, useful discoveries, and candidate implications, but it does not change the live project position, accepted semantics, selected implementation responsibility, or authorization on `main`.

Current inherited project position:

- Runtime Dependency-State Cycle 1 is closed and verified.
- The current product-direction work compares action-led, advisor-led, and hybrid delivery.
- The active project cycle on `main` remains in A2 / orientation-discussion territory; no product implementation is authorized by this branch.
- Recent report work is broader than file generation or storage: it concerns faithful maintainer-facing projection, useful explanation under uncertainty, saved-result boundaries, replay distinctions, and independent usefulness evaluation.

## Current learning model

### 1. Report is not merely a saved file

The report direction is currently understood as a product-facing decision-support layer:

```text
internal evidence / findings / uncertainty
        ↓
faithful projection
        ↓
maintainer-readable explanation
        ↓
decision-relevant unknowns
        ↓
justified next checks
        ↓
action or abstention when independently supported
        ↓
optional saved-result / provenance / evaluation
```

Saving a report, preserving raw evidence, replaying analysis, rerunning acquisition, and recovering an interrupted execution are separate promises and should not be collapsed.

### 2. Current direction intuition

Ali's current intuition:

- action-led alone is unattractive because UpgradePilot cannot always justify a strong action;
- hybrid feels more natural because useful assistance can survive uncertainty while action permission remains conservative.

Refined engineering interpretation:

> Advisory usefulness and action permission have different evidence thresholds.

Hybrid should therefore not mean "report plus action by default." It should mean:

> provide the strongest useful decision-support output that the available evidence truthfully supports, while independently controlling whether any stronger action claim has actually been earned.

### 3. Evidence strength ladder

Current conceptual ladder:

```text
observed evidence
      ↓
supported interpretation
      ↓
material unresolved proposition
      ↓
justified discriminating check
      ↓
positively supported maintainer action
```

Each level requires stronger evidence than the previous one.

If the action threshold is not reached, the product may still provide lower-level useful output without weakening claim discipline.

### 4. Main product risk discovered in discussion

A hybrid product can still fail if it becomes an evidence dump.

Useful output should not be organized around:

> everything UpgradePilot knows

but instead around:

> what the maintainer needs to understand to make progress on this exact dependency update.

Working conceptual structure:

```text
WHAT MATTERS
WHY IT MATTERS
WHAT REMAINS UNKNOWN
WHAT TO DO NEXT
WHY UPGRADEPILOT IS ALLOWED TO SAY THIS
```

Detailed provenance may remain inspectable underneath rather than dominating the first user-facing layer.

## Real-case learning anchors

### S014 — already satisfied vs installed by command

Useful distinction:

- command success plus exact requirement can support a state proposition such as "exact version satisfied/present at command completion";
- it does not necessarily support "this command installed the version";
- later persistence, later exercise, compatibility, and merge safety remain separate propositions.

Product-direction implication:

- action-led can truthfully abstain but may under-deliver useful information;
- advisor-led can explain the state/provenance distinction;
- hybrid can preserve that explanation while keeping action permission independent.

### S015 — marker-scoped applicability

Useful distinction:

- changed requirements file consumed != changed exact requirement applies in this environment;
- a green sibling matrix row cannot establish the changed marker-scoped dependency when the marker does not apply there;
- the relevant Python 3.8 row can fail while Python 3.9 succeeds because they exercise different applicable requirements.

Important current-product limitation:

- current normal product extraction does not support marker-bearing exact pins;
- therefore archived research knowledge must not be silently projected as current automated product output.

This sharpens a general rule:

```text
useful information exists in reality
        !=
UpgradePilot can currently acquire/derive it
        !=
UpgradePilot can currently present it
```

Hybrid must remain bounded by normal producer reachability and explicit uncertainty.

## Candidate discoveries worth carrying forward

These are branch-local hypotheses, not accepted design decisions.

1. **Usefulness should be graded by claim strength, not by binary action success.**
   A run that cannot justify merge/block may still materially reduce maintainer reasoning burden.

2. **Report projection should be decision-relevant rather than evidence-complete.**
   The first layer should prioritize the smallest set of findings and unknowns that change the maintainer's next decision.

3. **A good abstention should still be useful.**
   "Cannot decide" is weak if unexplained. A strong abstention may identify the exact missing proposition and, when supported, the cheapest discriminating check.

4. **A justified next check is itself a substantive product outcome.**
   It should not degrade into generic advice such as "run more tests." It needs a named unresolved proposition and an observation that could materially resolve it.

5. **Research-case insight and normal product capability must remain separate.**
   Product Simulation may reveal what a useful future report would say without proving that today's normal product can produce that statement.

6. **The likely user-facing architecture may be layered.**
   One layer exposes concise decision support; deeper layers expose provenance, evidence detail, and proof limits for trust/debugging.

## Open questions for continued learning

1. What exactly distinguishes a **justified next check** from speculative advice?
2. What minimum output should remain useful when UpgradePilot abstains?
3. How should report content be prioritized so technically correct evidence does not become noise?
4. Which internal typed results are already strong candidates for user-facing projection, and which are too low-level?
5. What information must be available to independently evaluate whether a report actually reduces maintainer work?
6. Where should an LLM eventually help: discovery, synthesis/presentation, or neither until a measurable deterministic baseline exists?
7. How should a future report distinguish:
   - observed fact,
   - supported interpretation,
   - unresolved proposition,
   - proposed check,
   - permitted action?

## Current route

Continue learning/discussion without changing `main`.

Near-term topic:

> distinguish a genuinely useful, evidence-backed next check from generic/speculative advice, and connect that distinction to UpgradePilot's existing investigation and stopping architecture.

When a discussion produces a durable useful discovery, add it here. If a finding later deserves acceptance on `main`, promote it only through the correct plan/specification/ADR/live-owner process with explicit authorization.

## Handoff

Current working hypothesis:

> Hybrid is promising not because it is more comfortable, but because it separates the threshold for useful explanation from the stronger threshold for action permission.

The next learning step is to test whether UpgradePilot's existing investigation/stopping model can already support **specific discriminating next checks**, and where the current product would still lack enough evidence to do so honestly.

No product/source/test/specification/plan/live-memory change has been made on `main` by this learning branch.
