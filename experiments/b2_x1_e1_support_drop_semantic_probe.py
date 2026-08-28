#!/usr/bin/env python3
"""Probe the real UpgradePilot support-drop semantic boundary with controlled release prose.

This experiment intentionally reuses the current product-owned support-drop path instead of
inventing a new planner contract::

    exact tagged changelog + trusted crossed-release index
    -> build_crossed_release_source_window(...)
    -> LocalSupportDropExtractor
    -> CandidateUpstreamClaimResult
    -> validate_support_drop_candidates(...)
    -> grounded support-drop claim OR explicit problem

The source prose is purpose-built experiment data, but parsing, model invocation, candidate
reconstruction, and deterministic grounding are the real UpgradePilot implementations.

The probe cases are deliberately small and discriminating. They test whether the adopted model
correctly distinguishes a *current* support drop from nearby wording that contains the same Python
version but explicitly means something else. If the model selects a false support-drop candidate,
current deterministic grounding can still verify exact attribution without independently proving
the English semantics. That is the boundary this probe is designed to observe.
"""

from __future__ import annotations

import argparse
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

_REPOSITORY = "example/friendly-bard"
_RESOLVED_COMMIT = "a" * 40
_VERSIONS = ("2.7", "2.8", "2.8.4")


@dataclass(frozen=True, slots=True)
class SemanticProbeCase:
    """One purpose-built semantic distinction exercised through the real product boundary."""

    case_id: str
    changelog: str
    expected_semantics: str


NEGATED_SUPPORT_CASE = SemanticProbeCase(
    case_id="e1-negated-python-support-drop",
    changelog=(
        "## 2.8.4\n"
        "- Fix selector behavior.\n"
        "## 2.8\n"
        "- Python 3.8 support was not dropped; Python 3.8 remains supported.\n"
        "## 2.7\n"
        "- Add a selector.\n"
    ),
    expected_semantics="Python 3.8 support is explicitly NOT dropped.",
)

FUTURE_SUPPORT_DROP_CASE = SemanticProbeCase(
    case_id="e1-future-python-support-drop",
    changelog=(
        "## 2.8.4\n"
        "- Fix selector behavior.\n"
        "## 2.8\n"
        "- Python 3.8 remains supported in this release; support will be dropped in the next major release.\n"
        "## 2.7\n"
        "- Add a selector.\n"
    ),
    expected_semantics=(
        "Python 3.8 remains supported in the current crossed releases; the drop is only future/planned."
    ),
)

CASES: dict[str, SemanticProbeCase] = {
    NEGATED_SUPPORT_CASE.case_id: NEGATED_SUPPORT_CASE,
    FUTURE_SUPPORT_DROP_CASE.case_id: FUTURE_SUPPORT_DROP_CASE,
}


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


def build_probe_inputs(case: SemanticProbeCase = NEGATED_SUPPORT_CASE) -> ProbeInputs:
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
        content=case.changelog,
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


def run_live_probe(case: SemanticProbeCase) -> ProbeObservation:
    """Run the adopted local semantic extractor, then apply real deterministic grounding."""

    inputs = build_probe_inputs(case)
    candidate_result = LocalSupportDropExtractor().extract(inputs.window)
    grounded_result = validate_support_drop_candidates(
        inputs.authority,
        candidate_result,
    )

    return ProbeObservation(
        case_id=case.case_id,
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


def _output_path(case: SemanticProbeCase) -> Path:
    return Path(f"/tmp/upgradepilot-b2-x1-{case.case_id}.json")


def _render_observation(
    case: SemanticProbeCase,
    observation: ProbeObservation,
) -> dict[str, object]:
    inputs = build_probe_inputs(case)
    return {
        "kind": "b2_x1_e1_support_drop_semantic_probe",
        "case_id": observation.case_id,
        "expected_semantics": case.expected_semantics,
        "source_text": inputs.window.text,
        "candidate_result": asdict(observation.candidate_result),
        "grounded_result_type": type(observation.grounded_result).__name__,
        "grounded_result": asdict(observation.grounded_result),
        "classification": observation.classification,
    }


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run one evidence-first support-drop semantic probe through LM Studio."
    )
    parser.add_argument(
        "--case",
        choices=tuple(CASES),
        default=NEGATED_SUPPORT_CASE.case_id,
        help="Purpose-built semantic case to execute.",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    case = CASES[args.case]
    observation = run_live_probe(case)
    output_path = _output_path(case)
    output = _render_observation(case, observation)
    output_path.write_text(
        json.dumps(output, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    print(f"case: {observation.case_id}")
    print(f"candidate_state: {observation.candidate_result.state}")
    print(f"candidate_count: {len(observation.candidate_result.candidates)}")
    print(f"grounded_result: {type(observation.grounded_result).__name__}")
    print(f"classification: {observation.classification}")
    print(f"output: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
