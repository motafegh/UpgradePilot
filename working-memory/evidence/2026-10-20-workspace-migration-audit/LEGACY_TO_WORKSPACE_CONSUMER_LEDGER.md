# Legacy result → Workspace family/material → consumer migration ledger

**Date:** 2026-10-20  
**Purpose:** pre-cutover evidence/ownership ledger required by AUDIT-015/AUDIT-018. This is not implementation authorization.  
**Source horizon:** audit branch with latest reconciled upstream `main@bfcc8b916fc33523a535f7c5a994d118d09552b8`.

## Disposition vocabulary

- **CAPTURED** — current Workspace family already records the relevant semantic owner/result.
- **DERIVABLE** — the legacy presentation value is already retained inside another captured native input/result and should be projected from that owner rather than gain a duplicate family.
- **MISSING FAMILY** — current supported report/synthesis meaning has no admitted Workspace native family/material representation yet.
- **REVIEW / POSSIBLY DROP** — legacy value is not itself an independent semantic responsibility; before adding a family, prove whether a migrated consumer can derive or omit it without losing supported report semantics.
- **WORKSPACE META** — canonical Workspace identity/revision, not a legacy domain evidence family.

The target is not one Workspace family per legacy field. The target is one correct semantic owner/material closure for each still-supported consumer proposition.

## Current ledger

| `PublicPullRequestInvestigation` field | Current semantic owner / origin | Workspace state | Current direct consumers | Migration disposition |
| --- | --- | --- | --- | --- |
| `pull_request` | `github.pull_request` exact PR identity acquired before dependency analysis | **CAPTURED** in `investigation_inputs` | report identity/locators; dependency/CI source locators; exact investigation target | Project consumer projection should read `investigation_inputs.pull_request`. |
| `changed_files` | PR acquisition | **CAPTURED** in `investigation_inputs` | report dependency section/context | Project from `investigation_inputs.changed_files`; no new family. |
| `dependency_result` | `dependency.change` | **CAPTURED** in `investigation_inputs` | report dependency; synthesis decisive reason/uncertainty; downstream producer inputs | Project from `investigation_inputs.dependency_result`; preserve supported/problem variants. |
| `workflow_evidence` | exact-head `WorkflowRun` + `WorkflowJob` tuples acquired for CI preparation | **DERIVABLE** from captured `ci_inputs`: each `WorkflowDependencyCoverageInput` already retains `run` and `jobs` plus static definition/environment sources | report raw workflow execution source identities | Do **not** add a parallel `workflow_evidence` family. Migrate report to enumerate `ci_inputs[*].run/jobs`. Add parity proof that ordering/identity matches current report semantics. |
| `ci_coverage_result` | `ci.dependency_exercise` | **CAPTURED** as `ci_coverage` | report CI assessments; synthesis residual uncertainty | Direct Workspace/native projection. Preserve `None`/problem/state semantics. |
| `runtime_dependency_state_result` | `ci.dependency_state` | **CAPTURED** as `runtime_dependency_state` | report runtime assessments; synthesis residual uncertainty | Direct Workspace/native projection. |
| `package_result` | `pypi.release` proposed release | **MISSING FAMILY** | report package evidence; synthesis upstream uncertainty; input to upstream repository/artifact branches | Add owner-specific package-release family/material only if current package report/upstream consumers remain supported. Preserve exact package/version/file/provenance source identity and problem states; do not rebuild from report text. |
| `upstream_repository_result` | `upstream.repository` | **MISSING FAMILY** | report upstream repository/provenance; synthesis unresolved branch | Add owner-specific family if supported upstream provenance/report path remains. Inputs should bind to retained package/provenance evidence, not a report projection. |
| `release_index_result` | `pypi.release` release-index owner | **MISSING FAMILY** | report upstream/release-window detail; synthesis unresolved branch | Add family only as part of retained upstream-authority producer closure; preserve exact index acquisition/problem identity. |
| `crossed_release_result` | `upstream.interval_evidence.select_crossed_release_index` | **MISSING FAMILY** | report release-window detail; synthesis unresolved branch; upstream authority assembly | Add owner-specific selection family/material if report needs this intermediate state and recovery must explain why authority stopped. Do not replace with only final authority if that would erase a currently surfaced stop reason. |
| `tag_commit_result` | `github.tag` | **MISSING FAMILY** | report upstream source evidence; synthesis unresolved branch; authority assembly | Add/reuse exact tag evidence family only if final authority material closure cannot independently retain the report/source proposition. Preserve problem state. |
| `changelog_path_result` | `github.changelog` | **MISSING FAMILY** | report upstream source evidence; synthesis unresolved branch; tagged changelog composition | Same rule: retain if needed to explain supported current report/stop semantics; otherwise prove derivability/intentional removal before dropping. |
| `tagged_changelog_result` | `upstream.interval_evidence` / `upstream.interval` tagged source composition | **MISSING FAMILY** | report retained changelog source; synthesis unresolved branch; upstream interval authority | High-value missing family/material because report currently preserves tagged source/authority problems. Could become an input/material of `upstream_authority` rather than a consumer-visible duplicate if the authority closure retains exact source text/identity and intermediate failure semantics. Requires design decision. |
| `upstream_interval_result` | `upstream.interval` | **CAPTURED** as `upstream_authority` | report upstream authority/support source; synthesis unresolved branch; support-drop evaluator input | Direct Workspace/native projection. Verify that its retained material closure includes any source needed by migrated report; do not infer missing intermediate stop reasons if final result cannot encode them. |
| `upstream_support_drop_result` | `upstream.claim` / selected support-drop evaluator | **CAPTURED** as `upstream_support_drop` | report support-drop; synthesis unresolved branch; Python impact input | Direct projection; preserve evaluator/method gaps and grounded source references. |
| `target_python_result` | `target.python` from selected repository file | **CAPTURED** inside `target_python` object together with exact source | report target declaration; target relevance input | Direct projection from `target_python.result`; report source locator should use retained `target_python.source`. |
| `target_python_relevance_result` | `target.relevance` | **CAPTURED** as `target_relevance` | report target relevance; Python post-impact input | Direct projection. |
| `python_support_drop_pre_investigation_result` | `impact.python_support` | **CAPTURED** as `python_support_pre_assessment` | report/decision-flow explanation; selection input | Direct projection. |
| `python_support_drop_investigation_selection` | `impact.python_support` selector | **CAPTURED** as `python_support_selection` | conditional target-read/reassessment path; possible report/control explanation | Direct projection; preserve executed `None` versus `not_evaluated` distinction from captured record outcome. |
| `python_support_drop_impact_result` | `impact.python_support` post assessment | **CAPTURED** as `python_support_post_assessment` | report Python impact; synthesis residual uncertainty | Direct projection. |
| `old_package_result` | `pypi.release` old release | **MISSING FAMILY** | report old artifact evidence; synthesis artifact-branch uncertainty; artifact candidate producer | Add package-release family capable of binding role/version (`old` vs proposed) rather than duplicate schema families if the owner semantics are the same. |
| `artifact_serviceability_candidate_result` | `impact.artifact_serviceability` candidate builder over old/new release evidence | **MISSING FAMILY** | report artifact candidate; synthesis artifact uncertainty; impact evaluator input | Add owner-specific family if artifact-serviceability remains supported. Preserve evidence-problem state separately from `None`/not evaluated. |
| `target_artifact_environment_results` | dependency-source contexts + `target.artifact_environment` interpreter | **MISSING FAMILY** | report target artifact-environment associations; synthesis artifact uncertainty; artifact impact evaluator input | Add family that retains **association to exact dependency source identity**, not just a tuple of target results. This association is decision-critical in marker/extra/environment cases. |
| `artifact_serviceability_impact_result` | `impact.artifact_serviceability` | **MISSING FAMILY** | report artifact impact; synthesis residual uncertainty | Add owner-specific assessment family only after candidate + target-environment material closure is representable. |
| `workspace_revision` | Workspace host/checkpoint publication | **WORKSPACE META** | tests/diagnostics; future Workspace consumers | Remove from the future projected domain result as an input field if direct consumers already receive a selected revision/context. Until then retain as migration/debug bridge, not semantic evidence. |

## Native families already admitted

Current `FAMILY_CONTRACTS` intentionally covers the initial CI/runtime + Python-support closure:

```text
investigation_inputs
ci_inputs
ci_coverage
runtime_dependency_state
upstream_authority
upstream_support_drop
python_support_pre_assessment
python_support_selection
target_python
target_relevance
python_support_post_assessment
```

This is a coherent initial closure, not the complete current report responsibility.

## Important design conclusions from the ledger

### 1. Do not add a separate raw workflow-evidence family

`WorkflowDependencyCoverageInput` already contains:

```text
run: WorkflowRun
jobs: tuple[WorkflowJob, ...]
definition: RepositoryFileEvidence
project_environment_sources: ...
```

The migrated report can project exact run/job execution identities from captured `ci_inputs`. A separate `workflow_evidence` family would create avoidable duplicate authority unless a concrete missing proposition is found.

### 2. Package release should likely be one reusable family with role/binding, not old/proposed duplicate types

`package_result` and `old_package_result` share the same `PackageReleaseResult` semantic owner. If capture is added, prefer one owner-specific family representation whose record identity/input binding establishes whether the release is the proposed or old side of the exact dependency transition. Do not create two schemas merely because the legacy result has two fields.

### 3. Upstream intermediate families require a material-closure decision, not mechanical field copying

`release_index_result`, `crossed_release_result`, `tag_commit_result`, `changelog_path_result` and `tagged_changelog_result` exist partly to explain why the upstream-authority branch succeeded/stopped and to preserve source provenance.

Before adding five permanent Workspace roots, inspect whether `upstream_authority` can retain their **exact material/source/problem closure** in a way that preserves all currently supported report/synthesis explanations. If yes, some can become retained material/input records rather than top-level consumer families. If no, preserve the missing intermediate owner explicitly.

The deciding question is information/authority loss, not one-field/one-family symmetry.

### 4. Artifact environment association is semantically important

`target_artifact_environment_results` pairs each target-environment interpretation with the exact `DependencySourceContext` that activated it. Migration must preserve that source-to-environment relation. A flat target-environment list would weaken evidence and break later marker/extra/environment reasoning.

### 5. Cutover should consume a Workspace projection, not reconstruct a new monolithic snapshot first

The ledger does **not** imply recreating `PublicPullRequestInvestigation` inside Workspace as another giant snapshot. The ADR target remains explicit owner-specific families/material plus consumer projections.

A temporary legacy projection may exist for parity proof, but the desired normal path is:

```text
Workspace selected revision
→ explicit consumer projection(s)
→ synthesis/report
```

## Minimum cutover proof matrix

Before synthesis/report migration, prove every row marked CAPTURED/DERIVABLE/MISSING FAMILY that remains in supported user-facing semantics across at least these states where applicable:

- normal/available;
- explicit problem/unresolved;
- `not_evaluated`/non-activation;
- unsupported/not-applicable;
- recovery from durable checkpoint for families required after restart.

For overlapping legacy/current paths during migration, compare **semantic meaning and evidence strength**, not only structural equality.

After direct consumers cut over and the legacy bridge is retired, remove parity tests whose only purpose was dual-surface comparison.

## Next architecture decision

The next Workspace migration design should resolve two clusters rather than field-by-field code edits:

1. **package/upstream material closure** — package old/new, repository provenance, release index/window/tag/changelog source chain and authority explanation;
2. **artifact-serviceability closure** — old/new package artifact facts, source-bound target artifact environments, candidate and impact assessment.

Each cluster should decide which records are native result families versus retained material/input records before implementation. CI/Python-support does not need redesign.

## Stop

This ledger does not authorize implementation. It establishes the minimum owner/material/consumer map needed to design the next Workspace migration increment without copying the legacy dataclass wholesale.
