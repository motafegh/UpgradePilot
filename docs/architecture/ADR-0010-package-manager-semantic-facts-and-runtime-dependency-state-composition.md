# ADR-0010 — Package-Manager Semantic Facts and Runtime Dependency-State Composition

**Status:** Accepted  
**Date:** 2026-09-27  
**Owner:** Ali Rajabi  
**Scope:** reusable CI execution evidence, dependency-owned effective package-manager semantics, and command-derived runtime dependency-state composition

## Context

UpgradePilot already establishes exact dependency changes, exact static dependency-consuming command occurrences, and bounded static/runtime correlation. Those facts deliberately stop before the stronger proposition that the exact proposed dependency requirement is satisfied in the exact relevant Python package environment at a justified command-completion boundary.

The closed R2/R3 design showed that this stronger proposition requires independently owned evidence for source applicability, effective package-manager semantics, manager environment, final destination, and exact command execution. It also showed that step success is not command success, provider/workflow code should not become pip/uv-aware, package-manager semantics should not implement GitHub PATH propagation, and existing CI coverage must not silently change meaning.

## Decision

### 1. Separate successful user-step execution from exact command execution

CI runtime evidence uses two proof levels:

1. static/runtime step correlation plus unmasked completed-successful runtime status produces a reusable user-step execution assessment for both run and uses steps;
2. exact parsed command identity plus admitted shell/execution-profile structure and bounded reachability produces exact command-occurrence execution evidence.

A successful step never means that every internal command executed. Existing correlation and runtime-strengthening machinery should be refactored/reused rather than replaced by a package-manager-specific execution path.

### 2. Keep effective package-manager interpretation dependency-owned

Provider/workflow/shell owners may establish manager-agnostic facts such as environment declarations, bounded propagation, exact-process environment values, executable/interpreter selection, and command structure.

Dependency/package-manager semantics own pip/uv precedence and meaning. Provider code must not interpret PIP_* or UV_* variables as package-manager semantics.

### 3. Use independent semantic facts with shared bounded provenance

The first command-derived proof uses independent semantic propositions conceptually equivalent to:

- ManagerEnvironmentSelectionFact
- InstallationDestinationFact
- PackageMutationModeFact
- DirectRequirementHandlingFact

These share one demand-driven provenance method rather than one giant effective-config object or one resolver framework per flag.

For a required semantic dimension, precedence is:

command line > exact process environment > applicable persistent configuration > manager default.

Only sources required to settle that dimension are inspected. A lower-priority source may win only after higher relevant sources are positively non-overriding, disabled, or otherwise resolved. An unresolved higher source keeps the dimension unresolved. A manager default is never inferred merely because a CLI flag is absent.

Provider relationships such as setup-python PATH selection, venv activation, and bare-executable ownership remain environment-identity evidence; they do not replace package-manager CLI/config precedence.

### 4. Parse one package-manager operation once

Parser-neutral command evidence is interpreted into one dependency-owned static package-manager operation declaration. Semantic resolvers consume that declaration rather than independently reparsing raw shell text or command atoms.

Parser-library nodes remain behind the command-analysis boundary established by ADR-0009.

### 5. Keep runtime dependency-state proof separate from CI coverage/exercise evidence

Existing DependencyCICoverageResult and workflow coverage evidence retain their current meaning: static changed-dependency consumption/direct exercise plus bounded runtime strengthening. They do not become package-state evidence.

A separate composition responsibility combines exact dependency/source applicability, supported static consumption, effective package-manager semantic facts, and exact command execution into a per-command RequirementSatisfiedAtCommandCompletion witness.

That witness preserves exact package/version identity, exact source/workflow/job/step/command provenance, manager environment/destination scope, semantic provenance, the command-completion observation boundary, and explicit limitations.

It establishes only that the exact proposed direct requirement is satisfied in the resolved package-state scope when that exact successful command completes. It does not establish fresh-install causality, artifact identity, later persistence/use, behavioral compatibility, or maintainer-action permission.

### 6. Preserve explicit proof problems

When a required edge cannot close, the state-proof layer returns an explicit not-established or unresolved problem with the blocking dimension/provenance when available.

Effective dry-run, unsupported first-family destination, unresolved process environment/configuration, masked/non-successful execution, or unresolved exact-command reachability do not become package-absence conclusions.

### 7. Keep direct target-owned package-state observation optional

A later direct state witness, such as a self-verifying importlib.metadata.version check, may independently establish package/version state at its own observation boundary.

Command-derived and directly observed witnesses must preserve recoverable package identity, version, state/inspection scope, runtime provenance, observation boundary/method, and limitations. They are not forced into one common destination type or base hierarchy merely for symmetry.

The first command-derived implementation does not require generic job-log, stdout, or artifact acquisition.

## Rejected alternatives

- **One giant package-manager configuration object:** rejected because it encourages universal reconstruction and mixes independent proof dimensions.
- **One precedence subsystem per option:** rejected because the settings share the same demand-driven provenance responsibility.
- **Package-manager-specific runtime execution:** rejected because execution evidence also serves setup actions, environment writes, venv sequences, and future observations.
- **Upgrade existing CI coverage to package-state meaning:** rejected because it would break the accepted proof boundary and downstream interpretation.
- **Mandatory direct observation/log parsing:** rejected because the first Route-A family can establish its bounded command-completion proposition without it.

## Consequences

Positive:
- reusable execution evidence across actions and commands;
- package-manager meaning stays with the dependency domain;
- independent semantic dimensions remain explainable;
- defaults cannot pass through unresolved higher-precedence evidence;
- existing CI coverage keeps its meaning;
- command-derived package state gains a precise time/environment boundary;
- future Route B evidence can coexist without becoming mandatory.

Costs:
- bounded provider/workflow environment evidence must grow;
- private runtime-strengthening logic needs coordinated refactoring;
- a focused package-manager runtime-semantics owner is needed;
- application orchestration will eventually carry an additional typed dependency-state result;
- some ordinary-looking workflows will remain truthfully unresolved until material environment/configuration provenance is available.

## Intentionally undecided

This ADR does not select final class/function/module names, every pip/uv option, universal environment/config reconstruction, arbitrary shell simulation, matrix/reusable-workflow expansion, generic log/stdout/artifact acquisition, final Route-B implementation, later-version continuity, behavioral compatibility, maintainer-action enablement, or the detailed implementation/test sequence.

## Reassessment triggers

Reassess if evidence shows that the two execution levels cannot be shared without duplication, independent semantic facts repeatedly require one inseparable operation representation, bounded provenance is less trustworthy or proportionate than a simpler model, the command-derived family cannot produce useful real-case evidence without universal reconstruction, or direct target-owned state becomes sufficiently available and decision-critical to justify a different primary route.

## Evidence and related owners

- ADR-0008 — bounded static GitHub Actions workflow definition.
- ADR-0009 — parser-backed static workflow command analysis.
- working-memory/2026-09-24_effective-package-manager-semantics-system-design.md — closed semantic boundary.
- working-memory/2026-09-27_effective-package-manager-evidence-source-type-data-flow-design.md — closed evidence/type/data-flow design.
- plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md — bounded implementation/proof coordination.
- docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md — trust/evidence/ownership invariants.
- docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md — technical evidence/decision semantics.

This ADR selects architecture only. Implementation truth remains with source/tests/reproducible validation, and live continuation remains exclusively with MEMORY.md.
