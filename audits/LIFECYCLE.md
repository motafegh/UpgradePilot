# Audit Lifecycle

Audit records are durable non-controlling review evidence. Lifecycle state is tracked through the four index folders below:

```text
audits/active/     validated findings selected as inputs to current engineering work
audits/scheduled/  validated findings explicitly selected for a concrete future trigger/plan
audits/deferred/   validated findings/opportunities not selected or scheduled for current work
audits/absorbed/   findings whose material conclusions have been incorporated into stronger owners
```

## Stable canonical audit paths

Existing canonical audit files remain directly under `audits/`.

Reason: those records contain repository-relative references written from the `audits/` root. Physically relocating them without rewriting every reference would silently damage reproducibility and navigation. The lifecycle folders therefore act as **status/index owners**, with lifecycle-prefixed link titles such as `ACTIVE — AUDIT-007` or `SCHEDULED — AUDIT-005`.

For new audits, prefer the same stable canonical location unless the repository later adopts a fully rewritten path-independent linking convention. Do not duplicate full audit content across lifecycle folders.

## Lifecycle movement

Changing lifecycle means:

1. preserve the canonical audit ID/file;
2. remove its entry from the old lifecycle index;
3. add it to the new lifecycle index with the new lifecycle title;
4. ensure the owning plan/`MEMORY.md` reflects any change in live execution responsibility.

Lifecycle reclassification does not itself modify product behavior, specifications, ADRs, plans, or source.

### Active

Use `active` when the validated finding is a selected input to the **current** engineering responsibility.

### Scheduled

Use `scheduled` when all of the following are true:

```text
validated finding/opportunity
+ explicit project selection
+ concrete prerequisite / activation trigger
+ named owning execution plan
+ defined handoff point
```

Scheduled is intentionally stronger than deferred. Once its trigger is satisfied, the project must either enter the owning checkpoint/plan or record an explicit reject/defer/reschedule decision. It must not be silently bypassed by a newer ordinary continuation.

Scheduling does not mean implementation has already begun, and it does not make the audit itself controlling authority. `MEMORY.md` still owns live activation.

### Deferred

Use `deferred` for valid findings/opportunities that are not selected for current work and have no committed activation point. Deferred audits should be re-entered only on a concrete trigger or explicit selection.

### Absorbed

Use `absorbed` when stronger accepted owners or completed work have materially incorporated the audit's conclusions such that the audit no longer needs to remain an open engineering input.
