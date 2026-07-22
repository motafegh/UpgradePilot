# S002 — Kubernetes Dashboard Token API: HTTPX 0.27.2 → 0.28.1

> **Record status:** Active progressive primary record. This case is being completed in the same investigation session. Candidate screening occurred before the case was frozen and is recorded separately from the active scenario steps rather than rewritten as if the case had been selected earlier.

## Scenario identity

- **Scenario ID:** S002
- **Status:** active
- **Repository:** `Aidan-Wallace/kubernetes-dashboard-token-api`
- **Dependency update:** `httpx==0.27.2` → `httpx==0.28.1`
- **Public change reference:** `https://github.com/Aidan-Wallace/kubernetes-dashboard-token-api/pull/20`
- **Base revision:** `b065646e4b7b894964567950f9ad770b02c136c2`
- **Head revision:** `391508134b083b8f54461c0b576e8f7985c6ecb4`
- **Merge commit:** `45bf6d64c91504a902b22539afa746a473fbae5d`
- **Investigated time boundary:** PR creation on 2024-12-09 through merge on 2025-06-28, with historical evidence observed on 2026-07-22
- **Date investigated:** 2026-07-22
- **Investigators:** AI assistant under Ali's direction; Ali review and independent verification are not yet claimed

## Live case state

- **Current phase:** Evidence verification and final decision construction
- **Current primary question:** Does the public evidence justify merging HTTPX 0.28.1, and what does the green CI actually prove?
- **Current working hypothesis:** The update is probably compatible because the target resolves a post-fix FastAPI/Starlette stack, but the relevant Python test workflow did not run, so a targeted test is still required before an evidence-grounded merge recommendation.
- **Last material finding:** The only preserved successful PR workflow built the Docker image; the Python workflow excludes `requirements.txt` changes and therefore did not execute the repository's `TestClient` tests.
- **Current recommendation state:** Provisional `run targeted checks`; merge only after the exact-head Python tests pass.
- **Current material limitations:** Exact resolved FastAPI/Starlette versions and expired job logs are unavailable; no public test run is attached to the PR head.
- **Next selected action:** Verify the upstream compatibility chain and audit recommendation-to-evidence traceability.
- **Reason for next action:** The removed HTTPX `app` argument matters only if the resolved Starlette `TestClient` still passes it.
- **Last updated:** 2026-07-22

## Pre-selection candidate screening

S001 already covered a transitive, lockfile-only, pure-Python documentation dependency with complete upstream information and green relevant CI. The highest-value contrast in `SCENARIO_COVERAGE.md` was a direct dependency with an API or behavior change and failing, conflicting, or misleading CI.

Several HTTPX 0.27.2 → 0.28.x Dependabot PRs were screened. PR #20 was selected because it provides all of the following:

- a direct manifest pin rather than a transitive lockfile change;
- a real upstream API removal (`httpx.Client(app=...)`);
- target tests that instantiate FastAPI's `TestClient`;
- a superseded predecessor PR (#17), exposing update succession;
- a successful Docker workflow;
- a separate Python test workflow whose path filter excludes the changed manifest;
- a historical merged outcome but no preserved public test proof.

Candidate screening is not treated as evidence that PR #20 was already selected. The active case begins with the identity freeze below.

## 1. Why this case was selected

This case tests product behavior absent from S001:

- direct declared dependency rather than lock-derived transitive dependency;
- manifest-only change rather than lockfile-only change;
- upstream API removal rather than security-advisory interpretation;
- repository tests directly traverse the dependency through a framework test client;
- green CI exists but does not exercise the decision-relevant path;
- the exact environment can drift because `fastapi[standard]` is unpinned;
- the earlier 0.28.0 PR was automatically superseded by 0.28.1;
- the final public repository action was merge, but the available evidence may justify only a conditional merge.

Known limits:

- the public workflow logs have expired and return HTTP 410;
- the exact resolved FastAPI and Starlette versions used by the successful Docker build are not preserved in accessible evidence;
- executing the untrusted public repository is outside this manual investigation; a maintainer-owned targeted test remains follow-up work;
- no human review comments explain the merge decision.

The case remains worth continuing because those limits themselves reveal required UpgradePilot behavior around CI-path alignment, environment capture, and conditional recommendations.

## 2. Initial real-world event

Dependabot opened PR #20 on 2024-12-09 to replace the direct pin:

```text
httpx==0.27.2
→
httpx==0.28.1
```

The PR followed PR #17, which proposed 0.28.0 and was closed by Dependabot with the explicit note `Superseded by #20.`

The maintainer saw a one-line requirements change, generated upstream release notes, a successful Docker workflow, and no public discussion. PR #20 remained open until it was merged on 2025-06-28.

Before UpgradePilot begins, the repository contains:

- a FastAPI application;
- a direct HTTPX pin in `requirements.txt`;
- tests using `fastapi.testclient.TestClient`;
- a Docker workflow triggered by all pull requests;
- a Python test workflow triggered only when application, static, template, or test files change.

## 3. Intended invocation

The smallest credible invocation is a repository and pull-request locator. Exact identity should be discovered and frozen before evidence is joined.

| Item | Value | Supplied by | Purpose | Requirement | Missing/wrong consequence |
|---|---|---|---|---|---|
| Repository locator | `Aidan-Wallace/kubernetes-dashboard-token-api` | Maintainer, GitHub event, or caller | Locate target repository | Required unless encoded in an authenticated event | Wrong repository invalidates all relevance analysis |
| Pull-request locator | `20` or PR URL | Maintainer, GitHub event, or caller | Locate proposed change | Required | Cannot identify exact change |
| Event/auth context | Not preserved in historical case | GitHub installation or runtime | Permit acquisition and identify actor/context | Conditional | Public read-only investigation remains possible; private/offline use may fail |
| Maintainer policy | Not supplied | Maintainer/project configuration | Apply local merge/check policy | Optional for this case, required for policy-specific automation | Product must provide evidence-grounded generic action rather than claim policy compliance |

Not invocation inputs:

- HTTPX release notes;
- target source and tests;
- workflow definitions and results;
- FastAPI/Starlette compatibility data;
- predecessor PR #17;
- the final merge outcome.

Those are acquired evidence.

## 4. Case identity and reproducibility boundary

Authoritative case identity:

- repository: `Aidan-Wallace/kubernetes-dashboard-token-api`;
- PR: `#20`;
- base branch: `main`;
- base SHA: `b065646e4b7b894964567950f9ad770b02c136c2`;
- head branch: `dependabot/pip/httpx-0.28.1`;
- head SHA: `391508134b083b8f54461c0b576e8f7985c6ecb4`;
- dependency: `httpx`;
- old version: `0.27.2`;
- new version: `0.28.1`;
- changed path: `requirements.txt`;
- merge commit: `45bf6d64c91504a902b22539afa746a473fbae5d`.

Reproducible:

- PR metadata and patch;
- exact base/head repository files;
- workflow definitions;
- target test code;
- upstream tagged HTTPX and Starlette source;
- available workflow-run summary.

Not exactly reproducible from current public evidence:

- resolved package set used by the historical Docker build;
- complete workflow logs;
- maintainer's private reasoning;
- whether tests were run outside GitHub;
- runtime behavior in the maintainer's deployment.

Later repository state must not be used as if it belonged to the frozen base/head without explicit labeling.

## 5. Actors and systems

| Actor or system | Role | Material data | Authority and limits | Interaction with UpgradePilot |
|---|---|---|---|---|
| Dependabot | Update producer | PR, version transition, generated notes, predecessor closure | Authoritative for proposal mechanics; generated notes are attributed upstream claims, not repository-specific proof | Starts or exposes the case |
| GitHub Pull Requests | Change store and identity boundary | Base/head SHAs, patch, timestamps, merge state | Strong case identity; does not explain correctness | Primary invocation/acquisition surface |
| Target repository | Product context | Requirements, application code, tests, workflows, Dockerfile | Authoritative for declared code and CI configuration at frozen revisions | Main relevance source |
| HTTPX project | Upstream dependency producer | Changelog, package metadata, tagged source | Authoritative for declared upstream changes; cannot establish target impact alone | Upstream evidence source |
| FastAPI project | Framework dependency producer | `standard` extra and Starlette requirement | Authoritative for declared dependency constraints at a tag; exact target resolution remains unknown | Compatibility bridge |
| Starlette project | TestClient implementation owner | Old and fixed `TestClient` behavior | Authoritative for source behavior at tagged versions | Determines whether HTTPX's removed argument is used |
| GitHub Actions | CI executor | Docker workflow success; absent Python workflow run | Authoritative for jobs actually run; a green result proves only workflow-defined behavior | Check evidence source |
| Docker/`pip` resolver | Build and dependency acquisition | Install/build result | Successful build proves resolution and image construction, not tests or runtime correctness | Conditional evidence producer |
| Maintainer | Decision maker | Merge action, possible private checks | Final authority to merge; merge is not proof that the update was safe | Consumes report and performs targeted check |
| Ali | Project owner/reviewer | Challenges product model and final artifact | No independent technical execution claimed in this case yet | Reviews UpgradePilot simulation |
| AI assistant | Manual investigator and recorder | Evidence acquisition, interpretation, report | Must preserve sources, uncertainty, and assistance; cannot run untrusted target code | Acts as manual UpgradePilot system |

## 6. Initial questions for the maintainer decision

| Question | Why it matters | Likely evidence | Consequence if unresolved |
|---|---|---|---|
| What exactly changed? | Bounds the case | PR identity and patch | No valid investigation |
| Is HTTPX runtime, test, or unused? | Determines impact surface | Manifest, imports, tests, Dockerfile | Cannot prioritize checks or claims |
| Which HTTPX 0.28 changes intersect target usage? | Release contains multiple unrelated changes | Changelog plus target code | Generic release notes may overstate risk |
| Does FastAPI's resolved Starlette still pass `app=` to HTTPX? | HTTPX 0.28 removed that constructor argument | FastAPI constraints, Starlette tagged source | TestClient may fail at collection/initialization |
| What did CI actually execute? | Green status may be misleading | Workflow definitions and run mapping | Cannot give green CI decision authority |
| Is the exact dependency environment reproducible? | Unpinned FastAPI can change compatibility | Lockfile/constraints/logs | Historical success may not replay |
| What action is justified now? | Product must support a maintainer decision | Joined findings and limitations | Must target checks or abstain rather than guess |

## 7. Evidence discovery map

| Potential source | Question | Expected authority | Access path | Acquired? |
|---|---|---|---|---|
| PR #20 metadata and patch | Identity and exact change | High | GitHub PR API | Yes |
| PR #17 and comments | Why predecessor closed | High for closure relationship | GitHub PR API/comments | Yes |
| Base/head `requirements.txt` | Direct declaration and versions | High | GitHub contents at SHAs | Yes |
| Target source imports | Runtime use | High for static usage | GitHub code/contents | Yes |
| Target tests | Test-path use | High | GitHub contents | Yes |
| Dockerfile | What image build executes | High | GitHub contents | Yes |
| GitHub workflow definitions | Check scope and triggers | High | GitHub contents | Yes |
| Workflow run/jobs/logs | Actual checks and outputs | High when available | GitHub Actions API | Summary/jobs yes; logs expired |
| HTTPX changelog and metadata | Upstream behavior and Python floor | High for upstream claims | Tagged GitHub files | Yes |
| FastAPI tagged metadata | Starlette compatibility floor | High for declared constraints | Tagged GitHub file | Yes |
| Starlette old/fixed source | Whether `app=` is passed | High for source behavior | Tagged GitHub file | Yes |
| Security advisories | Whether update is security-driven | High if applicable | Advisory sources | Not pursued; no security trigger found |
| Dynamic test execution | Actual target behavior | Highest direct behavior evidence | Maintainer-controlled CI/local environment | Not performed by investigator |

## 8. Evidence inventory

| ID | Evidence | Origin and identity | Direct observation | Purpose | Authority/limits | State | Downstream use |
|---|---|---|---|---|---|---|---|
| E01 | PR #20 metadata | GitHub PR, final historical state | Opened 2024-12-09; merged 2025-06-28; exact base/head/merge identity available | Freeze case | Strong identity; merge does not prove correctness | Accepted | Case identity and user-flow outcome |
| E02 | PR #20 patch | `requirements.txt` at PR | One line changes HTTPX 0.27.2 to 0.28.1 | Define proposal | Strong mechanical change evidence | Accepted | Version transition |
| E03 | PR #17 comment | Dependabot comment on predecessor | `Superseded by #20.` | Explain succession | Establishes closure reason for #17 only | Accepted | Update lifecycle model |
| E04 | Base requirements | Base SHA | `fastapi[standard]` unpinned; HTTPX 0.27.2; test/lint packages in same file | Classify dependencies/environment | Does not preserve resolved transitive versions | Accepted | Role and reproducibility findings |
| E05 | Head requirements | Head SHA | HTTPX 0.28.1; FastAPI remains unpinned | Confirm head state | Same resolution limitation | Accepted | Final proposed environment |
| E06 | Target tests | Base/head `tests/test_routes.py` | Imports `fastapi.testclient.TestClient` and constructs `TestClient(app)`; five route tests | Identify direct behavioral path | Does not itself prove pass/fail | Accepted | Targeted-check requirement |
| E07 | Target application source | `app/main.py`, `app/router/routes.py` | Application imports FastAPI but not HTTPX; routes do not use HTTPX | Separate runtime app from test path | Static search may miss dynamic use, but repository search found no source HTTPX use | Accepted | Dependency role finding |
| E08 | Target README | Base SHA | Project is a token UI/API; TODO says pytest and ruff should not be installed in container | Understand product and dependency hygiene | Documentation may be stale | Accepted | Production-installed/test-use distinction |
| E09 | HTTPX changelog | tag 0.28.1 | 0.28.0 removed deprecated `app` and `proxies`; 0.28.1 fixes SSL client-cert case | Identify upstream changes | Upstream claim; target relevance requires joining | Accepted | Compatibility question |
| E10 | HTTPX metadata | tag 0.28.1 | Requires Python >=3.8 | Check Python compatibility | Does not prove dependency-set compatibility | Accepted | Python-floor finding |
| E11 | FastAPI 0.115.2 metadata | tag 0.115.2 | Requires Starlette >=0.37.2,<0.41.0; `standard` includes HTTPX >=0.23.0 | Establish known compatible framework floor available before PR | Exact target resolution is not preserved | Accepted with limitation | Compatibility support |
| E12 | Starlette 0.36.3 source | tag 0.36.3 | `TestClient` passes `app=self.app` to `httpx.Client` | Define incompatible branch | Only applies if that version or equivalent resolved | Accepted | Failure variant |
| E13 | Starlette 0.37.2 source/release | tag 0.37.2 | `TestClient` uses transport without passing `app=`; release notes identify fix | Define compatible branch | Exact target resolution unknown | Accepted | Likely compatibility finding |
| E14 | Docker workflow | Head SHA | Runs on any PR and builds Docker image | Determine green-check scope | No tests defined | Accepted | CI authority limit |
| E15 | Dockerfile | Head SHA | `pip install -r requirements.txt`; no test command | Explain build proof | Build does not import or exercise TestClient | Accepted | CI authority limit |
| E16 | Workflow run | Head SHA, run 15940060582 | Docker job completed successfully | Prove install/image build succeeded | Does not prove tests or runtime behavior | Accepted | Installation evidence |
| E17 | Python workflow | Head SHA | Runs lint and `pytest --cov`, but path filter excludes `requirements.txt` | Determine missing relevant check | Strong workflow-definition evidence | Accepted | Misleading-green finding |
| E18 | Python workflow run on head | GitHub Actions lookup | No run returned for head | Confirm relevant workflow absent | API coverage may omit deleted/retention-limited data, but path filter independently explains absence | Missing/expected absent | Targeted-check requirement |
| E19 | Docker job logs | GitHub Actions job 44966848674 | Retrieval returns HTTP 410 | Preserve expired evidence | Exact resolved package versions and install output unavailable | Inaccessible | Reproducibility limitation |
| E20 | PR discussion | PR #20 comments | No comments | Check human rationale | Absence does not prove no private review | Accepted negative evidence | Human-interaction limitation |

## 9. Full progressive manual investigation log

### Investigation step 1 — Freeze the selected case and successor relationship

#### A. State before action

- **Current question or uncertainty:** Which non-duplicate real PR should become S002?
- **Why this matters:** The case must materially contrast with S001 and have reproducible evidence.
- **Current evidence:** S001 coverage gaps; several HTTPX 0.28 Dependabot PR candidates.
- **Current working hypothesis:** A target that uses FastAPI/Starlette TestClient can expose real API-removal and CI-alignment behavior.
- **Current recommendation or decision effect:** None; candidate not yet selected.
- **Current product-model implication:** Case selection must consider evidence availability, not only technical interest.

#### B. Approach selection

- **Selected approach:** Screen public HTTPX 0.27.2 → 0.28.x PRs for target usage, exact identity, review history, and CI evidence.
- **Why selected now:** HTTPX 0.28 removed an API known to affect framework test clients.
- **Alternatives considered:** Pydantic v1→v2 major updates; native dependency updates; another green lockfile bump.
- **Why alternatives were not selected now:** Pydantic migrations were broader and harder to bound; native cases remain valuable later; another lockfile case would duplicate S001.
- **Required inputs and assumptions:** Public PR/repository access.
- **Expected useful output:** One case with a concrete target path and preserved CI behavior.
- **What success would establish:** Case fitness and identity.
- **What success would not establish:** Compatibility or recommendation.
- **Stop, switch, or escalation condition:** Reject candidates whose closure reason, source path, or CI evidence cannot be established.
- **Approach proposed by:** AI assistant from S001 coverage needs.
- **Approach selected or approved by:** Ali authorized a new non-duplicate full case; AI selected the bounded candidate.

#### C. Execution

- **Performed by:** AI assistant.
- **Actions taken:** Searched public PRs; inspected candidate metadata; followed PR #17's supersession to PR #20; inspected changed path and target tests.
- **Tools, commands, APIs, or sources:** GitHub PR search, PR metadata, comments, changed-file listing, repository contents.
- **Identity, revision, and time boundary:** Historical PRs #17 and #20.
- **Reads, writes, external effects, or risk:** Public read-only access; no target mutation or code execution.
- **Execution problems or deviations:** Some candidates had no workflow evidence and were rejected.

#### D. Output and observations

- **Raw output or preserved reference:** PR #20 exact base/head and merged state; PR #17 comment `Superseded by #20.`
- **Direct observations:** PR #20 changes one requirements line and has a successor relationship from #17.
- **Missing, invalid, stale, conflicting, or inaccessible output:** No human explanation for merge.
- **What the output demonstrates:** A reproducible dependency-update lifecycle and exact event.
- **What the output does not demonstrate:** Update safety.

#### E. Interpretation and verification

- **Interpretation:** PR #20 is the correct event; #17 is predecessor evidence rather than a separate scenario.
- **Reasoning summary:** Selecting #20 avoids duplicating the same version family while preserving lifecycle context and final action.
- **Alternative explanations:** #17 may have had independent issues, but its explicit closure reason is supersession.
- **Supporting evidence:** PR metadata and Dependabot comment.
- **Contradicting evidence:** None.
- **Uncertainty and limitations:** Private maintainer context absent.
- **Interpreted by:** AI assistant.
- **Verification or challenge performed by:** Cross-check of #17 and #20 identities.

#### F. Outcome

- **Question answered or current state:** S002 selected and frozen.
- **Step output:** Exact case identity and predecessor link.
- **Step outcome:** Investigation can proceed without mixing 0.28.0 and 0.28.1 as separate target events.
- **Finding created, changed, rejected, or left unresolved:** Created finding that update succession is a product state.
- **Effect on recommendation:** None yet.
- **Effect on product understanding:** UpgradePilot must detect superseded update proposals and follow the active successor.
- **What remains unchanged:** Compatibility and CI authority unresolved.

#### G. Progressive continuation

- **Next selected action:** Classify dependency role and target usage.
- **Why it follows from this outcome:** Upstream changes only matter through an actual target path.
- **Other possible actions not pursued now:** Read every upstream commit before knowing relevance.
- **Current approach status:** complete.
- **If replaced, replacement approach and reason:** Not applicable.

### Investigation step 2 — Classify the changed dependency and target path

#### A. State before action

- **Current question or uncertainty:** Is HTTPX a runtime dependency, test dependency, or unused direct pin?
- **Why this matters:** Determines impact and targeted checks.
- **Current evidence:** One-line requirements change.
- **Current working hypothesis:** HTTPX is used through FastAPI's TestClient rather than application runtime code.
- **Current recommendation or decision effect:** No decision effect until usage is established.
- **Current product-model implication:** Declared dependency role cannot be inferred from one shared requirements file.

#### B. Approach selection

- **Selected approach:** Inspect manifest, repository HTTPX references, application code, tests, Dockerfile, and README.
- **Why selected now:** Static repository evidence is the simplest credible role classifier.
- **Alternatives considered:** Execute import tracing or tests; infer role from Dependabot title.
- **Why alternatives were not selected now:** Execution of untrusted code is unnecessary and unauthorized; title does not encode actual use.
- **Required inputs and assumptions:** Frozen base/head files and repository search.
- **Expected useful output:** Concrete usage path and install context.
- **What success would establish:** Static dependency role at current depth.
- **What success would not establish:** Runtime behavior or complete absence of dynamic use.
- **Stop, switch, or escalation condition:** If static references are ambiguous, require dynamic tracing by maintainer.
- **Approach proposed by:** AI assistant.
- **Approach selected or approved by:** AI assistant under active plan.

#### C. Execution

- **Performed by:** AI assistant.
- **Actions taken:** Compared base/head requirements; searched for HTTPX and TestClient; inspected tests, app source, Dockerfile, and README.
- **Tools, commands, APIs, or sources:** GitHub contents and code search.
- **Identity, revision, and time boundary:** Base/head SHAs.
- **Reads, writes, external effects, or risk:** Public read-only.
- **Execution problems or deviations:** Repository search found HTTPX only in requirements; direct file inspection supplied the meaningful path.

#### D. Output and observations

- **Raw output or preserved reference:** E04–E08.
- **Direct observations:** HTTPX is pinned in a shared requirements file; application files do not import it; tests instantiate `fastapi.testclient.TestClient`; Docker image installs all test packages.
- **Missing, invalid, stale, conflicting, or inaccessible output:** No separate production/test dependency groups or lockfile.
- **What the output demonstrates:** Direct declaration, test-path use, and production-image installation.
- **What the output does not demonstrate:** No hidden dynamic HTTPX use; tests pass.

#### E. Interpretation and verification

- **Interpretation:** HTTPX is a direct declared dependency with observed test-only functional use, while also being installed into production because dependency groups are not separated.
- **Reasoning summary:** `TestClient` depends on HTTPX; app routes do not. The shared file collapses development and production roles.
- **Alternative explanations:** FastAPI's standard extra also depends on HTTPX; the explicit pin may intentionally control that transitive test client version.
- **Supporting evidence:** Tests, FastAPI metadata, requirements, Dockerfile, README TODO.
- **Contradicting evidence:** None.
- **Uncertainty and limitations:** Exact production imports not dynamically traced.
- **Interpreted by:** AI assistant.
- **Verification or challenge performed by:** Joined manifest, source, test, and packaging evidence.

#### F. Outcome

- **Question answered or current state:** Dependency role classified at useful static depth.
- **Step output:** Usage and installation map.
- **Step outcome:** Main behavioral risk narrows to test-client compatibility; production app behavior is not directly changed by HTTPX source usage.
- **Finding created, changed, rejected, or left unresolved:** Created direct-declared/test-use/production-installed finding.
- **Effect on recommendation:** Relevant tests become mandatory before merge; broad runtime testing is lower priority.
- **Effect on product understanding:** Role is multi-dimensional: declaration, functional use, and deployment installation can differ.
- **What remains unchanged:** Exact compatibility unresolved.

#### G. Progressive continuation

- **Next selected action:** Inspect the upstream HTTPX change and framework compatibility chain.
- **Why it follows from this outcome:** The target path is through TestClient, so removed constructor parameters are decision-relevant.
- **Other possible actions not pursued now:** Security advisory search and exhaustive HTTPX commit review.
- **Current approach status:** complete.
- **If replaced, replacement approach and reason:** Not applicable.

### Investigation step 3 — Identify decision-relevant upstream changes

#### A. State before action

- **Current question or uncertainty:** Which HTTPX 0.28.1 changes can affect this repository?
- **Why this matters:** Release notes contain multiple changes with different target relevance.
- **Current evidence:** Target uses TestClient; no direct app HTTPX API calls.
- **Current working hypothesis:** Removal of `app` is relevant; SSL, proxies, JSON formatting, and URL escaping are probably not.
- **Current recommendation or decision effect:** Potential compatibility block until framework layer is checked.
- **Current product-model implication:** Upstream change extraction must be filtered by target path.

#### B. Approach selection

- **Selected approach:** Read tagged HTTPX changelog and package metadata, then map each material change to target usage.
- **Why selected now:** Official tagged source is the strongest bounded upstream evidence.
- **Alternatives considered:** Dependabot-generated copy only; inspect every upstream commit.
- **Why alternatives were not selected now:** Generated copy should be corroborated; exhaustive commit review adds little after target path is known.
- **Required inputs and assumptions:** HTTPX 0.28.1 tag corresponds to proposed version.
- **Expected useful output:** Relevant and irrelevant upstream change set.
- **What success would establish:** Attributed upstream changes and Python floor.
- **What success would not establish:** Downstream compatibility.
- **Stop, switch, or escalation condition:** Inspect implementation commits only if changelog meaning remains ambiguous.
- **Approach proposed by:** AI assistant.
- **Approach selected or approved by:** AI assistant under active plan.

#### C. Execution

- **Performed by:** AI assistant.
- **Actions taken:** Retrieved `CHANGELOG.md` and `pyproject.toml` at tag 0.28.1.
- **Tools, commands, APIs, or sources:** GitHub tagged-file retrieval.
- **Identity, revision, and time boundary:** HTTPX tag `0.28.1`.
- **Reads, writes, external effects, or risk:** Public read-only.
- **Execution problems or deviations:** None.

#### D. Output and observations

- **Raw output or preserved reference:** E09–E10.
- **Direct observations:** 0.28.0 removed `app` and `proxies`; 0.28.1 fixes an SSL client-certificate case; Python requirement remains >=3.8.
- **Missing, invalid, stale, conflicting, or inaccessible output:** No target-specific statement.
- **What the output demonstrates:** Upstream behavior and compatibility claims.
- **What the output does not demonstrate:** Whether target's framework calls removed APIs.

#### E. Interpretation and verification

- **Interpretation:** `app` removal is the only observed high-priority change for the TestClient path. SSL/client-cert, proxies, JSON representation, URL escaping, and socks changes have no observed target path.
- **Reasoning summary:** The target's tests construct a framework TestClient, not direct SSL/proxy clients.
- **Alternative explanations:** Hidden framework internals may touch other HTTPX behavior; no evidence suggests it.
- **Supporting evidence:** Target source and tests.
- **Contradicting evidence:** None.
- **Uncertainty and limitations:** Static relevance only.
- **Interpreted by:** AI assistant.
- **Verification or challenge performed by:** Cross-source target/upstream mapping.

#### F. Outcome

- **Question answered or current state:** Upstream change set narrowed.
- **Step output:** Relevant change: removed `app`; Python floor compatible with Docker Python 3.13.
- **Step outcome:** Compatibility analysis can focus on Starlette TestClient implementation.
- **Finding created, changed, rejected, or left unresolved:** Created targeted API-removal finding; marked other changes not currently applicable.
- **Effect on recommendation:** Maintains targeted-check requirement; no security/block reason added.
- **Effect on product understanding:** Release-level evidence should support question generation, not direct recommendations.
- **What remains unchanged:** Exact framework resolution unresolved.

#### G. Progressive continuation

- **Next selected action:** Compare old and fixed Starlette TestClient behavior and FastAPI constraints.
- **Why it follows from this outcome:** That bridge determines whether `app` removal is actually reached.
- **Other possible actions not pursued now:** Inspect target routes for SSL or proxy code already ruled out by source search.
- **Current approach status:** complete.
- **If replaced, replacement approach and reason:** Not applicable.

### Investigation step 4 — Resolve the FastAPI/Starlette compatibility branch

#### A. State before action

- **Current question or uncertainty:** Does the target's FastAPI/Starlette stack pass the removed `app` argument?
- **Why this matters:** If yes, `TestClient(app)` fails immediately with HTTPX 0.28.x; if no, the primary compatibility concern is removed.
- **Current evidence:** Unpinned `fastapi[standard]`; target tests use TestClient.
- **Current working hypothesis:** A post-0.37.2 Starlette stack is likely, but exact resolution is not preserved.
- **Current recommendation or decision effect:** Potential block becomes likely-compatible-but-unproven if post-fix stack is established.
- **Current product-model implication:** Compatibility depends on a multi-package version join, not one release note.

#### B. Approach selection

- **Selected approach:** Inspect FastAPI 0.115.2 requirements and Starlette 0.36.3 versus 0.37.2 TestClient source.
- **Why selected now:** It establishes the exact compatibility threshold with primary source.
- **Alternatives considered:** Assume current latest packages; rely on community issue reports; execute dependency resolver.
- **Why alternatives were not selected now:** Current latest would violate historical boundary; reports are secondary; execution is unnecessary and would not recreate the historical environment without a lock.
- **Required inputs and assumptions:** FastAPI 0.115.2 was available before PR #20; target's unpinned install could resolve it or later.
- **Expected useful output:** Known compatible and incompatible branches plus unresolved exact branch.
- **What success would establish:** Compatibility threshold and plausible target branch.
- **What success would not establish:** Exact installed versions or passing target tests.
- **Stop, switch, or escalation condition:** Require exact environment capture or targeted tests if resolver state cannot be frozen.
- **Approach proposed by:** AI assistant.
- **Approach selected or approved by:** AI assistant under active plan.

#### C. Execution

- **Performed by:** AI assistant.
- **Actions taken:** Retrieved FastAPI 0.115.2 metadata; inspected Starlette 0.36.3 and 0.37.2 TestClient implementations and release information.
- **Tools, commands, APIs, or sources:** GitHub tagged sources and official release notes.
- **Identity, revision, and time boundary:** FastAPI 0.115.2; Starlette 0.36.3 and 0.37.2.
- **Reads, writes, external effects, or risk:** Public read-only.
- **Execution problems or deviations:** Exact target resolution remains unavailable.

#### D. Output and observations

- **Raw output or preserved reference:** E11–E13.
- **Direct observations:** FastAPI 0.115.2 requires Starlette >=0.37.2; Starlette 0.36.3 passes `app=` to HTTPX; Starlette 0.37.2 no longer does.
- **Missing, invalid, stale, conflicting, or inaccessible output:** Historical resolved FastAPI/Starlette versions.
- **What the output demonstrates:** A clear compatibility threshold and a known compatible FastAPI release line available before the PR.
- **What the output does not demonstrate:** The exact package set used in any target test run.

#### E. Interpretation and verification

- **Interpretation:** The target was likely compatible when installing then-current unpinned FastAPI, but compatibility cannot receive final decision authority without exact resolution or tests.
- **Reasoning summary:** The fixed Starlette lower bound predates the PR, and FastAPI's standard extra permits HTTPX 0.28.1. Unpinned resolution makes the branch plausible, not reproducible.
- **Alternative explanations:** A cached, constrained, or private environment could still use older FastAPI/Starlette; no such constraint is public.
- **Supporting evidence:** FastAPI and Starlette tagged sources.
- **Contradicting evidence:** No public target failure.
- **Uncertainty and limitations:** Environment drift and absent lockfile.
- **Interpreted by:** AI assistant.
- **Verification or challenge performed by:** Old/fixed source comparison.

#### F. Outcome

- **Question answered or current state:** Compatibility risk is bounded but not behaviorally proven.
- **Step output:** Starlette >=0.37.2 removes the incompatible call; FastAPI 0.115.2 requires that floor.
- **Step outcome:** A hard block is not justified; a targeted test remains necessary.
- **Finding created, changed, rejected, or left unresolved:** Changed finding from possible direct break to likely compatibility with unresolved exact environment.
- **Effect on recommendation:** `investigate/block` narrows to `run targeted checks`.
- **Effect on product understanding:** Version-resolution evidence needs identity and reproducibility before it can support a strong decision.
- **What remains unchanged:** Green CI authority still unresolved.

#### G. Progressive continuation

- **Next selected action:** Audit workflow triggers and actual head runs.
- **Why it follows from this outcome:** A relevant passing test could close the remaining uncertainty.
- **Other possible actions not pursued now:** More upstream API analysis that would not replace target behavior evidence.
- **Current approach status:** complete.
- **If replaced, replacement approach and reason:** Not applicable.

### Investigation step 5 — Determine what the green CI proves

#### A. State before action

- **Current question or uncertainty:** Did CI exercise TestClient behavior under HTTPX 0.28.1?
- **Why this matters:** A green badge should affect the recommendation only if the relevant path ran.
- **Current evidence:** One successful Docker workflow associated with head SHA.
- **Current working hypothesis:** Docker build installs dependencies but does not run tests; Python workflow was skipped due path filter.
- **Current recommendation or decision effect:** Relevant green tests could permit merge; irrelevant green build cannot.
- **Current product-model implication:** CI status must be joined with workflow definition, trigger, revision, and exercised responsibility.

#### B. Approach selection

- **Selected approach:** Inspect all relevant workflow definitions, Dockerfile, head workflow runs, jobs, and logs.
- **Why selected now:** It is the direct way to establish CI-to-responsibility alignment.
- **Alternatives considered:** Trust combined status; infer from workflow name; inspect only PR UI summary.
- **Why alternatives were not selected now:** Names/statuses can hide path filters and omitted test commands.
- **Required inputs and assumptions:** Public workflow files and GitHub Actions metadata.
- **Expected useful output:** Exact checks run and relevant checks absent.
- **What success would establish:** Scope of CI proof.
- **What success would not establish:** Behavior outside executed jobs.
- **Stop, switch, or escalation condition:** If logs unavailable, use definitions and job summaries and preserve limitation.
- **Approach proposed by:** AI assistant.
- **Approach selected or approved by:** AI assistant under active plan.

#### C. Execution

- **Performed by:** AI assistant.
- **Actions taken:** Retrieved Docker and Python workflows; inspected Dockerfile; queried head workflow runs and jobs; attempted log retrieval.
- **Tools, commands, APIs, or sources:** GitHub contents and Actions APIs.
- **Identity, revision, and time boundary:** Head SHA `391508...`, run `15940060582`, job `44966848674`.
- **Reads, writes, external effects, or risk:** Public read-only.
- **Execution problems or deviations:** Job steps were absent from API response; log retrieval returned HTTP 410.

#### D. Output and observations

- **Raw output or preserved reference:** E14–E19.
- **Direct observations:** Docker workflow succeeded; Dockerfile installs requirements and builds image; no test command exists. Python workflow would run `pytest --cov`, but its path filter excludes `requirements.txt`; no Python workflow run was returned for head.
- **Missing, invalid, stale, conflicting, or inaccessible output:** Exact pip resolution and build logs expired.
- **What the output demonstrates:** Dependency resolution/image construction succeeded; relevant tests were not publicly executed by PR CI.
- **What the output does not demonstrate:** TestClient initialization, route behavior, or stable future resolution.

#### E. Interpretation and verification

- **Interpretation:** The PR is green at the platform level but lacks decision-relevant CI. Treating it as fully tested would be a false favorable inference.
- **Reasoning summary:** Workflow trigger and command coverage, not status color, determine authority.
- **Alternative explanations:** Maintainer may have run tests privately; no public evidence supports that.
- **Supporting evidence:** Workflow path filters, Dockerfile commands, Actions run mapping.
- **Contradicting evidence:** None; successful Docker build is complementary but narrower.
- **Uncertainty and limitations:** Expired logs prevent exact dependency-set capture.
- **Interpreted by:** AI assistant.
- **Verification or challenge performed by:** Cross-check of workflow definition and actual run list.

#### F. Outcome

- **Question answered or current state:** No public relevant test proof exists for the PR head.
- **Step output:** One successful install/build check; one path-filtered-out test workflow.
- **Step outcome:** Green CI cannot justify an unconditional merge recommendation.
- **Finding created, changed, rejected, or left unresolved:** Created `misleading/partial green CI` finding.
- **Effect on recommendation:** Targeted `pytest --cov` under exact head becomes the smallest sufficient next check.
- **Effect on product understanding:** CI-path alignment is a first-class evidence object; skipped checks must remain explicit.
- **What remains unchanged:** Likely compatibility from framework sources.

#### G. Progressive continuation

- **Next selected action:** Construct bounded decision and realistic changed-evidence variants.
- **Why it follows from this outcome:** The remaining uncertainty has a clear minimal recovery action.
- **Other possible actions not pursued now:** Exhaustive source audit or broad deployment tests before the focused suite.
- **Current approach status:** complete.
- **If replaced, replacement approach and reason:** Log-based environment reconstruction was stopped because logs returned 410; workflow-definition analysis replaced it.

### Investigation step 6 — Construct the bounded maintainer action

#### A. State before action

- **Current question or uncertainty:** What action is justified without overstating compatibility or CI evidence?
- **Why this matters:** UpgradePilot must convert evidence into a proportionate maintainer action.
- **Current evidence:** Likely compatible framework floor; direct TestClient path; green install/build; missing relevant test run; drifting unpinned FastAPI.
- **Current working hypothesis:** Run the repository's existing Python workflow/tests on the exact head, capture resolved versions, then merge if green.
- **Current recommendation or decision effect:** Provisional targeted checks.
- **Current product-model implication:** Recommendation can be conditional and include a proof plan.

#### B. Approach selection

- **Selected approach:** Apply a sufficiency test: identify the smallest check that directly exercises the unresolved path.
- **Why selected now:** All remaining material uncertainty is concentrated in TestClient behavior and exact resolution.
- **Alternatives considered:** Merge based on likely compatibility; block indefinitely; run broad Kubernetes deployment tests.
- **Why alternatives were not selected now:** Likelihood is insufficient; hard block is disproportionate; deployment tests do not target the changed interface first.
- **Required inputs and assumptions:** Maintainer can run CI or local tests in a trusted checkout.
- **Expected useful output:** Bounded recommendation with conditions and limits.
- **What success would establish:** Whether exact-head route tests initialize and pass under resolved dependencies.
- **What success would not establish:** Production safety beyond covered routes or future dependency resolutions.
- **Stop, switch, or escalation condition:** If tests fail, attribute failure and block/repair; if resolution cannot be captured, preserve reproducibility limitation.
- **Approach proposed by:** AI assistant.
- **Approach selected or approved by:** Pending Ali review; manual UpgradePilot recommendation constructed by AI.

#### C. Execution

- **Performed by:** AI assistant.
- **Actions taken:** Joined findings, limitations, and available recovery actions; avoided executing untrusted code.
- **Tools, commands, APIs, or sources:** Existing case evidence.
- **Identity, revision, and time boundary:** Exact PR head.
- **Reads, writes, external effects, or risk:** No external mutation or code execution.
- **Execution problems or deviations:** Historical merge occurred without public test proof; product recommendation is evaluated independently from that outcome.

#### D. Output and observations

- **Raw output or preserved reference:** Decision reasons and targeted-check plan below.
- **Direct observations:** Existing test suite is already defined; CI path filter is the reason it did not run.
- **Missing, invalid, stale, conflicting, or inaccessible output:** Actual targeted test result.
- **What the output demonstrates:** A minimal recovery path exists.
- **What the output does not demonstrate:** That the update passed it.

#### E. Interpretation and verification

- **Interpretation:** `Run targeted checks` is stronger than abstention and more cautious than immediate merge.
- **Reasoning summary:** Primary-source compatibility evidence lowers risk; missing target behavior proof prevents unconditional merge.
- **Alternative explanations:** The maintainer may accept dependency-bot risk without tests; that is policy, not evidence-grounded product advice.
- **Supporting evidence:** E06, E09, E11–E17.
- **Contradicting evidence:** No target failure evidence.
- **Uncertainty and limitations:** Exact historical environment and private checks unknown.
- **Interpreted by:** AI assistant.
- **Verification or challenge performed by:** Recommendation traced to findings and evidence inventory.

#### F. Outcome

- **Question answered or current state:** Bounded recommendation constructed.
- **Step output:** Targeted-check decision with merge condition.
- **Step outcome:** Case can proceed to report, machine result, and product-model update.
- **Finding created, changed, rejected, or left unresolved:** Final finding: likely compatible, insufficient public behavior proof.
- **Effect on recommendation:** Final provisional outcome `run targeted checks`; merge if exact-head tests pass.
- **Effect on product understanding:** UpgradePilot needs CI sufficiency analysis and targeted-check planning, not only status ingestion.
- **What remains unchanged:** Historical merge remains an observed user action, not validation proof.

#### G. Progressive continuation

- **Next selected action:** Complete traceability audit, coverage update, and final artifact.
- **Why it follows from this outcome:** The technical decision is stable; remaining work is preservation and cross-case learning.
- **Other possible actions not pursued now:** More evidence collection that would not replace the missing test run.
- **Current approach status:** complete.
- **If replaced, replacement approach and reason:** Not applicable.

## 10. Observation, interpretation, and finding separation

| Chain | Observation | Interpretation source | Finding state | Support/contradiction | Permitted decision effect |
|---|---|---|---|---|---|
| C01 | PR patch changes only HTTPX pin | Mechanical diff | Exact transition established | E01–E05 | Start investigation; no safety effect alone |
| C02 | Tests instantiate FastAPI TestClient; app code has no HTTPX import | AI static interpretation | HTTPX is direct-declared, test-use, production-installed | E04–E08 | Prioritize TestClient checks; avoid broad runtime claims |
| C03 | HTTPX 0.28 removes `app` | Upstream attributed claim corroborated by tagged source | Relevant compatibility hazard | E09 | Cannot merge based on release-note summary alone |
| C04 | Starlette 0.36.3 passes `app=`; 0.37.2 does not | Source comparison | Compatibility threshold established | E11–E13 | If resolved Starlette <0.37.2, block; otherwise continue |
| C05 | FastAPI 0.115.2 requires Starlette >=0.37.2 | Package metadata interpretation | Compatible framework line available before PR | E11 | Lowers risk but does not replace exact resolution/test |
| C06 | Docker workflow succeeds; Dockerfile runs install/build only | Workflow/command interpretation | Installation/image build passed, tests unproven | E14–E16 | Small favorable effect limited to resolution/build |
| C07 | Python test workflow excludes requirements changes | Workflow-path interpretation | Decision-relevant CI was skipped | E17–E18 | Require targeted test before merge |
| C08 | Logs return 410 and FastAPI is unpinned | Evidence-state interpretation | Historical environment is not reproducible from public record | E04, E19 | Report limitation; capture environment in future runs |
| C09 | PR was merged | User action observation | Maintainer accepted update | E01 | No correctness effect; informs follow-up/history only |

## 11. Repository-specific relevance

### Dependency relationship

HTTPX is:

- **directly declared** in `requirements.txt`;
- **functionally used by tests** through `fastapi.testclient.TestClient`;
- **not observed in application source imports**;
- **installed in the production Docker image** because test and runtime dependencies share one requirements file;
- also included by FastAPI's `standard` extra, making the explicit pin a version-control constraint over an otherwise transitive framework dependency.

A single label such as `development dependency` would lose important distinctions.

### Changed API intersection

The target does not call `httpx.Client(app=...)` directly. The relevant call, if present, belongs to Starlette's TestClient implementation.

- Starlette 0.36.3 passed `app=self.app` and is incompatible with HTTPX 0.28.x.
- Starlette 0.37.2 removed that call.
- FastAPI 0.115.2 requires Starlette >=0.37.2 and permits HTTPX >=0.23 through its standard extra.

Therefore the proposed update is likely compatible with a then-current unpinned FastAPI install, but the target does not preserve the exact resolution.

### Runtime and platform constraints

- Target Docker image uses Python 3.13.
- HTTPX 0.28.1 requires Python >=3.8.
- No Python-floor conflict is present.
- HTTPX is pure Python in this case; no native/platform wheel branch is activated.

### What static evidence cannot establish

- exact package versions installed in the historical workflow;
- whether `TestClient(app)` initializes under the head environment;
- whether all five route tests pass;
- behavior in private deployments;
- future reproducibility while FastAPI remains unpinned.

## 12. Checks, comparisons, and observed behavior

| Check/comparison | Question | Inputs/revision | Result | Demonstrates | Does not demonstrate | Reliability limits |
|---|---|---|---|---|---|---|
| PR patch comparison | Exact proposal | PR #20 | One-line HTTPX pin change | Mechanical transition | Compatibility | High |
| Repository usage search | Where HTTPX matters | Base/head | Tests use TestClient; no app HTTPX import found | Static relevance | Dynamic hidden use | Good at repository scope |
| HTTPX changelog comparison | Upstream changes | 0.27.2→0.28.1 | `app` removed; SSL fix; other behavior changes | Attributed upstream behavior | Target impact | High for declared changes |
| Starlette source comparison | Compatibility threshold | 0.36.3 vs 0.37.2 | Old passes `app=`, fixed version does not | Cause and fixed branch | Target resolution | High |
| FastAPI constraint inspection | Plausible resolved branch | 0.115.2 | Requires fixed Starlette floor | Compatible line available | Exact install | High for tag metadata |
| Docker Actions run | Can dependencies install and image build? | Head SHA | Success | Resolver/build succeeded in that run | Tests, app startup, route behavior | Exact logs unavailable |
| Python workflow trigger analysis | Did tests run? | Head workflow | `requirements.txt` excluded | Why relevant workflow skipped | Private/local tests | High for public CI |
| Job-log retrieval | What exact packages installed? | Job 44966848674 | HTTP 410 | Evidence expired | Resolution details | Inaccessible |
| Proposed targeted test | Does exact head behave? | Trusted checkout, exact head | Not run in this investigation | Would directly test unresolved path | Production completeness | Maintainer action required |

## 13. Missing, inaccessible, conflicting, and uncertain evidence

| Item/question | State | Why | Decision/report consequence | Recovery |
|---|---|---|---|---|
| Exact FastAPI/Starlette resolution | Missing | No lockfile or accessible install log | Compatibility remains likely, not proven | Capture `pip freeze`/resolver report in rerun |
| Python test run on PR head | Missing because path-filtered | `requirements.txt` not included in workflow paths | Green CI cannot support merge alone | Trigger workflow manually or expand path filter; run `pytest --cov` |
| Docker job logs | Inaccessible | GitHub returns 410 after retention | Cannot reconstruct exact environment | Re-run trusted build with artifact capture |
| Human merge rationale | Missing | No PR comments/reviews | Do not infer why maintainer merged | Ask maintainer if decision history matters |
| Private/local test execution | Unknown | Not publicly observable | Historical merge is not test evidence | Maintainer confirmation or new run |
| Hidden dynamic HTTPX use | Unresolved but low-evidence | Static search only | Avoid absolute claim of test-only use | Runtime import tracing if needed |
| Security trigger | Not indicated | Ordinary Dependabot update and changelog; no advisory evidence | Do not label security update | Search advisories only if policy requires |

There is no material contradiction among acquired sources. The important tension is between a green Docker status and absent decision-relevant test coverage; these are compatible observations with different authority.

## 14. Changed-evidence and failure variants

### Variant A — Old Starlette resolution

**Change:** Exact environment resolves Starlette 0.36.3 or another version whose TestClient passes `app=` to `httpx.Client`.

**Why realistic:** The target does not lock FastAPI/Starlette, and cached/private constraints could differ from the public latest-resolution assumption.

**Effects:**

- `TestClient(app)` is expected to fail on initialization with HTTPX 0.28.x;
- likely-compatibility finding is superseded;
- Docker build may still pass because it does not instantiate TestClient;
- recommendation becomes `investigate/block` until FastAPI/Starlette is upgraded or HTTPX remains <0.28.

**Stable conclusions:** CI path filtering remains a defect; Docker green remains insufficient.

### Variant B — Exact-head Python workflow passes with captured resolution

**Change:** Maintainer runs the existing lint/test commands on the exact head, preserves resolved versions, and all tests pass.

**Effects:**

- missing behavioral evidence becomes accepted passing evidence;
- recommendation changes from `run targeted checks` to `merge after normal review`;
- limitations remain for untested production behavior and future unpinned resolution;
- UpgradePilot should attach the test result, environment identity, and coverage scope to the report.

### Variant C — Requirements changes trigger Python CI

**Change:** `.github/workflows/python.yml` includes `requirements.txt` in its pull-request paths.

**Effects:**

- the relevant test workflow runs automatically for the proposed update;
- absence-of-test branch disappears for future dependency PRs;
- green status gains decision authority only if exact job and revision succeed;
- this is a repository process improvement, not a requirement for UpgradePilot to mutate the repository automatically.

## 15. Manual decision construction

- **Candidate outcome:** `Run targeted checks`; merge only if the exact-head Python tests pass under a captured dependency resolution.
- **Decision reasons:**
  1. The update reaches a real target path through FastAPI's TestClient.
  2. HTTPX 0.28.x removed the `app` argument, creating a known framework compatibility boundary.
  3. FastAPI 0.115.2 and Starlette >=0.37.2 provide strong evidence that a then-current environment is likely compatible.
  4. The successful Docker check proves dependency installation and image construction only.
  5. The Python workflow that runs `pytest --cov` was skipped because its path filter excludes `requirements.txt`.
  6. Exact resolved FastAPI/Starlette versions and historical logs are unavailable.
- **Evidence supporting each reason:** C02–C08 and E06, E09, E11–E19.
- **Material limitations:** No actual target test result; environment drift; no private review context.
- **Unresolved questions:** Exact historical package set and whether any private/local tests ran.
- **Why a stronger outcome is not justified:** Immediate merge would treat likely compatibility and irrelevant green CI as proof.
- **Why a weaker outcome is not justified:** Primary-source compatibility evidence and successful installation make indefinite block or abstention disproportionate.
- **Suggested next action:** In a trusted checkout of head `391508...`, install dependencies while capturing resolved versions, run `ruff check .` and `pytest --cov`, and attach results to the PR. If tests fail at TestClient initialization, inspect resolved FastAPI/Starlette and either upgrade the framework stack or retain HTTPX <0.28.
- **Human judgment still required:** Accepting residual risk, reviewing dependency hygiene, and merging.

The historical repository merged PR #20. That is recorded as a user action, not used as proof that the evidence supported an unconditional merge.

## 16. Human-readable maintainer report

### HTTPX 0.27.2 → 0.28.1

**Recommendation: run the repository's Python tests on this exact PR head, then merge if they pass.**

The change is a one-line direct pin update. The application does not directly import HTTPX, but the test suite constructs FastAPI's `TestClient`, which uses HTTPX internally.

HTTPX 0.28 removed the deprecated `app` constructor argument. Older Starlette TestClient versions passed that argument and would fail. Starlette 0.37.2 removed the incompatible call, and FastAPI 0.115.2 requires Starlette 0.37.2 or newer, so a normal then-current FastAPI resolution is likely compatible.

The available green GitHub check is not enough to confirm that. It builds the Docker image and successfully installs dependencies, but it does not run tests. The separate Python workflow would run `pytest --cov`, yet it is filtered to application/test paths and does not trigger for `requirements.txt` changes. No Python test run is attached to the PR head, and the old Docker logs have expired, so the exact resolved FastAPI/Starlette versions are unavailable.

Run the existing Python workflow or equivalent trusted commands while preserving the resolved package versions:

```text
ruff check .
pytest --cov
```

If those pass on head `391508134b083b8f54461c0b576e8f7985c6ecb4`, merge after normal review. If TestClient initialization fails, upgrade FastAPI/Starlette to a version using Starlette >=0.37.2 or keep HTTPX below 0.28 until that compatibility issue is resolved.

This report does not claim complete production safety. The update's observed functional path is the test client; the production image also installs HTTPX because development and runtime dependencies are not separated.

## 17. Conceptual machine-consumable result

The following is illustrative and non-binding:

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
    statement: The successful PR workflow built the image but did not run Python tests.
    evidence: [E14, E15, E16, E17, E18]
limitations:
  - exact_resolved_fastapi_starlette_missing
  - python_test_run_missing
  - docker_logs_expired
  - private_maintainer_checks_unknown
decision:
  outcome: run_targeted_checks
  reasons: [F1, F2, F3, F4]
  required_checks:
    - capture_resolved_versions
    - ruff_check
    - pytest_cov
  transition_on_pass: merge_after_normal_review
  transition_on_testclient_failure: investigate_or_block
user_follow_up:
  required: true
  actor: maintainer
  action: run trusted exact-head test workflow and review result
```

## 18. User interaction and follow-up flow

```text
PR locator supplied or event received
→ UpgradePilot freezes base/head and version transition
→ detects direct manifest pin and TestClient usage
→ retrieves upstream API-removal and framework compatibility evidence
→ maps actual workflows and identifies skipped Python tests
→ reports likely compatibility but insufficient public proof
→ maintainer authorizes/runs exact-head tests
→ new test evidence is attached
→ UpgradePilot re-evaluates:
   pass → merge after normal review
   relevant failure → investigate/block with failure attribution
   unavailable/inconclusive → remain targeted-check/defer state
→ maintainer decides and merge/history is recorded
```

What should persist across reruns:

- immutable case identity;
- evidence references and retrieval state;
- prior findings and supersession history;
- workflow definitions and exact run identities;
- environment/resolver capture when generated;
- user action and resulting state transition.

A new commit, rebase, dependency resolution, or test run should trigger comparison rather than silently replacing prior evidence.

## 19. Candidate methods by responsibility

| Responsibility | Manual method | Candidate automation | Simplest credible baseline | Strengths | Failure modes | Downstream risk | Adoption evidence needed |
|---|---|---|---|---|---|---|---|
| Resolve case identity | GitHub PR metadata | GitHub API adapter | Repository + PR lookup and SHA freeze | Deterministic | Moving head, permissions | Evidence mixing | Replay tests on rebases/forks |
| Parse version change | Patch inspection | Manifest-aware diff parser | Exact changed requirement line | Simple, traceable | Multiple files/ranges/groups | Wrong transition | Ecosystem fixtures and lock/manifest variants |
| Classify dependency role | Search manifest/source/tests/Docker | Repository index plus dependency graph | Declared/use/install dimensions | Avoids one-label oversimplification | Dynamic imports, aliases | Wrong check priority | Representative repos and human review |
| Acquire upstream changes | Tagged changelog | Source resolver + bounded extraction | Exact tag changelog retrieval | Authoritative source | Missing/fragmented notes | Missed breaking change | Cross-source evaluation |
| Map API change to target | Source comparison | Symbol/call-path analysis plus LLM-assisted interpretation | Search known removed symbol and framework adapter | Target-specific | Indirect/dynamic calls | False favorable result | Benchmarks with changed APIs |
| Resolve compatibility threshold | FastAPI/Starlette metadata/source join | Version-constraint solver and compatibility graph | Compare declared ranges and known fixed version | Explainable | Unpinned/cached/private constraints | Overconfidence | Captured resolver outputs |
| Analyze CI authority | Workflow and run inspection | Workflow parser + path/command coverage mapper | Map changed files to triggered jobs and commands | Detects misleading green | Reusable workflows, dynamic scripts | False favorable CI claim | Diverse workflow corpus |
| Plan targeted check | Manual sufficiency reasoning | Rule/LLM-assisted check planner with deterministic limits | Choose existing test job that exercises path | Low cost | Tests may not cover behavior | False reassurance | Historical failure/coverage evaluation |
| Produce decision/report | Evidence join | Deterministic decision control plus generated explanation | Conditional outcome with trace links | Bounded and auditable | Missing policy/context | Overstated recommendation | Cross-case calibration and review |

No candidate becomes architecture through this scenario.

## 20. Data-flow and operating-model changes revealed

This case adds or strengthens the following product responsibilities:

1. **Supersession resolution:** Detect when an update PR is replaced and investigate the active successor without losing predecessor evidence.
2. **Multi-axis dependency role:** Separate direct declaration, functional use, and deployment installation.
3. **Framework compatibility joins:** A direct dependency change may affect the target only through an adapter owned by another dependency.
4. **Environment identity:** Unpinned dependency resolution is evidence that must be captured, not background implementation detail.
5. **CI trigger coverage:** Determine whether changed files triggered each relevant workflow.
6. **CI command coverage:** Determine what successful jobs actually executed.
7. **Skipped-check state:** A relevant workflow that did not run is not equivalent to failure or success.
8. **Expired-evidence state:** Retention loss must remain visible and may require rerun.
9. **Targeted-check planning:** Recommend the smallest existing check that closes the material uncertainty.
10. **Historical action separation:** Merge state is user action/history, not validation evidence.

Local operating flow:

```text
PR #20
→ exact manifest transition
→ dependency role map
→ target TestClient path
→ HTTPX app-argument removal
→ FastAPI/Starlette compatibility threshold
→ workflow trigger and command map
→ Docker install/build success + Python tests skipped
→ exact environment/test evidence missing
→ run targeted exact-head tests
→ conditional merge or investigate/block
```

Possible product boundary implication:

UpgradePilot should analyze and report CI sufficiency and propose checks. It should not mutate workflow path filters or run repository code without authorization.

## 21. Scenario retrospective

- **What did this case teach that existing documents did not make concrete?** A green PR can be mechanically real yet decision-irrelevant because workflow path filters excluded the changed manifest from the test job.
- **Which assumed stage was unnecessary?** Security-advisory investigation was not useful after the ordinary-maintenance trigger and target path were established.
- **Which missing responsibility became important?** Workflow trigger/command coverage and environment capture.
- **Which method looked useful?** Joining tagged upstream source, framework constraints, target usage, and workflow definitions.
- **Which method was weak or misleading?** Treating workflow conclusion or Dependabot compatibility framing as sufficient.
- **Which responsibility is conditional?** Framework-source comparison is needed when a target calls through an adapter; not every dependency update requires it.
- **What should remain outside UpgradePilot?** Unauthorised execution of public code, automatic workflow edits, and merge authority.
- **What current plan/specification may conflict?** The current bounded decision vocabulary can represent `run_targeted_checks`, but later product output must express exact check rationale, CI insufficiency, and conditional transition.
- **What contrasting future case is valuable?** An actual failing CI update where the failure may be pre-existing or unrelated; alternatively a direct runtime dependency with application source use.
- **Did investigation stop at the right point?** Yes. Additional static research cannot replace the missing exact-head test run.
- **What remains unresolved?** Exact historical resolved versions and private maintainer verification.
- **What can Ali now explain without assistance?** Not assessed in this AI-executed case; Ali review is pending.
- **Which material step did Ali personally perform?** Ali selected the overall task and required a new non-duplicate full runtime; technical steps were AI-executed.
- **What still depends on AI interpretation or control?** Evidence selection, compatibility reasoning, decision construction, and artifact drafting.

## 22. Coverage update to apply

Register S002 as:

- direct declared HTTPX dependency;
- observed test-framework use and production-image installation;
- manifest-only version-pin change;
- upstream API removal with complete changelog;
- framework compatibility threshold;
- Python 3.13 versus HTTPX >=3.8 compatibility;
- green install/build CI but skipped relevant Python tests;
- missing exact dependency resolution and expired logs;
- ordinary maintenance update;
- `run targeted checks` decision;
- maintainer follow-up required;
- stable historical merged PR with insufficient public test proof.

Most valuable next contrast:

> A dependency update with an actual failing test workflow where UpgradePilot must distinguish update-caused failure from pre-existing, flaky, environmental, or unrelated failure.

## 23. Progressive-record audit

Current status before final closure:

- [x] Every material investigation step has a stated question and reason.
- [x] Every material approach has a selection rationale.
- [x] Material alternatives and reasons for not pursuing them are visible.
- [x] Expected output and stop/switch criteria are recorded.
- [x] Raw outputs and direct observations are separated from interpretations.
- [x] Step outputs are separated from step outcomes.
- [x] Findings trace to preserved evidence and exact identity.
- [x] Recommendation reasons trace to findings and limitations.
- [x] Each material next action traces to the prior outcome.
- [x] Failed/abandoned paths are visible, including rejected candidates, expired logs, and switch to workflow-definition evidence.
- [x] Superseded interpretations are visible, including the change from possible hard break to likely compatibility.
- [x] Human and AI contributions are attributed.
- [x] Missing, inaccessible, and uncertain evidence remains explicit.
- [x] No material decision reason appears only in the report.
- [x] Routine lookups are grouped rather than expanded into separate steps.
- [x] Investigation stopped where only maintainer-owned dynamic proof can resolve the case.

Process note: candidate screening preceded the formal case freeze. The active scenario log preserves the actual screening and selection boundary instead of presenting all screening work as if PR #20 had been selected from the outset.

## 24. Completion statement

This section will be finalized after the active record is re-read against primary evidence, shared files are updated, and Ali receives the committed result.
