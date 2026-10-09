"""Bounded replacement migration proof; progressive results, no product cutover."""

from __future__ import annotations

import argparse
import json
import tempfile
from collections import Counter
from contextlib import ExitStack, contextmanager
from dataclasses import asdict, replace
from hashlib import sha256
from importlib import import_module
from pathlib import Path
from unittest.mock import patch

from experiments.workspace_replacement_migration import (
    NATIVE_OPERATIONS,
    NOW,
    ProjectionUnavailable,
    add_projection_pressure,
    capture_normal_pipeline,
    native_field_projection,
    project_legacy_result,
)
from experiments.workspace_revision_representation import (
    decode_checkpoint,
    encode_checkpoint,
    material_closure,
)
from experiments.workspace_seam_checkpoints import MemoryCheckpoints, SQLiteCheckpoints
from upgradepilot import investigation as application
from upgradepilot import report_projection as report_owner
from upgradepilot.ci.dependency_state import (
    RequirementSatisfiedAtCommandCompletion,
    RequirementStateProblem,
)
from upgradepilot.maintainer_action import synthesize_maintainer_action
from upgradepilot.report import render_investigation_report
from upgradepilot.report_file import (
    decode_report,
    encode_report,
    read_report,
    save_report,
)
from upgradepilot.report_projection import project_investigation_report


def comparable_report(report):
    """Only generated report UUID is excluded; source IDs/references remain compared."""
    return replace(report, report_id="00000000-0000-0000-0000-000000000000")


@contextmanager
def count_consumer_attempts():
    """Parity deliberately invokes synthesis/report; count their real attempts too."""
    counts = Counter()
    synthesize = synthesize_maintainer_action
    project_report = project_investigation_report

    def counted_synthesis(*args, **kwargs):
        counts["synthesis_attempts"] += 1
        return synthesize(*args, **kwargs)

    def counted_report(*args, **kwargs):
        counts["report_attempts"] += 1
        return project_report(*args, **kwargs)

    with (
        patch(__name__ + ".synthesize_maintainer_action", counted_synthesis),
        patch.object(report_owner, "synthesize_maintainer_action", counted_synthesis),
        patch(__name__ + ".project_investigation_report", counted_report),
    ):
        yield counts


@contextmanager
def forbid_producer_reentry():
    """Independent call proof after capture ends; existing consumers may copy/synthesize.

    Reject current application/domain aliases, not just compare counters whose hooks
    have already exited. This is a bounded execution oracle, not process isolation.
    """
    with ExitStack() as stack:
        targets = {
            (application, "investigate_public_pull_request"),
            (application, "evaluate_support_drop_runtime"),
        }
        for name in NATIVE_OPERATIONS:
            operation = getattr(application, name)
            targets.add((application, name))
            targets.add((import_module(operation.__module__), operation.__name__))
        targets.add(
            (
                import_module("upgradepilot.upstream.support_drop"),
                "evaluate_support_drop_runtime",
            )
        )
        for module, name in targets:
            stack.enter_context(
                patch.object(
                    module,
                    name,
                    side_effect=AssertionError(f"Consumer/restore re-entered {name}"),
                )
            )
        yield


def _native_oracle(result):
    assert result.dependency_result.old_version == "1.0"
    assert result.dependency_result.proposed_version == "2.0"
    runtime = result.runtime_dependency_state_result.assessments
    assert len(runtime) == 2
    assert isinstance(runtime[0].result, RequirementSatisfiedAtCommandCompletion)
    assert isinstance(runtime[1].result, RequirementStateProblem)
    assert runtime[1].result.state == "unresolved"
    assert (
        result.python_support_drop_pre_investigation_result.applicability.state
        == "unresolved"
    )
    assert (
        result.python_support_drop_impact_result.applicability.state
        == "established_applicable"
    )
    assert result.target_python_relevance_result.state == "declared_python_overlap"
    assert result.artifact_serviceability_impact_result is None


def trial(backend, directory, progress=lambda family, data: None):
    port = (
        MemoryCheckpoints()
        if backend == "memory"
        else SQLiteCheckpoints(directory / "store", create=True)
    )
    try:
        with patch(
            "requests.sessions.Session.send",
            side_effect=AssertionError("Offline migration attempted egress"),
        ):
            capture, original = capture_normal_pipeline(port)
            _native_oracle(original)
            expected_calls = Counter(capture.calls)
            assert expected_calls["orchestration:investigate_public_pull_request"] == 1
            assert expected_calls["acquisition:pypi.release"] == 2
            assert expected_calls["native:evaluate_python_support_drop_impact"] == 2
            assert expected_calls["extractor:deterministic_fixture"] == 1
            assert expected_calls["acquisition:repository.target"] == 1
            progress(
                "native",
                {
                    "calls": dict(expected_calls),
                    "oracle": "independent native fact/state checks passed",
                },
            )
            # The remaining consumer/recovery operations execute with processing
            # forbidden independently of the now-finished capture counters.
            with (
                forbid_producer_reentry(),
                count_consumer_attempts() as consumer_counts,
            ):
                return _consumer_trial(
                    capture,
                    original,
                    expected_calls,
                    consumer_counts,
                    port,
                    directory,
                    progress,
                )
    finally:
        if backend == "sqlite":
            port.close()


def _consumer_trial(
    capture, original, expected_calls, consumer_counts, port, directory, progress
):
    before = encode_checkpoint(capture.revision)
    original_synthesis = synthesize_maintainer_action(original)
    original_report = project_investigation_report(original, now=NOW)
    direct = native_field_projection(capture.revision, capture.values)
    refusals = {}
    for name, consumer in (
        ("synthesis", synthesize_maintainer_action),
        ("report", lambda value: project_investigation_report(value, now=NOW)),
    ):
        try:
            consumer(direct)
        except TypeError as error:
            refusals[name] = str(error)
        else:
            raise AssertionError(
                "Current consumers unexpectedly admitted direct projection"
            )
    progress("direct_consumer_refusal", refusals)
    projected = project_legacy_result(capture.revision, capture.values)
    assert projected == original and projected is not original
    synthesis = synthesize_maintainer_action(projected)
    report = project_investigation_report(projected, now=NOW)
    assert asdict(synthesis) == asdict(original_synthesis)
    assert synthesis.source_investigation is projected
    assert comparable_report(report) == comparable_report(original_report)
    assert synthesis.action == report.action.state == "abstain"
    assert any(
        "Runtime requirement state" in text for text in synthesis.residual_uncertainty
    )
    assert any(
        "not establish complete impact-candidate" in text
        for text in synthesis.claim_limits
    )
    assert any("safe or unsafe" in text for text in synthesis.claim_limits)
    assert encode_checkpoint(capture.revision) == before
    progress(
        "legacy_parity",
        {
            "all_fields": True,
            "synthesis": "equal including original fact/unknown/limit meanings",
            "report": "equal except generated report UUID; fixed time; source IDs unchanged",
        },
    )
    old_revision = add_projection_pressure(capture)
    final = encode_checkpoint(capture.revision)
    assert encode_checkpoint(capture.history.history[old_revision]) == before
    after = project_legacy_result(capture.revision, capture.values)
    assert after == projected
    after_report = project_investigation_report(after, now=NOW)
    assert comparable_report(after_report) == comparable_report(report)
    assert not hasattr(after, "unfinished_operations")
    assert capture.calls == expected_calls
    recovered = port.load()
    assert encode_checkpoint(recovered) == final
    assert decode_checkpoint(final).records == recovered.records
    try:
        project_legacy_result(recovered, {})
    except ProjectionUnavailable as error:
        assert "unsupported_native_codec" in str(error)
        cold_restart = str(error)
    else:
        raise AssertionError(
            "Cold checkpoint bytes silently became trusted native objects"
        )
    # Same-process recovered projection is explicitly backed by this producer's
    # live values; it is not cold-restart hydration or continuation authority.
    assert project_legacy_result(recovered, capture.values) == after
    kinds = {record.kind for record in recovered.records.values()}
    assert {"view", "proposal", "unfinished_operation", "source_text"} <= kinds
    assert "migration:unfinished" in material_closure(recovered)
    assert (
        json.loads(recovered.records["migration:unfinished"].payload)["completion"]
        == "unknown"
    )
    assert (
        json.loads(recovered.records["migration:proposal"].payload)["evaluation"]
        == "unsupported_no_admitted_evaluator"
    )
    assert (
        json.loads(recovered.records["migration:view"].payload)["examined_or_used"]
        == "unknown"
    )
    assert "native:evaluate_dependency_ci_coverage:1:input" in material_closure(
        recovered
    )
    path = directory / "report.json"
    save_report(report, path)
    opened = read_report(path)
    assert opened == decode_report(encode_report(report)) == report
    assert render_investigation_report(
        opened, saved=True
    ) == render_investigation_report(report, saved=True)
    assert capture.calls == expected_calls
    progress(
        "lifecycle_retention",
        {
            "cold_restart": cold_restart,
            "legacy_projection_cannot_represent": [
                "source-input bundle",
                "revision/history",
                "view delivery/use",
                "proposal/evaluation status",
                "unknown completion/retry restriction",
            ],
            "checkpoint_equal": True,
            "offline_saved_report_equal": True,
            "consumer_or_restore_native_calls": 0,
        },
    )
    sources = [
        {"scope": record.scope, "sha256": record.digest, "bytes": len(record.payload)}
        for record in recovered.records.values()
        if record.kind == "source_text"
    ]
    summary = {
        "calls": dict(sorted(expected_calls.items())),
        "native_acquisition_port_returns": sum(
            count
            for name, count in expected_calls.items()
            if name.startswith("acquisition:")
        ),
        "native_owner_calls": sum(
            count
            for name, count in expected_calls.items()
            if name.startswith("native:")
        ),
        "model_calls": 0,
        "consumer_extra_native_or_acquisition_calls": 0,
        "parity_consumer_attempts": dict(consumer_counts),
        "runtime_results": [
            type(item.result).__name__
            for item in original.runtime_dependency_state_result.assessments
        ],
        "native_before": "unresolved",
        "native_after": "established_applicable",
        "action": "abstain",
        "residual_uncertainty": synthesis.residual_uncertainty,
        "report_assessments": [
            (item.assessment_id, item.state, item.strength)
            for item in report.assessments
        ],
        "direct_refusal": refusals,
        "cold_restart": cold_restart,
        "revision": recovered.number,
        "records": len(material_closure(recovered)),
        "checkpoint_sha256": sha256(final).hexdigest(),
        "checkpoint_bytes": len(final),
        "exact_sources": sources,
        "report_time": report.generated_at,
        "report_material_sha256": sha256(
            encode_report(comparable_report(report))
        ).hexdigest(),
        "producer_result_fields": len(projected.__dataclass_fields__),
    }
    return summary, final, report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    result = {
        "status": "running",
        "proof_class": "normal offline native orchestration plus synthetic lifecycle pressure",
        "production_cutover": False,
        "families": [],
        "cases": [],
    }

    def flush():
        (args.output / "results.json").write_text(
            json.dumps(result, sort_keys=True, indent=2) + "\n"
        )

    flush()
    try:
        outputs = []
        for backend in ("memory", "sqlite"):

            def progress(family, data, selected_backend=backend):
                result["families"].append(
                    {"backend": selected_backend, "family": family, "data": data}
                )
                flush()

            with tempfile.TemporaryDirectory() as directory:
                summary, checkpoint, report = trial(backend, Path(directory), progress)
            result["cases"].append({"backend": backend, "summary": summary})
            flush()
            outputs.append((summary, checkpoint, comparable_report(report)))
        assert outputs[0] == outputs[1]
        (args.output / "checkpoint.json").write_bytes(outputs[0][1])
        (args.output / "report.json").write_bytes(encode_report(outputs[0][2]))
        paths = [
            Path(__file__),
            Path("experiments/workspace_replacement_migration.py"),
            Path("experiments/tests/test_workspace_replacement_migration.py"),
            Path("experiments/workspace_revision_representation.py"),
            Path("experiments/workspace_seam_checkpoints.py"),
            Path("experiments/workspace_checkpoint_stores.py"),
        ]
        result["source_sha256"] = {
            str(path): sha256(path.read_bytes()).hexdigest() for path in paths
        }
        tree = sha256()
        for path in sorted(Path("src/upgradepilot").rglob("*.py")):
            tree.update(str(path).encode() + b"\0" + path.read_bytes() + b"\0")
        result["native_tree_sha256"] = tree.hexdigest()
        result["backend_equality"] = (
            "exact summaries/checkpoints and report except generated UUID"
        )
        result["status"] = "complete"
        flush()
    except Exception as error:
        result.update(status="failed", error=f"{type(error).__name__}: {error}")
        flush()
        raise
    print(json.dumps({"status": result["status"], "cases": result["cases"]}, indent=2))


if __name__ == "__main__":
    main()
