# Working Memory — B2/X1 Phase 1 Capability and Orchestration-Seam Inventory

**Date:** 2026-08-27  
**Status:** PHASE 1 COMPLETE — PHASE 2 NEXT  
**Current plan:** `../plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`  
**Phase-0 record:** `2026-08-27_B2-X1-PHASE0-ai-engineering-and-route-rebaseline.md`  
**Accepted deterministic executable baseline:** `b50e4b1a656625c3215dd3fbf08c28012c6d18aa`

## 1. Phase-1 responsibility

Phase 1 is a read-only inventory. It does **not** create planner types, refactor `investigation.py`, add a provider/model/framework, or move domain truth into prompts.

The question is narrower:

> Which already-admitted UpgradePilot capabilities are relevant to a first bounded planner, and where is the smallest seam at which a planner could choose one next action or stop/defer while deterministic code still owns authority, execution, interpretation, and evidence promotion?

## 2. Important distinction: provider primitive != planner-visible action

The current source contains many safe read-only provider calls, for example:

```text
GitHubPullRequestClient.get_pull_request(...)
GitHubPullRequestClient.get_changed_files(...)
GitHubActionsClient.get_exact_head_workflow_runs(...)
GitHubActionsClient.get_workflow_jobs(...)
GitHubRepositoryClient.get_exact_head_workflow_file(...)
GitHubRepositoryClient.get_exact_head_text_file(...)
PyPIReleaseClient.get_release(...)
PyPIReleaseIndexClient.get_release_index(...)
GitHubChangelogPathClient.discover(...)
```

These are **not automatically planner tools**.

A planner-visible action should correspond to a meaningful investigation proposition, not expose every transport call and force the model to reconstruct domain sequencing that the deterministic product already owns.

Controlling rule:

```text
provider primitive
!= planner action

planner action
→ one bounded investigation purpose
→ exact preconditions / identity
→ deterministic execution through existing owners
→ typed result/problem
```

## 3. Current capability inventory relevant to the first planner

### C1 — Exact pull-request / changed-file acquisition

Current owners:

```text
src/upgradepilot/github/pull_request.py
→ GitHubPullRequestClient.get_pull_request(...)
→ GitHubPullRequestClient.get_changed_files(...)
```

Inputs:

```text
public repository identity
pull number
then trusted PullRequestIdentity
```

Results:

```text
PullRequestIdentity
ChangedFile[]
```

Proposition advanced:

```text
exact PR identity + immutable base/head + complete changed-file set
```

Cannot prove:

```text
dependency semantics
CI consumption
impact/applicability
compatibility/safety/action
```

Security/cost:

```text
public read-only GitHub network
provider validates identity/pagination
low-to-moderate network cost
```

Planner disposition for first pilot:

```text
NOT EXPOSED AS A PLANNER ACTION
```

Reason: this is mandatory entry identity, not an adaptive evidence-gap choice.

### C2 — Dependency transition / source-context analysis

Current owner:

```text
src/upgradepilot/dependency/analysis.py
→ analyze_dependency_change(...)
```

Inputs:

```text
PullRequestIdentity
complete ChangedFile[]
GitHubRepositoryClient for exact source acquisition
```

Result family:

```text
DependencyChangeAnalysis
or DependencyChangeProblem
```

Proposition advanced:

```text
one admitted dependency transition + exact source contexts
```

Planner disposition:

```text
NOT EXPOSED AS A FIRST-PILOT ACTION
```

Reason: it establishes the typed state from which the bounded investigation question begins.

### C3 — Exact-head CI dependency coverage branch

Current owners:

```text
GitHubActionsClient.get_exact_head_workflow_runs(...)
GitHubActionsClient.get_workflow_jobs(...)
GitHubRepositoryClient.get_exact_head_workflow_file(...)
_acquire_project_environment_sources(...)
derive_project_environment_consumptions(...)
evaluate_dependency_ci_coverage(...)
```

Inputs:

```text
PullRequestIdentity
DependencyVersionChange
DependencySourceContext[]
exact workflow run/job/file evidence
```

Final result:

```text
DependencyCICoverageResult
```

Proof boundary:

```text
successful exact-head runtime authority
+ static changed-dependency consumption
→ supported_not_correlated

!= runtime correlation of the consuming command
!= exact runtime lock/version consumption
!= compatibility/safety/action
```

Security/cost:

```text
public read-only GitHub network
multiple API/file reads
moderate network cost
```

Planner disposition for first pilot:

```text
KEEP AS ESTABLISHED SNAPSHOT EVIDENCE
DO NOT EXPOSE THE CURRENT MULTI-CALL CLUSTER AS ONE MODEL TOOL YET
```

Reason: the current branch is a larger orchestration cluster rather than one already-defined action contract. Wrapping it only to give the model a tool would manufacture architecture before Phase 2 proves such an action is necessary.

S001/S011/S005 should therefore enter early evaluation primarily as **already-typed evidence states** that test correct stop/defer/proof discipline, not as invitations for the planner to reconstruct R3→R6.

### C4 — PyPI release / trusted upstream-repository / release-window acquisition

Current owners include:

```text
PyPIReleaseClient.get_release(...)
UpstreamRepositoryResolver.resolve(...)
PyPIReleaseIndexClient.get_release_index(...)
GitHub tag/changelog acquisition owners
assemble_upstream_interval_authority(...)
```

Result families include:

```text
PackageReleaseResult
UpstreamRepositoryResult
PackageReleaseIndexResult
CrossedReleaseIndexSelectionResult
GitHubTagCommitResult
ChangelogPathDiscoveryResult
TaggedChangelogCompositionResult
UpstreamIntervalAuthorityResult
```

Proof boundary:

```text
exact package/upstream/release/source authority
!= semantic support-drop claim
!= target applicability
```

Security/cost:

```text
public PyPI + GitHub read-only network
multiple calls
moderate network cost
```

Planner disposition:

```text
NOT EXPOSED AS FIRST-PILOT LOW-LEVEL ACTIONS
```

Reason: the deterministic authority chain is already valuable and security-sensitive. The model should not choose repository/source authority or arbitrary URLs.

### C5 — Bounded upstream support-drop semantic evaluation

Current owners:

```text
src/upgradepilot/upstream/support_drop.py
→ evaluate_support_drop_runtime(...)

src/upgradepilot/upstream/claim.py
→ validate_support_drop_candidates(...)
```

Input:

```text
AuthoritativeUpstreamIntervalEvidence
```

Result:

```text
GroundedPythonSupportDropClaim
or UpstreamSupportDropClaimProblem
```

Current model role:

```text
bounded semantic candidate extraction only
→ ADR-0006 local model
→ exact deterministic grounding/validation mandatory
```

Proof boundary:

```text
grounded upstream Python support-drop claim
!= target relevance
!= compatibility/safety/action
```

Security/cost:

```text
local LM Studio inference
untrusted model output
moderate/high latency relative to pure deterministic code
no model tool authority
```

Planner disposition:

```text
KEEP AS AN INDEPENDENT EXISTING CAPABILITY
DO NOT MERGE THE EXTRACTOR MODEL AND PLANNER ROLE IN THE FIRST PILOT
```

The planner may later reason over its typed result. Extraction success is not evidence of planning capability.

### C6 — Deterministic applicability state

Current owners:

```text
src/upgradepilot/impact/applicability.py
→ PropositionAssessment
→ CandidateApplicabilityAssessment
→ evaluate_applicability_path(...)
→ evaluate_candidate_applicability(...)
```

and mechanism adapter:

```text
src/upgradepilot/impact/python_support.py
→ evaluate_python_support_drop_impact(...)
```

Important state available to a planner:

```text
proposition key
state = established | refuted | unresolved | conflicted
evidence_coverage = sufficient | insufficient | unresolved
evidence owner
detail
candidate/path state
```

Planner disposition:

```text
PRIMARY TRUSTED SNAPSHOT INPUT
```

This is close to the right abstraction level for evidence-gap diagnosis. The planner should consume these typed states; it should not recompute them from raw prose.

### C7 — Existing action-shaped discriminating investigation

Current deterministic selector:

```text
src/upgradepilot/impact/python_support.py
→ select_python_support_drop_investigation(...)
```

Current selected kind:

```text
acquire_exact_target_python_declaration
```

Selection fields already contain:

```text
kind
repository
revision
path
proposition_key
detail
```

Required pre-state:

```text
GroundedPythonSupportDropClaim exists
+ PythonSupportDropImpactAssessment is unresolved
+ exact_target_python_declaration_established proposition is unresolved
+ evidence coverage is insufficient
+ target relevance has not already been attempted/established
```

Execution path already used by `investigation.py`:

```text
GitHubRepositoryClient.get_exact_head_text_file(
    pull_request,
    "pyproject.toml",
)
→ interpret_target_python_declaration(...)
→ TargetPythonEvidence
→ evaluate_target_python_relevance(...)
→ evaluate_python_support_drop_impact(...)
```

Typed success/problem family:

```text
TargetPythonDeclaration
or TargetPythonDeclarationProblem
```

Target relevance result:

```text
TargetPythonRelevanceResult
```

Exact proposition advanced:

```text
Does the exact target head expose an interpretable [project].requires-python declaration,
and does its declared stable range intersect the grounded dropped Python X.Y line?
```

Cannot prove:

```text
runtime environment usage
compatibility/safety
merge readiness
final maintainer action
```

Security/cost:

```text
one exact public GitHub repository-text read
fixed path = pyproject.toml
exact PR head SHA
bounded UTF-8 provider contract
low network cost
no target execution/mutation
```

Repeat/idempotence:

```text
same immutable repository + head SHA + fixed path
→ repeat read is logically idempotent

attempt history should still prevent blind redundant retries after an available/problem result
```

Planner disposition:

```text
STRONGEST FIRST PLANNER-VISIBLE ACTION CANDIDATE
```

This is not invented for X1. It already exists as a real deterministic discriminating investigation.

## 4. Minimum planner seam

The smallest clean seam is **not** at the beginning of `investigate_public_pull_request(...)` and not around raw provider calls.

It is around the already-existing candidate-specific investigation decision:

```text
GroundedPythonSupportDropClaim
→ build_python_support_drop_impact_candidate(...)
→ evaluate_python_support_drop_impact(...)
→ trusted unresolved propositions / evidence coverage

                ┌─────────────────────────────────────┐
                │          FIRST PLANNER SEAM          │
                │ choose admitted action OR stop/defer │
                └─────────────────────────────────────┘
                                  ↓
                deterministic action admission
                                  ↓
acquire_exact_target_python_declaration
→ exact repository/head/path validation
→ GitHubRepositoryClient read
→ interpret_target_python_declaration(...)
→ evaluate_target_python_relevance(...)
→ evaluate_python_support_drop_impact(...)
→ trusted updated state
```

This seam preserves the most important responsibility split:

```text
planner
→ proposes which admitted investigation is useful

admission/executor
→ validates action/state/identity/budget and performs read-only capability

domain modules
→ interpret result and promote trusted evidence state
```

## 5. What Phase 2 should NOT do

Do not start by exposing these as model tools:

```text
arbitrary get_exact_head_text_file(path)
arbitrary GitHub URL
arbitrary PyPI URL
raw workflow-run/job/file primitives
uv parser/reachability internals
direct local model extractor internals
shell/browser/MCP/plugin calls
```

Those would either enlarge authority, allow arbitrary source selection, or make the planner reconstruct already-owned domain orchestration.

## 6. Candidate first action catalog direction

Phase 1 does not freeze the contract, but the evidence supports this starting direction for Phase 2:

```text
planner states:
- choose_action
- stop
- defer
- unresolved

initial real action:
- acquire_exact_target_python_declaration

trusted snapshot includes:
- exact case/revision identity
- typed established/unresolved propositions
- evidence coverage
- prior attempted actions/results
- bounded budget
- admitted action catalog
- hard proof/security constraints
```

A one-action catalog is acceptable for the **first contract slice** because the frozen evaluation set also tests correct stop/defer behavior across S001/S011/S005 and correct selection in the Python-support case. However, Phase 2/3 must explicitly assess whether that is too weak for the owning comparison. If a second action is required for a fair planner comparison, add only an already-admitted capability or replay-safe composite with a real independent proposition—not a wrapper invented solely to make the agent look more general.

## 7. Phase-1 findings

### P1-F1 — clean planner seam exists

**PASS.** The Python-support applicability boundary already exposes typed unresolved propositions and a real discriminating read-only action.

### P1-F2 — provider primitives should remain hidden from the planner

**PASS.** Provider clients remain deterministic authority/execution owners. Exposing them directly would widen scope and duplicate orchestration semantics.

### P1-F3 — CI/upstream chains are not currently single action contracts

**PASS / HOLD.** They are legitimate capabilities but currently fixed multi-step orchestration clusters. Do not refactor them merely to create planner tools during Phase 1.

### P1-F4 — existing semantic extractor remains independent

**PASS.** ADR-0006 model output remains untrusted candidate evidence and should not be merged with planner authority.

### P1-F5 — first planner can start from typed applicability/evidence state

**PASS.** `PropositionAssessment` / `CandidateApplicabilityAssessment` provide a better snapshot substrate than raw repository/upstream prose.

## 8. Phase-1 gate

```text
relevant capability owners mapped                     PASS
current typed inputs/results/proof limits mapped      PASS
security/cost classes identified proportionately      PASS
smallest planner seam identified                      PASS
product refactor required to establish seam           NO
provider/model/framework selection required           NO
product source/test mutation performed                NO
```

## 9. Disposition

```text
PHASE 1 = COMPLETE
NEXT = PHASE 2 — freeze the smallest planner state/action/result contracts
```

Phase 2 should design and test the contract boundary before any model experiment. The contract must deterministically reject unknown actions, wrong repository/revision/path identity, invalid arguments, forbidden mutation classes, blind repeated actions, and over-budget execution; stop/defer must require no tool execution.
