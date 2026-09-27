# Increment 1 — Reusable Step and Exact-Command Execution Evidence — Learning-by-Doing Cycle

**Date:** 2026-09-27  
**Cycle status:** ACTIVE — canonical D current  
**Primary operation:** Build / Implement with canonical Learning-by-Doing  
**Controlling plan:** `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`  
**R4 implementation plan:** `working-memory/2026-09-27_runtime-dependency-state-proof-implementation-and-verification-planning.md`  
**Accepted architecture:** `docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md`  
**Live position owner:** `MEMORY.md`

UP-SKILL:upgradepilot-build-implement  
UP-SKILL:upgradepilot-learning-by-doing  
UP-SKILL:upgradepilot-working-memory

## Canonical cycle status

```text
A — DONE
B — DONE
C — DONE / progressively maintained through implementation
Verification gate — GREEN
D — CURRENT
E — PENDING
```

The verification gate is intentionally recorded between B+C and D. It is **not** canonical D.

## Cycle responsibility

Build the first shared runtime-execution evidence layer required by later setup-python, environment propagation, venv, package-manager, Route-A and optional Route-B reasoning:

```text
static/runtime user-step identity
→ unmasked successful user-step execution
→ exact command-occurrence execution when shell/structure eligibility permits
```

Preserve the existing CI dependency-coverage proof boundary. This cycle does **not** add package-manager semantics or package-state proof.

## A — Pre-implementation learning / orientation — DONE

### Starting model

Before Build, the current path was traced as:

```text
WorkflowRuntimeStepCorrelation
→ RuntimeStrengtheningEligibility
→ dependency_exercise.py privately combines:
   exact-step lookup
   + continue-on-error interpretation
   + runtime status/conclusion
→ existing CI coverage states
```

The important boundary established before implementation:

```text
step success
!=
proof that every command inside that step executed
```

The planned ownership split was:

```text
WorkflowRuntimeStepCorrelation
        ↓
CorrelatedStepExecutionAssessment
        ↓
ExactCommandExecutionAssessment
        ↓
domain consumers such as dependency_exercise
```

GitHub Runner source was checked for unnamed user-step display identity. For the admitted literal class, Runner derives a `Run ` prefix plus the repository action reference or first script line; dynamic values remain unresolved.

### Professional engineering ownership opportunity identified

Primary:
- **code/system understanding** — trace identity → execution evidence → domain-consumer responsibility.

Secondary:
- **design/system judgment** — understand why generic runtime execution belongs in a reusable CI layer rather than inside dependency-specific coverage logic.

Required depth:
- **must own** the responsibility/proof boundaries and normal flow;
- exact incidental Python syntax remains operational/lookup-level.

### A understanding gate

The intended B responsibility was explained before implementation: refactor generic execution truth into reusable CI evidence, add bounded unnamed-step correlation, preserve existing coverage semantics, and avoid package-manager/state-proof work in this cycle.

Historical note: this cycle began before the newly clarified governance rule required an explicit hard stop after A. Future cycles must stop at that gate. This record preserves the actual history rather than pretending the new gate occurred retroactively.

## B — Real bounded Build / action — DONE

Implementation head before later documentation-only commits:

`a47923ee778b0984966bc09b8d01169205d0f7f9`

### Implemented responsibility

1. **`ci/workflow_runtime_correlation.py`**
   - added provider-derived display identity for bounded unnamed literal `run:` and repository/local `uses:` steps;
   - dynamic/unsupported unnamed cases stay unresolved;
   - correlation still owns identity only.

2. **`ci/runtime_strengthening.py`**
   - introduced parser-neutral `RuntimeStrengthenableCommandOccurrence` protocol;
   - existing static shell/structure eligibility remains reusable and dependency-agnostic.

3. **new `ci/runtime_execution.py`**
   - `CorrelatedStepExecutionAssessment` owns unmasked runtime step success/failure/unresolved interpretation for correlated `run:` and `uses:` steps;
   - `ExactCommandExecutionAssessment` composes exact command eligibility with correlated step execution;
   - no dependency or package-manager semantics are introduced.

4. **`ci/dependency_exercise.py`**
   - stopped owning generic continue-on-error/runtime-status/exact-step interpretation;
   - now consumes reusable exact-command execution evidence;
   - preserves its existing public CI dependency-coverage semantics/reasons.

5. **tests**
   - runtime-correlation coverage protects unnamed run/uses identities and dynamic fail-closed behavior;
   - new `tests/test_ci_runtime_execution.py` protects shared step-success interpretation and exact-command execution boundaries.

### Build commits

- `bd9bf2b` — correlate unnamed user steps with Runner display identities
- `4190053` — test unnamed workflow-step identities
- `6e1cea3` — generalize runtime-strengthening eligibility protocol
- `97ac7d8` — add reusable step/exact-command execution evidence
- `69d4c5f` — focused execution-evidence tests
- `ad030ac` — migrate dependency coverage to reusable execution evidence

## C — Progressive state preservation — DONE / continuous through B

Meaningful progression was preserved during the Build rather than deferred until final closure:

- the old private ownership/coupling was identified before mutation;
- Runner display-name evidence was verified before adding unnamed-step correlation;
- the new execution layer was kept free of package-manager/dependency semantics;
- `dependency_exercise.py` was deliberately made a consumer rather than another execution owner;
- verification debt was explicitly recorded while tests could not initially be executed by the assistant environment;
- later executable evidence was added when Ali ran the proof surfaces.

No package-manager semantic facts, environment/config producers, Route-A state composer, maintainer-action expansion, or Route-B acquisition were added.

## Verification / evidence gate — GREEN

### Focused local proof

Ali ran the focused Increment-1 test set:

- **35 tests passed**
- no failures/errors.

The set covers:
- workflow runtime correlation;
- reusable runtime execution;
- runtime strengthening;
- runtime-correlated dependency coverage.

### Full deterministic regression

Ali ran:

```bash
python3 -m unittest discover -s tests -v
```

Result:

- **632 tests passed**
- no failures/errors.

### Product verification

Repository workflow:
- **Product verification**
- run id: **36338591767**
- event: `workflow_dispatch`
- exact implementation head: `a47923ee778b0984966bc09b8d01169205d0f7f9`
- conclusion: **success**

Material successful job:
- **Installed package and deterministic product tests**

Material successful steps included:
- fresh product installation;
- CLI entry-point verification;
- focused investigation composition;
- deterministic product regression.

### What this gate proves

It supports that:
- the new execution-evidence responsibility passes focused tests;
- the existing deterministic suite remains green;
- installed-product verification remains green on the exact implementation head;
- existing CI coverage behavior was not broken by the ownership refactor.

It does **not** prove:
- package-manager effective semantics;
- manager environment/destination resolution;
- Route-A package-state satisfaction;
- later package use/compatibility;
- maintainer-action permission.

Those belong to later increments.

## D — Post-implementation learning / ownership check — CURRENT

This phase must now teach from the **actual implemented and verified source**, not from the old plan.

D should cover proportionately:

1. actual source responsibility flow:
   `workflow_runtime_correlation.py`
   → `runtime_execution.py`
   → `runtime_strengthening.py`
   → `dependency_exercise.py`;

2. distinction between:
   - correlation/identity;
   - step execution;
   - exact-command eligibility/execution;
   - dependency-domain interpretation;

3. important states/failure paths:
   - supported;
   - not established;
   - unresolved;
   - continue-on-error masking;
   - failed/skipped runtime step;
   - structurally ineligible/unresolved command;

4. what the focused tests protect and what they do not prove;

5. ownership check through a small number of open-ended reasoning questions.

Do not infer ownership from Ali approving the design, running tests, or tests passing.

## E — Gap repair + next-slice orientation — PENDING

After D questions:

1. identify only central reasoning/ownership gaps;
2. repair them at minimum useful depth;
3. keep incidental syntax/API detail operational/lookup-level;
4. state what Increment 1 now establishes and what remains deferred;
5. briefly orient the next bounded slice, expected to be **Increment 2 — static package-manager operation declaration and semantic-fact core** if no new evidence changes the route;
6. stop before Increment 2 B; the next cycle must begin with its own A and explicit understanding gate.

## Governance clarification learned during this cycle

During the cycle, Ali identified drift in how A/B/C/D/E had been operationalized. The durable method was subsequently clarified in:
- `AGENTS.md`;
- `OPERATING_GUIDE.md`;
- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`;
- `.agents/skills/upgradepilot-working-memory/SKILL.md`;
- `working-memory/README.md`.

The corrected cadence is:

```text
A
→ STOP / understanding gate
→ B + C together
→ verification/evidence gate
→ D post-implementation learning/ownership
→ E gap repair + next-slice orientation
→ next cycle begins at A
```

This dedicated record is the single cycle-status owner for Increment 1. The R4 plan remains the broader implementation-sequence owner.
