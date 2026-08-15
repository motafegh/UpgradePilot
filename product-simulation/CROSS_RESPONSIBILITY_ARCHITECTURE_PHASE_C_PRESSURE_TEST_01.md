# Cross-Responsibility Architecture — Phase C Pressure Test 01

**Date:** 2026-08-15  
**Status:** Completed bounded transfer/adversarial evaluation; non-controlling product-simulation evidence  
**Branch at evaluation start:** `agent/product-simulation-case-screening-02`  
**Main/branch baseline at evaluation start:** `c1fa8e455fc581676d2b90a3a0f6325975241cc1`  
**Live-state authority:** [`../MEMORY.md`](../MEMORY.md)  
**Controlling architecture checkpoint:** [`../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md)  
**Main progressive reasoning record:** [`../working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md`](../working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md)

## 1. Purpose

Main has completed enough Phase-B architecture comparison to identify **Option B** as the leading candidate:

```text
RepositoryTextFile
        ↓
provider-specific bounded GitHub Actions workflow-definition IR
        ↓
   ┌────┴────┐
   ↓         ↓
  CI       Target

runtime WorkflowRun / WorkflowJob / WorkflowStep
remain a separate evidence family
```

Phase C asks whether existing real/adversarial evidence **supports, modifies, or rejects** that direction before main accepts an architecture decision.

This record performs that transfer pressure from the product-simulation side using already-admitted evidence. It does not replace main's architecture checkpoint and does not accept an ADR, implementation plan, parser dependency, source refactor, Target/CI contract migration, or orchestration change.

The owned question is:

> Does the proposed shared bounded static GitHub Actions structure survive the materially different evidence already preserved by UpgradePilot, and what constraints must main carry forward if it adopts that direction?

A secondary question, because the selected reconciliation also exposes `PublicPullRequestInvestigation` pressure, is:

> What do the existing multi-candidate simulation findings imply for the smallest safe heterogeneous-mechanism orchestration boundary?

## 2. Why no new case is justified

No S013 is required for this Phase-C question.

The existing corpus already contains discriminating pressure for the exposed decisions:

- **S008** — artifact-serviceability / exact-environment separation;
- **S011** — optional dependency environment formation and CI-coverage boundaries;
- **S004** — multi-job/matrix and CI-authority pressure;
- **AUDIT-002** — static command presence versus runtime execution/success hazards;
- **S010 + Cross-Candidate Context Synthesis Pressure Test 01** — heterogeneous mechanism/candidate preservation and anti-scalar synthesis pressure;
- current Target Artifact Environment Increment 1 — concrete consumer behavior that currently turns some unsupported source shapes into consumer-level problems.

The architecture question is therefore a **transfer/adversarial evaluation gap**, not a discovery gap.

## 3. Candidate under pressure

The minimum Option-B contract entering this evaluation is the Phase-B stop-line candidate recorded by main:

```text
WorkflowDefinitionResult
├─ WorkflowDefinition
│  ├─ source: RepositoryTextFile
│  ├─ workflow-level defaults.run
│  └─ ordered JobEntry[]
│     ├─ StepsJobDefinition
│     ├─ ReusableWorkflowJobDefinition
│     └─ JobProblem
└─ WorkflowDefinitionProblem

StepEntry
├─ RunStepDefinition
├─ UsesStepDefinition
└─ StepProblem
```

with provider-specific static structure such as:

```text
SourceSpan + source_index
bounded GitHubActionsStaticValue = scalar | sequence | mapping
job key/name/needs/runs-on/if/continue-on-error
workflow/job defaults.run
matrix/container fragments
job-level reusable workflow uses + with
ordered run/uses steps
step name/if/continue-on-error
run command + shell/working-directory
step uses + with
```

and these governing separations:

```text
raw exact source
!= normalized provider structure
!= CI interpretation
!= Target interpretation
!= runtime execution evidence
!= downstream impact/applicability conclusion
```

The Phase-C task is not to add more fields. It is to determine whether this shape survives real pressure and where it must be constrained.

## 4. Evaluation method

Each pressure is classified as one of:

```text
SUPPORT
= evidence directly reinforces the proposed boundary without material correction

MODIFY
= the architecture remains viable but must carry an explicit correction/constraint

REJECT
= the pressure exposes a structural contradiction that makes Option B the wrong base direction

INSUFFICIENT TO GENERALIZE
= no contradiction, but the evidence does not justify the broader claim being tested
```

The final Option-B classification is based on the combined pressure, not a vote count.

## 5. Pressure 1 — S008 artifact serviceability

### 5.1 Relevant S008 evidence

[`S008_POST_CASE_SYNTHESIS.md`](S008_POST_CASE_SYNTHESIS.md) establishes the OpenCV transition:

```text
old release
→ compatible CPython-3.6 Linux wheel exists

new release
→ compatible CPython-3.6 Linux wheel absent
→ source distribution remains
```

while separately preserving target facts such as Python-3.6 repository context, a real OpenCV relationship, an installation path, and insufficient exact CI coverage of the relevant artifact branch.

Its critical non-equivalences include:

```text
package/interpreter admissibility
!= binary artifact availability
!= source fallback availability
!= source fallback success
```

and:

```text
same package installed in CI
!= same artifact-selection branch exercised
```

### 5.2 Pressure result

**Classification: SUPPORT + CONSTRAINT.**

S008 strongly supports Option B's separation between:

```text
GitHub Actions source structure
```

and:

```text
Target/environment interpretation
```

A shared workflow-definition IR may preserve one workflow's declared runner, setup, commands, and structure. It must not absorb Dockerfile/repository Python context or artifact inventory evidence and manufacture one synthetic exact environment.

Therefore the architecture must continue to permit Target to combine **multiple proposition-specific evidence sources above the workflow IR** while retaining their provenance/scope separately.

### 5.3 Required constraint from S008

```text
workflow-definition facts
+
repository/Dockerfile/package facts
!= one exact target environment unless a later admitted rule proves that join
```

Option B survives S008 because it is a source-structure seam, not an environment reconstructor.

A future implementation would violate the transfer evidence if it changed the IR into a repository-wide target-environment union.

## 6. Pressure 2 — S011 optional dependency / CI environment coverage

### 6.1 Relevant S011 evidence

[`S011_POST_CASE_SYNTHESIS.md`](S011_POST_CASE_SYNTHESIS.md) establishes:

```text
Dictare optional [mlx] dependency family exists

standard PR CI
→ Ubuntu
→ installs .[dev]

macOS CI
→ macos-latest
→ installs .[dev]

neither inspected workflow installs .[mlx]
```

and therefore:

```text
platform-specific workflow exists
!= affected optional dependency environment exists
```

The case further separates:

```text
DEPENDENCY ENVIRONMENT FORMED?
↓
RUNTIME ACTIVATION CONDITIONS SATISFIED?
↓
BEHAVIOR PATH EXERCISED?
```

and:

```text
optional dependency declared
!= optional dependency installed
```

### 6.2 Pressure result

**Classification: MODIFY.**

Option B's structural boundary is supported: the IR should preserve macOS runner structure, Python setup structure, and the visible install command without deciding MLX applicability itself.

However, S011 exposes a semantic correction required above the IR.

The current Target Artifact Environment Increment 1 can emit:

```text
dependency_environment_formation = "established"
```

from static workflow-definition command text.

That wording is stronger than the evidence source.

Static workflow text can establish a proposition such as:

```text
direct installation declared/configured in this workflow/job scope
```

but not by itself:

```text
installation executed
installation succeeded
runtime environment formed
runtime activation occurred
behavior path exercised
```

### 6.3 Required semantic correction from S011

Main should carry this proof ladder explicitly into Phase D:

```text
STATIC DECLARATION / CONFIGURATION
workflow declares installation/path X

!=

RUNTIME EXECUTION
installation/path X actually executed

!=

RUNTIME SUCCESS
installation/path X succeeded

!=

ACTIVATION / EXERCISE
relevant dependency/runtime path participated
```

The final field/type names remain main's responsibility, but a static-only fact should not continue to be named as if runtime environment formation were established.

### 6.4 Bounded negative evidence remains valid

S011 also supports proposition-scoped negative reasoning:

```text
within these exact inspected workflow definitions,
no visible .[mlx] installation is declared
```

may be established if the bounded source-reader/evidence coverage is adequate.

It must not become:

```text
no CI/automation anywhere installs [mlx]
```

This is a consumer/evidence-coverage conclusion, not a parser conclusion.

## 7. Pressure 3 — S004 multi-job and matrix structure

### 7.1 Relevant S004 evidence

S004 includes materially different CI workflow shapes, including a multi-job workflow and matrix-backed test behavior. Later main inspection also identifies workflow definitions with ordered steps, setup actions, repeated installations, virtual-environment commands, and direct test execution.

The current narrow CI/Target readers commonly use:

```text
multiple jobs
→ unsupported / unresolved
```

as a first-slice consumer rule.

### 7.2 Pressure result

**Classification: SUPPORT.**

S004 supports the Phase-B distinction:

```text
shared lower-level structural preservation
!= downstream consumer support
```

A valid multi-job/matrix workflow should not become a whole-workflow parser failure merely because one current Target/CI rule cannot safely select or reason across those jobs.

The shared IR should preserve safely readable jobs, matrix fragments, `needs`, and ordered steps. CI or Target may still return unresolved for the proposition they own.

### 7.3 Required constraints from S004

```text
job source order
!= runtime scheduling order
```

```text
needs relationship
!= shared environment continuity
```

```text
multiple jobs in one workflow
!= one shared runtime environment
```

```text
one static matrix job
!= one runtime job instance
```

The IR may preserve all of these source facts while refusing operational inference.

## 8. Pressure 4 — AUDIT-002 CI proof hazards

### 8.1 Relevant hazards

[`../audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md`](../audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md) records concrete failure modes for the current bounded CI rule:

```text
pip install ... || true
continue-on-error: true
if: <condition>
exercise before installation
successful whole job while matched step failed/skipped
no exact proposed-version runtime witness
same job but changed interpreter/environment context
```

The audit also notes that runtime `WorkflowStep` evidence exists but is not yet safely correlated with matched static steps.

### 8.2 Pressure result

**Classification: SUPPORT + MODIFY IMPLEMENTATION SEQUENCING.**

Option B is strengthened by these hazards because ordered steps and proof-sensitive visible modifiers are genuinely shared static structure that both consumers should not reparse independently.

The IR should preserve at least the Phase-B admitted fields:

```text
ordered step variants
if condition text
continue-on-error value
run command text
shell / working-directory context
uses / with
```

But the IR must not decide runtime success.

### 8.3 `|| true` and shell-control-flow boundary

A key subtlety is that `|| true` is inside the `run` scalar rather than an Actions step modifier.

The static IR should preserve the decoded run text without destroying operator information.

A later command/dependency observation rule may recognize a potential installation command, but any **stronger proof rule** must either understand the admitted relevant control-flow form or abstain.

Therefore:

```text
IR preserves run text
!= IR proves command semantics
```

and:

```text
installation token recognized inside unsupported control flow
!= successful installation established
```

### 8.4 Static↔runtime correlation should remain a separate responsibility

AUDIT-002 supports future bounded static/runtime correlation, but it does not support hiding that join inside the base workflow-definition object.

A safer dependency direction remains:

```text
STATIC
RepositoryTextFile
→ GitHub Actions workflow-definition IR

RUNTIME
WorkflowRun / WorkflowJob / WorkflowStep

LATER, IF JUSTIFIED
explicit bounded static↔runtime correlation
→ stronger CI/runtime propositions
```

Naive correlation by step name alone or ordinal alone remains unaccepted.

### 8.5 Implementation-sequencing modification

The first Option-B implementation tranche should not silently combine:

```text
shared static parser migration
+
new runtime correlation semantics
```

Those are different responsibilities with different failure modes and proof obligations.

A cleaner sequence is:

```text
Tranche 1
bounded static Actions IR
+ CI static-reader migration
+ Target static-reader migration
+ static-proof semantic corrections

then, separately if authorized

Tranche 2
bounded static↔runtime correlation
+ stronger CI proof states/rules
```

This is a Phase-C recommendation to main, not an implementation authorization.

## 9. Pressure 5 — reusable workflows, aliases, and scoped structural problems

### 9.1 Available evidence

Main's Phase-B parser probe and source analysis establish that:

- reusable-workflow jobs are valid GitHub Actions job shapes;
- aliases can reuse YAML node source origins;
- cyclic aliases can create recursive node graphs;
- duplicate identities must remain visible before ordinary mapping collapse;
- one malformed/unmodeled job need not erase independently trustworthy neighboring structure.

The product-simulation corpus does not need a new public case merely to re-demonstrate valid YAML/provider syntax.

### 9.2 Pressure result

**Classification: SUPPORT WITH SAFETY CONSTRAINTS.**

The structural layer should distinguish:

```text
valid readable provider structure that a consumer cannot yet interpret
```

from:

```text
source structure that cannot safely be established
```

A reusable workflow reference can therefore be a valid static job variant while CI/Target remains unresolved about the called workflow.

Likewise scoped `JobProblem` / `StepProblem` is preferable to fabricating a valid object or discarding independently trustworthy sibling structure.

### 9.3 Safety requirements remain non-negotiable

If main later adopts PyYAML node composition or another parser front end, untrusted public YAML requires more than a non-constructing loader:

```text
bounded source size
active-recursion / alias-cycle detection
bounded depth
bounded node traversal
explicit duplicate material-key handling
```

This pressure does not select PyYAML versus `ruamel.yaml`.

No existing Phase-C case exposes a material requirement for round-trip formatting fidelity, because exact `RepositoryTextFile` source remains authoritative.

## 10. Pressure 6 — third-consumer/generalization test

### 10.1 Evidence state

There are currently two demonstrated consumers of overlapping static GitHub Actions structure:

```text
CI
Target
```

No third independent product consumer is currently implemented strongly enough to prove another abstraction boundary.

### 10.2 Pressure result

**Classification: INSUFFICIENT TO GENERALIZE.**

This does **not** reject Option B.

Two real consumers are enough to justify extracting demonstrated identical provider structure if the shared semantics are clear. They are not enough to justify turning that structure into a generic workflow framework.

Therefore the third-consumer test produces a negative design constraint:

```text
shared by CI + Target
!= generic workflow abstraction
```

Keep the IR explicitly provider-specific:

```text
GitHub Actions workflow definition
```

not:

```text
UniversalWorkflow
CIProviderWorkflow
GenericPipeline
```

Do not add extension interfaces, provider registries, plugin contracts, or generalized workflow-engine semantics for a hypothetical future consumer.

If a third real consumer arrives later, it should pressure the existing provider-specific contract rather than pre-authorize broader generalization now.

## 11. Secondary pressure — heterogeneous impact/orchestration boundary

The selected main reconciliation also asks whether `PublicPullRequestInvestigation` is becoming too first-mechanism-shaped.

Current application orchestration has explicit Python-support-specific fields for:

```text
pre-investigation impact assessment
selected investigation
post-observation impact assessment
```

while artifact serviceability and target artifact-environment behavior are not yet integrated into the same path.

### 11.1 S010 / cross-candidate evidence

[`CROSS_CANDIDATE_CONTEXT_SYNTHESIS_PRESSURE_TEST_01.md`](CROSS_CANDIDATE_CONTEXT_SYNTHESIS_PRESSURE_TEST_01.md) establishes that one proposal may contain multiple materially different technical candidates with different handling states, while repository-context findings and discovery-coverage limitations remain separate.

Its critical protections include:

```text
all currently known candidates resolved
!= candidate discovery complete
```

```text
candidate locally mitigated
!= candidate absent
```

```text
repository-context finding
!= technical applicability candidate
```

```text
one aggregate scalar
!= traceable synthesis
```

### 11.2 Orchestration pressure result

**Classification: SUPPORTS A SMALL TYPED COLLECTION/ENVELOPE; REJECTS A UNIVERSAL IMPACT OBJECT.**

The current evidence supports a future orchestration shape conceptually closer to:

```text
mechanism analysis/results collection
├─ Python-support mechanism-specific state
├─ artifact-serviceability mechanism-specific state
└─ future mechanism-specific state
```

than:

```text
UniversalImpactResult
risk_score
one compatibility state
```

Mechanism-specific candidates, evidence, evaluator states, and investigation semantics should remain typed by their mechanism.

The collection/envelope, if main admits it, should solve application field sprawl and heterogeneous transport/orchestration. It should not replace mechanism semantics or perform D-level synthesis.

### 11.3 Keep orchestration work separate from the workflow-IR migration

The shared workflow-definition seam and heterogeneous mechanism-result orchestration are both real architecture pressures, but they are not the same responsibility.

Phase C therefore recommends that main avoid one large refactor containing all of:

```text
new YAML parser dependency
shared workflow IR
CI migration
Target migration
runtime correlation
Target proof-state rename
artifact-serviceability application integration
new heterogeneous result envelope
```

unless Phase D can prove that such coupling is required for one coherent invariant.

The default safer interpretation is separate bounded tranches.

## 12. Consolidated Phase-C classification

| Pressure | Result for Option B | Material consequence |
|---|---|---|
| S008 artifact serviceability | **SUPPORT + constraint** | workflow structure must not flatten other target/environment evidence into a fabricated exact environment |
| S011 optional dependency / CI coverage | **MODIFY** | static install declaration must not be named/treated as runtime environment formation |
| S004 multi-job/matrix | **SUPPORT** | shared structure should preserve valid multi-job/matrix source while consumers may remain unresolved |
| AUDIT-002 CI hazards | **SUPPORT + sequencing modification** | preserve ordered/proof-sensitive structure; keep runtime correlation separate from base static IR |
| reusable/alias/scoped problems | **SUPPORT with safety constraints** | valid structure vs consumer unresolved vs structural hard problem must remain distinct; parser resource bounds required |
| third-consumer test | **INSUFFICIENT TO GENERALIZE** | keep the shared contract GitHub-Actions-specific; do not build a generic workflow framework |

No pressure produced a structural reason to reject Option B.

## 13. Phase-C conclusion for Option B

**Simulation-side conclusion: `OPTION B — SUPPORTED WITH REQUIRED CONSTRAINTS / MODIFICATIONS`.**

The evidence supports the architecture direction:

```text
RepositoryTextFile
→ bounded provider-specific GitHub Actions workflow-definition IR
→ separate CI and Target interpretation
```

while keeping runtime Actions evidence separate.

The following constraints should be treated as decision-critical if main accepts Option B:

### C-01 — Static declaration must retain static proof strength

```text
workflow declares installation/configuration
!= executed
!= succeeded
!= environment formed at runtime
!= dependency path exercised
```

### C-02 — Consumer limitations must not become shared parser limitations

```text
multi-job / matrix / reusable / dynamic value
may be valid preserved structure
while one current consumer remains unresolved
```

### C-03 — Multi-source target evidence must remain scoped

```text
workflow facts
+
Dockerfile/repository/package facts
!= synthetic exact environment without an explicit justified join
```

### C-04 — Static and runtime Actions evidence remain separate base contracts

Any later join must be explicit, bounded, and evidence-safe.

### C-05 — Source order/needs are structural evidence, not runtime continuity proof

No cross-job or same-job environment continuity should be inferred merely from source relationships.

### C-06 — Preserve run text/context without becoming a shell interpreter

Proof-sensitive operators or execution modifiers must either be covered by an admitted bounded rule or cause stronger downstream claims to remain unresolved.

### C-07 — Keep the IR provider-specific and selectively normalized

No generic workflow engine, provider abstraction, plugin system, or universal environment model is justified by current evidence.

### C-08 — Parser safety includes graph/resource bounds

Safe/non-constructing YAML handling alone is insufficient for untrusted public workflow source.

## 14. Parser-library disposition from Phase C

This transfer pressure does not expose a reason to reject main's leading parser method:

```text
YAML node/composition front end
→ guarded bounded GitHub Actions extraction
→ typed IR
```

It also does not independently prove that PyYAML is the only correct library.

Current Phase-C evidence requires capabilities such as:

```text
mapping-pair visibility before normal dict collapse
source marks
scalar/sequence/mapping distinction
non-constructing textual scalar handling
alias-cycle detection opportunity
bounded traversal
```

If PyYAML satisfies the accepted implementation tests safely, no simulation evidence currently justifies a heavier round-trip parser solely for formatting preservation.

Library/dependency acceptance remains main's Phase-D/implementation-handoff responsibility.

## 15. Recommended implementation sequencing if main accepts Option B

This is a transfer recommendation, not authorization.

### Tranche 1 — shared static source structure

```text
provider-specific bounded workflow-definition IR
+ parser safety/resource guards
+ focused structural tests
+ migrate CI static source reading
+ migrate Target static source reading
+ preserve/restate exact proof strength
+ correct static Target installation/formation naming semantics
+ focused CI/Target regressions
+ full active suite
```

Do not strengthen runtime command-success claims merely because the parser changed.

### Tranche 2 — stronger CI runtime proof, only if separately admitted

```text
explicit static↔runtime correlation rule
+ matched-step identity constraints
+ install-before-exercise rule
+ if / continue-on-error / control-flow handling or abstention
+ runtime step-success evidence
+ exact-version witness only when actually observed
```

### Separate orchestration tranche

If main decides application field sprawl now requires a heterogeneous result boundary:

```text
small typed mechanism-result collection/envelope
+ mechanism-specific result types preserved
+ no scalar collapse
+ no universal impact engine
```

This should not be coupled to the static parser migration merely because both questions were exposed by the same architecture checkpoint.

## 16. Main-thread handoff

Main can use this record as Phase-C pressure evidence when updating its progressive reconciliation record.

The simulation-side handoff is:

```text
Option B
→ SUPPORT WITH REQUIRED MODIFICATIONS/CONSTRAINTS

No new case required.
No source refactor authorized here.
No YAML dependency accepted here.
No runtime-correlation method accepted here.
No universal impact/orchestration abstraction accepted here.
```

The highest-value items for main to decide/promote in Phase D are:

1. accept/reject the provider-specific shared static workflow-definition seam;
2. require static installation/configuration semantics to remain distinct from runtime environment formation;
3. keep static/runtime correlation as an explicit later boundary rather than part of the base IR;
4. preserve multi-job/matrix/reusable source structure independently from consumer support;
5. decide parser method/dependency and exact resource-safety obligations;
6. decide whether heterogeneous mechanism orchestration is admitted now as a separate small typed collection/envelope or deferred until application integration requires it;
7. define separate bounded implementation tranches rather than one architecture-wide rewrite.

## 17. What this pressure test does not establish

It does not establish:

- that Option B is now controlling architecture;
- exact Python type/module names;
- PyYAML acceptance;
- a safe static↔runtime step-correlation algorithm;
- exact renamed Target public state names;
- matrix expansion semantics;
- reusable-workflow recursive acquisition/interpretation;
- container environment reconstruction;
- shell execution semantics;
- exact wheel-tag derivation;
- source-build success;
- a universal mechanism interface;
- final maintainer-facing synthesis;
- candidate-discovery completeness;
- production readiness.

Those require their own normal owners/evidence.

## 18. Stop

This Phase-C product-simulation pressure test is complete.

Do not create S013 or another architecture pressure document merely to add more examples unless main exposes a concrete unresolved discriminator that S004/S008/S010/S011/AUDIT-002 and the current source evidence cannot answer.

The next useful action is for main's architecture-reconciliation owner to inspect this record, decide whether the Phase-C evidence supports/modifies/rejects Option B, and proceed to its own Phase-D classification and implementation handoff if warranted.
