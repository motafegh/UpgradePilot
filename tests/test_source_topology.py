"""Protect the admitted responsibility-based source topology during reconciliation."""

from __future__ import annotations

import unittest

import upgradepilot
from upgradepilot.dependency.analysis import analyze_dependency_change
from upgradepilot.dependency.change import DependencyChangeProblem, DependencyVersionChange
from upgradepilot.dependency.requirements import extract_exact_requirement_changes
from upgradepilot.github.changelog import GitHubChangelogPathClient
from upgradepilot.github.pull_request import GitHubPullRequestClient
from upgradepilot.investigation import investigate_public_pull_request
from upgradepilot.target.python_specifier import evaluate_python_line_specifier
from upgradepilot.upstream.repository import UpstreamRepositoryEvidence


class SourceTopologyTests(unittest.TestCase):
    def test_root_package_is_not_an_internal_api_facade(self) -> None:
        self.assertEqual(upgradepilot.__all__, ())
        self.assertFalse(hasattr(upgradepilot, "PinnedDependencyChange"))
        self.assertFalse(hasattr(upgradepilot, "GitHubReadClient"))

    def test_dependency_owners_are_importable(self) -> None:
        self.assertIsNotNone(analyze_dependency_change)
        self.assertIsNotNone(DependencyVersionChange)
        self.assertIsNotNone(DependencyChangeProblem)
        self.assertIsNotNone(extract_exact_requirement_changes)

    def test_provider_and_target_owners_are_importable(self) -> None:
        self.assertIsNotNone(GitHubPullRequestClient)
        self.assertIsNotNone(GitHubChangelogPathClient)
        self.assertIsNotNone(evaluate_python_line_specifier)

    def test_upstream_repository_evidence_has_no_semantic_claim_state(self) -> None:
        self.assertNotIn("claim_state", UpstreamRepositoryEvidence.__dataclass_fields__)

    def test_application_orchestration_has_concrete_entry_point(self) -> None:
        self.assertEqual(
            investigate_public_pull_request.__name__,
            "investigate_public_pull_request",
        )


if __name__ == "__main__":
    unittest.main()
