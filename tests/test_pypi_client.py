"""Test exact PyPI release identity without making live network requests."""

from __future__ import annotations

import json
import unittest
from datetime import datetime, timezone
from unittest.mock import Mock

from requests.exceptions import Timeout

from upgradepilot.pypi_client import (
    PackageReleaseEvidence,
    PackageReleaseProblem,
    PyPIReleaseClient,
)


def _response(status: int, payload: object | None = None) -> Mock:
    """Build the small Requests response surface used by the client."""

    response = Mock()
    response.status_code = status
    response.headers = {}
    response.content = b"" if payload is None else json.dumps(payload).encode("utf-8")
    return response


def _release_payload(
    *,
    name: str = "friendly-bard",
    version: str = "2.4.0",
) -> dict[str, object]:
    """Return a minimal release-specific PyPI response."""

    return {
        "info": {
            "name": name,
            "version": version,
            "yanked": False,
            "yanked_reason": None,
            "project_urls": {
                "Source": "https://github.com/example/friendly-bard",
                "Changelog": "https://example.org/friendly-bard/changelog",
            },
        },
        "last_serial": 12345,
        "urls": [{"filename": "friendly_bard-2.4.0-py3-none-any.whl"}],
    }


class PyPIReleaseClientTests(unittest.TestCase):
    """Protect package normalization, exact identity, and explicit failure states."""

    def test_available_release_accepts_normalized_name_variation(self) -> None:
        response = _response(200, _release_payload())
        session = Mock()
        session.get.return_value = response
        fixed_now = datetime(2026, 7, 27, 18, 0, tzinfo=timezone.utc)

        result = PyPIReleaseClient(
            session=session,
            now=lambda: fixed_now,
        ).get_release("Friendly_Bard", "2.4.0")

        self.assertIsInstance(result, PackageReleaseEvidence)
        assert isinstance(result, PackageReleaseEvidence)
        self.assertEqual(result.normalized_package, "friendly-bard")
        self.assertEqual(result.published_version, "2.4.0")
        self.assertEqual(result.distribution_file_count, 1)
        self.assertEqual(result.retrieved_at, fixed_now)
        self.assertEqual(
            [candidate.label for candidate in result.project_urls],
            ["Changelog", "Source"],
        )

        call = session.get.call_args
        self.assertEqual(
            call.args[0],
            "https://pypi.org/pypi/friendly-bard/2.4.0/json",
        )
        kwargs = call.kwargs
        self.assertEqual(kwargs["headers"]["Accept"], "application/json")

    def test_success_with_different_version_is_identity_mismatch(self) -> None:
        session = Mock()
        session.get.return_value = _response(
            200,
            _release_payload(version="2.4.1"),
        )

        result = PyPIReleaseClient(session=session).get_release(
            "friendly-bard",
            "2.4.0",
        )

        self.assertIsInstance(result, PackageReleaseProblem)
        assert isinstance(result, PackageReleaseProblem)
        self.assertEqual(result.state, "identity_mismatch")

    def test_release_404_with_existing_package_is_version_not_found(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(404),
            _response(200, {"info": {"name": "friendly-bard"}}),
        ]

        result = PyPIReleaseClient(session=session).get_release(
            "friendly-bard",
            "9.9.9",
        )

        self.assertIsInstance(result, PackageReleaseProblem)
        assert isinstance(result, PackageReleaseProblem)
        self.assertEqual(result.state, "version_not_found")
        self.assertEqual(session.get.call_count, 2)

    def test_release_and_project_404_preserve_package_ambiguity(self) -> None:
        session = Mock()
        session.get.side_effect = [_response(404), _response(404)]

        result = PyPIReleaseClient(session=session).get_release(
            "missing-package",
            "1.0.0",
        )

        self.assertIsInstance(result, PackageReleaseProblem)
        assert isinstance(result, PackageReleaseProblem)
        self.assertEqual(result.state, "package_not_found_or_inaccessible")

    def test_malformed_success_is_not_trusted(self) -> None:
        session = Mock()
        session.get.return_value = _response(200, ["not", "an", "object"])

        result = PyPIReleaseClient(session=session).get_release(
            "friendly-bard",
            "2.4.0",
        )

        self.assertIsInstance(result, PackageReleaseProblem)
        assert isinstance(result, PackageReleaseProblem)
        self.assertEqual(result.state, "malformed_response")

    def test_body_larger_than_limit_is_malformed(self) -> None:
        response = _response(200, _release_payload())
        response.content = b"x" * 500
        session = Mock()
        session.get.return_value = response

        result = PyPIReleaseClient(
            session=session,
            max_response_bytes=100,
        ).get_release("friendly-bard", "2.4.0")

        self.assertIsInstance(result, PackageReleaseProblem)
        assert isinstance(result, PackageReleaseProblem)
        self.assertEqual(result.state, "malformed_response")
        self.assertIn("size limit", result.detail)

    def test_timeout_remains_distinct_from_missing_evidence(self) -> None:
        session = Mock()
        session.get.side_effect = Timeout("slow")

        result = PyPIReleaseClient(session=session).get_release(
            "friendly-bard",
            "2.4.0",
        )

        self.assertIsInstance(result, PackageReleaseProblem)
        assert isinstance(result, PackageReleaseProblem)
        self.assertEqual(result.state, "acquisition_failed")


if __name__ == "__main__":
    unittest.main()
