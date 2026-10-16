# Production Workspace and Investigator evidence interface — learning package

**Educational package date:** **2026-10-16**.

**Product-foundation snapshot:** **`5187f40ba974341eb29d765363f093922a881803`** for Notes 1–4.

**Mechanical-adapter extension:** **`4545d5f0b8717fb58c91e2a470aee5367b8d6846`** for Note 5.

The production `src/` and normal `tests/` responsibilities taught in Notes 1–4 are unchanged across those horizons. The later horizon adds an **experiment-owned Investigator adapter/trial/qualification layer** plus its evidence and lifecycle handoff; it does not replace the production Workspace or complete synthesis/report/CLI migration.

**Purpose:** provide one relearning route from UpgradePilot's canonical Workspace foundation through the bounded Investigator evidence interface and into the now-implemented model-free Investigator mechanical bridge, while preserving the still-in-progress migration from `PublicPullRequestInvestigation` consumers.

This package is educational material. It does **not** select live continuation, authorize model inference, or prove learner mastery. `MEMORY.md` alone owns live position.

## Read in this order

| Note | Snapshot | What you should be able to reason about afterward |
| --- | --- | --- |
| [1. Native capture, reconstruction and checkpoint publication](01_native_capture_reconstruction_and_checkpoint_publication.md) | `5187f40...` | Explain how domain-owned native facts are captured with their actual inputs, reconstructed without reevaluation and published/recovered through immutable SQLite-backed Workspace revisions; distinguish recovery integrity from semantic truth/current authority. |
| [2. Lifecycle host, material validity and execution truth](02_lifecycle_host_material_validity_and_execution_truth.md) | `5187f40...` | Distinguish original basis, current material validity, current execution authority and publication predecessor; trace intent-before-effect, observation/interruption, native reassessment and historical recovery without automatic retry/continuation. |
| [3. Frozen sources, native views, delivery and citations](03_frozen_sources_native_views_delivery_and_citations.md) | `5187f40...` | Trace shared dependency/CI preparation into frozen source/native consumer access; distinguish source availability, actual delivery, citation, evaluated support and action permission; explain the common-freeze/profile-versus-checkpoint boundary using HTTPX/glyphsLib. |
| [4. Current product flow and Workspace migration status](04_current_product_flow_and_workspace_migration_status.md) | `5187f40...` | Explain the transitional product architecture: canonical Workspace state is produced on the normal path while synthesis/report/CLI still consume the legacy result; identify completed Stages 1–3 and remaining Stages 4–6. Its adapter-status paragraph is historical at this snapshot and is extended by Note 5. |
| [5. Investigator adapter mechanical contract, packing and qualification](05_investigator_adapter_mechanical_contract_packing_and_qualification.md) | `4545d5f0...` | Explain the implemented experiment bridge: fresh assignment isolation, raw/structured treatment restriction, strict request/reference mapping, whole-event packing and consumer visibility, conservative versus actual accounting, model-free qualification and the still-unqualified deployment/model boundary. |

## One mental model for the package

```text
DOMAIN / NATIVE OWNERS
own bounded semantic facts
        ↓
NATIVE CAPTURE + VERSIONED RECONSTRUCTION
preserve exact historical owner results and material inputs
        ↓
CANONICAL WORKSPACE REVISION + CHECKPOINT
own immutable composition, history and recovery
        ↓
LIFECYCLE HOST
owns present capability admission, execution truth and current material validity
        ↓
FROZEN SOURCE + STRUCTURED NATIVE CONSUMER ACCESS
owns bounded delivery/reference/accounting, not semantic truth
        ↓
EXPERIMENT-OWNED INVESTIGATOR ADAPTER
owns strict tool/reference mapping, assignment isolation and laboratory attribution
        ↓
TRIAL PACKING + ACCOUNTING
owns actual consumer-visible whole events, resource admission and protocol freeze
        ↓
CURRENT FRONTIERS
model/deployment qualification + later semantic comparison
AND
legacy synthesis/report/CLI migration Stages 4–6
```

Across the whole package, preserve this ladder:

```text
source/native material exists
!= product delivery
!= experiment event retained
!= consumer-visible packed input
!= cited
!= evaluated support
!= sufficient investigation
!= maintainer action permission
```

## Authority map

These notes summarize rather than replace the real owners.

- [ADR-0012 — canonical Investigation Workspace and recovery boundary](../../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md) owns the canonical Workspace/recovery architecture.
- [ADR-0013 — versioned native reconstruction and Workspace checkpoint storage](../../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md) owns explicit native codecs, immutable revisions and SQLite checkpoint semantics/limits.
- [Core Pipeline and Contract Specification](../../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) owns evidence/trust/recovery/continuation invariants.
- [Product Decision Model](../../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) owns proposition/applicability/material-validity/adequacy distinctions.
- [Maintainer Action Synthesis Specification](../../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md) owns action permission; richer Workspace/experiment evidence does not strengthen an action by itself.
- [Workspace implementation and migration plan](../../plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md) owns the six-stage product migration and proof gates.
- [Investigator Integration and Comparative Evaluation Plan](../../plans/INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md) owns the experiment bridge, deployment qualification and later comparison sequence.
- Production source/tests establish product behavior; `experiments/` source plus its focused proof establishes only the experiment layer's bounded behavior.
- Dated working-memory/evidence records explain engineering progression and proof boundaries; they do not override accepted owners or current source.

## Relationship to the Oct 9 research package

The frozen [2026-10-09 Workspace implementation-architecture research package](../2026-10-09-workspace-implementation-architecture-research/README.md) remains valuable and should not be rewritten.

Use the horizons differently:

```text
Oct 9 research package
→ Why were immutable revisions, SQLite storage, typed interaction seams
  and direct migration recommended?
→ Which alternatives/negative controls shaped the method?

Oct 16 production package, Notes 1–4
→ What did UpgradePilot actually implement in product Workspace/host/access?
→ What does production proof establish/refuse?
→ What migration work remains?

Oct 16 adapter extension, Note 5
→ How does the experiment now consume the real product seam?
→ How are references, packing, visibility and accounting controlled before inference?
→ What is still unqualified before a model can be trusted as an experiment participant?
```

The historical research Workspace is not reintroduced as product machinery by the adapter. The new adapter intentionally consumes the real product host/source/native contracts.

## Current package boundary at the latest extension horizon

At `4545d5f0...`:

```text
production Workspace Stages 1–3             implemented/proven at admitted scope
common dependency/CI + source/native access  implemented/proven
Oct 16 shared input freeze                    qualified and retained
PublicPullRequestInvestigation                still transitional consumer surface
synthesis/report/CLI direct Workspace cutover not complete
user-facing Workspace continuation/replay     not implemented
Investigator adapter B                        DONE
adapter scoped mechanical Verification        GREEN
adapter D                                      CURRENT
adapter E                                      PENDING
model load/inference                           not performed by this adapter proof
semantic raw-vs-structured comparison          not performed
maintainer usefulness result                   not established
```

The newer adapter result changes the old `5187f40` status **“prepared — not started”**. It does not change the product Workspace Stages 1–3 mechanisms taught in Notes 1–4.

Ali selected parallel progression after the mechanical gate:

```text
adapter D/E learning and closure
        ||
Deployment & Model-Interface Qualification successor entry
```

A material D/E contradiction must still block affected later inference/qualification.

## Fast return route

If you return after several weeks, do not reread the whole package first.

1. Recreate the ownership chain: **native owner → capture → Workspace/checkpoint → lifecycle host → source/native access → experiment adapter → trial packing/accounting**.
2. Read the core mental model at the top of Notes 1, 2, 3 and 5.
3. Open only these implementation anchors:
   - `workspace/native_capture.py` + `workspace/native_projection.py`;
   - `workspace/lifecycle_host.py` + `workspace/material_validity.py`;
   - `workspace/source_access.py` + `workspace/consumer_access.py`;
   - `experiments/investigator_workspace_adapter.py` + `experiments/investigator_workspace_trial.py`.
4. Inspect one proof anchor per layer: durable checkpoint reconstruction, host integration, consumer access, then the adapter mechanical qualification/verification summaries.
5. Read Note 4 only to refresh the product migration frontier and legacy-consumer coexistence.
6. Answer at least one transfer question from each note you needed before treating the mechanism as refreshed.

## Proof and non-proof summary

The package's evidence supports:

```text
bounded native capture and cold reconstruction
immutable local checkpoint publication/backup
retained lifecycle/execution distinctions
current material-validity versus authority separation
bounded frozen raw-source/native delivery and citation provenance
real HTTPX/glyphsLib common-input qualification
normal-path production Workspace publication
fresh experiment assignment isolation
raw-versus-structured treatment restriction over common retained inputs
strict model-shaped request/reference validation
whole-event packing with explicit omissions
consumer-input visibility tracking
mechanical accounting/refusal/failure distinctions
model-free HTTPX/glyphsLib adapter qualification
```

It does not establish:

```text
complete native-family migration
direct Workspace-native synthesis/report/CLI cutover
user-facing continuation or replay
exactly-once external effects or power-loss durability
generic semantic/adequacy competence
positive maintainer action permission
model transport/runtime/template correctness
model fit/speed/context adequacy
raw-versus-structured semantic advantage
maintainer usefulness
```

Those remain separately owned responsibilities.

## Snapshot integrity

This package now has **two explicit, non-conflicting horizons**:

```text
Notes 1–4  → 5187f40... product-foundation snapshot
Note 5     → 4545d5f0... experiment-adapter extension
```

Product `src/` and normal `tests/` did not change between them. The later horizon adds experiment/planning/evidence files, so the package extends rather than silently rewrites the product snapshot.

Historical proof counts remain labelled by their actual proof horizons. If production implementation later changes the core responsibilities, create/revise a newer learning snapshot rather than pretending this package already covers that source change.

`UP-SKILL:upgradepilot-learning-artifact`
