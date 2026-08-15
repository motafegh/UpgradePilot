# 2026-08-15 Phase-E Onboarding Realignment

**Learning branch:** `learning/real-case-code-flows-2026-08-12`  
**Latest synchronized product baseline:** `main@54ce69082b0d74ec0412b05264dfae897f970d47`  
**Latest learning-branch sync merge:** `4bedb554174a8300f6b39233b2446c9049fb87e5`  
**Previous learning orientation:** [`2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md`](2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md)

## Why this checkpoint exists

The August 14 learning checkpoint was correct for its source state: Target Artifact Environment was then the highest-value new implemented slice to study. Before a substantive lesson began, `main` advanced through the B2 cross-responsibility architecture reconciliation and into Phase E.

The learning branch was first synchronized to the validated Cluster-1 onboarding pause. While the learning-lab realignment was being written, `main` advanced again with the first Cluster-2 source/test commits. The learning branch was synchronized again rather than freezing a stale orientation.

This checkpoint therefore records the newest synchronized source state while preserving a critical distinction:

```text
new Cluster-2 source/tests exist
!= Cluster 2 has necessarily been recorded as completed/green
```

At this exact snapshot, `MEMORY.md` still carries the earlier deliberate pause after validated Cluster 1. No later live-state/validation record had yet promoted Cluster 2 to completed/green. Source/tests are implementation truth for what code exists; `MEMORY.md` remains the live continuation owner.

## Preserved learning state

Before this realignment:

- the learning branch/workspace and broad learning plan were established;
- the August 14 Target Artifact Environment orientation was recorded;
- no substantive code-flow lesson had been completed;
- the older Target Artifact Environment, artifact-serviceability, applicability, Python-support, and PR/evidence items remained open;
- therefore there is no partially completed technical lesson whose completion state must be reconstructed.

The older items remain available and unchecked. They may be pulled in as prerequisites or resumed when they again have the highest learning value.

## Architecture state that changes the learning priority

Phase A-D accepted ADR-0008 after comparing the existing CI and Target workflow readers.

The durable direction is:

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

The central proof boundary remains:

```text
static declaration
!= runtime execution
!= runtime success
!= environment formation
!= dependency exercise
```

The architecture is earned by demonstrated overlap in provider structure, not by assuming CI and Target have the same domain semantics.

## Why Phase E exists

Two existing product responsibilities independently read overlapping GitHub Actions workflow-definition structure:

```text
Target artifact environment
→ src/upgradepilot/target/artifact_environment.py

CI dependency exercise
→ src/upgradepilot/ci/workflow_commands.py
→ src/upgradepilot/ci/dependency_exercise.py
```

Both first slices use shallow custom reading of jobs/run commands and related workflow structure, but they answer different domain questions.

The reconciliation established two problems:

1. provider/YAML structure was being reconstructed independently in multiple consumers;
2. static declarations were beginning to receive runtime-sounding domain claims.

The accepted correction is to share the bounded GitHub Actions structure while keeping CI/Target conclusions separate.

## Cluster 1 — validated parser foundation

Cluster 1 established the parser/traversal boundary beneath the provider IR:

```text
untrusted GitHub Actions workflow YAML text
        ↓
yaml.compose(..., Loader=yaml.BaseLoader)
        ↓
PyYAML representation nodes
        ↓
controlled malformed-YAML failure
        ↓
bounded recursive-alias / nesting-depth / node-visit validation
```

It established:

- a non-arbitrary-object construction parse path;
- textual scalar preservation under `BaseLoader`;
- mapping/sequence/scalar node access;
- YAML-decoded literal/folded block scalars;
- source marks;
- duplicate-pair visibility before mapping collapse;
- controlled malformed-YAML failure;
- recursive-alias rejection;
- proportionate depth/node-visit limits.

PyYAML node objects remain private syntax machinery.

## Newly landed Cluster-2 source/test implementation

After the initial onboarding pause, the following source commits landed on `main` and were synchronized into the learning branch:

```text
db57de7...  Implement bounded GitHub Actions static workflow IR
9c2abce...  Add static workflow IR regressions
54ce690...  Protect static workflow definition owner
```

Current provider source:

```text
src/upgradepilot/github/workflow_definition.py
```

now contains typed provider objects including:

```text
SourceSpan
StaticScalarValue
StaticSequenceValue
StaticMappingEntry / StaticMappingValue
RunDefaults
RunStepDefinition
UsesStepDefinition
StepProblem
StepsJobDefinition
ReusableWorkflowJobDefinition
JobProblem
WorkflowDefinition
WorkflowDefinitionProblem
WorkflowDefinitionResult
```

Main entrypoint:

```text
RepositoryTextFile
→ parse_workflow_definition(...)
→ WorkflowDefinition | WorkflowDefinitionProblem
```

### Important implemented semantics visible in source/tests

The current source/tests preserve:

- exact `RepositoryTextFile` source ownership inside `WorkflowDefinition`;
- source spans for provider-level structures;
- textual scalar values plus `contains_expression` rather than evaluating GitHub expressions;
- bounded scalar/sequence/mapping structure where needed;
- ordered jobs and steps through `source_index`;
- workflow and job `defaults.run` information;
- `needs`, `runs-on`, `if`, `continue-on-error`, `strategy`, and `container` structure;
- run steps separately from `uses` steps;
- reusable-workflow jobs without recursively executing/expanding them;
- workflow-level problems for source-wide invalidity/ambiguity;
- local `JobProblem` / `StepProblem` so one unreadable local structure does not automatically erase readable siblings;
- duplicate job identity and duplicate material-key protection;
- malformed YAML and unsupported workflow path as typed workflow-definition problems.

Focused regressions now exercise multi-job preservation, dynamic values, matrices as structure without expansion, reusable-workflow jobs, local problem preservation, duplicate identities, malformed YAML, and path boundaries.

## What the new IR still does not prove

The typed provider IR does **not** establish:

- GitHub Actions expression evaluation;
- matrix execution/expansion;
- reusable-workflow execution;
- shell execution semantics;
- runtime scheduling or cross-job environment continuity;
- command execution/success;
- CI dependency exercise;
- Target dependency-environment formation;
- exact wheel compatibility;
- static↔runtime step correlation.

Most importantly:

```text
provider structure readable
!= consumer proposition resolved
```

CI and Target still own their domain interpretations and, at this snapshot, their migrations are not implied merely by the IR source existing.

## Live-state caution at this snapshot

The latest source/test commits arrived faster than the live documentation/state record.

Therefore this learning checkpoint intentionally records both facts:

```text
SOURCE/TEST FACT
Cluster-2 typed IR implementation is present at main@54ce690...
```

```text
LIVE COMPLETION FACT
MEMORY.md had not yet recorded Cluster 2 as completed/green at the time of this checkpoint.
```

Do not collapse those into either of these false claims:

```text
"Cluster 2 does not exist"
```

or:

```text
"Cluster 2 is fully validated/accepted"
```

until the appropriate project evidence/live owner establishes the latter.

## Why the older Target lesson remains useful

The existing Target Artifact Environment implementation remains real current consumer code and is now especially useful as a contrast specimen:

```text
current Target-local parser
→ identify provider structure it reconstructs
→ identify Target-specific conclusions
→ compare with shared provider IR
→ later observe what migration removes and what remains Target-owned
```

CI provides the second consumer needed to understand why the architecture was earned.

Therefore the older Target lesson is postponed, not discarded. Pieces may be learned just in time inside the Phase-E onboarding block and checked only to the extent actually demonstrated.

## Current learning sequence

Unless Ali redirects, the highest-value sequence is now:

```text
1. why Phase E exists
2. current Target and CI readers as concrete evidence
3. shared-provider versus domain-specific responsibility boundary
4. ADR-0008 accepted architecture
5. Cluster-1 PyYAML parser foundation
6. current typed static workflow IR contracts
7. current IR parsing/result flow
8. focused IR tests and local-problem behavior
9. what the current source/tests prove / do not prove
10. reconnect to remaining consumer migrations only after the current block is understood
```

Prerequisites such as `RepositoryTextFile` provenance, GitHub Actions job/step structure, YAML nodes, static-vs-runtime evidence, or runtime Actions evidence should be taught only at the depth required by this sequence.

## Plan/rule impact

The broad `LEARNING_PLAN.md` remains valid and does not require a methodological rewrite.

Its existing rules already require:

- synchronization before affected substantial learning work;
- current source/tests and `MEMORY.md` over frozen learning order;
- state preservation before jumps;
- just-in-time prerequisite recovery;
- skipped/postponed work remaining unchecked;
- implemented behavior not being inferred from plans/ADRs alone;
- learning through real responsibilities rather than detached technology chapters.

The required refinement is operational:

- update README/TODO to the newest synchronized baseline;
- make Phase-E architecture + parser + typed-IR onboarding `▶ CURRENT`;
- preserve the August 14 historical checkpoint;
- keep older technical items open;
- distinguish source/test presence from validated/live completion;
- do not modify production source/tests merely for teaching.

## Resume point

Start with one small bounded block:

```text
WHY PHASE E EXISTS
```

Use the two current shallow readers as evidence, then connect that duplication to the shared provider IR now present in `workflow_definition.py`.

First target question:

> What provider-level GitHub Actions structure are CI and Target independently reconstructing, which parts are now represented once by the shared IR, and which conclusions must remain consumer-specific?

Do not begin or modify later Phase-E consumer migrations from the learning branch.
