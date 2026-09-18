# UpgradePilot Current Memory

**Last updated:** 2026-09-18  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** Cycle 3 **Phase A — runtime-strengthening eligibility orientation/design**.
- **Mode:** pre-implementation Planning / Learning-by-Doing. Do not mutate product source/tests until the bounded Phase-A contract is accepted.
- **Cycle state:** **Cycle 1 CLOSED; Cycle 2 A/B/C CLOSED; Cycle 2 D CLOSED with explicit deferred learning; Cycle 2 E COMPLETE with no repair increment; Cycle 3 A ACTIVE**.
- **Selected Cycle-3 working memory:** `working-memory/2026-09-17_cycle3-runtime-strengthening-phase-a-orientation.md`.
- **Cycle-2 D/E closure record:** `working-memory/2026-09-16_cycle2-phase-d-integrated-learning-plan.md`.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Selected bounded implementation plan:** `plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`.
- **Accepted architecture owner:** `docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.

## Closed foundations retained

Do not reopen without concrete contradiction/regression evidence:

- exact run/job attempt coherence and existing static↔runtime step correlation boundary;
- exact-revision dependency source provenance;
- ADR-0009 parser-backed static workflow-command architecture;
- Cycle 1 shell resolution + parser-neutral command-analysis foundation;
- Cycle 2 one-analysis consumer migration, canonical command identity, parser-neutral consumer handoff, and bounded static ordering;
- Cycle 2 hosted executable proof.

Accepted architecture remains:

```text
GitHub Actions RunStepDefinition
+ effective shell context
        ↓
Tree-sitter shell-family parser
        ↓
UpgradePilot-owned static command IR
        ↓
static dependency/project/invocation observers
        ↓
separate conservative runtime-strengthening policy
```

Persistent principles:

- parse broadly, claim narrowly;
- syntax family and execution profile are distinct;
- Tree-sitter nodes remain private implementation machinery;
- static occurrence does not prove execution or success;
- parser uncertainty stays conservative with no regex/text fallback for positive evidence;
- command identity/source order does not imply runtime execution order;
- unresolved step-level evidence does not automatically earn exact inner-command identity;
- bounded increments must remain faithful to the real product responsibility; “small” is not authority to reduce useful coverage merely because a smaller implementation is easier to prove;
- plans and working memories are important coordination/evidence artifacts, but new evidence or stronger engineering reasoning may justify revising the route through the proper owner instead of following an older plan mechanically;
- when Ali has not yet learned concepts needed for a consequential decision, the AI must first establish the minimum decision-relevant model and explain what a proposed narrowing gains, loses, defers, and would require to expand later.

## Cycle 1 — CLOSED

Cycle 1 established:

```text
EffectiveShellContext
StaticCommandAnalysis
StaticCommandOccurrence
StaticCommandAtom
CommandSourceSpan
structural context
```

Admitted first shell families:

```text
Bash / sh
PowerShell / pwsh
Windows CMD / batch
```

Cycle 3 may trust these producer facts; it must not reopen parser grammar internals without concrete evidence.

## Cycle 2 — CLOSED

### A/B/C

Cycle 2 established the final normal static consumer shape:

```text
one WorkflowDefinition
→ one CI job/step traversal
→ analyze each RunStepDefinition once
→ same StaticCommandAnalysis reused by:
     direct requirements
     project environment
     package invocation
→ canonical StaticCommandLocation + structural_context
→ bounded ordered_after | not_after | unresolved static composition
```

Ownership:

```text
GitHub/provider
→ shell context + syntax parsing + parser-neutral command IR/identity

dependency
→ pip requirements meaning + local project/extras/groups/uv selection
  + project membership / uv reachability

CI
→ workflow traversal + checkout provenance + changed-package invocation
  + cross-evidence composition + static ordering
```

Hosted authoritative proof closed Phase B with:

```text
fresh Python 3.12.14 environment               PASS
pip install .                                  PASS
python -m pip check                            PASS
installed CLI checks                           PASS
focused investigation composition              PASS — 15/15
full deterministic product regression          PASS — 587/587
```

### D/E closure

Cycle-2 Phase D was intentionally stopped after sufficient practical ownership for continuation. D1 was completed; D2–D7 remaining deep-dive exercises were explicitly reclassified as deferred rather than falsely marked complete.

What was established strongly enough to continue:

- Cycle-1 producer → Cycle-2 consumer architecture;
- shared analysis and provider/dependency/CI ownership boundaries;
- canonical source identity versus runtime identity;
- removal of fabricated/overloaded ordinal semantics;
- proposition-relative `observed` / `not_established` / `unresolved` reasoning;
- sound lower-level evidence may coexist with stronger unresolved composition;
- real S001 Pydantic/soupsieve and S011 Dictare/optional-extra evidence paths;
- single-traversal/source-in composition rationale;
- static evidence is not execution/success evidence;
- main hosted-proof migration lessons.

No concrete product/design defect or must-repair prerequisite gap was discovered during D. Therefore Cycle-2 Phase E completed with no repair increment.

Deferred D learning should be reopened only if Cycle 3 exposes a concrete prerequisite gap or Ali explicitly chooses deeper review.

## Cycle 3 — Phase A ACTIVE

Cycle 3 owns this new proposition:

```text
static command occurrence
+ structural/control-flow context
+ effective execution profile
+ exact correlated runtime step evidence
→ bounded runtime-strengthening eligibility for that specific occurrence
```

ADR-0009 requires that successful step evidence must **not** generally imply that every internal parsed command executed or succeeded.

### Current source pressure

Current `src/upgradepilot/ci/dependency_exercise.py` still reduces supported static evidence to step-level locations:

```text
(job_key, step_source_index)
```

through `_supported_consumption_locations(...)` and `_supported_direct_exercise_locations(...)`.

`_classify_runtime_step_execution(...)` then:

1. finds the correlated runtime step;
2. checks that the static owner is a run step;
3. rejects visible/dynamic `continue-on-error` masking;
4. treats `completed/success` runtime step status as supported runtime evidence.

The missing Cycle-3 input is the **specific command occurrence's structural context and effective execution profile**.

Representative pressure:

```yaml
- run: |
    if false; then
        pip install -r requirements-dev.txt
    fi
    echo done
```

The parser may correctly establish the static `pip install` occurrence and Cycle 2 may preserve that static declaration. A successful enclosing step must not by itself strengthen that conditional occurrence to executed/succeeded consumption.

### Phase-A decisions so far

A1–A3 are decided in the active working memory:

```text
A1 — strengthen only the exact bounded runtime-correlated consumption/direct-exercise occurrence proposition;
     do not upgrade to installed-version, wheel, compatibility, full behavior, update-safety, or maintainer-action proof.

A2 — use explicit eligible | ineligible | unresolved runtime-strengthening eligibility states.

A3 — introduce one narrow CI-owned runtime-strengthening candidate/handoff for a specific static occurrence,
     referencing existing canonical facts rather than inventing a second command identity.
```

A3 preserves/references at least:

```text
outer workflow/job/step identity
+ canonical StaticCommandLocation
+ structural_context
+ effective execution_profile
+ minimum step-level analysis shape required by A4
+ static proposition being strengthened
```

Runtime correlation remains identity-only; it does not absorb internal command semantics.

### A4 current design direction and reassessment

The controlling implementation plan provides a conservative starting direction:

```text
cleanly parsed straightforward top-level occurrence
+ established syntax family
+ established execution profile
+ exact correlated completed/success runtime step
+ no continue-on-error masking
→ candidate for bounded runtime strengthening
```

The earlier idea of requiring the **entire run block to contain exactly one command** is **not accepted** as the A4 rule. It is only a useful baseline case. A4 must instead determine the smallest **product-faithful proven family**.

A4 investigation then exposed a material proof-boundary issue: GitHub step success plus static command structure and a nominal Bash execution profile do not, by themselves, prove that the parsed inner command executed/succeeded. Non-interactive Bash may execute `BASH_ENV` before the script body, and GitHub permits earlier steps to publish environment variables to later steps through `GITHUB_ENV`. Current workflow IR does not model the complete effective runtime environment, and visible YAML `env` parsing alone would not close mutations introduced by earlier run/action steps.

Therefore provisional P1/P2 shapes remain useful **structural candidates**, but are **not locked as exact execution/success proof**.

This activates the plan/ADR reassessment boundary rather than authorizing ad-hoc guards. Before A4 can close, Phase A must decide which proposition is both useful and supportable:

```text
R1 — strict exact inner-command execution/success
R2 — weaker occurrence-relative runtime association/support with explicit non-proof
R3 — narrowly sanitized execution class whose startup/runtime environment is independently bounded
```

The comparison must use the actual downstream CI-coverage proposition and Product Decision Model. Do not:

- broaden merely because a structure is theoretically analyzable;
- narrow merely because a one-command implementation is easiest;
- treat absence from current workflow IR as proof that startup/environment mutation is absent;
- add a visible-`BASH_ENV` check and call the runtime environment proven;
- absorb broad action/runtime-environment simulation or log-ledger acquisition without separate planning.

## Cycle 3 Phase-A questions

Decision state:

```text
A1 exact strengthened proposition     DECIDED
A2 eligibility state model            DECIDED
A3 canonical occurrence handoff       DECIDED
A4 first admitted positive family     ACTIVE / OPEN
A5 negative/unresolved structures     OPEN
A6 runtime-correlation composition     OPEN
A7 proof matrix                        OPEN
```

A4 must now settle:

1. whether Cycle 3 needs strict exact inner-command execution/success or a weaker but still decision-useful runtime-supported proposition;
2. whether a narrowly sanitized execution class is sufficiently useful to justify modeling it;
3. only after that proposition is fixed, what structural relations and execution profiles can positively support it;
4. which profile/structure/environment combinations remain ineligible or unresolved;
5. what capability/common-case coverage would be lost by any narrowing, and whether that loss is acceptable for the product trajectory.

## Immediate next action

Continue Cycle 3 Phase A with the A4 reassessment from actual downstream semantics:

```text
dependency_exercise.py
+ Product Decision Model
→ what the runtime-consumption/direct-exercise states actually claim and need

compare R1 / R2 / R3
→ strict execution proof
→ weaker runtime-supported occurrence
→ sanitized execution class

then
→ select the strongest useful proposition the available evidence can honestly support
→ reconcile A1/A4 and the selected implementation plan if the proposition changes
→ only then finish A5/A6/A7 and authorize implementation
```

## Current stop line

Until Cycle 3 Phase A is accepted:

- do not modify runtime-strengthening product source/tests;
- do not treat successful run-step correlation as universal command execution proof;
- do not introduce a general shell CFG/execution simulator;
- do not add arbitrary GitHub expression evaluation, matrix expansion, reusable-workflow execution, or log parsing;
- do not broaden package-wrapper/pip/uv semantics as part of this cycle;
- do not absorb exact installed-version/wheel evidence, compatibility claims, Target redesign, or maintainer-action enablement;
- do not reopen deferred Cycle-2 learning unless a concrete Cycle-3 dependency requires it.

After all three command-analysis cycles close, re-audit the parent synthesis evidence path and select the next decision-critical bottleneck rather than broadening automatically.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`