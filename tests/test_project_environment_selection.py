"""Test parsed static pip/uv project-environment selection without runtime claims."""

from __future__ import annotations

import unittest

from upgradepilot.dependency.environment_selection import (
    AllDependencyGroupsSelector,
    AllOptionalExtrasSelector,
    DependencyGroupSelector,
    OptionalExtraSelector,
    observe_project_environment_selection,
)
from upgradepilot.github.workflow_command_analysis import (
    CommandSourceSpan,
    StaticCommandAnalysis,
    StaticCommandAtom,
    StaticCommandOccurrence,
    StaticCommandProblem,
)
from upgradepilot.github.workflow_command_shell import EffectiveShellContext
from upgradepilot.github.workflow_definition import (
    RunDefaults,
    RunStepDefinition,
    SourceSpan,
    StaticScalarValue,
)

_SPAN = SourceSpan(start_line=1, start_column=1, end_line=1, end_column=2)
_SHELL_CONTEXT = EffectiveShellContext(
    state="resolved",
    source="step",
    syntax_family="bash",
    execution_profile="github_builtin_bash",
    raw_declaration="bash",
)


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


def _literal(value: str) -> StaticCommandAtom:
    return StaticCommandAtom(raw_source=value, literal_value=value, state="literal")


def _dynamic(raw_source: str) -> StaticCommandAtom:
    return StaticCommandAtom(raw_source=raw_source, literal_value=None, state="dynamic")


def _occurrence(
    source_order: int,
    executable: str,
    *arguments: str | StaticCommandAtom,
    structural_context: tuple[str, ...] = ("straightforward_top_level",),
) -> StaticCommandOccurrence:
    argument_atoms = tuple(
        argument if isinstance(argument, StaticCommandAtom) else _literal(argument)
        for argument in arguments
    )
    raw_source = " ".join(
        (executable, *(argument.raw_source for argument in argument_atoms))
    )
    start_byte = source_order * 100
    return StaticCommandOccurrence(
        source_order=source_order,
        source_span=CommandSourceSpan(
            start_byte=start_byte,
            end_byte=start_byte + len(raw_source.encode("utf-8")),
            start_line=source_order,
            start_column=0,
            end_line=source_order,
            end_column=len(raw_source.encode("utf-8")),
        ),
        raw_source=raw_source,
        executable=_literal(executable),
        arguments=argument_atoms,
        structural_context=structural_context,  # type: ignore[arg-type]
    )


def _analysis(*occurrences: StaticCommandOccurrence) -> StaticCommandAnalysis:
    return StaticCommandAnalysis(
        state="analyzable",
        shell_context=_SHELL_CONTEXT,
        command_occurrences=tuple(occurrences),
        problems=(),
    )


def _failed_analysis() -> StaticCommandAnalysis:
    return StaticCommandAnalysis(
        state="parse_error",
        shell_context=_SHELL_CONTEXT,
        command_occurrences=(),
        problems=(
            StaticCommandProblem(
                reason="material_shell_parse_error",
                detail="Synthetic parser failure for project-selection proof.",
            ),
        ),
    )


def _observe(
    command: str,
    analysis: StaticCommandAnalysis,
    *,
    project_file_path: str = "pyproject.toml",
    working_directory: str | None = None,
    workflow_defaults: RunDefaults | None = None,
):
    return observe_project_environment_selection(
        _step(command, working_directory=working_directory),
        project_file_path=project_file_path,
        command_analysis=analysis,
        workflow_defaults=workflow_defaults,
    )


class ProjectEnvironmentSelectionTests(unittest.TestCase):
    def test_s011_pip_editable_dev_selects_only_visible_dev_extra(self) -> None:
        result = _observe(
            'pip install -e ".[dev]"',
            _analysis(_occurrence(0, "pip", "install", "-e", ".[dev]")),
        )

        self.assertEqual(result.state, "observed")
        declaration = result.declarations[0]
        self.assertEqual(declaration.manager, "pip")
        self.assertEqual(declaration.operation, "install")
        self.assertIsNone(declaration.project_root)
        self.assertEqual(declaration.package_scope, "bound_project")
        self.assertEqual(declaration.selectors, (OptionalExtraSelector("dev"),))
        self.assertNotIn(OptionalExtraSelector("mlx"), declaration.selectors)
        self.assertIsNone(declaration.segment_index)
        self.assertIsNotNone(declaration.command_location)

    def test_selector_names_preserve_spelling_and_expose_normalized_identity(self) -> None:
        extra = OptionalExtraSelector("Dev_Test")
        group = DependencyGroupSelector("Docs.Build")

        self.assertEqual(extra.name, "Dev_Test")
        self.assertEqual(extra.normalized_name, "dev-test")
        self.assertEqual(group.name, "Docs.Build")
        self.assertEqual(group.normalized_name, "docs-build")

    def test_pip_local_project_preserves_multiple_explicit_extras(self) -> None:
        result = _observe(
            'python -m pip install ".[dev,mlx]"',
            _analysis(
                _occurrence(0, "python", "-m", "pip", "install", ".[dev,mlx]")
            ),
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(
            result.declarations[0].selectors,
            (OptionalExtraSelector("dev"), OptionalExtraSelector("mlx")),
        )

    def test_pip_local_project_without_extra_is_still_visible_project_selection(self) -> None:
        result = _observe(
            "pip install -e .",
            _analysis(_occurrence(0, "pip", "install", "-e", ".")),
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(result.declarations[0].selectors, ())

    def test_pip_local_project_uses_effective_working_directory(self) -> None:
        result = _observe(
            'pip install -e ".[dev]"',
            _analysis(_occurrence(0, "pip", "install", "-e", ".[dev]")),
            project_file_path="services/api/pyproject.toml",
            workflow_defaults=_defaults("services/api"),
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(result.working_directory.source, "workflow")
        self.assertEqual(result.declarations[0].project_root, "services/api")

    def test_dynamic_working_directory_makes_material_pip_path_unresolved(self) -> None:
        result = _observe(
            'pip install -e ".[dev]"',
            _analysis(_occurrence(0, "pip", "install", "-e", ".[dev]")),
            project_file_path="services/api/pyproject.toml",
            working_directory="${{ matrix.project }}",
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.working_directory.state, "unresolved")

    def test_dynamic_pip_extra_is_unresolved(self) -> None:
        result = _observe(
            'pip install -e ".[${{ matrix.extra }}]"',
            _analysis(
                _occurrence(
                    0,
                    "pip",
                    "install",
                    "-e",
                    _dynamic('.[${{ matrix.extra }}]'),
                )
            ),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.declarations, ())

    def test_echoed_pip_text_is_not_a_selection_declaration(self) -> None:
        result = _observe(
            'echo "pip install -e .[dev]"',
            _analysis(_occurrence(0, "echo", "pip install -e .[dev]")),
        )

        self.assertEqual(result.state, "not_observed")

    def test_s001_style_uv_group_all_packages_and_all_extras_are_preserved(self) -> None:
        result = _observe(
            "uv sync --all-packages --group docs --all-extras",
            _analysis(
                _occurrence(
                    0,
                    "uv",
                    "sync",
                    "--all-packages",
                    "--group",
                    "docs",
                    "--all-extras",
                )
            ),
        )

        self.assertEqual(result.state, "observed")
        declaration = result.declarations[0]
        self.assertEqual(declaration.manager, "uv")
        self.assertEqual(declaration.operation, "sync")
        self.assertEqual(declaration.package_scope, "all_workspace_packages")
        self.assertIn(DependencyGroupSelector("docs"), declaration.selectors)
        self.assertIn(AllOptionalExtrasSelector(), declaration.selectors)

    def test_uv_without_all_packages_keeps_bound_project_scope(self) -> None:
        result = _observe(
            "uv sync --group docs",
            _analysis(_occurrence(0, "uv", "sync", "--group", "docs")),
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(result.declarations[0].package_scope, "bound_project")

    def test_uv_run_all_packages_preserves_workspace_scope_before_child_command(self) -> None:
        result = _observe(
            "uv run --all-packages --group docs pytest -q",
            _analysis(
                _occurrence(
                    0,
                    "uv",
                    "run",
                    "--all-packages",
                    "--group",
                    "docs",
                    "pytest",
                    "-q",
                )
            ),
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(result.declarations[0].package_scope, "all_workspace_packages")
        self.assertEqual(
            result.declarations[0].selectors,
            (DependencyGroupSelector("docs"),),
        )

    def test_uv_only_group_preserves_only_mode_for_each_explicit_group(self) -> None:
        result = _observe(
            "uv sync --only-group build --only-group docs",
            _analysis(
                _occurrence(
                    0,
                    "uv",
                    "sync",
                    "--only-group",
                    "build",
                    "--only-group",
                    "docs",
                )
            ),
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(
            result.declarations[0].selectors,
            (
                DependencyGroupSelector("build", mode="only"),
                DependencyGroupSelector("docs", mode="only"),
            ),
        )

    def test_uv_all_groups_is_preserved_as_explicit_all_groups_selector(self) -> None:
        result = _observe(
            "uv sync --all-groups",
            _analysis(_occurrence(0, "uv", "sync", "--all-groups")),
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(
            result.declarations[0].selectors,
            (AllDependencyGroupsSelector(),),
        )

    def test_uv_run_extra_before_invoked_command_is_observed(self) -> None:
        result = _observe(
            "uv run --extra mlx pytest -q",
            _analysis(
                _occurrence(0, "uv", "run", "--extra", "mlx", "pytest", "-q")
            ),
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(
            result.declarations[0].selectors,
            (OptionalExtraSelector("mlx"),),
        )

    def test_uv_run_invoked_command_flags_are_not_uv_selectors(self) -> None:
        result = _observe(
            "uv run pytest --group application-argument",
            _analysis(
                _occurrence(
                    0,
                    "uv",
                    "run",
                    "pytest",
                    "--group",
                    "application-argument",
                )
            ),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.declarations[0].selectors, ())

    def test_uv_run_child_negative_flag_does_not_override_uv_extra(self) -> None:
        result = _observe(
            "uv run --extra mlx pytest --no-group application-argument",
            _analysis(
                _occurrence(
                    0,
                    "uv",
                    "run",
                    "--extra",
                    "mlx",
                    "pytest",
                    "--no-group",
                    "application-argument",
                )
            ),
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(
            result.declarations[0].selectors,
            (OptionalExtraSelector("mlx"),),
        )

    def test_uv_without_explicit_selector_is_unresolved_not_negative(self) -> None:
        result = _observe(
            "uv sync",
            _analysis(_occurrence(0, "uv", "sync")),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(len(result.declarations), 1)
        self.assertEqual(result.declarations[0].selectors, ())
        self.assertIn("default-group", result.detail)

    def test_uv_dynamic_group_is_unresolved(self) -> None:
        result = _observe(
            'uv sync --group "${{ matrix.group }}"',
            _analysis(
                _occurrence(
                    0,
                    "uv",
                    "sync",
                    "--group",
                    _dynamic("${{ matrix.group }}"),
                )
            ),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.declarations[0].selectors, ())

    def test_uv_package_targeting_remains_unresolved_scope(self) -> None:
        result = _observe(
            "uv sync --package pydantic-core --group docs",
            _analysis(
                _occurrence(
                    0,
                    "uv",
                    "sync",
                    "--package",
                    "pydantic-core",
                    "--group",
                    "docs",
                )
            ),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.declarations, ())
        self.assertIn("--package", result.detail)

    def test_uv_literal_project_path_can_bind_subproject(self) -> None:
        result = _observe(
            "uv sync --project services/api --group docs",
            _analysis(
                _occurrence(
                    0,
                    "uv",
                    "sync",
                    "--project",
                    "services/api",
                    "--group",
                    "docs",
                )
            ),
            project_file_path="services/api/pyproject.toml",
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(
            result.declarations[0].selectors,
            (DependencyGroupSelector("docs"),),
        )

    def test_uv_discovery_outside_exact_project_root_is_unresolved(self) -> None:
        result = _observe(
            "uv sync --group docs",
            _analysis(_occurrence(0, "uv", "sync", "--group", "docs")),
            project_file_path="services/api/pyproject.toml",
            working_directory="services/api/tests",
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.declarations, ())
        self.assertIn("project discovery", result.detail)

    def test_uv_negative_selector_keeps_positive_fact_but_overall_state_unresolved(self) -> None:
        result = _observe(
            "uv sync --all-extras --no-extra mlx",
            _analysis(
                _occurrence(
                    0,
                    "uv",
                    "sync",
                    "--all-extras",
                    "--no-extra",
                    "mlx",
                )
            ),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(len(result.declarations), 1)
        self.assertIn(AllOptionalExtrasSelector(), result.declarations[0].selectors)
        self.assertIn("--no-extra", result.detail)

    def test_multiple_parsed_occurrences_preserve_canonical_locations(self) -> None:
        result = _observe(
            "uv sync --group docs && pip install -e '.[dev]'",
            _analysis(
                _occurrence(
                    0,
                    "uv",
                    "sync",
                    "--group",
                    "docs",
                    structural_context=("short_circuit",),
                ),
                _occurrence(
                    1,
                    "pip",
                    "install",
                    "-e",
                    ".[dev]",
                    structural_context=("short_circuit",),
                ),
            ),
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(
            tuple(
                declaration.command_location.source_order
                for declaration in result.declarations
                if declaration.command_location is not None
            ),
            (0, 1),
        )
        self.assertEqual(
            tuple(declaration.segment_index for declaration in result.declarations),
            (None, None),
        )

    def test_unrelated_expression_does_not_erase_literal_selection(self) -> None:
        result = _observe(
            "uv sync --group docs && echo '${{ matrix.other }}'",
            _analysis(
                _occurrence(
                    0,
                    "uv",
                    "sync",
                    "--group",
                    "docs",
                    structural_context=("short_circuit",),
                ),
                _occurrence(
                    1,
                    "echo",
                    _dynamic("${{ matrix.other }}"),
                    structural_context=("short_circuit",),
                ),
            ),
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(
            result.declarations[0].selectors,
            (DependencyGroupSelector("docs"),),
        )

    def test_analysis_failure_is_unresolved_without_text_fallback(self) -> None:
        result = _observe(
            'pip install -e ".[dev]',
            _failed_analysis(),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "project_environment_command_analysis_unresolved")
        self.assertEqual(result.declarations, ())

    def test_invalid_project_file_path_is_rejected_at_boundary(self) -> None:
        analysis = _analysis(_occurrence(0, "pip", "install", "-e", ".[dev]"))
        for path in ("", "/pyproject.toml", "../pyproject.toml", "setup.cfg"):
            with self.subTest(path=path):
                with self.assertRaises(ValueError):
                    _observe(
                        'pip install -e ".[dev]"',
                        analysis,
                        project_file_path=path,
                    )


if __name__ == "__main__":
    unittest.main()
