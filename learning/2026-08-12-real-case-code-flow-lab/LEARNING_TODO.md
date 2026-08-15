# UpgradePilot Learning TODO

**Broad rules:** [`LEARNING_PLAN.md`](LEARNING_PLAN.md)  
**Latest orientation:** [`2026-08-15_CLUSTER_3_VALIDATED_LEARNING_FRONTIER.md`](2026-08-15_CLUSTER_3_VALIDATED_LEARNING_FRONTIER.md)  
**Synchronized product baseline:** `main@72eb291e6ffc9112956e37f34dc5c7f7e3c40154`  
**Learning-branch sync merge:** `35bc756f02c6afd044d80ab545ae5b860ec87b2a`

## Status

- `[x]` covered
- `[ ]` open
- `▶ CURRENT` recommended current target unless Ali redirects
- `NEXT` likely continuation
- `POSTPONED` intentionally open, not complete
- `WAIT FOR MAIN` implementation not yet present

Skipped/postponed work stays unchecked. Later work may become current before earlier work is completed.

---

## 0. Learning lab

- [x] Dedicated learning branch/workspace created.
- [x] Broad learning plan written.
- [x] Learning-order override and prerequisite-recovery rule added.
- [x] Historical August 14 orientation preserved.
- [x] Phase-E Cluster-2 transition checkpoint preserved.
- [x] Re-synced through validated Cluster-3 pause on `main@72eb291e6ffc9112956e37f34dc5c7f7e3c40154`.
- [x] Current Cluster-3 learning frontier recorded.

**Preserved learning state:** no item below is checked merely because implementation exists. A concept/code responsibility becomes covered only after Ali demonstrates the intended level of understanding/practice.

---

## 1. Recent Phase-E foundation through Cluster 3 `▶ CURRENT`

Current product state:

```text
✓ Cluster 0 — green baseline
✓ Cluster 1 — PyYAML parser boundary
✓ Cluster 2 — typed static GitHub Actions workflow IR
✓ Cluster 3 — shared direct-install declaration observation

PAUSE before Cluster 4 — Target migration
```

Learning strategy for this block:

```text
frontier first
→ step backward only for blocking context
→ return to newest implementation
```

### 1A. Minimal architecture reason — a little backward

- [ ] Locate the existing Target workflow reader in `target/artifact_environment.py`.
- [ ] Locate the existing CI workflow reader in `ci/workflow_commands.py`.
- [ ] Identify the provider structure they independently reconstruct.
- [ ] Identify domain conclusions that must remain separate.
- [ ] Explain why duplicated GitHub Actions parsing became an architecture/proof-strength problem, not merely duplicated code.
- [ ] Explain the central proof ladder:

```text
static declaration
!= runtime execution
!= runtime success
!= environment formation
!= dependency exercise
```

### 1B. ADR-0008 boundary

- [ ] Trace `RepositoryTextFile → GitHub Actions static IR → CI / Target`.
- [ ] Explain why the shared representation belongs to `upgradepilot.github`.
- [ ] Explain why runtime `WorkflowRun` / `WorkflowJob` / `WorkflowStep` remain separate.
- [ ] Explain why valid dynamic values are readable static evidence rather than parser failure.
- [ ] Explain why `needs` and source order do not establish runtime environment continuity.

### 1C. Cluster 1 — parser foundation

Teach only the depth needed to understand current Cluster-2/3 code.

- [ ] Why PyYAML replaced expansion of custom indentation parsing as the shared syntax foundation.
- [ ] `yaml.compose(...)` at the depth used here.
- [ ] `BaseLoader` textual scalar preservation.
- [ ] `MappingNode`, `SequenceNode`, `ScalarNode`.
- [ ] block scalar decoding (`run: |`, `run: >`).
- [ ] source marks.
- [ ] duplicate mapping-pair visibility.
- [ ] controlled malformed-YAML failure.
- [ ] recursive-alias / depth / node-count safeguards.
- [ ] PyYAML nodes remain private parser machinery.

### 1D. Cluster 2 — typed static workflow IR

Current provider contracts include:

```text
SourceSpan
StaticScalarValue / StaticSequenceValue / StaticMappingValue
RunDefaults
RunStepDefinition / UsesStepDefinition / StepProblem
StepsJobDefinition / ReusableWorkflowJobDefinition / JobProblem
WorkflowDefinition / WorkflowDefinitionProblem
parse_workflow_definition(...)
```

- [ ] IR = Intermediate Representation: practical meaning in UpgradePilot.
- [ ] Why PyYAML nodes are translated into UpgradePilot-owned provider objects.
- [ ] Trace `RepositoryTextFile → parse_workflow_definition(...) → WorkflowDefinition | WorkflowDefinitionProblem`.
- [ ] `StaticScalarValue.text` and `contains_expression`.
- [ ] sequence/mapping preservation for `runs-on`, `needs`, `strategy`, `container`, `with`.
- [ ] ordered `source_index` without runtime-order claim.
- [ ] `SourceSpan` and diagnostics.
- [ ] `StepsJobDefinition` versus `ReusableWorkflowJobDefinition`.
- [ ] workflow-level problems versus local `JobProblem` / `StepProblem`.
- [ ] local structural failure can preserve readable sibling structure.
- [ ] duplicate material key / job-ID behavior.
- [ ] expressions are preserved, not evaluated.
- [ ] Read focused tests as executable semantics.

### 1E. Cluster 3 — direct-install declaration observation

Current source:

```text
src/upgradepilot/dependency/direct_install.py
```

Entry point:

```text
observe_direct_installation_declaration(...)
```

Inputs:

```text
RunStepDefinition
+ optional workflow RunDefaults
+ optional job RunDefaults
+ independently established dependency_source_path
```

- [ ] Why this responsibility belongs to `upgradepilot.dependency`, not `upgradepilot.github`, `ci`, or `target`.
- [ ] Trace one `RunStepDefinition` into `DirectInstallDeclarationObservation`.
- [ ] Understand result states: `observed`, `not_observed`, `unresolved`.
- [ ] Explain why `not_observed` is not established absence.
- [ ] Explain why dynamic path/working-directory context becomes `unresolved`.
- [ ] Working-directory precedence:

```text
step > job defaults.run > workflow defaults.run > repository root
```

- [ ] `_effective_working_directory(...)` responsibility.
- [ ] `_normalize_literal_working_directory(...)` boundary.
- [ ] `_resolve_requirement_path(...)` and repository-relative path safety.
- [ ] admitted direct `pip` / `python -m pip` requirements-file forms.
- [ ] shell-segment splitting is bounded recognition, not shell interpretation.
- [ ] Explain proof boundary:

```text
observed declaration
!= executed
!= succeeded
!= environment formed
!= exact version installed
!= generic dependency consumption
!= package exercise
```

### 1F. Cluster-3 tests as executable contract

- [ ] root requirements install → observed.
- [ ] step/job/workflow working-directory precedence.
- [ ] safe parent requirement path resolution.
- [ ] dynamic working directory → unresolved.
- [ ] dynamic requirement path → unresolved.
- [ ] nonmatching requirements path → not_observed.
- [ ] quoted pip text inside `echo` is not misclassified.
- [ ] direct install inside one shell segment can be observed without claiming execution.
- [ ] invalid dependency source path rejected at boundary.

### 1G. Current frontier checkpoint

- [ ] Explain the complete validated foundation:

```text
exact repository workflow source
→ bounded YAML parser
→ typed GitHub Actions static IR
→ direct-install declaration observation
```

- [ ] Explain what is still intentionally old/unmigrated in Target and CI.
- [ ] Explain why Cluster 4 is a **consumer migration**, not another parser foundation.
- [ ] Predict what Target should be able to reuse from Clusters 2–3 and what Target-specific interpretation must remain Target-owned.
- [ ] Do not treat Cluster 4 as implemented until `main` actually resumes it.

---

## 2. Target Artifact Environment positive flow `POSTPONED / RETURN POINT`

This older lesson remains useful and open. We will revisit it primarily as the **before-state** for Cluster-4 Target migration rather than learning it in isolation first.

- [ ] Provenance requirements for `RepositoryTextFile`.
- [ ] runner declaration.
- [ ] setup-python declaration.
- [ ] dependency-source installation declaration.
- [ ] `not_observed` versus absence.
- [ ] exact wheel compatibility remains independently unresolved.

---

## 3. Artifact Serviceability / applicability mechanisms `POSTPONED`

- [ ] Artifact Serviceability Increment 1.
- [ ] Artifact Serviceability Increment 2 broader flow.
- [ ] exact wheel-compatibility bridge.
- [ ] generic applicability composition comparison.
- [ ] Python-support mechanism comparison.

Return when current frontier work requires these semantics or Ali explicitly redirects.

---

## 4. PR/evidence foundations `POSTPONED`

- [ ] PR identity.
- [ ] changed-file evidence.
- [ ] dependency version change.
- [ ] exact-head CI evidence acquisition.
- [ ] repository-file provenance.

Teach just-in-time if a current Phase-E path requires one of these contracts.

---

## 5. Future Phase-E implementation `WAIT FOR MAIN`

Current approved sequence after the pause:

```text
[ ] Cluster 4 — Target migration
[ ] Cluster 5 — CI migration / proof-claim narrowing
[ ] Cluster 6 — repository-path reconciliation
[ ] Cluster 7 — Tranche-1 acceptance
[ ] Tranche-1 stop/review
```

When `main` resumes materially:

```text
check MEMORY.md
→ inspect changed source/tests
→ synchronize learning branch
→ preserve current learning position
→ decide whether newest code becomes the new frontier
→ teach only newly blocking prerequisites
```

---

## Learning execution rules

- Check current `main` before meaningful frontier learning if parallel implementation may have advanced.
- Source/tests/runtime evidence beat old learning notes.
- `MEMORY.md` alone owns live project continuation.
- Do not check an item merely because it was explained once; require demonstrated understanding at the intended depth.
- Skipped work remains open.
- Preserve the exact return point when Ali jumps ahead.
- Prefer newest implemented responsibility plus only necessary backward context.
- Avoid broad theory unless it directly improves understanding, prediction, diagnosis, or ownership of current UpgradePilot code.
