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
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md) | `pydantic/pydantic` — Soup Sieve 2.6 → 2.8.4 | First stable real PR; small diff with non-trivial transitive, security, compatibility, and CI questions | Lockfile-only; transitive docs tooling; reviewed security fixes; green relevant CI; merged historical case | Complete; execution trace retrofitted; advisory timing corrected | Decision authority required joining lock graph, target usage, upstream/advisory meaning, and exact CI coverage |
| [`S002`](scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | `Aidan-Wallace/kubernetes-dashboard-token-api` — HTTPX 0.27.2 → 0.28.1 | Highest-value contrast after S001: direct dependency, API removal, and misleading/partial green CI | Manifest-only; direct-declared/test-framework use/production-installed; superseded predecessor; likely framework compatibility; Docker build green; relevant Python tests skipped; expired logs | Complete; progressive live record | CI decision authority requires changed-path trigger coverage, commands actually executed, exercised responsibility, and tested environment identity—not a green status alone |

## S001 correction note

Fresh official verification during the execution-trace retrofit corrected two original statements:

- both official advisory pages currently state publication on June 1, 2026, not July 9;
- the exact Dependabot trigger is unresolved; a security trigger is plausible but not strongly established by public timing/configuration evidence.

Affected and patched ranges remain unchanged (`<=2.8.3` affected, `>=2.8.4` patched), so S001's primary recommendation remains merge after normal review.

## Evolving coverage dimensions

The entries below are discovery prompts. They are neither mandatory categories nor hard limits. “Covered” means only that the named case exposed the condition at its documented depth.

| Dimension | Starting contrasts to consider | Covered by | Remaining uncertainty |
|---|---|---|---|
| Update scale and lifecycle | patch, minor, major, pre-release, yanked, replacement, superseded proposal | S001: minor update crossing 2.7–2.8.4; S002: 0.x minor API-removal line and predecessor superseded by successor | major, pre-release, yanked, package replacement |
| Dependency relationship | direct, transitive, optional, runtime, development, test, build | S001: transitive documentation/tooling; S002: direct declaration, test-framework functional use, production-image installation | direct application-runtime, optional, build/native, marker-specific |
| Change shape | manifest-only, lockfile-only, source/config changes, multiple packages | S001: one-package lockfile-only; S002: one-line manifest-only pin | source/config changes, multi-package changes |
| Upstream information | complete, missing, fragmented, ambiguous, contradictory, migrated source | S001: complete changelog/tags/PyPI/advisories; S002: complete tagged changelog and framework source | missing, fragmented, contradictory, migrated |
| Repository relevance | directly affected, indirectly affected, apparently unaffected, unresolved | S001: indirect docs relevance; S002: direct test-path relevance through framework adapter, no observed app import | direct application-runtime and apparently irrelevant cases |
| Compatibility change | interpreter, operating system, architecture, build tool, API, behavior | S001: Python floor found irrelevant; S002: removed HTTPX API with Starlette compatibility threshold | OS, architecture, build-tool, data/behavior changes |
| CI and test evidence | passing, failing, unavailable, stale, flaky, skipped, unrelated failure | S001: relevant CI passed; S002: Docker install/build passed, relevant Python tests skipped, logs expired | actual failing, stale, flaky, unrelated failures |
| CI-to-responsibility alignment | owning path exercised, adjacent path only, no relevant path, unclear | S001: docs dependency path exercised; S002: adjacent install/build path exercised while TestClient path was not | reusable/dynamic workflows, partial test coverage, misleading combined status |
| Workflow trigger coverage | changed path triggers relevant workflow, excluded path, manual-only, unknown | S002: `requirements.txt` excluded from Python-test workflow path filters | complex filters, generated paths, reusable workflow conditions |
| Executed-command coverage | install, build, lint, unit test, integration test, deployment, unknown | S001: relevant docs build; S002: install/build only, while defined Ruff/pytest commands did not run | indirect scripts, matrix branches, conditionally skipped steps |
| Environment identity | locked, resolver output captured, partially known, drifting/unpinned, expired | S001: lockfile identity; S002: unpinned FastAPI resolution and expired build logs | private indexes, constraints, cache effects, platform-specific resolution |
| Security context | ordinary maintenance, known advisory, incomplete disclosure, disputed relevance | S001: two reviewed advisories with unresolved exploitability; S002: ordinary maintenance with no security claim | advisory conflict, incomplete disclosure, active exploitation |
| Security trigger identity | explicitly labelled, plausible but unresolved, unknown, contradicted, not indicated | S001: plausible but unresolved; S002: not indicated | explicit, unknown, contradicted cases |
| Package implementation | pure Python, native/compiled, generated artifacts, platform-specific wheels | S001 and S002: pure Python | native/compiled, generated, platform-specific |
| Evidence agreement | agreement, partial agreement, contradiction, no corroboration | S001: material agreement with later timing correction; S002: sources agree but exact environment/test proof is missing | true source contradiction and no-corroboration cases |
| Decision shape | normal review, targeted checks, investigate/block, defer, abstain, new outcome | S001: normal review; S002: primary `run targeted checks`, variants reach normal review or investigate/block | real primary block, defer, abstain cases |
| User interaction | automatic investigation, clarification, authorization, manual follow-up | S001: no clarification; S002: maintainer must authorize/run exact-head tests | clarification and privileged-action cases |
| Reproducibility | stable historical, moving PR, unavailable artifact, changed upstream state | S001: stable base/head with some unavailable operation evidence; S002: stable PR but expired logs and drifting unpinned resolution | moving open PR, disappearing upstream artifact, private source |
| Execution-record quality | progressive live record, retrospective reconstruction, incomplete outputs, exact replay | S001: retrospective reconstruction with explicit gaps; S002: progressive primary CASE record from selection boundary onward | exact raw-artifact bundle and multi-session handoff |
| Investigation value | extensive context useful, simple evidence sufficient, extra work adds little | S001: graph/advisory/CI join changed decision; S002: adapter/constraint/workflow join narrowed risk, then static work stopped at missing test | genuinely trivial case and high-cost low-value investigation |
| Invocation model | PR locator, exact identity supplied, event payload, manual evidence bundle | S001 and S002: PR locator sufficient to acquire/freeze identity | webhook payload, offline replay, inaccessible/private PR |
| Dependency-path evidence | declared direct, lock-derived transitive, conditional markers, framework adapter, unresolved | S001: lock-derived multi-hop docs path; S002: direct manifest → FastAPI TestClient → Starlette TestClient → HTTPX Client | extras, markers, multiple resolutions, dynamic plugin paths |
| Exploitability/effect evidence | confirmed exposure, confirmed non-exposure, limited static evidence, behavior test, unavailable production context | S001: limited exploitability evidence; S002: likely compatibility from source threshold but behavior test missing | confirmed positive/negative production effect |
| Update supersession | active PR, superseded predecessor, recreated/rebased successor, competing updates | S002: PR #17 explicitly superseded by #20 | rebases, parallel update bots, partial manual edits |
| Evidence retention | durable, summarized, expired, deleted, private | S001: retained sources with one unavailable run; S002: Docker logs expired with HTTP 410 | deleted artifacts, private logs, retention-policy handling |

## Cross-case questions to monitor

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
- How should changed-file filters, job conditions, and commands be represented as evidence?
- What tested-environment identity is required before passing CI can support a compatibility finding?
- When may a PR URL alone serve as invocation, and when is an offline evidence bundle required?
- How should inferred trigger context be represented without turning it into fact?
- Which dependency graph representations handle groups, extras, markers, adapters, and multiple resolutions accurately?
- Which raw outputs need durable preservation, and which may be summarized without losing auditability?
- How should later source verification correct a scenario without silently rewriting its historical execution?
- How should superseded dependency-update PRs be detected and linked?
- How should a failing check be attributed among update-caused, pre-existing, flaky, environmental, and unrelated causes?

## Next-case selection record

| From scenario | Contrasting case needed | Reason | Priority or dependency |
|---|---|---|---|
| S001 | Direct dependency with API/behavior change and misleading or conflicting CI | Tests source-level relevance, targeted-check sufficiency, and CI authority | Covered by S002 |
| S001 | Missing or fragmented upstream release information | Tests investigation without complete changelog | Later contrast |
| S001 | Native or platform-specific dependency update | Tests artifact/platform/architecture branches | Later contrast |
| S001 retrofit | Progressive live execution record | Tests new operation-lineage rule without excessive ceremony | Covered by S002 |
| S002 | Actual failing test workflow with ambiguous cause | Requires attribution among update-caused, pre-existing, flaky, environmental, and unrelated failure; exercises investigate/block or defer as a primary outcome | Highest-value next contrast |
| S002 | Direct application-runtime use instead of framework test adapter | Tests source-level behavior impact and production relevance | High-value later contrast |
| S002 | Locked environment with retained resolver/test artifacts | Contrasts drifting unpinned resolution and expired evidence | Useful later control case |

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
