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