# Learning-by-Doing Cycle Governance Refinement

**Date:** 2026-09-28
**Status:** CLOSED — conceptual model agreed, governance owners updated, consistency scan passed
**Responsibility:** refine UpgradePilot's canonical Learning-by-Doing cycle after the prior single-A/B+C model proved insufficient for fresh-session continuity and whole-cycle state preservation

## Problem observed

The prior model treated A as one pre-implementation orientation block, coupled C mainly to B, and asked E to orient the next slice. In normal UpgradePilot practice, substantive cycles commonly start in fresh conversations, so that model did not explicitly guarantee:

- assistant reconstruction of the latest repository/project truth before teaching;
- Ali onboarding from the last genuinely understood point to the current state;
- a separate stop between continuity onboarding and upcoming-work teaching;
- cycle working-memory creation and A-learning-map initialization at the beginning;
- continuous preservation of meaningful engineering and learning progression across the whole cycle;
- a clean distinction between brief next-responsibility handoff in E and fresh next-cycle teaching in A.

## Agreed canonical model

```text
A0 — current-state reconciliation + cycle initialization
→ A1 — continuity / recent-work onboarding
→ STOP
→ A2 — upcoming responsibility orientation
→ STOP
→ B — real bounded action
→ Verification / evidence gate
→ D — post-work evidence-backed learning / ownership
→ E — gap repair + cycle closure / next-responsibility handoff
→ STOP

C — continuous state preservation across A0→E
```

Key agreements:

- A0 is primarily agent orientation: reconstruct current truth, reconcile contradictions, create the cycle record, and seed a living A-phase orientation/learning map.
- A1 is primarily user continuity: onboard Ali from the last understood point to current state, then stop.
- A2 teaches the upcoming responsibility and its proof boundary; it is anticipatory/minimum-complete and normally lighter than D, then stops before B.
- B remains the real authorized coherent work.
- Verification remains a transition gate rather than a canonical learning phase.
- D remains fundamentally sound but explicitly uses situational depth, compares A2 expectation with reality, and identifies/characterizes ownership gaps.
- E repairs or explicitly defers important D gaps, consolidates proof/non-proof, closes the cycle, and gives only a brief next-responsibility pointer.
- C is cross-cutting rather than sequential; continuous preservation is not continuous logging.
- Smart Situational Override remains the mechanism for justified exceptional compression/adaptation rather than weakening the normal default.

## Owner updates

The agreed model was distributed by responsibility rather than copied verbatim everywhere:

- `AGENTS.md` — compact canonical contract and gates.
- `OPERATING_GUIDE.md` — full conceptual semantics and completion conditions.
- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md` — executable procedure.
- `working-memory/README.md` — cycle-record meaning/status structure and C mechanics.
- `.agents/skills/upgradepilot-working-memory/SKILL.md` — operational working-memory procedure.

Governance update commits:

- `8b4c2f3` — root canonical LbD contract.
- `6db9f01` — full Operating Guide model.
- `bdb9a82` — LbD Skill procedure.
- `faaf763` — working-memory owner alignment.
- `372d504` — working-memory Skill alignment.

## Verification

A cross-file scan found no remaining targeted stale phrases for the old model in the five updated owners, including `A → B → C → D → E`, `B+C`, old `next-slice orientation`, or the old single-A understanding-gate wording.

## Product-cycle relationship

This governance refinement interrupted Increment 2 before product Build. No Increment-2 product source/tests were modified. On resumption, the existing Increment-2 cycle record should be reconciled to the new model rather than pretending the old single-A gate was completed under the new rules.

UP-SKILL:upgradepilot-learning-by-doing
UP-SKILL:upgradepilot-working-memory
