from __future__ import annotations

import unittest
from datetime import datetime, timezone

from packaging.tags import Tag

from upgradepilot.dependency.change import DependencyVersionChange
from upgradepilot.github.pull_request import PullRequestIdentity
from upgradepilot.impact.artifact_serviceability import (
    ArtifactServiceabilityEvidenceProblem,
    build_artifact_serviceability_impact_candidate,
)
from upgradepilot.pypi.release import DistributionFile, PackageReleaseEvidence

_NOW = datetime(2026, 8, 12, tzinfo=timezone.utc)
_SHA256 = "a" * 64


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
        self.assertEqual(result.target_revision, "b" * 40)
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
        head_sha="b" * 40,
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
