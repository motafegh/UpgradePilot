from __future__ import annotations

import unittest
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

_NOW = datetime(2026, 8, 12, tzinfo=timezone.utc)
_SHA256 = "a" * 64
_TARGET_REVISION = "b" * 40


class ArtifactServiceabilityImpactTests(unittest.TestCase):
    def test_removed_published_wheel_tags_form_target_agnostic_candidate(self) -> None:
        dependency = _dependency()
        old_release = _release(
            "1.0",
            (
                _file(
                    "demo-1.0-cp36-cp36m-manylinux1_x86_64.whl",
                    "bdist_wheel",
                ),
            ),
        )
        proposed_release = _release(
            "2.0",
            (
                _file(
                    "demo-2.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl",
                    "bdist_wheel",
                ),
                _file("demo-2.0.tar.gz", "sdist"),
            ),
        )

        result = build_artifact_serviceability_impact_candidate(
            _pull_request(),
            dependency,
            old_release,
            proposed_release,
        )

        self.assertNotIsInstance(result, ArtifactServiceabilityEvidenceProblem)
        self.assertIsNotNone(result)
        assert result is not None
        assert not isinstance(result, ArtifactServiceabilityEvidenceProblem)
        self.assertEqual(result.target_repository, "example/project")
        self.assertEqual(result.target_revision, _TARGET_REVISION)
        self.assertEqual(result.mechanism_status, "established")
        self.assertEqual(result.exposure_status, "to_evaluate")
        self.assertEqual(result.consequence_status, "possible")
        self.assertEqual(
            result.removed_wheel_tags,
            frozenset({Tag("cp36", "cp36m", "manylinux1_x86_64")}),
        )
        self.assertTrue(result.proposed_source_distribution_available)
        self.assertFalse(result.old_source_distribution_available)
        self.assertIn("target environment", result.possible_consequence)
        self.assertIn("source-distribution fallback", result.possible_consequence)

    def test_unchanged_published_wheel_tag_set_does_not_manufacture_candidate(self) -> None:
        old_release = _release(
            "1.0",
            (_file("demo-1.0-cp39-abi3-manylinux_2_17_x86_64.whl", "bdist_wheel"),),
        )
        proposed_release = _release(
            "2.0",
            (_file("demo-2.0-cp39-abi3-manylinux_2_17_x86_64.whl", "bdist_wheel"),),
        )

        result = build_artifact_serviceability_impact_candidate(
            _pull_request(),
            _dependency(),
            old_release,
            proposed_release,
        )

        self.assertIsNone(result)

    def test_invalid_published_wheel_filename_is_preserved_as_evidence_problem(self) -> None:
        old_release = _release(
            "1.0",
            (_file("not-a-valid-wheel.whl", "bdist_wheel"),),
        )
        proposed_release = _release(
            "2.0",
            (_file("demo-2.0-py3-none-any.whl", "bdist_wheel"),),
        )

        result = build_artifact_serviceability_impact_candidate(
            _pull_request(),
            _dependency(),
            old_release,
            proposed_release,
        )

        self.assertIsInstance(result, ArtifactServiceabilityEvidenceProblem)
        assert isinstance(result, ArtifactServiceabilityEvidenceProblem)
        self.assertEqual(result.state, "wheel_filename_uninterpretable")
        self.assertEqual(result.release_version, "1.0")
        self.assertEqual(result.filename, "not-a-valid-wheel.whl")

    def test_release_identity_must_match_exact_dependency_transition(self) -> None:
        old_release = _release("0.9", ())
        proposed_release = _release("2.0", ())

        with self.assertRaises(ValueError):
            build_artifact_serviceability_impact_candidate(
                _pull_request(),
                _dependency(),
                old_release,
                proposed_release,
            )

    def test_missing_target_compatibility_evidence_remains_unresolved(self) -> None:
        candidate = _artifact_candidate()

        assessment = evaluate_artifact_serviceability_impact(candidate)

        self.assertEqual(assessment.applicability.state, "unresolved")
        self.assertIsNone(assessment.target_evidence)

    def test_old_compatible_and_proposed_incompatible_establishes_applicability(self) -> None:
        candidate = _artifact_candidate()
        target = TargetWheelCompatibilityEvidence(
            repository="example/project",
            revision=_TARGET_REVISION,
            source="controlled target observation",
            supported_tags=frozenset(
                {Tag("cp36", "cp36m", "manylinux1_x86_64")}
            ),
        )

        assessment = evaluate_artifact_serviceability_impact(candidate, target)

        self.assertEqual(assessment.applicability.state, "established_applicable")

    def test_different_proposed_compatible_tag_refutes_serviceability_loss(self) -> None:
        candidate = _artifact_candidate()
        target = TargetWheelCompatibilityEvidence(
            repository="example/project",
            revision=_TARGET_REVISION,
            source="controlled target observation",
            supported_tags=frozenset(
                {
                    Tag("cp36", "cp36m", "manylinux1_x86_64"),
                    Tag("cp37", "abi3", "manylinux_2_17_x86_64"),
                }
            ),
        )

        assessment = evaluate_artifact_serviceability_impact(candidate, target)

        # Losing one exact old tag is not enough when another proposed wheel still
        # serves this same observed target environment.
        self.assertEqual(assessment.applicability.state, "established_not_applicable")

    def test_target_without_old_compatible_wheel_refutes_serviceability_loss(self) -> None:
        candidate = _artifact_candidate()
        target = TargetWheelCompatibilityEvidence(
            repository="example/project",
            revision=_TARGET_REVISION,
            source="controlled target observation",
            supported_tags=frozenset(
                {Tag("cp37", "abi3", "manylinux_2_17_x86_64")}
            ),
        )

        assessment = evaluate_artifact_serviceability_impact(candidate, target)

        self.assertEqual(assessment.applicability.state, "established_not_applicable")

    def test_insufficient_target_compatibility_evidence_remains_unresolved(self) -> None:
        candidate = _artifact_candidate()
        problem = TargetWheelCompatibilityProblem(
            state="evidence_insufficient",
            repository="example/project",
            revision=_TARGET_REVISION,
            source="controlled target observation",
            detail="Exact supported wheel tags were not established.",
        )

        assessment = evaluate_artifact_serviceability_impact(candidate, problem)

        self.assertEqual(assessment.applicability.state, "unresolved")
        self.assertIs(assessment.target_evidence, problem)

    def test_target_repository_identity_must_match_candidate(self) -> None:
        candidate = _artifact_candidate()
        target = TargetWheelCompatibilityEvidence(
            repository="different/project",
            revision=_TARGET_REVISION,
            source="controlled target observation",
            supported_tags=frozenset(
                {Tag("cp36", "cp36m", "manylinux1_x86_64")}
            ),
        )

        with self.assertRaises(ValueError):
            evaluate_artifact_serviceability_impact(candidate, target)

    def test_target_revision_identity_must_match_candidate(self) -> None:
        candidate = _artifact_candidate()
        target = TargetWheelCompatibilityEvidence(
            repository="example/project",
            revision="c" * 40,
            source="controlled target observation",
            supported_tags=frozenset(
                {Tag("cp36", "cp36m", "manylinux1_x86_64")}
            ),
        )

        with self.assertRaises(ValueError):
            evaluate_artifact_serviceability_impact(candidate, target)


def _artifact_candidate():
    result = build_artifact_serviceability_impact_candidate(
        _pull_request(),
        _dependency(),
        _release(
            "1.0",
            (
                _file(
                    "demo-1.0-cp36-cp36m-manylinux1_x86_64.whl",
                    "bdist_wheel",
                ),
            ),
        ),
        _release(
            "2.0",
            (
                _file(
                    "demo-2.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl",
                    "bdist_wheel",
                ),
                _file("demo-2.0.tar.gz", "sdist"),
            ),
        ),
    )
    assert result is not None
    assert not isinstance(result, ArtifactServiceabilityEvidenceProblem)
    return result


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
        retrieved_at=_NOW,
        last_serial=1,
        distribution_files=files,
        project_urls=(),
    )


def _file(filename: str, package_type: str) -> DistributionFile:
    return DistributionFile(
        filename=filename,
        url=f"https://files.pythonhosted.org/{filename}",
        sha256=_SHA256,
        package_type=package_type,
    )


if __name__ == "__main__":
    unittest.main()
