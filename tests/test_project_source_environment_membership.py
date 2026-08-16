"""Test dependency-owned comparison of affected pyproject environments and selectors."""

from __future__ import annotations

import unittest

from upgradepilot.dependency.change import DependencyChangeSourceEvidence
from upgradepilot.dependency.environment import (
    PyprojectDependencyGroupContext,
    PyprojectOptionalExtraDependencyContext,
)
from upgradepilot.dependency.environment_membership import (
    evaluate_project_source_environment_membership,
)
from upgradepilot.dependency.environment_selection import (
    AllDependencyGroupsSelector,
    AllOptionalExtrasSelector,
    DependencyGroupSelector,
    OptionalExtraSelector,
    ProjectEnvironmentSelectionDeclaration,
)


def _evidence(path: str = "pyproject.toml") -> DependencyChangeSourceEvidence:
    return DependencyChangeSourceEvidence(
        path=path,
        file_format="pyproject_optional_extra",
        extraction_method="exact_base_head_files",
    )


def _extra(name: str = "mlx", *, path: str = "pyproject.toml"):
    return PyprojectOptionalExtraDependencyContext(
        repository="example/project",
        revision="a" * 40,
        normalized_package="numpy",
        source_evidence=_evidence(path),
        extra=name,
    )


def _group(name: str = "docs", *, path: str = "pyproject.toml"):
    return PyprojectDependencyGroupContext(
        repository="example/project",
        revision="a" * 40,
        normalized_package="soupsieve",
        source_evidence=_evidence(path),
        group=name,
    )


def _declaration(*selectors: object, project_root: str | None = None):
    return ProjectEnvironmentSelectionDeclaration(
        manager="pip",
        operation="install",
        segment_index=0,
        project_root=project_root,
        selectors=selectors,  # type: ignore[arg-type]
    )


class ProjectSourceEnvironmentMembershipTests(unittest.TestCase):
    def test_matching_optional_extra_is_direct_membership(self) -> None:
        result = evaluate_project_source_environment_membership(
            _extra("MLX"),
            _declaration(OptionalExtraSelector("mlx")),
        )

        self.assertEqual(result.state, "member")
        self.assertEqual(result.reason, "affected_optional_extra_selected")

    def test_s011_dev_does_not_establish_affected_mlx_extra(self) -> None:
        result = evaluate_project_source_environment_membership(
            _extra("mlx"),
            _declaration(OptionalExtraSelector("dev")),
        )

        self.assertEqual(result.state, "not_established")
        self.assertEqual(result.reason, "affected_optional_extra_not_selected")
        self.assertIn("mlx", result.detail)

    def test_all_extras_selects_affected_optional_extra(self) -> None:
        result = evaluate_project_source_environment_membership(
            _extra("mlx"),
            _declaration(AllOptionalExtrasSelector()),
        )

        self.assertEqual(result.state, "member")

    def test_matching_dependency_group_and_all_groups_are_supported(self) -> None:
        direct = evaluate_project_source_environment_membership(
            _group("Docs_Test"),
            _declaration(DependencyGroupSelector("docs-test")),
        )
        all_groups = evaluate_project_source_environment_membership(
            _group("docs"),
            _declaration(AllDependencyGroupsSelector()),
        )

        self.assertEqual(direct.state, "member")
        self.assertEqual(all_groups.state, "member")

    def test_extra_selector_does_not_imply_dependency_group_selection(self) -> None:
        result = evaluate_project_source_environment_membership(
            _group("docs"),
            _declaration(OptionalExtraSelector("docs")),
        )

        self.assertEqual(result.state, "not_established")

    def test_project_root_mismatch_is_unresolved(self) -> None:
        result = evaluate_project_source_environment_membership(
            _extra("mlx", path="packages/api/pyproject.toml"),
            _declaration(OptionalExtraSelector("mlx"), project_root=None),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "project_environment_root_mismatch")


if __name__ == "__main__":
    unittest.main()
