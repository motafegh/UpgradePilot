# 2026-08-15 Phase-E Onboarding Realignment

**Learning branch:** `learning/real-case-code-flows-2026-08-12`  
**Synchronized product baseline:** `main@89d2b845647a7159cb276cbb38c0cdea0608d8af`  
**Learning-branch sync merge:** `6e53c7a6c50dfa42e7cb1a26bc083040bdf0f996`  
**Previous learning orientation:** [`2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md`](2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md)

## Why this checkpoint exists

The August 14 learning checkpoint was correct for its source state: Target Artifact Environment was then the highest-value new implemented slice to study. Before a substantive lesson began, `main` advanced through the B2 cross-responsibility architecture reconciliation and into Phase E.

The learning branch has now been synchronized again. `MEMORY.md` deliberately pauses Phase-E implementation after completed Cluster 1 for user onboarding and understanding before any Cluster-2 work begins.

This checkpoint realigns the learning workspace to that live product state without rewriting the August 14 historical record or falsely marking older learning items complete.

`MEMORY.md` remains the sole live-state authority.

## Preserved learning state

Before this realignment:

- the learning branch/workspace and broad learning plan were established;
- the August 14 Target Artifact Environment orientation was recorded;
- no substantive code-flow lesson had been completed;
- the older Target Artifact Environment, artifact-serviceability, applicability, Python-support, and PR/evidence items remained open;
- therefore there is no partially completed technical lesson whose completion state must be reconstructed.

The older items remain available and unchecked. They may be pulled in as prerequisites or resumed when they again have the highest learning value.

## Current product state that changes the learning priority

Current `MEMORY.md` selects an onboarding/review checkpoint after Phase-E Tranche-1 Cluster 1.

Current implementation state:

```text
✓ Cluster 0 — synchronized, validated green baseline
✓ Cluster 1 — PyYAML dependency/parser boundary

PAUSE — onboarding / current-state understanding

[ ] Cluster 2 — typed bounded GitHub Actions static workflow IR
[ ] Cluster 3 — shared direct-install declaration observation
[ ] Cluster 4 — Target migration
[ ] Cluster 5 — CI migration / proof-claim narrowing
[ ] Cluster 6 — repository-path reconciliation
[ ] Cluster 7 — Tranche-1 acceptance gate
```

No later cluster is selected merely because it is next in the approved plan.

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

The architecture reconciliation established that this is no longer merely local duplication. It creates provider-parsing drift and proof-strength risk when static declarations are described with runtime-sounding conclusions.

The accepted durable architecture is therefore:

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

The learning goal is not merely to memorize this diagram. We need to understand which sameness earned the shared provider layer, which semantics remain consumer-owned, and how the current code demonstrates the need.

## Cluster 1 — implemented truth

Cluster 1 does not implement the typed workflow-definition IR.

It implements only the parser/traversal foundation required beneath it:

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

Current source owner:

```text
src/upgradepilot/github/workflow_definition.py
```

Current focused proof owner:

```text
tests/test_github_workflow_definition.py
```

Approved runtime dependency surface now includes:

```text
requests>=2.32,<3
packaging>=26.2,<27
PyYAML>=6.0.3,<7
```

and `tests/test_runtime_dependency_contract.py` explicitly protects that surface.

## What Cluster 1 establishes

At its bounded scope, current source/tests establish that UpgradePilot can:

- compose YAML through a non-arbitrary-object construction node path;
- preserve scalar text under `BaseLoader` for later provider interpretation;
- observe mapping/sequence/scalar representation shapes;
- receive YAML-decoded literal/folded block-scalar content;
- retain source marks needed by later bounded extraction/diagnostics;
- keep duplicate mapping pairs visible before ordinary mapping collapse;
- convert malformed YAML into a controlled `WorkflowYamlParseError`;
- reject recursive alias graphs;
- enforce proportionate depth and node-visit traversal bounds.

## What Cluster 1 does not establish

Cluster 1 does **not** establish:

- a typed GitHub Actions workflow definition;
- job/step domain contracts;
- GitHub Actions expression evaluation;
- matrix expansion or execution semantics;
- reusable-workflow execution semantics;
- shell semantics;
- CI dependency exercise;
- Target environment formation;
- runtime execution/success;
- exact wheel compatibility;
- arbitrary multi-job environment continuity;
- generic hostile-YAML hardening.

PyYAML node objects remain private parser machinery and must not leak into CI, Target, or other product contracts.

## Why the older Target lesson remains useful

The existing Target Artifact Environment implementation is still real current code. Its local shallow reader is now especially useful as a **contrast specimen** for Phase E:

```text
old consumer-local parsing
→ what structure does Target actually need?
→ what proof does Target currently over-name?
→ what belongs in the future shared provider IR?
→ what must remain Target-specific?
```

Likewise, CI's current workflow-command and dependency-exercise code provides the second consumer needed to understand why the architecture was earned.

Therefore the older Target lesson is postponed, not discarded. Pieces may be learned just in time inside the Phase-E onboarding block and checked only to the extent actually demonstrated.

## Current learning sequence

Unless Ali redirects, the highest-value sequence is now:

```text
1. why Phase E exists
2. current Target and CI readers as concrete evidence
3. shared-provider versus domain-specific responsibility boundary
4. ADR-0008 accepted architecture
5. Cluster-1 parser source
6. Cluster-1 focused tests
7. dependency-contract regression incident
8. what Cluster 1 proves / does not prove
9. conceptual Cluster-2 responsibility without implementation
```

Prerequisites such as `RepositoryTextFile` provenance, static-versus-runtime evidence, GitHub Actions job/step structure, YAML representation nodes, or runtime Actions evidence should be taught only at the depth required by this sequence.

## Plan/rule impact

The broad `LEARNING_PLAN.md` remains valid and does not require a rule rewrite.

In particular, its existing rules already require:

- synchronization before affected substantial learning work;
- current source/tests and `MEMORY.md` over frozen learning order;
- state preservation before jumps;
- just-in-time prerequisite recovery;
- skipped/postponed work remaining unchecked;
- intended architecture not being confused with implemented truth;
- learning through real responsibilities rather than detached technology chapters.

The required change is therefore operational, not methodological:

- update the lab README/index to the current synchronized baseline and orientation;
- realign `LEARNING_TODO.md` so Phase-E onboarding is `▶ CURRENT`;
- keep the August 14 checkpoint historical;
- keep older technical items open;
- do not modify production source/tests merely for teaching.

## Resume point

Start with one small bounded block:

```text
WHY PHASE E EXISTS
```

Use the two current shallow readers as evidence, not as a giant code-reading exercise.

First target question:

> What provider-level GitHub Actions structure are CI and Target independently reconstructing today, and which conclusions do they attach to that structure that must remain consumer-specific?

Do not implement Cluster 2 during this learning block.
