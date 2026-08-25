"""Protect the accepted responsibility-based source topology.

These are import/topology checks, not feature tests. They ensure new code can import the
preferred responsibility owners directly, the package root stays intentionally small,
and the completed migration cannot silently reintroduce the old flat compatibility
module layer.
"""

from __future__ import annotations

import importlib.util
import unittest

import upgradepilot
from upgradepilot.ci.consumption import compose_project_environment_consumption
from upgradepilot.ci.dependency_exercise import (
    evaluate_dependency_ci_coverage,
    evaluate_dependency_ci_exercise,
)
from upgradepilot.ci.workflow_commands import (
    derive_project_environment_consumptions,
    inspect_workflow_dependency_evidence,
)
from upgradepilot.dependency.analysis import analyze_dependency_change
from upgradepilot.dependency.change import DependencyVersionChange
from upgradepilot.dependency.direct_install import observe_direct_installation_declaration
from upgradepilot.dependency.environment_membership import (
    evaluate_project_source_environment_membership,
)
from upgradepilot.dependency.environment_selection import (
    observe_project_environment_selection,
)
from upgradepilot.dependency.pyproject import extract_pyproject_optional_extra_change
from upgradepilot.dependency.requirements import extract_exact_requirement_changes
from upgradepilot.dependency.uv_lock import extract_uv_lock_changes
from upgradepilot.dependency.uv_reachability import evaluate_uv_selected_root_reachability
from upgradepilot.dependency.versioning import parse_dependency_release_interval
from upgradepilot.github.actions import GitHubActionsClient
from upgradepilot.github.api import GitHubApiClient
from upgradepilot.github.changelog import GitHubChangelogPathClient
from upgradepilot.github.pull_request import GitHubPullRequestClient
from upgradepilot.github.release import GitHubReleaseClient
from upgradepilot.github.repository import GitHubRepositoryClient
from upgradepilot.github.tag import GitHubTagCommitClient
from upgradepilot.github.workflow_definition import parse_workflow_definition
from upgradepilot.pypi.api import PyPIJsonApiClient
from upgradepilot.pypi.provenance import PyPIProvenanceClient
from upgradepilot.pypi.release import PyPIReleaseClient
from upgradepilot.target.python import interpret_target_python_declaration
from upgradepilot.target.python_specifier import evaluate_python_line_specifier
from upgradepilot.target.relevance import evaluate_target_python_relevance
from upgradepilot.upstream.changelog import build_crossed_release_source_window
from upgradepilot.upstream.claim import validate_support_drop_candidates
from upgradepilot.upstream.interval import assemble_upstream_interval_authority
from upgradepilot.upstream.interval_evidence import select_crossed_release_index
from upgradepilot.upstream.repository import UpstreamRepositoryResolver
from upgradepilot.upstream.support_drop import evaluate_support_drop_runtime
from upgradepilot.upstream.support_drop_extractor import LocalSupportDropExtractor


_OBSOLETE_FLAT_MODULES = (
    "upgradepilot.ci_dependency_exercise",
    "upgradepilot.dependency_analysis",
    "upgradepilot.dependency_change",
    "upgradepilot.exact_requirement_change",
    "upgradepilot.github_actions",
    "upgradepilot.github_api",
    "upgradepilot.github_client",
    "upgradepilot.github_release",
    "upgradepilot.github_repository",
    "upgradepilot.github_tag",
    "upgradepilot.packaging_method",
    "upgradepilot.pypi_api",
    "upgradepilot.pypi_client",
    "upgradepilot.pypi_provenance",
    "upgradepilot.target_python",
    "upgradepilot.target_python_relevance",
    "upgradepilot.upstream_changelog",
    "upgradepilot.upstream_claim",
    "upgradepilot.upstream_interval_acquisition",
    "upgradepilot.upstream_source",
    "upgradepilot.uv_lock_change",
    "upgradepilot.workflow_commands",
)


class SourceTopologyTests(unittest.TestCase):
    def test_responsibility_modules_import_from_new_owners(self) -> None:
        objects = (
            compose_project_environment_consumption,
            evaluate_dependency_ci_coverage,
            evaluate_dependency_ci_exercise,
            derive_project_environment_consumptions,
            inspect_workflow_dependency_evidence,
            analyze_dependency_change,
            DependencyVersionChange,
            observe_direct_installation_declaration,
            evaluate_project_source_environment_membership,
            observe_project_environment_selection,
            evaluate_uv_selected_root_reachability,
            extract_pyproject_optional_extra_change,
            extract_exact_requirement_changes,
            extract_uv_lock_changes,
            parse_dependency_release_interval,
            GitHubActionsClient,
            GitHubApiClient,
            GitHubChangelogPathClient,
            GitHubPullRequestClient,
            GitHubReleaseClient,
            GitHubRepositoryClient,
            GitHubTagCommitClient,
            parse_workflow_definition,
            PyPIJsonApiClient,
            PyPIProvenanceClient,
            PyPIReleaseClient,
            interpret_target_python_declaration,
            evaluate_python_line_specifier,
            evaluate_target_python_relevance,
            build_crossed_release_source_window,
            validate_support_drop_candidates,
            assemble_upstream_interval_authority,
            select_crossed_release_index,
            UpstreamRepositoryResolver,
            evaluate_support_drop_runtime,
            LocalSupportDropExtractor,
        )
        self.assertTrue(all(callable(item) or isinstance(item, type) for item in objects))

    def test_package_root_remains_intentionally_minimal(self) -> None:
        self.assertEqual(upgradepilot.__all__, ())

    def test_obsolete_flat_module_paths_are_absent(self) -> None:
        for module_name in _OBSOLETE_FLAT_MODULES:
            with self.subTest(module=module_name):
                self.assertIsNone(importlib.util.find_spec(module_name))


if __name__ == "__main__":
    unittest.main()
