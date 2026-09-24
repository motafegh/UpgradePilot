# Effective package-manager semantics system design — 2026-09-24

Status: ACTIVE — design/reconciliation before Build  
Operation: Planning/Design + Learning-by-Doing  
Current intent: determine the proper and smartest coherent system UpgradePilot should build for effective package-manager semantics and runtime dependency-state proof.

## Why this working memory exists

Previous Runtime Dependency-State Proof Cycle 1 correctly rejected a narrow partial implementation that would only classify visible command-local cases such as `--dry-run` or `--no-sync`.

That result should not be interpreted as:

```text
simple implementation is insufficient
→ defer the responsibility
```

The current responsibility is instead:

```text
simple implementation is insufficient
→ use the investigation results to identify the proper system boundary
→ design the coherent evidence/proof subsystem that solves the real problem
→ build it when the design and proof contract are sound
```

The goal is not artificial minimality. The goal is the proper and smartest architecture for the real UpgradePilot product responsibility, while still avoiding unrelated universal infrastructure.

## Prior investigation records

Primary evidence and design records:

- `working-memory/2026-09-21_f6-post-install-package-state-feasibility.md`
  - established the exact F6 proposition;
  - separated runtime correlation from package state;
  - identified real pip/uv counterexamples;
  - compared target-owned runtime-state evidence sources;
  - established real public feasibility and retention limits.

- `working-memory/2026-09-21_runtime-install-command-semantic-eligibility.md`
  - Cycle 1 A→E record;
  - established the package-manager semantic families;
  - accepted B1 command-local semantic eligibility;
  - accepted B2 ownership/composition split;
  - accepted B3 bounded pip/uv semantic surface;
  - accepted B4 effective-semantics fail-closed proof contract;
  - accepted B5 command-success → requirement-satisfied-at-command-completion proof contract;
  - B6 rejected only the insufficient partial implementation routes.

- `working-memory/2026-09-22_b4-environment-evidence-data-flow-learning.md`
  - developed environment provenance/propagation/override reasoning;
  - distinguished declared values from executed writes and received process values;
  - explored `GITHUB_ENV`, step-local env, shell-local overrides, and precedence;
  - accepted proposition-first / demand-driven backward proof as the preferred reasoning strategy.

- `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`
  - owns the durable runtime dependency-state responsibility and proof boundaries.

- `working-memory/2026-09-24_runtime-package-state-decision-criticality.md`
  - parent action-relative investigation;
  - currently paused while this earlier runtime-state responsibility is reconsidered at the proper architecture level.

## Compact durable findings from previous investigation

### 1. Existing runtime correlation is intentionally weaker than package-state proof

```text
exact dependency source/version
+ exact dependency-consuming command
+ exact successful runtime correlation
!=
exact proposed version present in the relevant runtime environment
```

### 2. The problem is broader than visible flags

Material semantic families already identified include:

```text
non-mutating / no-sync behavior
package exclusion / selection narrowing
environment retargeting
overlay / version override
ambient environment/configuration
precedence and propagation
later state mutation
```

Representative examples include:

```text
pip --dry-run
PIP_DRY_RUN
uv --dry-run
uv run --no-sync
UV_NO_SYNC
--no-install-package
--target / --user / --prefix / --root
uv --with conflicting version
workflow/job/step env
GITHUB_ENV
pip/uv configuration
```

### 3. Command-local semantics and effective semantics are different responsibilities

Accepted distinction:

```text
command-local semantic eligibility
!=
effective package-manager semantics
!=
runtime package state
```

A visible decisive command-local defeater can be established positively.

Absence of a visible defeater does not prove effective semantics are safe/non-defeating.

### 4. Effective semantics are proposition-relative and dimension-based

Accepted B4 conceptual contract:

```text
exact occurrence
+ exact state-proof proposition
+ one material semantic dimension
→ resolved_non_defeating
  | resolved_defeating
  | unresolved
```

Aggregation:

```text
any required dimension defeating
→ occurrence cannot serve as the state-producing witness

no defeating + at least one required unresolved
→ effective semantics unresolved

all required dimensions resolved non-defeating
→ effective-semantics gate may close
```

### 5. Preferred proof strategy is demand-driven / backward

Accepted reasoning direction:

```text
exact semantic proposition
→ nearest trustworthy process-level evidence
→ shell-local evidence if needed
→ step-local environment if needed
→ GITHUB_ENV/job/workflow/config provenance only as needed
→ unresolved if a necessary material edge cannot be established
```

The system should not reconstruct irrelevant upstream history when a stronger nearer witness already decides the semantic dimension.

### 6. Ownership split is already clear

```text
GitHub/workflow + shell evidence
→ provenance, scope, ordering, propagation, process-value relationship

dependency/package-manager semantics
→ interpretation of pip/uv meaning

CI/state-proof composition
→ whether those typed facts satisfy the stronger dependency-state proof
```

Do not move pip/uv semantics into Tree-sitter or generic CI runtime code.

### 7. Accepted positive state-proof contract

B5 accepted the following general proof shape:

```text
P1 exact dependency identity
P2 exact source/environment relation
P3 exact static consumption occurrence
P4 command-local semantics admitted
P5 effective semantics resolved non-defeating
P6 exact runtime-success proof
P7 package-manager operation guarantee
→ exact proposed requirement satisfied at command completion
```

The claim stops at that boundary.

It does not establish:

```text
fresh installation by this command
artifact identity
later persistence
later exercise used the same state
behavioral compatibility
maintainer-action permission
```

### 8. What B6 actually rejected

B6 rejected:

```text
only visible command-local flag classification
only workflow/job/step env parsing
synthetic/rare explicit families built merely to satisfy the plan
```

because those routes did not close the real normal effective-semantics problem.

B6 did not prove that a coherent effective-semantics subsystem is undesirable.

The current reconsideration is therefore legitimate:

```text
partial implementation insufficient
→ investigate/design the proper complete bounded subsystem
```

## Current goal

Design the proper and smartest coherent effective package-manager semantics subsystem that UpgradePilot should actually build.

The design should be:

```text
useful for real normal UpgradePilot cases
architecturally coherent
evidence/provenance preserving
fail-closed where truth cannot be established
manager-aware for pip/uv
compatible with current static-consumption and runtime-correlation architecture
capable of composing into B5 requirement-satisfied-at-command-completion proof
extensible to explicit target-owned state evidence when semantic proof cannot close
```

It should not be constrained merely because a narrower implementation is easier.

It also should not become unrelated universal infrastructure such as a full GitHub Actions emulator, complete shell interpreter, or arbitrary operating-system environment simulator unless real evidence later proves such scope is required.

## Next design question

The next question is:

> What should the first proper and smart supported effective-semantics boundary contain so that it solves the real normal pip/uv problem coherently, and what should intentionally remain unresolved outside that boundary?

We should answer this by comparing real evidence sources and relationships already discovered, including:

```text
command-local options
shell-local assignments/exports
workflow/job/step env
proven GITHUB_ENV writes and propagation
package-manager environment variables
observable pip/uv configuration
retargeting/environment identity
manager-specific precedence
runtime-success identity
optional explicit target-owned state witnesses
```

The result of this design step should be a coherent subsystem boundary and implementation sequence, not another isolated rule list.

## Current state

```text
R1 — prior investigation reconstruction: DONE
R2 — proper subsystem boundary design: NEXT
R3 — source/type/data-flow design: PENDING
R4 — implementation/proof sequence: PENDING
R5 — Build authorization and implementation: PENDING
R6 — real-case + regression proof: PENDING
R7 — return to parent synthesis/action integration: PENDING
```

## Guardrails

- do not optimize for artificial minimality;
- do not implement isolated flag rules as the end solution;
- preserve uncertainty when required evidence is missing;
- use real product pressure and real supported cases;
- preserve current owner boundaries;
- do not weaken B4/B5 proof standards merely to make implementation easier;
- do not turn the subsystem into universal CI/shell/environment emulation without evidence;
- build the proper system once its boundary is understood well enough to justify implementation.
