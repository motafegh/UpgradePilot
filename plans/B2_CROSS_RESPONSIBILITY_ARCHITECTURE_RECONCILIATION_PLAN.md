# B2 Cross-Responsibility Architecture Reconciliation Plan

**Status:** Approved bounded B2 architecture-reconciliation plan  
**Owner:** Ali Rajabi  
**Parent responsibility:** [`B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md)  
**Parent gate:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Parent route:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)  
**Canonical product-decision semantics:** [`../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)  
**Trust/evidence invariants:** [`../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)  
**Generality control:** [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)  
**Source-ownership baseline:** [`../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md)  
**Whole-system orientation:** [`../proposals/UPGRADEPILOT_MATURE_SYSTEM_HORIZON.md`](../proposals/UPGRADEPILOT_MATURE_SYSTEM_HORIZON.md) — non-controlling  
**Historical structural precedent:** [`B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md`](B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md) and [`../working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md`](../working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md)

## 1. Purpose

Reconcile the **cross-responsibility architecture now exposed by real implemented behavior** before further target-artifact-environment expansion.

The trigger is not aesthetic duplication. Two active responsibilities now consume overlapping GitHub Actions workflow structure with materially different semantic goals:

```text
CI dependency exercise
→ did exact-head CI consume/exercise the changed dependency under the admitted proof rule?

Target artifact environment
→ what environment/configuration facts can an exact workflow/job establish for artifact applicability?
```

The current implementations also expose a proof-strength boundary that must not remain implicit:

```text
workflow definition declares command/path X
!= command/path X executed
!= command/path X succeeded
```

This plan determines the smallest durable ownership/dependency direction justified by current source, tests, two real impact mechanisms, and the B2/mature-system horizon. It does **not** pre-authorize a refactor, ADR, universal workflow model, or new target capability.

## 2. Why this checkpoint is justified now

The selected B2 foundation plan deliberately requires materially different implementation pressure before architecture is treated as stable.

That pressure now exists:

1. the Python-support-drop mechanism implements one candidate/applicability/investigation path;
2. artifact serviceability implements a materially different package-artifact mechanism and exact target-wheel-compatibility evaluator;
3. target artifact-environment Increment 1 introduced a second consumer of GitHub Actions workflow definitions;
4. `src/upgradepilot/ci/workflow_commands.py` and `src/upgradepilot/target/artifact_environment.py` independently perform overlapping job/run/pip/requirements parsing;
5. the CI side already distinguishes static workflow text from successful run/job evidence, while target-environment naming currently risks treating static configuration as stronger runtime formation evidence;
6. `PublicPullRequestInvestigation` remains shaped around the first mechanism, while a real second mechanism now creates credible orchestration pressure.

This satisfies the project rule:

```text
second materially different consumer / mechanism
→ compare actual responsibilities
→ extract only demonstrated sameness
→ keep real semantic differences separate
```

## 3. Governing architecture principles

The reconciliation must preserve these rules.

### 3.1 Share meaning, not merely syntax

A shared primitive is justified only when its meaning is genuinely identical across callers.

```text
same raw syntax
!= same domain conclusion
```

A common source-structure reader may be shared while CI and Target interpretations remain separate.

### 3.2 Separate acquisition, normalized structure, interpretation, and decision

Where the source supports it, preserve this conceptual layering:

```text
exact source acquisition / identity
→ bounded normalized source structure
→ responsibility-specific interpretation
→ proposition/evidence state
→ impact/applicability/investigation
```

Do not create layers merely for diagram symmetry. A layer must own a real stable responsibility.

### 3.3 Preserve proof strength

Static declaration/configuration evidence must not silently become runtime execution or success evidence.

Runtime run/job/step evidence must not become complete behavioral coverage merely because a job succeeded.

### 3.4 Preserve scope

Repository, immutable revision, workflow path, job, and where material step/run identity must remain attributable. Facts from distinct environments/scopes must not be unioned into a synthetic environment without proposition-specific justification.

### 3.5 No universal framework by anticipation

Do not introduce generic `common`, `utils`, services, plugin registries, workflow execution engines, universal environment reconstructors, provenance graphs, impact engines, or general planners merely because future breadth is imaginable.

## 4. Required inspection surface

Inspect these active responsibilities together, not as isolated files:

```text
src/upgradepilot/github/actions.py
src/upgradepilot/github/repository.py

src/upgradepilot/ci/workflow_commands.py
src/upgradepilot/ci/dependency_exercise.py

src/upgradepilot/target/artifact_environment.py
src/upgradepilot/target/python.py
src/upgradepilot/target/relevance.py

src/upgradepilot/impact/applicability.py
src/upgradepilot/impact/python_support.py
src/upgradepilot/impact/artifact_serviceability.py

src/upgradepilot/investigation.py
```

Inspect the focused/nearest active tests for each responsibility and any exact source/provenance contracts they depend on.

Use historical source-structure reconciliation records only as precedent for ownership rules; do not treat their old migration map as the current target architecture.

Use S001, S008, S011 and the existing transfer anchors only where they discriminate a concrete architecture/proof question. Do not turn this checkpoint into another simulation campaign.

## 5. Question set A — GitHub Actions source structure

Determine what the exact workflow-definition boundary should own independently of CI or Target semantics.

Questions:

1. Which workflow properties are already parsed more than once?
2. Which of those properties have identical structural meaning across consumers?
3. Should a bounded normalized workflow representation preserve:
   - workflow source identity/provenance;
   - ordered job definitions;
   - literal/dynamic `runs-on` form;
   - ordered steps;
   - `uses`;
   - `with` inputs;
   - `run` blocks;
   - condition presence/raw condition;
   - `continue-on-error` presence;
   - matrix/container/reusable-workflow presence even when unsupported downstream?
4. Which fields would be speculative and should remain raw/unmodeled?
5. Should the structural reader preserve multiple jobs even when a specific consumer cannot safely select among them?

Target principle:

```text
structural reader may preserve richer visible structure
while domain consumer may still return unresolved/unsupported
```

## 6. Question set B — static definition versus runtime execution

Map the evidence ladder explicitly:

```text
STATIC WORKFLOW DEFINITION
what repository configuration declares

RUNTIME WORKFLOW RUN
what exact revision/event produced a run

RUNTIME JOB
what job instance executed / concluded

RUNTIME STEP
what step instance executed / concluded, where observable

LOG / ARTIFACT EVIDENCE
what command/output/result can be attributed, where admitted
```

For every current or proposed proposition, identify the minimum proof class it actually requires.

In particular, determine whether target-artifact-environment state names should distinguish:

```text
direct installation declared/configured
installation observed/executed
installation succeeded
```

Do not rename contracts during the audit itself. Record the required semantic correction first.

## 7. Question set C — CI-specific versus Target-specific meaning

### CI must continue to own questions such as

```text
successful exact-head run/job authority
changed dependency consumed
changed package directly invoked/exercised under the admitted method
CI exercise sufficiency / insufficiency / unresolved
```

### Target must continue to own questions such as

```text
scoped environment/configuration facts
runner/platform declaration
Python declaration
changed dependency environment/configuration relation
exact target-wheel compatibility evidence or insufficiency
```

Determine what inputs can be shared without allowing one domain's proof semantics to leak into the other.

Reject an architecture where `target` imports CI-specific conclusions merely because CI currently has a workflow parser.

## 8. Question set D — dependency installation recognition

Compare the duplicated handling of visible direct installation commands.

Determine whether there is a genuinely shared primitive such as:

```text
static command/step
+
normalized dependency-source path
→ direct installation declaration observation
```

If admitted, its contract must be explicit about what it does **not** prove:

```text
declaration observed
!= executed
!= succeeded
!= affected package exercised
```

Determine the precise owner. Do not move it into `dependency/`, `github/`, or another package solely because that folder is convenient; ownership must follow semantic responsibility.

## 9. Question set E — multiple jobs, matrices, reusable workflows, containers

Do not decide that all forms must be supported.

Instead determine two separate boundaries:

```text
what normalized source structure can safely preserve?
```

versus:

```text
what can a current CI/Target interpreter safely conclude?
```

The structural layer should not necessarily reject a workflow merely because a downstream consumer lacks an interpretation method.

For each currently unsupported shape, decide one of:

- preserve structurally, consumer unresolved;
- preserve marker/raw form, consumer unresolved;
- structurally unsupported because safe bounded parsing is not credible yet.

## 10. Question set F — provenance and evidence contracts

Verify that any proposed shared source structure retains or references enough provenance for downstream claims:

```text
repository
immutable revision
requested/returned workflow path
workflow blob SHA
retrieval identity/time where required
job key/scope
step identity/order where material
runtime run/job/step identity when execution evidence participates
```

Do not collapse exact source evidence and interpreted facts into one object if that erases transformation boundaries.

## 11. Question set G — heterogeneous impact orchestration

Inspect `PublicPullRequestInvestigation` and the current two mechanism families.

Determine whether real pressure now justifies a small typed orchestration boundary for:

```text
zero or more mechanism-specific analysis/results
```

without replacing mechanism-specific contracts with an opaque universal impact object.

Questions:

1. Which fields are truly common across Python-support and artifact-serviceability results?
2. Is a common envelope/result collection sufficient?
3. Should each mechanism retain its own candidate/evidence/evaluator types?
4. How should later synthesis consume heterogeneous technical states without one scalar score?
5. What should remain direct orchestration until a third responsibility proves more generality is needed?

## 12. Question set H — dependency direction

Produce an explicit proposed dependency direction for the affected packages.

At minimum evaluate:

```text
github acquisition / normalized workflow structure
        ↓
ci interpretation      target interpretation
        ↓                    ↓
ci evidence           target evidence
        \                    /
         mechanism-specific impact
                  ↓
            applicability
                  ↓
           investigation/orchestration
```

The final direction may differ if source inspection disproves this shape.

Reject circular ownership and domain inversion such as Target depending on CI merely to reuse syntax parsing.

## 13. Question set I — horizon pressure versus current admission

Use the Mature System Horizon and current route to classify foreseeable needs into:

```text
SHAPES ARCHITECTURE NOW
already evidenced by active consumers / B2 gate

KEEP COMPATIBLE WITH
credible near-term responsibility; avoid blocking it but do not implement it

IGNORE FOR CURRENT ARCHITECTURE
speculative/open/experimental breadth
```

This classification is required so “future awareness” does not become speculative framework design.

## 14. Reconciliation execution sequence

### Phase A — baseline and source map

1. Record exact repository baseline in dated working-memory.
2. Inspect the required source/test surface.
3. Draw current dependency/data-flow map.
4. Enumerate actual duplication and proof-strength mismatches with exact source owners.
5. Separate semantic duplication from syntactic similarity.

No source edits.

### Phase B — candidate architecture options

Produce at least the simplest credible options, for example:

```text
Option 1 — keep local parsers; repair semantics only
Option 2 — shared bounded workflow-definition structure + separate interpreters
Option 3 — broader normalized Actions evidence model
```

Do not force these exact options if source inspection suggests better alternatives.

For each option assess:

- ownership clarity;
- proof-strength correctness;
- duplication removed/retained;
- effect on current tests;
- compatibility with B2/mature horizon;
- expansion cliff;
- risk of premature generalization;
- migration cost and reversibility.

### Phase C — transfer/adversarial check

Pressure the leading option against at least:

- S008 — static workflow plus separate Python-3.6 repository context must not manufacture one exact environment;
- S011 — macOS/Python/CI presence must not imply MLX optional environment formation;
- existing CI exercise cases — static command text must not replace successful exact-head runtime proof;
- multi-job workflow shape — structural preservation and consumer interpretation must remain distinct;
- both impact mechanisms — orchestration must carry heterogeneous state without erasing mechanism semantics.

### Phase D — decision classification

Classify each accepted conclusion by repository owner:

- framework-independent semantic invariant → specification update only if not already covered;
- consequential structural/method choice → new ADR or explicit amendment/supersession of an existing ADR;
- bounded implementation sequence → refactor/implementation plan;
- dated rationale/evidence → working-memory;
- live continuation → `MEMORY.md`.

Do not create an ADR simply because this plan exists.

### Phase E — implementation handoff

Only after the architecture decision is accepted:

1. define the smallest coherent refactor/contract migration;
2. define exact test/proof obligations;
3. decide whether target-environment naming/semantics must be migrated;
4. decide how CI tests protect runtime proof strength;
5. decide how/when artifact serviceability joins `investigation.py`;
6. update live continuation;
7. then begin source edits.

## 15. Required outputs

The reconciliation is complete only when we have:

1. **Current architecture/data-flow map** across GitHub Actions, CI, Target, Impact, and orchestration.
2. **Duplication inventory** distinguishing identical semantic primitives from merely similar syntax.
3. **Proof-strength map** for static definition, runtime run/job/step, and downstream propositions.
4. **Selected ownership/dependency direction** with rejected credible alternatives and reasons.
5. **Decision on shared workflow structure** — admit, defer, or reject.
6. **Decision on installation-recognition ownership** — admit, defer, or reject.
7. **Decision on multi-job structural preservation versus consumer support.**
8. **Decision on heterogeneous impact orchestration boundary.**
9. **Explicit future-pressure classification**: shapes now / keep compatible / ignore now.
10. **ADR disposition**: new ADR, amendment/supersession, or no ADR required.
11. **Bounded implementation/refactor handoff plan** if source changes are justified.
12. **Dated working-memory record** preserving detailed evidence/rationale.
13. **`MEMORY.md` synchronization** to the selected continuation.

## 16. Non-goals

This reconciliation does not itself implement:

- exact wheel-tag derivation from broad runner/Python labels;
- universal repository environment reconstruction;
- full GitHub Actions expression semantics;
- arbitrary matrix expansion;
- reusable-workflow execution semantics;
- container/deployment environment unification;
- shell execution interpretation;
- generic CI-provider abstraction;
- source-build success reasoning;
- a universal impact mechanism interface;
- a universal investigation planner;
- final maintainer synthesis/recommendation;
- target repository mutation;
- new simulation cases unless existing anchors cannot discriminate an exposed decision.

## 17. Validation/proof discipline

This plan is initially inspection/design work. Documentation/architecture decisions do not prove runtime behavior.

If/when a later refactor is authorized, validate in clusters:

```text
focused tests for changed shared primitive/contract
+
focused CI tests
+
focused Target tests
+
impact/orchestration tests where touched
+
package/import smoke where ownership moves
+
complete active product suite
```

Use safe live read-only proof only when the changed claim depends on live GitHub behavior.

## 18. Stop line

Stop this reconciliation when the required outputs above are complete and the repository has one explicit, evidence-backed architecture direction for the exposed cross-responsibility seams.

Do **not** continue into source refactoring merely because the design decision is clear. The source change must proceed under the resulting bounded implementation/refactor handoff and its own validation obligations.

Successful completion does not mean the architecture is final for the mature product. It means the present B2 implementation has been reconciled against the real responsibilities already visible and the next source change can proceed without knowingly duplicating or inflating those boundaries.

## 19. Maintenance

Change this plan only when the architecture-reconciliation question set, required inspection surface, outputs, proof obligations, or stop line changes.

Do not record live progress, latest commits, current blockers, or immediate continuation here. Those belong only in `../MEMORY.md`.