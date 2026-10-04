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
from .api_target_context import (
    DependencyDeclaration,
    ImportDependencyCandidate,
    ReferenceFact,
    file_sha256,
)


def decode_adapter_seed(packet: dict) -> AdapterDiscoverySeed:
    if packet.get("state") != "context_acquired":
        raise ValueError("Input lacks normally acquired target context.")
    target = packet["target"]
    prefix = (
        packet["identity"]["repository"] + "@" + packet["identity"]["head_sha"] + ":"
    )
    if target["revision"] != packet["identity"]["head_sha"]:
        raise ValueError("Target identity differs from PR head.")
    sources = {f["source_id"] for f in target["files"]}
    if any(not s.startswith(prefix) for s in sources):
        raise ValueError("Foreign target source identity.")
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
        record["keyword_names"] = tuple(record["keyword_names"])
        references.append(ReferenceFact(**record))
    return AdapterDiscoverySeed(tuple(candidates), tuple(references))


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
                "imports": [asdict(f) for f in s.imports],
                "references": [asdict(r) for r in s.references],
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
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
