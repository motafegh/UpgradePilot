# Plan 04 — Current Application Boundary → Return to Building

**Role:** learning execution map under `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`  
**Primary responsibility:** connect implemented Cluster-5 capability to the ordinary application seam without pretending integration already happened  
**Implementation anchor:** `f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099`  
**Prerequisite:** Plans 01–03 understood sufficiently for an end-to-end reconstruction  
**Live-state authority:** `../../MEMORY.md`  
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

## Chunk map

### [ ] Chunk 1 — Ordinary application path vs implemented Cluster-5 path

**Main subjects**
- application/orchestration responsibility;
- current public-PR CI evidence sequence;
- retained legacy compatibility projection and evaluator;
- new Cluster-5 typed coverage path that exists but is not yet wired into ordinary orchestration.

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

**Focused tests**
- `tests/test_investigation.py`;
- `tests/test_cli.py` where presentation/integration behavior matters;
- `tests/test_ci_dependency_exercise.py` for retained legacy behavior;
- `tests/test_ci_dependency_coverage.py` for the new parallel contract.

**Do not miss / assume**
- focused domain tests passing does not mean the public application path already uses the capability;
- Cluster 5 deliberately retained the legacy evaluator so application migration could remain a separate responsibility;
- do not describe Cluster-6 behavior as implemented before source/tests and live memory establish it.

**Gate / proceed when**
- Ali can point to the exact legacy call in `investigation.py`, name the new typed alternative, and explain why the seam was intentionally preserved.

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

Then predict:

```text
S011: affected mlx + selected dev → not_established
S005: tox-mediated lock use → transfer pressure; do not invent unsupported interpretation
```

**Do not miss / assume**
- keep resolver satisfiability/currentness, exact runtime version witness, static↔runtime correlation, and behavioral safety outside the established chain;
- remaining `[~]` gaps are acceptable when they do not block the next build decision;
- do not repeat every earlier chunk merely for ceremony.

**Gate / proceed when**
- Ali can narrate the major propositions, identify central owners/functions, and recognize the current application seam without needing a line-by-line script.

### [ ] Chunk 3 — Handoff to live building

**Main subjects**
- classify any remaining learning gaps as GREEN / YELLOW `[~]` / RED;
- re-read `MEMORY.md` and the active B2 implementation working memory;
- identify the current authorized next action from live project state;
- preserve only material learning gaps that should be revisited just-in-time during future implementation.

**Current authorship snapshot reminder**
At plan creation, `MEMORY.md` records:

```text
Clusters 0–4 COMPLETE/GREEN
Cluster 5 IMPLEMENTED / VALIDATION PENDING
Cluster 6 NOT STARTED / HOLD
immediate project action = validate Cluster 5 before Cluster 6
```

This reminder is **not** a permanent status owner. Re-check live memory when this chunk is reached.

**Do not miss / assume**
- plans are not a queue that must be exhausted before building resumes;
- if live implementation has moved, adapt remaining learning to the new frontier instead of finishing obsolete study for its own sake;
- no product mutation is authorized merely by completing this learning plan.

**Gate / proceed when**
- there is no RED learning gap that would make the next authorized project step materially unsafe or incomprehensible;
- the next action is taken from current `MEMORY.md`, not from this frozen plan.

## Plan-level TODO / gate

- [ ] Current ordinary application CI path is traced at the integration seam.
- [ ] Legacy-vs-new typed evaluator distinction is clear.
- [ ] S001 can be reconstructed end to end through the implemented Cluster-5 domain boundary.
- [ ] S011/S005 can be used as transfer checks without reopening full case studies.
- [ ] Remaining gaps are classified instead of blocking on perfection.
- [ ] Live `MEMORY.md` is re-read before any return-to-building decision.
- [ ] Learning hands back to implementation as soon as the next project step is safe and understandable.

## Depth / deliberate deferral

**Must master across the route:** domain-vs-application integration distinction, main proposition ladder, central responsibility ownership, current proof boundary, ability to re-enter implementation intelligently.  
**Operational only:** incidental CLI/presentation details not involved in the seam.  
**Deferred unless selected later:** Cluster-6 implementation details before live authorization, Tranche-2 static↔runtime correlation, Cluster-7 resolver-satisfiability work, later compatibility/safety/action responsibilities.

## Completion condition

This bounded learning phase is complete enough to return to building when Ali understands the major current mechanism and application seam sufficiently to participate in the next authorized implementation/validation decision.

Do **not** wait for perfect recall of every helper, syntax detail, external tool, or deferred proposition. Continue deeper learning later when future building work makes it causally relevant.
