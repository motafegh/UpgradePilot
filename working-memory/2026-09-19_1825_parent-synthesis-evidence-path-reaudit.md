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
