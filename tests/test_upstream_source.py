"""Test trusted upstream repository identity from PyPI metadata and provenance."""

from __future__ import annotations

import unittest
from datetime import datetime, timezone
from unittest.mock import Mock

from upgradepilot.pypi.provenance import (
    FileProvenanceEvidence,
    FileProvenanceProblem,
    PublisherIdentity,
)
from upgradepilot.pypi.release import (
    DistributionFile,
    PackageReleaseEvidence,
    ProjectUrlCandidate,
)
from upgradepilot.upstream.repository import (
    UpstreamRepositoryEvidence,
    UpstreamRepositoryProblem,
    UpstreamRepositoryResolver,
    normalize_project_url_label,
)


def _release(
    *,
    project_urls: tuple[ProjectUrlCandidate, ...] | None = None,
    file_count: int = 1,
) -> PackageReleaseEvidence:
    files = tuple(
        DistributionFile(
            filename=f"friendly_bard-2.4.0-{index}.whl",
            url=f"https://files.pythonhosted.org/file-{index}.whl",
            sha256="a" * 64,
            package_type="bdist_wheel",
        )
        for index in range(file_count)
    )
    return PackageReleaseEvidence(
        requested_package="friendly-bard",
        normalized_package="friendly-bard",
        requested_version="2.4.0",
        published_name="friendly-bard",
        published_version="2.4.0",
        source_url="https://pypi.org/pypi/friendly-bard/2.4.0/json",
        retrieved_at=datetime(2026, 7, 27, tzinfo=timezone.utc),
        last_serial=123,
        distribution_files=files,
        project_urls=project_urls
        or (
            ProjectUrlCandidate(
                label="Source",
                url="https://github.com/example/friendly-bard",
            ),
        ),
    )


def _provenance(
    distribution: DistributionFile,
    *,
    repository: str = "example/friendly-bard",
    kind: str = "GitHub",
) -> FileProvenanceEvidence:
    return FileProvenanceEvidence(
        package="friendly-bard",
        version="2.4.0",
        filename=distribution.filename,
        sha256=distribution.sha256,
        source_url="https://pypi.org/integrity/example",
        retrieved_at=datetime(2026, 7, 27, tzinfo=timezone.utc),
        api_version=1,
        attestation_count=1,
        publishers=(
            PublisherIdentity(
                kind=kind,
                repository=repository,
                workflow="release.yml",
            ),
        ),
    )


class UpstreamRepositoryResolverTests(unittest.TestCase):
    def test_matching_pypi_identity_returns_repository_without_semantic_claim_state(self) -> None:
        release = _release(file_count=2)
        provenance_client = Mock()
        provenance_client.get_file_provenance.side_effect = [
            _provenance(release.distribution_files[0]),
            FileProvenanceProblem(
                state="provenance_unavailable",
                package="friendly-bard",
                version="2.4.0",
                filename=release.distribution_files[1].filename,
                source_url="https://pypi.org/integrity/missing",
                detail="No provenance.",
                status_code=404,
            ),
        ]

        result = UpstreamRepositoryResolver(
            provenance_client=provenance_client,
        ).resolve(release)

        self.assertIsInstance(result, UpstreamRepositoryEvidence)
        assert isinstance(result, UpstreamRepositoryEvidence)
        self.assertEqual(result.repository, "example/friendly-bard")
        self.assertFalse(hasattr(result, "claim_state"))
        self.assertFalse(hasattr(result, "github_release"))
        self.assertEqual(
            result.provenance_unavailable_files,
            (release.distribution_files[1].filename,),
        )

    def test_homepage_github_candidate_requires_and_accepts_matching_provenance(self) -> None:
        release = _release(
            project_urls=(
                ProjectUrlCandidate(
                    label="Homepage",
                    url="https://github.com/example/friendly-bard",
                ),
            )
        )
        provenance_client = Mock()
        provenance_client.get_file_provenance.return_value = _provenance(
            release.distribution_files[0]
        )

        result = UpstreamRepositoryResolver(
            provenance_client=provenance_client,
        ).resolve(release)

        self.assertIsInstance(result, UpstreamRepositoryEvidence)
        assert isinstance(result, UpstreamRepositoryEvidence)
        self.assertEqual(result.repository, "example/friendly-bard")
        self.assertEqual(result.source_candidates, release.project_urls)
        provenance_client.get_file_provenance.assert_called_once_with(
            release,
            release.distribution_files[0],
        )

    def test_homepage_candidate_without_usable_provenance_is_not_trusted(self) -> None:
        release = _release(
            project_urls=(
                ProjectUrlCandidate(
                    label="Homepage",
                    url="https://github.com/example/friendly-bard",
                ),
            )
        )
        provenance_client = Mock()
        provenance_client.get_file_provenance.return_value = FileProvenanceProblem(
            state="provenance_unavailable",
            package="friendly-bard",
            version="2.4.0",
            filename=release.distribution_files[0].filename,
            source_url="https://pypi.org/integrity/missing",
            detail="No provenance.",
            status_code=404,
        )

        result = UpstreamRepositoryResolver(
            provenance_client=provenance_client,
        ).resolve(release)

        self.assertIsInstance(result, UpstreamRepositoryProblem)
        assert isinstance(result, UpstreamRepositoryProblem)
        self.assertEqual(result.state, "source_unavailable")

    def test_provenance_repository_mismatch_is_identity_mismatch(self) -> None:
        release = _release()
        provenance_client = Mock()
        provenance_client.get_file_provenance.return_value = _provenance(
            release.distribution_files[0],
            repository="other/project",
        )

        result = UpstreamRepositoryResolver(
            provenance_client=provenance_client,
        ).resolve(release)

        self.assertIsInstance(result, UpstreamRepositoryProblem)
        assert isinstance(result, UpstreamRepositoryProblem)
        self.assertEqual(result.state, "identity_mismatch")

    def test_distinct_source_candidates_are_ambiguous(self) -> None:
        release = _release(
            project_urls=(
                ProjectUrlCandidate(
                    label="Source",
                    url="https://github.com/example/friendly-bard",
                ),
                ProjectUrlCandidate(
                    label="Repository",
                    url="https://github.com/example/another-project",
                ),
            )
        )
        result = UpstreamRepositoryResolver(provenance_client=Mock()).resolve(release)
        self.assertIsInstance(result, UpstreamRepositoryProblem)
        assert isinstance(result, UpstreamRepositoryProblem)
        self.assertEqual(result.state, "ambiguous_source")

    def test_source_and_homepage_conflict_is_ambiguous_before_provenance(self) -> None:
        release = _release(
            project_urls=(
                ProjectUrlCandidate(
                    label="Source",
                    url="https://github.com/example/friendly-bard",
                ),
                ProjectUrlCandidate(
                    label="Homepage",
                    url="https://github.com/example/another-project",
                ),
            )
        )
        provenance_client = Mock()

        result = UpstreamRepositoryResolver(
            provenance_client=provenance_client,
        ).resolve(release)

        self.assertIsInstance(result, UpstreamRepositoryProblem)
        assert isinstance(result, UpstreamRepositoryProblem)
        self.assertEqual(result.state, "ambiguous_source")
        provenance_client.get_file_provenance.assert_not_called()

    def test_non_github_source_candidate_is_unsupported(self) -> None:
        release = _release(
            project_urls=(
                ProjectUrlCandidate(
                    label="Source",
                    url="https://gitlab.com/example/friendly-bard",
                ),
            )
        )
        result = UpstreamRepositoryResolver(provenance_client=Mock()).resolve(release)
        self.assertIsInstance(result, UpstreamRepositoryProblem)
        assert isinstance(result, UpstreamRepositoryProblem)
        self.assertEqual(result.state, "unsupported_source")

    def test_project_url_labels_follow_pep_753_normalization(self) -> None:
        self.assertEqual(normalize_project_url_label("Source Code"), "sourcecode")
        self.assertEqual(normalize_project_url_label("SOURCE-CODE"), "sourcecode")
        self.assertEqual(normalize_project_url_label("Home Page"), "homepage")


if __name__ == "__main__":
    unittest.main()
