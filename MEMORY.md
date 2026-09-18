# UpgradePilot Current Memory

**Last updated:** 2026-09-18  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** Cycle 3 Phase B **Build Stage 1 — Provider Structural Admission review/learning closure**.
- **Mode:** Build/Implement + Learning-by-Doing. Stage-1 implementation and hosted focused proof are complete. Finish Stage-1 review/teaching before entering Stage 2.
- **Cycle state:** **Cycle 1 CLOSED; Cycle 2 CLOSED; Cycle 3 Phase A COMPLETE; Cycle 3 Phase B Stage 1 IMPLEMENTED / HOSTED PROOF PASS / REVIEW ACTIVE**.
- **Selected Cycle-3 working memory:** `working-memory/2026-09-18_cycle3-runtime-strengthening-build.md`.
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

## Cycle 3 — Phase A COMPLETE / Build Ready

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

the first three Cycle-3 design responsibilities are decided in the active working memory:

```text
Exact Runtime-Strengthened Proposition Boundary — strengthen only the exact bounded runtime-correlated consumption/direct-exercise occurrence proposition;
     do not upgrade to installed-version, wheel, compatibility, full behavior, update-safety, or maintainer-action proof.

Runtime-Strengthening Eligibility State Model — use explicit eligible | ineligible | unresolved runtime-strengthening eligibility states.

Canonical Static-Occurrence Handoff Contract — introduce one narrow CI-owned runtime-strengthening candidate/handoff for a specific static occurrence,
     referencing existing canonical facts rather than inventing a second command identity.
```

Canonical Static-Occurrence Handoff Contract preserves/references at least:

```text
outer workflow/job/step identity
+ canonical StaticCommandLocation
+ structural_context
+ effective execution_profile
+ minimum step-level analysis shape required by Positive Structural Admission Policy
+ static proposition being strengthened
```

Runtime correlation remains identity-only; it does not absorb internal command semantics.

### Runtime-Correlated Support Proposition — selected

Cycle 3 has selected **Runtime-Correlated Support Proposition** as the exact strengthened proposition.

```text
exact supported static occurrence
+ eligible structural context
+ established execution profile
+ exact correlated completed/successful owning runtime step
+ no visible continue-on-error masking
→ supported runtime-correlated occurrence
```

This is stronger evidence than static declaration alone, but it is **not direct observation or
proof that the inner command definitely executed/succeeded**.

Explicit non-claims remain:

```text
not exact command-execution proof
not exact command-success proof
not exact installed dependency version
not wheel/sdist identity
not compatibility / complete behavior
not update safety
not maintainer-action permission
```

Runtime-Correlated Support Proposition was selected because:

- **Strict Inner-Command Execution/Success Proof Route strict execution/success** requires a stronger runtime-observability responsibility than
  the current step-level correlation path can honestly provide; shell startup/environment
  effects such as `BASH_ENV` demonstrate the gap.
- **Sanitized Execution-Environment Route sanitized execution class** would require materially broader environment/action modeling
  while excluding many ordinary workflows, without a current downstream need that justifies
  that cost.
- **Runtime-Correlated Support Proposition matches current product semantics**: the parent synthesis plan already treats
  `supported_runtime_correlated` as supported static consumption/exercise safely related to
  an exact successful runtime step, while withholding stronger runtime/artifact/compatibility
  claims.

No redesign of the Exact Runtime-Strengthened Proposition Boundary is required; the Runtime-Correlated Support Proposition clarifies the meaning of the already-selected
runtime-correlated occurrence proposition.

At that point, the Positive Structural Admission Policy remained **partially open only for the eligibility family**: exactly which structures and
execution profiles may receive Runtime-Correlated Support Proposition strengthening. Straightforward/mandatory-looking shapes
remain positive candidates; conditional/path-dependent structures must not inherit successful
step evidence automatically. The one-command-only rule is not accepted as the permanent
product boundary.

## Cycle 3 Phase-A questions

Decision state:

```text
Exact Runtime-Strengthened Proposition Boundary
→ DECIDED

Runtime-Strengthening Eligibility State Model
→ DECIDED

Canonical Static-Occurrence Handoff Contract
→ DECIDED

Runtime-Correlated Support Proposition
→ DECIDED

Positive Structural Admission Family
→ DECIDED
→ Sole Ordinary Top-Level Command Admission
→ First Sequential Bash/sh Command Admission

Negative and Unresolved Structural Classification
→ DECIDED

Runtime-Correlation and Eligibility Composition
→ DECIDED

Runtime-Strengthening Proof Matrix
→ DECIDED
```

### Accepted Positive Structural Admission and Negative/Unresolved Classification boundary

Runtime-strengthening admission now follows a **positive Tree-sitter-backed structural rule**:

```text
Tree-sitter shell-family CST
→ provider-owned parser adapter
→ small UpgradePilot-owned whole-step/position fact
→ CI runtime-strengthening eligibility
```

Tree-sitter nodes remain private. The product does not expose grammar-specific CST types or
build a general shell interpreter/CFG.

Do not treat these as sufficient positive proof by themselves:

```text
straightforward_top_level fallback
source_order == 0
one collected command occurrence
absence of a currently-known negative tag
```

The first accepted positive family is:

```text
Sole Ordinary Top-Level Command Admission — sole ordinary top-level command
→ admitted built-in/default Bash/sh, PowerShell/pwsh, or CMD profile
→ eligible structural/profile candidate for Runtime-Correlated Support Proposition

First Sequential Bash/sh Command Admission — first ordinary top-level Bash/sh command in a sequential script
→ admitted built-in/default Bash/sh fail-fast profile
→ outside conditional/status-inverting/nested/asynchronous structure
→ eligible structural/profile candidate for Runtime-Correlated Support Proposition
```

First Sequential Bash/sh Command Admission intentionally retains S002's real first-install multi-command case.

Accepted classification principle:

```text
ineligible
→ known structure positively permits successful step completion without meaningful support
  for the exact target occurrence

unresolved
→ current structural/profile representation is too coarse to justify a positive or stronger
  negative conclusion
```

Known ineligible examples include conditional/loop/deferred-function bodies, status inversion,
background/asynchronous execution, process substitution, and a positively identified `||`
rescue position.

Current unresolved examples include generic `short_circuit` (`&&`/`||` collapsed),
generic pipelines, generic nested/subshell structures, compound blocks, later generic linear
commands, complex unrecognized PowerShell/CMD structure, custom shell templates, and
parser/profile ambiguity.

The provider adapter may now use the existing Tree-sitter tree more fully where Cycle 3 needs
it, including preventing false-straightforward admission for Bash `! command`, `command &`,
process substitution/compound nesting, PowerShell flow-control/script-block structures, and
CMD goto/exit/parenthesized structures.

S004-style `. ./venv/bin/activate && pip install ...` remains explicitly deferred rather
than rejected. Re-entry requires a bounded operator/position/status-contribution relation and
shell-specific characterization.

### Accepted Runtime-Correlation and Eligibility Composition

The runtime-strengthening flow now preserves the exact static occurrence until the stronger
runtime proposition is classified.

```text
supported exact static occurrence
+ StaticCommandLocation
+ occurrence eligibility
+ exact owning runtime-step correlation
+ continue-on-error interpretation
+ factual GitHub runtime status/conclusion
→ occurrence runtime-strengthening result
```

Accepted semantics:

```text
eligible + exact completed/successful unmasked runtime step
→ runtime strengthening supported

ineligible
→ runtime strengthening not_established

eligible + exact failed/skipped/cancelled/non-successful runtime step
→ runtime strengthening not_established
→ preserve/report exact observed runtime status/conclusion

eligibility/correlation materially unresolved
→ runtime strengthening unresolved

continue-on-error true/dynamic or equivalent masking ambiguity
→ runtime strengthening unresolved
```

A known GitHub runtime outcome is never called unresolved merely because the broader coverage
interpretation remains unresolved.

Multiple exact occurrences are aggregated existentially: any supported candidate establishes
the runtime axis; otherwise materially unresolved candidates preserve unresolved; otherwise
the runtime axis is not established.

The weaker static-support state remains valid when stronger runtime support is merely
unavailable or structurally inadmissible:

```text
static support earned
+ stronger occurrence/runtime bridge not earned
→ preserve supported_not_correlated where appropriate
```

But an exact eligible occurrence with a known non-successful runtime step remains materially
visible at the broader CI-coverage layer; the aggregate may remain unresolved because
successful dependency coverage was not established, not because the factual step result is
unknown.

Runtime correlation remains identity-only and does not absorb Tree-sitter/shell semantics.
Direct-exercise runtime support uses the same exact-occurrence composition independently.

### Runtime-Strengthening Proof Matrix and Phase-A closure

The final Phase-A review found no architecture, product-semantic, ownership, or proof blocker
to Build entry.

The accepted proof responsibility covers:

```text
provider positive structural admission
+ false-straightforward prevention
+ eligibility classification
+ exact-occurrence runtime composition
+ multiple-occurrence identity preservation
+ separate direct-exercise runtime composition
+ S001/S002 admitted useful positives
+ S004 explicit deferred/re-entry pressure
+ stronger-claim limits
+ focused → nearby → full deterministic proof
```

The plan was reconciled so the runtime evidence states remain precise:

```text
positively ineligible structure
→ runtime strengthening not_established

materially insufficient structural/profile facts
→ runtime strengthening unresolved

eligible exact occurrence + known failed/skipped/cancelled runtime step
→ factual runtime status remains known
→ positive runtime strengthening not_established
→ broader CI coverage may remain unresolved
```

Cycle 3 Phase A is complete. No product source/tests were modified during Phase A.

## Immediate next action

Finish **Cycle 3 Phase B — Build Stage 1 review/learning closure**:

```text
hosted focused provider proof = PASS
18/18 tests on Python 3.12.14
→ explain/review the Stage-1 provider model with Ali
→ repair any important conceptual or implementation gap if exposed
→ record Stage-1 closure
→ only then enter Stage 2 — Exact Occurrence Handoff and Eligibility
```

Hosted proof details are recorded in
`working-memory/2026-09-18_cycle3-runtime-strengthening-build.md`.

Do not start Stage 2 before the Stage-1 learning/review gate is closed.

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