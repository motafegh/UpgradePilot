"""Proof for the first bounded maintainer-action synthesis evaluator."""

from __future__ import annotations

import unittest
from dataclasses import replace

from upgradepilot.ci.dependency_exercise import DependencyCICoverageResult
from upgradepilot.dependency.change import (
    DependencyChangeProblem,
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.github.changelog import ChangelogPathDiscoveryProblem
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.impact.artifact_serviceability import ArtifactServiceabilityEvidenceProblem
from upgradepilot.investigation import PublicPullRequestInvestigation
from upgradepilot.maintainer_action import synthesize_maintainer_action
from upgradepilot.pypi.release import PackageReleaseProblem
from upgradepilot.upstream.claim import UpstreamSupportDropClaimProblem
from upgradepilot.upstream.interval import release_interval_from_dependency_change


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

    def test_runtime_correlated_ci_support_does_not_create_action_permission(self) -> None:
        ci = DependencyCICoverageResult(
            state="supported_runtime_correlated",
            reason="successful_exact_head_ci_with_runtime_correlated_dependency_consumption",
            detail=(
                "One dependency-consuming user step is correlated to completed-successful "
                "runtime execution."
            ),
            workflows=(),
        )
        investigation = _investigation(_dependency(), ci_coverage_result=ci)

        result = synthesize_maintainer_action(investigation)

        self.assertEqual(result.action, "abstain")
        self.assertEqual(result.residual_uncertainty, ())
        self.assertIn("withholds merge", result.limitations[0])

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


    def test_branch_stopping_changelog_problem_is_preserved_without_python_impact(self) -> None:
        investigation = replace(
            _investigation(_dependency()),
            changelog_path_result=ChangelogPathDiscoveryProblem(
                state="no_candidate_path",
                repository="example/upstream",
                commit_sha="c" * 40,
                detail="No admitted changelog path.",
            ),
        )

        result = synthesize_maintainer_action(investigation)

        self.assertEqual(result.action, "abstain")
        self.assertEqual(
            result.residual_uncertainty,
            (
                "Upstream changelog discovery remains no_candidate_path: "
                "No admitted changelog path.",
            ),
        )

    def test_artifact_evidence_problem_is_preserved_without_impact_assessment(self) -> None:
        investigation = replace(
            _investigation(_dependency()),
            artifact_serviceability_candidate_result=ArtifactServiceabilityEvidenceProblem(
                state="wheel_filename_uninterpretable",
                release_version="1.0",
                filename="broken.whl",
                detail="Published wheel filename could not be interpreted.",
            ),
        )

        result = synthesize_maintainer_action(investigation)

        self.assertEqual(
            result.residual_uncertainty,
            (
                "Artifact-serviceability candidate evidence remains "
                "wheel_filename_uninterpretable: "
                "Published wheel filename could not be interpreted.",
            ),
        )

    def test_closed_no_support_drop_claim_does_not_manufacture_uncertainty(self) -> None:
        dependency = _dependency()
        investigation = replace(
            _investigation(dependency),
            upstream_support_drop_result=UpstreamSupportDropClaimProblem(
                state="no_support_drop_claim",
                interval=release_interval_from_dependency_change(dependency),
                detail="No relevant Python support-drop claim was established.",
            ),
        )

        result = synthesize_maintainer_action(investigation)

        self.assertEqual(result.residual_uncertainty, ())

    def test_independent_upstream_and_artifact_problems_are_preserved_deterministically(self) -> None:
        investigation = replace(
            _investigation(_dependency()),
            changelog_path_result=ChangelogPathDiscoveryProblem(
                state="no_candidate_path",
                repository="example/upstream",
                commit_sha="c" * 40,
                detail="No admitted changelog path.",
            ),
            old_package_result=PackageReleaseProblem(
                state="acquisition_failed",
                requested_package="demo",
                normalized_package="demo",
                requested_version="1.0",
                source_url="https://pypi.org/pypi/demo/1.0/json",
                detail="Old release lookup failed.",
            ),
        )

        result = synthesize_maintainer_action(investigation)

        self.assertEqual(
            result.residual_uncertainty,
            (
                "Upstream changelog discovery remains no_candidate_path: "
                "No admitted changelog path.",
                "Old package-release evidence remains acquisition_failed: "
                "Old release lookup failed.",
            ),
        )


def _investigation(
    dependency_result: DependencyVersionChange | DependencyChangeProblem,
    *,
    ci_coverage_result: DependencyCICoverageResult | None = None,
) -> PublicPullRequestInvestigation:
    return PublicPullRequestInvestigation(
        pull_request=_identity(),
        changed_files=(_changed_file(),),
        dependency_result=dependency_result,
        target_python_result=None,
        workflow_evidence=(),
        ci_coverage_result=ci_coverage_result,
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
