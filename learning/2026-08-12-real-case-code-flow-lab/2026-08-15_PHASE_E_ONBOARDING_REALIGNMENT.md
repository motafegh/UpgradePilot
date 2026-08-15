# 2026-08-15 Phase-E Onboarding Realignment

**Learning branch:** `learning/real-case-code-flows-2026-08-12`  
**Latest synchronized product baseline:** `main@1e3027f87fa5b187c7d333472fe849aa6a49b049`  
**Latest learning-branch sync merge:** `f6b433aa00b4d91d0542632bd4af632fb8b0a786`  
**Previous learning orientation:** [`2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md`](2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md)

## Why this checkpoint exists

The August 14 checkpoint was correct for its source state: Target Artifact Environment was then the highest-value new implemented slice to study. Before a substantive lesson began, `main` advanced through B2 cross-responsibility architecture reconciliation and into Phase E.

During this learning-lab realignment, `main` continued moving in parallel. Rather than freeze a stale snapshot, the learning branch was repeatedly synchronized until it included the current Phase-E live state in which Cluster 2 is written and awaiting real WSL validation.

This checkpoint preserves history while establishing the current learning orientation.

`MEMORY.md` remains the sole owner of main's live project continuation. Current source/tests remain the implementation truth for what code exists.

## Current main/live state

Current synchronized `MEMORY.md` states:

```text
✓ Cluster 0 — synchronized green baseline
✓ Cluster 1 — PyYAML dependency/parser boundary
→ Cluster 2 — typed static GitHub Actions workflow IR: implementation written, validation pending
[ ] Cluster 3 — direct-install declaration observation
[ ] Cluster 4 — Target migration
[ ] Cluster 5 — CI migration / proof-claim narrowing
[ ] Cluster 6 — repository-path reconciliation
[ ] Cluster 7 — Tranche-1 acceptance gate
```

The earlier onboarding pause on `main` is ended. Main's implementation preference is now to preserve momentum through learning-by-doing, with a broad/deep walkthrough deferred by default until a meaningful implementation milestone.

That default does not cancel this separate learning lab. Ali explicitly requested in this conversation that the learning branch continue now. Under the project instruction hierarchy, that current request controls this learning workspace while leaving `main` execution untouched.

Therefore:

```text
main implementation continuation
!= learning-lab continuation
```

and:

```text
learning deeply here
!= stopping or changing main
```

## Preserved learning state

Before this realignment:

- the dedicated learning branch/workspace existed;
- the broad learning method and adaptive-order rule were established;
- the August 14 Target Artifact Environment orientation existed;
- no substantive code-flow lesson had been completed;
- older Target, artifact-serviceability, applicability, Python-support, and PR/evidence items remained open.

No older item is marked complete merely because newer Phase-E code now exists.

## Why Phase E exists

Two current consumers independently reconstruct overlapping GitHub Actions workflow-definition structure:

```text
Target artifact environment
→ src/upgradepilot/target/artifact_environment.py

CI dependency exercise
→ src/upgradepilot/ci/workflow_commands.py
→ src/upgradepilot/ci/dependency_exercise.py
```

They share provider/YAML structure but answer different domain questions.

The architecture reconciliation found that continued consumer-local parsing creates both structural duplication and proof-strength drift.

The accepted architecture is:

```text
RepositoryTextFile
        ↓
bounded provider-specific GitHub Actions static workflow-definition IR
owner = upgradepilot.github
        ↓
   ┌────┴────┐
   ▼         ▼
  CI       Target
```

Runtime GitHub Actions evidence remains separate:

```text
WorkflowRun
WorkflowJob
WorkflowStep
```

The central proof boundary is:

```text
static declaration
!= runtime execution
!= runtime success
!= environment formation
!= dependency exercise
```

The key abstraction principle is:

```text
share the lowest layer where meaning is genuinely identical
keep domain conclusions with the responsible consumer
```

## Cluster 1 — validated parser foundation

Cluster 1 is completed/green.

It established:

```text
untrusted GitHub Actions YAML text
→ yaml.compose(..., Loader=yaml.BaseLoader)
→ PyYAML representation nodes
→ controlled malformed-YAML failure
→ bounded recursive-alias / depth / node traversal validation
```

Important properties:

- no arbitrary application-object construction;
- textual scalar preservation under `BaseLoader`;
- mapping/sequence/scalar node access;
- literal/folded block scalar decoding;
- source marks;
- duplicate mapping-pair visibility before ordinary mapping collapse;
- controlled malformed-YAML failure;
- recursive-alias rejection;
- proportionate depth/node-visit limits.

PyYAML nodes remain private syntax machinery.

## Cluster 2 — written, validation pending

Current source/test commits include:

```text
db57de7...  Implement bounded GitHub Actions static workflow IR
9c2abce...  Add static workflow IR regressions
54ce690...  Protect static workflow definition owner
7d550d7...  Resume Phase E with deferred deep learning
1e3027f...  Record Cluster 2 implementation pending validation
```

Current provider source:

```text
src/upgradepilot/github/workflow_definition.py
```

now defines typed provider contracts including:

```text
SourceSpan

GitHubActionsStaticValue
├─ StaticScalarValue
├─ StaticSequenceValue
└─ StaticMappingValue / StaticMappingEntry

RunDefaults

StepEntry
├─ RunStepDefinition
├─ UsesStepDefinition
└─ StepProblem

JobEntry
├─ StepsJobDefinition
├─ ReusableWorkflowJobDefinition
└─ JobProblem

WorkflowDefinitionResult
├─ WorkflowDefinition
└─ WorkflowDefinitionProblem
```

Provider entrypoint:

```text
RepositoryTextFile
→ parse_workflow_definition(...)
→ WorkflowDefinition | WorkflowDefinitionProblem
```

### Current written semantics

The IR preserves, where safely readable:

- authoritative `RepositoryTextFile` source reference;
- 1-based `SourceSpan` locations;
- scalar text plus `contains_expression` rather than expression evaluation;
- bounded scalar/sequence/mapping structure;
- ordered jobs and steps through source occurrence indices;
- workflow/job run defaults;
- `needs`;
- scalar/sequence/mapping `runs-on` structure;
- `if` and `continue-on-error` scalars;
- strategy/matrix structure without expansion;
- container structure;
- reusable-workflow references and `with` inputs without recursive execution;
- run command/shell/working-directory declarations;
- `uses` reference and inputs;
- workflow-wide typed problems;
- local job/step problems that preserve readable sibling structure.

Current focused tests cover ordered multi-job preservation, dynamic values, run defaults, matrix/container structure, ordered run/uses steps, reusable workflows, duplicate job identity, local problem isolation, malformed YAML, path boundaries, and source-topology ownership.

### Validation status

Cluster 2 is **not yet completed/green** at this synchronized snapshot.

Current `MEMORY.md` explicitly requires real WSL validation before Cluster 3:

```text
pull current main
→ focused workflow-definition tests
→ source-topology test
→ nearest GitHub repository/actions regressions
→ complete deterministic product suite
→ final clean worktree
```

This learning branch does not perform or claim that main validation unless Ali separately requests it in the appropriate implementation context.

## What the provider IR still does not prove

The IR does not establish:

- expression evaluation;
- matrix execution/expansion;
- reusable-workflow execution;
- shell execution semantics;
- runtime scheduling;
- cross-job environment continuity;
- command execution/success;
- CI dependency exercise;
- Target environment formation;
- exact wheel compatibility;
- static↔runtime step correlation.

Critical distinction:

```text
provider structure readable
!= consumer proposition resolved
```

CI and Target have not been migrated yet.

## Why the older Target lesson remains useful

The current Target Artifact Environment implementation is still real consumer code. It is now especially useful as a contrast:

```text
current Target-local reader
→ what provider structure does it reconstruct?
→ what Target-specific meaning does it attach?
→ which structural parts now belong to the shared IR?
→ which Target conclusions must remain Target-owned?
```

CI provides the corresponding second consumer.

Therefore the old Target lesson is postponed, not discarded. Any prerequisite learned during the Phase-E lesson is checked only at the depth actually demonstrated.

## Current learning sequence

Unless Ali redirects:

```text
1. why Phase E exists
2. current Target and CI shallow readers
3. shared provider structure vs consumer semantics
4. ADR-0008
5. Cluster-1 PyYAML foundation
6. current typed provider IR contracts
7. parse_workflow_definition(...) flow
8. focused IR tests and scoped-problem behavior
9. what is written vs what awaits validation
10. relation to future Target/CI migration
```

Teach prerequisites just in time rather than forcing older TODO sections first.

## Plan/rule impact

The broad `LEARNING_PLAN.md` remains valid. No methodological rewrite is needed.

Its adaptive rules already cover:

- synchronization with relevant `main` changes;
- latest source/tests over frozen lesson order;
- explicit state preservation before jumps;
- just-in-time prerequisite recovery;
- skipped work remaining open;
- separation of architecture intent, implementation truth, and learner ownership;
- real-responsibility learning rather than detached technology chapters.

The required refinements were therefore limited to:

- synchronizing the branch;
- updating the learning index/baseline;
- realigning the operational TODO;
- recording this dated Phase-E checkpoint;
- preserving August 14 as history;
- distinguishing main's implementation cadence from this explicitly requested learning-lab cadence.

## Resume point

Start with one bounded block:

```text
WHY PHASE E EXISTS
```

First target question:

> What provider-level GitHub Actions structure are CI and Target independently reconstructing, which parts are now represented once by the shared IR, and which conclusions must remain consumer-specific?

Do not implement Cluster 3 or modify main from this learning block.
