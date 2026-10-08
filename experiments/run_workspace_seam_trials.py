"""Reproducible offline consumer/lifecycle comparison; evidence is flushed per case.

Run from repository root with PYTHONPATH=src. Four traces (memory/SQLite × Python/wire)
share independent expected outcomes. Concrete replay inputs are synthetic; matching
traces are lifecycle fidelity, never semantic correctness or Investigator superiority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import statistics
import tempfile
import time
from dataclasses import replace
from pathlib import Path

from experiments.workspace_investigator_seam import (
    AcquisitionRequest,
    Binding,
    InvestigatorPort,
    Outcome,
    RevisionRef,
    TraceRecord,
    WorkspaceHost,
    decode_request,
    encode_projection,
    encode_request,
    payload,
)
from experiments.workspace_revision_representation import encode_checkpoint
from experiments.workspace_seam_checkpoints import MemoryCheckpoints, SQLiteCheckpoints
from experiments.workspace_seam_native import build_native_fixture


class ScriptedConsumer:
    """Reads a native need projection; proposes only, never grants admission or truth."""

    def __init__(self, port, transport):
        self.port = port
        self.transport = transport

    def plan(self):
        view = self.port.read(("support:need", "support:candidate"))
        # Only wire mode serializes the response. Both read the same native need fields;
        # neither consults a host policy, persistence object or native Python fixture.
        if self.transport == "wire":
            value = json.loads(encode_projection(view))
            need = json.loads(value["delivered"][0]["content"])["fields"]
            revision = RevisionRef(**value["revision"])
            basis = tuple(Binding(**item) for item in value["basis"])
            method = value["method"]
        else:
            need = json.loads(view.delivered[0].payload)["fields"]
            revision, basis, method = view.revision, view.basis, view.method
        request = AcquisitionRequest(
            "investigator:scripted-read",
            revision,
            basis,
            "read_target_declaration",
            f"{need['repository']}@{need['revision']}:{need['path']}",
            method,
            need["proposition_key"],
        )
        outcome = (
            self.port.request_bytes(encode_request(request))
            if self.transport == "wire"
            else self.port.request(request)
        )
        assert outcome.status == "admitted", outcome
        return request, view


def counter(host, content=None):
    record = TraceRecord(
        "counter:gap",
        "offline.fixture",
        "counterevidence",
        host.ref.target,
        None,
        gap="owner_relevant_counterobservation_unavailable",
    )
    host.retain_evidence(
        content or record, role="counterevidence", candidate="support:candidate"
    )


EXPECTED = {
    "normal": "observation_admitted",
    "unrelated": "observation_admitted",
    "material": "material_basis_changed",
    "counter_before": "material_basis_changed",
    "counter_content_before": "material_basis_changed",
    "target": "target_changed",
    "method": "method_changed",
    "capability": "capability_unavailable",
    "authority": "current_authority_unavailable",
    "duplicate": "duplicate_delivery",
    "unknown": "completion_unknown_no_auto_retry",
    "failed": "already_completed",
    "restore": "observation_admitted",
    "restore_method": "method_changed",
    "restore_capability": "capability_unavailable",
    "restore_target": "target_changed",
    "omitted": "observation_admitted",
    "counter_after": "requires_owner_revalidation",
    "counter_content_after": "requires_owner_revalidation",
    "cas_unrelated": "observation_admitted",
    "cas_material": "material_basis_changed",
}


def scenario(name, backend, transport, directory):
    fixture = build_native_fixture()
    port = (
        MemoryCheckpoints()
        if backend == "memory"
        else SQLiteCheckpoints(directory / "store", create=True)
    )
    competing_port = None
    try:
        host = WorkspaceHost(port, fixture.policy)
        host.seed(
            fixture.initial, {"candidate": "support:candidate", "need": "support:need"}
        )
        host.continue_current()
        consumer = ScriptedConsumer(InvestigatorPort(host), transport)
        request, view = consumer.plan()
        host.start(
            request.request_id
        )  # Admitted capability driver, outside consumer port.
        states = []
        if name in {
            "unrelated",
            "material",
            "counter_before",
            "counter_content_before",
        }:
            if name == "unrelated":
                host.retain_evidence(
                    TraceRecord(
                        "annotation", "fixture", "annotation", "other", b'"unrelated"'
                    ),
                    role="context",
                    candidate="other",
                )
            elif name == "material":
                host.rebind(
                    "candidate",
                    TraceRecord(
                        "candidate:updated",
                        "fixture",
                        "native",
                        host.ref.target,
                        b'"new premise"',
                    ),
                )
            else:
                counter(
                    host,
                    fixture.counter_source()
                    if name == "counter_content_before"
                    else None,
                )
        if name == "counter_content_before":
            assert [item.record_id for item in host.evaluation_inputs()] == [
                "counter:readme"
            ]
        if name in {"target", "method", "capability", "authority"}:
            changes = {
                "target": {"target": host.ref.target.replace("a" * 40, "d" * 40)},
                "method": {"method": "native-support-v2"},
                "capability": {"capabilities": frozenset()},
                "authority": {"authorized": False},
            }
            host.policy = replace(host.policy, **changes[name])
        if name.startswith("restore") or name == "unknown":
            host = WorkspaceHost(port, fixture.policy)
            states.append(
                "historical_only" if not host.active else "incorrect_active_restore"
            )
            suffix = name.removeprefix("restore_")
            if suffix == "method":
                host.policy = replace(host.policy, method="native-support-v2")
            elif suffix == "capability":
                host.policy = replace(host.policy, capabilities=frozenset())
            elif suffix == "target":
                host.policy = replace(
                    host.policy, target=host.ref.target.replace("a" * 40, "d" * 40)
                )
            states.append(host.continue_current().status)
        if name.startswith("cas_"):
            if backend == "sqlite":
                competing_port = SQLiteCheckpoints(directory / "store")
            competitor = WorkspaceHost(competing_port or port, fixture.policy)
            competitor.continue_current()
            if name == "cas_material":
                competitor.rebind(
                    "candidate",
                    TraceRecord(
                        "candidate:updated",
                        "fixture",
                        "native",
                        host.ref.target,
                        b'"new premise"',
                    ),
                )
            else:
                competitor.retain_evidence(
                    TraceRecord(
                        "annotation", "fixture", "annotation", "other", b'"unrelated"'
                    ),
                    role="context",
                    candidate="other",
                )
            conflict = host.observe(request.request_id, fixture.result())
            assert conflict.status == "publication_conflict", conflict
            states.append(conflict.status)
            host.refresh()
            host.continue_current()
        if name == "unknown":
            outcome = host.start(request.request_id)
        elif name == "failed":
            host.attempt_problem(
                request.request_id,
                "offline_provider_unavailable",
                completion_known=True,
            )
            outcome = host.start(request.request_id)
            assert host.evaluation_inputs() == ()
        else:
            outcome = host.observe(request.request_id, fixture.result())
            if name == "duplicate":
                number = host.ref.number
                outcome = host.observe(request.request_id, fixture.result())
                assert host.ref.number == number and len(host.evaluation_inputs()) == 1
            if name in {"counter_after", "counter_content_after"}:
                fixture.evaluate(host)
                evaluation = next(
                    record
                    for record in host.revision.records.values()
                    if record.kind == "domain_evaluation"
                )
                old_assessment = host.revision.records["native:assessment"]
                counter(
                    host,
                    fixture.counter_source()
                    if name == "counter_content_after"
                    else None,
                )
                selected = host.evaluation_inputs()
                assert {item.record_id for item in selected} == {
                    "target:source",
                    "counter:readme"
                    if name == "counter_content_after"
                    else "counter:gap",
                }
                status = host.evaluation_basis_status(evaluation.record_id)
                fixture.evaluate(host)
                assert host.revision.records["native:assessment"] == old_assessment
                states.append(status)
                outcome = Outcome(status)
            if name in {"normal", "unrelated", "restore", "omitted", "cas_unrelated"}:
                fixture.evaluate(host)
                consumer = ScriptedConsumer(InvestigatorPort(host), transport)
                omitted = consumer.port.read(("support:need",))
                assert "target:source" in omitted.omitted_but_addressable
                wrong = consumer.port.propose(
                    "proposal:undelivered",
                    omitted,
                    ("target:source",),
                    "scripted meaning",
                )
                assert wrong.status == "citation_not_delivered_in_view"
                delivered = consumer.port.read(("target:source",))
                proposal = consumer.port.propose(
                    "proposal:meaning",
                    delivered,
                    ("target:source",),
                    "scripted meaning",
                )
                assert proposal.status == "proposal_retained_evaluation_unsupported"
                states.extend((wrong.status, proposal.status))
        assert outcome.status == EXPECTED[name], (name, outcome)
        evaluations = [
            payload(record)
            for record in host.revision.records.values()
            if record.kind == "domain_evaluation"
        ]
        if evaluations:
            assert evaluations[-1]["adequacy"] == "unsupported_no_admitted_evaluator"
        data = encode_checkpoint(host.revision)
        restored = WorkspaceHost(port, fixture.policy)
        assert encode_checkpoint(restored.revision) == data and not restored.active
        return {
            "case": name,
            "backend": backend,
            "transport": transport,
            "outcome": outcome.status,
            "states": states,
            "revision": host.ref.number,
            "checkpoint_sha256": hashlib.sha256(data).hexdigest(),
            "evidence_inputs": [item.record_id for item in host.evaluation_inputs()],
            "domain_outcomes": [item["status"] for item in evaluations],
            "adequacy": "unsupported_no_admitted_evaluator",
            "request_bytes": len(encode_request(request)),
            "projection_bytes": len(encode_projection(view)),
        }, data
    finally:
        if competing_port:
            competing_port.close()
        if backend == "sqlite":
            port.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    results = {
        "status": "running",
        "python": platform.python_version(),
        "cases": [],
        "limits": [
            "offline synthetic fixture",
            "no semantic correctness or superiority",
            "no full native codec/capture",
            "no power-loss or physical-write proof",
            "no product adoption or migration",
        ],
    }

    def flush():
        (args.output / "results.json").write_text(
            json.dumps(results, indent=2, sort_keys=True) + "\n"
        )

    flush()
    try:
        for name, expected in EXPECTED.items():
            hashes = set()
            for backend in ("memory", "sqlite"):
                for transport in ("python", "wire"):
                    with tempfile.TemporaryDirectory() as directory:
                        result, checkpoint = scenario(
                            name, backend, transport, Path(directory)
                        )
                        results["cases"].append(result)
                        hashes.add(result["checkpoint_sha256"])
                        if (
                            name == "normal"
                            and backend == "sqlite"
                            and transport == "wire"
                        ):
                            (args.output / "interaction-checkpoint.json").write_bytes(
                                checkpoint
                            )
                    flush()
            assert len(hashes) == 1, (name, "transport/backend trace divergence")
            print(f"{name}: four matching traces, {expected}", flush=True)
        fixture = build_native_fixture()
        host = WorkspaceHost(MemoryCheckpoints(), fixture.policy)
        host.seed(
            fixture.initial, {"candidate": "support:candidate", "need": "support:need"}
        )
        host.continue_current()
        request = fixture.request(host.read(("support:need",)))
        envelope = encode_request(request)
        costs = {"typed_construction": [], "encode_decode": []}
        for _ in range(7):
            for name, operation in (
                ("typed_construction", lambda: replace(request)),
                ("encode_decode", lambda: decode_request(encode_request(request))),
            ):
                start = time.perf_counter_ns()
                for _ in range(1000):
                    assert operation() == request
                costs[name].append((time.perf_counter_ns() - start) / 1000 / 1000)
        results["envelope_cost"] = {
            "unit": "microseconds_per_request",
            "batch": 1000,
            "repeats": 7,
            "request_bytes": len(envelope),
            "samples": costs,
            "medians": {
                name: statistics.median(values) for name, values in costs.items()
            },
            "scope": "warm local parser/construction only; host validation and persistence excluded",
        }
        paths = [
            Path(__file__),
            Path("experiments/workspace_investigator_seam.py"),
            Path("experiments/workspace_seam_checkpoints.py"),
            Path("experiments/workspace_seam_native.py"),
            Path("experiments/tests/test_workspace_investigator_seam.py"),
        ]
        results["source_sha256"] = {
            str(
                path.relative_to(Path.cwd()) if path.is_absolute() else path
            ): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in paths
        }
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteCheckpoints(Path(directory) / "settings", create=True)
            try:
                results["provisional_store_settings"] = store.store.settings()
            finally:
                store.close()
        native_files = sorted(Path("src/upgradepilot").rglob("*.py"))
        tree_hash = hashlib.sha256()
        for path in native_files:
            tree_hash.update(str(path).encode() + b"\0" + path.read_bytes() + b"\0")
        results["native_tree_sha256"] = tree_hash.hexdigest()
        for path in (
            Path("experiments/workspace_retention_corpus.py"),
            Path("experiments/workspace_revision_representation.py"),
            Path("experiments/workspace_checkpoint_stores.py"),
        ):
            results["source_sha256"][str(path)] = hashlib.sha256(
                path.read_bytes()
            ).hexdigest()
        results["status"] = "complete"
    except Exception as error:
        results["status"] = "failed"
        results["error"] = f"{type(error).__name__}: {error}"
        flush()
        raise
    flush()


if __name__ == "__main__":
    main()
