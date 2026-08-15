# Cluster 3 Validated Learning Frontier

**Date:** 2026-08-15  
**Learning branch:** `learning/real-case-code-flows-2026-08-12`  
**Synchronized main baseline:** `72eb291e6ffc9112956e37f34dc5c7f7e3c40154`  
**Main live state:** validated Phase-E Clusters 0–3; pause before Cluster 4

## Purpose

Record the current learning frontier after synchronizing the dedicated learning branch with the newest validated Phase-E implementation state.

This checkpoint supersedes the earlier operational orientation that still described Cluster 2 as pending validation. It does not rewrite or invalidate the earlier dated checkpoints; those remain historical records of what was true at their respective baselines.

## Current product truth

Current `MEMORY.md` establishes:

```text
✓ Cluster 0 — synchronized green baseline
✓ Cluster 1 — PyYAML dependency/parser boundary
✓ Cluster 2 — typed static GitHub Actions workflow IR
✓ Cluster 3 — shared direct-install declaration observation

PAUSE — discussion / decision checkpoint

[ ] Cluster 4 — Target migration
```

Cluster 4 has not begun and is not currently selected for execution.

Validated implementation foundation:

```text
exact repository workflow source
→ PyYAML bounded parser boundary
→ typed GitHub Actions static workflow IR
→ dependency-owned direct-install declaration observation
```

## What changed since the previous learning orientation

The previous checkpoint treated Cluster 2 as written but awaiting WSL validation.

Since then:

1. Cluster 2 passed the real validation gate and is green.
2. Cluster 3 was implemented under `src/upgradepilot/dependency/direct_install.py`.
3. Cluster 3 passed focused/nearest tests and the full deterministic suite.
4. Main explicitly paused before Cluster 4 for discussion/decision.

Therefore the newest useful learning frontier is no longer merely "how the static IR is formed." It now includes the first shared semantic consumer built on that IR.

## Cluster 2 — current role

Provider owner:

```text
upgradepilot.github
```

Core path:

```text
RepositoryTextFile
→ parse_workflow_definition(...)
→ WorkflowDefinition | WorkflowDefinitionProblem
```

The typed provider representation preserves bounded visible GitHub Actions structure without leaking PyYAML nodes or making CI/Target conclusions.

Important objects include:

```text
StaticScalarValue
StaticSequenceValue
StaticMappingValue
RunDefaults
RunStepDefinition
UsesStepDefinition
StepsJobDefinition
ReusableWorkflowJobDefinition
WorkflowDefinition
scoped JobProblem / StepProblem / WorkflowDefinitionProblem
```

Static structure remains distinct from runtime GitHub Actions evidence.

## Cluster 3 — current role

Domain owner:

```text
upgradepilot.dependency
```

Entry point:

```text
observe_direct_installation_declaration(...)
```

Conceptual input:

```text
provider-owned static RunStepDefinition
+ effective workflow/job/step working-directory context
+ independently established repository-relative dependency source path
```

Conceptual result:

```text
DirectInstallDeclarationObservation
    state = observed | not_observed | unresolved
```

This is a deliberate architecture seam:

```text
GitHub provider layer
owns what the workflow statically declares

Dependency layer
owns whether that static command/path relation declares direct installation

CI / Target
later consume that meaning for their own propositions
```

## Working-directory semantics

Cluster 3 resolves declaration context using:

```text
step working-directory
        ↓ fallback
job defaults.run working-directory
        ↓ fallback
workflow defaults.run working-directory
        ↓ fallback
repository root
```

Dynamic or structurally unsafe path context is not guessed. It becomes `unresolved`.

The implementation deliberately supports repository-relative path resolution, including safe parent traversal from a nested working directory where the resolved path remains inside the repository.

## Proof boundary

The most important semantic guard remains:

```text
direct install declaration observed
!= command executed
!= command succeeded
!= environment formed
!= exact proposed dependency version installed
!= generic dependency consumption
!= package exercise
```

This distinction explains why Cluster 3 is shared dependency interpretation rather than CI proof or Target environment proof.

## Why this is the right learning frontier

Learning should now stay close to the implementation front:

```text
Cluster 3 direct-install observation
        ↑
Cluster 2 typed static IR
        ↑
Cluster 1 parser boundary
        ↑ only as needed
old CI / Target shallow readers
```

We do not need a broad GitHub Actions, YAML, parser, compiler, shell, or evidence-theory course before reading this code.

Backward study is justified only when it answers a concrete current question such as:

- why Cluster 3 consumes `RunStepDefinition` instead of raw YAML;
- why working-directory context belongs in the observation;
- why the observation belongs under `dependency/`;
- why dynamic path values become unresolved;
- why static declaration must not become runtime proof;
- why Target and CI can share this observation while keeping different final meanings.

## Recommended immediate learning sequence

```text
1. Cluster 3 responsibility in plain language
2. one concrete input/output example
3. read the public dataclasses + entry point
4. trace working-directory precedence
5. trace requirement-path resolution
6. inspect observed / not_observed / unresolved branches
7. read the focused tests as the contract
8. step back into Cluster 2 only where a Cluster-3 input type needs explanation
9. compare with the old Target/CI duplicate logic
10. predict what Cluster 4 should reuse vs keep Target-specific
```

This order keeps the learning near recent code while still building the required mental model underneath it.

## Preserved return points

Older learning work remains open rather than implicitly completed:

- Target Artifact Environment first-slice flow;
- Artifact Serviceability mechanism details;
- Python-support mechanism and applicability comparison;
- PR/evidence acquisition foundations.

These should be revisited when the current implementation naturally needs them or when Ali explicitly redirects.

## Synchronization rule from here

Before a meaningful learning block, if `main` may have advanced:

```text
check main + MEMORY.md
→ inspect new source/tests
→ sync branch if needed
→ preserve current learning state
→ decide whether the new implementation becomes the frontier
```

The learning lab should stay close to the product without chasing every commit so aggressively that understanding becomes fragmented.
