#!/usr/bin/env python3
"""Probe one real UpgradePilot semantic boundary with negated upstream release prose.

This experiment intentionally reuses the current product-owned support-drop path instead of
inventing a new planner contract::

    exact tagged changelog + trusted crossed-release index
    -> build_crossed_release_source_window(...)
    -> LocalSupportDropExtractor
    -> CandidateUpstreamClaimResult
    -> validate_support_drop_candidates(...)
    -> grounded support-drop claim OR explicit problem

The purpose is evidence-first engineering.  The source sentence is purpose-built test data, but
all parsing, model invocation, candidate reconstruction, and deterministic grounding are the real
UpgradePilot implementations.

The first case is deliberately simple and discriminating: the exact source explicitly says that
Python 3.8 support was *not* dropped and remains supported.  A correct semantic extractor should
therefore produce no support-drop candidate.  If the model nevertheless selects that line as a
support drop, current deterministic grounding can verify its exact attribution without independently
proving the English negation semantics.  That is the boundary this probe is designed to expose.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
from pathlib import Path

from upgradepilot.upstream.changelog import (
    CrossedReleaseSourceWindow,
    build_crossed_release_source_window,
)
from upgradepilot.upstream.claim import (
    CandidateUpstreamClaimResult,
    GroundedPythonSupportDropClaim,
    UpstreamSupportDropClaimProblem,
    validate_support_drop_candidates,
)
from upgradepilot.upstream.interval import (
    AuthoritativeUpstreamIntervalEvidence,
    CrossedReleaseIndexEvidence,
    DependencyReleaseInterval,
    TaggedChangelogEvidence,
    assemble_upstream_interval_authority,
)
from upgradepilot.upstream.support_drop_extractor import LocalSupportDropExtractor

CASE_ID = "e1-negated-python-support-drop"
OUTPUT_PATH = Path("/tmp/upgradepilot-b2-x1-e1-negated-support-drop.json")
_REPOSITORY = "example/friendly-bard"
_RESOLVED_COMMIT = "a" * 40
_VERSIONS = ("2.7", "2.8", "2.8.4")

# Purpose-built semantic pressure, not historical upstream evidence.
_NEGATED_CHANGELOG = (
    "## 2.8.4\n"
    "- Fix selector behavior.\n"
    "## 2.8\n"
    "- Python 3.8 support was not dropped; Python 3.8 remains supported.\n"
    "## 2.7\n"
    "- Add a selector.\n"
)


@dataclass(frozen=True, slots=True)
class ProbeInputs:
    """Exact trusted authority plus the deterministic model-facing release window."""

    authority: AuthoritativeUpstreamIntervalEvidence
    window: CrossedReleaseSourceWindow


@dataclass(frozen=True, slots=True)
class ProbeObservation:
    """One live model observation and the downstream deterministic grounding result."""

    case_id: str
    candidate_result: CandidateUpstreamClaimResult
    grounded_result: GroundedPythonSupportDropClaim | UpstreamSupportDropClaimProblem
    classification: str


def build_probe_inputs() -> ProbeInputs:
    """Build the exact current product evidence objects used by the live semantic adapter."""

    interval = DependencyReleaseInterval(
        package="friendly-bard",
        normalized_package="friendly-bard",
        old_version="2.6",
        proposed_version="2.8.4",
    )
    crossed = CrossedReleaseIndexEvidence(
        repository=_REPOSITORY,
        interval=interval,
        ordered_versions=_VERSIONS,
        source_url="https://pypi.org/pypi/friendly-bard/json",
        retrieved_at=datetime(2026, 8, 28, 12, 0, tzinfo=timezone.utc),
    )
    changelog = TaggedChangelogEvidence(
        repository=_REPOSITORY,
        interval=interval,
        resolved_commit_sha=_RESOLVED_COMMIT,
        path="docs/changelog.md",
        content=_NEGATED_CHANGELOG,
    )

    authority_result = assemble_upstream_interval_authority(
        interval,
        _REPOSITORY,
        crossed_releases=crossed,
        tagged_changelogs=(changelog,),
    )
    if not isinstance(authority_result, AuthoritativeUpstreamIntervalEvidence):
        raise RuntimeError(
            "Purpose-built E1 evidence did not form authoritative upstream interval evidence: "
            f"{authority_result!r}"
        )

    window_result = build_crossed_release_source_window(
        crossed,
        changelog,
        max_characters=4_096,
    )
    if not isinstance(window_result, CrossedReleaseSourceWindow):
        raise RuntimeError(
            "Purpose-built E1 changelog did not form a crossed-release source window: "
            f"{window_result!r}"
        )

    return ProbeInputs(authority=authority_result, window=window_result)


def run_live_probe() -> ProbeObservation:
    """Run the adopted local semantic extractor, then apply real deterministic grounding."""

    inputs = build_probe_inputs()
    candidate_result = LocalSupportDropExtractor().extract(inputs.window)
    grounded_result = validate_support_drop_candidates(
        inputs.authority,
        candidate_result,
    )

    return ProbeObservation(
        case_id=CASE_ID,
        candidate_result=candidate_result,
        grounded_result=grounded_result,
        classification=_classify(grounded_result),
    )


def _classify(
    result: GroundedPythonSupportDropClaim | UpstreamSupportDropClaimProblem,
) -> str:
    if isinstance(result, GroundedPythonSupportDropClaim):
        return "false_positive_grounded_support_drop"
    if result.state == "no_support_drop_claim":
        return "correct_no_support_drop"
    return f"conservative_or_other_problem:{result.state}"


def _render_observation(observation: ProbeObservation) -> dict[str, object]:
    inputs = build_probe_inputs()
    return {
        "kind": "b2_x1_e1_support_drop_semantic_probe",
        "case_id": observation.case_id,
        "expected_semantics": "Python 3.8 support is explicitly NOT dropped.",
        "source_text": inputs.window.text,
        "candidate_result": asdict(observation.candidate_result),
        "grounded_result_type": type(observation.grounded_result).__name__,
        "grounded_result": asdict(observation.grounded_result),
        "classification": observation.classification,
    }


def main() -> int:
    observation = run_live_probe()
    output = _render_observation(observation)
    OUTPUT_PATH.write_text(
        json.dumps(output, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    print(f"case: {observation.case_id}")
    print(f"candidate_state: {observation.candidate_result.state}")
    print(f"candidate_count: {len(observation.candidate_result.candidates)}")
    print(f"grounded_result: {type(observation.grounded_result).__name__}")
    print(f"classification: {observation.classification}")
    print(f"output: {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
