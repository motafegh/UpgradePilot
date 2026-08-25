"""Test static pip/uv project-environment selection without runtime claims."""

from __future__ import annotations

import unittest

from upgradepilot.dependency.environment_selection import (
    AllDependencyGroupsSelector,
    AllOptionalExtrasSelector,
    DependencyGroupSelector,
    OptionalExtraSelector,
    observe_project_environment_selection,
)
from upgradepilot.github.workflow_definition import (
    RunDefaults,
    RunStepDefinition,
    SourceSpan,
    StaticScalarValue,
)

_SPAN = SourceSpan(start_line=1, start_column=1, end_line=1, end_column=2)


def _scalar(text: str) -> StaticScalarValue:
    return StaticScalarValue(
        text=text,
        contains_expression="${{" in text,
        span=_SPAN,
    )


def _defaults(working_directory: str | None) -> RunDefaults | None:
    if working_directory is None:
        return None
    return RunDefaults(
        shell=None,
        working_directory=_scalar(working_directory),
        span=_SPAN,
    )


def _step(command: str, *, working_directory: str | None = None) -> RunStepDefinition:
    return RunStepDefinition(
        source_index=4,
        command=_scalar(command),
        name=None,
        condition=None,
        continue_on_error=None,
        shell=None,
        working_directory=(
            _scalar(working_directory) if working_directory is not None else None
        ),
        span=_SPAN,
    )


class ProjectEnvironmentSelectionTests(unittest.TestCase):
    def test_s011_pip_editable_dev_selects_only_visible_dev_extra(self) -> None:
        result = observe_project_environment_selection(
            _step('pip install -e ".[dev]"'),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(len(result.declarations), 1)
        declaration = result.declarations[0]
        self.assertEqual(declaration.manager, "pip")
        self.assertEqual(declaration.operation, "install")
        self.assertIsNone(declaration.project_root)
        self.assertEqual(declaration.package_scope, "bound_project")
        self.assertEqual(declaration.selectors, (OptionalExtraSelector("dev"),))
        self.assertNotIn(OptionalExtraSelector("mlx"), declaration.selectors)

    def test_selector_names_preserve_spelling_and_expose_normalized_identity(self) -> None:
        extra = OptionalExtraSelector("Dev_Test")
        group = DependencyGroupSelector("Docs.Build")

        self.assertEqual(extra.name, "Dev_Test")
        self.assertEqual(extra.normalized_name, "dev-test")
        self.assertEqual(group.name, "Docs.Build")
        self.assertEqual(group.normalized_name, "docs-build")

    def test_pip_local_project_preserves_multiple_explicit_extras(self) -> None:
        result = observe_project_environment_selection(
            _step('python -m pip install ".[dev,mlx]"'),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(
            result.declarations[0].selectors,
            (OptionalExtraSelector("dev"), OptionalExtraSelector("mlx")),
        )

    def test_pip_local_project_without_extra_is_still_visible_project_selection(self) -> None:
        result = observe_project_environment_selection(
            _step("pip install -e ."),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(result.declarations[0].selectors, ())

    def test_pip_local_project_uses_effective_working_directory(self) -> None:
        result = observe_project_environment_selection(
            _step('pip install -e ".[dev]"'),
            project_file_path="services/api/pyproject.toml",
            workflow_defaults=_defaults("services/api"),
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(result.working_directory.source, "workflow")
        self.assertEqual(result.declarations[0].project_root, "services/api")

    def test_dynamic_working_directory_makes_material_pip_path_unresolved(self) -> None:
        result = observe_project_environment_selection(
            _step(
                'pip install -e ".[dev]"',
                working_directory="${{ matrix.project }}",
            ),
            project_file_path="services/api/pyproject.toml",
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.working_directory.state, "unresolved")

    def test_dynamic_pip_extra_is_unresolved(self) -> None:
        result = observe_project_environment_selection(
            _step('pip install -e ".[${{ matrix.extra }}]"'),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.declarations, ())

    def test_echoed_pip_text_is_not_a_selection_declaration(self) -> None:
        result = observe_project_environment_selection(
            _step('echo "pip install -e .[dev]"'),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "not_observed")

    def test_s001_style_uv_group_all_packages_and_all_extras_are_preserved(self) -> None:
        result = observe_project_environment_selection(
            _step("uv sync --all-packages --group docs --all-extras"),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "observed")
        declaration = result.declarations[0]
        self.assertEqual(declaration.manager, "uv")
        self.assertEqual(declaration.operation, "sync")
        self.assertEqual(declaration.package_scope, "all_workspace_packages")
        self.assertIn(DependencyGroupSelector("docs"), declaration.selectors)
        self.assertIn(AllOptionalExtrasSelector(), declaration.selectors)

    def test_uv_without_all_packages_keeps_bound_project_scope(self) -> None:
        result = observe_project_environment_selection(
            _step("uv sync --group docs"),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(result.declarations[0].package_scope, "bound_project")

    def test_uv_run_all_packages_preserves_workspace_scope_before_child_command(self) -> None:
        result = observe_project_environment_selection(
            _step("uv run --all-packages --group docs pytest -q"),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(result.declarations[0].package_scope, "all_workspace_packages")
        self.assertEqual(
            result.declarations[0].selectors,
            (DependencyGroupSelector("docs"),),
        )

    def test_uv_only_group_preserves_only_mode_for_each_explicit_group(self) -> None:
        result = observe_project_environment_selection(
            _step("uv sync --only-group build --only-group docs"),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(result.declarations[0].package_scope, "bound_project")
        self.assertEqual(
            result.declarations[0].selectors,
            (
                DependencyGroupSelector("build", mode="only"),
                DependencyGroupSelector("docs", mode="only"),
            ),
        )

    def test_uv_all_groups_is_preserved_as_explicit_all_groups_selector(self) -> None:
        result = observe_project_environment_selection(
            _step("uv sync --all-groups"),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(
            result.declarations[0].selectors,
            (AllDependencyGroupsSelector(),),
        )

    def test_uv_run_extra_before_invoked_command_is_observed(self) -> None:
        result = observe_project_environment_selection(
            _step("uv run --extra mlx pytest -q"),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(
            result.declarations[0].selectors,
            (OptionalExtraSelector("mlx"),),
        )

    def test_uv_run_invoked_command_flags_are_not_uv_selectors(self) -> None:
        result = observe_project_environment_selection(
            _step("uv run pytest --group application-argument"),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.declarations[0].selectors, ())

    def test_uv_run_child_negative_flag_does_not_override_uv_extra(self) -> None:
        result = observe_project_environment_selection(
            _step("uv run --extra mlx pytest --no-group application-argument"),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(
            result.declarations[0].selectors,
            (OptionalExtraSelector("mlx"),),
        )

    def test_uv_without_explicit_selector_is_unresolved_not_negative(self) -> None:
        result = observe_project_environment_selection(
            _step("uv sync"),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(len(result.declarations), 1)
        self.assertEqual(result.declarations[0].selectors, ())
        self.assertIn("default-group", result.detail)

    def test_uv_dynamic_group_is_unresolved(self) -> None:
        result = observe_project_environment_selection(
            _step('uv sync --group "${{ matrix.group }}"'),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.declarations[0].selectors, ())

    def test_uv_package_targeting_remains_unresolved_scope(self) -> None:
        result = observe_project_environment_selection(
            _step("uv sync --package pydantic-core --group docs"),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "unresolved")
        self.assertIn("--package", result.detail)

    def test_uv_literal_project_path_can_bind_subproject(self) -> None:
        result = observe_project_environment_selection(
            _step("uv sync --project services/api --group docs"),
            project_file_path="services/api/pyproject.toml",
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(
            result.declarations[0].selectors,
            (DependencyGroupSelector("docs"),),
        )

    def test_uv_discovery_outside_exact_project_root_is_unresolved(self) -> None:
        result = observe_project_environment_selection(
            _step("uv sync --group docs", working_directory="services/api/tests"),
            project_file_path="services/api/pyproject.toml",
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.declarations, ())
        self.assertIn("project discovery", result.detail)

    def test_uv_negative_selector_keeps_positive_fact_but_overall_state_unresolved(self) -> None:
        result = observe_project_environment_selection(
            _step("uv sync --all-extras --no-extra mlx"),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(len(result.declarations), 1)
        self.assertIn(AllOptionalExtrasSelector(), result.declarations[0].selectors)
        self.assertIn("--no-extra", result.detail)

    def test_multiple_shell_segments_preserve_static_segment_indices(self) -> None:
        result = observe_project_environment_selection(
            _step("uv sync --group docs && pip install -e '.[dev]'"),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(
            tuple(declaration.segment_index for declaration in result.declarations),
            (0, 1),
        )

    def test_unrelated_expression_does_not_erase_literal_selection(self) -> None:
        result = observe_project_environment_selection(
            _step("uv sync --group docs && echo '${{ matrix.other }}'"),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(
            result.declarations[0].selectors,
            (DependencyGroupSelector("docs"),),
        )

    def test_malformed_quoting_in_candidate_command_is_unresolved(self) -> None:
        result = observe_project_environment_selection(
            _step('pip install -e ".[dev]'),
            project_file_path="pyproject.toml",
        )

        self.assertEqual(result.state, "unresolved")

    def test_invalid_project_file_path_is_rejected_at_boundary(self) -> None:
        for path in ("", "/pyproject.toml", "../pyproject.toml", "setup.cfg"):
            with self.subTest(path=path):
                with self.assertRaises(ValueError):
                    observe_project_environment_selection(
                        _step('pip install -e ".[dev]"'),
                        project_file_path=path,
                    )


if __name__ == "__main__":
    unittest.main()
