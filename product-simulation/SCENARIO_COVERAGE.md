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

This file is not:

- a frozen taxonomy;
- a fixed ten-case list;
- a production schema;
- a claim of representative frequency;
- proof that manual success is automatable;
- a substitute for scenario evidence.

## Selection rule

Use materially contrasting real cases. Do not stop merely because a minimum case
count exists and do not continue merely to increase the count.

A useful next case should expose at least one new or insufficiently tested:

- actor, source, or trust boundary;
- invocation or identity requirement;
- runtime or artifact state transition;
- evidence type, failure, or preservation need;
- repository-specific relevance pattern;
- decision or user interaction;
- baseline failure or sufficiency condition;
- replay, supersession, or partial-run behavior;
- review/evaluation problem;
- automation limitation.

## Scenario register

| Scenario | Repository/update | Narrative status | Artifact-bundle status | Baseline status | Review/evaluation status | Manual outcome | Most important insight |
|---|---|---|---|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md) | `pydantic/pydantic` — Soup Sieve 2.6 → 2.8.4 | Complete unified retrospective record with correction | Retrofit required; historical raw outputs/timestamps partly unrecoverable | Not yet materialized under v0.1 | Factual correction integrated; Ali capability not independently established; external safety not confirmed | Merge after normal review | Dependency graph, target usage, advisory meaning, exact CI relevance, and operation lineage must be joined |
| [`S002`](scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | `Aidan-Wallace/kubernetes-dashboard-token-api` — HTTPX 0.27.2 → 0.28.1 | Complete progressive-structured narrative | Retrofit required; fullest recoverable bundle plus durable-progression limitation | Not yet materialized under v0.1 | Ali review pending; exact behavior not confirmed; historical merge is action only | Run targeted checks; merge only after exact-head Python checks pass | CI authority requires trigger, command, responsibility, revision, and environment identity |

Neither scenario is artifact-lifecycle complete until its bundle is created and
validated. Retrofit must be labeled retrospective and must not invent historical
raw data.

## Current correction and reconstruction notes

### S001

- official advisory publication dates: June 1, 2026;
- exact Dependabot trigger: unresolved;
- affected/patched ranges unchanged;
- primary recommendation unchanged;
- operation history is a best-effort retrospective reconstruction;
- unavailable exact raw responses and timestamps must remain explicit.

### S002

- candidate screening occurred before formal identity freeze;
- historical Docker logs returned HTTP 410;
- exact FastAPI/Starlette resolution is missing;
- likely compatibility is not behavioral proof;
- the Python workflow was path-filtered and did not run;
- the narrative has progressive structure, but the retrofit must record the
  limits of durable checkpoint evidence.

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
| Evidence retention | S001 partial historical gaps; S002 expired logs | deleted artifacts, private logs, long-term replay policy |

## Artifact-lifecycle coverage dimensions

| Dimension | S001 | S002 | Remaining uncertainty |
|---|---|---|---|
| Narrative record | Unified retrospective complete | Progressive-structured complete | multi-session very large case |
| Run manifest | Missing; retrofit required | Missing; retrofit required | rerun and multi-run manifests |
| Invocation artifact | Narrative only | Narrative only | event payload and malformed invocation |
| Frozen identity artifact | Narrative only | Narrative only | moving/rebased identity comparison |
| Progressive operation events | Retrospective trace embedded | Structured steps embedded | live JSONL append and checkpoint discipline |
| Evidence-item artifacts | Markdown inventory | Markdown inventory | JSONL evolution, large raw evidence, conflict records |
| Claims/interpretations | Narrative chains | Narrative chains | automated/human mixed transformations and supersession |
| Findings artifact | Narrative/YAML | Narrative/YAML | versioned finding updates and contradiction |
| Baseline result | Missing | Missing | prospective baseline execution and simple sufficient case |
| Decision artifact | Illustrative YAML only | Illustrative YAML only | versioned decisions, supersession, disputed review |
| Machine report | Illustrative in CASE | Illustrative in CASE | external consumer validation and representation version |
| Human report | Embedded in CASE | Embedded in CASE | separate user-facing output and usability review |
| Follow-up state | Narrative flow | Conditional narrative flow | persistent action history and rerun state |
| Review/ownership | Narrative attribution | Narrative attribution | separate factual/Ali/external/capability state |
| Raw preservation | References and partial retained outputs | references; expired log failure | bounded snapshots, hashes, large payload policy |
| Check artifacts | Public CI references only | public CI references; proposed check unrun | isolated dynamic execution and stored outputs |
| Bundle validation | Not performed | Not performed | parsers, ID/reference validation, manifest consistency |
| Replay/supersession | correction and historical reconstruction | predecessor PR and future test transition | complete rerun comparison and partial recovery |

## Baseline and thesis evidence

The project thesis remains **qualitatively supported but not comparatively
validated** until baseline artifacts exist.

| Scenario | Expected baseline comparison question | Current status |
|---|---|---|
| S001 | Would passing CI + minor/transitive + security/fix keywords reach the same action but with weaker authority and exploitability calibration? | Retrospective v0.1 comparison required |
| S002 | Would passing CI + minor/direct + removal keyword reach targeted checks without discovering the exact TestClient check and misleading CI scope? | Retrospective v0.1 comparison required |

Future coverage must include:

- a case where the baseline selects the wrong action;
- a case where the baseline has the same action but materially weaker reasons;
- a case where the baseline is sufficient and full investigation adds little;
- a case where comparison remains unresolved due to label/evidence limits.

## Cross-case stability register

| Observation | Status after S001/S002 | Reason |
|---|---|---|
| A public PR locator can start acquisition | Repeated stable candidate | Both cases discovered and froze identity from a public locator |
| Exact repository/revision identity is mandatory before joining evidence | Repeated stable candidate | Both cases depend on historical base/head boundaries |
| Dependency role is one simple enum | Contradicted assumption | S002 separates declaration, functional use, and installation |
| Dependency path is first-class evidence | Repeated stable candidate | Lock graph in S001; adapter path in S002 |
| CI conclusion is globally authoritative | Contradicted assumption | S002 green Docker status did not cover TestClient behavior |
| CI requires trigger and command interpretation | Repeated stable candidate | S001 relevant docs path; S002 excluded Python workflow |
| Advisory analysis is universal | Conditional responsibility | Material in S001, unnecessary in S002 |
| Dynamic execution is always required | Contradicted as universal | Not needed for S001; decision-changing for S002 follow-up |
| Missing evidence can create a specific action | Repeated stable candidate | Missing exposure in S001 calibrated claims; missing tests in S002 created targeted check |
| Merge state proves correctness | Contradicted assumption | Both cases treat merge as history only |
| One CASE file is a complete runtime simulation | Contradicted assumption | Machine-state and artifact lifecycle were not materialized |
| Manual success proves automation feasibility | Unresolved/unsupported | No artifact-level automation evaluation yet |
| Full investigation always beats the simple baseline | Unresolved | No baseline artifacts yet; future simple control case required |

## Automation-feasibility coverage

| Responsibility | Current evidence | Status |
|---|---|---|
| Freeze PR identity | Repeated connector-based success | Deterministic automation appears credible |
| Parse simple version transition | Repeated simple cases only | Deterministic candidate; broader variation untested |
| Resolve dependency paths | uv lock and framework adapter examples | Tool-assisted; ecosystem variation untested |
| Acquire upstream information | Complete public sources in both | Deterministic retrieval candidate; missing-source behavior untested |
| Interpret target relevance | Substantial AI/manual reasoning | Human/model-assisted; automation unvalidated |
| Interpret CI authority | Workflow and run inspection useful | Partial deterministic structure; dynamic/reusable cases untested |
| Attribute failing CI | No real case | Not yet tested |
| Construct bounded decision | Manual evidence joining | Requires baseline/rubric and cross-case evaluation |
| Render reports | Manually produced | Deterministic rendering appears plausible after result contract stabilizes |
| Persist/replay artifacts | Not yet materialized | Not tested |

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
- Which responsibilities are stable, conditional, case-specific, or outside scope?
- Which methods are manually useful but not credibly automatable?
- What must Ali independently explain, verify, or perform before capability claims?

## Next-case and current-work record

| Source | Required work/contrast | Reason | Priority |
|---|---|---|---|
| New local artifact specification | Retrofit S001 | Test honest reconstruction, correction, missing raw outputs, and manifest states | Current first |
| New local artifact specification | Retrofit S002 | Test full bundle, expired evidence, conditional decision, and progression limits | Current second |
| S002 | Actual failing test workflow with ambiguous cause | Test failure attribution and primary investigate/block behavior | S003 after retrofits |
| Thesis | Deliberately simple case where baseline is sufficient | Prevent investigation overreach and measure cost | High-value early case |
| Evidence model | Missing/fragmented/contradictory upstream data | Test degradation, corroboration, defer, and abstain | High-value later case |
| Artifact/platform model | Native or platform-specific dependency | Test wheel/source/platform/toolchain records | Later contrast |

## Coverage interpretation

A marked dimension establishes only that one case exposed it at the recorded
depth. It does not establish:

- complete understanding;
- product implementation;
- automation reliability;
- representative frequency;
- decision correctness;
- target safety;
- Ali-owned capability.

Use validated scenario narratives, runtime bundles, baseline comparisons, reviews,
and final synthesis—not coverage marks alone—to decide when implementation may
resume.