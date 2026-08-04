"""Protect source-specific behavior around shared JSON value contracts."""

from __future__ import annotations

import json
import unittest
from unittest.mock import Mock

from upgradepilot.github.api import (
    GitHubResponseError,
    required_nonnegative_int,
)
from upgradepilot.pypi.release import PackageReleaseProblem, PyPIReleaseClient


def _response(payload: object) -> Mock:
    response = Mock()
    response.status_code = 200
    response.headers = {}
    response.iter_content.return_value = [json.dumps(payload).encode("utf-8")]
    return response


class ExternalContractAdapterTests(unittest.TestCase):
    def test_github_preserves_type_error_before_range_error(self) -> None:
        with self.assertRaisesRegex(
            GitHubResponseError,
            "GitHub field 'count' must be an integer",
        ):
            required_nonnegative_int({"count": True}, "count")

        with self.assertRaisesRegex(
            GitHubResponseError,
            "GitHub field 'count' must not be negative",
        ):
            required_nonnegative_int({"count": -1}, "count")

    def test_pypi_translates_shared_violation_to_malformed_response(self) -> None:
        payload = {
            "info": {
                "name": "friendly-bard",
                "version": "2.4.0",
                "project_urls": None,
            },
            "last_serial": True,
            "urls": [],
        }
        session = Mock()
        session.get.return_value = _response(payload)

        result = PyPIReleaseClient(session=session).get_release(
            "friendly-bard",
            "2.4.0",
        )

        self.assertIsInstance(result, PackageReleaseProblem)
        assert isinstance(result, PackageReleaseProblem)
        self.assertEqual(result.state, "malformed_response")
        self.assertIn("non-negative integer", result.detail)


if __name__ == "__main__":
    unittest.main()
