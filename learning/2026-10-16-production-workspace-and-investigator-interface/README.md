# Production Workspace and Investigator evidence interface — learning package

**Educational snapshot:** **2026-10-16**, repository horizon **`5187f40ba974341eb29d765363f093922a881803`**.

**Implementation horizon inside this snapshot:** the production Workspace/native/host/source-interface source and tests are unchanged from their verified implementation horizons; later commits through `5187f40` add current input-retention/qualification evidence, plans and prepared future-cycle records without changing `src/` or `tests/`.

**Purpose:** provide one current production relearning route for UpgradePilot's canonical Workspace foundation, lifecycle/authority host, bounded Investigator-facing evidence interface and the still-in-progress migration from `PublicPullRequestInvestigation` consumers.

This package is educational material. It does **not** select the live project continuation, authorize implementation/model execution, or prove learner mastery. `MEMORY.md` alone owns live position.

## Read in this order

| Note | What you should be able to reason about afterward |
| --- | --- |
| [1. Native capture, reconstruction and checkpoint publication](01_native_capture_reconstruction_and_checkpoint_publication.md) | Explain how domain-owned native facts are captured with their actual inputs, reconstructed without reevaluation and published/recovered through immutable SQLite-backed Workspace revisions; distinguish recovery integrity from semantic truth/current authority. |
| [2. Lifecycle host, material validity and execution truth](02_lifecycle_host_material_validity_and_execution_truth.md) | Distinguish original basis, current material validity, current execution authority and publication predecessor; trace intent-before-effect, observation/interruption, native reassessment and historical recovery without automatic retry/continuation. |
| [3. Frozen sources, native views, delivery and citations](03_frozen_sources_native_views_delivery_and_citations.md) | Trace shared dependency/CI preparation into frozen source/native consumer access; distinguish source availability, actual delivery, citation, evaluated support and action permission; explain the common-freeze/profile-versus-checkpoint boundary using the HTTPX/glyphsLib cases. |
| [4. Current product flow and Workspace migration status](04_current_product_flow_and_workspace_migration_status.md) | Explain the real transitional architecture: canonical Workspace state is produced on the normal path while synthesis/report/CLI still consume the legacy result; identify completed Stages 1–3, remaining Stages 4–6 and the prepared-but-unstarted future Investigator adapter boundary. |

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
CURRENT MIGRATION FRONTIER
legacy synthesis/report/CLI consumers remain until direct Workspace-native parity/cutover
```

Across the whole package, preserve this authority ladder:

```text
source/native material exists
!= delivered
!= observably used
!= cited
!= evaluated support
!= sufficient investigation
!= maintainer action permission
```

## Authority map

These notes summarize rather than replace the real owners.

- [ADR-0012 — canonical Investigation Workspace and recovery boundary](../../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md) owns the canonical Workspace/recovery architecture.
- [ADR-0013 — versioned native reconstruction and Workspace checkpoint storage](../../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md) owns explicit native codecs, immutable revisions and the SQLite checkpoint method/limits.
- [Core Pipeline and Contract Specification](../../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) owns evidence/trust/recovery/continuation invariants.
- [Product Decision Model](../../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) owns proposition/applicability/material-validity/adequacy distinctions.
- [Maintainer Action Synthesis Specification](../../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md) owns action permission; richer Workspace retention does not strengthen actions by itself.
- [Workspace implementation and migration plan](../../plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md) owns the six-stage execution/migration sequence and proof gates.
- Production source/tests at this pinned horizon establish implemented behavior.
- Dated working-memory/evidence records explain implementation progression, failures, corrections and proof boundaries; they do not override current source/accepted owners.

## Relationship to the Oct 9 research package

The frozen [2026-10-09 Workspace implementation-architecture research package](../2026-10-09-workspace-implementation-architecture-research/README.md) remains valuable and should not be rewritten.

Use the horizons differently:

```text
Oct 9 research package
→ Why were immutable revisions, SQLite storage, typed interaction seams
  and direct migration recommended?
→ Which alternatives/negative controls shaped the method?

Oct 16 production package
→ What did UpgradePilot actually implement?
→ What does current proof establish/refuse?
→ How does the real normal path use Workspace/host/source interfaces?
→ What migration work remains?
```

At the Oct 9 horizon, the research package correctly states that its mechanisms are experimental and not production adoption. Production implementation happened afterward. Keeping both snapshots intact preserves the engineering progression instead of rewriting history.

## Current snapshot boundary

At `5187f40...`:

```text
production Workspace Stages 1–3            implemented/proven at admitted scope
common dependency/CI + source/native access implemented/proven
new Oct 16 shared input freeze               qualified and retained
PublicPullRequestInvestigation               still transitional consumer surface
synthesis/report/CLI direct Workspace cutover not complete
user-facing Workspace continuation/replay    not implemented
future Investigator adapter cycle            PREPARED — NOT STARTED
model comparison/usefulness result            not established
```

Do not read the existence of the future integration plan or prepared cycle record as implementation evidence.

## Fast return route

If you return after several weeks, do not reread the entire package first.

1. Recreate the architecture from memory: **native owner → capture → Workspace/checkpoint → lifecycle host → source/native consumer access → transitional legacy consumers**.
2. Read the core mental model at the top of each note.
3. Open only these code anchors:
   - `workspace/native_capture.py` + `workspace/native_projection.py`;
   - `workspace/lifecycle_host.py` + `workspace/material_validity.py`;
   - `workspace/source_access.py` + `workspace/consumer_access.py`;
   - `investigation.py` + `maintainer_action.py` + `report_projection.py` + `cli.py`.
4. Inspect one proof anchor from each responsibility: durable checkpoint reconstruction, host integration, consumer access, then the current migration plan.
5. Answer at least one transfer question from each note before treating the mechanism as refreshed.

## Proof and non-proof summary

The package's current evidence supports:

```text
bounded native capture and cold reconstruction
immutable local checkpoint publication/backup
retained lifecycle/execution distinctions
current material-validity versus authority separation
bounded frozen raw-source/native delivery and citation provenance
real HTTPX/glyphsLib common-input qualification
normal-path production Workspace publication
```

It does not establish:

```text
complete native-family migration
direct Workspace-native synthesis/report/CLI cutover
user-facing continuation or replay
exactly-once external effects or power-loss durability
generic semantic/adequacy competence
positive maintainer action permission
Investigator usefulness or structured-interface superiority
```

Those remain separately owned responsibilities.

## Snapshot integrity

All implementation/source links in these notes pin the same repository horizon `5187f40...`. Historical proof counts are labelled with their actual tested implementation horizons where needed rather than being presented as reruns on October 16.

If later production implementation materially changes these responsibilities, preserve this package as the October 16 educational snapshot and create/revise an explicitly newer current learning artifact as justified. Do not silently refresh this frozen package with mutable future source.

`UP-SKILL:upgradepilot-learning-artifact`
