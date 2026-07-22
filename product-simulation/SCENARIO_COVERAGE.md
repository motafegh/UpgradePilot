# Product Simulation Scenario Coverage

**Status:** Active evolving discovery and comparative-evidence record  
**Local plan:** [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md)  
**Artifact specification:** [`RUNTIME_ARTIFACT_SPECIFICATION.md`](RUNTIME_ARTIFACT_SPECIFICATION.md)  
**Baseline:** [`TRANSPARENT_BASELINE_SPECIFICATION.md`](TRANSPARENT_BASELINE_SPECIFICATION.md)  
**Current synthesis:** [`S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`](S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md)  
**Next-case requirements:** [`S003_FAILING_CI_SCENARIO_REQUIREMENTS.md`](S003_FAILING_CI_SCENARIO_REQUIREMENTS.md)

## Purpose

Track whether real scenarios are materially different enough to expose:

- the actual UpgradePilot operating model;
- the durable runtime artifact lifecycle;
- strengths and failures of the transparent baseline;
- stable, conditional, contradicted, and unresolved responsibilities;
- review, evaluation, and ownership status;
- the next highest-value scenario.

This file is a compact status record, not a frozen taxonomy, production schema,
frequency claim, automation proof, or substitute for scenario evidence.

## Scenario register

| Scenario | Repository/update | Narrative and artifact status | Baseline status | Review/evaluation status | Manual outcome | Most important insight |
|---|---|---|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md) | `pydantic/pydantic` — Soup Sieve 2.6 → 2.8.4 | Complete retrospective reconstruction; 35 manifest items, 22 operations, 26 evidence items, 16 transformations, 12 findings; validation passed | Complete v0.1: same action with weaker reasons, certainty, and actionability | Factual correction complete; Ali challenged and final acceptance pending; external confirmation absent | Merge after normal review | Dependency path, target use, advisory authority, artifact identity, exact CI responsibility, and uncertainty must be joined |
| [`S002`](scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | `Aidan-Wallace/kubernetes-dashboard-token-api` — HTTPX 0.27.2 → 0.28.1 | Complete retrospective reconstruction; 39 files, 10 operations, 20 evidence items, 9 transformations, 9 findings; validation passed | Complete v0.1: same action with weaker reasons, certainty, and actionability | AI factual recheck complete; Ali review pending; exact-head behavior not confirmed | Run targeted checks; merge only after exact-head Python checks pass | CI authority requires trigger, command, responsibility, revision, environment, and retention context |

Both bundles are artifact-lifecycle complete as retrospective reconstructions.
Neither claims that its JSON/JSONL artifacts existed during the original
investigation.

Artifact and record counts describe granularity and preservation choices. They
are not quality metrics.

## Cross-case artifact result

The default top-level logical artifact family survived both cases:

- run manifest;
- invocation;
- frozen case identity;
- operation events;
- evidence items;
- claims and interpretations;
- findings;
- baseline result;
- decision;
- machine and human reports;
- follow-up state;
- review and ownership;
- bounded raw and check outputs.

No current evidence justifies removing a universal responsibility or adding a new
universal top-level artifact.

Current defects and open tests:

| Area | Current result | Next evidence required |
|---|---|---|
| Common fields and IDs | Equivalent concepts drift across S001/S002 | Apply one S003 representation profile |
| Time/run identity | Different formats and precision | Use RFC 3339 UTC and one S003 run-ID pattern |
| Serialization | Pretty and compact JSON both present | Use deterministic readable JSON for S003 |
| Validation | Both passed different validation methods | Use one declared S003 validation profile |
| Prospective progression | Not tested; both are retrofits | S003 natural selected/frozen → investigation → decision → review checkpoints |
| Repeated check executions | Not cleanly represented as structured comparisons | Trial `CHECK_EXECUTIONS.jsonl` in S003 |
| Causal failure state | Not tested | Trial `FAILURE_ATTRIBUTION.json` in S003 |
| Decision axes | Dependency assessment and PR mergeability not yet separated | Test explicitly in S003 |
| Production schema | Not selected | More cases and synthesis required |

Existing S001/S002 IDs and fields remain unchanged because cosmetic normalization
would rewrite referenced historical records without adding evidence.

## Product coverage dimensions

| Dimension | Covered by | Remaining uncertainty |
|---|---|---|
| Update lifecycle | S001 minor multi-release; S002 superseded predecessor and 0.x API-removal line | major, pre-release, yanked, replacement, competing active PRs |
| Dependency relationship | S001 transitive docs tooling; S002 direct declaration, adapter-mediated test use, production installation | direct application runtime, optional, build/native, markers/extras |
| Change shape | S001 lockfile-only; S002 manifest-only | source/config changes and multi-package updates |
| Upstream information | Complete primary sources in both | missing, fragmented, contradictory, migrated sources |
| Repository relevance | Indirect docs path; framework-adapter test path | direct runtime and genuinely irrelevant cases |
| Compatibility | Python floor and framework threshold | OS, architecture, compiler, build-tool, data/behavior changes |
| CI/test evidence | Relevant passing CI; green but incomplete CI | actual failing, flaky, stale, environmental, unrelated failure |
| CI trigger/command coverage | Relevant docs build; excluded Python workflow | reusable workflows, matrices, dynamic commands, generated paths |
| Environment identity | Lock-derived environment; unpinned drifting framework environment | private indexes, caches, platform resolution, constraints |
| Security | Advisory remediation with unresolved exploitability; ordinary maintenance | incomplete disclosure and active exploitation |
| Evidence agreement | S001 correction; S002 agreement with missing behavioral proof | direct contradiction and no-corroboration cases |
| Decision shape | Normal review; targeted checks | primary block, defer, abstain, mixed dependency/PR action |
| Reproducibility | Stable historical cases with explicit gaps | moving open PR, real rerun, partial recovery |
| Failure attribution | Not covered | update-caused, pre-existing, flaky, environmental, unrelated, mixed, unresolved |
| Baseline class | Same action with stronger full investigation in two cases | wrong action, baseline sufficient, unresolved, overreach/cost |

## Cross-case stability classification

### Repeated stable candidates

- public repository and PR locator can start acquisition;
- exact repository/base/head/change identity must be frozen;
- invocation and discovered identity remain separate;
- dependency path is first-class evidence;
- dependency role is multi-axis;
- upstream information requires repository-specific relevance analysis;
- CI authority requires trigger, commands, responsibility, revision, environment,
  and retention state;
- evidence absence, expiry, or inaccessibility can produce a specific action;
- operation, evidence, transformation, finding, decision, report, follow-up, and
  review are distinct logical responsibilities;
- superseded records remain visible;
- machine and human reports are distinct projections;
- merge history is action, not correctness evidence;
- structural validation is a credible deterministic responsibility;
- AI-generated completion does not establish Ali-owned capability.

### Conditional responsibilities

- advisory and exploitability analysis;
- adapter/framework compatibility;
- artifact/hash identity verification;
- dynamic execution;
- private or credentialed acquisition;
- post-merge publication/deployment checks;
- platform/native/toolchain analysis;
- repeated execution and causal failure attribution.

### Contradicted assumptions

- one dependency-role enum is adequate;
- direct imports are the only meaningful use path;
- green CI has global authority;
- workflow color is enough without command coverage;
- advisory presence proves target exploitability;
- merge state proves correctness;
- every case needs dynamic execution;
- one `CASE.md` simulates the complete runtime;
- full investigation must change the broad action to add value;
- artifact counts measure quality;
- manual success proves automation feasibility.

### Unresolved

- claims and interpretations as one or two physical streams;
- append-only finding history versus current-state projection;
- follow-up physically separate from decision;
- raw capture grouping and manifest growth at scale;
- dependency assessment versus PR action as separate outcomes;
- real rerun and replay semantics;
- conflicting evidence and decision versioning;
- investigation cost when the baseline is sufficient;
- reliable automation boundary;
- Ali independent execution and explanation depth.

## Baseline and thesis evidence

There are now two materialized comparisons:

| Scenario | Baseline outcome | Full outcome | Comparative result |
|---|---|---|---|
| S001 | `merge_after_normal_review` | `merge_after_normal_review` | Same action; full result better located uncertainty, bounded CI authority, exploitability, remediation, and follow-up |
| S002 | `run_targeted_checks` | `run_targeted_checks` | Same action; full result identified the TestClient path, framework threshold, skipped tests, exact checks, and transitions |

Supported thesis class:

```text
same broad action
+
materially stronger authority, calibration, explanation, auditability, or
actionability
```

The overall thesis remains unvalidated. Required future classes:

- baseline wrong action;
- baseline sufficient with little added value;
- unresolved comparison;
- full-investigation overreach or excessive cost.

S003 is for causal failure attribution and must not be forced into any thesis
class.

## Automation-feasibility coverage

| Responsibility | Current evidence | Status |
|---|---|---|
| Freeze change identity | Repeated connector-backed success | Deterministic automation appears credible |
| Parse simple version transition | Two simple ecosystems/changes | Deterministic candidate; broader syntax untested |
| Resolve dependency path | Lock and adapter examples | Tool-assisted; ecosystem variation untested |
| Acquire public upstream evidence | Successful in both | Deterministic retrieval candidate; failure behavior untested |
| Interpret repository relevance | Substantial AI/manual reasoning | Human/model-assisted; automation unvalidated |
| Interpret CI authority | Workflow/run inspection useful | Partial deterministic structure; complex CI untested |
| Attribute failing CI | No real case | S003 primary target |
| Construct bounded decision | Two structured manual results | Requires broader calibration and failure cases |
| Render reports | Separate machine/human artifacts in both | Deterministic rendering plausible after contracts stabilize |
| Persist/replay | Two retrospective bundles | Logical need demonstrated; prospective behavior untested |
| Validate bundle | Two zero-defect passes with different methods | Deterministic candidate; common validator/profile needed |

## S003 required coverage

S003 must add evidence for:

- actual failing decision-relevant CI;
- exact run/job/step/command/environment identity;
- base/head/main/rerun comparability;
- update-caused versus pre-existing, flaky, environmental, unrelated, mixed, or
  unresolved attribution;
- dependency-specific assessment versus overall PR action;
- structured check execution records;
- versioned failure attribution;
- prospective artifact checkpoints;
- baseline comparison under failing CI;
- transition behavior after rerun, rebase, fix, or changed environment.

Candidate selection and execution details are controlled by
[`S003_FAILING_CI_SCENARIO_REQUIREMENTS.md`](S003_FAILING_CI_SCENARIO_REQUIREMENTS.md).

## Current work and next action

| Work | Status | Next action |
|---|---|---|
| S001 retrofit | Complete and validated | Include in Ali review |
| S002 retrofit | Complete and validated | Include in Ali review |
| S001/S002 artifact review | Complete; Ali acceptance pending | Review synthesis and challenged items |
| S003 requirements | Written; Ali acceptance pending | Review before candidate selection |
| S003 candidate | Not selected | Select only after requirements review |
| M2-S03 implementation | Paused | Remains paused pending further simulation and synthesis |

The next selected action is Ali review of the cross-case synthesis and S003
requirements. After acceptance or correction, select one qualifying S003
candidate and begin prospectively from the selected-and-frozen checkpoint.

## Interpretation limits

Coverage establishes only that a case exposed a condition at the documented
depth. It does not establish complete understanding, product implementation,
automation reliability, representative frequency, decision correctness, target
safety, final schema fitness, or Ali-owned capability.
