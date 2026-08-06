"""Test bounded changelog-path discovery at one exact upstream commit."""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from requests.exceptions import Timeout

from upgradepilot.github.changelog import (
    ChangelogPathDiscoveryProblem,
    DiscoveredChangelogPath,
    GitHubChangelogPathClient,
)

_REPOSITORY = "example/friendly-bard"
_COMMIT = "a" * 40
_TREE = "b" * 40


def _response(status: int, payload: object) -> Mock:
    response = Mock()
    response.status_code = status
    response.json.return_value = payload
    return response


def _commit(*, sha: str = _COMMIT, tree_sha: str = _TREE) -> dict[str, object]:
    return {"sha": sha, "tree": {"sha": tree_sha}}


def _tree(
    entries: list[object],
    *,
    sha: str = _TREE,
    truncated: object = False,
) -> dict[str, object]:
    return {"sha": sha, "truncated": truncated, "tree": entries}


def _entry(path: str, *, object_type: str = "blob") -> dict[str, str]:
    return {"path": path, "type": object_type}


class GitHubChangelogPathClientTests(unittest.TestCase):
    def test_unique_nested_changelog_path_is_discovered_without_directory_constant(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(200, _commit()),
            _response(
                200,
                _tree(
                    [
                        _entry("README.md"),
                        _entry("docs/src/markdown/about/changelog.md"),
                        _entry("docs/src", object_type="tree"),
                    ]
                ),
            ),
        ]

        result = GitHubChangelogPathClient(session=session).discover(
            _REPOSITORY,
            _COMMIT,
        )

        self.assertIsInstance(result, DiscoveredChangelogPath)
        assert isinstance(result, DiscoveredChangelogPath)
        self.assertEqual(result.repository, _REPOSITORY)
        self.assertEqual(result.commit_sha, _COMMIT)
        self.assertEqual(result.tree_sha, _TREE)
        self.assertEqual(result.path, "docs/src/markdown/about/changelog.md")
        self.assertEqual(result.candidate_paths, (result.path,))
        self.assertEqual(session.get.call_count, 2)

    def test_admitted_basename_matching_is_case_insensitive(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(200, _commit()),
            _response(200, _tree([_entry("docs/CHANGELOG.MD")])),
        ]

        result = GitHubChangelogPathClient(session=session).discover(
            _REPOSITORY,
            _COMMIT,
        )

        self.assertIsInstance(result, DiscoveredChangelogPath)
        assert isinstance(result, DiscoveredChangelogPath)
        self.assertEqual(result.path, "docs/CHANGELOG.MD")

    def test_non_blob_candidate_name_is_not_admitted(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(200, _commit()),
            _response(200, _tree([_entry("CHANGELOG.md", object_type="tree")])),
        ]

        result = GitHubChangelogPathClient(session=session).discover(
            _REPOSITORY,
            _COMMIT,
        )

        self.assertIsInstance(result, ChangelogPathDiscoveryProblem)
        assert isinstance(result, ChangelogPathDiscoveryProblem)
        self.assertEqual(result.state, "no_candidate_path")

    def test_no_admitted_path_is_explicit(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(200, _commit()),
            _response(200, _tree([_entry("docs/guide.md"), _entry("README.md")])),
        ]

        result = GitHubChangelogPathClient(session=session).discover(
            _REPOSITORY,
            _COMMIT,
        )

        self.assertIsInstance(result, ChangelogPathDiscoveryProblem)
        assert isinstance(result, ChangelogPathDiscoveryProblem)
        self.assertEqual(result.state, "no_candidate_path")

    def test_multiple_admitted_paths_are_ambiguous_not_ranked(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(200, _commit()),
            _response(
                200,
                _tree(
                    [
                        _entry("CHANGELOG.md"),
                        _entry("docs/history.md"),
                    ]
                ),
            ),
        ]

        result = GitHubChangelogPathClient(session=session).discover(
            _REPOSITORY,
            _COMMIT,
        )

        self.assertIsInstance(result, ChangelogPathDiscoveryProblem)
        assert isinstance(result, ChangelogPathDiscoveryProblem)
        self.assertEqual(result.state, "multiple_candidate_paths")
        self.assertEqual(result.candidate_paths, ("CHANGELOG.md", "docs/history.md"))

    def test_truncated_recursive_tree_never_becomes_complete_discovery(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(200, _commit()),
            _response(200, _tree([_entry("CHANGELOG.md")], truncated=True)),
        ]

        result = GitHubChangelogPathClient(session=session).discover(
            _REPOSITORY,
            _COMMIT,
        )

        self.assertIsInstance(result, ChangelogPathDiscoveryProblem)
        assert isinstance(result, ChangelogPathDiscoveryProblem)
        self.assertEqual(result.state, "recursive_tree_truncated")

    def test_commit_response_must_echo_exact_requested_commit(self) -> None:
        session = Mock()
        session.get.return_value = _response(200, _commit(sha="c" * 40))

        result = GitHubChangelogPathClient(session=session).discover(
            _REPOSITORY,
            _COMMIT,
        )

        self.assertIsInstance(result, ChangelogPathDiscoveryProblem)
        assert isinstance(result, ChangelogPathDiscoveryProblem)
        self.assertEqual(result.state, "identity_mismatch")
        self.assertEqual(session.get.call_count, 1)

    def test_tree_response_must_echo_commit_root_tree(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(200, _commit()),
            _response(200, _tree([_entry("CHANGELOG.md")], sha="c" * 40)),
        ]

        result = GitHubChangelogPathClient(session=session).discover(
            _REPOSITORY,
            _COMMIT,
        )

        self.assertIsInstance(result, ChangelogPathDiscoveryProblem)
        assert isinstance(result, ChangelogPathDiscoveryProblem)
        self.assertEqual(result.state, "identity_mismatch")

    def test_non_boolean_truncated_field_is_malformed(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(200, _commit()),
            _response(200, _tree([_entry("CHANGELOG.md")], truncated="false")),
        ]

        result = GitHubChangelogPathClient(session=session).discover(
            _REPOSITORY,
            _COMMIT,
        )

        self.assertIsInstance(result, ChangelogPathDiscoveryProblem)
        assert isinstance(result, ChangelogPathDiscoveryProblem)
        self.assertEqual(result.state, "malformed_response")

    def test_malformed_tree_item_is_not_ignored(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(200, _commit()),
            _response(200, _tree([{"type": "blob"}])),
        ]

        result = GitHubChangelogPathClient(session=session).discover(
            _REPOSITORY,
            _COMMIT,
        )

        self.assertIsInstance(result, ChangelogPathDiscoveryProblem)
        assert isinstance(result, ChangelogPathDiscoveryProblem)
        self.assertEqual(result.state, "malformed_response")

    def test_missing_commit_is_source_unavailable(self) -> None:
        session = Mock()
        session.get.return_value = _response(404, {})

        result = GitHubChangelogPathClient(session=session).discover(
            _REPOSITORY,
            _COMMIT,
        )

        self.assertIsInstance(result, ChangelogPathDiscoveryProblem)
        assert isinstance(result, ChangelogPathDiscoveryProblem)
        self.assertEqual(result.state, "source_unavailable")
        self.assertEqual(result.status_code, 404)

    def test_transport_timeout_is_acquisition_failed(self) -> None:
        session = Mock()
        session.get.side_effect = Timeout("slow")

        result = GitHubChangelogPathClient(session=session).discover(
            _REPOSITORY,
            _COMMIT,
        )

        self.assertIsInstance(result, ChangelogPathDiscoveryProblem)
        assert isinstance(result, ChangelogPathDiscoveryProblem)
        self.assertEqual(result.state, "acquisition_failed")

    def test_invalid_commit_locator_is_rejected_before_network_access(self) -> None:
        session = Mock()

        with self.assertRaises(ValueError):
            GitHubChangelogPathClient(session=session).discover(
                _REPOSITORY,
                "main",
            )

        session.get.assert_not_called()


if __name__ == "__main__":
    unittest.main()
