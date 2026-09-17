# UpgradePilot Current Memory

**Last updated:** 2026-09-17  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** execute Cycle 2 **Phase D**, currently **D2 — canonical command identity + bounded static ordering**, as an integrated post-implementation learning / engineering-ownership check over the stable, proven parser-backed static workflow-command consumer architecture.
- **Mode:** **Learning-Only for Phase D** — product/source/test mutation is paused while learning is the selected responsibility. If learning exposes a real defect, record it and explicitly transition later to Audit/Planning/Build before mutation.
- **Cycle state:** **Cycle 1 CLOSED; Cycle 2 A COMPLETE; B CLOSED + hosted proof green; C COMPLETE through progressive preservation; D ACTIVE with D1 DONE / D2 ACTIVE; E PENDING; Cycle 3 NOT STARTED**.
- **Selected Phase-D working memory / checklist:** `working-memory/2026-09-16_cycle2-phase-d-integrated-learning-plan.md`.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Selected bounded implementation plan:** `plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`.
- **Accepted method owner:** `docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`.
- **Phase A decision memory:** `working-memory/2026-09-14_static-command-consumer-migration-and-identity.md`.
- **Phase B engineering history:** `working-memory/2026-09-15_cycle2-static-consumer-build.md`.
- **Phase B hosted proof closure:** `working-memory/2026-09-16_cycle2-phase-b-hosted-proof-closure.md`.
- **Hosted proof-repair records:** `working-memory/2026-09-16_phase-b-hosted-proof-repair.md` and `working-memory/2026-09-16_phase-b-hosted-proof-repair-3.md`.
- **Closed Cycle 1 working memory:** `working-memory/2026-09-13_static-workflow-command-three-cycle-implementation.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.

## Closed foundations retained

Do not reopen these without concrete contradictory/regression evidence:

- exact run/job attempt coherence;
- bounded static↔runtime correlation within its previously admitted identity boundary;
- exact-revision requirements/constraints provenance;
- ADR-0009 static workflow-command architecture/design;
- **Cycle 1 parser/shell/command-analysis foundation**;
- **Cycle 2 Phase A migration design contract**;
- **Cycle 2 Phase B static evidence consumer migration + command-identity correction**;
- **Cycle 2 Phase B hosted executable proof**.

## Accepted workflow-command architecture

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

First admitted shell families:

```text
Bash / sh
PowerShell / pwsh
Windows CMD / batch
```

Persistent principles:

- parse broadly, claim narrowly;
- syntax family and execution profile are distinct;
- Tree-sitter nodes remain private implementation machinery;
- static occurrence does not prove command execution or success;
- parser uncertainty remains conservative with no regex/text-splitter fallback for positive evidence;
- Python/custom interpreters remain separate language responsibilities.

## Cycle 1 — CLOSED

Cycle 1 established provider-owned shell resolution and parser-neutral static command analysis:

```text
EffectiveShellContext
StaticCommandAnalysis
StaticCommandOccurrence
StaticCommandAtom
CommandSourceSpan
structural context
```

Bounded proof:

```text
parser characterization RESULT=PASS
python -m pip check → PASS
34 focused + nearest-provider tests → PASS
```

Cycle 2 may trust that producer/foundation; Phase D does not need to relearn Tree-sitter grammar internals at high depth.

## Cycle 2 — A/B/C complete, D active

### Phase A — COMPLETE

Accepted A1–A6 contract:

```text
A1  one parsed WorkflowDefinition / one normal CI workflow traversal /
    analyze each RunStepDefinition exactly once

A2  outer identity = workflow path + revision + job key + step_source_index
    inner identity = StaticCommandLocation(source_span, source_order)

A3  segment_index overload removed from final migrated contracts;
    identity, ordering, and placeholder/unresolved responsibilities are separated

A4  dependency observers consume StaticCommandAnalysis / typed atoms;
    shell parsing remains provider-owned

A5  CI package invocation is recognized from real parsed command occurrences

A6  same-step composition uses
    ordered_after | not_after | unresolved
    with parser-neutral structural context
```

### Phase B — CLOSED / PROVEN

Final normal static consumer shape:

```text
one WorkflowDefinition
        ↓
one CI workflow traversal
        ↓
for each RunStepDefinition:
    analyze_run_step_commands(...) once
        ↓
    same StaticCommandAnalysis reused by:
      direct requirements
      project environment
      package invocation
        ↓
    canonical StaticCommandLocation + structural_context
        ↓
    bounded CI static ordering
```

Ownership:

```text
GitHub/provider
→ shell context + syntax parsing + parser-neutral command IR/identity

dependency
→ pip requirements meaning + local project/extras/groups/uv selection
  + project membership / uv reachability

CI
→ one workflow traversal + checkout provenance + changed-package invocation
  + cross-evidence composition + static ordering
```

No migrated consumer reconstructs shell command identity with textual splitting as a positive fallback.

Hosted authoritative proof:

```text
workflow: Product verification
run id: 35108271298
run attempt: 1
tested revision: ee93143b58c3cf0dbb191c543ef4a66a437d0aec
result: SUCCESS

fresh Python 3.12.14 environment               PASS
pip install .                                  PASS
python -m pip check                            PASS
installed CLI checks                           PASS
focused investigation composition              PASS — 15/15
full deterministic product regression          PASS — 587/587
```

Everything committed after that tested SHA before Phase-D activation is documentation/working-memory only; product source remained the tested implementation.

Important proof-driven lessons retained for Phase D:

- strict internal evidence-contract migration must include secondary downstream consumers;
- removing obsolete identity fields can leave stale fixtures/clients;
- uncertainty may move to an earlier trustworthy owner without changing the final conservative proposition;
- step-scoped unresolved evidence does not imply exact inner-command identity;
- single-traversal composition prevents detached evidence identity from being guessed/rebound later;
- proof failures must be classified before repair rather than weakening contracts reflexively.

### Phase C — COMPLETE through progressive preservation

Cycle-2 state/history was preserved progressively rather than postponed into one later documentation step:

```text
Phase A decisions
+ B1–B5 engineering progression
+ failures / surprises / repairs
+ executable proof debt and final proof
+ live continuation
→ preserved in working-memory + MEMORY.md
```

No separate replay of C is needed. Phase D maintains its own active working memory progressively.

## Phase D — ACTIVE

Canonical Phase-D owner/checklist:

`working-memory/2026-09-16_cycle2-phase-d-integrated-learning-plan.md`

Primary purpose:

- integrate Phase-A design rationale with the final Phase-B implementation and proof history;
- reach proportionate engineering ownership without source memorization;
- cover important source/tests and real cases without turning D into a full parser/pip/uv course;
- discover and record any real learning gap before Cycle 3.

Selected learning blocks:

```text
D1  Cycle-2 problem + A1–A6 design reconstruction                 DONE
D2  canonical command identity + bounded static ordering          ACTIVE
D3  parser-neutral facts → dependency/CI domain semantics         PENDING
D4  one-analysis production handoff + project-environment composition
D5  S001-style uv + S011-style pyproject real cases
D6  static presence / direct exercise / runtime proof boundary
D7  hosted-proof failures + final ownership synthesis
```

D1 completion evidence: practical ownership was demonstrated through real-shaped workflow examples. Ali correctly reasoned about the Cycle-1 producer / Cycle-2 consumer split, shared analysis, canonical source identity, removal of fabricated ordinals, domain ownership, and the distinction between sound lower-level observations and stronger unresolved composition under conditional/short-circuit structure. Static evidence was not confused with runtime execution or success.

The Phase-D record owns status updates, newly discovered learning items, depth classification, and completion evidence.

### Immediate next action

Continue **D2** in Learning-Only mode using the final stable source and representative proof rather than repeating D1 theory:

```text
StaticCommandOccurrence
→ StaticCommandLocation(source_span, source_order)
→ StaticDependencyConsumptionEvidence / DirectPackageInvocationEvidence
→ relate_invocation_after_consumption(...)
```

Focus on the missing implementation/proof ownership: where canonical identity is created and carried, how missing same-step identity fails closed, and how final ordering combines step order, source order, and path-dependent structure. Concepts already demonstrated during D1 should be recalled briefly, not retaught from zero.

## Phase E — PENDING

After D:

- repair only demonstrated must-own learning/prerequisite gaps;
- if D exposes a real product/design defect, select Audit/Planning/Build explicitly before mutation;
- reconcile the Phase-D working memory and `MEMORY.md`;
- orient Cycle 3 A only after Cycle-2 ownership is sufficient.

## Cycle 3 — PLANNED / NOT STARTED

Planned responsibility:

```text
static command occurrence
+ structural/control-flow context
+ effective execution profile
+ exact correlated runtime step evidence
→ bounded runtime-strengthening eligibility
```

Cycle 3 must not begin while Phase D/E remain open.

## Current stop line

Until Cycle-2 Phase D/E close:

- do not start Cycle-3 runtime-strengthening implementation/design beyond boundary-level learning needed for D;
- do not treat static source order as execution proof;
- do not expose Tree-sitter nodes as dependency/CI contracts;
- do not broaden pip/uv/package-wrapper semantics merely because typed atoms exist;
- do not reintroduce textual splitters as positive-evidence fallback;
- do not absorb runtime logs/artifacts, matrix/reusable-workflow execution, exact installed-version/wheel evidence, Target redesign, or maintainer-action enablement;
- do not mutate product/source/tests during Learning-Only unless Ali explicitly changes the operation boundary.

After all three command-analysis cycles close, re-audit the parent synthesis evidence path and select the next decision-critical bottleneck rather than broadening automatically.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
