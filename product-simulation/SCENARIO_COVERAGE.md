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

| Scenario | Repository/update | Why selected | Material differences | Status | Most important product insight |
|---|---|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md) | `pydantic/pydantic` — Soup Sieve 2.6 → 2.8.4 | First stable real PR; small diff with non-trivial transitive, security, compatibility, and CI questions | Lockfile-only; transitive docs tooling; reviewed security fixes; green relevant CI; merged historical case | Complete | Decision authority required joining lock graph, target usage, upstream/advisory meaning, and exact CI coverage |

## Evolving coverage dimensions

The entries below are discovery prompts. They are neither mandatory categories nor hard limits. “Covered” means only that the named case exposed the condition at its documented depth.

| Dimension | Starting contrasts to consider | Covered by | Remaining uncertainty |
|---|---|---|---|
| Update scale and lifecycle | patch, minor, major, pre-release, yanked, replacement | S001: minor update crossing 2.7–2.8.4 | major, pre-release, yanked, replacement |
| Dependency relationship | direct, transitive, optional, runtime, development, test, build | S001: transitive documentation/tooling | direct runtime, optional, test-only, build/native |
| Change shape | manifest-only, lockfile-only, source/config changes, multiple packages | S001: one-package lockfile-only | all other shapes |
| Upstream information | complete, missing, fragmented, ambiguous, contradictory, migrated source | S001: complete changelog plus tags, PyPI, and advisories | missing/fragmented/contradictory |
| Repository relevance | directly affected, indirectly affected, apparently unaffected, unresolved | S001: indirect docs relevance; exploitability unresolved/appears limited | direct runtime and apparently irrelevant cases |
| Compatibility change | interpreter, operating system, architecture, build tool, API, behavior | S001: Python floor change, irrelevant after target comparison | API, OS, architecture, build-tool conflicts |
| CI and test evidence | passing, failing, unavailable, stale, flaky, skipped, unrelated failure | S001: relevant CI passed; third-party workflow skipped; secret-bearing post-merge run unavailable | failing, stale, flaky, unrelated failures |
| CI-to-responsibility alignment | owning path exercised, only adjacent path exercised, no relevant path, unclear | S001: docs dependency path exercised by PR docs build | misleading green CI and partial coverage |
| Security context | ordinary maintenance, known advisory, incomplete disclosure, disputed relevance | S001: two reviewed high-severity advisories; target exploitability not established | advisory conflict, incomplete disclosure, active exploitation |
| Security trigger identity | explicitly labelled, strongly inferred, unknown, contradicted | S001: strongly inferred from advisory timing, fixed version, and absent periodic uv config | explicit and contradictory cases |
| Package implementation | pure Python, native/compiled, generated artifacts, platform-specific wheels | S001: pure Python universal wheel | native/compiled and platform-specific |
| Evidence agreement | agreement, partial agreement, cross-source contradiction, no corroboration | S001: material agreement with bounded unresolved questions | contradiction and no-corroboration |
| Decision shape | normal review, targeted checks, investigate/block, defer, abstain, new candidate outcome | S001: normal review; variants show targeted checks and investigate/block | real primary cases for other outcomes |
| User interaction | fully automatic investigation, clarification needed, authorization needed, manual follow-up | S001: no clarification needed; human decision retained | clarification/authorization cases |
| Reproducibility | stable historical case, moving open PR, unavailable artifact, changed upstream state | S001: stable historical base/head; one operational run unavailable | moving PR and disappearing evidence |
| Investigation value | extensive context useful, simple evidence sufficient, extra investigation adds little | S001: graph/advisory/CI context changed interpretation; source audit became unnecessary | genuinely trivial cases and high-cost cases |
| Invocation model | PR locator only, exact identity supplied, event payload, manual evidence bundle | S001: PR URL can locate case; exact identity acquired and frozen | event/webhook and offline replay inputs |
| Dependency-path evidence | declared direct path, lock-derived transitive path, conditional marker path, unresolved path | S001: lock-derived multi-hop docs paths | markers, extras, multiple versions, unresolved graphs |
| Exploitability evidence | confirmed exposure, confirmed non-exposure, limited static evidence, unavailable production context | S001: limited static evidence; private context unavailable | confirmed positive/negative cases |

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
- How should the system distinguish vulnerable-package presence from target exploitability?
- How much CI-path alignment is required before a green result can affect a recommendation?
- When may a PR URL alone serve as invocation, and when is an offline evidence bundle required?
- How should inferred update-trigger context be represented without turning it into fact?
- Which dependency graph representations handle groups, extras, markers, and multiple lock resolutions accurately?

Add new cross-case questions when real evidence exposes them.

## Next-case selection record

| From scenario | Contrasting case needed | Reason | Priority or dependency |
|---|---|---|---|
| S001 | Direct runtime dependency with an API/behavior change and failing or conflicting CI | Tests source-level relevance, failure attribution, targeted-check sufficiency, investigate/block behavior, and conflict reporting | Highest-value next contrast |
| S001 | Missing or fragmented upstream release information | Tests whether the investigation can proceed without a complete changelog | Later contrast |
| S001 | Native or platform-specific dependency update | Tests artifact/platform/architecture branches absent from the pure-Python case | Later contrast |

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
