# Product Simulation Scenario Coverage

**Status:** Active evolving discovery and comparative-evidence record  
**Local plan:** [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md)  
**Artifact specification:** [`RUNTIME_ARTIFACT_SPECIFICATION.md`](RUNTIME_ARTIFACT_SPECIFICATION.md)  
**Baseline:** [`TRANSPARENT_BASELINE_SPECIFICATION.md`](TRANSPARENT_BASELINE_SPECIFICATION.md)  
**S001/S002 review:** [`S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`](S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md)  
**Current synthesis:** [`S003_POST_CASE_SYNTHESIS.md`](S003_POST_CASE_SYNTHESIS.md)

## Purpose

Track whether contrasting real cases expose the operating model, durable artifact
lifecycle, baseline strengths/failures, automation boundaries, review states, and
the next highest-value case.

This file is not a production schema, frequency claim, case-count completion
claim, or substitute for scenario evidence.

## Scenario register

| Scenario | Update and contrast | Execution/artifact status | Baseline comparison | Current decision | Review/evaluation |
|---|---|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md) | Soup Sieve 2.6 → 2.8.4; transitive docs tooling; advisory remediation; relevant green docs CI | Complete honest retrospective reconstruction; structural validation passed | Same action; full investigation improved dependency path, advisory authority, exploitability calibration, CI relevance, and auditability | Merge after normal maintainer review | Factual correction complete; Ali final acceptance pending; no independent behavior confirmation |
| [`S002`](scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | HTTPX 0.27.2 → 0.28.1; direct declaration, adapter-mediated test use, production-image installation; relevant tests skipped | Complete honest retrospective reconstruction; structural validation passed | Same action; full investigation identified TestClient path, compatibility threshold, skipped workflow, exact checks, and transitions | Run targeted checks; merge only after exact-head Python checks under captured resolution | AI factual recheck complete; Ali review pending; exact behavior not confirmed |
| [`S003`](scenarios/S003-event-handler-loader-typescript-5.9.3-to-7.0.2/README.md) | TypeScript 5.9.3 → 7.0.2; direct tooling dependency; actual failing install; same-base comparison; peer conflict | **Complete prospective run** with separate screening, freeze, failure, attribution, decision/report, and validation checkpoints | Same broad action; full investigation identified `npm ci`, peer-range mechanism, comparison evidence, recovery, and decision dimensions | Block current proposal as-is; evaluate coordinated compatible toolchain in a new run | AI factual review complete; Ali review pending; public evidence strongly supports attribution; controlled local reproduction unavailable |

## Product coverage

| Dimension | Covered evidence | Remaining uncertainty |
|---|---|---|
| Invocation | Public PR locator sufficient in S001–S003 | webhook/event payload, offline bundle, malformed/private invocation |
| Identity | Exact base/head/change freeze essential in all three | moving/rebased open PR comparison, multi-PR replacement |
| Update shape | lockfile-only, manifest-only, major toolchain proposal | source/config change, multi-dependency coordinated update |
| Dependency relationship | transitive docs path; direct/framework-mediated/install; direct toolchain with peer support | optional/extras/markers, plugins, native/runtime platform paths |
| Dependency path | lock graph, adapter chain, peer/support boundary | multiple resolutions, workspace/monorepo paths, generated dependency sets |
| Upstream information | advisories, release notes, tagged framework source, lock metadata | missing/fragmented/contradictory upstream sources |
| Compatibility | Python floor, removed API threshold, semantic-version peer conflict | OS/architecture/compiler/native/data/behavior compatibility |
| CI authority | relevant passing docs CI; partial green CI; actual failing install before lint | matrices, reusable workflows, flaky/stale/unrelated failures |
| Environment identity | lock identity, unpinned resolver gap, public runner/image comparison | caches, private indexes, exact npm/runner reproduction, platform matrices |
| Failure attribution | S003 update-caused, strongly supported with limits | pre-existing, unrelated, flaky, environmental, mixed and unresolved real cases |
| Security | advisory remediation/exploitability calibration in S001 | active exploitation, conflicting/incomplete disclosure |
| Decision shape | normal review, targeted checks, block current proposal | defer, abstain, clarification, accepted update but PR blocked |
| User interaction | maintainer-owned checks and strategy choice | credentials, policy conflicts, explicit clarification loops |
| Reproducibility | retrospective reconstruction and first prospective checkpoints | real rerun comparison, partial recovery, long-term replay |
| Evidence retention | partial historical gaps, expired logs, missing diagnostic tail, failed local acquisition | large/secret/private/deleted artifacts and retention policy |

## Artifact-lifecycle coverage

| Responsibility | S001 | S002 | S003 | Status after three cases |
|---|---|---|---|---|
| Narrative and manifest | retrospective complete | retrospective complete | prospective complete | repeated stable candidate |
| Invocation and frozen identity | reconstructed | reconstructed | created before deep investigation | repeated stable candidate |
| Operation events | reconstructed 22 events | reconstructed 10 events | 12 prospective operations | append-oriented stable candidate |
| Evidence records | 26 | 20 | 15 | stable logical responsibility; record granularity provisional |
| Claims/interpretations | 16 | 9 | 8 | stable transformation boundary; physical split unresolved |
| Findings | 12 | 9 | 7 | stable current projection; append history unresolved |
| Baseline result | complete | complete | prospectively frozen before investigation | universal simulation responsibility |
| Decision | normal review | targeted checks | broad plus trial dependency/PR dimensions | stable responsibility; dimensional split one-case observation |
| Machine/human reports | separate | separate | separate | repeated stable candidate |
| Follow-up and transitions | complete | complete | coordinated repair/rerun/supersession | repeated stable candidate |
| Review/ownership | separate states | separate states | separate states | repeated stable candidate |
| Raw/check preservation | bounded historical | bounded plus expired state | bounded execution/source captures and failed method state | repeated stable policy |
| Structural validation | scenario validator | isolated validation result | retained common profile, zero errors | deterministic stable candidate |
| Prospective checkpoint history | not applicable | not applicable | demonstrated across five checkpoints | first evidence; stable simulation responsibility candidate |
| `CHECK_EXECUTIONS.jsonl` | not needed | implicit execution evidence | four comparable execution records | conditional stable candidate |
| `FAILURE_ATTRIBUTION.json` | not needed | no actual failing causal problem | competing causes and selected classification | conditional stable candidate |

Artifact, operation, evidence, transformation, finding, and file counts are not
quality metrics.

## Cross-case stability register

### Repeated stable candidates

- public locator can begin acquisition;
- invocation remains separate from discovered identity;
- exact repository/base/head/change identity is mandatory;
- dependency path is first-class evidence;
- dependency role is multi-axis;
- peer/support relationships may be part of dependency path;
- CI authority requires trigger, job, step, command, responsibility, revision,
  environment, and retention context;
- missing, expired, inaccessible, and failed-method evidence can create actions;
- findings and decisions require supersession rather than silent replacement;
- machine and human reports are projections, not truth stores;
- merge history is action, not correctness evidence;
- structural validation is credible deterministic work;
- AI-produced completion does not establish Ali-owned capability.

### Conditional responsibilities

- advisory and exploitability analysis;
- framework/adapter compatibility;
- package identity/hash verification;
- repeated execution comparison;
- causal failure attribution;
- semantic-version and peer-range analysis;
- dynamic execution;
- private or credentialed acquisition;
- platform/native/compiler/toolchain analysis;
- post-merge publication/deployment checks.

### Contradicted or narrowed assumptions

- one dependency-role enum is adequate;
- direct imports are the only meaningful relevance path;
- green or red workflow color has global authority;
- workflow name identifies the failed responsibility;
- advisory presence proves exploitability;
- one comparison execution proves identical-environment causality;
- peer-suppression flags prove compatibility;
- every case requires dynamic execution;
- one `CASE.md` represents the runtime;
- full investigation must change the broad action to create value;
- more artifacts mean higher quality;
- manual success proves automation feasibility.

## Baseline and thesis evidence

| Scenario | Baseline/full relationship | Thesis class |
|---|---|---|
| S001 | same action; full result improved authority, calibration, auditability and actionability | same-action/stronger-support |
| S002 | same action; full result identified exact repository path, missing test authority and targeted checks | same-action/stronger-support |
| S003 | same broad action; full result identified failed command, peer conflict, comparison evidence, repair and decision dimensions | same-action/stronger-support |

The thesis has three examples of one class, not representative validation.

Still required:

- baseline-sufficient control;
- baseline wrong action;
- unresolved comparison;
- possible full-investigation overreach or excessive cost.

## Automation-feasibility register

| Responsibility | Current evidence | Discovery status |
|---|---|---|
| Freeze PR/change identity | repeated structured retrieval | deterministic automation credible |
| Parse version mutation | three simple ecosystems/shapes | deterministic candidate; broader syntax untested |
| Retrieve workflow/run/job/step | S002/S003 public Actions data | deterministic where public/retained |
| Parse commands and conclusions | S003 exact install/lint boundary | deterministic candidate |
| Extract package constraints | lock/source metadata across cases | parser/tool-assisted candidate |
| Compare semantic versions/ranges | S001 Python floor and S003 peer range | deterministic candidate with ecosystem variation |
| Resolve dependency paths | lock, adapter and peer examples | tool-assisted; generality untested |
| Assess CI responsibility/authority | useful in all cases | mixed deterministic structure plus interpretation |
| Select comparable executions | S003 one strong adjacent comparison | interpretation required; more cases needed |
| Attribute failure | one update-caused case | tool-assisted/human-model judgment; not generalized |
| Construct proportionate action | all cases | interpretive and human-reviewed |
| Render reports | three structured examples | deterministic rendering plausible |
| Validate artifacts | three passed bundles | deterministic stable candidate |
| Persist/replay | retrospective plus one prospective run | logical need demonstrated; implementation unselected |

## Current next-case record

| Priority | Case target | Primary uncertainty |
|---|---|---|
| **S004 next** | deliberately simple baseline-sufficient dependency update | Can the system stop early and avoid unnecessary investigation? |
| High after S004 | baseline wrong-action case | Does joined evidence change the broad action? |
| High after S004 | failing CI with divergent dependency/PR decisions | Can an unrelated or pre-existing failure block the PR while the update remains acceptable? |
| Later | missing/fragmented/contradictory upstream evidence | corroboration, defer, abstain and clarification |
| Later | native/platform-specific dependency | artifacts, wheel/source/toolchain/platform state |

## Current gate

M2-S03 remains paused.

1. Ali reviews S003 and [`S003_POST_CASE_SYNTHESIS.md`](S003_POST_CASE_SYNTHESIS.md).
2. Correct only evidence-backed local-model defects.
3. Select and execute S004 prospectively as the baseline-sufficient control.
4. Do not treat scenario count alone as implementation authorization.

Coverage marks do not establish complete understanding, production behavior,
automation reliability, decision correctness, target safety, representative
frequency, or Ali-owned capability.
