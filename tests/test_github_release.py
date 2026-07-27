"""Test published GitHub Release and exact tag-ref acquisition."""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from upgradepilot.github_release import (
    GitHubReleaseClient,
    GitHubReleaseEvidence,
    GitHubReleaseProblem,
)


def _response(status: int, payload: object) -> Mock:
    response = Mock()
    response.status_code = status
    response.json.return_value = payload
    return response


def _release_payload(
    *,
    tag: str = "2.4.0",
    body: str | None = "Release notes",
) -> dict[str, object]:
    return {
        "id": 42,
        "tag_name": tag,
        "html_url": f"https://github.com/example/friendly-bard/releases/tag/{tag}",
        "name": "",
        "body": body,
        "draft": False,
        "prerelease": False,
        "published_at": "2026-07-27T20:00:00Z",
    }


class GitHubReleaseClientTests(unittest.TestCase):
    def test_release_is_bound_to_exact_tag_reference(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(200, _release_payload()),
            _response(
                200,
                {
                    "ref": "refs/tags/2.4.0",
                    "object": {"type": "commit", "sha": "abc123"},
                },
            ),
        ]

        result = GitHubReleaseClient(session=session).get_release(
            "example/friendly-bard",
            "2.4.0",
        )

        self.assertIsInstance(result, GitHubReleaseEvidence)
        assert isinstance(result, GitHubReleaseEvidence)
        self.assertEqual(result.release_id, 42)
        self.assertEqual(result.release_name, "")
        self.assertEqual(result.tag_ref, "refs/tags/2.4.0")
        self.assertEqual(result.tag_object_type, "commit")
        self.assertEqual(result.tag_object_sha, "abc123")
        self.assertEqual(session.get.call_count, 2)

    def test_missing_published_release_is_source_unavailable(self) -> None:
        session = Mock()
        session.get.return_value = _response(404, {})

        result = GitHubReleaseClient(session=session).get_release(
            "example/friendly-bard",
            "2.4.0",
        )

        self.assertIsInstance(result, GitHubReleaseProblem)
        assert isinstance(result, GitHubReleaseProblem)
        self.assertEqual(result.state, "source_unavailable")
        self.assertEqual(session.get.call_count, 1)

    def test_returned_release_tag_mismatch_is_rejected(self) -> None:
        session = Mock()
        session.get.return_value = _response(
            200,
            _release_payload(tag="2.4.1"),
        )

        result = GitHubReleaseClient(session=session).get_release(
            "example/friendly-bard",
            "2.4.0",
        )

        self.assertIsInstance(result, GitHubReleaseProblem)
        assert isinstance(result, GitHubReleaseProblem)
        self.assertEqual(result.state, "identity_mismatch")
        self.assertEqual(session.get.call_count, 1)

    def test_oversized_release_body_is_malformed(self) -> None:
        session = Mock()
        session.get.return_value = _response(
            200,
            _release_payload(body="abcd"),
        )

        result = GitHubReleaseClient(
            session=session,
            max_release_body_chars=3,
        ).get_release("example/friendly-bard", "2.4.0")

        self.assertIsInstance(result, GitHubReleaseProblem)
        assert isinstance(result, GitHubReleaseProblem)
        self.assertEqual(result.state, "malformed_response")
        self.assertIn("character limit", result.detail)


if __name__ == "__main__":
    unittest.main()
