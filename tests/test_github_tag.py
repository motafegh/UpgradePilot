"""Test exact Git tag-reference identity and bounded annotated-tag peeling."""

from __future__ import annotations

import unittest
from datetime import datetime, timezone
from unittest.mock import Mock

from requests.exceptions import Timeout

from upgradepilot.github.tag import (
    GitHubTagCommitClient,
    GitHubTagCommitEvidence,
    GitHubTagCommitProblem,
)

_NOW = datetime(2026, 8, 2, 12, 0, tzinfo=timezone.utc)
_REPOSITORY = "example/friendly-bard"
_TAG = "v2.8.4"


def _response(status: int, payload: object) -> Mock:
    response = Mock()
    response.status_code = status
    response.json.return_value = payload
    return response


def _ref(*, object_type: str, object_sha: str, tag: str = _TAG) -> dict[str, object]:
    return {
        "ref": f"refs/tags/{tag}",
        "object": {"type": object_type, "sha": object_sha},
    }


def _tag_object(
    sha: str,
    *,
    target_type: str,
    target_sha: str,
) -> dict[str, object]:
    return {
        "sha": sha,
        "object": {"type": target_type, "sha": target_sha},
    }


class GitHubTagCommitClientTests(unittest.TestCase):
    """Protect the ref → tag-object(s) → commit evidence path."""

    def test_lightweight_tag_resolves_directly_to_commit(self) -> None:
        session = Mock()
        session.get.return_value = _response(
            200,
            _ref(object_type="commit", object_sha="commit-sha"),
        )

        result = GitHubTagCommitClient(
            session=session,
            now=lambda: _NOW,
        ).resolve_tag_to_commit(_REPOSITORY, _TAG)

        self.assertIsInstance(result, GitHubTagCommitEvidence)
        assert isinstance(result, GitHubTagCommitEvidence)
        self.assertEqual(result.tag_ref, "refs/tags/v2.8.4")
        self.assertEqual(result.tag_object_type, "commit")
        self.assertEqual(result.tag_object_sha, "commit-sha")
        self.assertEqual(result.resolved_commit_sha, "commit-sha")
        self.assertEqual(result.peeled_tag_object_shas, ())
        self.assertEqual(result.peel_depth, 0)
        self.assertEqual(result.retrieved_at, _NOW)
        self.assertEqual(session.get.call_count, 1)

    def test_annotated_tag_peels_one_tag_object_to_commit(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(200, _ref(object_type="tag", object_sha="tag-object-a")),
            _response(
                200,
                _tag_object(
                    "tag-object-a",
                    target_type="commit",
                    target_sha="commit-sha",
                ),
            ),
        ]

        result = GitHubTagCommitClient(session=session).resolve_tag_to_commit(
            _REPOSITORY,
            _TAG,
        )

        self.assertIsInstance(result, GitHubTagCommitEvidence)
        assert isinstance(result, GitHubTagCommitEvidence)
        self.assertEqual(result.tag_object_type, "tag")
        self.assertEqual(result.tag_object_sha, "tag-object-a")
        self.assertEqual(result.resolved_commit_sha, "commit-sha")
        self.assertEqual(result.peeled_tag_object_shas, ("tag-object-a",))
        self.assertEqual(result.peel_depth, 1)
        self.assertEqual(session.get.call_count, 2)

    def test_nested_annotated_tags_peel_deterministically(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(200, _ref(object_type="tag", object_sha="tag-a")),
            _response(
                200,
                _tag_object("tag-a", target_type="tag", target_sha="tag-b"),
            ),
            _response(
                200,
                _tag_object("tag-b", target_type="commit", target_sha="commit-sha"),
            ),
        ]

        result = GitHubTagCommitClient(session=session).resolve_tag_to_commit(
            _REPOSITORY,
            _TAG,
        )

        self.assertIsInstance(result, GitHubTagCommitEvidence)
        assert isinstance(result, GitHubTagCommitEvidence)
        self.assertEqual(result.resolved_commit_sha, "commit-sha")
        self.assertEqual(result.peeled_tag_object_shas, ("tag-a", "tag-b"))
        self.assertEqual(result.peel_depth, 2)

    def test_exact_returned_ref_must_match_requested_tag(self) -> None:
        session = Mock()
        session.get.return_value = _response(
            200,
            _ref(object_type="commit", object_sha="commit-sha", tag="v2.8.3"),
        )

        result = GitHubTagCommitClient(session=session).resolve_tag_to_commit(
            _REPOSITORY,
            _TAG,
        )

        self.assertIsInstance(result, GitHubTagCommitProblem)
        assert isinstance(result, GitHubTagCommitProblem)
        self.assertEqual(result.state, "identity_mismatch")

    def test_missing_tag_reference_is_source_unavailable(self) -> None:
        session = Mock()
        session.get.return_value = _response(404, {})

        result = GitHubTagCommitClient(session=session).resolve_tag_to_commit(
            _REPOSITORY,
            _TAG,
        )

        self.assertIsInstance(result, GitHubTagCommitProblem)
        assert isinstance(result, GitHubTagCommitProblem)
        self.assertEqual(result.state, "source_unavailable")
        self.assertEqual(result.status_code, 404)

    def test_unsupported_direct_git_object_type_is_explicit(self) -> None:
        session = Mock()
        session.get.return_value = _response(
            200,
            _ref(object_type="tree", object_sha="tree-sha"),
        )

        result = GitHubTagCommitClient(session=session).resolve_tag_to_commit(
            _REPOSITORY,
            _TAG,
        )

        self.assertIsInstance(result, GitHubTagCommitProblem)
        assert isinstance(result, GitHubTagCommitProblem)
        self.assertEqual(result.state, "unsupported_object_type")
        self.assertEqual(result.object_sha, "tree-sha")

    def test_annotated_tag_response_must_echo_requested_object_sha(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(200, _ref(object_type="tag", object_sha="tag-a")),
            _response(
                200,
                _tag_object("different-tag", target_type="commit", target_sha="commit"),
            ),
        ]

        result = GitHubTagCommitClient(session=session).resolve_tag_to_commit(
            _REPOSITORY,
            _TAG,
        )

        self.assertIsInstance(result, GitHubTagCommitProblem)
        assert isinstance(result, GitHubTagCommitProblem)
        self.assertEqual(result.state, "identity_mismatch")
        self.assertEqual(result.object_sha, "tag-a")

    def test_annotated_tag_object_cycle_is_rejected(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(200, _ref(object_type="tag", object_sha="tag-a")),
            _response(200, _tag_object("tag-a", target_type="tag", target_sha="tag-b")),
            _response(200, _tag_object("tag-b", target_type="tag", target_sha="tag-a")),
        ]

        result = GitHubTagCommitClient(session=session).resolve_tag_to_commit(
            _REPOSITORY,
            _TAG,
        )

        self.assertIsInstance(result, GitHubTagCommitProblem)
        assert isinstance(result, GitHubTagCommitProblem)
        self.assertEqual(result.state, "peel_cycle")
        self.assertEqual(result.object_sha, "tag-a")
        self.assertEqual(session.get.call_count, 3)

    def test_configured_peel_depth_is_a_hard_bound(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(200, _ref(object_type="tag", object_sha="tag-a")),
            _response(200, _tag_object("tag-a", target_type="tag", target_sha="tag-b")),
        ]

        result = GitHubTagCommitClient(
            session=session,
            max_peel_depth=1,
        ).resolve_tag_to_commit(_REPOSITORY, _TAG)

        self.assertIsInstance(result, GitHubTagCommitProblem)
        assert isinstance(result, GitHubTagCommitProblem)
        self.assertEqual(result.state, "peel_depth_exceeded")
        self.assertEqual(result.object_sha, "tag-b")
        self.assertEqual(session.get.call_count, 2)

    def test_missing_required_tag_object_field_is_malformed(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(200, _ref(object_type="tag", object_sha="tag-a")),
            _response(200, {"sha": "tag-a", "object": {"type": "commit"}}),
        ]

        result = GitHubTagCommitClient(session=session).resolve_tag_to_commit(
            _REPOSITORY,
            _TAG,
        )

        self.assertIsInstance(result, GitHubTagCommitProblem)
        assert isinstance(result, GitHubTagCommitProblem)
        self.assertEqual(result.state, "malformed_response")
        self.assertIn("sha", result.detail)

    def test_timeout_is_acquisition_failed_not_missing_source(self) -> None:
        session = Mock()
        session.get.side_effect = Timeout("slow")

        result = GitHubTagCommitClient(session=session).resolve_tag_to_commit(
            _REPOSITORY,
            _TAG,
        )

        self.assertIsInstance(result, GitHubTagCommitProblem)
        assert isinstance(result, GitHubTagCommitProblem)
        self.assertEqual(result.state, "acquisition_failed")

    def test_public_input_and_bound_validation_is_strict(self) -> None:
        with self.assertRaises(ValueError):
            GitHubTagCommitClient(max_peel_depth=0)
        with self.assertRaises(ValueError):
            GitHubTagCommitClient(max_peel_depth=True)

        client = GitHubTagCommitClient(session=Mock())
        with self.assertRaises(ValueError):
            client.resolve_tag_to_commit("not-a-repository", _TAG)
        with self.assertRaises(ValueError):
            client.resolve_tag_to_commit(_REPOSITORY, " v2.8.4 ")


if __name__ == "__main__":
    unittest.main()
