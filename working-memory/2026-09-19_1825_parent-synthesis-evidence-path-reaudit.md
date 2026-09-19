# Parent Synthesis — End-to-End Evidence-Path Re-Audit

**Opened:** 2026-09-19, 18:25 (session-local time)  
**Session status:** ACTIVE  
**Primary operation:** read-only cross-responsibility product analysis/review, with A → B → C → D → E Learning-by-Doing  
**Repository:** `motafegh/UpgradePilot`, `main`; initial observed product source head `0201069d91f2d2bc776b84616870fe0926386f3f`; documentary commits thereafter  
**Controlling plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Live position:** [`../MEMORY.md`](../MEMORY.md)  
**Cycle-3 technical closure:** [`2026-09-18_cycle3-runtime-strengthening-build.md`](2026-09-18_cycle3-runtime-strengthening-build.md)  
**Independent parallel learning:** [`2026-09-19_cycle3-integrated-learning-review.md`](2026-09-19_cycle3-integrated-learning-review.md)

## Formal decision, scope and authorization

Ali explicitly selected and STARTED the parent evidence-sufficiency and maintainer-action synthesis re-audit as the MAIN workstream on 2026-09-19. Cycle-3 implementation is CLOSED, and its remaining integrated learning continues independently in another conversation, **not as a gate** for this review. Reconstruct the ACTUAL product flow while learning its real inputs, control/data/evidence handoffs and module boundaries; repair local understanding gaps as discovered. Preserve significant reasoning, decisions, changed assumptions, code/test evidence, proof/non-proof and the stopping point progressively in this single record.

Authorization: read-only product-source/test review and relevant working-memory/live-state coordination updates. Do not mutate product source/tests, accepted specs/ADRs/plans, simulations or external targets; observations and promising implementation candidates do not themselves authorize Build. `MEMORY.md` exclusively owns canonical live position. Avoid reopening closed Cycle-3 details absent contradiction.

## Current-session focus (not a new plan)

1. Trace normally reachable PR → identity/dependency → CI/Target/upstream/impact → typed `PublicPullRequestInvestigation` → standalone action evaluator and current CLI evidence report; use real repository source/test evidence and representative public cases when relevant. Distinguish source fact, test fixture, observed runtime and inference.
2. Contrast current reachable producer evidence with action-specific positive permission. Classify gaps precisely: correctness/provenance; available but lost/miscomposed evidence; missing producer; deliberate coverage boundary; unimplemented action permission; or operational failure outside semantic result.
3. Compare candidates (exact consuming-job → Target, exact installed-version/artifact witness, exact target wheel-tag witness or a more fundamental demonstrated gap), and select a bounded next responsibility ONLY after end-to-end impact, owner, alternatives, proof and stop line are understood.
4. Continue a bounded A/B/C/D/E Learning-by-Doing loop; explain before meaningful reasoning checks, inspect evidence, transfer appropriate source/evidence diagnosis understanding, preserve the session trail. Any later Build uses separate authorization and proper operation route.

## Progressive engineering record

### Entry / A — initial orientation

- Read project governance/Charter/Operating Guide, selected parent plan/accepted semantics, `MEMORY.md`, closed Cycle-3 and parallel learning records, and repository-audit, Learning-by-Doing and working-memory Skills. Historical hosted Cycle-3 proof: run `35448172928`, focused 76/76 and full deterministic 604/604. This review has not re-executed tests; closed implementation proof does NOT establish installed version, compatibility or action permission.
- Primary ownership: reconstruct actual producer → composition → consumer semantics and diagnose exactly which proposition fails at each boundary. Parser internals and repeated Cycle-3 drills are deferred without material need.

### B — source/test findings (IN PROGRESS)

**1. Public PR and dependency entry (`src/upgradepilot/investigation.py`).** Application calls `get_pull_request`, `get_changed_files`, and `analyze_dependency_change`. A supported `DependencyChangeAnalysis` carries `DependencyVersionChange` and exact source contexts, enabling downstream CI/PyPI/upstream/impact branches; otherwise `DependencyChangeProblem` and empty source contexts. `PublicPullRequestInvestigation` stores typed results and possible `None`/empty states. Exceptions are not all automatically converted to typed investigation results.

**2. CI's existing exact identity (`src/upgradepilot/ci/consumption.py`, `ci/dependency_exercise.py`).** `StaticDependencyConsumptionEvidence` already owns state/mechanism, normalized package, `workflow_path`, `workflow_revision`, `job_key`, `step_source_index`, `source_path` and bounded command context. Static job/install declaration support does not itself prove runtime execution, installed exact version or package artifact. Application acquires exact-head workflow runs/jobs plus definition and evaluates CI coverage.

**3. CI → Target integration (`investigation.py` `_compose_target_artifact_environments`, `target/artifact_environment.py`).** Only when a real `ArtifactServiceabilityImpactCandidate` exists does application compose Target results; only supported `direct_requirements` consumption enters this path. It verifies workflow correspondence and exactly one matching `RequirementsFileDependencyContext` by source/revision/package. It invokes `interpret_target_artifact_environment(definition, dependency_source_file=...)` **without** `consumption.job_key`. Its dedup key `(workflow_revision, workflow_path, source_context.source_path)` omits job: two distinct supported consuming jobs for the same source collapse to one target relationship. Target's `_select_target_job` sees whole workflow, accepts exactly one job and conservatively returns `ambiguous_target_job_selection` for multi-job workflows. Existing positive target evidence is not thereby shown false; this is a concrete available-but-not-transferred relation plus deliberate narrow job-selection rule. Any proposed improvement must bind source, exact workflow/revision, supported job identity and actual relevant static declarations, rather than pass arbitrary job keys or infer execution.

**4. CI → Target nearest tests (`tests/test_target_artifact_environment.py`, `tests/test_investigation.py`).** Focused Target test confirms multi-job ambiguity is a Target selection problem, not a parser failure; single-job result can preserve runner/Python/install declaration while exact wheel compatibility stays unresolved. Application tests `test_target_artifact_environment_uses_supported_direct_requirements_relationship` and `test_multi_job_target_ambiguity_is_preserved_despite_ci_job_relevance` cover supported static consumption; the second supplies a purpose-built test+lint workflow, and asserts Target ambiguity and unresolved artifact applicability. `test_target_artifact_environment_stays_inactive_without_real_candidate` proves the artifact-candidate gate. These are real repository test **fixtures**, not real-world public-PR execution or a fresh test run. Do not broaden this result to project-environment consumption paths.

**5. Next decisive seam: published wheel candidate → target applicability (`investigation.py`, `impact/artifact_serviceability.py`, `tests/test_artifact_serviceability.py`).** Application obtains old/proposed PyPI release evidence; if a bounded published-wheel tag loss candidate is built, it immediately calls `evaluate_artifact_serviceability_impact(candidate)` **without target compatibility evidence**, then separately derives static `target_artifact_environment_results`; the latter are NOT passed back into impact assessment. The impact contract requires `TargetWheelCompatibilityEvidence` with trustworthy exact target `supported_tags` tied to target repository/revision; static Target facts (runner/Python/install declaration) carry `exact_wheel_compatibility_state='unresolved'` and cannot be substituted for that evidence. Impact evaluates exact compatibility using intersections against BOTH old and proposed full wheel-tag inventories, not just observing one lost wheel tag. Focused tests prove no target witness → unresolved; manually constructed `TargetWheelCompatibilityEvidence` with controlled/fabricated target tags can establish applicability or non-applicability and mismatched repo/revision is rejected. Those contract fixtures do NOT prove a normal production producer of target tags. **Critical correction:** improving consuming-job selection alone may improve static declared-environment detail but does not currently produce the exact target tags necessary for artifact applicability or maintainer-action permission. Do not call absence of a recomposition here a correctness defect until there is an admitted target-evidence producer whose exact typed evidence the application should carry.

**6. Synthesis/CLI current path (`maintainer_action.py`, `cli.py`, `tests/test_maintainer_action.py`, `tests/test_cli.py`).** `MaintainerAction = Literal['abstain']`; `synthesize_maintainer_action(investigation)` is a separately callable abstention-only evaluator preserving typed investigation, decisive reasons/uncertainty/limits. `cli.main` calls `investigate_public_pull_request` then `_print_investigation`; it does NOT invoke synthesis, and the current CLI outputs evidence rather than maintainer-action reporting. Existing evaluator tests use fixture investigations, not normal-path positive permission proof. CLI tests intentionally assert absence of `Maintainer recommendation` for an artifact case. Acquisition failures can produce operational CLI error exits, not semantic typed abstention. Distinguish current `PR → investigation → evidence CLI` from future intended `investigation → synthesis → action output`.

**Still open:** Find representative public cases where they discriminate these integration seams; trace remaining current impact/upstream branches and reachability; compare precise action-relative premises. No next implementation is selected. The limited job selection is a real partial-static-evidence bottleneck; absent exact wheel-tag production is a separate stronger-evidence bottleneck; CLI integration is a further independently unimplemented output responsibility.

### C — progressive preservation

- Started this active session record and reconciled `MEMORY.md` with the selected main re-audit, retaining Cycle-3 learning independently. Recorded and progressively refined source/test-backed actual flow, omitted job handoff/deduplication, artifact-candidate gate, and stronger target-tag evidence requirement; separated accepted behavior from possible next Build proposals.

### D — learning and reasoning checks

- First question was premature: Ali did not remember CI/Target prerequisites. Briefly taught CI consuming-job identity, Target static environment job selection and installed-version proof limits, using illustrative two-job YAML explicitly synthetic. Ali correctly predicted `ambiguous_target_job_selection` and rejected exact-installed-version inference; source-level handoff explanation was tentative. Explained that Target sees both jobs but is not passed CI's already-supported job identity; recorded understanding of outcome and proof limit, NOT independent source/design mastery.
- Source trace and existing application fixture now make the flow concrete. Next small transfer exercise may consider two genuinely supported consuming jobs of the same dependency source with differing environments: why source/workflow-only dedup is insufficient if preserving each environment becomes the selected responsibility. Do not ask untaught compatibility internals or treat explanation as completed mastery.

### E — immediate continuation

- Compare the exact target-wheel-tag evidence-production requirement and specific action-relative product value against the partial-job handoff. Inspect relevant real-case pressure and next producer/consumer seam before proposing a bounded repair. Keep tests/proof class clear; do not reopen Cycle 3 or implement from an isolated finding.

## Current handoff

Main parent evidence-path re-audit ACTIVE. Initial PR/dependency→CI→Target→artifact applicability→standalone action/CLI seams source-traced; nearest Target/application and artifact-domain tests inspected. Crucial separation: (a) supported CI job identity omitted during Target selection, (b) static Target facts cannot substitute for missing exact target wheel compatibility witness, (c) no target witness is passed to impact in the current normal application, and (d) action evaluator is abstention-only and not called by CLI. No product runtime tests newly executed; no source/tests/specs/plans changed. Next assess the precise evidence proposition and real-case/action significance before ranking a Build responsibility.

**Activated procedures:** `UP-SKILL:upgradepilot-repository-audit`; `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`.


## Formal full-system audit checkpoint — 2026-09-19

### Route change

Ali explicitly redirected the main workstream from continuing one seam at a time to a **full current-system cross-responsibility audit** using the repository's `upgradepilot-repository-audit` procedure. The purpose is to establish one durable evidence-backed system assessment and use that audit, rather than scattered local observations, as the basis for the next journey decision.

Created canonical audit:

- `audits/2026-09-19_AUDIT-008_current-system-evidence-to-action-readiness.md`
- creation commit: `5023b178fdae16f935bacc9b93a2661136c02f45`

### Audit evidence/proof basis

- Audited current owner chain: Charter → Core/Product-Decision/Maintainer-Action specifications → parent synthesis plan → current source/tests → live state.
- Inspected the normal PR/dependency/CI/Target/upstream/impact/investigation/synthesis/CLI responsibilities and representative tests.
- Directly inspected GitHub Actions run `35448172928`: Python 3.12.14, fresh install/pip check/CLI PASS, focused investigation 15/15, Cycle-3 focused 76/76, full deterministic 604/604, S001/S002 eligible and S004 unresolved/deferred.
- Compared the proof commit `c5e3f08da8822fe4b80342d415640413009ab439` with product-source main `0201069d91f2d2bc776b84616870fe0926386f3f` and then with the pre-audit main documentary head; no product source/test changes occurred in those later commits. Therefore the hosted run remains evidence for the current product source/test implementation, not for future changes or live external/model behavior.
- No fresh product execution was performed in this audit; live public acquisition and live LM Studio quality remain distinct proof classes.

### Durable audit findings

AUDIT-008 records eleven findings. The key classification is:

```text
KEEP / strong foundation
→ F1 exact identity/provenance foundations
→ F2 evidence-report vs final-action separation is intentional incompleteness
→ F6 current runtime-correlation proof boundary
→ F8 local-model trust architecture with explicit live-model proof limit

CURRENT CORRECTNESS / TRUST / COORDINATION
→ F3 abstention evaluator can omit material branch-stopping residual uncertainty
→ F9 ambient GITHUB_TOKEN can silently alter/fail public acquisition
→ F11 audit lifecycle ACTIVE metadata conflicts with MEMORY.md live route

ACTION-RELATIVE CAPABILITY GAPS / CANDIDATES
→ F4 exact CI consuming job is not composed into Target job selection
→ F5 exact target wheel-compatibility contract has no normal producer
→ F7 bounded candidate/context discovery does not yet support favorable merge closure

REASSESS ON CONCRETE TRIGGER
→ F10 acquisition-failure containment risk is source-traced but not freshly proven as a defect
```

The most important newly discovered correction is **AUDIT-008-F3**: even the already-admitted abstention baseline can currently under-explain why stronger actions were unavailable because `_material_residual_uncertainty(...)` covers only a subset of branch-stopping investigation/problem states. This is more fundamental than immediately expanding Target/job/wheel evidence because stronger permissions should not be layered on an explanation baseline that can hide material unresolved evidence.

### A → B → C → D → E state for the formal audit slice

- **A — DONE:** established cross-responsibility audit question, owners, boundaries and evidence classes.
- **B — DONE:** inspected source/tests/spec/plan/runtime proof and produced AUDIT-008 with evidence-backed findings and smallest dispositions.
- **C — DONE:** durable audit created, active audit index registered, working memory and live state reconciled without product mutation.
- **D — PENDING:** review the audit findings with Ali; teach the few decision-relevant findings before asking him to choose/challenge the first post-audit responsibility.
- **E — PENDING:** after Ali's review, repair any understanding gap and select the next bounded Planning/Design or Build responsibility. Audit recommends F3 as the correctness gate, but the audit itself does not authorize implementation.

### Current stop / handoff

The previous narrow CI→Target reasoning path is now subordinate evidence inside AUDIT-008, not the controlling next step. **No new Build task is selected or authorized yet.** Continue from the full audit: first review/understand the important findings, then explicitly select the first post-audit responsibility. Preserve AUDIT-005's lifecycle validity question as F11; do not silently reclassify it without an explicit lifecycle decision.


## Post-audit learning/build execution plan selection — 2026-09-19

Ali accepted the post-audit direction and explicitly requested one durable plan that preserves **both learning ownership and product-building progression** before continuing implementation.

Created:

- `plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md`
- creation commit: `f0b01a090f4ad14119dfa8edc0f33705c9f8fdf8`

### Planning result

The plan is a single consequential child plan under the existing parent synthesis plan, not a replacement roadmap or plan family. It converts AUDIT-008 into this durable dependency order:

```text
verified end-to-end product-flow ownership
→ honest abstention-synthesis baseline (AUDIT-008-F3)
→ deliberate public-auth trust boundary (F9)
→ audit/live-state lifecycle reconciliation (F11)
→ action-relative reachability comparison
→ one selected producer/composition build
→ one non-abstention action admission
→ product presentation integration
→ first credible bounded public-PR synthesis proof
```

Learning and engineering are intentionally coupled through the canonical A → B → C → D → E cycle. The plan defines ownership/working/lookup learning depth, reasoning checks, proof ladders, working-memory discipline, a future durable product-flow learning artifact, and explicit stop lines against implementing all audit findings or all action labels.

### First selected slice

The plan's first live slice is **product-flow reconstruction and ownership baseline**.

Purpose:

- reconstruct the actual current source/test path end-to-end;
- establish producer → proposition/evidence → composition → consumer → unresolved/failure boundaries;
- teach only the concepts needed to own the real flow;
- create the durable product-flow learning/reference artifact only after the reconstruction is source-verified;
- perform **no product source mutation** in this first slice.

This first slice prepares the real Build work around F3 without asking Ali to reason from an incomplete mental model.

### Authorization / stop line

This plan creation and selection do **not** authorize product implementation. The next operation is source/test reconstruction + Learning-by-Doing. Product mutation begins only when a later bounded Build slice is explicitly entered under the normal Build procedure.

### A → B → C → D → E state for planning slice

- **A — DONE:** oriented the need for one combined learning/build execution plan from AUDIT-008 and the parent synthesis plan.
- **B — DONE:** created the bounded plan with sequence, learning depth, proof, gates, and prohibited scope.
- **C — DONE:** selected the plan in live state and preserved this planning result.
- **D — compactly complete:** the plan reflects Ali's explicit goal that learning and building progress together rather than as separate tracks.
- **E — DONE:** next slice is the source-verified end-to-end product-flow reconstruction; product Build remains stopped until that slice establishes the relevant ownership baseline.

**Activated procedures:** `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`.


## Product-flow reconstruction slice — front door through dependency transition

### A — orientation

Started the first live slice from `plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md`: source-verified reconstruction of the actual normal product flow. Current bounded chunk is:

```text
CLI/input
→ PR identity
→ changed-file / exact-file evidence
→ dependency-source interpretation
→ one trusted DependencyVersionChange or explicit DependencyChangeProblem
```

No product mutation is authorized in this slice.

### B — source/test trace

**CLI boundary.** `src/upgradepilot/cli.py` owns argument parsing, ambient environment input, rendering and exit policy. It passes `repository`, `pull_number`, and current `GITHUB_TOKEN` value into `investigate_public_pull_request(...)`. It does not own evidence semantics or orchestration.

**Application boundary.** `src/upgradepilot/investigation.py` owns orchestration. It creates provider clients, acquires one `PullRequestIdentity`, acquires coherent changed-file evidence, calls `analyze_dependency_change(...)`, and only enters downstream CI/PyPI/upstream/impact work when that result is a trusted `DependencyChangeAnalysis`.

**PR snapshot identity.** `PullRequestIdentity` freezes repository/PR identity plus exact base/head SHAs and declared changed-file count. `GitHubPullRequestClient.get_changed_files(...)` is not a blind mutable PR-files read: each returned `contents_url` must name the exact repository/path and frozen head SHA, the full declared record count must be acquired, and a post-acquisition PR re-read must preserve base SHA, head SHA and changed-file count. Controlled tests cover same-count head races, post-read base/head/count drift, multi-page drift, wrong repo/path locators and count disagreement. This establishes bounded observable snapshot coherence for admitted PR patch evidence; tests explicitly do not claim transactional GitHub snapshot isolation.

**Dependency-source acquisition is format-specific.**
- requirements/constraints: source-specific exact-pin extraction uses the coherent changed-file patch and records `extraction_method='changed_file_patch'`; it does not separately fetch base/head file contents.
- modified `uv.lock`: application acquires exact immutable base/head files through `GitHubRepositoryClient`, then structured lock extraction records `extraction_method='exact_base_head_files'`.
- modified `pyproject.toml` optional-extra path: likewise uses exact base/head repository files before optional-extra comparison.
- arbitrary files are ignored; unsupported statuses, missing/incomplete patches, malformed/unavailable files, ambiguous changes, and other source problems remain explicit `DependencyChangeProblem` states.

**PR-wide consensus boundary.** `compare_extracted_dependency_changes(...)` does not accept the first convenient success. Any admitted source problem blocks promotion. Otherwise all admitted extracted sources must agree on normalized package identity and exact old/proposed version pair. Only then is `DependencyVersionChange` created with the unique source-provenance records.

**Source-context handoff.** `DependencyChangeAnalysis` adds typed source contexts bound to the exact target repository and frozen head revision. These contexts mean “this dependency transition came from this source scope”; they do **not** prove workflow selection, installation, execution, compatibility, or maintainer action.

### Corrected mental model

Historical concern that requirements patch evidence could simply be stamped onto a stale frozen PR identity is no longer current behavior. The mutable PR-files endpoint is fenced by exact-head per-file locator validation plus a post-acquisition identity read. This is weaker than direct immutable base/head content comparison in mechanism, but it is an intentionally repaired coherent snapshot contract and is covered by focused tests. Do not reopen the earlier frozen-revision defect absent new contradiction/regression evidence.

### C — preservation

This front-door trace is now preserved as the first verified segment of the end-to-end flow. No live-state change is required; the selected plan and slice remain the same.

### D — ownership check prepared

The key ownership distinction for Ali is:

```text
PullRequestIdentity
→ freezes WHICH proposal snapshot is under investigation

ChangedFile / exact RepositoryTextFile
→ supplies source evidence tied to that snapshot

source-specific extractor
→ interprets one admitted dependency source

PR-wide comparison
→ promotes only agreeing non-problematic sources

DependencyChangeAnalysis
→ trusted transition + typed source scopes for downstream reasoning
```

Success at this stage proves one trustworthy **declared dependency transition** inside the supported source boundary. It does not prove CI exercised it, what exact version was installed at runtime, target compatibility, or any maintainer recommendation.

### E — next bounded chunk

After the ownership check, continue from `DependencyChangeAnalysis.source_contexts` into:

```text
exact-head workflow runs/jobs
→ workflow definition at frozen head
→ dependency consumption/direct exercise
→ bounded runtime strengthening
```

and reconstruct exactly what CI does and does not establish.


### D — front-door ownership check result

Ali's reasoning:

1. For conflicting requirements/lock transitions, correctly rejected promotion to one trusted dependency change and preferred preserving the explicit conflict.
2. Correctly separated source-level dependency evidence from runtime installation/execution. Precision added: successful front-door analysis establishes one trusted **PR-wide declared exact transition at the frozen proposal snapshot**, not merely that relevant files were observed.
3. Correctly identified provenance/context as necessary for evidence-based downstream work and reproducibility. Precision added: typed source contexts are also **active semantic inputs** to downstream CI/environment reasoning, because the system must preserve which exact dependency source/scope is being selected or consumed rather than pass only a package/version tuple.

Ownership depth for this segment is adequate to continue. Do not treat it as proof of independent mastery of every source extractor/provider detail.

## Product-flow reconstruction slice — dependency transition into CI evidence

### A — orientation

Next bounded chunk:

```text
DependencyChangeAnalysis.source_contexts
→ exact-head workflow runs
→ exact-attempt jobs/steps
→ exact-head workflow definition
→ static dependency consumption / direct exercise
→ bounded runtime strengthening
→ DependencyCICoverageResult
```

Key conceptual separation:

- GitHub Actions provider owns **factual runtime records and identity**.
- exact workflow definition + dependency source contexts support **static meaning**.
- CI domain composes them into dependency-consumption/direct-exercise propositions.
- runtime strengthening can strengthen an already-supported static proposition only within admitted structural/correlation boundaries.

### B — source/test findings

**Exact-head runtime acquisition.** `GitHubActionsClient.get_exact_head_workflow_runs(...)` queries pull-request workflow runs for the frozen PR `head_sha`, validates event/head identity and complete bounded pagination. `get_workflow_jobs(...)` uses the captured `run_attempt` endpoint so a later rerun cannot silently replace jobs paired with the recorded run. Each job must retain run ID and frozen head SHA. Provider output is factual execution evidence; it does not interpret command meaning.

**Exact workflow definition.** For each exact-head run, application calls `GitHubRepositoryClient.get_exact_head_workflow_file(...)`, which revalidates run identity/path and reads the workflow file at the frozen PR head revision.

**Source-context composition.** Before CI interpretation, application acquires any exact project-environment sources needed by the dependency source contexts. The static workflow owner then combines workflow commands with those source contexts. This is why the earlier source-context handoff is operationally necessary, not documentary provenance only.

**Static consumption.** `StaticDependencyConsumptionEvidence` means an exact static workflow/job/step/command declaration is supported as consuming the changed dependency. It preserves workflow path/revision, `job_key`, step source index, source path where applicable, command occurrence and parser-neutral structure. It does not prove runtime execution or installation success.

**Direct exercise is a separate axis.** A later package invocation can support direct-exercise evidence only when it is ordered after supported dependency consumption in the admitted static job. A workflow can therefore support consumption while direct exercise remains not established.

**Runtime strengthening.** Static evidence is mapped to an exact-attempt runtime step only when the command occurrence's structural relation/execution profile is eligible and runtime correlation is sufficiently strong. `supported_runtime_correlated` means the owning user-defined run step was matched to a GitHub step reported completed-successful without visible continue-on-error masking. It still does not prove exact dependency version, wheel/sdist, artifact tags or compatibility.

**Real repository integration fixture.** `tests/test_r6_investigation_ci_integration.py` uses the preserved Pydantic/S001-shaped dependency path for `soupsieve`: an exact `uv.lock` source context plus exact workflow text. The `docs-build` command `uv sync --all-packages --group docs` is supported with reachability witness `mkdocs-llmstxt → beautifulsoup4 → soupsieve`, while the lint environment is not treated as consuming the changed dependency. This fixture proves normal orchestration derives the static relationship from exact sources; it intentionally stops unrelated upstream work and does not by itself prove live execution/runtime correlation.

### Current mental model

```text
green exact-head job
!= dependency coverage

static workflow mentions/install/selects relevant source
→ possible supported static consumption

supported static consumption
+ eligible exact occurrence
+ exact runtime step correlation
+ completed-successful unmasked runtime step
→ bounded runtime-correlated support
```

No live state change yet; continue reconstruction before creating the durable learning artifact.


### D — CI ownership check result

Ali correctly identified the static structure/order distinction: the requirements install can establish supported static consumption when tied to the known requirements source, and a later package invocation can support a distinct direct-exercise proposition. He also correctly rejected treating static source order alone as proof of actual runtime execution/success.

Precision corrections:

- `StaticDependencyConsumptionEvidence.state='supported'` is the relevant static consumption state; package invocation evidence is a separate observation, and direct-exercise support depends on its admitted relation to supported consumption.
- The third answer initially attributed the remaining proof gap to needing static evidence/correlation. In the posed scenario, successful correlation was already assumed. The surviving gap is stronger: exact correlation proves the owning user-defined step was reported completed-successful, but does **not** prove which dependency version/artifact was actually resolved/installed or that the inner dependency-specific behavior executed successfully. An exact runtime installed-version/artifact witness would be a distinct future evidence producer if an action proposition requires it.

Ownership is sufficient to continue; retain this distinction for later AUDIT-008-F6 analysis.

## Product-flow reconstruction slice — PyPI/upstream support-drop to target applicability

### A — orientation

Next bounded branch:

```text
trusted DependencyVersionChange
→ exact proposed/old PyPI release evidence
→ trusted upstream repository identity
→ exact crossed release interval + tag/changelog authority
→ bounded support-drop candidate extraction
→ deterministic grounding
→ PythonSupportDropImpactCandidate
→ exact target pyproject requires-python
→ target relevance
→ applicability assessment
```

This branch answers a different question from CI. CI asks whether the changed dependency source is statically/runtime-related to project execution. The upstream/target branch asks whether the dependency transition crosses a documented Python-support drop that is relevant to the target revision's declared Python range.

### B — source/test findings

**PyPI release evidence.** `PyPIReleaseClient.get_release(package, version)` acquires exact requested release JSON, checks normalized package identity and exact published version, and preserves retrieval/source identity, distribution files and project URLs. Problems such as package/version absence, identity mismatch, malformed response and acquisition failure stay typed; they are not converted into “no risk.”

**Upstream repository identity.** `UpstreamRepositoryResolver` does not trust a project URL alone. It reconciles admitted PyPI repository-association URLs with PyPI file provenance publishers and requires one matching GitHub repository identity. Missing/unsupported/ambiguous/mismatched provenance remains an explicit problem.

**Release interval authority.** From the exact dependency transition the application constructs the old-exclusive/proposed-inclusive release interval, uses the PyPI release index to select crossed releases, resolves the proposed version tag, discovers the changelog at the resolved tag commit, acquires that changelog at the exact immutable commit, and assembles `AuthoritativeUpstreamIntervalEvidence`. Source problems remain part of authority composition rather than being hidden by another convenient source.

**Bounded semantic extraction.** `evaluate_support_drop_runtime(...)` requires authoritative interval evidence, builds a bounded crossed-release source window, invokes the local extractor only on that bounded source, then passes candidates through deterministic validation/grounding. The model/extractor proposes candidates; it does not establish authority.

**Grounded support-drop claim.** `GroundedPythonSupportDropClaim` exists only after candidate identity matches the trusted package/release interval, category/state are admitted, Python line is canonical, introduced release is inside the trusted crossed interval, and the source quote is grounded in admitted authoritative source evidence. Multiple distinct claims remain explicit rather than being silently selected.

**Impact candidate does not self-authorize applicability.** Once one grounded Python support-drop claim exists, `build_python_support_drop_impact_candidate(...)` binds it to the exact PR target repository/head revision. It marks mechanism established but target exposure/activation as `to_evaluate`.

**Mechanism-specific investigation selection.** Initial impact evaluation is unresolved because the exact target Python declaration has not yet been acquired. The selector chooses exactly one bounded read-only investigation: read `pyproject.toml` at the exact target head and interpret `[project].requires-python`. Once that evidence exists—even if it is a problem—the same acquisition is not repeatedly selected.

**Target relevance.** `evaluate_target_python_relevance(...)` asks only whether the dropped Python major/minor line intersects the exact target revision's declared `requires-python` range. Outcomes include `declared_python_overlap`, `outside_declared_python_range`, target-declaration unresolved, upstream-claim unresolved, or comparison unsupported.

**Applicability.** The Python-support impact path requires three proposition states: grounded upstream support drop, exact target Python declaration, and overlap/activation. Overlap can establish the bounded candidate as applicable; non-overlap can establish it as not applicable for this mechanism. Neither outcome is equivalent to whole-update safety or a final maintainer action.

### Current mental model

```text
PyPI says release exists
!= trusted upstream semantic claim

project URL
!= trusted upstream repository

model says "Python 3.8 dropped"
!= grounded support-drop claim

grounded support-drop claim
!= target affected

target requires-python overlaps dropped line
→ bounded mechanism applicability established

bounded mechanism applicability
!= block/merge/action permission
```

No live-state change. Continue source reconstruction through artifact-serviceability and then synthesis/CLI before authoring the durable end-to-end learning artifact.


### D — Python-support applicability ownership check

Ali correctly concluded that when an upstream Python 3.9 support drop does not intersect the target's declared `requires-python >=3.10` range, the bounded Python-support-drop candidate is **established not applicable**. He also correctly rejected upgrading that one mechanism result into whole-update safety or merge permission: other mechanisms/candidates may still matter, and candidate-discovery coverage is bounded.

Ownership depth is sufficient to continue.

## Product-flow reconstruction slice — artifact serviceability through synthesis and CLI

### A — orientation

Final reconstruction chunk:

```text
old/proposed PyPI release inventories
→ published wheel capability comparison
→ artifact-serviceability candidate
→ partial Target artifact-environment evidence
→ exact target wheel-compatibility gap
→ PublicPullRequestInvestigation
→ standalone maintainer-action synthesis
→ current evidence-report CLI
```

### B — source/test findings

**Artifact candidate formation.** `build_artifact_serviceability_impact_candidate(...)` validates exact dependency/release identity, parses old/proposed published wheel filenames into exact compatibility tags, and forms a candidate only when at least one old published wheel-tag capability disappears. Malformed wheel evidence is explicit; unchanged tag sets produce no candidate.

A removed tag alone does not prove target impact. The evaluator compares the target's supported tag set against the **complete old and proposed wheel inventories**. A different proposed wheel can still serve the same target.

**Exact Target compatibility contract.** `TargetWheelCompatibilityEvidence` requires exact target repository/revision/source plus a non-empty exact `supported_tags` set. The module explicitly forbids deriving this from UpgradePilot's own `sys_tags()` or broad labels such as “Python 3.6 on Linux.”

**Current Target artifact evidence is partial static evidence.** `interpret_target_artifact_environment(...)` can read one safely selected workflow job and preserve literal runner, setup-python version, and a static dependency-installation declaration. It intentionally leaves `exact_wheel_compatibility_state='unresolved'`. It also currently requires exactly one workflow job; multi-job definitions become `ambiguous_target_job_selection`.

**Current normal application gap.** When an artifact candidate exists, application currently calls `evaluate_artifact_serviceability_impact(candidate)` **without** `TargetWheelCompatibilityEvidence`, so applicability remains unresolved. It separately derives partial static Target environment results. These partial results cannot substitute for exact supported wheel tags. This is the AUDIT-008-F5 producer gap; the earlier exact consuming-job handoff issue is F4.

**PublicPullRequestInvestigation is the application evidence container.** It aggregates the frozen PR/dependency state plus CI, package, upstream, Target, impact, and problem/unresolved states. It is not itself a recommendation.

**Maintainer synthesis is a separate layer.** `synthesize_maintainer_action(...)` currently admits only `action='abstain'`. It deliberately does not map “applicable technical concern” directly to block/investigate/etc. Non-abstention actions wait for action-specific normal-producer proof.

**Current synthesis correctness gap.** `_material_residual_uncertainty(...)` currently projects dependency problems, non-supported CI states, unresolved/conflicted Python impact, and unresolved/conflicted artifact impact. It does not yet preserve all materially branch-stopping package/upstream/target/support-drop problem states from `PublicPullRequestInvestigation`. This is AUDIT-008-F3 and is why the plan places honest abstention repair before adding stronger actions.

**Current CLI is an evidence renderer.** `cli.main(...)` invokes `investigate_public_pull_request(...)`, renders `PublicPullRequestInvestigation`, and returns exit status according to input/acquisition/response errors. It does **not** call `synthesize_maintainer_action(...)`. CLI tests explicitly verify that artifact evidence is rendered at its current proof strength and that no “Maintainer recommendation” is emitted.

### Complete reconstructed normal model

```text
CLI/input
→ frozen public-PR identity
→ coherent dependency-source evidence
→ trusted PR-wide DependencyVersionChange + source contexts
→ exact-head/exact-attempt CI evidence
→ static dependency consumption/direct exercise
→ bounded runtime strengthening
→ exact PyPI release evidence
→ trusted upstream repository + crossed-release authority
→ bounded semantic candidate extraction + deterministic grounding
→ mechanism-specific impact candidates
    ├─ Python-support-drop applicability via exact target requires-python
    └─ artifact-serviceability applicability via exact target wheel tags
       (normal producer currently missing)
→ typed PublicPullRequestInvestigation
→ standalone abstention-only maintainer synthesis
   (currently incomplete residual-uncertainty projection)
→ current CLI evidence report
   (synthesis not yet wired)
```

### C — preservation

The end-to-end reconstruction is now source/test-backed across all major current responsibilities. No product source was changed. The next planned action after one final ownership check is to create the durable learning/reference artifact from this verified model, then enter the F3 synthesis-correctness Build slice only after that learning artifact is completed and the Build route is explicitly activated.

### Current proof hierarchy retained

```text
declared dependency transition
< static CI consumption/direct exercise
< bounded runtime-correlated CI support

upstream semantic candidate
< deterministically grounded upstream claim
< mechanism-specific target applicability

mechanism applicability
< action-specific permission
< maintainer-facing action output
```

Each '<' means “stronger/different proposition requiring additional evidence,” not a universal numeric confidence score.


## Main-session learning boundary correction and reconstruction closure

Ali clarified the operating boundary for this main session:

- continue real project progression, Learning-by-Doing, building/coding/testing and interactive teaching here;
- **do not create learning-note artifacts automatically**;
- learning-note artifact authoring is occurring in another conversation and is only in scope here if Ali explicitly requests it.

The selected execution plan was corrected accordingly. Interactive source-backed explanation + reasoning checks + working-memory preservation are sufficient; a durable learning artifact is no longer a completion gate.

### Final reconstruction ownership check

Ali correctly distinguished mechanism-specific applicability from whole-update action authority:

```text
Python-support-drop established_not_applicable
!= whole update safe

Python-support-drop established_applicable
!= automatic block
```

For the block question, Ali correctly reasoned that synthesis must not decide from one isolated investigation signal and instead must combine the material decision-relevant evidence at the decision layer.

Precision from the accepted synthesis specification: synthesis does consider material evidence together, but `block` is still **positively permissioned**, not an aggregate confidence/severity result. For a declared Python-support conflict, `established_applicable` alone is insufficient. The hold additionally requires:

- trusted exact proposal/revision/dependency identity;
- grounded relevant support exclusion;
- exact target support obligation for the affected Python environment;
- evidence that the proposed dependency is required in that environment;
- a demonstrated conflict after relevant dependency conditions, alternative supported paths and admitted proposal changes are accounted for.

Runtime-correlated CI can strengthen evidence that an owning dependency-consuming step ran successfully, but it does not itself establish those missing support-obligation/conflict premises.

### Reconstruction slice status

A — DONE: major owners/handoffs oriented interactively.  
B — DONE: front door, CI, PyPI/upstream, target applicability, artifact-serviceability, synthesis and CLI source/test paths reconstructed.  
C — DONE: material findings preserved progressively.  
D — DONE: Ali demonstrated the key transition/applicability/action distinctions at sufficient ownership depth for continuation.  
E — DONE: no material learning gap blocks engineering continuation.

The end-to-end reconstruction/ownership baseline is therefore **COMPLETE**.

### Next bounded responsibility

Selected next responsibility: **AUDIT-008-F3 — honest abstention synthesis**.

Goal: preserve materially branch-stopping uncertainty in `MaintainerActionSynthesis` without duplicating domain semantics or creating new action permission. This is the first post-reconstruction Build responsibility. Learning remains interactive; no learning-note artifact is part of this slice unless explicitly requested.


## AUDIT-008-F3 Build — honest abstention residual uncertainty

### A — pre-change model

Selected responsibility: repair the already-admitted abstention evaluator so material branch-stopping investigation problems remain visible even when the branch stops before a mechanism-specific impact object exists.

Ownership boundary:

```text
domain modules
→ own problem types, states and details

PublicPullRequestInvestigation
→ preserves typed intermediate branch state

maintainer_action synthesis
→ projects only material action-relevant residual uncertainty
```

No new evidence producer, action permission, CLI integration or generic evidence graph is in scope.

### B — implementation

Changed `src/upgradepilot/maintainer_action.py`.

Added explicit synthesis projection for current typed branch-stopping states across:

- proposed package-release problems;
- upstream repository identity problems;
- release-index problems;
- crossed-release selection problems;
- proposed-version tag problems;
- changelog-discovery problems;
- tagged-changelog/source-authority problems;
- upstream interval-authority problems;
- unresolved/problematic support-drop semantic results;
- old package-release problems on the independent artifact branch;
- artifact candidate evidence problems;
- Target artifact-environment problems.

The upstream projection reports the furthest material problem reached on the causal branch, avoiding a dump of several derived failures for one root cause. The independent artifact branch can still contribute its own uncertainty simultaneously.

`UpstreamSupportDropClaimProblem(state='no_support_drop_claim')` is deliberately treated as a closed bounded mechanism result rather than manufactured residual uncertainty. Existing unresolved/conflicted Python/artifact impact summaries remain intact.

No change was made to `MaintainerAction = Literal['abstain']`, positive action permissions, domain result types, evidence acquisition, or CLI behavior.

### Proof additions

Extended `tests/test_maintainer_action.py` with focused cases proving:

- changelog branch-stop preserved even without Python impact;
- artifact candidate evidence problem preserved even without artifact impact assessment;
- closed no-support-drop result does not manufacture uncertainty;
- independent upstream + artifact problems are preserved in deterministic order.

Extended the existing normal application fixture in `tests/test_investigation.py::test_upstream_source_problem_stops_semantics_target_and_impact_but_not_ci` so the real application-shaped changelog stop is passed into synthesis and must surface its uncertainty.

### Verification correction

Initial integration assertion was accidentally inserted into the preceding closed `no_support_drop_claim` test due to an overly broad textual edit anchor. Source review caught this before closure. Commit `b3b1963e3466eac9b829f269293e86d43109ddb1` moved the assertion into the intended changelog-failure test. This correction reinforces the semantic boundary: closed no-claim must stay quiet; actual changelog evidence failure must remain visible.

### C — proof state

Source/tests are committed on `main`:

- synthesis implementation: `520df8c0b507f639e798518fcb99cdded69d36d0`
- focused tests: `c3f4b110b4cd88ce8dd11100127a0b41771c9c2d`
- normal-path integration proof edit: `ddf4ceb0944376ea7c7e1f5e52a229cb78572adb`
- integration placement correction: `b3b1963e3466eac9b829f269293e86d43109ddb1`

Executable validation is **PENDING**. The repository's `.github/workflows/product-verification.yml` is manual `workflow_dispatch` only. The available GitHub connector can inspect/rerun existing workflows but exposes no workflow-dispatch action, and no run/status exists for the current F3 commit. Container network access cannot clone the public repository in this environment. Therefore source review is not being misreported as test proof.

### Current F3 status

IMPLEMENTED / PROOF-PENDING — not technically closed.

Next required proof when an execution path is available:

```text
focused maintainer-action tests
→ investigation integration test
→ full deterministic product regression
→ hosted installed-package verification when justified
```

Do not advance the live engineering route to F9 as though F3 has passed regression proof.


## Canonical cycle alignment checkpoint — F3 Build

Ali explicitly re-anchored the main workstream to the root `AGENTS.md` mandatory Learning-by-Doing cycle. Coordination artifacts were reviewed and aligned so Build does not bypass the project-level A → B → C → D → E rhythm.

### Alignment decisions

1. Every substantive slice normally completes A → B → C → D → E before the next substantive responsibility is selected.
2. Build/Implement remains the primary operation for F3; the canonical cycle wraps that operation rather than replacing it.
3. When executable proof is temporarily unavailable, the implementation slice still completes D/E for what was actually established.
4. Deferred executable validation is then a **separate bounded evidence slice** with its own proportional A → B → C → D → E.
5. D/E completion never upgrades source-reviewed tests into executed proof.
6. F3 remains not technically closed until required executable validation passes.
7. No learning-note artifact is created in this main session unless Ali explicitly requests one.

The selected execution plan was updated to encode these rules; `MEMORY.md` now owns the live phase.

### F3 implementation-slice cycle status

```text
A — DONE
    Pre-implementation orientation established:
    domain problems remain domain-owned;
    PublicPullRequestInvestigation preserves typed branch state;
    synthesis projects only material action-relevant uncertainty;
    no new action/evidence producer/CLI integration.

B — DONE FOR IMPLEMENTATION
    maintainer_action.py changed;
    focused synthesis tests added;
    normal-shaped investigation→synthesis assertion added;
    misplaced assertion detected and corrected during source review.

C — DONE
    commits and source-review findings preserved;
    executable proof debt explicit;
    no test pass claimed;
    F3 status remains IMPLEMENTED / PROOF-PENDING.

D — ACTIVE
    Next conversation action is post-implementation learning/ownership from the real code:
    source/control/evidence flow, causal de-duplication, closed-vs-unresolved semantics,
    responsibility placement, focused test intent, and proof limits.

E — PENDING
    Use Ali's D answers to repair important gaps only, then orient the later F3 executable-validation evidence slice.
```

### Deferred F3 executable-validation slice

This later slice begins only when an executable path is actually available:

```text
A — exact proof claims + expected failure/pass meaning
B — focused evaluator → integration → broad deterministic execution
C — exact commands/results/revision preserved
D — interpret proof/non-proof and diagnose failures if any
E — close F3 on sufficient proof, or orient bounded repair
```

Until that proof executes, do not advance the live engineering route to F9 as if F3 had passed.
