# B2 Cross-Responsibility Architecture Implementation Plan

**Status:** Approved bounded Phase-E implementation/refactor plan  
**Date:** 2026-08-15  
**Owner:** Ali Rajabi  
**Parent checkpoint:** [`B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md)  
**Parent responsibility:** [`B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md)  
**Accepted architecture:** [`../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md)  
**Source ownership baseline:** [`../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md)  
**Canonical product-decision semantics:** [`../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)  
**Security boundary:** [`../SECURITY.md`](../SECURITY.md)

## 1. Purpose

Implement the smallest coherent source/test migration required by the accepted cross-responsibility architecture after Phase A–D reconciliation.

The implementation must replace duplicated GitHub Actions source parsing with one bounded provider-specific static workflow-definition representation, migrate CI and Target to that representation without merging their domain semantics, correct proof-strength naming/claims exposed by the reconciliation, and remove the demonstrated repository-path ownership drift.

The work is deliberately split into two tranches:

```text
TRANCHE 1
static workflow IR + consumer migration + semantic corrections

TRANCHE 2
optional bounded static↔runtime correlation + stronger CI proof
```

Do not stack Tranche 2 onto an unvalidated Tranche 1.

## 2. Accepted architecture carried into implementation

```text
RepositoryTextFile
        ↓
GitHub Actions static workflow-definition IR
owner: upgradepilot.github
        ↓
   ┌────┴────┐
   ▼         ▼
  CI       Target
```

Runtime Actions evidence remains separate:

```text
WorkflowRun
WorkflowJob
WorkflowStep
```

A later optional explicit correlation responsibility may join static and runtime evidence when a proposition requires stronger proof.

Important guards:

```text
static declaration != execution != success
consumer unresolved != parser failure
multiple jobs visible != cross-job environment continuity
workflow evidence != complete Target context
direct-install declaration != generic dependency consumption
```

## 3. Non-goals

This plan does **not** authorize:

- a generic YAML AST/domain model;
- a universal CI-provider abstraction;
- full GitHub Actions expression evaluation;
- arbitrary matrix execution/expansion;
- reusable-workflow recursive execution semantics;
- container environment reconstruction;
- a shell interpreter;
- generic script/task-runner tracing;
- arbitrary cross-job environment composition;
- universal dependency-consumption tracing;
- exact wheel-tag derivation from broad workflow labels;
- a universal Target environment model;
- final action/recommendation synthesis;
- a universal impact/planner/orchestration framework;
- automatic upstream mutation;
- source changes unrelated to the demonstrated reconciliation inventory.

## 4. Tranche 1 — static provider architecture and semantic migration

### Cluster 0 — synchronize and validate the baseline

Before source edits:

1. synchronize the implementation branch with current `main`;
2. verify a clean worktree;
3. record the exact baseline revision;
4. run the focused CI, Target artifact-environment, GitHub repository/actions, and repository-path regressions currently relevant to the migration;
5. run the complete active product deterministic suite;
6. classify any baseline failure before changing source.

The current accepted architecture/docs do not themselves prove runtime behavior.

### Cluster 1 — add PyYAML and prove the parser dependency boundary

Add PyYAML as the selected runtime dependency with a bounded version range justified by current Python support and implementation tests.

Use a non-arbitrary-object-construction representation/node parsing path suitable for untrusted public workflow text.

Prove at minimum:

- import/install works in the active supported Python environment;
- normal mapping/sequence/scalar node handling;
- block-scalar handling needed by `run`;
- source marks/locators are available where used;
- duplicate material keys can be detected before silent semantic collapse;
- aliases/recursive structures fail safely under the bounded converter;
- malformed YAML becomes typed/controlled failure rather than an uncaught parser leak.

Keep parser safety proportionate. Do not build a generalized hostile-YAML framework or arbitrary parser-budget subsystem.

### Cluster 2 — implement the bounded GitHub Actions static workflow IR

Create the provider-owned static workflow-definition module under `src/upgradepilot/github/` only when the implementation enters it.

Exact class/module names may be refined during implementation, but the responsibility must preserve the accepted contract.

Minimum structural responsibilities:

```text
WorkflowDefinitionResult
├─ WorkflowDefinition
│  ├─ exact RepositoryTextFile source/provenance reference
│  ├─ workflow run defaults where admitted
│  └─ ordered job entries
│     ├─ normal steps job
│     ├─ reusable-workflow job
│     └─ scoped job problem
└─ workflow-level problem

normal steps job
├─ source occurrence/index + diagnostic span where useful
├─ key/name
├─ needs
├─ runs-on structured value
├─ if
├─ continue-on-error
├─ run defaults
├─ matrix/strategy bounded fragment
├─ container bounded fragment
└─ ordered step entries

step entry
├─ run step
├─ uses step
└─ scoped step problem
```

For selected structured fields, preserve bounded scalar/sequence/mapping structure as required by real GitHub Actions syntax.

Required semantic behavior:

```text
absent != literal != dynamic
valid dynamic expression != parser failure
multiple jobs preserved structurally
source order preserved without runtime scheduling claim
needs preserved without environment-continuity claim
raw RepositoryTextFile remains authoritative
```

Do not expose PyYAML node objects as the UpgradePilot contract.

### Cluster 3 — implement the shared direct-installation declaration observation

Add the bounded dependency-owned primitive only after the static IR exposes stable run/context inputs.

Conceptual input:

```text
static run command
+ effective working-directory context
+ independently established dependency-source path
```

Conceptual result:

```text
direct installation declaration observed
or
not observed / unresolved under bounded interpretation
```

The primitive must account for workflow/job/step `working-directory` precedence before comparing a requirements path.

It may recognize the currently admitted direct `pip` / `python -m pip` requirements-file forms, but it must not claim:

```text
execution
success
exact proposed version installed
general dependency consumption
package exercise
```

Keep package invocation/exercise recognition under `ci/`.

### Cluster 4 — migrate Target artifact-environment interpretation

Migrate `target/artifact_environment.py` from its local indentation parser to the shared static workflow IR and shared direct-install declaration observation.

Correct the current proof-strength contract:

```text
dependency_environment_formation
```

must no longer describe a state established solely from static YAML.

Replace it with static declaration/configuration semantics, with exact type/field names selected for clarity during implementation.

Preserve:

- exact repository/revision/workflow/blob/job provenance;
- literal runner facts only where actually literal/established;
- setup-python declaration interpretation only within Target;
- `not_observed` as non-absence;
- exact wheel compatibility unresolved unless independently established;
- workflow evidence as one Target evidence source, not the Target model.

Multiple/matrix/reusable/container structures that the IR can read must not automatically become parser failure. Target may remain unresolved/limited where its current proposition cannot safely interpret them.

### Cluster 5 — migrate CI static reading and narrow claim strength

Migrate `ci/workflow_commands.py` / `ci/dependency_exercise.py` to the shared static workflow IR and shared direct-install declaration observation where their semantics are identical.

Keep CI-specific:

- successful exact-head run/job authority;
- direct package invocation/exercise recognition;
- CI-specific combination of available evidence;
- CI unresolved/no-successful-CI states.

Narrow/refine the current `proven` meaning so successful run/job evidence plus static install/invocation structure is not represented as matched-command runtime execution/success proof.

Exact state/enum naming is implementation work, but tests and user-facing detail must make the proof class explicit.

Do not implement static↔runtime step correlation in this cluster.

### Cluster 6 — reconcile repository-path ownership drift

Remove the duplicate private repository-relative path validation in `github/repository.py` where its semantics are already owned by `src/upgradepilot/repository_path.py`.

Provider-specific constraints such as `.github/workflows/` stay with the GitHub caller. Source-neutral relative POSIX path structure uses the existing neutral owner.

This is reconciliation under ADR-0007, not a new architecture decision.

### Cluster 7 — Tranche-1 regression and acceptance gate

Required focused coverage should include at least:

- static workflow parser normal single-job case;
- ordered multi-job preservation;
- `needs` preservation;
- literal and dynamic `runs-on` forms;
- matrix presence without expansion;
- reusable-workflow job recognition;
- ordered run/uses steps;
- `if` and `continue-on-error` preservation;
- workflow/job/step run-default / working-directory precedence inputs;
- block `run: |` / folded `run: >` behavior relevant to command text;
- duplicate material key/identity handling;
- malformed YAML problem behavior;
- bounded alias/recursive input handling;
- Target static declaration semantics and regression of existing provenanced facts;
- CI narrowed proof semantics and existing direct-exercise regressions;
- direct-install declaration observation with working-directory context;
- S004-style multi-job/matrix structural transfer;
- S011-style “workflow context exists but affected optional environment not formed/exercised” guard;
- repository-path shared-owner regression.

Validation gate:

```text
focused changed-responsibility tests
+ nearest GitHub/CI/Target/dependency regressions
+ installed/import smoke when dependency/package surface changes
+ complete active product deterministic suite
```

Record exact commands/results in dated implementation working-memory. Do not infer passing runtime behavior from ADR acceptance.

### Tranche-1 stop line

STOP after Tranche 1 if:

- the shared static IR is implemented and migrated;
- Target static proof semantics are corrected;
- CI current proof wording/state is narrowed appropriately;
- direct-install declaration observation is shared at the dependency boundary;
- repository-path drift is reconciled;
- focused/nearest/full validation is green or any remaining failure is explicitly classified.

Do not continue automatically into Tranche 2 in the same unreviewed change.

## 5. Tranche 2 — optional static↔runtime correlation and stronger CI proof

Begin only after Tranche 1 is accepted/validated and the stronger CI proposition is still worth pursuing.

### Responsibility

Design the smallest trustworthy correlation between safely identifiable static workflow job/step structure and existing runtime `WorkflowRun` / `WorkflowJob` / `WorkflowStep` evidence.

Potential stronger evidence ladder:

```text
static install step identified
+
corresponding runtime step identified
+
runtime step executed/succeeded
+
static exercise step identified
+
corresponding runtime step identified
+
runtime step executed/succeeded
```

This still does not automatically establish the exact proposed dependency version unless a separate witness/evidence chain supports that proposition.

### Required pressure before accepting an algorithm

The correlation method must account for at least:

- generated setup/cleanup runtime steps;
- duplicate or absent step names;
- step-number/source-index mismatch risk;
- reusable actions;
- skipped steps / `if`;
- `continue-on-error`;
- ordering;
- matrix one-static-job-to-many-runtime-job relationships;
- run attempts/retries where relevant.

Naive name-only or ordinal-only matching is not automatically admissible.

If a trustworthy bounded correlation cannot be established proportionately, leave the stronger proposition unresolved rather than expanding into logs/full workflow execution semantics.

### Tranche-2 stop line

Stop when the admitted stronger CI proposition has one tested bounded correlation method or when evidence shows that a proportionate method is not currently available.

Do not add logs, arbitrary shell tracing, or exact-version discovery merely to avoid an explicit unresolved state unless a separately selected proposition requires it.

## 6. Heterogeneous mechanism orchestration — separate later responsibility

Phase D accepts that application orchestration must eventually carry multiple typed mechanism results without growing one field family per mechanism indefinitely.

Do **not** design or implement a universal mechanism envelope in Tranche 1 or Tranche 2.

When artifact serviceability is actually integrated into `investigation.py`, design only the smallest typed collection/envelope required by the real second mechanism while preserving mechanism-specific result types and lineage.

That work may receive its own bounded plan/ADR only if the concrete implementation boundary becomes consequential enough to warrant one.

## 7. Documentation and promotion obligations

During implementation:

- `ADR-0008` remains the durable architecture owner;
- this plan owns implementation order, proof obligations, and stop lines;
- `SECURITY.md` owns the general proportional untrusted-YAML safety rule;
- the Product Decision Model specification remains the owner of framework-independent proof-strength semantics;
- dated implementation/debugging/validation evidence belongs in `working-memory/`;
- `MEMORY.md` alone owns live continuation and latest verification;
- do not rewrite historical simulation/audit records to mirror new source names.

If implementation materially contradicts ADR-0008 rather than merely refining class names/limits, stop and classify whether the ADR must be amended or superseded before continuing.

## 8. Completion condition

This Phase-E plan is complete only when the selected tranche has reached its stop line with source/tests/documentation synchronized.

Tranche 1 completion is required before the parent architecture checkpoint can be treated as implemented. Tranche 2 is a separately reviewed strengthening and is not required merely to prove that the shared static architecture exists.
