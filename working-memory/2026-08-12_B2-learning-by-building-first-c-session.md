# B2 Learning-by-Building First Discriminating-Investigation Session

**Date:** 2026-08-12  
**Type:** Dated session working memory  
**Live-state authority:** `../MEMORY.md` only  
**Planning correction:** `2026-08-12_B2-responsibility-shaped-expansion-decision.md`

## Session intent and how we will proceed

This session keeps UpgradePilot in **learning-by-building** mode. The project should not return to long theory-first work, but it also should not let one small implementation slice become the architecture horizon.

The working rule is now:

```text
understand the complete owning responsibility
↓
choose the smallest useful implementation increment
↓
learn only what the increment requires
↓
implement + test + diagnose
↓
pressure the result against materially different real evidence
↓
continue thickening the end-to-end product
```

A small step is a learning/execution unit, not a statement that the product responsibility itself is small.

Working loop:

```text
small real implementation step
→ inspect only exact relevant source/tests/plan/horizon/case evidence
→ Ali predicts or explains behavior where useful
→ learn minimum concepts/syntax needed to understand the step correctly
→ design the smallest justified change that still respects the owning responsibility
→ test/predict behavior
→ implement
→ focused proof and diagnosis
→ ask what the result means for the broader responsibility/architecture
→ continue
```

Session behavior:

- prefer code, tests, concrete examples, and execution over standalone theory;
- do not require Ali to memorize the mature-system horizon or decision-model taxonomy;
- use `../proposals/UPGRADEPILOT_MATURE_SYSTEM_HORIZON.md` as an orientation map only when the real implementation needs the larger connection;
- use the selected B2 plan just in time;
- explain terminology and syntax at the point it becomes operationally relevant;
- keep implementation increments small enough that Ali can question, predict, and trace them;
- distinguish source/test truth from plans, simulation evidence, and horizon proposals;
- distinguish **implementation increment boundary** from **product responsibility horizon**;
- never use bare `A`, `B`, `C`, or `D` labels as if Ali is expected to remember them. Prefer the full responsibility name. If shorthand is useful, pair it with:
  - **technical impact-candidate formulation** — formulate a justified mechanism-specific concern;
  - **candidate-specific applicability / evidence / composition** — determine what is established, refuted, unresolved, or conflicted for that exact candidate and target;
  - **discriminating investigation selection / feedback / stopping** — identify evidence that can resolve a material non-final state, select an admitted investigation when justified, feed the observation back, and stop/prune when appropriate;
  - **later overall evidence sufficiency / residual uncertainty / repository context / maintainer-facing synthesis** — combine heterogeneous evidence into an overall supported action or abstention.

## Starting technical position

The first Python-support-drop **technical impact-candidate formulation → candidate-specific applicability** implementation is locally verified.

The domain model can represent:

```text
exact target Python declaration not yet acquired
→ target proposition unresolved
→ candidate applicability unresolved
```

separately from:

```text
target acquisition/evaluation attempted
→ unavailable/invalid/problem evidence preserved
→ unresolved for a different reason
```

Accepted local proof before this planning correction:

- 24 focused impact/applicability/investigation-integration tests;
- 384 active product tests passing;
- installed/import smoke passing.

This proof does **not** establish runtime discriminating-investigation selection/feedback/stopping and does not establish a second technical mechanism.

Reference: `2026-08-11_B2-impact-applicability-local-verification.md`.

## Immediate learning/build sequence — first real investigation loop

Proceed in small implementation steps:

1. finish the concrete reading of `evaluate_applicability_path()`;
2. read `evaluate_candidate_applicability()` and connect path state to candidate state;
3. briefly trace Python-support candidate formulation into applicability composition;
4. inspect `src/upgradepilot/investigation.py`, the exact target-acquisition seam, and the existing read-only repository-file acquisition contract;
5. identify the pre-acquisition unresolved state **before** direct target acquisition;
6. derive the exact target declaration as the discriminating target;
7. represent/select the existing exact-head read-only acquisition as the justified investigation;
8. test/predict the expected behavior before or alongside implementation;
9. execute the admitted acquisition through the existing capability boundary;
10. validate/feed the observation into existing Target-Python relevance evaluation;
11. reevaluate candidate applicability;
12. separately preserve the `already attempted and failed/unavailable` condition so the same investigation is not blindly retried;
13. run focused proof, then the nearest required regression suite;
14. reconnect the completed runtime loop to the selected plan/horizon briefly.

The first complete runtime loop should become:

```text
Python-support impact candidate
→ candidate applicability unresolved because target evidence is not yet acquired
→ discriminating target = exact target Python declaration
→ selected read-only acquisition
→ validated observation
→ Target-Python relevance evaluation
→ candidate applicability reevaluation
```

The exact source/type shape is not predetermined. Active source/tests control implementation placement.

## 2026-08-12 implementation checkpoint — first runtime investigation contract

Source/test inspection confirmed the expected application gap:

```text
DOMAIN MODEL
PythonSupportDropImpactCandidate
→ evaluate without target evidence
→ candidate applicability = unresolved
→ exact target declaration proposition = unresolved because not yet acquired

CURRENT APPLICATION ORCHESTRATION
grounded upstream claim
→ directly read pyproject.toml
→ evaluate target relevance
→ only then build/evaluate the impact candidate
```

Therefore the domain already represents the pre-acquisition uncertainty, but `investigate_public_pull_request()` currently bypasses that state instead of allowing it to drive the acquisition.

The first implementation contract will remain **Python-support-specific** rather than introducing a generic investigation planner before a second mechanism exists.

Selected design direction:

```text
PythonSupportDropImpactAssessment (pre-acquisition)
↓
select a mechanism-specific exact-target-declaration investigation
only when the assessment is unresolved because target evidence is not yet acquired
↓
execute the already-existing read-only exact-head file acquisition
↓
interpret target evidence
↓
evaluate Target-Python relevance
↓
reevaluate the same impact candidate
```

The selection must preserve at least:

- target repository identity;
- exact target revision;
- selected target file/path;
- the unresolved proposition/reason that made the acquisition discriminating.

The result should also remain observable from `PublicPullRequestInvestigation`; otherwise the runtime would perform the acquisition but would not expose that it was **selected because of a specific unresolved reasoning state**.

Architecture restraint at this checkpoint:

- do not create a generic `planner`, registry, plugin system, or universal investigation type;
- do not create a new package solely for one mechanism;
- keep the first selection contract beside the Python-support impact responsibility unless implementation pressure proves otherwise;
- preserve the existing final `python_support_drop_impact_result` as the post-observation applicability result;
- expose the pre-investigation assessment and selected investigation separately enough for tests/traceability to prove the loop actually occurred.

This is intentionally temporary architectural evidence: after the first loop is implemented, the second mechanism/transfer checkpoint will decide which parts are genuinely reusable.

## What happens after the first loop

The session/project no longer treats completion of that first loop as sufficient evidence to freeze the reasoning architecture.

After verification, perform a short implementation-grounded transfer checkpoint against materially different cases:

```text
S006 → static evidence insufficient; targeted behavior observation can be discriminating
S007 → authoritative static evidence sufficient; execution can be pruned/revalidated
S008 → artifact/installability mechanism differs from Python support-range semantics
S009 → repository purpose/provenance context must remain separate from technical applicability
```

The goal is not to study all scenario documents front-to-back. Inspect only the case evidence needed to answer concrete architecture questions raised by the implemented source.

Questions to answer at that checkpoint:

- What is genuinely reusable in our candidate/applicability representation?
- What is specifically Python-support semantics?
- Is `PublicPullRequestInvestigation` beginning to grow one dedicated field/branch per known mechanism?
- What result/orchestration boundary would a second mechanism actually need?
- Which possible abstraction is now supported by evidence, and which is still speculation?

## Second technical mechanism direction

Unless the first-loop implementation exposes a better lower-cost contrast, the next technical breadth step is an **S008-style artifact-serviceability / installation-mode mechanism**.

The learning goal is not OpenCV specifically. It is to implement a real second mechanism that can distinguish concepts such as:

```text
package/interpreter admissibility
!= compatible binary artifact availability
!= source fallback availability
!= source fallback success
```

This should pressure package evidence, target environment relevance, proposition design, stopping, heterogeneous result integration, and orchestration without forcing arbitrary target code execution.

Implementation must not hardcode the S008 repository/package/version answer.

## Architecture-learning checkpoint after two mechanisms

Only after two materially different mechanisms exist should we seriously ask whether a shared abstraction is earned.

Prefer:

```text
mechanism-specific candidate/evaluator
+
small shared contracts where both implementations demonstrate real sameness
```

Avoid:

- universal impact engine;
- generic planner;
- generic rule tree;
- generic dependency graph;
- universal mechanism plugin system;
- opaque scalar impact/safety score.

The lesson to practice is **evidence-driven abstraction**: tolerate some duplication while responsibility is still being discovered, then refactor only demonstrated stable sameness.

## End-to-end continuation

After the first investigation loop and second-mechanism architecture checkpoint, the project should identify the concrete question that blocks the remaining B2 user-visible path:

```text
heterogeneous technical results
+ CI/evidence authority
+ relevant repository/context evidence
+ residual uncertainty
→ what minimum overall-sufficiency / maintainer-output logic is now required?
```

At that point, open only the concrete later synthesis responsibility exposed by source/evidence. Do not continue deepening the impact foundation merely because additional mechanisms can be imagined.

## Session boundaries that still remain

The broader responsibility horizon does **not** authorize implementing every simulation case or mature-system feature.

Do not introduce without demonstrated need:

- exhaustive candidate discovery;
- final universal mechanism taxonomy;
- arbitrary graph traversal infrastructure;
- generic investigation planner;
- numerical value-of-information ranking;
- universal dynamic/differential executor;
- generic retry/history/event-sourcing framework;
- autonomous target repository execution;
- persistence/services/queues;
- unrelated B3/B4/B5/X1 infrastructure;
- final action mapping before concrete synthesis inputs exist.

Stop an **increment** when its evidence is sufficient. Then select the next highest-value move toward the end-to-end B2 responsibility rather than treating the increment stop as a permanent project boundary.

## Session learning success condition

This learning-by-building phase is succeeding when Ali can increasingly:

- explain how proposition states compose into a path and candidate applicability;
- explain why pre-acquisition unresolved state creates a specific investigation need;
- trace the selected investigation into the current orchestration and back into reevaluation;
- distinguish `not checked yet` from `checked but unavailable/failed`;
- explain why a selected investigation may later be pruned;
- compare the first and second technical mechanisms and identify genuine commonality versus mechanism-specific semantics;
- reason about when duplication is appropriate and when abstraction is earned;
- understand how each small code change thickens the public-PR-to-decision product rather than merely closing a local task.

No requirement exists to memorize the full theory or horizon taxonomy before implementation can continue.

## Record maintenance

Update this dated record with material learning/build decisions and implementation evidence produced during this session only when useful. `../MEMORY.md` remains the sole live continuation owner.
