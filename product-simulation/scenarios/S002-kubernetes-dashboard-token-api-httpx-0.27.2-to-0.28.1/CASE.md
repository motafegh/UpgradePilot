# S002 — Kubernetes Dashboard Token API: HTTPX 0.27.2 → 0.28.1

> **Narrative status:** Complete.  
> **Artifact-lifecycle status:** Complete retrospective reconstruction; exact historical raw logs, resolver state, operation timestamps, and original progressive artifact checkpoints remain unavailable.  
> **Review status:** AI factual recheck complete; Ali review pending.  
> **Execution mode:** `retrospective_artifact_reconstruction`.

## Scenario identity

- **Scenario ID:** `S002`
- **Run ID:** `s002-retrofit-2026-07-22-r1`
- **Repository:** `Aidan-Wallace/kubernetes-dashboard-token-api`
- **Public change:** PR `#20`
- **Dependency update:** `httpx==0.27.2` → `httpx==0.28.1`
- **Base SHA:** `b065646e4b7b894964567950f9ad770b02c136c2`
- **Head SHA:** `391508134b083b8f54461c0b576e8f7985c6ecb4`
- **Historical merge commit:** `45bf6d64c91504a902b22539afa746a473fbae5d`
- **Original investigation date:** 2026-07-22
- **Artifact reconstruction date:** 2026-07-22
- **Investigators:** AI assistant under Ali's direction
- **Ali capability claim:** none from this scenario; independent review and execution remain pending

## Live case state

- **Current phase:** Runtime narrative and manual artifact bundle complete; awaiting Ali review and maintainer-owned targeted checks.
- **Current primary question:** Do the exact-head Ruff and route tests pass under a captured dependency resolution?
- **Current finding:** A then-current FastAPI/Starlette line was likely compatible, but the public PR evidence did not execute the relevant TestClient behavior and the historical resolved environment is unavailable.
- **Current decision:** `run_targeted_checks`
- **Current limitations:** no public exact-head Python test result; historical Docker logs expired; exact FastAPI/Starlette resolution missing; private checks and rationale unknown.
- **Next action:** In a trusted isolated checkout of the frozen head, capture resolved versions and run `ruff check .` plus `pytest --cov`.
- **Decision transition:** pass → merge after normal review; relevant failure → investigate/block; unavailable/inconclusive → retain targeted-check/defer state; changed head/resolution → new run or comparison.

## Runtime artifact bundle

| Logical responsibility | Artifact | State |
|---|---|---|
| Run index and reconstruction disclosure | [`artifacts/RUN_MANIFEST.json`](artifacts/RUN_MANIFEST.json) | Present |
| Starting product invocation | [`artifacts/INVOCATION.json`](artifacts/INVOCATION.json) | Present; retrospectively reconstructed |
| Frozen case identity | [`artifacts/CASE_IDENTITY.json`](artifacts/CASE_IDENTITY.json) | Present |
| Material operation sequence | [`artifacts/OPERATION_EVENTS.jsonl`](artifacts/OPERATION_EVENTS.jsonl) | Present; original times partly unknown |
| Evidence and evidence states | [`artifacts/EVIDENCE_ITEMS.jsonl`](artifacts/EVIDENCE_ITEMS.jsonl) | Present |
| Claims and interpretations | [`artifacts/CLAIMS_AND_INTERPRETATIONS.jsonl`](artifacts/CLAIMS_AND_INTERPRETATIONS.jsonl) | Present |
| Case findings and supersession | [`artifacts/FINDINGS.json`](artifacts/FINDINGS.json) | Present |
| Transparent baseline | [`artifacts/BASELINE_RESULT.json`](artifacts/BASELINE_RESULT.json) | Present; retrospective v0.1 |
| Current decision | [`artifacts/DECISION.json`](artifacts/DECISION.json) | Present |
| Machine-facing report | [`artifacts/MACHINE_REPORT.json`](artifacts/MACHINE_REPORT.json) | Present |
| Maintainer-facing report | [`artifacts/HUMAN_REPORT.md`](artifacts/HUMAN_REPORT.md) | Present |
| Follow-up and rerun state | [`artifacts/FOLLOW_UP_STATE.json`](artifacts/FOLLOW_UP_STATE.json) | Present |
| Review and ownership | [`artifacts/REVIEW_AND_OWNERSHIP.json`](artifacts/REVIEW_AND_OWNERSHIP.json) | Present; Ali review pending |
| Bounded source captures | [`artifacts/raw/`](artifacts/raw/) | Present |
| Manual comparisons and validation | [`artifacts/checks/`](artifacts/checks/) | Present |

The bundle is a manual simulation representation. Its exact files and fields are not accepted production schemas.

## Retrospective reconstruction disclosure

The original S002 investigation produced this `CASE.md` before the runtime-artifact requirement existed. The current bundle was created afterward.

The retrofit does **not** claim that:

- JSON or JSONL artifacts existed during the original investigation;
- every historical operation time is known;
- the original candidate list or every discarded lookup can be recovered;
- historical Docker logs or the exact package resolution are recoverable;
- the original Git history proves all artifact states were progressively committed.

The retrofit preserves:

- candidate screening before formal identity freeze;
- the exact PR, patch, base/head revisions, and superseded predecessor;
- evidence IDs `E01`–`E20`;
- the HTTP 410 log-retrieval failure;
- the earlier possible-hard-break hypothesis as superseded;
- the likely-compatible but unproven finding;
- the targeted-check decision and transition state;
- honest AI/Ali ownership limits.

## 1. Why this case was selected

S001 covered a transitive, lockfile-only documentation dependency with relevant green CI. S002 was selected to expose a materially different runtime:

- direct manifest pin;
- upstream API removal;
- target use through a framework adapter;
- dependency installed into the production image;
- green CI that did not exercise the relevant behavior;
- a relevant workflow skipped by path filtering;
- an unpinned environment with expired historical logs;
- a predecessor update explicitly superseded by the selected PR.

The case remains useful because it demonstrates that dependency directness and a green status are insufficient without usage, adapter, trigger, command, and environment analysis.

## 2. Initial real-world event

Dependabot opened PR #20 on 2024-12-09:

```text
httpx==0.27.2
→
httpx==0.28.1
```

PR #17 had proposed HTTPX 0.28.0 and was closed with the Dependabot comment:

```text
Superseded by #20.
```

Before UpgradePilot begins, the repository has:

- a FastAPI application;
- direct HTTPX and unpinned `fastapi[standard]` requirements;
- route tests using FastAPI `TestClient`;
- a Docker workflow that builds on pull requests;
- a Python workflow containing Ruff and pytest but excluding `requirements.txt` from its path filters.

## 3. Invocation and identity

The product-runtime invocation begins with only:

- repository locator: `Aidan-Wallace/kubernetes-dashboard-token-api`;
- PR locator: `20`;
- request: investigate the dependency update and support the maintainer decision;
- public-only access and no target mutation authorization.

Candidate selection is pre-run simulation context, not a semantic answer supplied to the runtime.

After invocation, exact identity is discovered and frozen in [`CASE_IDENTITY.json`](artifacts/CASE_IDENTITY.json). Base/head SHAs, the changed dependency, versions, changed path, merge state, and supersession relationship are not treated as starting input.

## 4. Actors and trust boundaries

| Actor/system | Responsibility | Authority and limit |
|---|---|---|
| Dependabot | Creates update and supersession comment | Strong for proposal mechanics, not correctness |
| GitHub Pull Requests | Stores PR identity, patch, lifecycle | Strong for exact change and history, not safety |
| Target repository | Requirements, application, tests, workflows, Dockerfile | Strong for frozen declared state; static source is not runtime proof |
| HTTPX | Changelog and package metadata | Strong upstream declaration; not target impact alone |
| FastAPI | Framework constraints and HTTPX extra | Strong for exact tagged metadata |
| Starlette | TestClient implementation | Strong for exact tagged source behavior |
| GitHub Actions | Workflow, run, job, and log states | Strong only for the exact commands and retained outputs |
| pip resolver/Docker | Historical install and image build | Build success exists; exact resolved graph is unavailable |
| Maintainer | Final decision and private context | Merge authority; merge action is not correctness proof |
| Ali | Product owner and reviewer | Directed work; independent technical execution not shown |
| AI assistant | Manual system and artifact constructor | Substantial interpretation/control; must preserve limits |

## 5. Maintainer-decision questions

1. What exact update and repository revision are proposed?
2. Is HTTPX direct, transitive, test-only, runtime, or installed in deployment?
3. Which HTTPX 0.28 changes intersect actual repository use?
4. Does the resolved Starlette adapter still pass the removed `app` argument?
5. Which workflow ran, which commands executed, and which responsibility was exercised?
6. Can the historical dependency environment be reconstructed?
7. What is the smallest justified maintainer action?
8. What artifacts must persist for replay, review, and a later result transition?

## 6. Evidence model

The machine-readable inventory is [`EVIDENCE_ITEMS.jsonl`](artifacts/EVIDENCE_ITEMS.jsonl). It retains original IDs:

| IDs | Evidence family | Key state |
|---|---|---|
| `E01`–`E03` | PR identity, patch, supersession | Accepted |
| `E04`–`E08` | target requirements, tests, source search, Docker/README context | Accepted with static limits |
| `E09`–`E13` | HTTPX/FastAPI/Starlette compatibility sources | Accepted with target-resolution limit |
| `E14`–`E18` | workflow definitions, Dockerfile, run/job, missing Python run | Accepted or missing/expected absent |
| `E19` | Docker job-log retrieval | Expired/inaccessible, HTTP 410 |
| `E20` | public discussion/review lookup | Accepted negative evidence; private review unknown |

Every evidence record identifies its producing operation, source identity, raw/reference capture, authority, limitations, and downstream use.

## 7. Progressive operation history

[`OPERATION_EVENTS.jsonl`](artifacts/OPERATION_EVENTS.jsonl) records ten material operations:

1. candidate screening and case selection;
2. exact identity freeze;
3. dependency role and target path classification;
4. upstream HTTPX change acquisition;
5. FastAPI/Starlette compatibility threshold comparison;
6. CI trigger, command, run, and environment authority analysis;
7. failed Docker log retrieval and recovery path;
8. transparent baseline v0.1 reconstruction;
9. decision, machine report, human report, and follow-up materialization;
10. bundle validation.

`op-001` and the original operation timing are reconstructed from the prior narrative. Retrofit retrieval and validation operations are dated 2026-07-22.

## 8. Repository-specific relevance

HTTPX is simultaneously:

- **declared:** direct pin in `requirements.txt`;
- **functionally used:** through `fastapi.testclient.TestClient`;
- **direct application import:** not observed by static search;
- **deployment installed:** included in the production image because all dependencies share one requirements file.

Observed path:

```text
tests/test_routes.py
→ fastapi.testclient.TestClient
→ starlette.testclient.TestClient
→ httpx.Client
```

A single `runtime`, `test-only`, or `development` label would lose material meaning.

## 9. Upstream and adapter compatibility

HTTPX 0.28 removed the deprecated `app` argument.

Starlette 0.36.3 calls:

```python
super().__init__(app=self.app, ...)
```

Starlette 0.37.2 calls HTTPX without `app=`.

FastAPI 0.115.2 requires:

```text
starlette>=0.37.2,<0.41.0
```

Therefore:

- old Starlette branch → expected incompatibility;
- fixed Starlette branch → removed-argument incompatibility resolved;
- target historical branch → unknown because FastAPI is unpinned and resolver evidence is missing.

The original concern that HTTPX 0.28 might directly break the target is preserved as finding `F0`, then superseded by the narrower finding `F5`: likely compatibility with unresolved exact environment.

## 10. CI authority

The Docker workflow:

- triggers for PRs;
- builds the Dockerfile;
- installs the shared requirements;
- has one successful run and job on the frozen head;
- does not run Ruff, pytest, TestClient initialization, or application startup during the build.

The Python workflow:

- would run `ruff check .`;
- would run `pytest --cov`;
- triggers only for changes under `app/**`, `static/**`, `templates/**`, and `tests/**`;
- does not include `requirements.txt`;
- therefore did not trigger for the one-file manifest update.

The log request for job `44966848674` returned HTTP 410. The exact installed FastAPI/Starlette versions cannot be reconstructed publicly.

Conclusion:

> Green CI is real but has authority only for installation and image construction. It does not establish TestClient behavior.

## 11. Findings

The current versioned findings are in [`FINDINGS.json`](artifacts/FINDINGS.json).

Most material findings:

- `F2` — multi-axis dependency role;
- `F3` — HTTPX `app` removal;
- `F4` — old/fixed Starlette compatibility threshold;
- `F5` — likely compatibility with unresolved target environment;
- `F6` — green Docker CI but skipped decision-relevant tests;
- `F7` — historical environment and rationale unavailable;
- `F8` — exact-head resolver capture and existing Python checks are the smallest proportionate action.

Every finding references evidence and claim/interpretation IDs.

## 12. Transparent baseline comparison

[`BASELINE_RESULT.json`](artifacts/BASELINE_RESULT.json) applies `simulation-transparent-baseline-v0.1` using only:

- version category: `minor`;
- overall CI conclusion: `passing`;
- directness: `direct`;
- literal release-note signals: `deprecated`, `removed`, and `fixed`.

Rule `B04` matches because caution keywords are present. Baseline outcome:

```text
run_targeted_checks
```

The full investigation reaches the same broad action, but materially improves it:

- identifies the exact TestClient path;
- shows a compatible framework threshold;
- limits green CI to install/build authority;
- exposes skipped Python tests;
- preserves the missing historical environment;
- specifies exact checks and result transitions.

Comparative classification:

- `baseline_same_action_weaker_reasons`;
- `baseline_same_action_miscalibrated_certainty`;
- `baseline_same_action_less_actionable`.

This case qualitatively supports the project thesis, but it is not a wrong-action baseline example.

## 13. Decision

The current structured decision is [`DECISION.json`](artifacts/DECISION.json).

### Outcome

```text
run_targeted_checks
```

### Required checks

1. `ck-001` — install the frozen requirements in a trusted isolated checkout and preserve the complete resolved versions;
2. `ck-002` — run `ruff check .`;
3. `ck-003` — run `pytest --cov`.

### Why not merge immediately

Likely compatibility, a successful installation, and a green Docker workflow do not prove the exact TestClient path.

### Why not block indefinitely

Primary-source evidence establishes a compatible framework branch, and one dependency resolution installed successfully. A focused existing test is proportionate before a hard block.

## 14. Reports and follow-up

- Machine-facing result: [`MACHINE_REPORT.json`](artifacts/MACHINE_REPORT.json)
- Maintainer-facing result: [`HUMAN_REPORT.md`](artifacts/HUMAN_REPORT.md)
- Persistent next-state model: [`FOLLOW_UP_STATE.json`](artifacts/FOLLOW_UP_STATE.json)

The human report is intentionally shorter than this case narrative. It contains only the exact change, repository relevance, current evidence, recommendation, checks, transitions, and limits.

## 15. Changed-evidence behavior

| New evidence | State transition |
|---|---|
| Resolver captured and Ruff/pytest pass | `merge_after_normal_review` |
| TestClient or route tests fail due to HTTPX/Starlette | `investigate_or_block` |
| Checks unavailable or inconclusive | retain `run_targeted_checks` or defer |
| New head SHA or changed constraints | new run/comparison required |
| Different resolved environment | do not silently reuse current conclusion |

A future result must supersede or compare with this run, not overwrite it.

## 16. Candidate methods and automation implications

| Responsibility | Current method | Automation status |
|---|---|---|
| PR identity and patch | GitHub structured retrieval | Deterministic automation appears credible |
| Manifest transition | direct diff comparison | Credible simple parser; broader syntax untested |
| Dependency role | repository/test/Docker join | Tool-assisted; multi-axis representation required |
| Upstream acquisition | tagged source retrieval | Credible retrieval; missing-source behavior untested |
| Adapter relevance | manual/AI source comparison | Automation unvalidated |
| CI authority | trigger, command, run, and environment join | Partial deterministic structure; complex workflows untested |
| Targeted-check selection | manual sufficiency reasoning | Requires cross-case evaluation |
| Decision/report rendering | structured manual artifacts | Deterministic rendering plausible after contracts stabilize |
| Persistence/replay | manual bundle | First materialized example; implementation not selected |

Simulation use does not select a permanent architecture.

## 17. Review and ownership

[`REVIEW_AND_OWNERSHIP.json`](artifacts/REVIEW_AND_OWNERSHIP.json) separates:

- execution completion;
- AI factual review;
- Ali review;
- external behavior confirmation;
- learner ownership.

Current state:

- **AI factual review:** completed against re-acquired primary sources;
- **Ali review:** pending;
- **external behavioral confirmation:** absent;
- **AI contribution:** substantial control;
- **Ali contribution:** direction and requirement definition;
- **Ali capability evidence from S002:** none yet.

## 18. Validation

[`artifacts/checks/CK04-bundle-validation.json`](artifacts/checks/CK04-bundle-validation.json) records:

- every JSON file parsed;
- every JSONL line parsed;
- unique operation, evidence, record, finding, reason, and check IDs;
- resolved internal references;
- consistent scenario/run/frozen identity;
- coherent operation order;
- evidence-to-operation lineage;
- finding-to-evidence/interpretation lineage;
- decision-to-finding lineage;
- report/decision consistency;
- manifest/file agreement;
- explicit review and historical-gap states.

Validation establishes structural consistency only. It does not establish external correctness or Ali ownership.

## 19. Completion audit

- [x] Complete narrative exists.
- [x] Every required logical runtime artifact exists.
- [x] Retrofit status and historical gaps are explicit.
- [x] Raw/reference captures are bounded and indexed.
- [x] Material operations, failures, and supersession are preserved.
- [x] Evidence, claims, interpretations, findings, decision, and reports remain distinct.
- [x] Baseline v0.1 is executed without full-investigation leakage.
- [x] Decision and follow-up transitions are explicit.
- [x] JSON/JSONL syntax and cross-references are validated.
- [x] AI/Ali/external review states remain separate.
- [x] No unexecuted target check is represented as a result.
- [x] No unavailable historical data was invented.

## 20. Completion statement

S002 is now complete at two separate levels:

1. **Product-behavior simulation:** complete at the available public evidence level.
2. **Artifact-lifecycle simulation:** complete as an honest retrospective reconstruction.

Supported conclusion:

> Run exact-head Python checks under a captured dependency resolution; merge after normal review only if they pass.

Not supported:

- definite compatibility of the historical exact environment;
- complete production safety;
- correctness inferred from the historical merge;
- TestClient behavior inferred from Docker build success;
- independent Ali ownership of the investigation.

The most important product-model finding remains:

> CI evidence needs trigger, command, responsibility, revision, and environment lineage. A green conclusion has no global authority.

The next scenario remains a real dependency-update PR with an actual failing workflow requiring causal attribution—but it must begin with progressive runtime artifacts from the first frozen checkpoint.
