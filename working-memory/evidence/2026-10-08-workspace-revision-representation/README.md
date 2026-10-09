# Experiment 1 — material closure and revision representation

**Recommendation for review:** use immutable published revisions with shared immutable native payloads as the provisional comparison baseline. A mutable draft is feasible, but adds staging/rollback state without a demonstrated consumer need. This selects neither production architecture nor checkpoint cadence/storage. Main owns adoption; experiment 2 is not activated.

## Question and setup

Can direct immutable successors and mutable drafts with frozen publication preserve the same material history, identity and native meanings, and what does each cost? The [cycle record](../../2026-10-08_workspace-implementation-architecture-research_lbd-cycle.md) preserves the progressive reasoning, including corrections and negative results; the [program](../../../plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_ARCHITECTURE_RESEARCH_PLAN.md) owns the bounded comparison.

The [corpus](../../../experiments/workspace_retention_corpus.py) executes native evaluators on synthetic offline inputs patterned on existing tests. It is not GitHub acquisition or a whole-PR integration run. CI retains a command-completion witness beside another command's unresolved environment; optional-extra selection remains unresolved because marker truth is unevaluated. A caller-supplied support-drop candidate passes native grounding, then applicability changes from `unresolved` to `established_applicable` after native target relevance. No extractor/model ran, and applicability grants no action permission.

New request/admission/attempt/proposal/view/lineage records are expressly lifecycle simulations. These preserve empty versus failed reads, unsupported evaluation without an assessment, completion unknown without retry permission, delivered versus omitted-but-addressable content, and unknown examination. The simulated method-provenance gap pressures missing-content handling; it does not describe an actual unrecorded model invocation.

The [representations](../../../experiments/workspace_revision_representation.py) share frozen records and immutable bytes. Both copy an index at publication; the draft also permits unpublished staged edits. Tagged native fields/type identities retain the inspected dataclasses without string-salvaging unknown types. Their reader restores opaque records, never trusted native objects. The [schema descriptor](checkpoint-schema-draft.json) is an experiment sketch, not a production JSON Schema or migration codec.

## Consumer-driven closure and capture ledger

| Named consumer | Retained material basis in this trace | Existing owner / earliest useful capture boundary |
| --- | --- | --- |
| Runtime dependency evaluator and later inspection | PR/dependency identity, exact base/head requirements bytes, source context, complete supplied workflow run/jobs/steps/definition input, native coverage and command-scoped results | [Dependency analysis](../../../src/upgradepilot/dependency/analysis.py) supplies context; [investigation](../../../src/upgradepilot/investigation.py) composes `coverage_inputs` before calling [coverage](../../../src/upgradepilot/ci/dependency_exercise.py) and [runtime state](../../../src/upgradepilot/ci/dependency_state.py). Capture these local inputs before the final result projection loses them. The fixture constructs requirements context rather than proving its acquisition. |
| Optional-extra selection | Exact base/head project and workflow bytes, changed-file identity, native analysis/source context and selection result | Native analysis boundary, then workflow inspection's project-environment source input in [workflow commands](../../../src/upgradepilot/ci/workflow_commands.py). Shared head project bytes also feed target relevance. |
| Support applicability and refinement inspection | Interval authority with release-index/changelog fields, attributed supplied proposal, grounded claims, impact candidate, earlier assessment/need, exact project bytes, declaration, relevance and successor assessment | [Interval assembly](../../../src/upgradepilot/upstream/interval.py), [claim validation](../../../src/upgradepilot/upstream/claim.py), [impact](../../../src/upgradepilot/impact/python_support.py) and [target relevance](../../../src/upgradepilot/target/relevance.py). Preserve each native output and its input association where produced; the simulated lineage explains the successor without overwriting earlier bytes. |
| Investigator context and lifecycle inspection, simulated | Exact empty content/unavailable record; view delivery/omission; proposal and unsupported evaluation attempt; request basis/admission/completion unknown; annotation and explicit provenance gap | Future Workspace orchestration records actual interactions at their boundaries. No existing production lifecycle contract or executable Investigator seam is claimed by these simulations. |

Seven final consumer roots reach **36 material records** out of 37 addressable records. One debug record is discardable and absent from the checkpoint; material annotation/lineage remain. The final [checkpoint example](checkpoint-example.json) is **80,115 bytes**, including **62,410 payload bytes** and one explicit gap. Exact source-text records total only **1,002 bytes** here; nested native results dominate, including runtime state (18,849) and coverage (14,662). Inspect native normalization/versioning before assuming large source blobs are the storage pressure.

This is a closure of **declared** material edges, not proof every native family or evaluation premise is captured. History and retention edges are currently conservative; distinct evaluation-basis roles must precede semantic staleness decisions. Changing target declaration marks relevance/successor/view/lineage as affected while leaving prior assessment bytes intact; it neither reevaluates nor declares adequacy.

## Failures and rejected alternatives

- **Actual setup failure:** early differential tests passed while two fixtures supplied different project bytes for one repository/revision/path. An independent identity probe exposed it. [Both conflicting inputs/digests](setup-correction.json) are retained. Both consumers now share one binding; regression rejects inconsistent bytes even under different binding IDs. No contradiction in main's semantics was found.
- **Aliased read-only proxy:** the executed control leaked 15 new record IDs into an old view. Publication must own a frozen backing index; a read-only wrapper is insufficient.
- **Result-only capture:** structural round-trip validation passed despite five independently required CI/source inputs being absent. Thus round-trip equality cannot establish retention completeness; the named-consumer oracle is essential.
- **Digest-only identity:** two empty reads with different scopes had the same digest. Content deduplication cannot substitute for observation/binding identity.

The last three controls and concrete missing/leaked IDs are in [results.json](results.json). Deep-copying payloads and delta/event-store machinery were deferred simpler-baseline alternatives, not measured losers. Review also corrected repeated closure traversal before benchmarking and strengthened the draft to expose genuine unpublished staging; these were source/setup corrections, not measured failures.

## Measurements and recommendation

The [runner](../../../experiments/run_workspace_revision_comparison.py) measured 1/10/50 copies (37/370/1,850 starting records), 30 updates, batches of 1/10, five trials per combination. Every trace revision is byte-identical across approaches and round-trips exactly. Largest-scale medians:

| Representation / batch | Total 30 updates (ms) | Per publication (ms) | Encode / decode final checkpoint (ms) | Peak index allocation (KiB) |
| --- | ---: | ---: | ---: | ---: |
| Immutable / 1 | 14.555 | 0.480 | 18.121 / 12.844 | 1,864.4 |
| Draft / 1 | 13.025 | 0.418 | 17.675 / 13.385 | 1,918.7 |
| Immutable / 10 | 1.618 | 0.521 | 17.593 / 13.288 | 409.1 |
| Draft / 10 | 1.381 | 0.453 | 16.906 / 13.309 | 460.1 |

At 37 records, total updates range 0.378–0.451 ms for batch 1 and 0.062–0.068 ms for batch 10. Small mixed differences between representations do not earn additional canonical mutable state. Prefer the direct immutable baseline provisionally; add draft staging only for a demonstrated need to accumulate unpublished work. Batching has greater cost impact, but changes recoverable progress/publication granularity, so these timings cannot select checkpoint cadence.

Runs used Python 3.12.3 on WSL2 Linux x86_64, i7-12700H / 20 logical CPUs; `stat` reported filesystem type `ext2/ext3`. Timings exclude fixture creation/initial population and disk I/O. Allocation is a separate `tracemalloc` run excluding prebuilt payload bytes, not RSS. Fixed approach order, warm local trials and copied inputs limit performance inference; copies add volume, not semantic diversity. Raw ranges, environment, native source-tree identity, preparation HEAD and exact experiment-file hashes are retained in results. No throughput budget or storage winner is established.

## Verification, limits and review boundary

**15 focused tests pass**, covering independent native meanings/basis, every-revision fidelity, historical stability, collision/broken-reference batch rollback, exact-source consistency, scoped identity, gaps and distinct outcomes, staging, delivery order, dependency impact and executed negative controls. Offline corpus/reader tests block HTTP and semantic-extractor calls. **58 native/report anchors pass** freshly; touched Ruff checks/format and document integrity checks pass. These establish bounded experiment fidelity, not product recovery.

Rerun from the repository root:

```sh
PYTHONPATH=src .venv/bin/python3 -m unittest experiments.tests.test_workspace_revision_representation -v
PYTHONPATH=src .venv/bin/python3 -m experiments.run_workspace_revision_comparison --output /tmp/upgradepilot-workspace-experiment-1 --repeats 5
```

No full product/experiment suite, live model, durable store, crash/power-loss test, concurrency, migration or replay was run. The sketch does not harden arbitrary external JSON imports, checksum all metadata, authenticate authority, validate all source families, rehydrate/version native objects or set retention policy. A structural reader cannot silently turn this deliberately gapped checkpoint into sufficient product recovery.

**Stop for experiment 1 review.** The next bounded question, if approved, is whether file and SQLite publication can preserve this declared closure under interruption/corruption and explicit lost-progress outcomes. Carry capture-completeness, native-codec and relation-role debt forward; storage transactions cannot resolve them. No experiment 2 prototype or production adoption is included.
