# Investigation Workspace implementation architecture research

**Status:** Research program; activation, evidence and review position are owned by `MEMORY.md` and the linked cycle record. Production adoption is separate.
**Responsibility:** Compare concrete implementations of main's canonical Workspace, producing discriminating evidence and recommendations for main. This is Workspace implementation R&D; the separate LLM/H1 workstream owns Investigator mechanisms.

## Constraints and entry evidence

Use [Core §§3–6.3](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md), [Product Decision Model §§7–13](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Maintainer Action Synthesis](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md), [ADR-0010](../docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md), [ADR-0011](../docs/architecture/ADR-0011-explicit-source-association-bases-and-proposal-boundary.md) and [Security](../SECURITY.md) as controlling owners.

[ADR-0012](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md) and the [main design cycle](../working-memory/2026-10-07_investigation-workspace-and-investigator-interface-design_lbd-cycle.md) constrain composition, lifecycle, recovery and replacement migration. The B2 direction is accepted; the ADR and exact Core §6.4 recovery delta remain Proposed at inspected main `08243e5b`. Research respects those boundaries without promoting them. Genuine contradictions return to main with a minimal reproducer and affected owner; experiments cannot silently amend contracts.

The complete responsibility includes evolving canonical knowledge, native authority, projections, coherent durable recovery and validated continuation. Each experiment exercises a bounded part; no prototype is the full production Workspace. Deterministic retained-input replay remains a separate obligation: identify retention implications, but do not implement or claim replay here.

## Open decisions and implementation pressure

These choices concern implementation within the selected architecture, not alternatives to canonical Workspace ownership.

| Decision genuinely open | Credible comparison | Discriminating evidence / major risk |
| --- | --- | --- |
| State and revision representation | Immutable composed revisions versus mutable working state with separately frozen published revisions/history; compact deltas only if full-copy cost warrants them | Old views/bases stay stable; successor lineage and dependency invalidation remain explicit. Measure copying/serialization cost rather than assume event sourcing. |
| Canonical persistence | Versioned file checkpoints; SQLite records and content together; SQLite metadata with immutable external blobs | Same dependency closure and faults across options. Hybrid adds a publication/cleanup boundary between database and files; avoid two writable truth stores. |
| Checkpoint publication and recovery | Complete revision publication versus coordinated incremental record writes with a declared checkpoint boundary | Restore one validated revision, disclose uncheckpointed loss, preserve ambiguous attempts. Cadence, retention duration, backup and schema evolution remain decisions, not defaults. |
| Identity, references and retained content | Scoped record/attempt identities plus separately declared content digests; inline versus separately retained material content | Equal bytes can belong to different scopes/authorities. Annotations must not alter original payload identity; URLs/digests cannot replace missing material bytes. |
| Internal decomposition | Focused records with one publication boundary; extract a service only where a real consumer/failure boundary earns it | Trace identity/reference admission, native storage, history, views and checkpoint validation. Avoid a universal evidence hierarchy or competing domain evaluators. |
| Investigator executable seam | Small typed Python interaction boundary; explicit serializable projection/request envelopes where the research consumer needs them | Separate retained-state reading/view delivery from acquisition attempts; preserve request basis, admission, unsupported evaluation and observed delivery. No framework/model topology selected. |
| Legacy migration | Direct Workspace consumer cutover; temporary Workspace-to-legacy projection only for identified proof/caller need | Native/report parity and new lifecycle preservation without a second acquisition path. No external compatibility obligation has been established by this bounded inspection. |
| Staleness and local concurrency | Serialized publication baseline versus conditional publication against an expected revision, with material-basis revalidation | Two delayed results or writers must not lose updates or double-count support. Revision conflict is distinct from evidential staleness; no distributed-service requirement inferred. |

## Reuse ledger grounded in current source

| Existing seam | Reuse / limitation |
| --- | --- |
| [Investigation orchestration](../src/upgradepilot/investigation.py): `investigate_public_pull_request`, injected clients | Useful producer sequence and offline test ports. `PublicPullRequestInvestigation` is a frozen final result, not a revision/checkpoint owner. `source_contexts`, `coverage_inputs`, workflow definitions and project-environment inputs are locally composed; the returned result does not retain them as a complete input bundle. |
| [Dependency analysis](../src/upgradepilot/dependency/analysis.py), [repository acquisition](../src/upgradepilot/github/repository.py) | Reuse typed source contexts, exact-revision text and distinct unavailable-file results. Retention starts at the producer/composition boundary before material inputs disappear; no blanket raw HTTP capture. |
| [CI coverage](../src/upgradepilot/ci/dependency_exercise.py), [dependency state](../src/upgradepilot/ci/dependency_state.py), [Python-support impact](../src/upgradepilot/impact/python_support.py), [artifact impact](../src/upgradepilot/impact/artifact_serviceability.py) | Reuse native evaluators and scoped records directly. A command-completion witness and another command's unresolved environment can coexist; do not compress them into an installed/success flag. |
| [Upstream support-drop bridge](../src/upgradepilot/upstream/support_drop.py) and [claim validation](../src/upgradepilot/upstream/claim.py) | Reuse existing admitted extraction/grounding meanings. The final result is not a full model-call/view/rejected-proposal history; preserve available material basis and explicit missing method provenance. General semantic/adequacy evaluation remains unavailable. |
| [Synthesis](../src/upgradepilot/maintainer_action.py), [report projection](../src/upgradepilot/report_projection.py), [CLI](../src/upgradepilot/cli.py) | Concrete migration consumers: synthesis type-checks and retains the old result; report projection invokes synthesis. Current action support is explained abstention. Report-local sequential source IDs are not stable Workspace binding IDs. |
| [Report file codec/publication](../src/upgradepilot/report_file.py), [tests](../tests/test_report_file.py) | Reuse strict version/reference/integrity handling and publication failure tests as patterns, not as a Workspace schema. File fsync plus non-replacing hard-link publication does not establish a multi-record checkpoint or power-loss recovery contract. Offline report opening remains separate. |
| [Experiment transition](../experiments/evidence_gap_investigation_transition.py), [planner composition](../experiments/evidence_gap_product_planner_composition.py) | Reuse explicit attempt/failure and deterministic transition-replay test ideas. The single target-Python action and model-hidden projection are too narrow to become the Workspace contract. Product code cannot import experiments. |

The [older persistence proposal](../proposals/2026-09-08_RUN_RECORDS_EVIDENCE_PRESERVATION_REPLAY_AND_RECOVERY_PROPOSAL.md) supplies useful fault/retention questions. Its no-save CLI assessment and export-first ordering are historical; current report save/open and the newly intended recovery responsibility supersede that entry context. Its file preference is not a selection.

Pinned [H1 design `253b48de`](https://github.com/motafegh/UpgradePilot/blob/253b48de20b475eada48810d193bd420c51aa7d4/proposals/2026-10-08_H1_WORKSPACE_INVESTIGATOR_INTEGRATION_EXPERIMENT_DESIGN.md) supplies consumer pressure only: `SourceWorkspace` is a corpus backend, not canonical state; native fact access needs real sufficient inputs; pure view delivery must not masquerade as acquisition. No H1 mechanism comparison or model execution belongs to this program.

## Prioritized bounded experiments

### 1. Establish material closure and compare revision representations

Create one experiment-local trace corpus from native offline paths: command-completion plus unresolved environment/conditional extra; support-drop before/after target relevance; failed versus empty read; retained-but-undelivered evidence; a proposal with unsupported evaluation; and interrupted work. Real source/tests supply existing facts; new lifecycle scenarios are explicitly simulated, never product semantic evidence.

For each trace, map named consumer → material native/input/history/content dependencies → owning producer/capture point → retained bytes or explicit gap. Draft a minimal versioned checkpoint schema and exercise two state implementations against the same expected relationships. Do not encode all native families yet. Compare historical-view stability, exact identity, duplicate/collision handling, successor invalidation and closure size. Vary target, scope, payload, annotation and ordering independently.

**Exit evidence:** a dependency-closure/retention ledger, minimal schemas, identical semantic observations for both representations and measured update/serialization costs. A lossy round trip or required owner change blocks progression. Recommend a representation provisionally; keep storage independent.

### 2. Compare checkpoint stores through actual interruption and recovery

Implement disposable file and all-in-SQLite stores for that same schema/corpus. Try SQLite-plus-blobs only if captured content sizes or backup/update costs give it a concrete advantage to test. This stages comparison effort, not a commitment to files or SQLite. No ORM, backend framework or durable product repository layer is needed.

Exercise process termination before/after content writes, record writes, publication and acknowledgement; truncated/corrupted/missing content; broken references; unsupported schema; write refusal/full-storage simulation; earlier-checkpoint fallback; and observation recorded before evaluation. Restoration must make zero provider/model/evaluator calls and preserve completion-unknown work. In hybrid trials include both orphan blobs and committed references to absent blobs. Test supported backup/restore and explicitly label lost progress.

Use one writer initially, then two independent processes/readers to expose stale publication, contention and duplicate-result races. Declare expected-revision/locking behavior rather than treating a store's transaction as request-validity logic. For each SQLite configuration record journal/synchronization/foreign-key settings and runtime version. SQLite's [atomic commit](https://www.sqlite.org/atomiccommit.html), [WAL](https://www.sqlite.org/wal.html) and [backup guidance](https://www.sqlite.org/backup.html) inform fault boundaries; engine guarantees alone cannot establish application closure.

**Exit evidence:** per-option fault matrix, recovered revision/closure, acknowledged versus lost progress, backup fidelity, storage/write amplification, update/restore latency and maintenance cost. Benchmark the same disclosed corpus and scaled copies; copies probe volume, not generality. Name hardware/filesystem and repeats. Process-kill and injected faults do not prove power-loss durability; document that residual boundary. Reject correctness failures before ranking performance. State cadence/retention trade-offs before proposing a durability promise.

### 3. Exercise decomposition and the Investigator-facing seam

Use a deterministic scripted consumer, one native producer/evaluator path and explicit unsupported outcomes for unavailable evaluation. Compare the smallest in-process seam with a serialized envelope only where it changes consumer usability or validation cost. Reads generate view/delivery evidence; acquisition requests use actual discovery/need bases and separate admission/attempt/observation paths.

Exercise delayed same-target results after unrelated versus material changes; head change; counterevidence; method/capability withdrawal; forged authority; duplicated delivery; identical content under different scopes; and omitted-but-addressable evidence. Restoration followed by explicit continuation must revalidate current bindings and host authority. A stale publication can be retried only after revalidation; unknown external completion cannot become automatic retry permission.

**Exit evidence:** a small executable interaction sketch, responsibility/import map, authority and invalidation tests, and the minimum H1-facing projection requirements. This proves plumbing/record fidelity, not semantic correctness, adequate investigation or Investigator superiority.

### 4. Demonstrate replacement migration feasibility

Trace one normal offline native path into the prototype Workspace and one-way synthesis/report consumers. Use existing native/report assertions as an oracle; compare material meanings at fixed report time while accounting for generated IDs. Add lifecycle/retention assertions the legacy projection cannot express. If a temporary legacy bridge is required, identify its precise caller/proof reason, loss boundary and removal trigger; do not run a second legacy acquisition sequence to generate its input.

**Exit evidence:** acquisition/evaluator call counts, preserved facts/unknowns/action limits, consumer cutover map, remaining native families/retention debt and legacy retirement conditions. No production cutover occurs on this branch.

## Review, artifact and adoption boundary

Preparation may change this plan, its single [cycle record](../working-memory/2026-10-08_workspace-implementation-architecture-research_lbd-cycle.md), and branch-local `MEMORY.md`. After review, prototypes/tests belong under `experiments/` and `experiments/tests/`; public-safe results go in the cycle's dated evidence directory. Keep production source/tests, main's specifications/ADRs and the H1 mechanism unchanged. Do not capture credentials, call models, execute target code or write to target repositories.

The initial sequencing recommendation was to activate **experiment 1 only** first: retention closure determines what later stores must preserve. Its exclusions are temporary research sequencing. Experiments 2–4 and coverage of the native families admitted for a production slice supply later proof; that does not require every future family to be implemented before a bounded production slice. Reassess ordering when evidence changes the discriminating question, recording its exact scope and limits first.

Program review precedes experiment activation. Each coherent experiment ends with evidence, rejected options and remaining uncertainty before expanding. Main alone selects final method/technology, accepts semantic changes and authorizes production integration. A recommendation requires correctness/authority fidelity first, then measured cost and simpler-baseline comparison; no arbitrary aggregate score can offset a broken recovery boundary.

## Cross-experiment recommendation for main — evidence dated 2026-10-09

This is a non-controlling research synthesis, not an ADR, adopted schema or implementation authorization. The dated evidence below supports provisional choices within main's Workspace direction. Activation and final review remain owned by `MEMORY.md`.

| Implementation question | Recommendation and discriminating evidence | Remaining decision / limit |
| --- | --- | --- |
| Revision representation | Prefer immutable published successors sharing immutable payloads. [Experiment 1](../working-memory/evidence/2026-10-08-workspace-revision-representation/README.md) found byte-equal histories for both implementations; aliased read-only views leaked new IDs, while mutable staging supplied no demonstrated consumer advantage. | Full-index copying was adequate at measured volumes. Neither draft staging nor deltas/event storage were disproved; add them only for an observed need. Publication batching timings do not select checkpoint cadence. |
| Storage | Carry the user-accepted **all-in-SQLite WAL/FULL** baseline. [Experiment 2](../working-memory/evidence/2026-10-08-workspace-checkpoint-stores/README.md) demonstrated process-kill/fault/backup fidelity, conditional publication, shared-history savings and publication with a held reader. | Files remain credible and restored faster in this corpus. The rollback comparator was DELETE/**EXTRA**, not FULL. Hybrid has no demonstrated benefit; power loss, physical writes, retention and production storage operations remain unproved/unselected. |
| Checkpoint/recovery | Publish one declared coherent revision and expose publication conflict/unconfirmed acknowledgement separately from operation completion. Restore validated retained state before explicit continuation. E2 faults and [E3 interactions](../working-memory/evidence/2026-10-08-workspace-investigator-seam/README.md) preserve those distinctions. | Opaque byte recovery works in the research schema; trusted native consumer reconstruction does not. Workspace checkpoints and engine WAL checkpoints are different boundaries. No exactly-once external effects or product replay proof. |
| Identity/content/basis | Keep exact target lineage, scoped record identity and content digests distinct; preserve original payloads and material references. [Public grounding](../working-memory/evidence/2026-10-08-workspace-experiment3-grounding/README.md) corrected a target token that incorrectly included mutable PR metadata. | Historical PR/base/head evidence never moves to another target. Declared edges do not discover missing premises; selective retention, source-association completeness and schema evolution need admitted methods. |
| Decomposition/Investigator seam | Prefer small typed consumer values, separate host admission/attempt/observation/proposal history, native evaluation and private checkpoint adapters. E3 memory/SQLite and Python/wire traces agree; original and current basis/method checks independently mattered. | Keep storage details out of the contract. Serialization is optional; fixture-controlled relevance/capability routing is not a general scheduler, evaluator or authority system. |
| Migration | Prefer direct producer publication into Workspace and consumer cutover. [Experiment 4](../working-memory/evidence/2026-10-09-workspace-replacement-migration/README.md) preserves native meanings, synthesis limits and report/save/open parity from one offline producer sequence. | Current synthesis requires the legacy type. The one-way bridge earns an experiment parity reason only; its live typed cache, fixed legacy field manifest and capture hooks are not production selections. Cold recovery explicitly refuses `unsupported_native_codec`. |
| Staleness/concurrency | Use expected-revision publication and material-basis validation for distinct problems. E2 competing writers and E3 delayed results reject lost updates without treating every revision difference as stale evidence. | Current product orchestration is synchronous. Parallel/outstanding operations and adaptive invalidation are future pressure; keep the [scenario classification/source paths](../working-memory/evidence/2026-10-08-workspace-experiment3-grounding/README.md#scenario-roles-and-concrete-current-paths), defensive tests and unsupported owner-input outcomes. |

The known public grounding case retained two roughly 606 KB lockfiles; it qualified E1's small-source rationale without measuring a hybrid advantage. Grounding's checkpoint-contained input recipe permits bounded offline native re-execution, while E4's cold native projection refuses. These findings concern different capabilities: retained-input re-execution does not supply an admitted typed recovery codec. Neither result proves production recovery/replay or unseen semantic acceptance. Supplied extraction candidates and unsupported proposal/adequacy outcomes remain disclosed.

### Adoption obligations and ownership

| Priority / obligation | Correct owner and evidence needed |
| --- | --- |
| First: main review of method and recovery semantics | Main reconciles the still-Proposed ADR-0012/Core recovery delta and selects consequential implementation methods. This branch supplies evidence; it does not promote those owners. |
| First technical risk: native capture and cold reconstruction | Explicit owner-specific, versioned capture/codec design for the admitted families. Prove retained input/basis closure and cold native consumer parity without acquisition/evaluator reruns; reject unsupported versions, missing material and inconsistent references. Checksums alone do not authenticate provenance. |
| Before promising durable progress: retention/cadence/backup | Main specifies admitted loss/retention/privacy behavior; production design establishes checkpoint cadence, supported backup/restore, schema upgrades and failure handling. Preserve power-loss and unavailable physical-write measurements as limits rather than implied guarantees. |
| Before production cutover: scope and retirement | Main selects supported families; production proves their producer/consumer/native/lifecycle boundaries and rollback without canonical-history loss. E4's cutover map supplies concrete callers. Keep conditional/uv/group, artifact/environment, provider-failure and extraction-provenance debt explicit; no second writable truth path. |
| Separate responsibilities | Investigator mechanisms stay with H1; semantic/adequacy methods and deterministic replay need their own admission/proof. Future adaptive pressure does not justify a framework/service or broaden this branch automatically. |

### Candidate follow-up, requiring separate activation

If main wants more discriminating evidence before production design/build, prioritize **a cold native capture/codec proof for the already exercised CI/runtime and Python-support families**. Its question is whether a fresh process can reconstruct explicitly supported native consumer inputs from a checkpoint alone, preserving meanings, exact target/basis and unknowns without live values, acquisition or reevaluation.

Use the existing controlled E4 path and E1–3 storage-independent checkpoint boundary. Require fresh-process parity, original-input association, explicit supported version/type mapping, zero provider/model/domain reruns, and refusal for missing material, wrong target, unsupported schema/type and malformed references. Never instantiate arbitrary class tags. Keep the legacy projection only as a named comparison oracle; this does not authorize full codec implementation, new families, production capture, schema-upgrade policy or cutover. Stop at result review.

Main may instead resolve that method and proof inside a separately authorized production design/build. Choose the spike only if uncertainty would materially change that work. No further storage/framework/model comparison is justified by these results alone.
