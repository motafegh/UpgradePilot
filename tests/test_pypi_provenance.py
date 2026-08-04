"""Test PyPI Integrity API acquisition without live network requests."""

from __future__ import annotations

import json
import unittest
from datetime import datetime, timezone
from unittest.mock import Mock

from upgradepilot.pypi.provenance import (
    FileProvenanceEvidence,
    FileProvenanceProblem,
    PyPIProvenanceClient,
)
from upgradepilot.pypi.release import (
    DistributionFile,
    PackageReleaseEvidence,
    ProjectUrlCandidate,
)


def _response(status: int, payload: object | None = None) -> Mock:
    response = Mock()
    response.status_code = status
    response.headers = {}
    body = b"" if payload is None else json.dumps(payload).encode("utf-8")
    response.iter_content.return_value = [body]
    return response


def _release() -> PackageReleaseEvidence:
    distribution = DistributionFile(
        filename="friendly_bard-2.4.0-py3-none-any.whl",
        url="https://files.pythonhosted.org/friendly_bard-2.4.0.whl",
        sha256="a" * 64,
        package_type="bdist_wheel",
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
        distribution_files=(distribution,),
        project_urls=(
            ProjectUrlCandidate(
                label="Source",
                url="https://github.com/example/friendly-bard",
            ),
        ),
    )


def _payload(*, version: int = 1) -> dict[str, object]:
    return {
        "version": version,
        "attestation_bundles": [
            {
                "attestations": [{"envelope": {}}],
                "publisher": {
                    "kind": "GitHub",
                    "repository": "example/friendly-bard",
                    "workflow": "release.yml",
                },
            }
        ],
    }


class PyPIProvenanceClientTests(unittest.TestCase):
    def test_available_provenance_preserves_publisher_identity(self) -> None:
        release = _release()
        session = Mock()
        session.get.return_value = _response(200, _payload())
        fixed_now = datetime(2026, 7, 27, 20, 0, tzinfo=timezone.utc)

        result = PyPIProvenanceClient(
            session=session,
            now=lambda: fixed_now,
        ).get_file_provenance(release, release.distribution_files[0])

        self.assertIsInstance(result, FileProvenanceEvidence)
        assert isinstance(result, FileProvenanceEvidence)
        self.assertEqual(result.filename, release.distribution_files[0].filename)
        self.assertEqual(result.sha256, "a" * 64)
        self.assertEqual(result.attestation_count, 1)
        self.assertEqual(result.publishers[0].kind, "GitHub")
        self.assertEqual(result.publishers[0].repository, "example/friendly-bard")
        self.assertEqual(result.retrieved_at, fixed_now)
        self.assertEqual(
            session.get.call_args.kwargs["headers"]["Accept"],
            "application/vnd.pypi.integrity.v1+json",
        )

    def test_non_github_publisher_is_valid_but_not_forced_into_github_shape(self) -> None:
        release = _release()
        payload = _payload()
        payload["attestation_bundles"][0]["publisher"] = {"kind": "Google"}
        session = Mock()
        session.get.return_value = _response(200, payload)

        result = PyPIProvenanceClient(session=session).get_file_provenance(
            release,
            release.distribution_files[0],
        )

        self.assertIsInstance(result, FileProvenanceEvidence)
        assert isinstance(result, FileProvenanceEvidence)
        self.assertEqual(result.publishers[0].kind, "Google")
        self.assertIsNone(result.publishers[0].repository)
        self.assertIsNone(result.publishers[0].workflow)

    def test_github_publisher_without_repository_is_malformed(self) -> None:
        release = _release()
        payload = _payload()
        del payload["attestation_bundles"][0]["publisher"]["repository"]
        session = Mock()
        session.get.return_value = _response(200, payload)

        result = PyPIProvenanceClient(session=session).get_file_provenance(
            release,
            release.distribution_files[0],
        )

        self.assertIsInstance(result, FileProvenanceProblem)
        assert isinstance(result, FileProvenanceProblem)
        self.assertEqual(result.state, "malformed_response")

    def test_404_is_explicit_provenance_unavailable(self) -> None:
        release = _release()
        session = Mock()
        session.get.return_value = _response(404)

        result = PyPIProvenanceClient(session=session).get_file_provenance(
            release,
            release.distribution_files[0],
        )

        self.assertIsInstance(result, FileProvenanceProblem)
        assert isinstance(result, FileProvenanceProblem)
        self.assertEqual(result.state, "provenance_unavailable")

    def test_unknown_integrity_version_is_unsupported(self) -> None:
        release = _release()
        session = Mock()
        session.get.return_value = _response(200, _payload(version=2))

        result = PyPIProvenanceClient(session=session).get_file_provenance(
            release,
            release.distribution_files[0],
        )

        self.assertIsInstance(result, FileProvenanceProblem)
        assert isinstance(result, FileProvenanceProblem)
        self.assertEqual(result.state, "unsupported_provenance")

    def test_empty_attestation_bundle_is_malformed(self) -> None:
        release = _release()
        payload = _payload()
        payload["attestation_bundles"][0]["attestations"] = []
        session = Mock()
        session.get.return_value = _response(200, payload)

        result = PyPIProvenanceClient(session=session).get_file_provenance(
            release,
            release.distribution_files[0],
        )

        self.assertIsInstance(result, FileProvenanceProblem)
        assert isinstance(result, FileProvenanceProblem)
        self.assertEqual(result.state, "malformed_response")


if __name__ == "__main__":
    unittest.main()
