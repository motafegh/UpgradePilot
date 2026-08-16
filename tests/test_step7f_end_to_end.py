"""Controlled Step 7F proof across the normal application path.

The external acquisition clients are controlled fixtures and LM Studio is replaced by one
controlled HTTP response, but the product executes the real Step 7B source window, Step
7C structured adapter/reconstruction, Step 7D deterministic claim admission, and Step
7E conditional target activation.
"""

from __future__ import annotations

import json
import unittest
from datetime import datetime, timezone
from unittest.mock import Mock, patch

from upgradepilot.dependency.analysis import DependencyChangeAnalysis
from upgradepilot.dependency.change import (
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.dependency.environment import RequirementsFileDependencyContext
from upgradepilot.github.changelog import DiscoveredChangelogPath
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.tag import GitHubTagCommitEvidence
from upgradepilot.investigation import investigate_public_pull_request
from upgradepilot.pypi.release import (
    PackageReleaseEvidence,
    PackageReleaseIndexEvidence,
    PyPIReleaseClient,
    PyPIReleaseIndexClient,
)
from upgradepilot.upstream.repository import UpstreamRepositoryEvidence
from upgradepilot.upstream.support_drop import evaluate_support_drop_runtime
from upgradepilot.upstream.support_drop_extractor import LocalSupportDropExtractor

_NOW = datetime(2026, 8, 5, tzinfo=timezone.utc)


class Step7FControlledEndToEndTests(unittest.TestCase):
    def test_real_runtime_layers_ground_claim_then_activate_target(self) -> None:
        harness = _Harness()
        post = Mock(
            return_value=_model_response(
                candidates=[
                    {
                        "python_line": "3.9",
                        "introduced_in_version": "1.1",
                        "source_line_id": "L2",
                    }
                ],
                unresolved=False,
                detail="",
            )
        )

        def evaluator(authority):
            harness.repository_client.get_exact_head_text_file.assert_not_called()
            return evaluate_support_drop_runtime(
                authority,
                extractor=LocalSupportDropExtractor(post=post),
            )

        result = _run(harness, evaluator)

        self.assertEqual(result.upstream_support_drop_result.python_line, "3.9")  # type: ignore[union-attr]
        self.assertEqual(
            result.upstream_support_drop_result.introduced_in_version,  # type: ignore[union-attr]
            "1.1",
        )
        self.assertEqual(result.target_python_result.requires_python, ">=3.10")  # type: ignore[union-attr]
        self.assertEqual(
            result.target_python_relevance_result.state,  # type: ignore[union-attr]
            "outside_declared_python_range",
        )
        harness.repository_client.get_exact_head_text_file.assert_called_once_with(
            harness.identity,
            "pyproject.toml",
        )
        harness.release_index_client.get_release_index.assert_called_once_with("demo")
        post.assert_called_once()

    def test_real_runtime_layers_no_claim_leave_target_inactive(self) -> None:
        harness = _Harness()
        post = Mock(
            return_value=_model_response(
                candidates=[],
                unresolved=False,
                detail="",
            )
        )

        def evaluator(authority):
            return evaluate_support_drop_runtime(
                authority,
                extractor=LocalSupportDropExtractor(post=post),
            )

        result = _run(harness, evaluator)

        self.assertEqual(
            result.upstream_support_drop_result.state,  # type: ignore[union-attr]
            "no_support_drop_claim",
        )
        self.assertIsNone(result.target_python_result)
        self.assertEqual(
            result.target_python_relevance_result.state,  # type: ignore[union-attr]
            "upstream_claim_unresolved",
        )
        harness.repository_client.get_exact_head_text_file.assert_not_called()
        harness.release_index_client.get_release_index.assert_called_once_with("demo")
        post.assert_called_once()
        self.assertEqual(result.ci_exercise_result.state, "no_successful_ci")  # type: ignore[union-attr]


class _Harness:
    def __init__(self) -> None:
        self.pull_client = Mock()
        self.actions_client = Mock()
        self.repository_client = Mock()
        self.package_client = Mock(spec=PyPIReleaseClient)
        self.release_index_client = Mock(spec=PyPIReleaseIndexClient)
        self.upstream_resolver = Mock()
        self.tag_client = Mock()
        self.changelog_client = Mock()

        self.identity = PullRequestIdentity(
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
        self.dependency = DependencyVersionChange(
            package="demo",
            normalized_package="demo",
            old_version="1.0",
            proposed_version="1.1",
            source_evidence=(
                DependencyChangeSourceEvidence(
                    path="requirements.txt",
                    file_format="exact_requirement",
                    extraction_method="changed_file_patch",
                ),
            ),
        )
        self.package = PackageReleaseEvidence(
            requested_package="demo",
            normalized_package="demo",
            requested_version="1.1",
            published_name="demo",
            published_version="1.1",
            source_url="https://pypi.org/pypi/demo/1.1/json",
            retrieved_at=_NOW,
            last_serial=1,
            distribution_files=(),
            project_urls=(),
        )
        self.upstream = UpstreamRepositoryEvidence(
            package_release=self.package,
            repository="example/upstream",
            source_candidates=(),
            provenance=(),
            provenance_unavailable_files=(),
        )

        self.pull_client.get_pull_request.return_value = self.identity
        self.pull_client.get_changed_files.return_value = (
            ChangedFile(
                filename="requirements.txt",
                status="modified",
                additions=1,
                deletions=1,
                changes=2,
                patch="-demo==1.0\n+demo==1.1",
            ),
        )
        self.actions_client.get_exact_head_workflow_runs.return_value = ()
        self.package_client.get_release.return_value = self.package
        self.release_index_client.get_release_index.return_value = PackageReleaseIndexEvidence(
            requested_package="demo",
            normalized_package="demo",
            published_name="demo",
            source_url="https://pypi.org/pypi/demo/json",
            retrieved_at=_NOW,
            last_serial=2,
            release_versions=("1.0", "1.1"),
        )
        self.upstream_resolver.resolve.return_value = self.upstream
        self.tag_client.resolve_tag_to_commit.return_value = GitHubTagCommitEvidence(
            repository="example/upstream",
            requested_tag="1.1",
            tag_ref="refs/tags/1.1",
            tag_object_type="commit",
            tag_object_sha="c" * 40,
            resolved_commit_sha="c" * 40,
            peeled_tag_object_shas=(),
            retrieved_at=_NOW,
        )
        self.changelog_client.discover.return_value = DiscoveredChangelogPath(
            repository="example/upstream",
            commit_sha="c" * 40,
            tree_sha="d" * 40,
            path="CHANGELOG.md",
            candidate_paths=("CHANGELOG.md",),
        )

        changelog = "## 1.1\n- Drop support for Python 3.9.\n"
        changelog_size = len(changelog.encode("utf-8"))
        self.repository_client.get_exact_commit_text_file.return_value = RepositoryTextFile(
            repository="example/upstream",
            path="CHANGELOG.md",
            returned_path="CHANGELOG.md",
            revision="c" * 40,
            blob_sha="e" * 40,
            reported_byte_count=changelog_size,
            decoded_byte_count=changelog_size,
            content=changelog,
            retrieved_at=_NOW,
        )

        target = '[project]\nrequires-python = ">=3.10"\n'
        target_size = len(target.encode("utf-8"))
        self.repository_client.get_exact_head_text_file.return_value = RepositoryTextFile(
            repository="example/project",
            path="pyproject.toml",
            returned_path="pyproject.toml",
            revision=self.identity.head_sha,
            blob_sha="f" * 40,
            reported_byte_count=target_size,
            decoded_byte_count=target_size,
            content=target,
            retrieved_at=_NOW,
        )


def _run(harness: _Harness, evaluator):
    source_context = RequirementsFileDependencyContext(
        repository=harness.identity.repository,
        revision=harness.identity.head_sha,
        normalized_package=harness.dependency.normalized_package,
        source_evidence=harness.dependency.source_evidence[0],
    )
    with patch(
        "upgradepilot.investigation.analyze_dependency_change",
        return_value=DependencyChangeAnalysis(
            dependency=harness.dependency,
            source_contexts=(source_context,),
        ),
    ):
        return investigate_public_pull_request(
            "example/project",
            7,
            pull_client=harness.pull_client,
            actions_client=harness.actions_client,
            repository_client=harness.repository_client,
            package_client=harness.package_client,
            release_index_client=harness.release_index_client,
            upstream_repository_resolver=harness.upstream_resolver,
            tag_client=harness.tag_client,
            changelog_client=harness.changelog_client,
            support_drop_evaluator=evaluator,
        )


def _model_response(*, candidates, unresolved: bool, detail: str) -> Mock:
    response = Mock()
    response.status_code = 200
    response.json.return_value = {
        "choices": [
            {
                "finish_reason": "stop",
                "message": {
                    "content": json.dumps(
                        {
                            "candidates": candidates,
                            "unresolved_if_no_candidates": unresolved,
                            "detail": detail,
                        }
                    )
                },
            }
        ]
    }
    return response


if __name__ == "__main__":
    unittest.main()
