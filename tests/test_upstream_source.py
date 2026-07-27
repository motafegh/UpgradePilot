"""Test the accepted PyPI-to-GitHub upstream authority chain."""

from __future__ import annotations

import unittest
from datetime import datetime, timezone
from unittest.mock import Mock

from upgradepilot.github_release import (
    GitHubReleaseEvidence,
    GitHubReleaseProblem,
)
from upgradepilot.pypi_client import (
    DistributionFile,
    PackageReleaseEvidence,
    ProjectUrlCandidate,
)
from upgradepilot.pypi_provenance import (
    FileProvenanceEvidence,
    FileProvenanceProblem,
    PublisherIdentity,
)
from upgradepilot.upstream_source import (
    UpstreamReleaseEvidence,
    UpstreamSourceProblem,
    UpstreamSourceResolver,
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


def _github_release(tag: str = "2.4.0") -> GitHubReleaseEvidence:
    return GitHubReleaseEvidence(
        repository="example/friendly-bard",
        requested_tag=tag,
        release_id=42,
        release_url=f"https://github.com/example/friendly-bard/releases/tag/{tag}",
        release_name=tag,
        body="Release notes",
        prerelease=False,
        published_at="2026-07-27T20:00:00Z",
        tag_ref=f"refs/tags/{tag}",
        tag_object_type="commit",
        tag_object_sha="abc123",
        retrieved_at=datetime(2026, 7, 27, tzinfo=timezone.utc),
    )


class UpstreamSourceResolverTests(unittest.TestCase):
    def test_matching_authority_chain_returns_unresolved_claim_evidence(self) -> None:
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
        github_client = Mock()
        github_client.get_release.side_effect = [
            _github_release("2.4.0"),
            GitHubReleaseProblem(
                state="source_unavailable",
                repository="example/friendly-bard",
                requested_tag="v2.4.0",
                detail="No release.",
                status_code=404,
            ),
        ]

        result = UpstreamSourceResolver(
            provenance_client=provenance_client,
            github_release_client=github_client,
        ).resolve(release)

        self.assertIsInstance(result, UpstreamReleaseEvidence)
        assert isinstance(result, UpstreamReleaseEvidence)
        self.assertEqual(result.repository, "example/friendly-bard")
        self.assertEqual(result.claim_state, "unresolved_claim")
        self.assertEqual(
            result.provenance_unavailable_files,
            (release.distribution_files[1].filename,),
        )
        self.assertEqual(result.github_release.requested_tag, "2.4.0")

    def test_provenance_repository_mismatch_stops_before_github(self) -> None:
        release = _release()
        provenance_client = Mock()
        provenance_client.get_file_provenance.return_value = _provenance(
            release.distribution_files[0],
            repository="other/project",
        )
        github_client = Mock()

        result = UpstreamSourceResolver(
            provenance_client=provenance_client,
            github_release_client=github_client,
        ).resolve(release)

        self.assertIsInstance(result, UpstreamSourceProblem)
        assert isinstance(result, UpstreamSourceProblem)
        self.assertEqual(result.state, "identity_mismatch")
        github_client.get_release.assert_not_called()

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

        result = UpstreamSourceResolver(
            provenance_client=Mock(),
            github_release_client=Mock(),
        ).resolve(release)

        self.assertIsInstance(result, UpstreamSourceProblem)
        assert isinstance(result, UpstreamSourceProblem)
        self.assertEqual(result.state, "ambiguous_source")

    def test_non_github_source_candidate_is_unsupported(self) -> None:
        release = _release(
            project_urls=(
                ProjectUrlCandidate(
                    label="Source",
                    url="https://gitlab.com/example/friendly-bard",
                ),
            )
        )

        result = UpstreamSourceResolver(
            provenance_client=Mock(),
            github_release_client=Mock(),
        ).resolve(release)

        self.assertIsInstance(result, UpstreamSourceProblem)
        assert isinstance(result, UpstreamSourceProblem)
        self.assertEqual(result.state, "unsupported_source")

    def test_two_accepted_tag_forms_are_ambiguous(self) -> None:
        release = _release()
        provenance_client = Mock()
        provenance_client.get_file_provenance.return_value = _provenance(
            release.distribution_files[0]
        )
        github_client = Mock()
        github_client.get_release.side_effect = [
            _github_release("2.4.0"),
            _github_release("v2.4.0"),
        ]

        result = UpstreamSourceResolver(
            provenance_client=provenance_client,
            github_release_client=github_client,
        ).resolve(release)

        self.assertIsInstance(result, UpstreamSourceProblem)
        assert isinstance(result, UpstreamSourceProblem)
        self.assertEqual(result.state, "ambiguous_source")

    def test_project_url_labels_follow_pep_753_normalization(self) -> None:
        self.assertEqual(normalize_project_url_label("Source Code"), "sourcecode")
        self.assertEqual(normalize_project_url_label("SOURCE-CODE"), "sourcecode")


if __name__ == "__main__":
    unittest.main()
