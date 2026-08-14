# B2 Cross-Responsibility Architecture Reconciliation — Progressive Working Record

**Date:** 2026-08-14  
**Operation:** B2 cross-responsibility architecture reconciliation  
**Result classification:** IN PROGRESS / progressive reasoning record  
**Repository baseline at start:** `f2c19e1ed246f3b3a30f0d1814743752ff44b474` on `main`

## 1. Purpose

Preserve the detailed evidence, reasoning, comparisons, rejected interpretations, and evolving findings produced while executing [`../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md).

This is the **single progressive working record** for the current reconciliation unless the investigation materially changes responsibility. Continue appending to this file rather than creating one dated file per architecture question.

This record does not own live project position, authorize implementation, or replace accepted specifications/ADRs. `../MEMORY.md` remains the sole live-state owner. Accepted durable conclusions must later be promoted to their normal specification/ADR/plan owner when the reconciliation closes.

## 2. Governing and orientation sources

Normal authority / execution owners:

- [`../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) — accepted A→B→C product-decision semantics and proof-strength boundaries.
- [`../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) — trust, evidence, provenance, and abstention invariants.
- [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) — bounded-domain generality and anti-fixture constraints.
- [`../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md) — current source-ownership and dependency-direction baseline.
- [`../plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](../plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md) — parent responsibility.
- [`../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md) — selected bounded architecture checkpoint.
- [`../proposals/UPGRADEPILOT_MATURE_SYSTEM_HORIZON.md`](../proposals/UPGRADEPILOT_MATURE_SYSTEM_HORIZON.md) — non-controlling future-pressure/orientation surface only.

## 3. Prior reasoning/evidence being reused

These records are provenance and pressure evidence, not the canonical owner of accepted semantics:

- [`2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md) — historical A→B→C reconciliation rationale later promoted to the Product Decision Model specification.
- [`../audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md`](../audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md) — known CI proof-strength risks: static command presence vs matched runtime execution/success, control-flow masking, step modifiers, ordering, step correlation, exact-version witness, and environment continuity.
- [`2026-08-04_B2-source-structure-reconciliation-final-acceptance.md`](2026-08-04_B2-source-structure-reconciliation-final-acceptance.md) — accepted precedent for promoting genuinely identical primitives while preserving responsibility-specific meaning.
- [`2026-08-12_B2-responsibility-shaped-expansion-decision.md`](2026-08-12_B2-responsibility-shaped-expansion-decision.md) — small implementation increments must not imply a small architecture horizon; second materially different mechanisms/consumers should pressure shared contracts.
- [`2026-08-13_B2-target-evidence-design-checkpoint.md`](2026-08-13_B2-target-evidence-design-checkpoint.md) — target-evidence design exploration and evidence-source boundary pressure.
- [`2026-08-13_B2-target-evidence-boundary-adoption.md`](2026-08-13_B2-target-evidence-boundary-adoption.md) — adopted first target-evidence boundary and deliberately unresolved exact wheel compatibility.
- [`2026-08-14_B2-target-artifact-environment-increment-1-implementation.md`](2026-08-14_B2-target-artifact-environment-increment-1-implementation.md) — implementation evidence for the first static Actions target-environment slice.
- [`2026-08-14_B2-cross-responsibility-architecture-plan-alignment.md`](2026-08-14_B2-cross-responsibility-architecture-plan-alignment.md) — why this reconciliation became the selected checkpoint before more target-environment expansion.

## 4. Active source/test surface inspected so far

Primary source:

```text
src/upgradepilot/github/actions.py
src/upgradepilot/github/repository.py
src/upgradepilot/repository_path.py

src/upgradepilot/ci/workflow_commands.py
src/upgradepilot/ci/dependency_exercise.py

src/upgradepilot/target/artifact_environment.py

src/upgradepilot/impact/applicability.py
src/upgradepilot/impact/python_support.py
src/upgradepilot/impact/artifact_serviceability.py

src/upgradepilot/investigation.py
```

Focused tests inspected:

```text
tests/test_github_actions.py
tests/test_ci_dependency_exercise.py
tests/test_target_artifact_environment.py
tests/test_artifact_serviceability.py
```

## 5. Current architecture/data-flow baseline

Observed current shape:

```text
                         GitHub provider
                              │
             ┌────────────────┴────────────────┐
             │                                 │
             ▼                                 ▼
 exact Actions runtime evidence        exact repository text
 WorkflowRun / WorkflowJob /           RepositoryTextFile
 WorkflowStep                          workflow definition
             │                                 │
             │                     ┌───────────┴────────────┐
             │                     │                        │
             ▼                     ▼                        ▼
       CI runtime facts      ci/workflow_commands   target/artifact_environment
                                  static parsing         static parsing
             │                     │                        │
             └──────────────┬──────┘                        │
                            ▼                               ▼
                   ci/dependency_exercise       partial target-environment facts


                    mechanism-specific impact
                 ┌──────────────┴──────────────┐
                 ▼                             ▼
          Python support               artifact serviceability
                 │                             │
                 └──────────────┬──────────────┘
                                ▼
                       impact/applicability
                    shared proposition/path logic


application orchestration: investigation.py
  integrated today: Python-support path
  not yet integrated: artifact-serviceability + target-artifact-environment path
```

Interpretation:

- `github/actions.py` is already a sound provider/acquisition boundary: it records what GitHub reported about exact-head runs/jobs/steps and does not interpret dependency meaning.
- `github/repository.py` is the exact static-file acquisition boundary.
- CI currently composes runtime run/job success with static workflow-command recognition.
- Target Increment 1 currently interprets only static workflow definition evidence.
- Applicability composition is already a demonstrated good shared abstraction across two impact mechanisms.
- application orchestration remains first-mechanism-shaped.

## 6. Progressive findings

### F-001 — Acquisition, static structure, domain interpretation, and conclusion are distinct responsibilities

Observed:

```text
exact source/runtime acquisition
!= normalized workflow structure
!= CI interpretation
!= Target interpretation
!= downstream proposition/impact conclusion
```

This separation is already partially present and should be preserved. The architecture problem is not solved by merging CI and Target into one domain.

### F-002 — CI and Target duplicate lower-level workflow-definition parsing

`src/upgradepilot/ci/workflow_commands.py` and `src/upgradepilot/target/artifact_environment.py` independently implement materially overlapping handling for:

```text
jobs: discovery
job indentation / job key detection
run: extraction
multiline run blocks
pip / pip3 / python -m pip installation recognition
-r / --requirement path recognition
repository-command path normalization
```

This is demonstrated implementation duplication, not merely conceptual similarity.

The consumers nevertheless have different semantic questions:

```text
CI
→ did admitted successful exact-head CI consume/exercise the changed dependency?

Target
→ what scoped environment/configuration facts can this target evidence establish?
```

Provisional implication: shared **source structure / factual observation** is plausible; shared CI/Target domain conclusions are not.

### F-003 — Static declaration, runtime execution, and runtime success require separate proof strengths

Accepted semantic guard:

```text
workflow definition declares command/path X
!= command/path X executed
!= command/path X succeeded
```

AUDIT-002 already demonstrates concrete hazards:

- `pip install ... || true` can mask failure;
- `continue-on-error: true` can permit failure;
- `if:` can skip a step;
- current command matching does not prove install-before-exercise ordering;
- runtime `WorkflowStep` evidence is already acquired but not correlated to the matched static step;
- even matched install/exercise success does not automatically establish the exact proposed package version was used.

The current CI `proven` state is therefore safest when read as a bounded static-path + successful run/job claim, not matched-command runtime-success proof.

The current Target field `dependency_environment_formation="established"` is potentially too strong if sourced solely from static YAML. The reconciliation must decide whether the correct contract should distinguish at least:

```text
direct installation declared/configured
installation runtime-observed/executed
installation succeeded
```

No rename/change is accepted yet.

### F-004 — Multiple jobs should be separated into structural preservation vs consumer support

Both current CI and Target readers reject multiple statically visible jobs.

That restriction may remain valid for their current proof rules, but it should not automatically become a lower-level workflow-structure limitation.

Likely distinction to pressure-test:

```text
normalized structural layer
→ preserve N ordered jobs

CI / Target consumer
→ decide whether current rule can safely interpret/select/compose those jobs
→ otherwise unresolved
```

This avoids losing visible source structure merely because one current consumer lacks a multi-job reasoning rule.

Cross-job environment continuity must not be inferred merely because jobs belong to one workflow.

### F-005 — Ordered steps and step modifiers already shape architecture now

AUDIT-002 establishes that install-before-exercise ordering matters for CI's causal claim.

Therefore a credible normalized static workflow structure should be evaluated for preserving ordered steps and relevant visible modifiers such as:

```text
name
uses
with
run
if / raw condition presence
continue-on-error
```

Preservation does not imply full GitHub expression or shell interpretation.

### F-006 — Bounded static↔runtime step correlation is a credible near-term strengthening

Runtime step summaries already exist through `WorkflowJob.steps`:

```text
step number
step name
status
conclusion
```

A future stronger CI rule may correlate an identifiable static install/exercise step with its exact runtime step and require runtime success.

The correlation rule itself must be trustworthy. Naive name-only or ordinal-only matching is not accepted yet because generated setup/cleanup steps, duplicate names, omitted names, reusable actions, and other transformations may make identity ambiguous.

### F-007 — CI should be strengthened, but Target must not become a child of CI

Stronger workflow/runtime evidence can serve both responsibilities, but Target needs evidence beyond CI and may use static configuration even when no successful CI run exists.

Credible future Target evidence sources include repository/build/runtime context such as:

```text
GitHub Actions configuration/runtime
Dockerfile/container configuration
project metadata
optional dependency configuration
runtime/usage code
tox/nox/task configuration
documentation where proposition-appropriate
```

Therefore the likely dependency direction is:

```text
shared provider/static structure/runtime factual evidence
        ↓                    ↓
       CI                  Target
```

not:

```text
Target → CI conclusion
```

### F-008 — `impact/applicability.py` is a positive precedent for earned abstraction

Python-support and artifact-serviceability retain mechanism-specific candidate/evidence/evaluator semantics while sharing only the genuinely identical proposition/path/candidate applicability composition contract.

This is the architectural pattern to imitate:

```text
share demonstrated identical semantics
keep mechanism/domain-specific meaning separate
```

### F-009 — application orchestration is first-mechanism-shaped

`PublicPullRequestInvestigation` currently has explicit Python-support-specific fields such as pre-investigation result, selected investigation, and final impact result.

Artifact serviceability and target artifact-environment capability are not yet integrated into this real application path.

This creates demonstrated pressure for a small typed heterogeneous-mechanism orchestration boundary, but does not yet justify a universal impact engine or opaque scalar result.

### F-010 — an older shared primitive has drifted back into local duplication

`src/upgradepilot/repository_path.py` is the accepted source-neutral repository-relative path structural owner from the August 4 reconciliation.

`src/upgradepilot/github/repository.py` nevertheless contains a separate `_validate_repository_path(...)` implementation with different details.

This is a concrete semantic-drift risk and belongs in the eventual reconciliation/refactor inventory.

### F-011 — stronger CI is part of the likely implementation handoff, not a distant later phase

The current architecture checkpoint exists precisely because the old bounded CI rule and new Target consumer now expose shared structure and proof-strength pressure.

After architecture option comparison, adversarial transfer, and accepted ownership direction, the resulting implementation/refactor handoff should evaluate a coherent tranche including:

```text
shared bounded workflow-definition structure
CI migration to shared structure
Target migration to shared structure
ordered-step preservation
multi-job structural preservation
step modifier preservation
CI proof fact/claim-strength refinement
bounded static↔runtime step correlation where safely justified
Target declaration/runtime formation semantics correction
heterogeneous mechanism orchestration pressure
```

Exact scope remains undecided until the architecture decision is accepted.

## 7. Future-pressure classification — current provisional view

### SHAPES ARCHITECTURE NOW

Already demonstrated by active source/audit/current B2 pressure:

- multiple workflow jobs as visible structure;
- ordered steps;
- `uses` / `with`;
- `if` presence/raw condition and `continue-on-error` where they affect proof strength;
- literal/dynamic runner and setup-python facts;
- static installation declaration as a distinct proof fact;
- static definition vs runtime run/job/step evidence;
- possible bounded static↔runtime step correlation;
- heterogeneous impact-result orchestration;
- exact provenance and job/step scope preservation.

### KEEP COMPATIBLE WITH

Credible near-term B3/B4/real-repository pressures; avoid architecturally blocking them, but do not necessarily implement semantics now:

- matrix workflow declaration and later static/runtime instance correlation;
- reusable workflow references;
- job containers;
- tox/nox/task-runner/config tracing when a real proposition requires it;
- runtime exact-version witnesses;
- other target-evidence sources beyond GitHub Actions;
- broader replay/changed-head/failed-acquisition correlation from B3.

### IGNORE FOR CURRENT ARCHITECTURE

Still too speculative/broad to shape implementation contracts now:

- universal CI-provider abstraction;
- full shell interpreter;
- full GitHub Actions expression evaluator;
- universal environment reconstruction;
- generic provenance graph;
- arbitrary recursive script/task execution semantics;
- universal workflow execution engine;
- generic impact engine / universal planner.

## 8. Architecture concepts / learning notes

The current investigation provides concrete examples of several reusable engineering concepts:

```text
acquisition != interpretation != conclusion

static declaration != execution != success

same syntax != same domain meaning

lossless lower-level structure can support conservative higher-level consumers

duplicate code is dangerous because semantics can drift, not merely because lines repeat

domain polymorphism and application orchestration are separate design problems

first-slice limitations may be acceptable in a consumer,
but should not automatically become permanent shared architecture
```

## 9. Open questions for Phase B/C

Still unresolved:

1. What is the smallest credible normalized GitHub Actions workflow-definition contract?
2. Which package should own that structure: existing `github/`, a source-neutral owner, or another demonstrated responsibility?
3. Should direct installation recognition live in the workflow structural layer, a separate factual-observation layer, or remain consumer-specific?
4. What exact CI public/internal states should replace or refine overloaded `proven` semantics, if any?
5. What bounded static↔runtime step correlation rule is trustworthy enough to admit?
6. Which multi-job behavior should be implemented now versus merely preserved structurally?
7. How much matrix/container/reusable-workflow structure should be modeled without executing/interpreting it?
8. What is the smallest typed mechanism-result collection/envelope that avoids `PublicPullRequestInvestigation` field sprawl while preserving mechanism-specific types?
9. Which source moves/refactors require a new ADR versus an implementation plan under ADR-0007?
10. Which current target-environment state names/contracts must change after the static/runtime distinction is accepted structurally?

## 10. Next record update trigger

Append to this same file when Phase B architecture options are compared, when a transfer/adversarial case changes the preferred design, when an option is rejected for a concrete reason, or when an accepted architecture direction is ready for classification/promotion.

Do not use this section as live continuation; `../MEMORY.md` owns the exact next action.

## 11. Phase B formally opened — candidate architecture options

**Phase B entry:** Phase A has established enough current-state evidence to compare architecture options without guessing from a single consumer. No source refactor is authorized by opening this phase.

Phase B will compare at least:

```text
Option A — keep local CI/Target parsers and repair semantics locally
Option B — shared bounded GitHub Actions workflow-definition structure + separate interpreters
Option C — broader normalized static+runtime Actions evidence model
```

Comparison criteria remain those required by the controlling reconciliation plan:

```text
ownership clarity
proof-strength correctness
duplication removed/retained
current-test impact
multi-job / ordered-step behavior
future matrix/container/reusable compatibility
CI strengthening capability
Target independence from CI
migration cost/reversibility
risk of premature generalization
```

### 11.1 First Phase B step — make Option B concrete before accepting or rejecting it

The first design exercise is deliberately narrower than choosing the final architecture:

> What is the smallest normalized **static GitHub Actions workflow-definition contract** that preserves the structure both CI and Target already need, while making no CI, Target, runtime-success, or environment conclusion itself?

#### Real pressure examples inspected

Two retained product-simulation artifacts provide useful contrasting shapes.

`product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/artifacts/raw/E17-python-workflow.yml` contains a simple one-job workflow:

```text
build
→ runs-on: ubuntu-latest
→ checkout
→ setup-python with literal 3.10
→ multiline pip installation
→ lint
→ pytest
```

`product-simulation/scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/artifacts/raw/ev-004-ci-workflows.txt` contains two materially different workflow definitions:

```text
ci.yml
├─ lint job
└─ test job
   ├─ dynamic runs-on from matrix.platform
   ├─ matrix python-version/platform declarations
   ├─ setup-python
   └─ tox-based execution

regression.yml
└─ test job
   ├─ setup-python
   ├─ multiple checkout steps
   ├─ multiline run blocks
   ├─ virtual-environment creation/activation
   ├─ repeated requirements installation
   └─ later pytest execution
```

These examples reinforce that the shared structural layer must not equate:

```text
multiple jobs
matrix declaration
virtual-environment commands
static command order
```

with understood runtime environment semantics. It should preserve visible structure first.

#### Option B candidate contract — v0.1, not accepted

A first candidate shape is:

```text
RepositoryTextFile
        ↓
read/normalize bounded GitHub Actions structure
        ↓
GitHubActionsWorkflowDefinition
├─ source identity/reference to exact RepositoryTextFile
└─ jobs: ordered tuple[GitHubActionsJobDefinition, ...]

GitHubActionsJobDefinition
├─ key
├─ runs_on_raw / literal-or-dynamic status
├─ reusable_workflow reference/presence where visible
├─ strategy/matrix presence + bounded raw/static representation
├─ container presence + bounded raw/static representation
└─ steps: ordered tuple[GitHubActionsStepDefinition, ...]

GitHubActionsStepDefinition
├─ source order/index
├─ name if visible
├─ uses if visible
├─ with inputs as bounded visible key/value structure
├─ run block if visible
├─ if/raw condition if visible
└─ continue-on-error visible value/presence
```

The exact Python type names and module filename are intentionally **not** decided yet.

The structural result may also require an explicit typed problem/limitation state when even the bounded source shape cannot be read safely. The goal is not to force every YAML document into a partially fabricated model.

#### What the candidate structure must NOT own

Option B v0.1 explicitly excludes these conclusions:

```text
job/run/step executed
job/run/step succeeded
changed dependency was installed
changed package was exercised
exact proposed package version was present
one job shares an environment with another job
matrix combinations actually executed
GitHub expressions evaluated
shell control flow evaluated
virtual-environment continuity established
Target environment established
exact wheel tags derived
CI sufficiency decided
```

Those are later factual/runtime joins or responsibility-specific interpretations.

#### Static vs runtime relationship under Option B v0.1

The candidate architecture keeps the two evidence classes separate:

```text
STATIC
RepositoryTextFile
→ GitHubActionsWorkflowDefinition

RUNTIME
github/actions.py
→ WorkflowRun / WorkflowJob / WorkflowStep
```

A later bounded correlation responsibility may join an identifiable static job/step to runtime job/step evidence. That join is **not** hidden inside the static workflow-definition object.

This is intentional because:

```text
normalized static source
!= observed execution instance
```

and because one static matrix job can correspond to several runtime job instances.

#### Direct dependency installation recognition under Option B v0.1

The pure structural model should preserve the raw ordered `run` content, but should **not yet classify** it as “dependency installation” merely as part of parsing.

Reason:

```text
run: <text>
```

is GitHub Actions structure, while:

```text
this command directly installs dependency source file X
```

is a factual command/dependency relation that requires shell-token/path interpretation and an independently established source path.

Therefore the leading decomposition to test is:

```text
workflow structural reader
→ ordered static steps/run content
        ↓
shared bounded command/install observation (possible separate primitive)
        ↓
CI interpretation / Target interpretation
```

Whether that middle observation deserves its own module/type remains open; this phase must compare it against keeping recognition consumer-specific.

### 11.2 Phase B findings added from the first concrete design exercise

#### F-012 — Real workflow evidence supports multi-job preservation in the shared structural layer

S004 already contains a two-job workflow with a matrix-backed test job. A lower-level reader that globally rejects `len(jobs) != 1` would encode a current consumer limitation into shared source structure and would discard visible information needed by later CI/Target reasoning.

Provisional direction:

```text
shared structure preserves all safely identifiable jobs
consumer decides whether one or more are interpretable for its proposition
```

#### F-013 — Ordered static steps are structural evidence, while environment continuity is not

S004 regression workflow shows repeated virtual-environment creation, activation, installation, checkout, and test steps. Preserving their source order is necessary for later reasoning, but the structural layer must not infer that two commands use the same interpreter/environment merely because they occur in one job.

This reinforces:

```text
step order = structural fact
same runtime environment = stronger interpreted proposition
```

#### F-014 — Static workflow definition and runtime Actions evidence should remain separate contracts

A combined static+runtime object at the lowest layer would blur definition identity with execution-instance identity and complicate matrix/retry/multi-run cases. Option B therefore currently has a structural advantage over a broad Option C model: it allows a later explicit correlation/join without weakening either evidence class.

This is provisional and must still be compared formally against Option C.

#### F-015 — Direct installation recognition is likely above the pure structural reader

Both current consumers need visible direct-install recognition, but the meaning is not merely YAML structure. The shared workflow-definition layer should probably preserve ordered `run` content and leave “installs exact source X” to a separate bounded observation/interpretation primitive.

This avoids making the GitHub Actions source model dependency-aware while still allowing the duplicated CI/Target matcher to converge later if its semantics are proven identical.

### 11.3 First-step unresolved design questions

Before Option B can become a serious candidate rather than a diagram, Phase B must next resolve:

1. **Owner:** does this provider-specific static structure belong under existing `upgradepilot.github`?
2. **Parsing method:** retain a bounded indentation reader, adopt a real YAML parser, or use another bounded method? The contract must be selected before the implementation method.
3. **Raw vs normalized values:** what exact representation safely preserves literal versus dynamic `runs-on`, `with`, `if`, matrix, container, and reusable-workflow values?
4. **Problem model:** when should the structural reader return partial structure with limitations versus a typed unreadable/unsupported problem?
5. **Job ordering semantics:** source order can be preserved, but must not imply runtime scheduling order.
6. **Step identity:** what source identity/order fields are sufficient for a later bounded static↔runtime step correlation?
7. **Installation observation:** whether the shared direct-install matcher is a separate neutral/provider-adjacent primitive or remains temporarily consumer-specific.

These are the active first-step questions. No final Option B selection has occurred yet.

### 11.4 Provisional ownership result — `upgradepilot.github` is the strongest current owner

Phase B has now compared four plausible homes for the normalized static workflow-definition responsibility:

```text
ci/
target/
github/
a new generic/source-neutral owner
```

Current provisional ranking:

```text
1. github/                      strongest
2. new generic/shared owner     unnecessary/weak
3. ci/                          wrong dependency direction
4. target/                      wrong dependency direction
```

Reasoning:

- `ci/` is not a valid neutral owner because Target legitimately needs static Actions configuration evidence without inheriting CI proof semantics or requiring a successful CI run.
- `target/` is symmetricly wrong because CI also needs the same static job/step structure for a different proposition.
- a generic source-neutral owner would misclassify the responsibility: `jobs`, `runs-on`, `steps`, `uses`, `with`, matrix, and related fields are specifically **GitHub Actions** concepts rather than generic workflow concepts.
- `github/` already owns provider-specific GitHub acquisition/identity responsibilities under ADR-0007 and can own a bounded provider-specific static definition representation while CI and Target remain separate consumers.

Key distinction:

```text
neutral between consumers
!=
source-neutral
```

The structure can be neutral between CI and Target while remaining specifically GitHub Actions structure.

Provisional dependency direction:

```text
github/repository.py
        ↓
github/<static workflow-definition owner>
        ↓
   ┌────┴────┐
   ↓         ↓
  ci/      target/
```

The exact module filename remains undecided; `github/workflow_definition.py` is only a candidate name until the contract is settled.

`github/actions.py` remains a distinct runtime Actions-evidence owner. Mixing static workflow-definition parsing into that module is currently disfavored because static definitions and runtime run/job/step instances have different identity and lifecycle semantics, especially for matrices, retries, and multiple runs.

#### F-016 — Provider-specific structure can be cross-consumer without becoming source-neutral

This reconciliation exposes an important ownership rule:

```text
shared by CI and Target
!= generic/common
```

A primitive belongs at the narrowest owner whose semantics are genuinely stable. Static GitHub Actions structure is shared across consumers but still provider-specific, so the existing `github/` package is the strongest current owner.

This is provisional Phase-B reasoning, not an accepted ADR decision. It must survive the raw/normalized contract design and later Option A/B/C comparison before promotion.

### 11.5 Raw vs normalized vs interpreted values — Option B contract v0.2

The next contract refinement separates three levels explicitly:

```text
RAW EVIDENCE
RepositoryTextFile
= exact repository/revision/path/blob/content provenance

NORMALIZED STATIC STRUCTURE
= what bounded GitHub Actions syntax visibly declares

INTERPRETED DOMAIN FACTS
= CI or Target meaning derived from that structure plus any additional evidence
```

The normalized structure functions as a bounded provider-specific **Intermediate Representation (IR)** between exact YAML source and responsibility-specific reasoning. It is not a generic YAML Abstract Syntax Tree (AST) and not an Actions execution model.

#### Raw source ownership

`RepositoryTextFile` remains the authoritative exact source. The normalized workflow object should retain/reference that source at the workflow root rather than copying repository/revision/path/blob provenance into every job and step.

Jobs and steps should preserve structural locators such as source order/index and job key so an extracted downstream fact can later materialize exact provenance at the scope it needs.

This means the normalized model can decode safe source syntax without pretending to replace the raw evidence. Comments, quoting style, and whitespace need not become semantic fields merely to claim losslessness because exact source remains available through the root evidence object.

#### Candidate normalized shape — v0.2, still provisional

```text
GitHubActionsWorkflowDefinition
├─ source: RepositoryTextFile
└─ jobs: ordered tuple[JobDefinition, ...]

JobDefinition
├─ source_index
├─ key
├─ name?                    # visible value only
├─ runs_on?                 # static scalar/fragment, literal or dynamic
├─ matrix?                  # bounded preserved fragment; NOT expanded
├─ container?               # bounded preserved fragment
├─ reusable_workflow?       # visible job-level uses/reference
└─ steps: ordered tuple[StepDefinition, ...]

StepDefinition
├─ source_index
├─ name?
├─ uses?
├─ with_inputs              # bounded visible key/value collection
├─ run_block?               # preserved as one source command block
├─ if_condition?            # raw/normalized condition text; NOT evaluated
└─ continue_on_error?       # visible literal/dynamic value; NOT execution result
```

The final model may also preserve job-level execution modifiers if source/adversarial checks demonstrate they are required for the admitted proof boundary. No generic job-execution semantics are accepted merely by this sketch.

#### Scalar/value states

At minimum, scalar-like fields should preserve:

```text
ABSENT
PRESENT + LITERAL
PRESENT + DYNAMIC
```

A small structural value can conceptually preserve:

```text
text
form: literal | dynamic
```

The exact dynamic expression text remains available. There is no need yet to make pure expressions and templated strings separate public state categories; consumers can distinguish them later if real semantics require it.

Examples:

```text
runs-on: ubuntu-latest
→ present + literal("ubuntu-latest")

runs-on: ${{ matrix.platform }}
→ present + dynamic("${{ matrix.platform }}")

python-version absent
→ absent

python-version: ${{ vars.PYTHON_VERSION }}
→ present + dynamic(...)
```

Dynamic is therefore **valid structural evidence**, not a parser failure. What remains unresolved is its evaluated runtime value.

#### Field-specific interpretation stays above the IR

The structural reader may preserve:

```text
uses: actions/setup-python@v4
with:
  python-version: "3.10"
```

but it should not itself conclude:

```text
Target Python = 3.10
```

That meaning remains in the Target interpreter.

Likewise the structural reader may preserve:

```text
run: pip install -r requirements.txt
```

but it should not itself conclude:

```text
dependency source X is installed
```

The command/dependency relation remains a separate bounded observation/interpretation step.

#### Run blocks remain structural text

A `run` block should remain intact and ordered at this layer. The structural model does not split shell operators, infer virtual-environment activation, prove command ordering inside shell semantics, or classify installation/exercise behavior.

For S004 regression, for example:

```text
. ./regression/bin/activate && pip install -r requirements.txt -r requirements-dev.txt
```

remains visible run content. It does not become a claim that the virtual environment was successfully activated or that installation succeeded.

#### Matrix/container/reusable values are preserved without operational expansion

The initial shared contract should preserve visible matrix/container/reusable-workflow structure enough that consumers know the shape exists and can later inspect it, but it should not:

```text
expand matrix Cartesian products
infer runtime matrix instances
resolve reusable workflows recursively
reconstruct container environments
```

Where the bounded representation cannot yet safely model a structured value, retaining a scoped source fragment/marker plus an explicit limitation is preferable to fabricating a normalized semantic object.

#### Source order is not execution order

Jobs may be kept in source order for determinism and traceability. That order does not imply GitHub runtime scheduling order.

Steps are also kept in source order because later proof questions need causal ordering, but source order alone still does not establish execution/success or environment continuity.

### 11.6 Findings from the raw/normalized contract refinement

#### F-017 — Exact raw source should remain authoritative once, with scoped structural locators below it

The workflow-definition IR should reference the exact `RepositoryTextFile` at its root. Jobs/steps should carry enough structural scope (job key and source indices/order) for downstream facts to materialize exact workflow/job/step provenance without duplicating the entire source evidence contract on every node.

#### F-018 — Dynamic source values are first-class evidence, not unsupported structure

A dynamic `runs-on`, `with` input, or condition is a valid observation that the repository declares a dynamic value. It must not be collapsed with field absence or parser failure.

```text
absent != literal != dynamic
```

This improves on the current tendency of narrow consumers to turn dynamic values directly into local limitations while preserving the fact that domain interpretation may still remain unresolved.

#### F-019 — Normalize provider syntax only; domain meaning stays with CI/Target or a separate factual observation primitive

The IR should normalize visible GitHub Actions structure such as job/step boundaries, source order, fields, literal/dynamic scalar form, and run blocks. It should not recognize setup-python as Target Python evidence or pip syntax as dependency-installation proof merely because those strings appear in the YAML.

This is the core separation:

```text
syntax normalization
!= domain interpretation
```

#### F-020 — The shared contract should be source-recoverable rather than a universal YAML AST

Because exact `RepositoryTextFile` evidence remains attached, the normalized structure does not need to reproduce every YAML feature, comment, whitespace choice, or arbitrary node recursively. Matrix/container/reusable structures may be represented as bounded fragments/markers until a real consumer needs stronger typed structure.

This avoids turning Option B into a generic YAML framework while keeping future extension possible.

#### F-021 — Source order is evidence; scheduling/execution semantics are not

Ordered jobs/steps are useful structural facts. Job source order must not imply runtime scheduling order. Step source order may support later causal checks, but execution, success, and environment continuity still require additional evidence/interpretation.

### 11.7 Parsing/problem boundary — parser-method comparison

The current active readers are both hand-written indentation/text parsers. This was proportionate for their original narrow one-job responsibilities, but Phase B must decide whether that method is credible as the shared structural foundation.

Current runtime dependencies in `pyproject.toml` are only `requests` and `packaging`; adopting a YAML library is therefore a real dependency/method decision rather than reusing an existing project dependency.

#### Method A — retain a hand-written indentation reader

Advantages:

```text
no new dependency
small implementation surface
explicitly bounded behavior
current team/project already understands the mechanism
```

Disadvantages now exposed:

```text
shared owner would gradually reimplement YAML structure
flow-style mappings/sequences are awkward or unsupported
anchors/aliases require more custom semantics
structured values such as runs-on arrays/maps become parser-specific work
current run-block extraction strips indentation/content presentation
consumer limitations can leak into source parsing
continued CI/Target evolution risks another parser fork
```

Conclusion at this checkpoint: still defensible for a narrow consumer, but increasingly weak as the long-lived shared GitHub Actions structural foundation.

#### Method B — parse YAML directly into ordinary Python dict/list/scalars

Advantages:

```text
mature YAML syntax handling
mapping/sequence structure available directly
anchors/aliases can be handled by the YAML implementation
small amount of extraction code for normal mappings
```

Risks:

```text
implicit scalar construction can change source text/type too early
mapping construction can collapse duplicate keys before UpgradePilot evaluates ambiguity
useful source marks/locations may be lost
Python-native values can tempt domain interpretation at the parser layer
GitHub Actions values such as expressions still need explicit preservation rules
```

Conclusion at this checkpoint: better syntax coverage than Method A, but a direct dict/list model is not the strongest evidence-oriented boundary.

#### Method C — YAML syntax parser / node tree → UpgradePilot bounded Actions IR

Conceptual flow:

```text
RepositoryTextFile.content
        ↓
YAML syntax parser / representation nodes
        ↓
scalar / sequence / mapping nodes + source marks
        ↓
UpgradePilot extracts only admitted GitHub Actions fields
        ↓
bounded GitHub Actions IR
```

Advantages:

```text
mature YAML grammar without hand-reimplementing it
source marks support job/step locators and diagnostics
scalar text can be preserved before field-specific interpretation
mapping/sequence kinds are explicit
possible duplicate-key detection before ordinary dict construction
the parser tree is not exposed as the UpgradePilot domain contract
GitHub Actions expressions remain source text rather than being evaluated
```

Costs/risks:

```text
new runtime dependency likely required
library/version behavior becomes part of implementation risk
YAML parser correctness is not GitHub Actions schema correctness
anchors/aliases and merge behavior still need explicit tests
field extraction/schema checks still belong to UpgradePilot
```

Current provisional ranking for the parsing method inside Option B:

```text
1. Method C — YAML node/tree front-end + bounded Actions IR   strongest
2. Method B — YAML to Python mapping/list                     viable but weaker evidence boundary
3. Method A — custom indentation parser                       weakest shared-foundation choice
```

No library has been selected. In particular, choosing this method does not yet choose PyYAML versus `ruamel.yaml` or another parser.

A parser API that exposes representation nodes is attractive because PyYAML, for example, exposes scalar, sequence, and mapping nodes with start/end source marks. A base/failsafe-style loader can also avoid treating generic YAML scalar resolution as UpgradePilot domain meaning. This must be validated before implementation rather than assumed.

#### Current GitHub Actions syntax pressure

Current GitHub documentation materially changes two assumptions from the earlier v0.2 sketch:

1. `runs-on` may be a single string/variable, an array, or a `group`/`labels` mapping. Therefore `runs_on: StaticScalar | None` is too narrow for the shared contract.
2. GitHub Actions supports YAML anchors and aliases. Therefore a long-lived shared parser that only recognizes indentation/text patterns would knowingly reject or mis-handle valid source structure that a real YAML parser can naturally represent.

The IR still does not need to expose a generic recursive YAML AST. It needs a bounded representation that can preserve these admitted field shapes without operationally interpreting them.

### 11.8 Problem/limitation model — provisional separation

Phase B should distinguish at least three levels of failure/uncertainty:

```text
1. STRUCTURAL HARD PROBLEM
   UpgradePilot cannot safely establish the bounded workflow/job/step structure.

2. PRESERVED STRUCTURE + LIMITATION
   source structure is safely represented, but a field/value is dynamic or beyond current typed detail.

3. CONSUMER-LEVEL UNRESOLVED
   shared structure is valid, but CI or Target cannot make its proposition from that structure/evidence.
```

Examples:

```text
invalid/unparseable YAML
→ structural hard problem

root is not a mapping / jobs is not a readable mapping
→ structural hard problem

duplicate job key that prevents stable job identity
→ structural hard problem or explicit ambiguity problem

runs-on: ${{ matrix.platform }}
→ successful preserved dynamic structure, NOT parser failure

matrix exists but is not expanded
→ preserved structure + limitation/marker

reusable-workflow job safely identified
→ preserved job shape; consumer may remain unresolved

CI sees two valid jobs but cannot prove one admitted install→exercise path
→ CI-level unresolved, NOT workflow parse failure
```

A future implementation should prefer **partial preservation only where the preserved facts remain independently trustworthy**. It must not manufacture a complete job or step from a malformed/ambiguous subtree merely to return a partial object.

### 11.9 Findings from parsing/problem analysis

#### F-022 — The original indentation reader was proportionate locally but is not the strongest shared parser foundation

The existing readers were intentionally bounded and conservative for first-slice consumers. The architecture issue is not that they were mistakes; it is that moving the same method into a durable shared GitHub Actions owner would require UpgradePilot to increasingly implement YAML syntax itself as valid workflow variation grows.

#### F-023 — Parse syntax with a mature YAML front-end, but keep UpgradePilot's IR independent

The strongest current parser method is a real YAML syntax/node front-end followed by explicit extraction into the bounded GitHub Actions IR. The YAML parser should not become the public/domain representation and should not evaluate GitHub Actions expressions or CI/Target semantics.

#### F-024 — `runs-on` requires structured-value support in the shared contract

Current GitHub Actions syntax permits more than a scalar `runs-on`. Option B must preserve the allowed structural shapes without interpreting which runner actually executed.

This invalidates an overly narrow `StaticScalar`-only contract for `runs_on` while preserving the broader rule:

```text
static declaration != evaluated runtime runner
```

#### F-025 — Dynamic/unsupported-for-consumer is not the same as structurally unreadable

A workflow may be perfectly readable even when a consumer cannot resolve a matrix expression, reusable workflow, container, or dynamic input. The shared layer should preserve readable structure and let the consumer return unresolved at its own semantic boundary.

#### F-026 — Structural hard failure should be reserved for trust/ambiguity boundaries

Whole-workflow structural failure should be used when parsing or core identity is not trustworthy: unparseable source, unreadable root/jobs mapping, duplicate/ambiguous identities, or a malformed subtree whose partial representation would fabricate facts. Unsupported downstream semantics alone should not cause this state.

#### F-027 — Exact raw source eliminates the need for a round-trip YAML model

Because `RepositoryTextFile.content` remains authoritative, the parser does not need to preserve comments, quote style, or re-emit equivalent YAML. This weakens the case for a heavy round-trip parser solely for formatting fidelity. The selection should optimize safe syntax structure, source marks, predictable scalar handling, and bounded extraction instead.

### 11.10 Edge-case pressure — contract v0.3 refinements

Further pressure against current GitHub Actions syntax and the existing command matchers exposes additional structure that the shared IR should preserve before Option B is compared formally.

#### Bounded structural value

For selected admitted Actions fields, the IR likely needs a provider-scoped structural value capable of the YAML shapes actually used by Actions:

```text
GitHubActionsStaticValue
├─ Scalar(text, literal|dynamic)
├─ Sequence(items...)
└─ Mapping(entries...)
```

This is not a public generic YAML AST. It is an internal IR primitive used only for admitted GitHub Actions fields whose valid source forms require scalar/sequence/mapping structure.

`runs-on` is the strongest current example because GitHub permits a scalar/variable form, an array of labels/expressions, and a group/labels mapping.

#### Updated job shape — still provisional

The current candidate should preserve more than v0.2 originally listed:

```text
JobDefinition
├─ source_index
├─ source_span?                 # diagnostic/trace support, not runtime identity
├─ key
├─ name?
├─ needs?                       # declared prerequisite relationship
├─ runs_on?
├─ if_condition?
├─ continue_on_error?
├─ defaults_run?                # shell / working-directory defaults when visible
├─ strategy / matrix?
├─ container?
├─ reusable_workflow?
└─ steps / scoped JobProblem

StepDefinition
├─ source_index
├─ source_span?
├─ name?
├─ uses?
├─ with_inputs
├─ run_block?
├─ if_condition?
├─ continue_on_error?
├─ shell?
└─ working_directory?
```

`needs` is structural rather than execution proof: it preserves the declared dependency relation between jobs without claiming actual scheduling or shared environment state.

`defaults.run`, step `shell`, and step `working-directory` are preserved because later command/path interpretation depends on their context. The structural layer still does not evaluate shell semantics or resolve a repository path by itself.

#### Run scalar normalization

For `run: |` and `run: >`, YAML scalar decoding belongs to the YAML syntax front-end. The IR may preserve the YAML-decoded scalar text plus source locator/style metadata when useful. It still does not split shell operators or infer execution behavior.

This corrects the current shallow readers, which manually strip block lines and can therefore lose meaningful YAML block-scalar presentation/decoding behavior.

#### Reusable-workflow job variant

A job-level `uses` should be modeled as a recognizable reusable-workflow job shape rather than a malformed normal steps job.

Conceptually:

```text
NormalStepsJob
ReusableWorkflowJob
JobProblem
```

The structural layer may preserve the called-workflow reference and visible inputs while leaving recursive resolution/execution semantics to later work.

#### Partial scoped problems

The preferred provisional problem shape is now:

```text
WorkflowDefinitionResult
├─ WorkflowDefinition
│  ├─ independently trustworthy JobDefinition entries
│  ├─ scoped JobProblem entries where one job cannot be represented safely
│  └─ limitations
└─ WorkflowDefinitionProblem
```

Whole-workflow problems remain for root-level trust/identity failures such as unparseable YAML, unreadable root/jobs mapping, or duplicate job IDs that destroy stable job identity.

A scoped malformed job does not require fabricating a complete job object, but it also need not erase unrelated job structure that remains independently readable. Consumers remain responsible for deciding whether a scoped problem prevents their proposition.

### 11.11 Additional findings from edge-case pressure

#### F-028 — Multi-job preservation without `needs` would lose the principal declared job relationship

Once the shared IR preserves multiple jobs, it should also preserve `needs`. Source order alone is not an adequate representation of job relationship and must not be substituted for declared prerequisite structure.

#### F-029 — Run context is part of correct later dependency-installation observation

The current direct-install matchers compare visible command paths with the known dependency-source path while normalizing slashes and leading `./`. They do not account for effective `working-directory` or shell/default context.

Therefore future shared installation observation should conceptually depend on:

```text
run command
+ effective run working-directory/shell context where material
+ known repository source path
→ bounded direct-installation declaration observation
```

The workflow IR should preserve the context; the later command/dependency interpreter owns its meaning.

#### F-030 — YAML block-scalar decoding is syntax normalization, not shell interpretation

A real YAML parser may decode literal/folded scalar syntax before the IR stores a run block. This increases structural correctness without increasing proof strength. Shell control flow remains outside the YAML/IR layer.

#### F-031 — GitHub Actions job-ID validation should be separate from YAML parsing

The current job-key regex accepts a broader character/starting set than GitHub's documented job-ID grammar. A future shared reader should first parse YAML structure, then apply GitHub-Actions-specific structural validation for job identity.

This reinforces:

```text
YAML syntax validity
!= GitHub Actions structural/schema validity
```

#### F-032 — Duplicate mapping identities must be detected before normal dictionary construction

Stable job identity is evidence-critical. A node/tree parser that exposes mapping pairs before conversion to a normal dictionary provides a credible place to detect duplicate job IDs or duplicate material fields rather than silently allowing last-write/first-write collapse.

#### F-033 — Reusable workflows are a distinct static job shape, not merely unsupported normal jobs

Job-level reusable-workflow `uses` is valid Actions structure and should be preserved as such. CI/Target consumers may still remain unresolved until the called workflow is acquired/interpreted under an admitted method.

#### F-034 — Partial structural preservation is acceptable only for independently trustworthy scopes

A parseable workflow may preserve unaffected jobs while representing one malformed/unmodeled job as a scoped `JobProblem`. This does not assert that GitHub would execute the overall workflow; it preserves only the source facts that remain structurally trustworthy.

### 11.12 Parser-library candidate — not yet selected

The leading concrete implementation experiment is currently a YAML node/composition API with failsafe/base-style scalar handling, followed by UpgradePilot's own bounded Actions extraction.

PyYAML is a plausible first candidate because it exposes scalar/sequence/mapping representation nodes and source marks and supports a base loader that avoids early application-native scalar construction. `ruamel.yaml` remains a credible alternative with stronger YAML 1.2/round-trip capabilities, but round-trip formatting preservation is not itself needed while exact `RepositoryTextFile` source remains authoritative.

No parser dependency is accepted yet. A dependency choice must be pressure-tested against:

```text
GitHub expression preservation
runs-on scalar/sequence/mapping forms
matrix include/exclude
yaml anchors/aliases
literal/folded run blocks
duplicate keys
source marks/alias occurrence behavior
untrusted public YAML safety
version stability / packaging cost
```

### 11.13 Next Option-B substep

The next design block should finalize the **minimum typed IR/problem contract** and parser-front-end candidate sufficiently to run a focused architecture comparison:

1. decide the exact minimum `GitHubActionsStaticValue`/run/defaults/job/step types;
2. decide which fields are typed now versus retained as bounded fragments;
3. decide source-index/source-span semantics, especially for aliases;
4. decide hard workflow problem vs scoped job problem states;
5. decide whether PyYAML node composition is strong enough for the implementation handoff or whether `ruamel.yaml`/another parser offers a material advantage;
6. then compare completed Option B against Options A and C rather than continuing to enrich Option B indefinitely.

No source refactor or dependency addition is authorized yet.