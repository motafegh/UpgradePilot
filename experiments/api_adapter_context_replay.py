"""Replay adapter acquisition from a normally produced target-context manifest.

This is an experiment component replay, not fresh ordinary PR execution or product
report reopen. No expected paths/names/versions are added. Serialized syntax checks
are not evidence-authenticity or semantic checks; retain input hash and proof class.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path

from .api_adapter_exploration import AdapterDiscoverySeed, AdapterSourceExplorer
from .api_change_source_acquisition import TrialPublicSession
from .api_python_bindings import (
    BINDING_ANALYSIS_VERSION,
    MAX_BINDING_ORIGINS,
    MAX_BINDING_TRACE_STEPS,
    BindingAssessment,
    BindingTraceStep,
    binding_state,
    python_facts_manifest,
)
from .api_target_context import (
    DependencyDeclaration,
    ImportDependencyCandidate,
    ReferenceFact,
    file_sha256,
)


def _decode_binding(
    raw: dict, source: str, steps: tuple[BindingTraceStep, ...]
) -> BindingAssessment:
    """Saved-input shape/relationship checks, not source authenticity or reanalysis."""
    try:
        record = dict(raw)
        if any(
            not isinstance(record[key], (tuple, list))
            for key in ("possible_imports", "reasons", "trace")
        ):
            raise ValueError("Binding collections must be sequences.")
        record["possible_imports"] = tuple(record["possible_imports"])
        record["reasons"] = tuple(record["reasons"])
        if any(
            type(index) is not int or not 0 <= index < len(steps)
            for index in record["trace"]
        ):
            raise ValueError("Invalid binding trace index.")
        record["trace"] = tuple(steps[index] for index in record["trace"])
        binding = BindingAssessment(**record)
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError("Malformed binding assessment.") from exc
    if (
        type(binding.unknown_possible) is not bool
        or type(binding.unbound_possible) is not bool
        or not isinstance(binding.scope, str)
        or not binding.scope
        or len(binding.possible_imports) > MAX_BINDING_ORIGINS
        or not 1 <= len(binding.trace) <= MAX_BINDING_TRACE_STEPS
        or not binding.possible_imports
        and not binding.unknown_possible
        and not binding.unbound_possible
        or any(not isinstance(r, str) or not r for r in binding.reasons)
        or any(
            not isinstance(o, str) or not all(p.isidentifier() for p in o.split("."))
            for o in binding.possible_imports
        )
        or binding.possible_imports != tuple(sorted(set(binding.possible_imports)))
        or binding.state
        != binding_state(
            binding.possible_imports, binding.unknown_possible, binding.unbound_possible
        )
    ):
        raise ValueError("Inconsistent binding states/origins.")
    for step in binding.trace:
        if step.source_id != source:
            raise ValueError("Foreign reference binding trace.")
    return binding


def _decode_trace_steps(raw, sources) -> tuple[BindingTraceStep, ...]:
    try:
        if not isinstance(raw, (list, tuple)):
            raise TypeError("Trace table must be a sequence.")
        steps = tuple(BindingTraceStep(**step) for step in raw)
    except (TypeError, ValueError) as exc:
        raise ValueError("Malformed binding trace table.") from exc
    for step in steps:
        if (
            not isinstance(step.source_id, str)
            or step.source_id not in sources
            or not isinstance(step.scope, str)
            or not step.scope
            or any(
                type(n) is not int
                for n in (step.line, step.column, step.end_line, step.end_column)
            )
            or step.line < 1
            or step.column < 0
            or step.end_line < step.line
            or step.end_column < 0
            or step.end_line == step.line
            and step.end_column < step.column
            or not isinstance(step.operation, str)
            or not step.operation
            or not isinstance(step.name, str)
            or any(
                v is not None and not isinstance(v, str)
                for v in (step.origin, step.input_name)
            )
        ):
            raise ValueError("Malformed or foreign binding trace.")
    return steps


def decode_adapter_seed(packet: dict) -> AdapterDiscoverySeed:
    if packet.get("state") != "context_acquired":
        raise ValueError("Input lacks normally acquired target context.")
    target = packet["target"]
    version = target.get("binding_analysis_version", 1)
    if type(version) is not int or version not in {1, BINDING_ANALYSIS_VERSION}:
        raise ValueError("Unsupported binding-analysis packet version.")
    prefix = (
        packet["identity"]["repository"] + "@" + packet["identity"]["head_sha"] + ":"
    )
    if target["revision"] != packet["identity"]["head_sha"]:
        raise ValueError("Target identity differs from PR head.")
    sources = {f["source_id"] for f in target["files"]}
    if any(not s.startswith(prefix) for s in sources):
        raise ValueError("Foreign target source identity.")
    steps = (
        _decode_trace_steps(target.get("binding_trace_steps"), sources)
        if version == BINDING_ANALYSIS_VERSION
        else ()
    )
    candidates = []
    references = []
    for raw in target["candidates"]:
        d = dict(raw["declaration"])
        d["extras"] = tuple(d["extras"])
        if (
            raw["import_source_id"] not in sources
            or d["source_id"] not in sources
            or not all(
                part.isidentifier() for part in raw["imported_module"].split(".")
            )
        ):
            raise ValueError("Malformed candidate source/module relationship.")
        candidates.append(
            ImportDependencyCandidate(
                raw["imported_module"],
                DependencyDeclaration(**d),
                raw["import_source_id"],
                raw["import_line"],
                raw["basis"],
            )
        )
    for raw in target["references"]:
        if raw["source_id"] not in sources:
            raise ValueError("Reference source not acquired.")
        record = dict(raw)
        if version == BINDING_ANALYSIS_VERSION and set(record) != {
            "source_id",
            "line",
            "kind",
            "expression",
            "lexical_import",
            "binding_limit",
            "keyword_names",
            "positional_count",
            "binding",
        }:
            raise ValueError("Malformed version-2 reference fields.")
        if version == BINDING_ANALYSIS_VERSION and (
            type(record["line"]) is not int
            or record["line"] < 1
            or not isinstance(record["kind"], str)
            or record["kind"] not in {"call", "class_base"}
            or not isinstance(record["expression"], str)
            or type(record["positional_count"]) is not int
            or record["positional_count"] < 0
            or not isinstance(record["keyword_names"], (list, tuple))
            or any(
                not isinstance(name, str) or not name
                for name in record["keyword_names"]
            )
        ):
            raise ValueError("Malformed version-2 reference.")
        record["keyword_names"] = tuple(record["keyword_names"])
        if version == BINDING_ANALYSIS_VERSION:
            binding = _decode_binding(record.get("binding"), raw["source_id"], steps)
            positive = (
                binding.possible_imports[0] if binding.state == "established" else None
            )
            if record["lexical_import"] != positive or (
                record["binding_limit"] is None
            ) != (positive is not None):
                raise ValueError(
                    "Reference promotes or disagrees with binding assessment."
                )
            if positive is None and (
                not isinstance(record["binding_limit"], str)
                or not record["binding_limit"]
            ):
                raise ValueError("Uncertain reference needs an explicit limitation.")
            if positive is not None and not any(
                step.operation == "import"
                and step.origin
                and (positive == step.origin or positive.startswith(step.origin + "."))
                for step in binding.trace
            ):
                raise ValueError("Established reference lacks an import trace.")
            record["binding"] = binding
        elif record.get("binding") is not None:
            raise ValueError("Legacy packet cannot carry new binding assessments.")
        references.append(ReferenceFact(**record))
    return AdapterDiscoverySeed(tuple(candidates), tuple(references), version)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("context_manifest", type=Path)
    args = parser.parse_args()
    with args.context_manifest.open("rb") as handle:
        data = handle.read(1024 * 1024 + 1)
    if len(data) > 1024 * 1024:
        parser.error("Context manifest exceeds 1 MiB.")
    seed = decode_adapter_seed(json.loads(data))
    session = TrialPublicSession()
    result = AdapterSourceExplorer(session=session).explore(seed)
    manifest = {
        "mode": "adapter_stage_replay_of_recorded_normal_target_context",
        "timestamp": datetime.now(UTC).isoformat(),
        "input_sha256": hashlib.sha256(data).hexdigest(),
        "input_binding_analysis_version": seed.binding_analysis_version,
        "auth": "anonymous",
        "github_requests": session.github_requests,
        "code_sha256": {
            name: hashlib.sha256(
                Path(__file__).with_name(name).read_bytes()
            ).hexdigest()
            for name in (
                "api_adapter_exploration.py",
                "api_change_source_acquisition.py",
                "api_adapter_context_replay.py",
                "api_target_context.py",
                "api_python_bindings.py",
            )
        },
        "limits": {
            "release_identities": 4,
            "module_files": 12,
            "adapter_text_bytes": 2 * 1024 * 1024,
            "dependency_hops": 2,
        },
        "samples": [
            {
                "candidate": asdict(s.candidate),
                "depth": s.depth,
                "version": s.version,
                "selection": s.selection,
                "association_basis": s.association.basis,
                "provenance_state": s.association.provenance_result.state,
                "repository": s.file.repository,
                "revision": s.file.revision,
                "path": s.file.path,
                "sha256": file_sha256(s.file),
                "metadata": asdict(s.metadata),
                **python_facts_manifest(s.imports, s.references),
                "gaps": [asdict(g) for g in s.gaps],
            }
            for s in result.samples
        ],
        "problems": [
            {"stage": p.stage, "reason": p.reason, "detail": p.detail}
            for p in result.problems
        ],
        "omitted_candidates": [asdict(c) for c in result.omitted_candidates],
        "limitations": result.limitations,
        "proof": "fresh adapter reads from retained producer facts; not fresh full PR path, resolution, model or compatibility acceptance",
    }
    # Machine-consumed evidence uses compact JSON; whitespace must not consume
    # the existing saved-input budget without adding any retained knowledge.
    print(json.dumps(manifest, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
