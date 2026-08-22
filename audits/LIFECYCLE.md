# Audit Lifecycle

Audit records are durable non-controlling review evidence. Lifecycle state is tracked through the three index folders below:

```text
audits/active/    validated findings selected as inputs to current engineering work
audits/deferred/  validated findings/opportunities not selected for current work
audits/absorbed/  findings whose material conclusions have been incorporated into stronger owners
```

## Stable canonical audit paths

Existing canonical audit files remain directly under `audits/`.

Reason: those records contain repository-relative references written from the `audits/` root. Physically relocating them without rewriting every reference would silently damage reproducibility and navigation. The lifecycle folders therefore act as **status/index owners**, with lifecycle-prefixed link titles such as `ACTIVE — AUDIT-007`.

For new audits, prefer the same stable canonical location unless the repository later adopts a fully rewritten path-independent linking convention. Do not duplicate full audit content across lifecycle folders.

## Lifecycle movement

Changing lifecycle means:

1. preserve the canonical audit ID/file;
2. remove its entry from the old lifecycle index;
3. add it to the new lifecycle index with the new lifecycle title;
4. ensure the owning plan/`MEMORY.md` reflects any change in live execution responsibility.

Lifecycle reclassification does not itself modify product behavior, specifications, ADRs, plans, or source.

When an audit becomes absorbed, the stronger owner or completed work should make the disposition clear. Deferred audits should be re-entered only on a concrete trigger or explicit selection.
