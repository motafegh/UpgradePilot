"""Proof for the first bounded maintainer-action synthesis evaluator."""

from __future__ import annotations

import unittest

from upgradepilot.dependency.change import (
    DependencyChangeProblem,
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.investigation import PublicPullRequestInvestigation
from upgradepilot.maintainer_action import synthesize_maintainer_action


class MaintainerActionSynthesisTests(unittest.TestCase):
    def test_supported_transition_does_not_default_to_favorable_or_other_active_action(self) -> None:
        investigation = _investigation(_dependency())

        result = synthesize_maintainer_action(investigation)

        self.assertEqual(result.action, "abstain")
        self.assertIs(result.source_investigation, investigation)
        self.assertEqual(
            result.decisive_reasons,
            (
                "No non-abstention maintainer-action permission is admitted at the "
                "current evaluator proof boundary.",
            ),
        )
        self.assertEqual(result.residual_uncertainty, ())
        self.assertIn("withholds merge", result.limitations[0])
        self.assertTrue(
            any("not establish complete impact-candidate" in item for item in result.claim_limits)
        )

    def test_dependency_problem_is_preserved_in_abstention_reason_and_uncertainty(self) -> None:
        problem = DependencyChangeProblem(
            reason="no_supported_dependency_file",
            detail="No admitted dependency source established one dependency transition.",
        )
        investigation = _investigation(problem)

        result = synthesize_maintainer_action(investigation)

        self.assertEqual(result.action, "abstain")
        self.assertIn("no_supported_dependency_file", result.decisive_reasons[0])
        self.assertEqual(len(result.residual_uncertainty), 1)
        self.assertIn(
            "No admitted dependency source established one dependency transition.",
            result.residual_uncertainty[0],
        )
        self.assertTrue(
            any("safe or unsafe" in item for item in result.claim_limits)
        )


def _investigation(
    dependency_result: DependencyVersionChange | DependencyChangeProblem,
) -> PublicPullRequestInvestigation:
    return PublicPullRequestInvestigation(
        pull_request=_identity(),
        changed_files=(_changed_file(),),
        dependency_result=dependency_result,
        target_python_result=None,
        workflow_evidence=(),
        ci_coverage_result=None,
        package_result=None,
        upstream_repository_result=None,
    )


def _identity() -> PullRequestIdentity:
    return PullRequestIdentity(
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


def _changed_file() -> ChangedFile:
    return ChangedFile(
        filename="uv.lock",
        status="modified",
        additions=1,
        deletions=1,
        changes=2,
        patch=None,
    )


def _dependency() -> DependencyVersionChange:
    return DependencyVersionChange(
        package="demo",
        normalized_package="demo",
        old_version="1.0",
        proposed_version="1.1",
        source_evidence=(
            DependencyChangeSourceEvidence(
                path="uv.lock",
                file_format="uv_lock",
                extraction_method="exact_base_head_files",
            ),
        ),
    )


if __name__ == "__main__":
    unittest.main()
