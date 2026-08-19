# Plan 04 — Current Application Boundary → Return to Building

**Role:** learning execution map under `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`  
**Primary responsibility:** connect implemented Cluster-5 capability to the ordinary application seam without pretending integration already happened  
**Implementation anchor:** `f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099`  
**Prerequisite:** Plans 01–03 understood sufficiently for an end-to-end reconstruction  
**Live-state authority:** `../../MEMORY.md`  
**Career ownership overlay:** `CAREER_DAY30_OWNERSHIP_HANDOFF.md` — modification/diagnosis evidence rules only when legitimate project work provides the opportunity  
**Status:** `[ ] NOT STARTED`

## Purpose and stop line

Close this bounded learning phase by distinguishing:

```text
domain capability exists and has focused tests
!=
ordinary application currently invokes that capability
```

Then perform one compact end-to-end ownership check and hand back to the live learning-by-doing build as soon as the next project step is understandable and safe.

This plan is **not** authorization to implement Cluster 6. At every handoff, re-read `MEMORY.md`; live project authority decides the actual next build action.

## Pace rule

Do not turn this into a comprehensive review of the whole application. Inspect only the orchestration seam required to see what the normal public-PR path calls today, what the new typed path provides, and what must happen before future integration.

## Smart seam-reading, ownership, and engineering-audit rule

At the application boundary, read enough code to understand **actual orchestration**, not every branch of the application:

```text
entry/orchestration path
→ Ali predicts current/desired behavior at a meaningful seam
→ exact legacy call and data shape
→ exact new typed capability available in parallel
→ representative tests protecting both paths
→ material syntax/control flow at the seam
→ rationale for the transitional split
→ critique whether the seam is still justified at the pinned/live state
```

Do not assume that a compatibility property, legacy evaluator, or duplicated path is good engineering merely because it was intentionally retained. Determine whether it is a deliberate migration boundary, what risk it isolates, and whether the live project state says it is still temporary. Likewise, do not remove or redesign it during learning without authorization.

This plan is the **prime candidate** for a future Career ownership-bearing modification because it exposes a real integration seam, but only if live `MEMORY.md` selects/authorizes the corresponding implementation. Career evidence never creates implementation authority.

If such a legitimate mutation is selected, use this protocol before AI writes the change:

```text
Ali states:
what should change?
why does this layer own it?
what should remain unchanged?
what observable result/test is expected?
what stronger claim will still not be proved?
```

After implementation, Ali inspects the actual diff/source/tests and explains what changed, why there, what protects it, whether the result matched the prediction, and where understanding still stops.

If a real relevant failure occurs, pause before repair for Ali to identify the likely failure layer, best current hypothesis, and one discriminating check. Do not manufacture a failure merely to satisfy Career evidence.

## Chunk map

### [ ] Chunk 1 — Ordinary application path vs implemented Cluster-5 path

**Main subjects**
- application/orchestration responsibility;
- current public-PR CI evidence sequence;
- retained legacy compatibility projection and evaluator;
- new Cluster-5 typed coverage path that exists but is not yet wired into ordinary orchestration at the pinned snapshot.

**UpgradePilot source / functions / types**
- `src/upgradepilot/investigation.py`
  - `PublicPullRequestInvestigation`;
  - `investigate_public_pull_request(...)`;
  - `DependencyChangeAnalysis.direct_requirements_install_path` usage;
  - construction of `WorkflowDependencyExerciseInput`;
  - current call to `evaluate_dependency_ci_exercise(...)`;
- `src/upgradepilot/dependency/analysis.py`
  - `DependencyChangeAnalysis.source_contexts` vs compatibility property `direct_requirements_install_path`;
- `src/upgradepilot/ci/dependency_exercise.py`
  - retained `evaluate_dependency_ci_exercise(...)`;
  - new `evaluate_dependency_ci_coverage(...)` for contrast;
- `src/upgradepilot/ci/workflow_commands.py`
  - retained `inspect_workflow_commands(...)` vs `inspect_workflow_dependency_evidence(...)`.

**Material code-reading / ownership focus**
- before the seam is fully explained, Ali predicts which path ordinary orchestration currently uses at the inspected snapshot and which typed capability remains parallel;
- trace the orchestration call chain and typed object construction at the exact migration seam;
- explain material conditionals/early returns/unions only where they determine which evaluator/path runs;
- inspect compatibility projections as transitional APIs rather than treating them as permanent architecture by default;
- use at least one representative test to explain setup → action → assertion → protected integration behavior → non-proof.

**Focused tests**
- `tests/test_investigation.py`;
- `tests/test_cli.py` where presentation/integration behavior matters;
- `tests/test_ci_dependency_exercise.py` for retained legacy behavior;
- `tests/test_ci_dependency_coverage.py` for the new parallel contract.

**Engineering-audit prompts**
- What migration risk or responsibility separation justified keeping legacy and new typed paths in parallel?
- Is `direct_requirements_install_path` clearly marked/used as a compatibility projection rather than a new source of truth?
- Does the seam create duplicated semantics or stale risk, and does current live state already plan its removal/migration?
- Which observations are implementation facts versus recommendations for the next authorized cluster?

**Do not miss / assume**
- focused domain tests passing does not mean the public application path already uses the capability;
- Cluster 5 deliberately retained the legacy evaluator so application migration could remain a separate responsibility;
- deliberate/transitional does not automatically mean optimal forever;
- do not describe Cluster-6 behavior as implemented before source/tests and live memory establish it;
- comments/documentation around the seam are scaffolding; executable call/data flow is the ownership evidence.

**Gate / proceed when**
- Ali can point to the exact legacy call in `investigation.py`, name the new typed alternative, explain the material code/data-shape difference and one representative test, and evaluate why the seam exists without confusing critique with authorization to change it.

### [ ] Chunk 2 — Compact end-to-end reconstruction

**Main subjects**
- reconstruct the current implemented reasoning chain without re-teaching every detail;
- use S001 as the main positive path;
- use S011 and S005 only as short transfer checks;
- identify proof boundaries and current integration stop.

**Ali ownership check**
Ali should be able to reconstruct, with decreasing assistance:

```text
S001 real dependency update
→ exact change/source context
→ static workflow/environment selection
→ exact selected-environment membership witness
→ static CI consumption
→ separate direct exercise
→ separate runtime authority
→ supported_not_correlated
→ ordinary application integration seam
```

Then predict before the answer is restated:

```text
S011: affected mlx + selected dev → not_established
S005: tox-mediated lock use → transfer pressure; do not invent unsupported interpretation
```

The reconstruction should include central owners/functions, source paths, material executable code mechanisms, and representative-test meaning, but it is **not** a demand to recite every helper or line.

**Career evidence consolidation**
At this point, identify only evidence actually demonstrated:
- source candidate(s);
- representative test candidate(s);
- changed-case transfer candidate;
- modification candidate only if legitimate authorized work occurred;
- diagnosis candidate only if a real failure occurred.

Do not inflate a category merely to make the return package look complete.

**Do not miss / assume**
- keep resolver satisfiability/currentness, exact runtime version witness, static↔runtime correlation, and behavioral safety outside the established chain;
- remaining `[~]` gaps are acceptable when they do not block the next build decision;
- do not repeat every earlier chunk merely for ceremony;
- any design concerns found during the route should be classified as blocking, non-blocking, or future refactor/capability pressure rather than silently forgotten.

**Gate / proceed when**
- Ali can narrate the major propositions, identify central owners/functions and important control flow, recognize the current application seam, explain representative-test meaning, and distinguish implementation truth from any remaining engineering judgments without needing a line-by-line script.

### [ ] Chunk 3 — Handoff to live building

**Main subjects**
- classify any remaining learning gaps as GREEN / YELLOW `[~]` / RED;
- classify material engineering-audit findings separately from learning gaps;
- re-read `MEMORY.md` and the active B2 implementation working memory;
- identify the current authorized next action from live project state;
- preserve only material learning/design/ownership evidence that should survive the handoff;
- continue remaining learning just-in-time during future implementation.

**Current snapshot reminder**
At original plan creation, `MEMORY.md` recorded Cluster 5 validation pending. By 2026-08-18 live `MEMORY.md` had advanced to Cluster 5 COMPLETE/GREEN (`508 tests / OK`) and selected a bounded source-clarity/refactoring pass before Cluster 6. This paragraph remains only a dated reminder: **re-read live `MEMORY.md` when this chunk is reached** because it alone owns the current action.

**Legitimate modification opportunity rule**
If live project authority now selects an integration/refactor/change at this seam:

```text
PRE-CHANGE
Ali predicts owner + intended behavior + unchanged behavior + expected test/result + proof limit

IMPLEMENT
AI assistance remains allowed and recorded honestly

POST-CHANGE
Ali inspects actual diff/source/test/result and explains whether evidence matched prediction
```

If the live action is still learning, source clarity, validation, or another bounded responsibility, follow that instead. Plan 04 completion does not create a need to mutate code.

**Real failure diagnosis rule**
If a genuine failure/unexpected result appears during the authorized work, treat it as a diagnosis opportunity before repair. If none appears, record “no natural diagnosis opportunity” rather than breaking something intentionally.

**Do not miss / assume**
- plans are not a queue that must be exhausted before building resumes;
- if live implementation has moved, adapt remaining learning to the new frontier instead of finishing obsolete study for its own sake;
- no product mutation is authorized merely by completing this learning plan;
- a useful design critique may become an input to the next planning/build discussion, but only after it is grounded in source/tests/live project state;
- Career ownership evidence records participation quality; it does not select the next project responsibility.

**Gate / proceed when**
- there is no RED learning gap that would make the next authorized project step materially unsafe or incomprehensible;
- material engineering concerns are recorded/classified rather than mistaken for settled architecture decisions;
- actual source/test/transfer/modification/diagnosis evidence is preserved honestly at the level demonstrated;
- the next action is taken from current `MEMORY.md`, not from this frozen plan.

## Plan-level TODO / gate

- [ ] Current ordinary application CI path is traced at the integration seam.
- [ ] Legacy-vs-new typed evaluator distinction is clear at both conceptual and executable code/control-flow levels.
- [ ] Transitional compatibility machinery is understood and engineering-audited rather than blindly accepted.
- [ ] At least one representative integration/seam test is understood beyond “green”.
- [ ] S001 can be reconstructed end to end through the implemented Cluster-5 domain boundary.
- [ ] S011/S005 can be used as Ali-first transfer checks without reopening full case studies.
- [ ] Remaining learning gaps and engineering-audit findings are classified instead of blocking on perfection.
- [ ] Live `MEMORY.md` is re-read before any return-to-building decision.
- [ ] Any legitimate modification uses pre-change prediction and post-change diff/test explanation; no modification is forced merely for Career evidence.
- [ ] Any real failure uses diagnosis-before-repair; no failure is manufactured.
- [ ] Learning hands back to implementation as soon as the next project step is safe and understandable.

## Depth / deliberate deferral

**Must master across the route:** domain-vs-application integration distinction, main proposition ladder, central responsibility ownership, current proof boundary, material orchestration code/control flow, representative-test reasoning, ability to critique transitional architecture proportionately, and ability to re-enter implementation intelligently.  
**Operational only:** incidental CLI/presentation details not involved in the seam, unrelated orchestration branches, incidental syntax.  
**Deferred unless selected later:** Cluster-6 implementation details before live authorization, Tranche-2 static↔runtime correlation, Cluster-7 resolver-satisfiability work, later compatibility/safety/action responsibilities.

## Completion condition

This bounded learning phase is complete enough to return to building when Ali understands the major current mechanism and application seam sufficiently to participate in the next authorized implementation/validation decision.

Do **not** wait for perfect recall of every helper, syntax detail, external tool, or deferred proposition. Continue deeper learning later when future building work makes it causally relevant. Career reassessment should use only evidence actually demonstrated; it must not delay legitimate project progress merely to fill every evidence category.
