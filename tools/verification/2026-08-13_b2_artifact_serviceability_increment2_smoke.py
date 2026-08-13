#!/usr/bin/env python3
"""Retained smoke proof for B2 Artifact Serviceability Increment 2.

Why this script is retained
---------------------------
The Increment-2 source change added target wheel-compatibility evidence and artifact
applicability evaluation. During implementation, the GitHub connector could not update
the permanent product regression file, so this bounded developer-operated smoke check
preserves the exact executable cases used to verify the new semantics in Ali's normal
UpgradePilot environment.

What this verifies
------------------
- no exact target wheel-compatibility evidence -> applicability remains unresolved;
- an old-compatible / proposed-incompatible target -> candidate becomes applicable;
- a different proposed wheel that still serves the target -> bounded candidate is not
  applicable even though an old exact tag disappeared;
- a target that never had an old compatible wheel -> bounded candidate is not applicable;
- attempted but insufficient target evidence -> applicability remains unresolved;
- target evidence from a different revision is rejected.

What this does NOT prove
------------------------
- that UpgradePilot can yet acquire/derive target-supported wheel tags from repository or
  CI evidence;
- that source-distribution fallback succeeds;
- that the whole dependency update is safe or merge-ready;
- that permanent product regression coverage exists for these new cases.

This is a developer verification aid under ``tools/verification/``. It exercises product
code only and intentionally does not import fixtures/helpers from ``tests/``.
"""

from __future__ import annotations

from datetime import datetime, timezone

from packaging.tags import Tag

from upgradepilot.dependency.change import DependencyVersionChange
from upgradepilot.github.pull_request import PullRequestIdentity
from upgradepilot.impact.artifact_serviceability import (
    ArtifactServiceabilityEvidenceProblem,
    TargetWheelCompatibilityEvidence,
    TargetWheelCompatibilityProblem,
    build_artifact_serviceability_impact_candidate,
    evaluate_artifact_serviceability_impact,
)
from upgradepilot.pypi.release import DistributionFile, PackageReleaseEvidence


_RETRIEVED_AT = datetime(2026, 8, 13, tzinfo=timezone.utc)
_SHA256 = "a" * 64
_TARGET_REVISION = "b" * 40


def main() -> int:
    """Execute the retained Increment-2 semantic smoke cases."""

    old_tag = Tag("cp36", "cp36m", "manylinux1_x86_64")
    new_tag = Tag("cp37", "abi3", "manylinux_2_17_x86_64")

    result = build_artifact_serviceability_impact_candidate(
        _pull_request(),
        _dependency(),
        _release(
            "1.0",
            (
                _distribution(
                    "demo-1.0-cp36-cp36m-manylinux1_x86_64.whl",
                    "bdist_wheel",
                ),
            ),
        ),
        _release(
            "2.0",
            (
                _distribution(
                    "demo-2.0-cp37-abi3-manylinux_2_17_x86_64.whl",
                    "bdist_wheel",
                ),
                _distribution("demo-2.0.tar.gz", "sdist"),
            ),
        ),
    )

    assert result is not None
    assert not isinstance(result, ArtifactServiceabilityEvidenceProblem)
    candidate = result

    # Before target-owned environment evidence exists, the package-side change is real
    # but target exposure is not yet established.
    assessment = evaluate_artifact_serviceability_impact(candidate)
    assert assessment.applicability.state == "unresolved"

    # The target could use an old wheel but no proposed wheel: the bounded prebuilt-wheel
    # serviceability-loss path is established.
    old_only = TargetWheelCompatibilityEvidence(
        repository="example/project",
        revision=_TARGET_REVISION,
        source="controlled retained verification fixture",
        supported_tags=frozenset({old_tag}),
    )
    assessment = evaluate_artifact_serviceability_impact(candidate, old_only)
    assert assessment.applicability.state == "established_applicable"

    # A removed exact old tag is not enough. If a different proposed tag still serves the
    # same target environment, the target has not lost its prebuilt-wheel path.
    old_and_new = TargetWheelCompatibilityEvidence(
        repository="example/project",
        revision=_TARGET_REVISION,
        source="controlled retained verification fixture",
        supported_tags=frozenset({old_tag, new_tag}),
    )
    assessment = evaluate_artifact_serviceability_impact(candidate, old_and_new)
    assert assessment.applicability.state == "established_not_applicable"

    # If the target could not use the old published wheel in the first place, this bounded
    # artifact-loss candidate does not apply to that target.
    new_only = TargetWheelCompatibilityEvidence(
        repository="example/project",
        revision=_TARGET_REVISION,
        source="controlled retained verification fixture",
        supported_tags=frozenset({new_tag}),
    )
    assessment = evaluate_artifact_serviceability_impact(candidate, new_only)
    assert assessment.applicability.state == "established_not_applicable"

    problem = TargetWheelCompatibilityProblem(
        state="evidence_insufficient",
        repository="example/project",
        revision=_TARGET_REVISION,
        source="controlled retained verification fixture",
        detail="Exact supported wheel tags were not established.",
    )
    assessment = evaluate_artifact_serviceability_impact(candidate, problem)
    assert assessment.applicability.state == "unresolved"

    wrong_revision = TargetWheelCompatibilityEvidence(
        repository="example/project",
        revision="c" * 40,
        source="controlled retained verification fixture",
        supported_tags=frozenset({old_tag}),
    )
    try:
        evaluate_artifact_serviceability_impact(candidate, wrong_revision)
    except ValueError:
        pass
    else:
        raise AssertionError("Mismatched target revision should have been rejected.")

    print("B2 Artifact Serviceability Increment 2 retained smoke: PASS")
    return 0


def _pull_request() -> PullRequestIdentity:
    return PullRequestIdentity(
        repository="example/project",
        number=7,
        title="Bump demo",
        state="open",
        merged=False,
        author="dependabot[bot]",
        base_ref="main",
        base_sha="a" * 40,
        head_ref="dependabot/demo",
        head_sha=_TARGET_REVISION,
        changed_files=1,
    )


def _dependency() -> DependencyVersionChange:
    return DependencyVersionChange(
        package="demo",
        normalized_package="demo",
        old_version="1.0",
        proposed_version="2.0",
        source_evidence=(),
    )


def _release(
    version: str,
    files: tuple[DistributionFile, ...],
) -> PackageReleaseEvidence:
    return PackageReleaseEvidence(
        requested_package="demo",
        normalized_package="demo",
        requested_version=version,
        published_name="demo",
        published_version=version,
        source_url=f"https://pypi.org/pypi/demo/{version}/json",
        retrieved_at=_RETRIEVED_AT,
        last_serial=1,
        distribution_files=files,
        project_urls=(),
    )


def _distribution(filename: str, package_type: str) -> DistributionFile:
    return DistributionFile(
        filename=filename,
        url=f"https://files.pythonhosted.org/{filename}",
        sha256=_SHA256,
        package_type=package_type,
    )


if __name__ == "__main__":
    raise SystemExit(main())
