# ADR-0013 — Versioned native reconstruction and Workspace checkpoint storage

**Status:** Accepted by Ali with the stated support/refusal and durability limits on 2026-10-10. Production implementation requires separate activation and proof.
**Date:** 2026-10-09
**Accepted:** 2026-10-10
**Responsibility:** Preserve native owner meanings across cold Workspace restoration through explicit versioned codecs and coherent local checkpoint publication.
**Requirements:** [Core §§3–6.4](../specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md), [ADR-0012](ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md), [native semantic ownership](ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md), [source-association boundary](ADR-0011-explicit-source-association-bases-and-proposal-boundary.md), [Security](../../SECURITY.md).
**Execution/proof:** [Workspace implementation and migration plan](../../plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md).
**Evidence:** [revision research](../../working-memory/evidence/2026-10-08-workspace-revision-representation/README.md), [storage research](../../working-memory/evidence/2026-10-08-workspace-checkpoint-stores/README.md), [public grounding](../../working-memory/evidence/2026-10-08-workspace-experiment3-grounding/README.md), [migration research](../../working-memory/evidence/2026-10-09-workspace-replacement-migration/README.md).
**Decision provenance:** [planning-cycle result review and closure](../../working-memory/2026-10-09_2045_workspace-implementation-and-usefulness-planning_lbd-cycle.md). Method adoption does not establish implementation or learner mastery.

## Context and decision

The research restores opaque bytes, but its migration projection still needs producer-captured live Python values. Input-tape re-execution can reproduce a native result; it cannot satisfy offline restoration without running producers/evaluators again. A saved report omits native inputs/history and cannot supply this boundary. Production needs an explicit reconstruction method instead of arbitrary class-tag hydration or a cache whose contents disappear at restart.

Use immutable published Workspace revisions sharing immutable native payloads. Capture inputs and results at the earliest sufficient native/composition boundary, before orchestration discards material local values. Keep native meaning with its domain owner and lifecycle/reference validation with the Workspace. Implement the following one-way path:

```text
admitted producer input/result + actual method/source bindings
→ owner-specific versioned encoding + immutable capture envelope
→ coherent Workspace revision/checkpoint
→ offline storage/envelope/reference validation
→ explicit supported owner codec reconstruction
→ native consumer projection with historical identity/basis
```

### Native codec and authority boundary

Each supported family has explicit encode/decode functions and a fixed type/version table. The table identifies supported success, problem, absent/not-evaluated and nested variants. Preserve declared order, exact version strings/text, optionality and unknowns where they carry meaning. Internal Python module/class paths are not persisted dispatch authority. A shared scalar/reference helper is justified only for identical encoding responsibilities; it does not discover dataclass fields or become a universal evidence evaluator.

The immutable envelope associates record ID, native family/owner, codec version, exact source/target scope, available producer/method version and material input references with the payload. Content digests serve corruption detection/deduplication; they do not replace scoped record identity or authenticate a source. Host annotation and later assessment remain separate records referring to the original capture. Missing method/source provenance is an explicit gap, never a guessed current value.

Decoding performs non-executing bounded parsing, fixed variant/type checks and owner-specific representation validation; Workspace reconstruction validates cross-record bindings before exposing the projection. It does not fetch inputs, run parsers/interpreters/domain evaluators to rederive facts, import names supplied by the checkpoint or use pickle. Existing native constructors may be reused where they validate representation without external or semantic execution. Material validation is placed at its earliest sufficient owner rather than duplicated in every consumer.

Reconstruction preserves what a supported admitted owner recorded at the checkpoint. It does not reevaluate semantic truth, freshness, adequacy or action permission. Trust depends on the admitted capture/storage boundary and retained provenance; self-asserted producer names plus checksums cannot admit an arbitrary imported checkpoint. The initial supported store is host-created, host-owned local storage. Untrusted checkpoint import/authentication is outside this method; structural inspection must not promote such material to native authority.

Unsupported family/codec/semantic versions, missing material and inconsistent bindings have explicit outcomes. Unaffected history can remain inspectable. Absence of a nested value cannot be replaced with a current dataclass default. Preserve original method identity separately from the decoder identity. A code change must either retain an explicitly tested compatible decoder or refuse affected reconstruction; relabeling old assessments with the new method is forbidden.

### Storage and publication

Use standard-library SQLite on the supported local filesystem, with WAL, synchronous FULL, foreign keys and explicitly configured bounded writer contention. Validate the selected settings instead of silently falling back. Storage adapters are private to persistence; native codecs and consumer contracts do not expose SQL or require a wire transport.

The minimal relational boundary stores immutable record bodies, revision headers/material membership and one conditional lineage head. A transaction checks the expected predecessor, immutable identity/content consistency and coherent material references, inserts the successor and atomically advances its head. Exact physical table/column names are routine implementation details; the transaction and ownership boundaries are this decision. Keep the previous immutable revision when publication fails. A competing writer receives a publication conflict rather than an automatic merge or capability retry.

Initial cadence is one durable checkpoint per successful canonical publication. Admission/attempt intent is published before a capability begins; observation and evaluation may be separate coherent publications so interrupted work does not fabricate completion. Unpublished staging carries no durability promise. Successful checkpoint acknowledgement follows commit; commit followed by lost acknowledgement remains an explicit unconfirmed-publication outcome and can be reconciled by identity. Workspace publication does not establish exactly-once external effects, and an engine WAL checkpoint is not an investigation checkpoint.

Initial retention preserves every declared revision and its material closure for a retained local investigation. No automatic expiry, pruning, compression or cross-investigation deduplication is selected. This conservative first contract permits growth and requires disk-full handling; later compaction/deletion needs a separate retention decision preserving surviving boundaries. Capture only relevant public content and available public-safe method metadata under Security, never credentials, secret headers, hidden reasoning or unrelated environment values. Local checkpoints/backups stay outside the Git repository in an owner-only store directory.

Use SQLite's online backup API into a new destination and validate the backed-up schema, declared revisions and material contents before reporting success. Keep the source intact on failure. DB-file-only copying, replacing the live store and automated backup rotation are not supported first operations. Initial schema/codec support is explicit version 1 with refusal of incompatible versions; automatic upgrade/downgrade is absent. A later migration requires a supported version map, validated backup and before/after native/history proof.

### Recovery and continuation

Offline recovery selects and validates one declared revision from one store/backup. It performs zero provider, model, evaluator (including synthesis/adequacy) or target-code calls. Return the selected revision, supported native projections, retained historical conclusions with their basis, explicit gaps and the recoverable boundary; an earlier-boundary fallback discloses lost progress. Restoring/rendering a retained conclusion is distinct from generating fresh synthesis; the latter is a separately admitted evaluation operation and cannot be hidden in recovery or historical report inspection. Do not combine torn histories or substitute an external provider for missing content.

Continuation is a separately invoked host operation under Core §6.4. It validates current exact target, material premises, supported method/capability and present authorization before using historical results or starting work. An unknown completion remains unknown until explicitly reconciled; no automatic retry is granted. Unsupported semantic/adequacy methods remain unsupported. These transitions preserve the full ADR-0012 target without selecting an Investigator policy or a general semantic evaluator.

## Alternatives, consequences and reversal

- **Generic dataclass/class-tag reconstruction:** less initial mapping work but freezes implementation shapes, permits hidden type authority and fails owner/version compatibility. Reject as a production method; explicit mappings cost maintenance but make support and refusal testable.
- **Re-run native processing from retained inputs:** useful for the separately admitted replay obligation, but performs evaluation and may change methods/results. Reject as the recovery method.
- **Keep live values or recover only reports:** cheaper but cannot support a fresh process's native consumers/history. Retain only as clearly bounded experiment/report behavior.
- **Self-contained files:** credible simpler storage alternative with faster measured opaque restore, but the exercised history duplicates payloads and needs coordinated publication/locking/backup. Retain as a reassessment alternative; SQLite's measured sharing and coherent publication justify its provisional production use. No engine-only speed or power-loss winner is asserted.
- **Hybrid blobs/event storage/services:** add publication, cleanup and compatibility boundaries without demonstrated benefit. Reassess only if measured content volume, write/restore cost or concurrency defeats this baseline.

Explicit codecs, retained history and per-transition publication add implementation/storage cost. Their independent reasons are cold reconstruction, historical validity and truthful interrupted progress. They do not solve missing capture inputs, semantic accuracy, discovery coverage or usefulness. Process-interruption tests are required; power-loss/device guarantees remain unproved and require separate evidence before a claim.

Before consumer cutover, stop adoption while preserving native behavior and acquired research evidence. After canonical history exists, reversal must preserve inspectable checkpoints/version support; returning to a legacy snapshot cannot silently discard history. Keep a one-way legacy projection only for a named parity/compatibility obligation and remove/reassess it when that obligation ends.

Reassess if a required native family cannot be reconstructed without re-evaluation, the codec duplicates native semantics, storage cannot satisfy the declared loss/backup boundary, compatible schema evolution is infeasible, or representative cases need unsupported retained context. Resolve the owning method/contract before expanding implementation. Acceptance includes the per-publication cadence and conservative initial retention cost described above; ADR acceptance and production implementation remain separate.
