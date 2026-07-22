# S002 — Kubernetes Dashboard Token API: HTTPX 0.27.2 → 0.28.1

> **Record status:** Complete progressive primary record. Candidate screening occurred before the case was frozen and is preserved separately from the active scenario steps rather than rewritten as though PR #20 had been selected from the beginning.

## Scenario identity

- **Scenario ID:** S002
- **Status:** complete
- **Repository:** `Aidan-Wallace/kubernetes-dashboard-token-api`
- **Dependency update:** `httpx==0.27.2` → `httpx==0.28.1`
- **Public change reference:** `https://github.com/Aidan-Wallace/kubernetes-dashboard-token-api/pull/20`
- **Base revision:** `b065646e4b7b894964567950f9ad770b02c136c2`
- **Head revision:** `391508134b083b8f54461c0b576e8f7985c6ecb4`
- **Merge commit:** `45bf6d64c91504a902b22539afa746a473fbae5d`
- **Investigated time boundary:** PR creation on 2024-12-09 through merge on 2025-06-28, with historical evidence observed on 2026-07-22
- **Date investigated:** 2026-07-22
- **Investigators:** AI assistant under Ali's direction; Ali review and independent technical verification are not claimed

## Live case state

- **Current phase:** Complete; awaiting Ali's review
- **Current primary question:** Resolved at the available evidence level
- **Current working hypothesis:** Superseded by the final bounded finding below
- **Last material finding:** HTTPX 0.28.1 is likely compatible with a then-current FastAPI/Starlette resolution, but the dependency-only PR bypassed the Python test workflow, so public CI does not prove `TestClient` behavior
- **Current recommendation state:** `run targeted checks`; merge only after the exact-head Python tests pass under a captured dependency resolution
- **Current material limitations:** Exact resolved FastAPI/Starlette versions and historical job logs are unavailable; no public Python test run is attached to the PR head; private maintainer checks are unknown
- **Next selected action:** Ali reviews this case; the next scenario should contain an actual failing test workflow requiring failure attribution
- **Reason for next action:** Further static investigation cannot replace the missing exact-head behavioral test, and the next highest-value product uncertainty is distinguishing update-caused failure from pre-existing, flaky, environmental, or unrelated failure
- **Last updated:** 2026-07-22

## Pre-selection candidate screening

S001 covered a transitive, lockfile-only documentation dependency with complete upstream information and green decision-relevant CI. The highest-value contrast in `SCENARIO_COVERAGE.md` was a direct dependency with an API or behavior change and failing, conflicting, or misleading CI.

Several HTTPX 0.27.2 → 0.28.x Dependabot PRs were screened. PR #20 was selected because it provides:

- a direct manifest pin rather than a transitive lockfile change;
- a real upstream API removal, `httpx.Client(app=...)`;
- target tests that instantiate FastAPI's `TestClient`;
- a superseded predecessor PR, #17;
- a successful Docker workflow;
- a separate Python test workflow whose path filter excludes the changed manifest;
- a historical merged outcome but no preserved public Python-test proof.

Candidate screening establishes why this case was selected. It is not treated as evidence that PR #20 had already been frozen before screening finished.

## 1. Why this case was selected

This case materially contrasts with S001:

- direct declared dependency rather than lock-derived transitive dependency;
- manifest-only change rather than lockfile-only change;
- upstream API removal rather than advisory interpretation;
- repository tests directly traverse the dependency through a framework test client;
- green CI exists but does not execute the decision-relevant path;
- the exact environment can drift because `fastapi[standard]` is unpinned;
- the earlier HTTPX 0.28.0 PR was automatically superseded by 0.28.1;
- the repository eventually merged the change, while the preserved public evidence supports only a conditional recommendation.

Known limits:

- historical workflow logs have expired and return HTTP 410;
- the exact FastAPI and Starlette versions used in the successful Docker build are not preserved;
- no public review explains the merge decision;
- executing untrusted public repository code is outside this manual simulation, so the decisive dynamic test remains a maintainer-owned follow-up.

These limits are useful product evidence. They expose requirements for CI-path analysis, environment identity, expired-evidence handling, and conditional recommendations.

## 2. Initial real-world event

Dependabot opened PR #20 on 2024-12-09 to replace the direct requirement:

```text
httpx==0.27.2
→
httpx==0.28.1
```

PR #20 followed PR #17, which proposed HTTPX 0.28.0 and was closed by Dependabot with the explicit comment `Superseded by #20.`

Before UpgradePilot begins, the target repository contains:

- a FastAPI application;
- a direct HTTPX pin in `requirements.txt`;
- route tests using `fastapi.testclient.TestClient`;
- a Docker workflow triggered by pull requests;
- a Python test workflow triggered only by changes under application, static, template, or test paths.

The maintainer sees a one-line dependency change, generated upstream notes, a successful Docker workflow, no public Python-test run, and no review discussion.

## 3. Intended invocation

The smallest credible invocation is a repository and pull-request locator. Exact identity must then be acquired and frozen.

| Item | Value | Supplied by | Purpose | Requirement | Missing or wrong consequence |
|---|---|---|---|---|---|
| Repository locator | `Aidan-Wallace/kubernetes-dashboard-token-api` | Maintainer, event, or caller | Locate target repository | Required unless authenticated event already binds it | Wrong repository invalidates all relevance analysis |
| Pull-request locator | `20` or PR URL | Maintainer, event, or caller | Locate proposed change | Required | Exact change cannot be identified |
| Event/auth context | Not preserved historically | GitHub installation/runtime | Access and actor context | Conditional | Public investigation remains possible; private operation may fail |
| Maintainer policy | Not supplied | Project configuration or maintainer | Apply local merge/check policy | Optional for generic result; required for policy compliance | Product must not claim policy compliance |

The following are acquired evidence, not invocation inputs:

- release notes and upstream source;
- target manifests, application code, tests, and workflows;
- CI results;
- FastAPI/Starlette compatibility information;
- predecessor PR #17;
- the eventual merge action.

## 4. Case identity and reproducibility boundary

Authoritative identity:

- repository: `Aidan-Wallace/kubernetes-dashboard-token-api`;
- PR: `#20`;
- base branch: `main`;
- base SHA: `b065646e4b7b894964567950f9ad770b02c136c2`;
- head branch: `dependabot/pip/httpx-0.28.1`;
- head SHA: `391508134b083b8f54461c0b576e8f7985c6ecb4`;
- changed dependency: `httpx`;
- old version: `0.27.2`;
- new version: `0.28.1`;
- changed path: `requirements.txt`;
- merge commit: `45bf6d64c91504a902b22539afa746a473fbae5d`.

Reproducible from public evidence:

- exact PR metadata and patch;
- base/head repository files;
- workflow definitions;
- target tests;
- tagged HTTPX, FastAPI, and Starlette source;
- surviving workflow-run summaries.

Not exactly reproducible:

- the package resolution used by the historical Docker build;
- full historical workflow logs;
- private/local tests;
- maintainer reasoning;
- private deployment behavior.

Later repository state is not treated as evidence for the frozen base/head unless explicitly labeled as later context.

## 5. Actors and systems

| Actor or system | Role | Material data | Authority and limits | Interaction with UpgradePilot |
|---|---|---|---|---|
| Dependabot | Update producer | PR, version transition, generated notes, supersession comment | Authoritative for proposal mechanics; generated notes are not target proof | Starts or exposes case |
| GitHub Pull Requests | Identity and change store | Base/head SHAs, patch, timestamps, state | Strong identity; does not establish correctness | Invocation and acquisition surface |
| Target repository | Product context | Requirements, source, tests, workflows, Dockerfile | Authoritative for frozen declared behavior/configuration | Primary relevance source |
| HTTPX project | Dependency producer | Changelog, metadata, tagged implementation | Authoritative for upstream declarations; not target impact alone | Upstream evidence source |
| FastAPI project | Framework producer | Standard extra and Starlette constraints | Authoritative for tagged requirements; exact target resolution unknown | Compatibility bridge |
| Starlette project | TestClient implementation owner | Old and fixed adapter behavior | Authoritative for tagged source behavior | Determines removed-argument exposure |
| GitHub Actions | CI executor | Docker success; absent Python run | Authoritative only for jobs actually run | Check evidence source |
| Docker and pip resolver | Build/dependency environment | Installation and image-build result | Successful build proves resolution/build, not tests | Conditional evidence producer |
| Maintainer | Decision maker | Merge action and possible private checks | Final merge authority; merge is not correctness proof | Report consumer and follow-up actor |
| Ali | UpgradePilot owner/reviewer | Product-model challenge and review | Independent execution not claimed here | Reviews simulation |
| AI assistant | Manual investigator | Acquisition, interpretation, report | Must preserve provenance, uncertainty, and assistance | Acts as manual system |

## 6. Initial questions for the maintainer decision

| Question | Why it matters | Evidence likely needed | Consequence if unresolved |
|---|---|---|---|
| What exact change is proposed? | Bounds all later evidence | PR identity and patch | No valid investigation |
| What role does HTTPX have? | Determines impact surface | Manifest, source, tests, Dockerfile | Checks may target wrong boundary |
| Which HTTPX changes intersect target use? | Release contains unrelated changes | Upstream changelog plus target path | Generic release notes may overstate risk |
| Does resolved Starlette still pass `app=` to HTTPX? | HTTPX 0.28 removed it | FastAPI constraints and Starlette source | TestClient may fail at initialization |
| What did CI execute? | Green status may be misleading | Workflow definitions, triggers, commands, run identity | CI cannot receive correct authority |
| Is environment identity reproducible? | Unpinned FastAPI can alter compatibility | Lock/constraints/resolver output/logs | Historical success may not replay |
| What action is justified? | Product must support maintainer choice | Joined findings and limitations | Must target checks or abstain rather than guess |

## 7. Evidence discovery map

| Source | Question | Expected authority | Acquisition | Result |
|---|---|---|---|---|
| PR #20 metadata and patch | Identity and change | High | GitHub PR API | Acquired |
| PR #17 and comment | Supersession | High for lifecycle | GitHub PR/comments | Acquired |
| Base/head requirements | Declaration/version | High | Contents at exact SHAs | Acquired |
| Application source | Runtime use | High for static use | Repository files/search | Acquired |
| Tests | Test-path use | High | Repository file | Acquired |
| Dockerfile | Build behavior | High | Repository file | Acquired |
| Workflow definitions | Trigger and command coverage | High | Repository files | Acquired |
| Workflow run/job/logs | Actual checks and environment | High when retained | Actions API | Summary/job acquired; logs expired |
| HTTPX changelog/metadata | Upstream changes/Python floor | High for upstream | Tagged source | Acquired |
| FastAPI metadata | Framework constraints | High for tag | Tagged source | Acquired |
| Starlette old/fixed source | Compatibility threshold | High for tag | Tagged source | Acquired |
| Dynamic target tests | Actual behavior | Highest direct behavior evidence | Trusted maintainer environment | Not performed |

## 8. Evidence inventory

| ID | Item and identity | Direct observation | Purpose | Authority and limits | State | Downstream use |
|---|---|---|---|---|---|---|
| E01 | PR #20 final metadata | Exact base/head, dates, merged state | Freeze case | Strong identity; merge not correctness proof | Accepted | Identity/history |
| E02 | PR #20 patch | One line changes HTTPX 0.27.2 to 0.28.1 | Define proposal | Strong mechanical evidence | Accepted | Transition |
| E03 | PR #17 Dependabot comment | `Superseded by #20.` | Explain predecessor closure | Establishes lifecycle only | Accepted | Supersession model |
| E04 | Base `requirements.txt` | Unpinned `fastapi[standard]`, HTTPX 0.27.2, test tools in same file | Classify role/environment | No resolved transitive versions | Accepted | Role/reproducibility |
| E05 | Head `requirements.txt` | HTTPX 0.28.1; FastAPI still unpinned | Confirm head | Same resolution limit | Accepted | Proposed environment |
| E06 | `tests/test_routes.py` | Imports FastAPI TestClient and constructs `TestClient(app)`; five route tests | Identify behavioral path | Does not prove pass/fail | Accepted | Targeted-check need |
| E07 | Application source/search | No direct HTTPX import observed | Separate app and test path | Static search cannot rule out every dynamic use | Accepted | Relevance bound |
| E08 | README and Dockerfile | Shared requirements installed in production image; TODO notes test tools should not be there | Deployment role | Documentation may be stale | Accepted | Multi-axis role |
| E09 | HTTPX 0.28.1 changelog | 0.28.0 removed `app` and `proxies`; 0.28.1 fixed SSL client-cert case | Upstream change | Target relevance requires joining | Accepted | Compatibility question |
| E10 | HTTPX 0.28.1 metadata | Requires Python >=3.8 | Python compatibility | Not full dependency compatibility | Accepted | Python-floor finding |
| E11 | FastAPI 0.115.2 metadata | Requires Starlette >=0.37.2,<0.41.0; standard extra includes HTTPX >=0.23 | Compatible framework line available | Exact target resolution unknown | Accepted with limit | Compatibility support |
| E12 | Starlette 0.36.3 source | TestClient passes `app=self.app` to HTTPX Client | Define incompatible branch | Applies only if old branch resolves | Accepted | Failure variant |
| E13 | Starlette 0.37.2 source | TestClient uses transport without passing `app=` | Define fixed branch | Exact target resolution unknown | Accepted | Likely compatibility |
| E14 | Docker workflow definition | Runs on PRs and builds image | Check scope | No tests defined | Accepted | CI authority |
| E15 | Dockerfile | Installs requirements; no test or app-start command | Explain proof boundary | Build only | Accepted | CI authority |
| E16 | Head Actions run 15940060582 | Docker job succeeded | Installation/build evidence | No test evidence | Accepted | Limited favorable evidence |
| E17 | Python workflow definition | Runs Ruff and `pytest --cov`, but PR paths exclude `requirements.txt` | Relevant-check trigger analysis | Strong config evidence | Accepted | Skipped-check finding |
| E18 | Head workflow lookup | No Python test run returned | Confirm absence | Retention/API limits possible; path filter independently explains absence | Missing/expected absent | Targeted-check requirement |
| E19 | Docker job log retrieval | HTTP 410 | Preserve expired evidence | Exact resolution unavailable | Inaccessible | Reproducibility limit |
| E20 | PR #20 discussion | No public comments/reviews | Check human rationale | Does not rule out private review | Accepted negative evidence | Interaction limit |

## 9. Full progressive manual investigation log

### Step 1 — Select and freeze the case

#### State before action

- **Question:** Which non-duplicate real PR should become S002?
- **Why it matters:** The case must expose product behavior not covered by S001 and retain enough evidence for a full runtime.
- **Working hypothesis:** An HTTPX 0.28 update affecting FastAPI/Starlette TestClient can expose API-removal and CI-alignment behavior.

#### Approach selection

- **Approach:** Screen public HTTPX 0.27.2 → 0.28.x PRs for target use, identity, lifecycle, and CI evidence.
- **Why now:** HTTPX 0.28 removed a constructor argument known to affect framework adapters.
- **Alternatives:** Broad Pydantic migrations, native dependency changes, another lockfile update.
- **Why not selected:** Pydantic cases were harder to bound; native cases remain later coverage; another lockfile case would duplicate S001.
- **Expected output:** One reproducible case with an actual target path and meaningful CI behavior.
- **Success would establish:** Case fitness and identity, not compatibility.
- **Stop/switch condition:** Reject candidates without a discoverable target path, closure relationship, or useful CI evidence.
- **Proposed/executed by:** AI assistant under Ali's instruction to perform a new non-duplicate full case.

#### Execution and output

Public PR search and bounded repository inspection identified PR #20. PR #17 explicitly states that it was superseded by #20. PR #20 has exact base/head identity, one changed manifest, target TestClient use, Docker CI, and a path-filtered Python workflow.

#### Interpretation, outcome, continuation

PR #20 was selected. The predecessor is lifecycle evidence, not a duplicate scenario. UpgradePilot must recognize superseded updates and follow the active successor while preserving history.

**Next action:** Classify HTTPX's actual target role before interpreting upstream changes.

### Step 2 — Classify declaration, use, and installation

#### State before action

- **Question:** Is HTTPX runtime, test-only, or unused?
- **Why it matters:** The answer determines relevance and the smallest credible check.
- **Working hypothesis:** HTTPX is used through FastAPI TestClient, not by application routes.

#### Approach selection

- **Approach:** Inspect requirements, application source, tests, Dockerfile, and README.
- **Why now:** Static repository evidence is the simplest credible role classifier.
- **Alternatives:** Execute import tracing or infer role from Dependabot labels.
- **Why not selected:** Untrusted execution is unnecessary; labels do not establish use.
- **Expected output:** Concrete declaration, functional-use, and deployment-installation paths.
- **Success would establish:** Static role at current depth, not complete dynamic absence.
- **Switch condition:** Require maintainer-owned runtime tracing only if static evidence remains ambiguous.

#### Execution and output

HTTPX is pinned directly in a shared requirements file. Application source does not directly import it. Tests import FastAPI TestClient and construct `TestClient(app)`. The Docker image installs the shared file, including HTTPX and test tools.

#### Interpretation, outcome, continuation

HTTPX is simultaneously:

- directly declared;
- functionally used through the test framework;
- not observed in application source;
- installed in the production image.

A single `runtime` or `development` label would be misleading. The principal behavioral question narrows to TestClient compatibility.

**Next action:** Identify which HTTPX 0.28 changes intersect that path.

### Step 3 — Identify target-relevant upstream changes

#### State before action

- **Question:** Which changes from HTTPX 0.27.2 to 0.28.1 matter here?
- **Why it matters:** Release notes include unrelated SSL, proxy, JSON, URL, and request changes.
- **Working hypothesis:** Removal of `app` is relevant; other listed changes have no observed path.

#### Approach selection

- **Approach:** Read tagged HTTPX changelog and package metadata, then map changes to target use.
- **Why now:** Tagged upstream source is stronger than the copied Dependabot body.
- **Alternatives:** Trust generated notes or inspect every upstream commit.
- **Why not selected:** Generated text needs corroboration; exhaustive commits add little after relevance is known.
- **Expected output:** Relevant/irrelevant change set and Python floor.
- **Success would establish:** Upstream claims, not target compatibility.

#### Execution and output

HTTPX 0.28.0 removed the deprecated `app` and `proxies` arguments. HTTPX 0.28.1 fixed a client-certificate SSL case. Its Python floor remains >=3.8.

#### Interpretation, outcome, continuation

The removed `app` argument is the only observed high-priority change for the TestClient path. No target source path was found for SSL certificates, proxies, JSON-body formatting, URL escaping, or SOCKS behavior. Release evidence generates the compatibility question; it does not answer it.

**Next action:** Determine whether the framework adapter still passes `app=`.

### Step 4 — Resolve the FastAPI/Starlette compatibility threshold

#### State before action

- **Question:** Does the target's resolved TestClient pass the removed argument?
- **Why it matters:** Old Starlette would fail at TestClient initialization; fixed Starlette would not.
- **Working hypothesis:** A then-current unpinned FastAPI likely resolves a fixed Starlette, but the exact environment is unavailable.

#### Approach selection

- **Approach:** Compare FastAPI 0.115.2 constraints and Starlette 0.36.3 versus 0.37.2 source.
- **Why now:** This establishes a primary-source compatibility threshold.
- **Alternatives:** Assume current latest packages, rely on secondary issue reports, or run a fresh resolver.
- **Why not selected:** Current latest violates the historical boundary; reports are weaker; a fresh resolver cannot reproduce the historical environment without a lock.
- **Expected output:** Compatible and incompatible branches plus the unresolved exact branch.
- **Success would establish:** Threshold and plausible compatibility, not target test success.
- **Stop/switch condition:** Exact environment or behavior requires a captured resolver output and targeted tests.

#### Execution and output

Starlette 0.36.3 calls `httpx.Client(app=self.app, ...)`. Starlette 0.37.2 no longer passes `app=`. FastAPI 0.115.2 requires Starlette >=0.37.2 and was available before PR #20.

#### Interpretation, outcome, continuation

A normal then-current FastAPI resolution was likely compatible, so a hard block is not justified. Exact target compatibility remains unproven because `fastapi[standard]` is unpinned and the historical resolution is unavailable.

The working finding changed from **possible direct break** to **likely compatibility with unresolved exact environment**. This supersession is preserved rather than silently rewriting the earlier concern.

**Next action:** Determine whether public CI closed the remaining behavioral uncertainty.

### Step 5 — Determine the authority of green CI

#### State before action

- **Question:** Did CI execute TestClient behavior under HTTPX 0.28.1?
- **Why it matters:** Green status should affect the decision only if the relevant path ran.
- **Working hypothesis:** Docker CI installs/builds but does not test; Python CI is skipped by path filter.

#### Approach selection

- **Approach:** Inspect workflow triggers, job commands, Dockerfile, head runs, jobs, and retained logs.
- **Why now:** CI authority depends on exact revision, trigger, and executed responsibility.
- **Alternatives:** Trust combined status, workflow name, or PR badge.
- **Why not selected:** Status color can hide skipped jobs and missing commands.
- **Expected output:** Checks actually run, relevant checks absent, and environment evidence retained or missing.
- **Success would establish:** CI proof scope, not behavior outside those commands.
- **Switch condition:** If logs are unavailable, use definitions/run summaries and preserve the limitation.

#### Execution and output

The Docker workflow ran and succeeded for head `391508...`. Its Dockerfile performs `pip install -r requirements.txt` and image construction, but no tests or app startup. The separate Python workflow runs `ruff check .` and `pytest --cov`, but its pull-request path filter excludes `requirements.txt`. No Python workflow run is attached to the head. Docker job-log retrieval returned HTTP 410.

#### Interpretation, outcome, continuation

The green check proves that one dependency resolution installed and the image built. It does not prove TestClient initialization or route tests. Public CI is therefore **green but incomplete/misleading if interpreted globally**.

The failed log-retrieval approach is preserved. Workflow-definition and run-summary analysis replaced it, but exact package resolution remains unavailable.

**Next action:** Construct the smallest check that closes the material uncertainty.

### Step 6 — Construct the bounded recommendation

#### State before action

- **Question:** What maintainer action is justified without overstating compatibility or CI?
- **Evidence state:** Likely compatible framework line; direct TestClient path; successful install/build; skipped Python tests; missing exact resolution.
- **Working hypothesis:** Run existing Python checks on the exact head while capturing resolved versions.

#### Approach selection

- **Approach:** Apply a sufficiency test: choose the smallest existing check that directly exercises the unresolved path.
- **Alternatives:** Merge immediately, block indefinitely, or run broad Kubernetes deployment tests first.
- **Why not selected:** Likelihood is not proof; indefinite block is disproportionate; broad deployment tests do not first target the changed interface.
- **Expected output:** Conditional recommendation and state transitions.
- **Success would establish:** Exact-head TestClient and route-test behavior under captured resolution.
- **Success would not establish:** Complete production safety or future unpinned resolutions.
- **Escalation condition:** Relevant failure changes outcome to investigate/block; unavailable or inconclusive checks retain targeted-check/defer state.

#### Execution and output

The smallest credible recovery action is a trusted exact-head environment that records resolved packages and runs:

```text
ruff check .
pytest --cov
```

#### Interpretation, outcome, continuation

The final outcome is `run targeted checks`.

- Passing exact-head checks permits `merge after normal review`.
- TestClient initialization failure requires inspecting resolved FastAPI/Starlette and either upgrading to a fixed framework stack or retaining HTTPX <0.28.
- Unavailable or inconclusive evidence retains the targeted-check/defer state.

The historical merge is recorded as a maintainer action, not used as proof that unconditional merge was evidence-grounded.

Further static investigation stopped because it cannot replace the missing dynamic proof.

## 10. Observation, interpretation, finding, and decision chains

| Chain | Observation | Interpretation | Finding state | Supporting/contradicting evidence | Permitted decision effect |
|---|---|---|---|---|---|
| C01 | PR changes one HTTPX pin | Exact transition established | Corroborated | E01–E05 | Start investigation only |
| C02 | Tests instantiate FastAPI TestClient; app has no observed HTTPX import | HTTPX is direct-declared, test-used, and production-installed | Supported with static limit | E04–E08 | Prioritize TestClient checks |
| C03 | HTTPX 0.28 removes `app` | Relevant adapter compatibility hazard | Corroborated upstream | E09 | Require framework-path analysis |
| C04 | Starlette 0.36.3 passes `app=`, 0.37.2 does not | Compatibility threshold established | Corroborated | E12–E13 | Old branch blocks; fixed branch continues |
| C05 | FastAPI 0.115.2 requires Starlette >=0.37.2 | Compatible framework line existed before PR | Supported with resolution limit | E11, E13 | Lowers risk; cannot replace test |
| C06 | Docker workflow succeeds and runs install/build only | Installation/image build passed; behavior untested | Corroborated | E14–E16 | Limited favorable effect |
| C07 | Python workflow excludes `requirements.txt` | Relevant test workflow was skipped | Corroborated | E17–E18 | Require targeted test |
| C08 | Logs expired and FastAPI is unpinned | Historical environment is not reproducible publicly | Corroborated limitation | E04, E19 | Report limitation/capture environment |
| C09 | PR was eventually merged | Maintainer accepted the update | Historical action only | E01 | No correctness authority |

Every decision reason traces to the evidence inventory and frozen identity. No final reason first appears only in the report.

## 11. Repository-specific relevance

### Relationship and path

HTTPX is:

- directly declared in `requirements.txt`;
- used functionally through `fastapi.testclient.TestClient`;
- not observed in application imports;
- installed into the production Docker image because test and runtime packages share one file;
- also included by FastAPI's standard extra, with the explicit pin constraining that framework dependency.

Observed path:

```text
tests/test_routes.py
→ fastapi.testclient.TestClient
→ starlette.testclient.TestClient
→ httpx.Client
```

### Relevant compatibility branch

- Starlette 0.36.3 passes the removed `app` argument and is incompatible with HTTPX 0.28.x.
- Starlette 0.37.2 removes that call.
- FastAPI 0.115.2 requires Starlette >=0.37.2.

A then-current resolution is therefore likely compatible, but no lockfile or retained install report establishes the exact historical versions.

### Platform constraints

- Docker uses Python 3.13.
- HTTPX 0.28.1 requires Python >=3.8.
- No Python-floor conflict exists.
- No native or platform-specific artifact branch is activated.

### What static evidence cannot prove

- exact resolved FastAPI/Starlette versions;
- successful TestClient initialization;
- passing route tests;
- private deployment behavior;
- future reproducibility under unpinned FastAPI.

## 12. Checks, comparisons, and observed behavior

| Check or comparison | Question | Inputs | Result | Demonstrates | Does not demonstrate | Limit |
|---|---|---|---|---|---|---|
| PR patch | What changed? | PR #20 | One HTTPX pin | Exact transition | Compatibility | High reliability |
| Repository-use inspection | Where does HTTPX matter? | Frozen source/tests | TestClient path; no app import observed | Static relevance | Complete dynamic absence | Static only |
| HTTPX changelog | What changed upstream? | 0.27.2→0.28.1 | `app` removed | Upstream behavior | Target impact | Requires join |
| Starlette source comparison | What is compatibility threshold? | 0.36.3/0.37.2 | Old passes `app=`, fixed does not | Cause/fix branch | Target resolution | Exact tags only |
| FastAPI metadata | Was compatible line available? | 0.115.2 | Requires fixed Starlette floor | Plausible compatibility | Exact install | Metadata only |
| Docker Actions run | Can resolution install/build? | Head SHA | Success | Installation/image build | Tests/runtime | Logs expired |
| Python workflow trigger analysis | Did tests run? | Workflow + changed path | Path filter excludes requirements | Why tests skipped | Private tests | Public CI only |
| Job-log retrieval | What versions installed? | Historical job | HTTP 410 | Evidence expired | Exact environment | Inaccessible |
| Targeted exact-head test | Does unresolved path work? | Trusted checkout | Not run by investigator | Would answer primary behavior question | Complete production safety | Maintainer action required |

## 13. Missing, inaccessible, and uncertain evidence

| Item or question | State | Reason | Decision consequence | Recovery |
|---|---|---|---|---|
| Exact FastAPI/Starlette resolution | Missing | No lockfile or retained install output | Compatibility remains likely, not proven | Capture resolver report or `pip freeze` |
| Python test run on PR head | Missing because path-filtered | Requirements path does not trigger workflow | Green CI cannot justify merge alone | Run workflow manually or include manifest path |
| Docker job logs | Inaccessible | HTTP 410 after retention | Cannot reconstruct historical environment | Re-run trusted build and retain artifact |
| Human merge rationale | Missing | No public review/comments | Do not infer reason | Ask maintainer only if history matters |
| Private/local tests | Unknown | Not publicly observable | Merge is not test evidence | Maintainer confirmation or new run |
| Hidden dynamic HTTPX use | Low-evidence unresolved | Static analysis only | Avoid absolute `test-only` claim | Runtime tracing if necessary |
| Security trigger | Not indicated | Ordinary Dependabot update; no advisory evidence | Do not label security update | Search only if policy requires |

The evidence does not materially contradict itself. The important distinction is that Docker CI and Python-test CI answer different questions.

## 14. Changed-evidence and failure variants

### Variant A — Old Starlette resolves

If the exact environment contains Starlette 0.36.3 or another version passing `app=` to HTTPX Client:

- TestClient is expected to fail during initialization;
- the likely-compatible finding is superseded;
- Docker build may remain green;
- outcome changes to `investigate/block` until the framework is upgraded or HTTPX remains <0.28.

### Variant B — Exact-head Python checks pass

If the maintainer captures resolved versions and the existing Ruff/pytest checks pass:

- missing behavior evidence becomes accepted passing evidence;
- outcome changes to `merge after normal review`;
- residual limits remain for production behavior and future unpinned resolution.

### Variant C — Manifest changes trigger Python CI

If `requirements.txt` is added to the Python workflow's pull-request paths:

- future dependency PRs automatically execute the relevant tests;
- green status gains authority only when the exact relevant job succeeds;
- this is a repository improvement opportunity, not permission for UpgradePilot to mutate workflows automatically.

## 15. Manual decision construction

- **Outcome:** `Run targeted checks`; merge only if exact-head Python checks pass under a captured dependency resolution.
- **Reasons:**
  1. The dependency reaches a real target path through TestClient.
  2. HTTPX 0.28 removed an argument used by older Starlette TestClient versions.
  3. A compatible FastAPI/Starlette line existed before the PR, making compatibility likely.
  4. Docker CI proves installation/image construction only.
  5. Python CI was skipped because the changed manifest is outside its path filter.
  6. Exact resolved framework versions and retained logs are unavailable.
- **Material limitations:** No public target test result, environment drift, unknown private checks.
- **Why stronger is unjustified:** Immediate merge would treat likely compatibility and unrelated green CI as proof.
- **Why weaker is unjustified:** Primary-source compatibility evidence and successful installation make indefinite block or abstention disproportionate.
- **Required next check:** In a trusted checkout of head `391508134b083b8f54461c0b576e8f7985c6ecb4`, capture resolved versions and run `ruff check .` plus `pytest --cov`.
- **Failure response:** If TestClient initialization fails, inspect FastAPI/Starlette and upgrade to a fixed stack or retain HTTPX <0.28.
- **Human judgment:** Review residual risk, dependency hygiene, and merge action.

## 16. Human-readable maintainer report

### HTTPX 0.27.2 → 0.28.1

**Recommendation: run the repository's Python checks on this exact PR head, then merge if they pass.**

The application does not directly import HTTPX, but the test suite constructs FastAPI's `TestClient`, which uses HTTPX through Starlette.

HTTPX 0.28 removed the deprecated `app` constructor argument. Older Starlette TestClient versions passed that argument and would fail. Starlette 0.37.2 removed the incompatible call, and FastAPI 0.115.2 requires Starlette 0.37.2 or newer. A normal then-current FastAPI resolution is therefore likely compatible.

The available green GitHub check does not confirm this behavior. It installs dependencies and builds the Docker image, but does not run tests. The separate Python workflow would run Ruff and `pytest --cov`, yet it does not trigger for `requirements.txt` changes. No Python test run is attached to the PR head, and historical build logs have expired, so the exact resolved FastAPI/Starlette versions are unavailable.

Run in a trusted exact-head environment while retaining the resolved package set:

```text
ruff check .
pytest --cov
```

If those checks pass, merge after normal review. If TestClient initialization fails, upgrade FastAPI/Starlette to a line using Starlette >=0.37.2 or keep HTTPX below 0.28 until compatibility is resolved.

This report does not claim complete production safety. HTTPX is functionally observed in the test-client path and is also installed in the production image because development and runtime dependencies are not separated.

## 17. Conceptual machine-consumable result

Illustrative and non-binding:

```yaml
case:
  repository: Aidan-Wallace/kubernetes-dashboard-token-api
  pull_request: 20
  base_sha: b065646e4b7b894964567950f9ad770b02c136c2
  head_sha: 391508134b083b8f54461c0b576e8f7985c6ecb4
  dependency:
    ecosystem: pypi
    name: httpx
    from: 0.27.2
    to: 0.28.1
  change_shape: manifest_only
invocation:
  minimum_locator:
    repository: Aidan-Wallace/kubernetes-dashboard-token-api
    pull_request: 20
dependency_relationships:
  - declared: direct
    functional_use: test_framework
    deployment_installation: production_image
    path:
      - tests/test_routes.py
      - fastapi.testclient.TestClient
      - starlette.testclient.TestClient
      - httpx.Client
findings:
  - id: F1
    state: corroborated
    statement: HTTPX 0.28 removed the app Client argument.
    evidence: [E09]
  - id: F2
    state: corroborated
    statement: Starlette 0.37.2 no longer passes app to HTTPX Client.
    evidence: [E12, E13]
  - id: F3
    state: supported_with_limit
    statement: A then-current FastAPI resolution is likely compatible.
    evidence: [E11, E13]
    limitation: exact target resolution unavailable
  - id: F4
    state: corroborated
    statement: Successful PR CI built the image but did not run Python tests.
    evidence: [E14, E15, E16, E17, E18]
limitations:
  - exact_resolved_fastapi_starlette_missing
  - python_test_run_missing
  - docker_logs_expired
  - private_maintainer_checks_unknown
decision:
  outcome: run_targeted_checks
  required_checks:
    - capture_resolved_versions
    - ruff_check
    - pytest_cov
  transition_on_pass: merge_after_normal_review
  transition_on_testclient_failure: investigate_or_block
user_follow_up:
  required: true
  actor: maintainer
  action: run trusted exact-head checks and review result
```

## 18. User interaction and follow-up flow

```text
PR locator or event
→ freeze base/head and version transition
→ classify declaration/use/installation
→ map target TestClient path
→ acquire HTTPX API-removal evidence
→ resolve FastAPI/Starlette compatibility threshold
→ map CI triggers and commands
→ observe Docker build success and skipped Python tests
→ report likely compatibility but insufficient behavior proof
→ maintainer runs exact-head checks
→ new evidence causes state transition:
   pass → merge after normal review
   relevant failure → investigate/block
   unavailable or inconclusive → remain targeted-check/defer
→ maintainer decides; action and evidence history persist
```

Persist across reruns:

- immutable case identity;
- evidence and retrieval states;
- prior findings and supersession history;
- workflow definitions and exact run identities;
- captured environment identity;
- user action and resulting state transition.

A rebase, new commit, changed resolution, or new check must produce comparison evidence rather than silently replacing the prior state.

## 19. Candidate methods by responsibility

| Responsibility | Manual method | Candidate automation | Simplest credible baseline | Strength | Failure modes | Downstream risk | Evidence before adoption |
|---|---|---|---|---|---|---|---|
| Case identity | PR metadata | GitHub API adapter | Freeze repository/PR/base/head | Deterministic | Moving head, permissions | Mixed evidence | Rebase/fork replay tests |
| Version transition | Patch inspection | Manifest-aware parser | Exact changed requirement | Traceable | Ranges/multiple files/groups | Wrong transition | Ecosystem variation corpus |
| Dependency role | Manifest/source/test/Docker join | Repository index plus graph | Declaration/use/install dimensions | Avoids one-label error | Dynamic imports/aliases | Wrong checks | Representative repositories |
| Upstream acquisition | Tagged changelog | Source resolver/extractor | Retrieve exact tag notes | Primary source | Missing/fragmented notes | Missed break | Cross-source evaluation |
| Target impact | Source comparison | Symbol/call-path analysis with bounded model assistance | Search removed symbol and adapters | Specific | Indirect/dynamic calls | False favorable result | Known-break benchmark |
| Compatibility threshold | Metadata/source join | Constraint solver and compatibility graph | Compare ranges/fixed version | Explainable | Unpinned/private constraints | Overconfidence | Captured resolver outputs |
| CI authority | Workflow/run inspection | Trigger/command coverage mapper | Map changed paths to jobs/commands | Detects misleading green | Reusable/dynamic workflows | False favorable CI | Diverse workflow corpus |
| Targeted checks | Sufficiency reasoning | Bounded check planner | Select existing relevant job | Low-cost | Tests lack coverage | False reassurance | Historical check outcomes |
| Decision/report | Evidence join | Deterministic decision control plus generated explanation | Conditional traceable result | Auditable | Missing policy/context | Overstatement | Cross-case calibration |

No method becomes product architecture through this case.

## 20. Data-flow and operating-model changes revealed

S002 adds or strengthens these responsibilities:

1. **Supersession resolution:** identify active successor PRs without losing predecessor history.
2. **Multi-axis dependency role:** separate declaration, functional use, and deployment installation.
3. **Adapter-aware compatibility:** direct dependency changes may reach the target through another dependency's adapter.
4. **Environment identity:** unpinned resolution must be captured as evidence.
5. **CI trigger coverage:** determine whether changed files triggered relevant workflows.
6. **CI command coverage:** determine what successful jobs actually executed.
7. **Skipped-check state:** relevant workflow not run is neither success nor failure.
8. **Expired-evidence state:** retention loss remains explicit and may require rerun.
9. **Targeted-check planning:** identify the smallest check that closes material uncertainty.
10. **Historical action separation:** merge state is user history, not validation proof.

Observed operating flow:

```text
PR #20
→ exact manifest transition
→ dependency role map
→ TestClient adapter path
→ HTTPX app-argument removal
→ Starlette compatibility threshold
→ workflow trigger and command map
→ install/build success + Python tests skipped
→ exact environment and behavior evidence missing
→ targeted exact-head checks
→ conditional merge or investigate/block
```

UpgradePilot may analyze CI sufficiency and propose checks. It must not execute untrusted code, edit workflows, or merge without authorization.

## 21. Scenario retrospective

- **New product insight:** A green PR can be real but decision-irrelevant when workflow path filters exclude the changed manifest from the test job.
- **Unnecessary stage:** Security-advisory investigation was not warranted after the ordinary-maintenance trigger and target path were established.
- **New responsibility:** Workflow trigger/command analysis and environment capture.
- **Useful method:** Join tagged upstream source, framework constraints, target usage, and exact workflow configuration.
- **Misleading method:** Treat workflow conclusion, Dependabot framing, or eventual merge as sufficient evidence.
- **Conditional responsibility:** Framework-adapter comparison is needed when the target reaches a dependency through another library.
- **Outside product:** Unauthorised execution, automatic workflow mutation, and merge authority.
- **Plan implication:** `run_targeted_checks` fits the current bounded decision vocabulary, but later outputs must encode exact check rationale, CI insufficiency, and transition conditions.
- **Best next contrast:** A real failing test workflow requiring failure attribution.
- **Stop quality:** Correct. Additional static evidence cannot replace exact-head tests.
- **Remaining unresolved:** Historical resolved package set and private maintainer verification.
- **Ali capability evidence:** Not assessed. Ali directed the task but did not independently execute or verify the technical steps.
- **AI assistance:** Evidence selection, compatibility reasoning, decision construction, and drafting were AI-controlled under Ali's direction.

## 22. Coverage update

S002 covers:

- direct declaration with test-framework use and production-image installation;
- manifest-only pin change;
- upstream API removal;
- framework adapter compatibility threshold;
- Python compatibility without conflict;
- successful install/build CI but skipped decision-relevant tests;
- missing exact dependency resolution and expired logs;
- ordinary maintenance update;
- `run targeted checks` decision;
- required maintainer follow-up;
- stable historical merged PR with insufficient public behavior proof;
- superseded predecessor update.

Highest-value next contrast:

> A dependency update with an actual failing test workflow where UpgradePilot must distinguish update-caused failure from pre-existing, flaky, environmental, or unrelated failure.

## 23. Progressive-record audit

- [x] Every material investigation step has a stated question and reason.
- [x] Every material approach has a selection rationale.
- [x] Material alternatives and reasons for not pursuing them are visible.
- [x] Expected outputs and stop/switch/escalation conditions are recorded.
- [x] Raw outputs/direct observations are separated from interpretation.
- [x] Step outputs are separated from outcomes.
- [x] Findings trace to preserved evidence and exact identity.
- [x] Recommendation reasons trace to findings and limitations.
- [x] Each next action traces to the prior outcome.
- [x] Failed or abandoned paths remain visible, including rejected candidates and expired log retrieval.
- [x] Superseded interpretation remains visible: possible hard break → likely compatibility with unresolved environment.
- [x] Human and AI contributions are attributed.
- [x] Missing, inaccessible, and uncertain evidence remains explicit.
- [x] No material decision reason first appears only in the final report.
- [x] Routine lookups are grouped.
- [x] Investigation stopped where only maintainer-owned dynamic proof can resolve the case.

Process note: candidate screening preceded the formal identity freeze. This record preserves that boundary rather than presenting a fabricated perfectly linear history.

## 24. Completion statement

S002 is complete because the full intended manual runtime has been executed from real update event through identity, invocation, evidence acquisition, repository-specific relevance, upstream/framework compatibility analysis, CI sufficiency analysis, missing-evidence handling, bounded decision, maintainer report, conceptual machine result, user flow, method assessment, product-model changes, retrospective, and coverage update.

Produced outputs:

- one complete progressive `CASE.md`;
- evidence inventory and reasoning chains;
- changed-evidence variants;
- human-readable maintainer report;
- conceptual machine-consumable result;
- candidate-method assessment;
- operating-model and coverage changes.

Unavailable evidence:

- exact historical FastAPI/Starlette resolution;
- expired Docker job logs;
- public exact-head Python test results;
- private maintainer checks and reasoning.

Supported conclusions:

- the update reaches target tests through FastAPI/Starlette TestClient;
- HTTPX 0.28 removes an argument used by old Starlette TestClient;
- a compatible Starlette/FastAPI line existed before the PR;
- Docker install/build succeeded;
- decision-relevant Python tests did not publicly run because of workflow path filtering;
- targeted exact-head tests are the proportionate next action.

Unsupported conclusions:

- that the historical exact environment was definitely compatible;
- that the eventual merge proves correctness;
- that the green Docker workflow proves TestClient behavior;
- that the update is completely safe in production;
- that Ali independently owns or verified this investigation.

**Single most important product-model change:** CI evidence must include trigger coverage and executed-command/responsibility coverage; a green status cannot receive global decision authority.

**Most valuable next scenario:** an actual failing dependency-update workflow requiring causal attribution among update-caused, pre-existing, flaky, environmental, and unrelated failures.
