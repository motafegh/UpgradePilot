# Product Simulation Scenario Coverage

**Status:** Active evolving discovery record  
**Controlling plan:** [`../plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md`](../plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md)

## Purpose

Track whether the manual runtime scenarios are materially different enough to expose the real UpgradePilot operating model.

This file is not:

- a frozen taxonomy;
- a fixed ten-case list;
- a product schema;
- a claim of exhaustive real-world coverage;
- a checklist that every case must satisfy.

Add, split, merge, rename, or remove dimensions when scenario evidence justifies it.

## Selection rule

Use at least ten substantially different real cases before final synthesis, but do not stop merely because ten exist and do not continue merely to increase the count.

Select the next case because it contrasts with completed evidence or addresses a material unresolved product question.

A useful next case should expose at least one of:

- a new actor or source;
- a new invocation or evidence requirement;
- a new runtime branch or ordering;
- a new failure, degradation, or uncertainty state;
- a different repository-specific relevance pattern;
- a different decision or user-interaction need;
- a challenge to a repeated assumption;
- a method limitation not visible in existing cases.

## Scenario register

Add rows only when a real case is selected.

| Scenario | Repository/update | Why selected | Material differences | Status | Most important product insight |
|---|---|---|---|---|---|

## Initial non-exhaustive coverage dimensions

The entries below are discovery prompts. They are neither mandatory categories nor hard limits.

| Dimension | Starting contrasts to consider | Covered by | Remaining uncertainty |
|---|---|---|---|
| Update scale and lifecycle | patch, minor, major, pre-release, yanked, replacement | — | — |
| Dependency relationship | direct, transitive, optional, runtime, development, test, build | — | — |
| Change shape | manifest-only, lockfile-only, source/config changes, multiple packages | — | — |
| Upstream information | complete, missing, fragmented, ambiguous, contradictory, migrated source | — | — |
| Repository relevance | directly affected, indirectly affected, apparently unaffected, unresolved | — | — |
| Compatibility change | interpreter, operating system, architecture, build tool, API, behavior | — | — |
| CI and test evidence | passing, failing, unavailable, stale, flaky, skipped, unrelated failure | — | — |
| Security context | ordinary maintenance, known advisory, incomplete disclosure, disputed relevance | — | — |
| Package implementation | pure Python, native/compiled, generated artifacts, platform-specific wheels | — | — |
| Evidence agreement | agreement, partial agreement, cross-source contradiction, no corroboration | — | — |
| Decision shape | normal review, targeted checks, investigate/block, defer, abstain, new candidate outcome | — | — |
| User interaction | fully automatic investigation, clarification needed, authorization needed, manual follow-up | — | — |
| Reproducibility | stable historical case, moving open PR, unavailable artifact, changed upstream state | — | — |
| Investigation value | extensive context useful, simple evidence sufficient, extra investigation adds little | — | — |

## Cross-case questions to monitor

These questions may change as the operating model develops:

- What is the smallest credible invocation input?
- Which identity elements must be supplied and which can be discovered?
- Which evidence sources are universal, conditional, or rarely useful?
- Which questions recur across cases and which are case-specific?
- Which evidence can affect a recommendation directly?
- Which evidence needs corroboration before it may affect a recommendation?
- Which missing evidence causes degradation, targeted work, deferral, or abstention?
- Where is user clarification or authorization genuinely required?
- Which runtime stages are stable enough to automate?
- Which candidate methods generalize across responsibilities?
- Which tasks should remain human-reviewed?
- Which current M2-S03 assumptions survive the manual cases?
- Which responsibilities belong in later milestones or outside UpgradePilot?

Add new cross-case questions when real evidence exposes them.

## Next-case selection record

After each completed scenario, record one or more useful contrasting needs. This is not an automatic authorization to select a case; it is input to the next discussion.

| From scenario | Contrasting case needed | Reason | Priority or dependency |
|---|---|---|---|

## Coverage interpretation

A marked dimension means only that at least one case exposed that condition at the documented depth.

It does not establish:

- complete understanding;
- general product capability;
- implemented support;
- method reliability;
- representative frequency in the ecosystem;
- safety or correctness beyond the evidence.

Use scenario records and final synthesis—not checkmarks alone—to judge readiness to resume implementation.