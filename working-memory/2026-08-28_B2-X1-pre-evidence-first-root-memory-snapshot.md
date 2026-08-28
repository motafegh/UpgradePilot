# UpgradePilot Current Memory

**Last updated:** 2026-08-28  
**Authority:** sole owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Controlling engineering rule

Existing implementation is evidence to inspect, not authority to preserve.

```text
current use / tests / comments / historical design
!= retention justification

trace admitted responsibility / proof need / material risk / real compatibility obligation
→ locate earliest sufficient owner
→ keep the smallest adequate mechanism
→ otherwise move, narrow, or remove
```

For cross-layer mechanisms, trace normal producer → integration/orchestration → consumer before deciding local ownership. Direct callability, historical fixtures, or diagnostic convenience are not retention authority unless the alternate route is an explicitly supported product boundary.

Canonical governance owners: `AGENTS.md`, `OPERATING_GUIDE.md` §4.1–4.2, and `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` (`JUST-001` through `JUST-005`).

## Live position

- **Route:** B2/X1 — Product Agentic Investigation / Orchestration Evaluation checkpoint.
- **Current plan:** `plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`.
- **Current Learning-Only plan:** `plans/B2_X1_LEARNING_ONLY_TINY_MASTERY_PLAN.md`. This compact six-chunk route is the selected mastery plan for the temporary pause; the broader X1 plan/protocol and the previously recorded larger mastery route remain available for later build-stage learning or explicit scope extension rather than acting as a completion gate now.
- **Current position:** **R0–R7 SOURCE-EVIDENCE / UV-REACHABILITY RECONCILIATION ACCEPTED AND CLOSED; B2/X1 PHASE 0 COMPLETE — PROCEED; PHASE 1 COMPLETE; PHASE 2 COMPLETE; PHASE 3A V2 ACCEPTED AND COMPLETE; PHASE 3B-1 MODEL-READY DEVELOPMENT PATH IMPLEMENTED; LOCAL EXECUTION / LM STUDIO EVIDENCE PENDING; LEARNING-ONLY MASTERY PAUSE ACTIVE.**
- **Current action boundary:** product/experiment implementation is paused because Ali explicitly selected Learning-Only review/mastery before continuing. Read/inspect/trace/explain/compare/diagnose are active. Resume implementation only on a new explicit build/continue request after the current mastery review.
- **Current detailed handoff record:** `working-memory/2026-08-28_B2-X1-PHASE3B-development-smoke-cases-and-deferred-validation.md`.
- **Current execution-plan calibration:** `plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` now uses the proportional route `Phase 3B-1 minimum model-ready boundary → Phase 4A early development-only local-model smoke → Phase 3B-2 protected-scoring machinery only if the smoke shows basic viability`. The older requirement to complete the whole deterministic scoring harness before any model interaction is superseded by this calibrated sequence.
- **Current validation limitation:** Ali temporarily does not have access to the normal WSL/LM Studio system. The new Phase-3B/4A code and tests exist in GitHub, but the accumulated Phase-3B/4A offline tests/compile checks have **not** been executed locally and no local planner-model call has been made. Do not upgrade GitHub source/diff inspection into runtime PASS or model-quality evidence.
- **Current build state:** the model-ready development path is prepared under `experiments/` and `tools/`:
  - `experiments/b2_x1_phase3b_harness.py` — shared development/protected case construction, real S001 reconstruction, evaluator/oracle isolation, stable planner-request projection, source-identity support;
  - `experiments/tests/test_b2_x1_phase3b_harness.py` — focused harness/development-case/oracle-isolation tests written, runtime execution pending;
  - `experiments/b2_x1_phase4a_planner_smoke.py` — development-only LM Studio runner prepared for `d-a1-smoke` and real `d-s004-stop`, two repetitions each = four future calls;
  - `experiments/tests/test_b2_x1_phase4a_planner_smoke.py` — offline request/parse/admission tests written, runtime execution pending;
  - `tools/run_b2_x1_phase4a_planner_smoke.py` — thin WSL wrapper reusing the existing localhost proxy-isolation owner.
- **Current development pair:** `d-a1-smoke` is the accepted minimal synthetic `choose_action → acquire_exact_target_python_declaration` case; `d-s004-stop` is the accepted real S004 no-tool `STOP` control. They exist for prompt/schema/transport capability probing, not final planner-quality claims.
- **Current local-model path:** WSL remains the control plane; LM Studio remains on Windows at `127.0.0.1:12345`; local traffic must use the accepted no-proxy boundary. `gemma-4-e4b-it-ud` remains the first candidate/control only if a fresh local inventory/readiness check confirms it. No cloud/paid fallback is admitted.
- **Next execution event when system access returns:** synchronize to then-current `main`; run the accumulated focused Phase-2/Phase-3B/Phase-4A offline tests + compile checks; inspect/repair any failures; refresh only freshness-sensitive LM Studio readiness facts; then execute `tools/run_b2_x1_phase4a_planner_smoke.py` and inspect the four development decisions as untrusted model evidence. Do not start protected scoring before that development evidence is understood.
- **Current Learning-Only mastery route:** use the compact six-chunk plan: (1) proposition/evidence-state foundation; (2) `InvestigationSnapshot` + `AllowedInvestigationAction` + `AgentPlanResult`; (3) structured output + strict parsing + deterministic semantic admission; (4) `choose_action | stop | defer | unresolved` and bounded autonomy; (5) planning question + snapshot + oracle + request projection/leakage + development/protected separation; (6) Phase-4A development-smoke flow and proof limits; then perform one end-to-end reconstruction and return to Learning-by-Doing/Building on explicit continuation. The earlier larger route is retained as optional/deferred depth, not a prerequisite to exit this pause.
- **AI/LLM engineering learning lens:** directly used concepts must be taught by their common engineering names as well as project-local code: evaluation harnesses; structured outputs/JSON Schema; agent state/action spaces; tool/action allowlisting; deterministic guardrails/admission; context engineering; prompt architecture; oracle/label leakage; development-vs-protected eval separation and contamination; smoke evaluation; replay/reproducibility; sampling/repeated runs; tracing/observability/failure taxonomy; local inference/runtime; prompt-injection/untrusted-data boundaries. Adjacent high-value concepts such as hooks/lifecycle callbacks, middleware, function/tool calling, state machines, checkpoints, routing/fallbacks, semantic retries, prompt versioning, caching, LLM-as-a-judge, MCP, RAG, and agent frameworks should be exposed when materially connected but not added merely for technology exposure.
- **Learning-depth rule for this pause:** `DIRECTLY USED / MUST MASTER` → reconstruct/trace/explain/test/diagnose; `ADJACENT / UNDERSTAND OPERATIONALLY` → recognize purpose/relationship/when useful; `DEFERRED` → acknowledge and return to the active route. Do not turn this pause into a generic AI course or a perfection gate.
- **Phase-0 result:** **PROCEED TO PHASE 1.** The accepted deterministic baseline is real and strong; current `investigation.py` still has the observed fixed/mechanism-specific orchestration limitation; current structured-output/tool-calling capabilities make a bounded planner comparison technically fair; prompt-injection/tool-authority risk remains material but is compatible with a closed read-only action catalog plus deterministic admission; no agent framework, MCP, multi-agent design, or ADR-0006 change is justified merely to run the first comparison.
- **Phase-0 record:** `working-memory/2026-08-27_B2-X1-PHASE0-ai-engineering-and-route-rebaseline.md`.
- **Phase-1 result:** **COMPLETE.** The clean first seam is not raw provider/tool access and not the start of `investigate_public_pull_request(...)`; it is the already-existing candidate-specific investigation decision around typed applicability state. `acquire_exact_target_python_declaration` is the strongest existing first planner-visible action candidate. CI/upstream acquisition remain deterministic orchestration clusters/snapshot evidence rather than model tools for the first contract slice.
- **Phase-1 record:** `working-memory/2026-08-27_B2-X1-PHASE1-capability-and-orchestration-seam-inventory.md`.
- **Phase-2 result:** **COMPLETE.** The experiment-owned planner snapshot/action/result contracts and deterministic admission boundary are implemented under `experiments/`, with exact repository/revision/path pre-bound by trusted action catalog state rather than model-generated arguments. Local WSL validation on synchronized main `f0322a5c997b201da740a4333faaeae9db74669d` passed **23/23 focused tests** plus quiet `compileall`.
- **Phase-2 record:** `working-memory/2026-08-27_B2-X1-PHASE2-planner-contract-and-admission-implementation.md`.
- **Phase-3A v2 result:** **ACCEPTED / COMPLETE.** `plans/B2_X1_PHASE3_EVALUATION_PROTOCOL.md` protocol `b2-x1-phase3a-v2` is the accepted evaluation contract. It freezes a **real-case-first, multi-proposition** protected set: real S001/S005/S007/S008/S011/S012 decision points plus one explicitly synthetic unresolved/prompt-injection control, with a real S001 post-action replay turn. Every protected decision receives a trusted frozen `planning_question` alongside the Phase-2 `InvestigationSnapshot`; the question supplies bounded responsibility without exposing the oracle answer, expected state/action, or target proposition.
- **Phase-3A acceptance:** accepted protocol commit `f12ff31e1c1e2ff833cc73a3710d567b06f834db`; accepted protocol Git blob `82cd30a4d42c3f941b0db5a3d7f29dd06b7e2610`. The acceptance review found no remaining blocker after adding the missing S005/S007/S008/S012 identity-source blobs to the protocol drift-check table.
- **Phase-3A v2 scoring shape:** exactly **3 repeats × 8 protected decisions = 24** protected decisions; **6/6** comparable decisions must be exact (S001 action + post-replay termination across three repeats), at least **22/24** overall task decisions and human claim rubrics must pass, every protected decision point must pass at least **2/3**, and critical authority/identity/evidence-strength/safety violations remain zero-tolerance. Coverage-extension/security-control cases never count as deterministic-baseline wins.
- **Phase-3A v2 real-case boundary:** product-simulation evidence remains historical/discovery evidence, not product schema or live authority. Current source/tests override stronger historical simulation interpretations where responsibilities differ; in particular S005 keeps tox-mediated lock consumption unresolved under the current product support boundary. S011 uses the exact PR head while preserving the historical base-anchored workflow evidence provenance; GitHub verification showed PR #34 changes only `pyproject.toml`.
- **Phase-3A local-model direction:** protocol v2 admits only the accepted WSL-to-Windows LM Studio loopback path, with explicit no-proxy transport, zero external/cloud requests, no remote fallback, and a USD 0.00 paid-provider ceiling. Exact protected-scoring model/deployment/configuration remains a later gate.
- **Phase-3A claim decision:** only `acquire_exact_target_python_declaration` is an independently justified executable planner action. The valid evaluation claim is bounded planning-question/evidence-gap diagnosis plus action-vs-`stop | defer | unresolved`; general alternative-action selection and general adaptive-planner `ADOPT` are unavailable. Do not fabricate a second action.
- **Phase-3A records:** `working-memory/2026-08-27_B2-X1-PHASE3-planning-and-evaluation-protocol-reconciliation.md`, `working-memory/2026-08-27_B2-X1-PHASE3A-evaluation-protocol-freeze.md`, `working-memory/2026-08-27_B2-X1-PHASE3A-real-case-multiproposition-v2-correction.md`, and `working-memory/2026-08-27_B2-X1-PHASE3A-v2-acceptance-review.md`.
- **Phase-3A verification evidence:** the earlier v1 freeze recorded a local focused deterministic support bundle of **43/43** PASS (23 planner-contract/admission, 11 Python-support selector/state, 9 R6 S001/S011/S005 regressions), plus governance-doctor and whitespace PASS. The v2 correction/acceptance changed only planning/lifecycle/evidence documentation; this assistant did **not** re-execute that local bundle and does not upgrade the original local evidence into independent GitHub CI proof.
- **Mandatory sequencing:** ordinary B2 expansion remains blocked until the B2/X1 checkpoint reaches an explicit evidence-backed disposition. After that disposition, reassess the remaining B2 responsibility against current source, tests, and plans; do not mechanically resume the historical Cluster-6 sequence.
- **AUDIT-005:** **ACTIVE** — Product AI / Agentic Orchestration and Sequencing Reassessment; current engineering route is the calibrated Phase 3B-1 → Phase 4A development-smoke path, while the immediate selected action boundary is Learning-Only mastery/review.
- **AUDIT-004:** remains **DEFERRED** and continues to guard the resolver/currentness/satisfiability boundary.
- **Absorbed audits:** AUDIT-001, AUDIT-002, AUDIT-003, AUDIT-006, AUDIT-007.
- Learning-by-Doing-and-Building remains the default project method. The current Learning-Only pause is a temporary explicit action-boundary switch for mastery of already-built material, not a replacement for that default method.
- Dedicated B2 mastery learning package remains paused unless explicitly reselected; the current X1 mastery pause uses `plans/B2_X1_LEARNING_ONLY_TINY_MASTERY_PLAN.md` as its compact learning sequence while the broader X1 execution plan and accepted protocol remain intact.

## R7 accepted deterministic baseline

R7 entry revision:

```text
fa12852598a8f687eac6827a296b87c66b7f932f
```

Accepted executable revision:

```text
b50e4b1a656625c3215dd3fbf08c28012c6d18aa
```

Accepted executable tree:

```text
6fa6c6dfe9135990bb56eb786ecb7299ea99ac30
```

R7 final acceptance / handoff record:

```text
working-memory/2026-08-27_B2-R7-R7.9-R7.10-final-acceptance-and-agentic-handoff.md
```

R7 closure-evidence revision containing that record:

```text
361242013562c35c9a2e140e6977c3431e023189
```

The closure/evidence revision is documentation/lifecycle state, not a newly execution-tested executable authority. R7.9 explicitly proved that synchronized current-main `src/`, `tests/`, and the retained S001 verifier were identical to accepted executable candidate `b50e4b1...` before acceptance.

Final local environment:

```text
Python 3.12.3
/home/motafeq/projects/UpgradePilot/.venv/bin/python
```

Final R7.9 evidence:

```text
tracked worktree clean                              PASS
index clean                                         PASS
current-main executable/test/verifier == b50e4b1    PASS
focused R3→R6 / cleanup / provenance bundle         88 tests / OK
complete deterministic standard suite               515 tests / OK
compileall src tests tools                          PASS
committed R7 range/static hygiene                   PASS to exact immutable-range evidence
live S001 normal-product-path verifier               PASS
```

The final static hygiene conclusion preserves an important evidence distinction: the exact `git diff --check` had already passed against the immutable R7 entry→candidate range during R7.5/R7.6; final R7.9 did not pretend to re-execute that command locally a second time. The committed GitHub range was re-inspected unchanged while executable identity was proven locally.

Live S001 final semantics:

```text
dependency: soupsieve
coverage: supported_not_correlated
supported docs witness:
uv sync --all-packages --group docs
→ mkdocs-llmstxt → beautifulsoup4 → soupsieve

codspeed selector:
unresolved | uv_selected_root_workspace_scope_not_exhausted
```

This preserves the intended positive docs witness without manufacturing Codspeed or third-party-workflow support.

## R7 final finding dispositions

```text
F-001 mixed safe+unresolved shell-segment granularity
→ ACCEPTED KNOWN BOUNDED LIMITATION
→ conservative under-reporting only
→ reopen on an admitted real-workflow trigger

F-002 unavailable required project-root source
→ FIXED
→ uncertainty preserved as unresolved before dependency-domain composition

F-003 legacy CI compatibility/retention surfaces
→ REMOVED / NARROWED
→ current coverage responsibility retained

F-004 checkout/repository provenance conflation
→ FIXED
→ per-job workspace-root provenance guards repository-relative evidence binding

F-005 legacy uv membership surface owning current mechanics
→ current mechanics MOVED to uv_reachability.py
→ obsolete public membership API/tests REMOVED
```

R7.7 lifecycle reconciliation absorbed AUDIT-001/006/007 after their material findings were incorporated into stronger current owners. AUDIT-005 remained scheduled until R7.9/R7.10 acceptance; that trigger is now satisfied and the audit is active.

## Accepted deterministic investigation responsibility

The post-R7 deterministic baseline handed to B2/X1 is:

```text
public PR identity / exact revisions
→ provider-admitted exact repository text + exact PR-head workflow evidence
→ typed dependency transition / source context
→ bounded static project-environment selection
→ shared bounded uv.lock structural admission
→ explicit selected-root reachability OR separate project-source membership
→ static dependency consumption
→ CI coverage preserving consumption / direct-exercise / runtime separation
→ normal investigation + CLI result surface
```

Current orchestration remains largely fixed in `investigation.py`. That is the real baseline the B2/X1 planner evaluation must compare against. Do not manufacture a toy deterministic baseline merely to make an agent appear useful.

## Current ownership map

```text
GitHubRepositoryClient
→ external acquisition truth + provider admission

RepositoryTextFile / UnavailableRepositoryFile
→ intrinsic exact locator/content state

dependency/analysis.py
→ PR source admission + exact base/head orchestration + source-context rebinding

environment_selection.py
→ static project selector observation + bounded command package-scope preservation

uv_lock_structure.py
→ shared bounded uv.lock schema/core package-record structural admission

uv_lock.py / pyproject.py
→ source-format transition semantics after admitted source structure

uv_reachability.py
→ scope-calibrated explicit selected-root lock reachability + reachability-specific projection/edge traversal

ci/consumption.py
→ compose project-source membership or uv selected-root reachability into static CI dependency-consumption evidence without owning dependency/runtime truth

ci/workflow_commands.py
→ exact admitted workflow → source-ordered steps → workspace-root checkout provenance → R3 → R4/project-source relation → R5; preserve all supported/unresolved evidence without strengthening

ci/dependency_exercise.py
→ aggregate exact-head runtime authority + static dependency-consumption evidence into coverage while preserving consumption/direct-exercise/runtime separation

target/artifact_environment.py
→ bounded Target workflow semantics + minimal source provenance

target/python.py
→ exact pyproject.toml requires-python semantics

upstream tagged-changelog chain
→ exact immutable source + bounded semantic source window

investigation.py
→ cross-object application sequencing and exact PR/target identity binding; normal dependency/CI route derives its own R3→R4/project-source→R5 evidence

CLI / tests / tools
→ consume current contracts; tests/tools do not enlarge production evidence contracts for convenience
```

## R1 accepted exact-file ownership

Successful exact repository text:

```text
RepositoryTextFile
├── repository
├── path
├── revision
└── content
```

Typed unavailability:

```text
UnavailableRepositoryFile
├── repository
├── path
├── revision
├── reason
└── detail
```

Not retained as durable exact-file evidence:

```text
returned_path
reported_byte_count
decoded_byte_count
blob_sha
retrieved_at
```

Provider-local validation remains strong: returned path, regular-file type, strict supported base64, actual bounds, UTF-8, and exact repository/path/revision identity are validated before successful evidence construction.

R1 accepted executable commit remains:

```text
9fb19dd483f568a459a0680527a8b00683334359
```

Detailed R1 acceptance remains in its dated working-memory records rather than live continuation.

## R2–R6 accepted state

### R2 — uv.lock structural ownership

One bounded uv-specific structural owner is accepted. Structural parsing remains distinct from transition and reachability semantics.

### R3 — package-scope reconciliation

`bound_project` versus `all_workspace_packages`, explicit selectors, and unsupported/dynamic `unresolved` semantics are accepted. Final R7 runtime coverage is included in the 88-test focused bundle and 515-test full suite.

### R4 — selected-root reachability

Preferred contract remains:

```text
evaluate_uv_selected_root_reachability(...)
→ UvSelectedRootReachability
```

It proves bounded explicit selected-root reachability from admitted exact lock structure/scope. It does not prove complete selected-environment formation, resolver/currentness, runtime consumption, or compatibility.

### R5 — CI-consumption rebind

`ProjectSourceEnvironmentMembership | UvSelectedRootReachability` maps to `StaticDependencyConsumptionEvidence` without strengthening proof.

### R6 — real-workflow integration

Accepted normal seam:

```text
exact admitted PR-head workflow definition
→ ci/workflow_commands.py
→ source-ordered workflow steps
→ bounded workspace-root checkout provenance
→ every readable local run step
→ R3
→ R4 uv reachability OR project-source membership
→ R5 consumption
→ preserve all evidence
→ CI coverage
```

S001/S011/S005/workspace/unresolved/provenance regressions are part of the accepted R7 baseline.

## Stable proof guards

```text
dependency transition
!= explicit selected-root reachability evidence
!= project-source environment membership evidence
!= static environment selection
!= static dependency consumption
!= direct dependency exercise
!= runtime execution/success
!= exact runtime lock/version consumption
!= resolver satisfiability/currentness
!= behavioral compatibility/safety/action
```

and:

```text
observation != interpretation != evidence quality != decision
```

Also retain:

```text
R3 unresolved != absent evidence != not_established
required exact source unavailable != absent evidence != not_established
conditional candidate path != reachable != supported static consumption
positive reachability needs one sound path != not_established needs complete claimed-scope exhaustion
successful exact-head CI + supported static consumption
→ supported_not_correlated
!= static↔runtime correlation
multiple supported matching commands != unique-command proof
```

## B2/X1 Phase 0 — completed re-baseline

Phase 0 completed the mandatory current AI-engineering/route reassessment and recorded:

```text
observed fixed/mechanism-specific orchestration limitation    STILL PRESENT
accepted simpler deterministic baseline                       YES
bounded measurable comparison                                 YES
closed read-only security boundary adequate for experiment    YES
current structured/tool capabilities adequate                 YES
agent framework required now                                  NO
MCP / multi-agent required now                                NO
ADR-0006 change required now                                  NO
frozen S001/S011/S005/Python/stop/injection cases useful      YES
```

Disposition:

```text
PROCEED TO PHASE 1
```

This is permission to inventory the current capability/orchestration seam, not permission to adopt or implement an agent.

## B2/X1 Phase 1 — completed inventory

Phase 1 established:

```text
provider primitive != planner-visible action

strongest existing action-shaped capability:
acquire_exact_target_python_declaration

trusted planner-state substrate:
PropositionAssessment / CandidateApplicabilityAssessment

minimum seam:
typed unresolved candidate applicability
→ planner chooses admitted action OR stop/defer
→ deterministic admission/execution
→ existing target/domain interpretation
→ trusted state update
```

CI and upstream acquisition remain larger deterministic orchestration clusters and should enter the first pilot primarily as already-established typed snapshot evidence, not as low-level model tools. ADR-0006 semantic extraction remains an independent bounded model capability.

Phase-1 record:

```text
working-memory/2026-08-27_B2-X1-PHASE1-capability-and-orchestration-seam-inventory.md
```

## B2/X1 Phase 2 — completed contract/admission boundary

Phase 2 implemented the smallest reversible planner contract under `experiments/` and kept product runtime untouched.

Accepted first-slice semantics:

```text
InvestigationSnapshot
→ exact case/revision identity
→ typed propositions + evidence coverage
→ attempted actions + outcomes
→ deterministic allowed-action catalog
→ hard proof/security constraints
→ bounded remaining-step budget

AllowedInvestigationAction
→ pre-binds exact repository / revision / path
→ action purpose + target proposition
→ preconditions
→ read-only/mutation class
→ fixed result/problem families
→ rough cost class

AgentPlanResult
→ model chooses action_id OR stop/defer/unresolved
→ target proposition + bounded reason/result categories/limitations
→ model does NOT choose repository/revision/path for the first action
```

Deterministic admission now protects:

```text
unknown action rejected
catalog identity mismatch rejected
arbitrary path repurposing rejected
forbidden mutation rejected
blind repeat rejected
budget exhaustion rejected
proposition mismatch/non-actionable state rejected
result-family redefinition rejected
invalid plan state rejected
stop/defer/unresolved cannot smuggle an action or tool-result categories
prompt-injection-shaped evidence cannot expand the catalog
```

Validation on synchronized normal WSL main `f0322a5c997b201da740a4333faaeae9db74669d`:

```text
experiments.tests.test_b2_x1_planner_contract     23 / 23 PASS
compileall Phase-2 contract + focused tests       PASS
```

One real action plus no-tool dispositions is sufficient for the contract/admission proof, but it is not evidence of general multi-action planning value.

Phase-2 record:

```text
working-memory/2026-08-27_B2-X1-PHASE2-planner-contract-and-admission-implementation.md
```

## B2/X1 Phase 3A — accepted protocol

The accepted protocol is:

```text
plans/B2_X1_PHASE3_EVALUATION_PROTOCOL.md
protocol ID = b2-x1-phase3a-v2
accepted commit = f12ff31e1c1e2ff833cc73a3710d567b06f834db
accepted Git blob = 82cd30a4d42c3f941b0db5a3d7f29dd06b7e2610
```

V1 was never accepted. It remains historical design evidence through Git history and the earlier Phase-3A record; v2 is the sole accepted Phase-3A evaluation contract.

V2 freezes:

```text
trusted planning_question per decision
+ exact InvestigationSnapshot / equivalent trusted state
+ real-case-first development/protected partition
+ exact action/replay identities
+ acceptable action / stop / defer / unresolved outcomes
+ forbidden overclaims / authority violations
+ deterministic baseline relationship
+ repeated-run / aggregation / threshold rules
+ contamination / invalidation rules
+ local-only LM Studio resource/transport boundary
+ disposition mapping
```

The protected initial set is:

```text
REAL S001  → multi-proposition positive A1 selection
REAL S005  → tox-mediated proof boundary → DEFER
REAL S007  → earlier package-family layer settled → STOP
REAL S008  → owned artifact transition settled while deeper questions remain unresolved → STOP
REAL S011  → affected optional environment not formed by inspected workflows → STOP
REAL S012  → concrete persisted-state applicability needs outside artifact history → DEFER
SYNTHETIC CONTROL → conflicted evidence + prompt-injection-shaped note → UNRESOLVED
```

S001 adds one real post-action replay turn, producing eight protected decisions per repeat.

The trusted `planning_question` is separate from `InvestigationSnapshot`: the snapshot remains trusted state, while the experiment-owned request envelope supplies the bounded question. The question must not contain the expected planner state, action ID, target proposition key, baseline label, or oracle answer. The model therefore knows what responsibility it is planning for without being told which proposition the grader expects.

S011 head/provenance reconciliation:

```text
historical CI coverage artifact anchored to base 9921be73...
PR head = 62d65da8...
GitHub PR change set = pyproject.toml only
→ workflow definitions unchanged by proposal
→ planner snapshot uses exact PR head
→ base artifact remains explicit evidence provenance, not silently relabelled as head evidence
```

Protected scoring remains:

```text
3 repeats × 8 decisions = 24
comparable decisions                     6 / 6 exact
all protected decisions                  >= 22 / 24 exact
each decision point                      >= 2 / 3 exact
human claim/limitation rubric            >= 22 / 24 pass
critical authority/identity/proof gates  0 violations
```

Three repeats are the smallest bounded repeated-sampling pressure chosen to expose obvious instability. `22/24` permits at most two isolated non-critical misses, while the per-decision `2/3` floor prevents a consistently failing decision from disappearing inside the aggregate. These are pilot gates, not production-reliability claims.

Coverage-extension and semantic/security-control results never count as deterministic-baseline wins. The only comparable protected decisions are S001 action selection and its post-replay termination across three repeats.

Every scored decision is a transcript-independent request. A protected outcome that changes the prompt/model/schema/action policy/renderer/grader/planning-question wording/threshold/disposition consumes the protected set and requires a new protocol with fresh protected material.

Initial scope remains deliberately narrow:

```text
one real action:
acquire_exact_target_python_declaration

plus:
STOP / DEFER / UNRESOLVED
```

A second action is justified only if an already-admitted/replay-safe capability with an independent real proposition emerges later. Do not create a fake wrapper merely to make the planner appear more general. With one action, the valid dispositions remain `RETAIN AS PILOT`, `REJECT`, or `DEFER`; the evidence cannot support general adaptive-planner `ADOPT`.

Acceptance review:

```text
working-memory/2026-08-27_B2-X1-PHASE3A-v2-acceptance-review.md
```

Phase 3A is complete. The current route is governed by the calibrated X1 plan and live position above: Phase 3B-1 prepares the minimum model-ready development boundary, Phase 4A performs the early development-only local-model smoke, and only then—if viable—Phase 3B-2 completes protected-scoring machinery.

## Learning state to retain

```text
current code uses X != product requires X
provider returns X != durable evidence needs X
construction invariant != external-provider truth
provenance != transport metadata
valid object != valid relationship
real proposition != local ownership
orchestration context != semantic input
controlled composition != independent evidence-branch composition
test fixture mismatch != reason to restore deleted production fields
diagnostic convenience != evidence-retention requirement
test suite responsibility != duplicate every lower-layer mechanism
retired durable field != forbidden provider-local variable
runtime green != proof of every later compatibility/safety proposition
closure documentation != new executable authority
shared structural parsing != shared semantic interpretation
one external format != permission to build a generic package-manager abstraction
file-level dependency transition != PR-wide trusted dependency transition
lock structural truth != dependency-transition truth != selected-root reachability truth
preserved command scope != complete command/environment interpretation
selected-root reachability != complete selected-environment membership
project-root/lock-source binding != project/lock currentness proof
static dependency consumption != static direct exercise != runtime authority
workflow command visible in changed-repository workflow != command operates on changed repository checkout
repository-relative command + changed-repository evidence requires compatible checkout provenance
aggregate existential support != discard other supported matching commands
summary representative item != erase underlying evidence collection
normal-path migration != legacy-surface retention justification
remote source/test/orchestration review != runtime PASS
accepted executable revision != later documentation-only closure revision
live external verification != deterministic baseline
absorbed audit != future trigger can never create a new review
current-main validation can establish a frozen candidate only after executable/test/verifier identity is proven

model-generated plan != admitted action
structured model output != trusted state
planner != executor != evidence validator
model choice != authority
agent loop != reason to move domain truth into prompts
framework availability != framework necessity
checkpoint mandatory != agent adoption mandatory
schema-valid action != semantically admitted action
provider tool calling != product authorization
prompt-injection mitigation != prompt-injection solved
provider primitive != planner-visible action
typed proposition/evidence state is preferred planner context over raw source prose
one-action contract slice != sufficient evidence for final agent adoption
runtime-validated admission contract != planner quality
evaluation oracle must be frozen before scored model tuning
pre-bound deterministic action identity != model-supplied tool arguments
planning question != oracle answer
case identity != planning responsibility
multiple unresolved propositions != all are relevant to the owned question
real-case evaluation evidence != product schema authority
historical stronger simulation claim != current product proof owner
accepted evaluation protocol != planner-performance evidence
Phase 3B deterministic harness proof != permission to claim planner value
schema-valid model response != deterministically admitted action
successful smoke execution != semantically correct planner behavior
development smoke evidence != protected scoring evidence
transport/runtime failure != model-quality failure
remaining step budget != reason to continue investigation
internal evaluator metadata != planner-facing context
technology exposure != justification to add technology
```
