# Cycle 1 — Runtime dependency-state semantic proof — 2026-09-21

**Status:** ACTIVE — Cycle 1 ready to begin at Phase A.  
**Master plan:** `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`  
**Investigation evidence:** `working-memory/2026-09-21_f6-post-install-package-state-feasibility.md`  
**Operation:** canonical Learning-by-Doing A → B → C → D → E, composed with the applicable primary operation. Planning/Design controls the cycle until a Build decision is explicitly selected.

## Cycle responsibility

Establish whether UpgradePilot can truthfully derive:

```text
exact proposed dependency version
+ semantically eligible dependency-consuming command
+ exact successful runtime correlation
→ proposed version satisfied/present at the admitted command-completion boundary
```

without adding a new runtime package-state/log producer unless the evidence proves that one is necessary.

Cycle 1 combines two closely coupled master-plan layers:

1. install-command semantic eligibility;
2. command-success → dependency-state proof contract.

## Entry state

The full F6 investigation is complete.

Verified source facts entering this cycle:

- Tree-sitter already preserves shell structure and literal command arguments;
- `pip install --dry-run -r requirements.txt` can currently retain the same direct requirements-source declaration as an ordinary install because `--dry-run` is not yet interpreted at the dependency semantic layer;
- short-circuit, conditional, pipeline, asynchronous and related shapes are shell-structure concerns already represented by the parser-backed provider;
- current runtime correlation establishes bounded successful execution, not resulting package state;
- generic job-log/package-state acquisition is not selected.

## Agreed Cycle 1 working rhythm

This cycle follows the root `AGENTS.md` Learning-by-Doing contract exactly:

```text
A — pre-implementation learning / orientation
B — real bounded action
C — progressive state preservation
D — post-action learning / ownership check
E — gap repair + next-slice orientation
```

The phases are not equal in size. Phase B is expected to contain most engineering work; Phase C is progressive rather than paperwork-heavy; A/D/E are interactive learning and decision checkpoints.

### Interaction agreement

- Work in **small meaningful chunks inside each phase**, not micro-phases.
- Ali may interrupt or challenge any premise; if a premise is challenged, stop advancing that proposition and verify it before continuing.
- Do not ask Ali to reason from premises that have not yet been taught or established.
- Use real source/tests/evidence first; avoid detached quizzes and fictional examples when real evidence is available.
- Reasoning checks should come from the real work and focus on ownership, proof, design, diagnosis, or changed cases.
- Do not silently jump from A → B or B → D.
- Do not silently create or begin Cycle 2.
- If new evidence exposes a better route, challenge the current plan rather than following it mechanically; update the correct plan/owner before materially changing route.
- Ali's target ownership is not source-code memorization. Priority is understanding the source/proof flow, design judgment, verification, diagnosis, and exact proof/non-proof boundaries.
- Mechanical source tracing, repetitive inspection, and routine edits may be handled by the AI; consequential design/proof decisions remain interactive.

Approximate interaction intensity:

```text
A — very high
B — medium-high
C — low
D — very high
E — high but short
```

## Phase status tracker

```text
A — IN PROGRESS: source/proof flow re-anchored; Ali reconstruction/acceptance-boundary check remains
B — PENDING: real source-backed design/action and possible bounded implementation
C — PENDING: progressive preservation + formal proof-state checkpoint
D — PENDING: post-action learning / ownership verification
E — PENDING: gap repair + Cycle 1 closure / Cycle 2 decision
```

Update this tracker only at meaningful transitions.

## Phase A — orientation / minimum-complete learning — IN PROGRESS

**Purpose:** make the coming engineering action understandable before doing the real classification/design work.

### Tasks

1. Reconstruct the important current flow only to the depth needed for this cycle:
   ```text
   Tree-sitter / shell structure
   → parsed command occurrence
   → pip/uv semantic interpretation
   → dependency consumption
   → runtime correlation
   → possible dependency-state proof
   ```
2. Re-establish why shell-structure cases such as short-circuit/conditional/pipeline are different from package-manager semantic options such as `--dry-run`.
3. Establish the Cycle 1 success boundary:
   - what stronger proposition we want to earn;
   - what important negative/unresolved states must remain distinguishable;
   - what stronger claims remain out of scope.
4. Establish the minimum relevant source/type/file map before Phase B.
5. Give Ali room to interrupt/challenge/reconstruct the model before real engineering work starts.

### Interaction

Very interactive but concise. Explain first; do not quiz before premises exist.

### Phase A output

Ali and the AI share a minimum-complete mental model of the current source/proof flow, responsibility boundaries, and Cycle 1 acceptance/non-goal boundary.

### Phase A progress — source/proof flow re-anchored

Fresh source inspection confirmed this ownership chain:

```text
workflow_command_analysis.py
→ shell syntax/structure + parser-neutral command atoms

pip_command.py / environment_selection.py / direct_install.py
→ bounded dependency/package-manager interpretation

workflow_commands.py + consumption.py
→ exact static CI changed-dependency consumption proposition

runtime_strengthening.py + dependency_exercise.py
→ bounded eligibility + exact successful runtime correlation

Cycle 1 target
→ only then consider the stronger proposed-version-present/satisfied proposition
```

Key boundary reconfirmed: `dependency_exercise.py` explicitly states that `supported_runtime_correlated` does not prove the exact resolved version, wheel, or compatibility. The current Cycle 1 responsibility is therefore a new stronger composition boundary, not a reinterpretation of existing runtime-correlation evidence.

Remaining Phase A work: Ali reconstructs the owner/proof boundaries and confirms the intended success/non-goal model before Phase B begins.

### Phase A stop line

No broad source classification, no design selection, and no product implementation. Those are Phase B responsibilities.

## Phase B — real bounded engineering action — PENDING

**Purpose:** perform the actual Cycle 1 engineering work. Because the initial primary operation is Planning/Design, Phase B begins with real source-backed investigation and design rather than coding.

### Planning/Design tasks

1. Trace current pip and uv option handling from parsed command atoms into dependency-consumption/project-environment evidence.
2. Enumerate only the materially relevant options reachable in today's supported product paths.
3. Classify each relevant case:
   - positive / compatible with stronger state inference;
   - non-installing / excluding / retargeting;
   - ambiguous / dynamic / unsupported.
4. Compare that classification with existing focused tests and real supported scenarios.
5. Identify the earliest correct semantic owner for the rule.
6. Determine the smallest trustworthy command-success → dependency-state proof contract.
7. Decide whether existing result types are sufficient or whether a new state/result is actually necessary.
8. Surface the consequential design decision to Ali before Build/Implement begins.

### Build continuation — only if explicitly authorized after the design checkpoint

If Ali explicitly authorizes Build and the design is sufficiently resolved, Phase B may continue within the same cycle responsibility:

- implement only the earliest required owner(s);
- add focused positive, close-defeater, and unresolved tests;
- connect the smallest required normal-path composition;
- preserve existing declaration evidence rather than overloading it with claims it does not own.

A switch from Planning/Design to Build does not automatically create another cycle because the semantic responsibility remains the same.

### Interaction

Medium-high. The AI may perform mechanical source tracing and routine inspection, but should surface findings in meaningful chunks. Ali should participate at real design/proof decisions, not every file or option.

### Phase B output

A source-backed semantic classification and proof design; if Build is authorized, the bounded implementation and focused tests needed by that design.

### Phase B stop lines

- no generic log ingestion;
- no explicit package-state producer merely because such evidence exists;
- no silent responsibility expansion;
- no implementation before the design checkpoint is understood and Build is authorized.

## Phase C — progressive state preservation and proof-state checkpoint — PENDING

**Purpose:** preserve the real engineering progression without turning preservation into a separate paperwork exercise.

### During Phase B

Update this working-memory record at meaningful progression points with:

- decisions and changed understanding;
- important source/evidence findings;
- implementation changes when any;
- tests/proof obtained;
- surprises/failures and corrections;
- explicit proof debt;
- what is and is not established.

### Formal checkpoint before Phase D

Record compactly:

```text
what was discovered/changed
→ what evidence exists
→ what remains unproven
→ current A/B/C status
```

Update `MEMORY.md` only if the live position, milestone, blocker, deferral, or selected continuation materially changes.

### Interaction

Low. The AI maintains the record and briefly tells Ali what was preserved.

### Phase C stop line

Do not convert unexecuted tests, source review, or deferred runtime proof into a pass claim.

## Phase D — post-action learning / ownership check — PENDING

**Purpose:** learn from what was actually designed, implemented, and proven rather than from the pre-work theory.

### Tasks

1. Trace the actual resulting flow:
   ```text
   input/source
   → semantic rule
   → evidence state
   → runtime composition
   → resulting dependency-state proposition
   → exact proof boundary
   ```
2. Compare planned behavior with what source/tests/evidence actually show.
3. Explain the important code/types/states/failure modes only to the depth required for ownership.
4. Inspect focused/integration/regression/live evidence at its actual proof strength.
5. State what the result proves and what stronger claim it does not prove.
6. Use only 1–2 meaningful open-ended reasoning checks from the real slice, such as:
   - a changed pip/uv command;
   - owner/layer placement;
   - proof/non-proof distinction;
   - diagnosis of one close-defeater case.
7. Check the durable ownership opportunity:
   - primary: source/proof-flow understanding;
   - secondary: design/system judgment and verification.

### Interaction

Very high. This is the main ownership-transfer phase.

### Phase D success

Ali can explain the important source/proof flow, why the chosen owner/layer is correct, and what the evidence establishes without needing to reproduce source syntax from memory.

## Phase E — gap repair + Cycle 1 closure / next-cycle decision — PENDING

**Purpose:** repair only important gaps, then decide the continuation from actual evidence.

### Tasks

1. Use Phase D answers/evidence to identify any important learning or engineering gaps.
2. Repair only gaps central to the current responsibility.
3. Distinguish:
   - learning gap;
   - implementation/proof gap;
   - genuinely new product responsibility.
4. Decide Cycle 1 closure:

   ```text
   Cycle 1 sufficient
   → close runtime dependency-state proof at this bounded path
   → do NOT create Cycle 2
   → return to parent evidence-to-action plan

   Cycle 1 insufficient for a real decision-critical normal case
   + explicit target-owned package-state evidence is justified
   → append/select conditional Cycle 2 in the master plan
   → create a new active Cycle 2 working-memory record
   ```

5. Briefly orient the next selected responsibility only after the closure decision is earned.

### Interaction

High but short. Ali and the AI make the closure/continuation decision together.

### Phase E stop line

Do not create Cycle 2 merely for completeness, and do not silently roll downstream behavior/action work into this cycle.

## Cycle pass condition

One bounded normal command family has a precise, source-backed proof path from exact dependency source through semantic eligibility and exact successful runtime correlation to proposed-version presence/satisfaction at the admitted command-completion boundary, while close defeaters remain explicit.

## Current handoff

Start **Phase A** only.

The immediate task is orientation: reconstruct the exact source/proof flow and acceptance boundary needed to make the later Phase B classification/design meaningful. No Build/Implement action has yet been selected.

**Procedural provenance:** `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`.
