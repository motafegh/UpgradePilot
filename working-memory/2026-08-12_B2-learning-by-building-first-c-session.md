# B2 Learning-by-Building First-C Session

**Date:** 2026-08-12  
**Type:** Dated session working memory  
**Live-state authority:** `../MEMORY.md` only

## Session intent and how we will proceed

This session returns UpgradePilot learning to its intended **learning-by-building** mode after a useful but overly theory-heavy review of the new mature-system horizon.

The goal is not to study the horizon, plans, or A→D model front-to-back. The goal is to continue the real B2 implementation in small steps and learn only the concepts, source, syntax, plan clauses, and horizon context needed by the step currently being built.

Working loop:

```text
small real implementation step
→ inspect only the exact relevant source/tests/plan/horizon section
→ Ali predicts or explains the behavior where useful
→ learn the minimum concepts/syntax needed to understand the step correctly
→ design the smallest justified change
→ test/predict the behavior
→ implement
→ run focused proof and diagnose together
→ briefly reconnect the result to the plan and mature-system horizon
→ continue
```

Session behavior:

- prefer code, tests, concrete examples, and execution over standalone theory;
- do not require Ali to memorize the 895-line mature-system horizon;
- use `../proposals/UPGRADEPILOT_MATURE_SYSTEM_HORIZON.md` as an orientation map when a real implementation question needs the larger-system connection;
- use the selected B2 plan just in time, reading only the clauses that own the next bounded change;
- explain terminology and syntax at the point it becomes operationally relevant;
- preserve correct technical mental models without long repeated lectures;
- keep steps small enough that Ali can question, predict, and trace what the code is doing before the next step;
- distinguish implemented truth from plans/horizon descriptions throughout the session.

## Starting technical position

The first bounded Python-support-drop A→B slice is implemented and locally verified. The existing domain model can explicitly represent the important pre-acquisition state:

```text
exact target Python declaration not yet acquired
→ target-specific proposition unresolved
→ candidate applicability unresolved
```

This differs from:

```text
target acquisition/evaluation attempted
→ evidence unavailable/invalid/problematic
→ unresolved for a different provenance/reason
```

The previous local verification established 24 focused tests passing, 384 total active tests passing, and installed imports working. That verification did not establish runtime Conversation-C investigation selection/stopping.

Reference: `2026-08-11_B2-impact-applicability-local-verification.md`.

## Immediate learning/build sequence

Proceed in these small steps, adjusting only when the source/tests reveal a better bounded sequence:

1. **Finish the path-level source reading** — inspect `evaluate_applicability_path()` in `src/upgradepilot/impact/applicability.py`, using concrete proposition states rather than another abstract logic lesson.
2. **Read candidate-level composition** — inspect `evaluate_candidate_applicability()` and connect it to the path result just understood.
3. **Trace the first Python-support A→B flow briefly** — follow only the calls and data needed to see how the mechanism-specific candidate reaches the generic applicability composition.
4. **Inspect the existing orchestration and target-acquisition seam** — identify the exact source/functions already used to acquire the exact-head target Python declaration and where the current runtime jumps directly to that acquisition.
5. **Define the smallest first C runtime behavior** — from pre-acquisition unresolved state, derive the discriminating target and select the already-existing exact-head target-declaration acquisition as the justified investigation.
6. **Test/predict first** — state the expected observable behavior and add/adjust the narrowest relevant test before or alongside implementation.
7. **Implement the bounded C activation** — no generic planner; only the first real discriminating-investigation path required by the selected B2 responsibility.
8. **Verify together** — run focused tests first, then the nearest broader regression proof required by the change; diagnose any failure before adding breadth.
9. **Reconnect to the horizon** — after the code works, locate the completed behavior in the mature map (`candidate applicability → discriminating investigation`) in a short practical review.

## Current implementation target

The smallest expected runtime C case is:

```text
candidate applicability = unresolved
because exact target Python declaration has not yet been acquired

↓

discriminating target = exact target Python declaration

↓

selected investigation = acquire/read exact-head target declaration

↓

observation feeds the existing Target-Python relevance evaluator

↓

candidate applicability is reevaluated
```

The exact implementation shape is **not assumed by this record**. Source and tests must be inspected before editing.

## Session stop boundaries

Do not expand this session merely because the mature horizon contains larger future responsibilities.

Unless a concrete blocker in the first C activation proves otherwise, do not introduce:

- broad candidate-discovery implementation;
- final mechanism-family taxonomy;
- cross-candidate/D-level overall sufficiency or maintainer-action synthesis;
- a generic investigation planner;
- numerical value-of-information scoring/ranking;
- a generic retry/history/lineage framework;
- speculative source packages/modules/directories;
- final action mapping;
- unrelated B3/B4/B5/X1 infrastructure.

The mature-system horizon remains available to explain **where** the small slice belongs, not to authorize building the rest of the mature system now.

## Session learning success condition

This session is successful if Ali can increasingly follow and explain the real code path being changed, including:

- how proposition states compose into a path;
- how paths compose into candidate applicability;
- why pre-acquisition unresolved state creates a specific C investigation need;
- where the selected investigation enters the current orchestration;
- what the new test proves and does not prove;
- where the implemented slice sits in the mature-system horizon.

No requirement exists to memorize the full theory or horizon taxonomy before implementation can continue.

## Record maintenance

Update this same dated working-memory record with material session decisions, implementation evidence, debugging conclusions, or handoff context produced during this session.

Do not use this file to replace `../MEMORY.md` as the live continuation owner. Update `MEMORY.md` only if the live project position, continuation-relevant verification, blocker, selected continuation, or other fact owned there materially changes.
