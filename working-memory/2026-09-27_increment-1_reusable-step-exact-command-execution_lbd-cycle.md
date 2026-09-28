# Increment 1 — Reusable Step and Exact-Command Execution Evidence — Learning-by-Doing Cycle

## **Smart Situational Override Rule**

This cycle follows the canonical A/B/C/verification/D/E cadence under the **Smart Situational Override Rule**. The recorded phase state reflects the route actually taken, not a rigid requirement to force future work through the same shape. If D/E or any later cycle phase must be expanded, shortened, reordered, paused, or otherwise adapted because the real situation requires it, state the reason and update this record rather than silently drifting.

The rule does not create new authorization or weaken evidence truth; verification remains what the evidence actually established.


**Date:** 2026-09-27  
**Closed:** 2026-09-28  
**Cycle status:** CLOSED — A/B/C + verification + D/E complete  
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
D — DONE
E — DONE
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

## D — Post-implementation learning / ownership check — DONE

Post-implementation learning was performed from the actual verified source and focused on the real evidence ladder:

```text
static/runtime step identity
→ correlated user-step execution
→ exact-command structural eligibility
→ exact-command execution
→ domain consumer interpretation
```

Key ownership outcomes:
- Ali correctly understood that successful step execution cannot prove an arbitrary later command ran when shell structure may bypass it;
- Ali correctly understood why step execution and exact-command execution are separate evidence propositions with separate provenance rather than one boolean;
- one material gap surfaced in the ownership questions: Ali initially interpreted `ExactCommandExecutionAssessment = supported` as proving only structural/correlation readiness rather than the stronger bounded proposition that the exact command occurrence itself executed successfully;
- that gap was repaired: **exact command execution can be supported while package-manager effect/package-state remains unproven**.

The resulting proof ladder now owned for this slice is:

```text
exact command executed successfully
!= effective package-manager semantics
!= target Python environment/destination
!= package-state satisfaction
!= later package use
!= compatibility/action permission
```

Learning-depth calibration was also clarified. Ali is not expected to memorize every class/function/reason code. Required ownership is:
- retain the system responsibility, important evidence/proof boundaries, normal flow and important failure/unresolved states;
- recognize the source areas and know how to recover exact APIs/types/tests from the repository;
- keep incidental symbol names, helper details and exact reason strings at recognize/lookup level unless a later responsibility makes them central.

This satisfies the selected D ownership opportunity: code/system understanding plus design/system judgment over the execution-evidence boundary.

## E — Gap repair + next-slice orientation — DONE

### Gap repair

The central D gap was repaired at the minimum useful depth:

```text
Correlation/structure + runtime evidence
→ can establish exact-command execution

but

exact-command execution
→ does not establish what pip/uv effectively did
→ does not establish resulting package state
```

No further central Increment-1 ownership gap currently blocks continuation. Exact implementation symbol memorization is intentionally not required.

### Increment 1 closure

Increment 1 now establishes a reusable, verified execution-evidence foundation:

```text
WorkflowRuntimeStepCorrelation
→ CorrelatedStepExecutionAssessment
→ ExactCommandExecutionAssessment
→ dependency/domain consumers
```

with provider-backed unnamed literal step identity, continue-on-error masking, structural eligibility, explicit supported/not-established/unresolved states, and preserved existing dependency-coverage semantics.

It still intentionally does **not** establish:
- package-manager effective operation semantics;
- manager-selected Python environment;
- final installation destination;
- dry-run/direct-requirement handling as package-manager facts;
- requirement satisfaction/package state at command completion;
- later use/compatibility/action permission.

### Next-slice orientation

The next planned responsibility remains technically justified by the implementation evidence:

**Increment 2 — static package-manager operation declaration and semantic-fact core.**

Its purpose is to move from:

```text
"this exact command executed"
```

toward:

```text
"this exact command is a specific pip/uv operation with explicit static invocation semantics
that can feed independent package-manager semantic facts"
```

The next cycle should begin with canonical A and explain before Build:
- why one `PackageManagerOperationDeclaration` should parse an occurrence once;
- invocation families such as bare pip, `python -m pip`, supported explicit interpreter forms and global `--python`;
- why manager environment, installation destination, mutation mode and direct-requirement handling remain separate facts;
- what Increment 2 deliberately does **not** solve yet: ambient process environment/config/default reconstruction and final package-state composition.

Per the canonical LbD method, stop at Increment 2's A understanding gate before its B starts.

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

Governance/process promotion commits for this clarification include:
- `c4fa855` — final root `AGENTS.md` gate correction;
- `eba06bd` — full LbD Skill alignment;
- `c4eaee0` — Operating Guide cadence alignment;
- `371ee5e` — working-memory Skill cycle ownership;
- `29a481c` — working-memory owner/readme cycle structure;
- `16349e3` — R4 record reconciled so it no longer owns competing phase status;
- `4704716` — live `MEMORY.md` points to canonical D and this cycle record.

This dedicated record is the single cycle-status owner for Increment 1. The R4 plan remains the broader implementation-sequence owner.
