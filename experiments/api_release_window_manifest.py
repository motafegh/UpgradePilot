"""Shared experiment projection of admitted windows and retained observations.

Both trial writers use this boundary. Explicitly project known acquisition
records; arbitrary provider problems are never recursively serialized. Complete
eligibility refers only to the section window, not API meaning or product action.
"""

import hashlib
from dataclasses import asdict

from .api_change_source_acquisition import (
    AcquisitionProblem,
    DeclaredReleaseWindow,
    IncompleteDeclaredReleaseWindow,
    ReleaseWindowExamination,
)


def release_window_manifest(result: DeclaredReleaseWindow | AcquisitionProblem) -> dict:
    if isinstance(result, DeclaredReleaseWindow):
        return {
            "state": "available",
            "complete_window_eligible": True,
            "basis": result.association.basis,
            "repository": result.file.repository,
            "revision": result.file.revision,
            "path": result.file.path,
            "versions": result.ordered_versions,
            "sha256": result.full_text_sha256,
            "window_sha256": result.window_sha256,
            "coverage": result.coverage,
            "sections": [
                {
                    "version": s.version,
                    "start_line": s.start_line,
                    "start_offset": s.start_offset,
                    "end_offset": s.end_offset,
                    "characters": len(s.text),
                    "sha256": hashlib.sha256(s.text.encode("utf-8")).hexdigest(),
                    "text": s.text,
                }
                for s in result.sections
            ],
        }
    packet = {
        "state": "incomplete",
        "complete_window_eligible": False,
        "stage": result.stage,
        "reason": result.reason,
        "detail": result.detail,
    }
    evidence = result.evidence
    if isinstance(evidence, IncompleteDeclaredReleaseWindow):
        packet["source_context"] = {
            "interval": asdict(evidence.interval),
            "basis": evidence.release_associations[-1].basis,
            "release_metadata_urls": [
                a.release.source_url for a in evidence.release_associations
            ],
            "provenance_states": [
                a.provenance_result.state for a in evidence.release_associations
            ],
            "release_index_url": evidence.release_index.source_url,
            "ignored_index_versions": evidence.ignored_index_versions,
            "tags": [
                {**asdict(t), "retrieved_at": t.retrieved_at.isoformat()}
                for t in evidence.tags
            ],
            "tag_problems": [
                {"state": p.state, "tag": p.requested_tag, "detail": p.detail}
                for p in evidence.tag_problems
            ],
        }
        evidence = evidence.examination
    if isinstance(evidence, ReleaseWindowExamination):
        packet["section_examination"] = asdict(evidence)
    return packet
