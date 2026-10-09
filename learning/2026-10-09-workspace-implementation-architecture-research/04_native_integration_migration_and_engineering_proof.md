# Native integration, migration and engineering proof

**Snapshot:** research `7ae80a07d5fb9180ddb30145ea389bebe6553c5f`, 2026-10-09. See the [package horizon](README.md). This note combines two complementary development proofs, with their different inputs and execution boundaries kept explicit.

## Why integration evidence was needed

The earlier experiments showed declared retention, local store recovery and lifecycle interaction. They did not establish that the normal producer could supply a Workspace, that existing consumers could use its projections, or that real public input sizes matched the synthetic corpus.

Two later increments addressed different parts of that uncertainty:

| Teaching path | What actually ran | What it did not establish |
| --- | --- | --- |
| Known public Soup Sieve update | Anonymous exact-input acquisition and a model-free native support-impact subset, wrapped by research Workspace mechanics. | Complete product CLI/orchestration, CI/runtime/artifact coverage, autonomous semantic extraction or unseen acceptance. |
| Controlled normal orchestration | Actual `investigate_public_pull_request` once per backend, with offline ports and an explicit candidate extractor, then unchanged synthesis/report/save/open consumers. | Real-provider trust, model correctness, cold typed recovery or production cutover. |

They must not be spliced into one supposedly complete live investigation. Grounding provides real data pressure; migration provides normal-entry composition and consumer parity. A successful known development case also cannot become unseen acceptance evidence simply by rerunning it.

## Trace the public case

The [grounding evidence](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/working-memory/evidence/2026-10-08-workspace-experiment3-grounding/README.md) pins `pydantic/pydantic#13432`, Soup Sieve **2.6 → 2.8.4**:

- Base `652a61ce4f9d7d76eaada31535807a485ece0e21`.
- Head `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a`.
- Exact upstream tag/commit/changelog and target project texts are retained with the acquired public inputs.

Open [run_workspace_public_grounding.py](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/experiments/run_workspace_public_grounding.py). It composes existing PR/file, dependency, package/provenance, upstream interval, claim-grounding, impact and target owners. The default support interpretation would call a model, so this trial explicitly supplies the known changelog candidate through existing native validation. It acquires 14 anonymous GET inputs and executes no target code.

The native result changes from unresolved to `established_not_applicable`: the supplied/grounded Python-3.8 support-drop candidate falls outside the target's declared `requires-python >=3.10`. The selected follow-up need retires. This answers that bounded applicability question; it does not prove all impacts absent, adequate stopping or action permission.

The [public input tape](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/experiments/workspace_public_input_tape.py) preserves ordered URLs, statuses, permitted public headers, acquisition times, digests and decoded response bodies. Those are decoded input bytes, not compressed network-wire reproduction. Retaining content hashes alone would leave the source unavailable offline.

Initially the checkpoint retained content/native results but native re-execution still depended on an external tape's acquisition recipe. The correction adds immutable capture-manifest records. Now the checkpoint itself can reconstruct that recipe and replay the bounded native subset offline with network blocked, producing byte-identical summary/checkpoint on memory and SQLite. Read `test_sqlite_recovery_reconstructs_native_inputs_without_external_tape` in [grounding tests](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/experiments/tests/test_workspace_public_grounding.py).

This is retained-input research re-execution, which intentionally runs native processing. It is not cold reconstruction of previously produced typed results, nor the full admitted product replay obligation. The distinction matters when comparing it with the migration trial's codec refusal.

Two other discoveries changed the mental model. Full PR-record serialization included title/state/ref metadata in the target token; a title-only refresh therefore incorrectly looked like another continuation target. The corrected token uses repository/PR/base/head. Separately, two real lockfiles were roughly 606 KB each, versus E1's tiny source-text corpus. Full provider envelopes plus admitted texts duplicate research bytes deliberately. This qualifies the small-source rationale without measuring hybrid benefit or selecting production raw-input retention.

## Trace the normal offline producer into captured state

Read [workspace_replacement_migration.py](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/experiments/workspace_replacement_migration.py), beginning with `capture_normal_pipeline`, `NativeCapture.acquire`, `NativeCapture.evaluate` and `bind_legacy_fields`.

The controlled requirements transition is demo 1.0 → 2.0. Existing native CI/runtime processing yields one command-completion requirement witness and another command's unresolved ambient environment. The supplied changelog candidate plus exact target declaration gives support-impact `unresolved → established_applicable`. Here the fixture includes the dropped target Python line, unlike the public case's `>=3.10` declaration.

The current product producer still constructs its original `PublicPullRequestInvestigation`. The experiment captures that same invocation's native inputs/results and uses its return as the independent parity oracle. It demonstrates a possible replacement route; it does not retire the production constructor.

```text
controlled acquisition ports
→ unchanged normal product orchestration/native owners
→ capture actual material arguments and returned native values
→ immutable experimental revisions/private checkpoint adapter
→ one-way consumer projection
→ existing synthesis/report/save/open
```

Capture happens while orchestration still has `source_contexts`, `coverage_inputs`, workflow/target texts, the requirements patch and extraction-window/proposal inputs. Waiting for the final frozen result would lose some of that bundle. Execution machinery such as a client object is not serialized as evidence; its actual input/returned data is captured separately.

The first fixture omitted `ChangedFile.patch`, so normal dependency analysis returned `missing_dependency_patch`. Supplying constructed full base/head files would not repair the actual path: this path consumes the validated requirements patch. Correcting the patch and discovery-record shape let the intended native branch execute. The lesson is to trace the real producer input contract, not imitate the earlier corpus's shape.

`NativeCapture` publishes immutable input/output records and retains live typed objects in a disposable cache. All records are roots and many input dependencies include preceding captures. This conservatively demonstrates retained material without claiming minimal premises, selective retention or scalable invalidation. Its 90 publications are instrumentation choices, not checkpoint cadence policy. Capture hooks and the legacy-field manifest are proof machinery, not selected production design.

## The consumer boundary and the bridge's earned reason

At this snapshot, [maintainer_action.py](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/src/upgradepilot/maintainer_action.py) explicitly requires `PublicPullRequestInvestigation`. [Report projection](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/src/upgradepilot/report_projection.py) invokes that synthesis owner. A direct native-field namespace was tried; synthesis rejects it, and report reaches the same rejection.

The one-way `project_legacy_result` bridge therefore earns a precise experiment reason: reuse unchanged consumers and compare their meanings against the single original producer result. It does not earn a production compatibility obligation. It never runs a second acquisition path or copies synthesis semantic rules.

`projection_values` requires the full expected field manifest, retained material bytes, matching live values and matching exact target. It compares `encode_fields(live_value)` with the retained payload before constructing the legacy result. Missing optional fields cannot silently receive dataclass defaults; that would conceal lost captured state. Mutating a live value cannot override immutable evidence.

Parity preserves all 24 producer fields, complete synthesis meanings and the fixed-time report. The comparison normalizes only the generated report UUID; source/reference IDs, strengths, unknowns and timestamps remain part of the comparison. Report codec, saved-file read and rendering preserve their own meanings. A saved report still cannot restore canonical lifecycle/history state.

The native witness remains scoped to command completion. Another command's unresolved environment remains unresolved, artifact impact stays not evaluated, and applicable support impact still gives synthesis action `abstain`. The snapshot's native fact does not imply installed/safe/compatible or active maintainer-action permission.

## Successful parity still leaves cold recovery blocked

`encode_fields` retains tagged native fields. `decode_checkpoint` reconstructs opaque records. Neither is an admitted mapping from checkpoint bytes into trusted versioned native objects.

When the live cache is absent, `projection_values` explicitly raises `ProjectionUnavailable("unsupported_native_codec: live values unavailable")`. Same-process restoration can use captured typed values only if their bytes and exact target match. This is useful parity evidence, but a restart cannot recreate those objects from that cache.

| Capability | Result at this horizon |
| --- | --- |
| Recover opaque checkpoint records | Demonstrated for the research schema/stores. |
| Re-execute the bounded public native slice from checkpoint-contained inputs | Demonstrated with explicit retained recipe and network blocked. |
| Feed current typed consumers after restart without live cache or reevaluation | Explicitly unsupported. |
| Recover/continue a complete production canonical Workspace | Not implemented/adopted. |

Importing classes by arbitrary retained type tags or silently rerunning native evaluators would conceal the gap. A later explicit native capture/codec method must specify supported types/versions, retained associations, malformed/missing material behavior and consumer proof. This note does not authorize that work.

## Why the call oracle needed its own test

The [migration runner](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/experiments/run_workspace_migration_trial.py) records one orchestration entry, 13 acquisition-port returns, 15 instrumented application/native-boundary invocations and one explicit fixture extractor per backend. Nested helpers are not a global evaluation metric. Two impact calls are the legitimate before/after native sequence.

Eight early tests passed, but capture hooks ended with the producer. Flat counters could then miss a later native call. A separate control invoked an actual native owner and obtained a result without changing those counters. The repair uses `forbid_producer_reentry` during consumers/restoration to reject current application and domain aliases independently. The regression exercises both aliases. Patching only the definition would miss an imported application alias; guard the actual lookup sites.

The parity trial also performs **7 synthesis attempts and 4 report attempts** across baseline, rejected direct inputs, bridged inputs and post-lifecycle comparison. Those are real consumer evaluations and are counted separately. “Zero further acquisition/domain processing” is narrower and supported by refusal guards. It does not mean zero computation, nor isolation from arbitrary hostile references in Python.

## Migration direction and proof limits

The resulting recommendation is direct native producer publication into Workspace, then consumer projections under separately admitted production design/build. Retire the bridge when direct consumer inputs preserve native/action/report meanings and no independent caller/compatibility obligation earns it. The current legacy type remains a real migration dependency; its existence is not architectural retention authority.

The bridge cannot represent revision/basis history, delivery/use/proposal/evaluation lifecycle, material-input closure or unfinished work. Workspace retains those separately; projecting them cannot strengthen action permission. The added unfinished record is simulated future/defensive pressure, not a native outstanding operation produced by today's synchronous orchestrator. Rollback after product cutover would need to preserve new canonical history rather than silently revert to the old lossy snapshot.

Read [migration evidence](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/working-memory/evidence/2026-10-09-workspace-replacement-migration/README.md) and [migration tests](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/experiments/tests/test_workspace_replacement_migration.py). The final receipt records 9 migration plus 112 inherited experiment tests, and 115 focused product tests. These were not full suites, hosted verification or new live-model proof. Complete native-family capture, schema evolution, retention/cadence, provider trust, semantic/adequacy evaluation, physical writes, power-loss durability and deterministic product replay remain separate obligations.

## Learning depth and fast return

**Own:** real-data versus normal-path proof, capture before local inputs disappear, parity versus complete recovery, and independent measurement oracles. **Understand operationally:** invocation capture, field manifests, byte-bound typed caches, report normalization and consumer alias guards. **Lookup:** mock/context-manager mechanics and exact serialization syntax. **Defer:** full codecs, broader families, production cutover/rollback and H1 mechanism research.

Fast return: trace the public candidate to target relevance; inspect `projection_values` with an empty live cache; follow direct-input failure to the one-way bridge; read the call-oracle regression; state exactly what the final parity test cannot recover.

### Transfer questions

1. Why do the public and controlled support-drop examples legitimately produce different applicability results?
2. What acquisition recipe was missing when checkpoint re-execution still needed the external tape?
3. How can complete report parity coexist with failed cold native recovery?
4. Why can counters remain unchanged after an actual native invocation, and how does the corrected oracle expose it?
5. What would independently earn retaining the legacy bridge after direct consumers are available?
