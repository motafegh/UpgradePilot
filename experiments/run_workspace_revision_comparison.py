"""Run the approved retention/revision experiment; export public-safe local evidence.

No file/database Workspace store is implemented. JSON outputs are research artifacts,
not durable checkpoint publication or recovery. Timing separates normal operation from
tracemalloc instrumentation; scaled corpus copies measure volume, not new semantics.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import statistics
import subprocess
import time
import tracemalloc
from dataclasses import replace
from pathlib import Path
from types import MappingProxyType

from experiments.workspace_retention_corpus import build_retention_corpus
from experiments.workspace_revision_representation import (
    ImmutableSuccessorHistory,
    MutableDraftHistory,
    TraceRecord,
    affected_dependents,
    decode_checkpoint,
    encode_checkpoint,
    material_closure,
    retention_gaps,
)

APPROACHES = (ImmutableSuccessorHistory, MutableDraftHistory)


def _summary(values):
    return {"median": statistics.median(values), "min": min(values), "max": max(values)}


def _scaled_records(revision, copies):
    records, roots = [], []
    for index in range(copies):
        prefix = f"copy-{index}/"
        records.extend(
            replace(
                record,
                record_id=prefix + key,
                dependencies=tuple(prefix + ref for ref in record.dependencies),
            )
            for key, record in revision.records.items()
        )
        roots.extend(prefix + key for key in revision.roots)
    return tuple(records), tuple(roots)


def _publication_trial(approach, target, records, roots, updates, batch):
    history = approach(target)
    history.publish(records, roots)
    root_list = list(roots)
    durations = []
    for offset in range(0, updates, batch):
        additions = tuple(
            TraceRecord(
                f"update-{i}",
                "experiment.lifecycle",
                "annotation",
                "benchmark-scope",
                b'{"note":"scaled synthetic update"}',
                (roots[0],),
            )
            for i in range(offset, min(offset + batch, updates))
        )
        root_list.extend(record.record_id for record in additions)
        start = time.perf_counter_ns()
        if approach is MutableDraftHistory:
            for record in additions:
                history.stage((record,))
            history.publish_pending(tuple(root_list))
        else:
            history.publish(additions, tuple(root_list))
        durations.append(time.perf_counter_ns() - start)
    return history, durations


def benchmark(revision, copies, updates, batch, repeats):
    records, roots = _scaled_records(revision, copies)
    rows = []
    for approach in APPROACHES:
        totals, publications, encodes, decodes = [], [], [], []
        for _ in range(repeats):
            history, durations = _publication_trial(
                approach, revision.target, records, roots, updates, batch
            )
            totals.append(sum(durations))
            publications.extend(durations)
            start = time.perf_counter_ns()
            data = encode_checkpoint(history.history[-1])
            encodes.append(time.perf_counter_ns() - start)
            start = time.perf_counter_ns()
            restored = decode_checkpoint(data)
            decodes.append(time.perf_counter_ns() - start)
            assert encode_checkpoint(restored) == data
        tracemalloc.start()
        measured, _ = _publication_trial(
            approach, revision.target, records, roots, updates, batch
        )
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        rows.append(
            {
                "approach": approach.__name__,
                "copies": copies,
                "starting_records": len(records),
                "updates": updates,
                "batch_size": batch,
                "repeats": repeats,
                "publication_ns": _summary(publications),
                "total_update_ns": _summary(totals),
                "encode_ns": _summary(encodes),
                "decode_ns": _summary(decodes),
                "checkpoint_bytes": len(data),
                "peak_index_allocation_bytes": peak,
                "history_revisions": len(measured.history),
                "memory_scope": "index/closure operations; prebuilt immutable payload bytes excluded",
            }
        )
    return rows


def negative_controls(corpus, revision):
    # Tempting no-copy publication: read-only proxy still aliases a mutable backing map.
    draft = {record.record_id: record for record in corpus.steps[0][0]}
    aliased = MappingProxyType(draft)
    before = set(aliased)
    draft.update((record.record_id, record) for record in corpus.steps[1][0])
    leaked = sorted(set(aliased) - before)
    # Graph validity cannot discover dependencies an author never declared.
    result = replace(revision.records["ci:runtime"], dependencies=())
    output_only = replace(
        revision,
        records=MappingProxyType({result.record_id: result}),
        roots=(result.record_id,),
        triggering_records=(result.record_id,),
    )
    structural_pass = encode_checkpoint(
        decode_checkpoint(encode_checkpoint(output_only))
    ) == encode_checkpoint(output_only)
    required = {
        "ci:workflow-text",
        "ci:input",
        "ci:source-context",
        "dependency:base-text",
        "dependency:head-text",
    }
    missing = sorted(required - set(material_closure(output_only)))
    first_empty = TraceRecord(
        "read:one", "experiment.lifecycle", "source_text", "empty.txt", b""
    )
    second_empty = replace(first_empty, record_id="read:two", scope="another-empty.txt")
    return {
        "aliased_read_only_proxy": {
            "historical_record_ids_added": leaked,
            "rejected": bool(leaked),
            "reason": "Published addressability changes when backing draft changes.",
        },
        "result_only_capture": {
            "structural_round_trip_passed": structural_pass,
            "missing_independent_consumer_basis": missing,
            "rejected": bool(missing),
            "reason": "Declared-edge closure alone cannot prove material completeness.",
        },
        "digest_only_identity": {
            "same_bytes": first_empty.payload == second_empty.payload,
            "scopes": [first_empty.scope, second_empty.scope],
            "byte_digests": [first_empty.digest, second_empty.digest],
            "rejected": first_empty != second_empty
            and first_empty.digest == second_empty.digest,
            "reason": "One content digest cannot identify two scoped read observations.",
        },
    }


def run(output, repeats=5, updates=30, copies=(1, 10, 50), batches=(1, 10)):
    corpus = build_retention_corpus()
    histories = []
    for approach in APPROACHES:
        history = approach(corpus.target)
        for step in corpus.steps:
            history.publish(*step)
        histories.append(history)
    trace_rows = []
    for left, right in zip(histories[0].history, histories[1].history, strict=True):
        encoded = encode_checkpoint(left)
        assert encoded == encode_checkpoint(right)
        assert encode_checkpoint(decode_checkpoint(encoded)) == encoded
        closure = material_closure(left)
        trace_rows.append(
            {
                "revision": left.number,
                "records": len(closure),
                "encoded_bytes": len(encoded),
                "payload_bytes": sum(
                    len(left.records[key].payload or b"") for key in closure
                ),
                "digest": hashlib.sha256(encoded).hexdigest(),
                "retention_gaps": retention_gaps(left),
                "byte_equal": True,
            }
        )
    revision = histories[0].history[-1]
    benchmark_rows = []
    for count in copies:
        for batch in batches:
            benchmark_rows.extend(benchmark(revision, count, updates, batch, repeats))
    files = [
        Path("experiments/run_workspace_revision_comparison.py"),
        Path("experiments/workspace_revision_representation.py"),
        Path("experiments/workspace_retention_corpus.py"),
        Path("experiments/tests/test_workspace_revision_representation.py"),
    ]
    result = {
        "protocol": "retention/revision-only-v1",
        "git_head_at_run": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "native_source_tree": subprocess.check_output(
            ["git", "rev-parse", "HEAD:src"], text=True
        ).strip(),
        "experiment_source_sha256": {
            str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in files
        },
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "machine": platform.machine(),
            "processor": next(
                (
                    line.split(":", 1)[1].strip()
                    for line in Path("/proc/cpuinfo").read_text().splitlines()
                    if line.startswith("model name")
                ),
                platform.processor(),
            ),
            "logical_cpus": os.cpu_count(),
            "filesystem": subprocess.check_output(
                ["stat", "-f", "-c", "%T", "."], text=True
            ).strip(),
        },
        "native_outcomes": corpus.native_outcomes,
        "trace": trace_rows,
        "negative_controls": negative_controls(corpus, revision),
        "affected_by_target_declaration": affected_dependents(
            revision, {"support:target-declaration"}
        ),
        "benchmarks": benchmark_rows,
        "limits": [
            "Offline fixtures, not real acquisition or model/extraction evidence",
            "Opaque pinned native-field encoding, no native rehydration/migration promise",
            "Declared closure completeness requires independent consumer/capture audit",
            "No durable store, crash recovery, concurrency, full consumer migration or replay",
            "Scaled copies test volume only; no throughput requirement established",
        ],
    }
    output.mkdir(parents=True, exist_ok=True)
    (output / "results.json").write_text(json.dumps(result, indent=2) + "\n")
    (output / "checkpoint-example.json").write_bytes(encode_checkpoint(revision))
    schema = {
        "purpose": "Minimal experiment closure schema; structural checks in decode_checkpoint, not production admission",
        "version": 1,
        "header": {
            "schema": "experiment.workspace-material-closure",
            "native_encoding": "pinned-tagged-fields-v1-no-rehydration",
            "lineage": "string",
            "revision": "nonnegative integer",
            "predecessor": "prior integer or null at revision zero",
            "target": "exact UTF-8 tagged target identity fields",
            "roots": "material consumer record IDs",
            "triggering_records": "material update IDs",
        },
        "record": {
            "id": "scoped stable identity",
            "owner": "native module or experiment.lifecycle",
            "kind": "native/source_text or simulated lifecycle kind",
            "scope": "exact native origin or target scope",
            "payload": "retained UTF-8 bytes represented as text; null only with explicit gap",
            "dependencies": "material record IDs",
            "gap": "explicit missing-content/provenance reason or null",
            "digest": "SHA-256 of exact payload bytes or null; consistency only",
        },
        "obligations": [
            "Every root/dependency/trigger resolves",
            "Identity collisions rejected",
            "No unknown version coercion",
            "Declared gaps remain explicit",
            "Retained zero bytes differ from missing content",
            "Closure completeness is not inferred from structural success",
        ],
    }
    (output / "checkpoint-schema-draft.json").write_text(
        json.dumps(schema, indent=2) + "\n"
    )
    print(
        json.dumps(
            {
                "revisions": len(trace_rows),
                "benchmark_rows": len(benchmark_rows),
                "final_checkpoint_bytes": trace_rows[-1]["encoded_bytes"],
                "output": str(output),
            }
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--repeats", type=int, default=5)
    args = parser.parse_args()
    if args.repeats < 1:
        parser.error("repeats must be positive")
    run(args.output, repeats=args.repeats)
