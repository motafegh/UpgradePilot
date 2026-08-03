"""Test exact PyPI project release-key acquisition without live network access."""

from __future__ import annotations

import json
import unittest
from datetime import datetime, timezone
from unittest.mock import Mock

from requests.exceptions import Timeout

from upgradepilot.pypi_client import (
    PackageReleaseIndexEvidence,
    PackageReleaseIndexProblem,
    PyPIReleaseIndexClient,
)


def _response(status: int, payload: object | None = None) -> Mock:
    """Build the streamed Requests response surface used by the PyPI base client."""

    response = Mock()
    response.status_code = status
    response.headers = {}
    body = b"" if payload is None else json.dumps(payload).encode("utf-8")
    response.iter_content.return_value = [body]
    return response


def _project_payload(
    *,
    name: str = "friendly-bard",
    releases: object | None = None,
) -> dict[str, object]:
    if releases is None:
        releases = {
            "2.8.4": [],
            "2.6": [],
            "2.8": [],
            "2.7": [],
        }
    return {
        "info": {"name": name},
        "last_serial": 54321,
        "releases": releases,
    }


class PyPIReleaseIndexClientTests(unittest.TestCase):
    """Protect package identity, raw release keys, and explicit source failures."""

    def test_available_index_preserves_raw_keys_without_semantic_sorting(self) -> None:
        session = Mock()
        session.get.return_value = _response(200, _project_payload())
        fixed_now = datetime(2026, 8, 2, 12, 0, tzinfo=timezone.utc)

        result = PyPIReleaseIndexClient(
            session=session,
            now=lambda: fixed_now,
        ).get_release_index("Friendly_Bard")

        self.assertIsInstance(result, PackageReleaseIndexEvidence)
        assert isinstance(result, PackageReleaseIndexEvidence)
        self.assertEqual(result.requested_package, "Friendly_Bard")
        self.assertEqual(result.normalized_package, "friendly-bard")
        self.assertEqual(result.published_name, "friendly-bard")
        self.assertEqual(result.last_serial, 54321)
        self.assertEqual(result.retrieved_at, fixed_now)
        self.assertEqual(result.release_versions, ("2.6", "2.7", "2.8", "2.8.4"))
        self.assertEqual(
            result.source_url,
            "https://pypi.org/pypi/friendly-bard/json",
        )

        call = session.get.call_args
        self.assertEqual(call.args[0], "https://pypi.org/pypi/friendly-bard/json")
        self.assertEqual(call.kwargs["headers"]["Accept"], "application/json")
        self.assertTrue(call.kwargs["stream"])

    def test_releases_field_must_be_an_object(self) -> None:
        session = Mock()
        session.get.return_value = _response(
            200,
            _project_payload(releases=["2.7", "2.8"]),
        )

        result = PyPIReleaseIndexClient(session=session).get_release_index("friendly-bard")

        self.assertIsInstance(result, PackageReleaseIndexProblem)
        assert isinstance(result, PackageReleaseIndexProblem)
        self.assertEqual(result.state, "malformed_response")

    def test_each_release_entry_must_be_an_array(self) -> None:
        session = Mock()
        session.get.return_value = _response(
            200,
            _project_payload(releases={"2.7": {"not": "a-list"}}),
        )

        result = PyPIReleaseIndexClient(session=session).get_release_index("friendly-bard")

        self.assertIsInstance(result, PackageReleaseIndexProblem)
        assert isinstance(result, PackageReleaseIndexProblem)
        self.assertEqual(result.state, "malformed_response")
        self.assertIn("2.7", result.detail)

    def test_conflicting_published_package_name_is_identity_mismatch(self) -> None:
        session = Mock()
        session.get.return_value = _response(
            200,
            _project_payload(name="different-package"),
        )

        result = PyPIReleaseIndexClient(session=session).get_release_index("friendly-bard")

        self.assertIsInstance(result, PackageReleaseIndexProblem)
        assert isinstance(result, PackageReleaseIndexProblem)
        self.assertEqual(result.state, "identity_mismatch")

    def test_package_404_remains_explicit(self) -> None:
        session = Mock()
        session.get.return_value = _response(404)

        result = PyPIReleaseIndexClient(session=session).get_release_index("missing-package")

        self.assertIsInstance(result, PackageReleaseIndexProblem)
        assert isinstance(result, PackageReleaseIndexProblem)
        self.assertEqual(result.state, "package_not_found_or_inaccessible")
        self.assertEqual(result.status_code, 404)

    def test_timeout_is_acquisition_failed(self) -> None:
        session = Mock()
        session.get.side_effect = Timeout("slow")

        result = PyPIReleaseIndexClient(session=session).get_release_index("friendly-bard")

        self.assertIsInstance(result, PackageReleaseIndexProblem)
        assert isinstance(result, PackageReleaseIndexProblem)
        self.assertEqual(result.state, "acquisition_failed")

    def test_oversized_success_is_malformed(self) -> None:
        response = _response(200, _project_payload())
        response.iter_content.return_value = [b"x" * 500]
        session = Mock()
        session.get.return_value = response

        result = PyPIReleaseIndexClient(
            session=session,
            max_response_bytes=100,
        ).get_release_index("friendly-bard")

        self.assertIsInstance(result, PackageReleaseIndexProblem)
        assert isinstance(result, PackageReleaseIndexProblem)
        self.assertEqual(result.state, "malformed_response")
        self.assertIn("size limit", result.detail)

    def test_invalid_success_json_is_malformed(self) -> None:
        response = _response(200)
        response.iter_content.return_value = [b"{not-json"]
        session = Mock()
        session.get.return_value = response

        result = PyPIReleaseIndexClient(session=session).get_release_index("friendly-bard")

        self.assertIsInstance(result, PackageReleaseIndexProblem)
        assert isinstance(result, PackageReleaseIndexProblem)
        self.assertEqual(result.state, "malformed_response")


if __name__ == "__main__":
    unittest.main()
