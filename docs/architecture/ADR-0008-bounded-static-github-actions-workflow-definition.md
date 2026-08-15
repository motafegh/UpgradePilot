# ADR-0008 — Bounded Static GitHub Actions Workflow Definition

**Status:** Accepted  
**Date:** 2026-08-15  
**Owner:** Ali Rajabi  
**Scope:** GitHub Actions static workflow-definition structure, parser method, provider/domain dependency direction, and static/runtime evidence separation

## Context

B2 now has two implemented responsibilities that consume GitHub Actions workflow definitions for materially different purposes:

```text
CI dependency exercise
→ did admitted successful exact-head CI consume/exercise the changed dependency?

Target artifact environment
→ what scoped environment/configuration facts can exact target evidence establish?
```

The first implementations independently parse overlapping workflow structure in `ci/workflow_commands.py` and `target/artifact_environment.py`, including job discovery, `run` blocks, direct `pip`/requirements installation syntax, and repository-path handling.

The duplication is not merely cosmetic. It has begun to create architectural and proof-strength pressure:

```text
static workflow declaration
!= runtime execution
!= runtime success
!= environment formation
!= dependency behavior exercise
```

The Target first slice currently uses runtime-sounding `dependency_environment_formation` terminology for a state derived only from static workflow text. The CI first slice combines successful run/job evidence with static command recognition under a bounded `proven` state, while AUDIT-002 shows that this is not the same as proving matched install/exercise steps executed and succeeded.

Real workflow/case pressure also demonstrates that a durable source reader must not encode one current consumer's limitations as permanent source limitations. GitHub Actions workflows may contain multiple jobs, matrices, dynamic values, reusable-workflow jobs, containers, ordered steps, conditions, run-context fields, and other valid structure that a current CI or Target interpreter may not yet understand semantically.

Phase A mapped the current responsibilities. Phase B compared local parsers, a shared static workflow representation, and a broader combined static/runtime model. Phase C adversarially pressure-tested the leading design against product-simulation cases and the existing CI proof-boundary audit. Phase D accepted the decisions recorded below.

## Decision

### 1. Introduce one bounded provider-specific static workflow-definition responsibility

The accepted dependency direction is:

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

The shared representation owns **what bounded GitHub Actions source structure visibly declares**. It does not own CI conclusions, Target conclusions, dependency exercise, exact target compatibility, or runtime-success claims.

This structure belongs under `upgradepilot.github` because it is neutral between CI and Target consumers while still being specifically GitHub Actions syntax. Shared across consumers does not make it source-neutral.

### 2. Preserve exact source and selectively normalize provider structure

`RepositoryTextFile` remains the authoritative exact source/provenance object. The static workflow representation references that source and preserves only the provider structure current responsibilities or demonstrated near-term pressure require.

The admitted structural surface includes, where safely readable:

```text
workflow-level run defaults
ordered jobs
job key/name
needs
runs-on structure
if
continue-on-error
job run defaults
matrix/strategy fragment
container fragment
reusable-workflow job shape/reference
ordered steps
run step command + shell + working-directory
uses step reference + with inputs
source occurrence/index and diagnostic source location where useful
```

Dynamic values are valid source evidence, not parser failure:

```text
absent
!= present + literal
!= present + dynamic/expression-backed
```

Multiple jobs are preserved structurally even when a current consumer cannot safely select or compose them. `needs` and source order are structural facts; they do not prove runtime scheduling, environment continuity, or cross-job state transfer.

The representation is deliberately **not** a generic YAML AST, full GitHub Actions schema, expression evaluator, shell interpreter, matrix executor, reusable-workflow executor, or environment reconstruction model.

### 3. Keep static definition and runtime Actions evidence separate

Existing runtime provider evidence remains a separate family:

```text
github/actions.py
→ WorkflowRun
→ WorkflowJob
→ WorkflowStep
```

The base static representation must not merge with runtime run/job/step instances.

A later stronger CI capability may explicitly correlate identifiable static jobs/steps with runtime evidence, but that correlation is a separate optional responsibility. Its algorithm is not selected by this ADR.

This separation preserves the evidence ladder:

```text
static definition
!= runtime instance
!= runtime success
```

and avoids forcing one static matrix job into a fabricated one-to-one runtime identity.

### 4. Use PyYAML representation/node parsing as the selected syntax method

PyYAML is the accepted YAML parser dependency/method for this responsibility.

The implementation method is:

```text
RepositoryTextFile.content
        ↓
PyYAML representation/node parsing
        ↓
bounded UpgradePilot GitHub Actions extraction
        ↓
typed static workflow-definition IR
```

PyYAML parser/node objects remain internal syntax machinery. Ordinary YAML mappings/lists or parser-specific nodes do not become UpgradePilot's public/domain representation.

The implementation should use a non-arbitrary-object construction path suitable for untrusted repository evidence and should preserve enough node structure/source location to detect material ambiguity before collapsing it into domain objects.

If implementation evidence later demonstrates that PyYAML cannot satisfy the accepted contract proportionately, a follow-up decision may replace the library without discarding the provider/domain architecture.

### 5. Apply proportionate untrusted-YAML safeguards

Public repository workflow text is untrusted evidence.

The parser boundary must therefore preserve the repository's existing source-size bound and provide proportionate safeguards against obvious structural/resource hazards, including:

- no arbitrary application-object construction from YAML;
- safe failure/abstention for malformed or materially ambiguous structure;
- duplicate material identity/key detection where silent collapse would fabricate meaning;
- bounded recursion/traversal sufficient to prevent obvious alias/cycle/resource abuse.

Exact numeric depth/node limits, exception types, and similar mechanics are implementation/test decisions unless later evidence requires stronger durable policy. `SECURITY.md` owns the repository-wide untrusted-evidence safety invariant.

### 6. Share direct-installation declaration observation at the dependency boundary

The pure GitHub Actions IR preserves run structure and run context. It does not become dependency-aware merely because a command contains `pip`.

A separate bounded shared primitive may interpret:

```text
static run command
+ effective working-directory context
+ independently established dependency-source path
→ direct installation declaration observation
```

This responsibility belongs under `upgradepilot.dependency` because its meaning is the relation between a command and a dependency source, not GitHub Actions syntax itself.

Its proof strength stops at declaration/configuration:

```text
direct installation declaration observed
!= command executed
!= command succeeded
!= exact proposed dependency version installed
!= changed dependency consumed generally
!= changed package exercised
```

Package invocation/exercise recognition remains CI-specific. S005 demonstrates that exact dependency consumption may instead require lock/resolver/tox/uv/matrix or other evidence chains, so the shared direct-install primitive must not become a universal dependency-consumption abstraction.

### 7. Correct Target and CI claim strength during implementation

The first implementation tranche must migrate Target's current runtime-sounding environment-formation state to static direct-installation-declaration semantics.

It must also narrow/refine the current CI `proven` contract so a successful exact-head run/job plus static install/invocation path is not presented as if the matched commands were runtime-correlated and successful.

This ADR selects the proof boundary, not the exact replacement field/enum names. Those API details belong to the implementation plan, source, and tests.

### 8. Do not solve arbitrary multi-job semantics in the base migration

The shared IR preserves safely readable multiple jobs and their structural relations.

CI and Target may remain unresolved/unsupported when their current proposition cannot safely select or compose those jobs. The migration must not infer:

```text
install in job A
+
exercise in job B
→ same environment / dependency continuity
```

without explicit evidence that justifies that proposition.

## Rejected alternatives

### Keep separate CI and Target workflow parsers

Rejected as the durable direction because the duplicated provider syntax is already demonstrated and continuing it would require the same GitHub/YAML structural corrections to evolve independently in multiple domains.

A consumer-local parser remains an acceptable fallback only if the shared contract later proves unable to preserve the required provider structure safely.

### Put the shared structure under `ci/` or `target/`

Rejected because either choice creates the wrong dependency direction. Target may consume static workflow configuration without successful CI; CI also requires the same source structure without inheriting Target semantics.

### Put the structure in a generic `common`/workflow package

Rejected because `jobs`, `runs-on`, `uses`, `with`, matrices, reusable-workflow jobs, and related fields are GitHub Actions concepts. Cross-consumer does not imply provider-neutral.

### Keep expanding the custom indentation parser

Rejected as the shared long-lived foundation. It was proportionate for the original bounded first slices, but a shared provider owner should not gradually reimplement YAML structure as valid workflow variation grows.

### Parse YAML directly into ordinary Python mappings as the domain contract

Rejected because early native construction can lose source/duplicate-key information, can coerce scalars before UpgradePilot decides their meaning, and would expose generic YAML representation instead of the bounded provider contract.

### One combined static + runtime Actions base object

Rejected because it blurs definition identity with execution-instance identity and makes matrices/retries/multiple executions harder to represent honestly. A proof-safe version decomposes naturally into the accepted static IR plus existing runtime evidence plus an explicit later correlation layer.

### Universal workflow/environment engine

Rejected. This ADR does not authorize full Actions expression evaluation, shell execution, matrix expansion, reusable-workflow recursion, generic CI providers, environment reconstruction, arbitrary task/script tracing, or universal provenance/impact engines.

## Consequences

Positive:

- CI and Target share provider structure without sharing domain conclusions;
- valid multi-job/dynamic workflow structure can be preserved even when a current consumer abstains;
- static and runtime proof strength remain explicit;
- Target can continue to use workflow evidence as one evidence source without becoming a child of CI;
- PyYAML handles YAML syntax while UpgradePilot retains a small typed provider contract;
- direct-install declaration logic can converge without becoming a universal dependency-consumption claim;
- later runtime-correlation strengthening has a clear seam rather than requiring a redesign of the base model.

Costs:

- PyYAML becomes a runtime dependency once the implementation tranche begins;
- a new bounded static provider model and parser tests are required;
- CI and Target must migrate from their local shallow readers;
- current Target and CI state/wording requires compatibility-aware migration in the pre-1.0 codebase;
- parser safety and ambiguous-structure handling require focused tests;
- structural multi-job support does not itself give consumers multi-job semantic understanding.

## Deferred / intentionally undecided

This ADR does not select:

- exact Python class/module names beyond ownership under `upgradepilot.github` and `upgradepilot.dependency`;
- exact PyYAML version range until implementation dependency integration;
- exact parser depth/node limits;
- exact static↔runtime step-correlation algorithm;
- arbitrary matrix expansion or runtime instance mapping;
- arbitrary reusable-workflow/container execution semantics;
- cross-job environment continuity rules;
- universal dependency-consumption tracing;
- exact heterogeneous impact/orchestration envelope;
- final action/recommendation synthesis.

Application orchestration has demonstrated pressure to carry multiple typed mechanism results, but the exact envelope remains deferred until the second mechanism enters the real application path.

## Reassessment triggers

Reassess this decision if demonstrated evidence shows that:

- PyYAML cannot safely/proportionately preserve the required bounded source structure;
- a second CI provider creates genuinely provider-neutral workflow semantics worth extracting;
- static/runtime correlation cannot be expressed as a separate evidence responsibility without duplicating or weakening identity;
- repeated consumer needs justify additional typed workflow fields;
- direct-install declaration semantics differ materially between current callers;
- a real multi-job proposition requires explicit cross-job continuity/transfer semantics;
- parser hardening begins to exceed the demonstrated risk/value boundary and requires a different ingestion strategy.

## Evidence and related owners

- [`../../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](../../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md) — bounded architecture checkpoint and phase sequence.
- [`../../working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md`](../../working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md) — Phase A/B reasoning and progressive findings.
- [`../../product-simulation/CROSS_RESPONSIBILITY_ARCHITECTURE_PHASE_C_PRESSURE_TEST_01.md`](../../product-simulation/CROSS_RESPONSIBILITY_ARCHITECTURE_PHASE_C_PRESSURE_TEST_01.md) — non-controlling Phase-C pressure evidence adopted by the architecture owner.
- [`../../audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md`](../../audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md) — CI proof-strength hazards.
- [`../specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) — canonical framework-independent evidence/decision semantics; not duplicated here.
- [`ADR-0007-responsibility-based-python-subpackages.md`](ADR-0007-responsibility-based-python-subpackages.md) — source-ownership baseline.
- [`../../SECURITY.md`](../../SECURITY.md) — untrusted-evidence/parser safety invariant.

Implementation proof, dependency installation, test results, and live continuation remain owned by source/tests/commands/evidence and `MEMORY.md`, not by this ADR.
