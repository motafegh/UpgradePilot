# Product Simulation Scenario Coverage

**Status:** Active evolving discovery and comparative-evidence record  
**Local plan:** [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md)  
**Artifact specification:** [`RUNTIME_ARTIFACT_SPECIFICATION.md`](RUNTIME_ARTIFACT_SPECIFICATION.md)  
**Baseline:** [`TRANSPARENT_BASELINE_SPECIFICATION.md`](TRANSPARENT_BASELINE_SPECIFICATION.md)

## Purpose

Track whether real scenarios are materially different enough to expose:

- the actual UpgradePilot operating model;
- the durable runtime artifact lifecycle;
- the strengths and failures of the transparent baseline;
- stable, conditional, contradicted, and unresolved product responsibilities;
- review, evaluation, and ownership status;
- the next highest-value scenario.

This file is not a frozen taxonomy, production schema, frequency claim, proof of
automation reliability, or substitute for scenario evidence.

## Selection rule

Use materially contrasting real cases. Do not stop merely because a minimum case
count exists and do not continue merely to increase the count.

A useful next case should expose at least one insufficiently tested actor, source,
trust boundary, artifact transition, evidence failure, repository relevance
pattern, decision, baseline condition, replay behavior, review problem, or
automation limitation.

## Scenario register

| Scenario | Repository/update | Narrative status | Artifact-bundle status | Baseline status | Review/evaluation status | Manual outcome | Most important insight |
|---|---|---|---|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md) | `pydantic/pydantic` — Soup Sieve 2.6 → 2.8.4 | Complete unified retrospective record with correction | Parallel retrofit in progress; historical raw outputs/timestamps partly unrecoverable | Retrospective v0.1 pending | Factual correction integrated; Ali capability not independently established; external safety not confirmed | Merge after normal review | Dependency graph, target usage, advisory meaning, exact CI relevance, and operation lineage must be joined |
| [`S002`](scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | `Aidan-Wallace/kubernetes-dashboard-token-api` — HTTPX 0.27.2 → 0.28.1 | Rechecked complete retrospective narrative | **Complete retrospective reconstruction:** 39-file bundle, 20 evidence/raw records, 10 operation events, and validation passed | **Complete:** v0.1 reached the same action with weaker reasons, miscalibrated certainty, and less actionable follow-up | AI factual recheck complete; Ali review pending; exact behavior not confirmed; historical merge is action only | Run targeted checks; merge only after exact-head Python checks pass | CI authority requires trigger, command, responsibility, revision, and environment identity |

S002 is artifact-lifecycle complete as a retrospective reconstruction. It does
not claim that its JSON/JSONL artifacts existed during the original
investigation. S001 remains incomplete until its parallel retrofit is validated.

## Current correction and reconstruction notes

### S001

- official advisory publication dates: June 1, 2026;
- exact Dependabot trigger: unresolved;
- affected/patched ranges unchanged;
- primary recommendation unchanged;
- operation history is a best-effort retrospective reconstruction;
- unavailable exact raw responses and timestamps must remain explicit.

### S002

- run ID: `s002-retrofit-2026-07-22-r1`;
- execution mode: `retrospective_artifact_reconstruction`;
- candidate screening occurred before formal identity freeze;
- historical Docker logs returned HTTP 410 and remain an expired evidence item;
- exact historical FastAPI/Starlette resolution is unrecoverable publicly;
- likely compatibility is not behavioral proof;
- the Python workflow was path-filtered and did not run;
- finding `F0` preserves the earlier possible-hard-break concern as superseded;
- decision `decision-s002-v1` remains `run_targeted_checks`;
- Ali review and exact-head behavioral checks remain pending;
- the artifact bundle passed syntax, identity, reference, lineage, inventory, and
  report-consistency validation.

## Product coverage dimensions

“Covered” means only that a case exposed the condition at its documented depth.

| Dimension | Covered by | Remaining uncertainty |
|---|---|---|
| Update lifecycle | S001 minor multi-release; S002 0.x API-removal line and superseded predecessor | major, pre-release, yanked, replacement, competing PRs |
| Dependency relationship | S001 transitive docs tooling; S002 direct declaration, framework-test use, production installation | direct application runtime, optional, build/native, markers/extras |
| Change shape | S001 lockfile-only; S002 manifest-only | source/config changes, multi-package updates |
| Upstream information | S001 complete sources/advisories; S002 complete tagged framework sources | missing, fragmented, contradictory, migrated |
| Repository relevance | S001 indirect docs path; S002 adapter-mediated test path | direct runtime and genuinely irrelevant cases |
| Compatibility | S001 irrelevant Python-floor change; S002 removed API and framework threshold | OS, architecture, compiler, build-tool, data/behavior changes |
| CI/test evidence | S001 relevant passing CI; S002 install/build pass, relevant tests skipped, logs expired | actual failing, flaky, stale, unrelated failure |
| CI trigger coverage | S002 changed manifest excluded from Python workflow | complex conditions, reusable workflows, generated paths |
| Executed-command coverage | S001 docs build; S002 install/build without tests | matrices, scripts, conditional steps, deployment checks |
| Environment identity | S001 lockfile identity; S002 unpinned drifting resolution | private indexes, caches, platform resolution, constraints |
| Security | S001 reviewed advisories with unresolved exploitability; S002 ordinary maintenance | conflicting/incomplete disclosure, active exploitation |
| Package implementation | S001/S002 pure Python | native/compiled, generated, platform-specific artifacts |
| Evidence agreement | S001 correction after later verification; S002 agreement with missing dynamic proof | direct source contradiction and no-corroboration |
| Decision shape | S001 normal review; S002 targeted checks | primary block, defer, abstain, new action |
| User interaction | S001 no clarification; S002 maintainer-owned targeted check | clarification, credential/paid authorization, policy conflict |
| Reproducibility | stable historical cases with different missing evidence | moving open PR, deleted source, private evidence |
| Failure attribution | not covered | update-caused, pre-existing, environmental, flaky, unrelated |
| Invocation | PR locator sufficient in both cases | webhook/event, offline bundle, inaccessible/private PR |
| Dependency path | S001 lock-derived chain; S002 framework adapter path | markers, extras, multiple resolutions, plugins |
| Effect/exploitability | S001 limited static exposure; S002 likely compatibility without test | confirmed positive/negative behavior |
| Evidence retention | S001 partial historical gaps; S002 expired logs preserved as first-class state | deleted artifacts, private logs, long-term replay policy |

## Artifact-lifecycle coverage dimensions

| Dimension | S001 | S002 | Remaining uncertainty |
|---|---|---|---|
| Narrative record | Unified retrospective complete | Rechecked complete retrospective record | multi-session very large case |
| Run manifest | Parallel retrofit pending | Complete; 39-entry inventory and historical-gap disclosure | rerun and multi-run manifests |
| Invocation artifact | Parallel retrofit pending | Complete retrospective locator boundary | event payload and malformed invocation |
| Frozen identity artifact | Parallel retrofit pending | Complete exact base/head, versions, lifecycle, supersession | moving/rebased identity comparison |
| Operation events | Retrospective trace embedded; JSONL pending | 10 ordered JSONL operations; timing/progression limits explicit | live append and checkpoint discipline |
| Evidence-item artifacts | Markdown inventory; retrofit pending | 20 JSONL evidence records with bounded raw captures | large evidence, conflicts, replacement chains |
| Claims/interpretations | Narrative chains; retrofit pending | 9 transformation records with authority and limitations | automated/human mixed transformations |
| Findings artifact | Narrative/YAML; retrofit pending | Versioned `F0`–`F8`, including superseded `F0` | multi-run contradiction and withdrawal |
| Baseline result | Retrospective v0.1 pending | Complete; same action but materially weaker baseline | wrong-action, sufficient, and unresolved cases |
| Decision artifact | Retrofit pending | `decision-s002-v1` with reasons, checks, and transitions | disputed/superseded decision revisions |
| Machine report | Retrofit pending | Separate machine-facing report | external consumer/schema validation |
| Human report | Embedded; separate report pending | Separate maintainer-facing report | maintainer usability review |
| Follow-up state | Retrofit pending | Persistent pass/fail/unavailable/rebase transitions | real user action and rerun history |
| Review/ownership | Retrofit pending | Separate record; AI recheck complete, Ali pending | independent Ali execution and review |
| Raw preservation | Partial historical gaps | 20 bounded captures; expired log preserved explicitly | hashes/large payload policy over time |
| Check artifacts | Public CI references | CK01–CK04 performed; target Ruff/pytest explicitly not run | isolated dynamic execution outputs |
| Bundle validation | Pending | Passed JSON/JSONL, IDs, references, identity, lineage, inventory, reports | reusable automated validator |
| Replay/supersession | correction and reconstruction | predecessor PR, finding supersession, result transitions, new-run triggers | actual rerun comparison and partial recovery |

## Baseline and thesis evidence

The thesis now has **one materialized comparative case**, but is not validated
across the scenario set while S001 and major contrasting classes remain pending.

| Scenario | Comparison question | Current status |
|---|---|---|
| S001 | Would passing CI + minor/transitive + security/fix keywords reach the same action but with weaker authority and exploitability calibration? | Retrospective v0.1 comparison pending |
| S002 | Would passing CI + minor/direct + removal keywords request targeted checks without identifying the TestClient path and misleading CI scope? | **Completed:** same action; baseline had weaker reasons, miscalibrated certainty, and less actionable checks |

S002 does not prove a baseline wrong-action case. It shows that matching the
broad action is insufficient when the reasons, evidence authority, exact check,
and state transitions are materially weaker.

Future coverage must include:

- a case where the baseline selects the wrong action;
- a case where the baseline has the same action but materially weaker reasons;
- a case where the baseline is sufficient and full investigation adds little;
- a case where comparison remains unresolved due to label/evidence limits.

## Cross-case stability register

| Observation | Status after current evidence | Reason |
|---|---|---|
| A public PR locator can start acquisition | Repeated stable candidate | Both cases discovered and froze identity from a public locator |
| Exact repository/revision identity is mandatory before joining evidence | Repeated stable candidate | Both cases depend on historical base/head boundaries |
| Dependency role is one simple enum | Contradicted assumption | S002 separates declaration, functional use, and installation |
| Dependency path is first-class evidence | Repeated stable candidate | Lock graph in S001; adapter path in S002 |
| CI conclusion is globally authoritative | Contradicted assumption | S002 green Docker status did not cover TestClient behavior |
| CI requires trigger and command interpretation | Repeated stable candidate | S001 relevant docs path; S002 excluded Python workflow |
| Advisory analysis is universal | Conditional responsibility | Material in S001, unnecessary in S002 |
| Dynamic execution is always required | Contradicted as universal | Not needed for S001; decision-changing follow-up for S002 |
| Missing evidence can create a specific action | Repeated stable candidate | Missing exposure calibrated S001; missing tests produced S002 checks |
| Merge state proves correctness | Contradicted assumption | Both cases treat merge as history only |
| One CASE file is a complete runtime simulation | Contradicted assumption | S002 required 39 separate runtime/narrative artifacts |
| Manual success proves automation feasibility | Unresolved/unsupported | S002 materializes records but does not validate automated production |
| Full investigation always changes the broad action | Contradicted by S002 | Baseline and full investigation both requested checks |
| Full investigation can add value without changing action | Supported by one case | S002 improved cause, authority, check specificity, and transitions |
| Full investigation always beats the baseline | Unresolved | A deliberately simple baseline-sufficient case remains required |

## Automation-feasibility coverage

| Responsibility | Current evidence | Status |
|---|---|---|
| Freeze PR identity | Repeated connector-based success | Deterministic automation appears credible |
| Parse simple version transition | Repeated simple cases only | Deterministic candidate; broader variation untested |
| Resolve dependency paths | lock and framework-adapter examples | Tool-assisted; ecosystem variation untested |
| Acquire upstream information | Complete public sources in both | Deterministic retrieval candidate; missing-source behavior untested |
| Interpret target relevance | Substantial AI/manual reasoning | Human/model-assisted; automation unvalidated |
| Interpret CI authority | Workflow/run inspection useful | Partial deterministic structure; complex workflows untested |
| Attribute failing CI | No real case | Not yet tested |
| Construct bounded decision | Manual evidence joining plus S002 structured result | Requires rubric and broader cross-case evaluation |
| Render reports | S002 separate machine/human artifacts | Deterministic rendering appears plausible after contracts stabilize |
| Persist/replay artifacts | First complete manual S002 bundle | Logical need demonstrated; implementation and replay behavior untested |
| Validate bundle consistency | One custom S002 validation pass | Credible deterministic responsibility; reusable implementation unselected |

## Cross-case questions to monitor

- What is the smallest credible invocation input?
- Which identities must be supplied, discovered, frozen, and versioned?
- What are the minimum durable artifacts for a resumable run?
- Which operation/evidence records should be append-only?
- Which raw outputs need full capture, bounded capture, hash, or reference only?
- How should expired or inaccessible evidence affect replay and decisions?
- Which evidence may affect a recommendation directly?
- Which claims need independent corroboration?
- How should findings and decisions be superseded without silent replacement?
- When does a new head, test run, or dependency resolution create a new run?
- What CI trigger, command, environment, and responsibility evidence is required?
- How should failing checks be attributed?
- Which baseline failures support the main thesis?
- When is the baseline sufficient?
- Which methods are manually useful but not credibly automatable?
- What must Ali independently explain, verify, or perform before capability claims?

## Next-case and current-work record

| Source | Required work/contrast | Reason | Priority |
|---|---|---|---|
| Parallel S001 work | Complete and validate S001 retrospective bundle | Test correction, unavailable raw data, and cross-case bundle consistency | Current |
| S002 completed retrofit | Compare S001/S002 artifacts and identify any model defect | Prevent one-case artifact overfitting | After S001 |
| S002 | Actual failing test workflow with ambiguous cause | Test failure attribution and primary investigate/block behavior | S003 after retrofits/review |
| Thesis | Deliberately simple case where baseline is sufficient | Prevent investigation overreach and measure cost | High-value early case |
| Evidence model | Missing/fragmented/contradictory upstream data | Test degradation, corroboration, defer, and abstain | High-value later case |
| Artifact/platform model | Native or platform-specific dependency | Test wheel/source/platform/toolchain records | Later contrast |

## Coverage interpretation

A marked dimension establishes only that one case exposed it at the recorded
depth. It does not establish complete understanding, product implementation,
automation reliability, representative frequency, decision correctness, target
safety, or Ali-owned capability.

Use validated scenario narratives, runtime bundles, baseline comparisons,
reviews, and synthesis—not coverage marks alone—to decide when implementation may
resume.
