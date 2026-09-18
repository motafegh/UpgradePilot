# Cycle 3 Phase B — Runtime-Strengthening Build Working Memory

**Date:** 2026-09-18  
**Status:** ACTIVE  
**Primary operation:** Build / Implement  
**Method:** Learning-by-Doing  
**Selected plan:** [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)  
**Architecture owner:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)  
**Phase-A design record:** [`2026-09-17_cycle3-runtime-strengthening-phase-a-orientation.md`](2026-09-17_cycle3-runtime-strengthening-phase-a-orientation.md)

## Responsibility

Implement the accepted Cycle-3 runtime-strengthening contract without reopening closed Phase-A
semantics unless executable evidence exposes a concrete contradiction.

The build must preserve this boundary:

```text
static command occurrence
+ provider-owned positive whole-step/position fact
+ effective execution profile
+ exact runtime step correlation
+ runtime status / continue-on-error interpretation
→ bounded Runtime-Correlated Support for the exact occurrence
```

It still does not prove exact inner-command execution/success, exact installed version,
artifact choice, compatibility, update safety, or maintainer action.

## Phase-B build roadmap

Phase B is one bounded implementation responsibility executed as three coherent build stages,
followed by final proof/closure.

### Build Stage 1 — Provider Structural Admission

Goal:

```text
existing Tree-sitter CST
→ bounded parser-neutral positive whole-step/position facts
→ known false-straightforward structures cannot enter the positive family
```

Scope:

- implement provider-owned positive facts for:
  - Sole Ordinary Top-Level Command Admission;
  - First Sequential Bash/sh Command Admission;
- use the whole parsed script, not `source_order == 0`, as the admission basis;
- prevent false positive admission for the Phase-A identified structures, including Bash
  status inversion, background/asynchronous execution, process substitution, compound
  structure, and relevant PowerShell/CMD non-command control-flow pressure;
- keep Tree-sitter nodes private;
- do not change CI runtime-strengthening behavior yet;
- add/adjust focused provider proofs only.

Stop line:

- no occurrence-level CI handoff yet;
- no runtime aggregation changes;
- no general shell CFG/interpreter;
- no S004 `&&` positive support.

Learning/recording rhythm:

```text
A — orient the provider structural responsibility
B — implement the bounded provider facts + focused tests
C — progressively record implementation/proof/limitations here
D — explain/teach what was actually built and why
E — repair any important understanding/implementation gap and orient Stage 2
```

Current state:

```text
A orientation                  COMPLETE
B implementation               COMPLETE
C state preservation            COMPLETE
D post-build learning           COMPLETE
E gap repair / next orientation COMPLETE
```

### Build Stage 1 — orientation / implementation model

Stage 1 is provider-only. It will add one **positive whole-step relationship fact** to each
parsed command occurrence without deciding CI eligibility yet.

The implementation model is:

```text
whole Tree-sitter CST
+ exact command node
        ↓
provider-owned positive relation
        ↓
sole_ordinary_top_level_command
OR
first_ordinary_top_level_command_in_sequential_script
OR
no positive relation established
```

The third state is intentionally represented by absence of the positive relation, not by a
provider-owned `ineligible` verdict. Stage 2 remains responsible for combining this provider
fact with structural context and execution profile into:

```text
eligible | ineligible | unresolved
```

This separation prevents the parser adapter from owning CI policy.

#### Grammar characterization used for Stage 1

The pinned Bash grammar confirms:

- root `program` contains shell statements;
- `negated_command`, `compound_statement`, `list`, and `pipeline` are distinct
  statements from ordinary `command`;
- process substitution is a named expression that can contain statements;
- Bash statement terminators include `;`, newline, and `&`.

The pinned PowerShell grammar confirms:

- root `program` contains a `statement_list`;
- top-level statements include `pipeline`, `flow_control_statement`, conditionals,
  loops, functions, try/trap, and other non-command statements;
- therefore one collected `command` occurrence is not sufficient proof of a sole
  top-level command.

Stage-1 implementation consequence:

- positive admission must inspect the whole root/top-level statement shape;
- `source_order == 0` is never the admission rule;
- Bash background `&` must be rejected explicitly because it is an anonymous terminator;
- nested/compound/control-flow commands must not receive a positive whole-step relation.

#### Stage-1 source shape selected

Add a small parser-neutral provider fact to `StaticCommandOccurrence`:

```text
whole_step_relation:
    sole_ordinary_top_level_command
    | first_ordinary_top_level_command_in_sequential_script
    | None
```

`None` means only:

> the provider did not positively establish one of the two admitted whole-step relations.

It does not mean the occurrence is ineligible. Stage 2 will decide whether the missing
positive relation is a known negative or an unresolved structure.

No Tree-sitter node escapes the provider layer.

### Build Stage 1 — implementation checkpoint

Stage-1 provider implementation is complete at the selected source boundary.

Changed product/test owners:

```text
src/upgradepilot/github/workflow_command_analysis.py
tests/test_github_workflow_command_analysis.py
```

No CI runtime-composition module was changed.

#### Implemented provider fact

`StaticCommandOccurrence` now carries:

```text
whole_step_relation:
    sole_ordinary_top_level_command
    | first_ordinary_top_level_command_in_sequential_script
    | None
```

This fact is provider-owned and parser-neutral.

It is intentionally separate from `structural_context`:

```text
structural_context
→ what relevant syntax/control structure surrounds this occurrence

whole_step_relation
→ one positively established relationship between this exact occurrence and the whole run script
```

Neither field is a runtime-strengthening eligibility verdict.

#### Whole-tree positive admission implemented

Bash:

- sole positive requires the exact command to be the only significant top-level statement;
- first-sequential positive requires the exact command to be the first top-level statement
  and every significant top-level statement to be an ordinary command;
- a top-level Bash background `&` terminator prevents either positive relationship.

PowerShell:

- sole positive requires exactly one collected command in the full script;
- the program must contain one top-level statement list with one pipeline statement;
- the exact command must reach that top-level pipeline only through admitted pipeline wrappers;
- a command nested under subexpressions/script blocks/control flow therefore cannot become
  a false sole top-level positive.

CMD:

- sole positive requires the exact `cmd` node to be the only significant top-level program
  statement;
- preceding `exit`/`goto`/other non-`cmd` statements therefore prevent false admission.

#### New structural distinctions retained for Stage 2

Bash command structural context now explicitly preserves:

```text
status_inverted
asynchronous
process_substitution
```

These were added because Phase A classified them as meaningful known-negative pressure for
runtime strengthening.

They do not themselves change runtime evidence in Stage 1.

#### Focused proof added

Existing cross-shell simple-command proof now also requires:

```text
simple Bash / PowerShell / CMD command
→ sole_ordinary_top_level_command
```

New focused cases cover:

```text
S002-shaped two-command Bash script
→ first command gets first-sequential positive
→ second command gets no positive relation

! command
command &
process substitution
compound Bash block
→ target does not receive positive whole-step relation

PowerShell exit before target
CMD exit before target
→ target does not receive false sole-command admission
```

#### Commits

```text
430fc0fab940ac38a4b202275e6bf275bca6d10e
→ add provider whole-step command relations

b61a502eba162cd02a9eeed84623ab9dc4ef9462
→ keep ordered command nodes immutable

893fac1844a88eb6f94d64c5aab97f4482139f09
→ prove provider whole-step command relations

703ef1cea9e36fa1bf629c48f6529c6b07491fc8
→ tighten top-level PowerShell command admission
```

#### Stage-1 proof status

Repository/diff inspection confirms the change is bounded to the provider + focused provider
proof, plus Phase-B state artifacts.

Executable proof is **PASS** through GitHub Actions.

Because the existing product-verification workflow is manual-dispatch only and the connected
GitHub tool surface does not expose `workflow_dispatch`, a temporary proof branch was created
from the exact current `main` revision and given a branch-triggered focused workflow.

Proof vehicle:

```text
branch:
agent/cycle3-stage1-provider-proof

workflow:
.github/workflows/cycle3-stage1-provider-proof.yml

proof commit:
42848185c5c6eeafc38c5c12efc5979f64fc8d53

GitHub Actions run:
35378727316

job:
Focused workflow command analysis proof
```

Hosted environment established:

```text
CPython 3.12.14

tree-sitter          0.25.0
tree-sitter-bash     0.25.1
tree-sitter-pwsh     0.38.1
tree-sitter-batch    0.11.1
```

Executed:

```text
python -m pip install .
python -m unittest tests.test_github_workflow_command_analysis -v
```

Observed result:

```text
Ran 18 tests in 0.028s
OK
GitHub Actions job conclusion: success
```

All new Stage-1 provider proofs passed, including:

- cross-shell sole top-level command admission;
- first sequential Bash command admission;
- Bash status inversion/background/process-substitution rejection;
- compound Bash non-admission;
- PowerShell/CMD earlier-control-flow false-sole prevention;
- retained conditional/pipeline/short-circuit/parser-error/source-identity regressions.

This closes the Stage-1 focused executable proof debt.

The temporary workflow is an execution/proof vehicle only; it is not part of the product
architecture and must not be merged to `main` as product behavior.

#### Stage-1 status

```text
A orientation                  COMPLETE
B implementation               COMPLETE
C state preservation            COMPLETE
D post-build learning           ACTIVE — current handoff
E gap repair / next orientation BLOCKED on focused executable proof + review
```

### Build Stage 1 — CLOSED

Stage 1 is complete.

Ali reviewed and understood the key provider model:

```text
source_order
!= whole-script execution relationship

structural_context
→ surrounding syntax/control-flow fact

whole_step_relation
→ positively established relationship between exact occurrence and whole run script

whole_step_relation = None
→ no admitted positive provider relation established
→ NOT an eligibility verdict
```

The provider therefore stops at parser-neutral structural facts. CI policy remains responsible
for interpreting those facts together with execution profile.

Stage-1 closure evidence:

```text
implementation complete
focused provider tests added
GitHub Actions hosted proof PASS — 18/18
conceptual/logical review complete
no Stage-2 behavior implemented during Stage 1
```

No material gap was exposed by the review.

### Build Stage 2 — Exact Occurrence Handoff and Eligibility

**Status:** ACTIVE

Goal:

```text
exact StaticCommandLocation
+ provider structural admission
+ execution profile
+ static proposition kind
→ exact runtime-strengthening candidate
→ eligible | ineligible | unresolved
```

Scope:

- preserve exact occurrence identity/context through the existing one-analysis traversal;
- do not invent a second command identity;
- classify eligibility from accepted provider facts + structural/profile facts;
- prove multiple occurrences in one step do not collapse into one strengthening candidate;
- keep `workflow_runtime_correlation.py` identity-only;
- stop before changing final workflow runtime aggregation.

Stage 1 is now reviewed, recorded, taught, and closed. Stage 2 is formally active.

Stage-2 Learning-by-Doing state:

```text
A orientation                  ACTIVE
B implementation               NOT STARTED
C state preservation            ACTIVE
D post-build learning           NOT STARTED
E gap repair / next orientation NOT STARTED
```

### Build Stage 2 — orientation / implementation model

The source trace confirmed the exact Stage-2 loss boundary:

```text
one StaticCommandAnalysis per run step
→ exact command occurrence is identified
→ static consumption / invocation evidence preserves:
     StaticCommandLocation
     structural_context
BUT previously dropped:
     whole_step_relation
     execution_profile
→ dependency_exercise later reduced supported evidence to (job_key, step_source_index)
```

Stage 2 therefore preserves the missing provider facts in existing static evidence records
before any runtime aggregation.

#### Selected handoff shape

Normal production static consumption and invocation evidence now preserve/reference:

```text
workflow path/revision
job key
step source index
StaticCommandLocation
structural_context
whole_step_relation
execution_profile
proposition kind (when converted to runtime-strengthening candidate)
```

No Tree-sitter node is retained.

Precomposed/synthetic compatibility evidence may lack the new provider facts. Stage 2 must
classify that stronger runtime proposition as `unresolved`; it must not reparse or guess.

#### Eligibility ownership

A new CI-owned runtime-strengthening candidate/classifier will own:

```text
provider/static occurrence facts
+ execution profile
→ eligible | ineligible | unresolved
```

Provider parsing does not own this policy.

Accepted Stage-2 classification order:

```text
1. known positively disqualifying structure
   → ineligible

2. incomplete exact identity/context/profile
   → unresolved

3. Sole Ordinary Top-Level Command Admission
   + admitted built-in/default execution profile
   → eligible

4. First Sequential Bash/sh Command Admission
   + admitted GitHub Bash/sh fail-fast execution profile
   → eligible

5. anything else within the current coarse representation
   → unresolved
```

Known ineligible structures at this stage:

```text
conditional
loop
function definition/body
status_inverted
asynchronous
process_substitution
```

Generic `short_circuit`, `pipeline`, `nested_or_subshell`, compound/no-positive relation,
later generic linear commands, custom shell templates, and incomplete profile/identity remain
`unresolved`.

The current generic short-circuit representation does not distinguish `&&` from `||`, so
Stage 2 must not invent the Phase-A deferred operator-specific classification.

#### Implementation progress

Completed so far:

- project-environment declarations preserve `whole_step_relation`;
- static dependency-consumption evidence preserves `whole_step_relation` and
  `execution_profile`;
- direct invocation evidence preserves exact workflow identity, `whole_step_relation`, and
  `execution_profile`;
- normal workflow traversal populates these facts from the already-existing single
  `StaticCommandAnalysis`.

No runtime correlation or workflow aggregation behavior has changed.

Stage-2 state:

```text
A orientation                  COMPLETE
B implementation               ACTIVE
C state preservation            ACTIVE
D post-build learning           NOT STARTED
E gap repair / next orientation NOT STARTED
```

### Build Stage 2 — implementation checkpoint

Stage-2 implementation is complete at the selected boundary.

Changed product/test owners:

```text
src/upgradepilot/dependency/environment_selection.py
src/upgradepilot/ci/consumption.py
src/upgradepilot/ci/workflow_commands.py
src/upgradepilot/ci/runtime_strengthening.py
src/upgradepilot/ci/static_command_order.py

tests/test_ci_runtime_strengthening.py
tests/test_parser_backed_ci_command_evidence.py
tests/test_single_pass_workflow_static_evidence.py
tests/test_static_command_order.py
```

No runtime-step correlation or final workflow runtime aggregation logic was changed.

#### Exact occurrence handoff now preserved

Normal production static evidence now carries enough context for later runtime strengthening:

```text
workflow path/revision
job key
step source index
StaticCommandLocation
structural_context
whole_step_relation
execution_profile
```

Direct-exercise invocation evidence now also preserves workflow path/revision, which previously
were not part of the invocation record.

Project-environment selection declarations preserve `whole_step_relation`, and CI
consumption composition adds the already-resolved execution profile from the same
`StaticCommandAnalysis`.

No reparsing or shell re-resolution is introduced.

#### CI-owned runtime-strengthening candidate

A new focused module:

```text
src/upgradepilot/ci/runtime_strengthening.py
```

defines:

```text
RuntimeStrengtheningCandidate
RuntimeStrengtheningEligibility
eligible | ineligible | unresolved
```

and factories for:

```text
StaticDependencyConsumptionEvidence
→ dependency_consumption candidate

DirectPackageInvocationEvidence
→ direct_package_exercise candidate
```

The candidate preserves exact command occurrence identity. It does not correlate runtime
steps or inspect runtime status.

#### Eligibility behavior implemented

```text
known conditional / loop / function-body / status-inverted /
asynchronous / process-substitution structure
→ ineligible

missing exact workflow/job/command identity
→ unresolved

missing execution profile
→ unresolved

custom shell template
→ unresolved

sole ordinary top-level command
+ admitted built-in/default profile
→ eligible

first ordinary top-level sequential Bash/sh command
+ admitted Bash/sh fail-fast profile
→ eligible

other currently unmodeled/coarse structures
→ unresolved
```

Generic short-circuit remains unresolved because the current representation still collapses
`&&` and `||`.

#### Same-step identity preservation

Focused proof constructs two supported static occurrences in the same job/step with different
`StaticCommandLocation` values.

Expected/implemented result:

```text
same outer job/step
+ occurrence source_order 0
+ occurrence source_order 1
→ two distinct RuntimeStrengtheningCandidate objects
→ eligibility can differ independently
```

This directly protects against the current pre-Cycle-3 step-level collapse.

#### Static-order integration safeguard

Because Stage 1 introduced:

```text
status_inverted
asynchronous
process_substitution
```

the existing same-step static ordering rule now treats those structures as path-dependent.
This prevents the new provider facts from being ignored by the older ordering consumer.

#### Stage-2 focused proof set

Hosted proof should run:

```text
tests.test_github_workflow_command_analysis
tests.test_parser_backed_ci_command_evidence
tests.test_single_pass_workflow_static_evidence
tests.test_ci_runtime_strengthening
tests.test_static_command_order
tests.test_ci_static_direct_exercise_order
```

Stage-2 state before hosted proof:

```text
A orientation                  COMPLETE
B implementation               COMPLETE
C state preservation            COMPLETE
D post-build learning           NOT STARTED
E gap repair / next orientation BLOCKED on hosted focused proof
```

### Build Stage 2 — hosted proof PASS / review gate

Focused Stage-2 executable proof passed in GitHub Actions.

Proof vehicle:

```text
branch:
agent/cycle3-stage2-occurrence-proof

workflow:
.github/workflows/cycle3-stage2-occurrence-proof.yml

proof commit:
1bae4965e5f8df335fcc14b943f4fdd845506574

GitHub Actions run:
35383672477

job:
Focused exact occurrence and eligibility proof
```

Executed focused suites:

```text
tests.test_github_workflow_command_analysis
tests.test_parser_backed_ci_command_evidence
tests.test_single_pass_workflow_static_evidence
tests.test_ci_runtime_strengthening
tests.test_static_command_order
tests.test_ci_static_direct_exercise_order
```

Observed result:

```text
Ran 40 tests in 0.032s
OK
GitHub Actions job conclusion: success
```

The proof directly established:

- existing Stage-1 provider relations remain green;
- normal single-analysis production preserves `whole_step_relation` and
  `execution_profile` into static evidence;
- direct invocation evidence preserves workflow/revision identity;
- sole-command positive profiles classify eligible;
- first-sequential positive is admitted only for the accepted Bash/sh profiles;
- known negative structures classify ineligible;
- coarse/unadmitted/custom/missing-context cases remain unresolved;
- two occurrences in one job/step remain distinct by `StaticCommandLocation`;
- the new path-dependent structures do not accidentally earn same-step static ordering;
- existing direct-exercise ordering behavior remains green.

No Stage-3 runtime status/correlation aggregation behavior has been changed.

Stage-2 state after hosted proof:

```text
A orientation                  COMPLETE
B implementation               COMPLETE
C state preservation            COMPLETE
D post-build learning           ACTIVE
E gap repair / next orientation READY after review
```

The temporary proof workflow is evidence machinery only and is not part of the product
architecture or intended for merge to `main`.

### Build Stage 2 — CLOSED

Stage 2 is complete.

Ali reviewed and correctly distinguished the eligibility states:

```text
ineligible
→ the exact occurrence has a positively identified structure/profile condition
  that does not justify runtime strengthening

unresolved
→ the available structural/profile representation is genuinely insufficient
  to establish either the admitted positive or a known negative classification
```

Concrete reviewed example:

```text
conditional pip install
+ successful containing step
→ exact occurrence remains visible statically
→ eligibility = ineligible
→ do not treat successful step as positive runtime support for that occurrence
```

The reason is not merely that the shape "looks risky"; it is that the conditional relation
is positively known and the containing step can succeed even when the target command is
skipped.

By contrast, coarse structures such as the current generic short-circuit representation
remain `unresolved` because the current IR does not yet expose enough operator-specific
status semantics to decide safely.

Stage-2 closure evidence:

```text
implementation complete
hosted focused proof PASS — 40/40
exact occurrence preservation proven
eligibility classifier proven
conceptual/logical review complete
no Stage-3 runtime composition implemented during Stage 2
```

No material gap was exposed by the review.

### Build Stage 3 — Runtime Composition

**Status:** ACTIVE

Goal:

```text
exact runtime-strengthening candidate
+ existing exact runtime step correlation
+ continue-on-error interpretation
+ factual runtime status/conclusion
→ supported | not_established | unresolved runtime-strengthening result
→ correct workflow static fallback / runtime-correlated / broader unresolved state
```

Scope:

- remove the current early `(job_key, step_source_index)` reduction from runtime
  strengthening;
- preserve factual failed/skipped/cancelled outcomes;
- preserve static `supported_not_correlated` when stronger evidence is merely unavailable
  or structurally inadmissible;
- keep eligible exact runtime non-success materially visible at the broader CI layer;
- apply the same exact-occurrence composition separately to direct exercise.

Stage 2 is now reviewed, recorded, taught, and closed. Stage 3 is formally active.

Stage-3 Learning-by-Doing state:

```text
A orientation                  ACTIVE
B implementation               NOT STARTED
C state preservation            ACTIVE
D post-build learning           NOT STARTED
E gap repair / next orientation NOT STARTED
```

### Final proof and Phase-B closure

After the three build stages:

```text
focused provider proof
→ focused eligibility/composition proof
→ runtime-correlated CI proof
→ direct-exercise proof
→ nearby regression proof
→ full deterministic product suite
→ S001/S002 useful-positive pressure
→ S004 deferred/re-entry pressure
→ state/memory closure
```

Record actual executable proof results. Historical test totals are not proof.

## Progressive-recording rule

After every material discovery, implementation decision, focused proof result, failure, or
scope correction:

1. update this working memory before moving materially forward;
2. distinguish planned behavior from actual source/test evidence;
3. preserve failures/proof debt explicitly;
4. update `MEMORY.md` only when the live stage/milestone/blocker changes;
5. do not silently move to the next build stage before the current stage's teaching/review.

## Stage-transition rule

For each Build stage:

```text
implement
→ inspect the actual diff/source
→ focused validation as available
→ record
→ teach/explain the logical + conceptual model
→ resolve material questions/gaps
→ only then enter the next stage
```

Ali may challenge or redirect any stage before the next transition.

## Current entry state

Phase A is complete and accepted.

Phase B Stage 1 is formally selected and authorized.

No Stage-1 product source/test mutation has yet been performed in this working record.

`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
