from __future__ import annotations

import unittest

from upgradepilot.dependency.direct_install import observe_direct_installation_declaration
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
        source_index=3,
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
                detail="Synthetic parser failure for dependency-observer proof.",
            ),
        ),
    )


class DirectInstallDeclarationTests(unittest.TestCase):
    def test_observes_root_requirements_install(self) -> None:
        result = observe_direct_installation_declaration(
            _step("python -m pip install -r requirements.txt"),
            dependency_source_path="requirements.txt",
            command_analysis=_analysis(
                _occurrence(0, "python", "-m", "pip", "install", "-r", "requirements.txt")
            ),
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(result.reason, "direct_requirements_install_declared")
        self.assertEqual(result.matched_requirement_path, "requirements.txt")
        self.assertIsNotNone(result.command_location)
        assert result.command_location is not None
        self.assertEqual(result.command_location.source_order, 0)
        self.assertEqual(result.working_directory.state, "repository_root")
        self.assertEqual(result.working_directory.source, "repository_root")

    def test_working_directory_precedence_is_step_then_job_then_workflow(self) -> None:
        cases = (
            (
                _step(
                    "pip install -r requirements.txt",
                    working_directory="step-dir",
                ),
                _defaults("job-dir"),
                _defaults("workflow-dir"),
                "step-dir/requirements.txt",
                "step",
            ),
            (
                _step("pip install -r requirements.txt"),
                _defaults("job-dir"),
                _defaults("workflow-dir"),
                "job-dir/requirements.txt",
                "job",
            ),
            (
                _step("pip install -r requirements.txt"),
                None,
                _defaults("workflow-dir"),
                "workflow-dir/requirements.txt",
                "workflow",
            ),
        )
        analysis = _analysis(
            _occurrence(0, "pip", "install", "-r", "requirements.txt")
        )

        for step, job_defaults, workflow_defaults, source_path, expected_source in cases:
            with self.subTest(expected_source=expected_source):
                result = observe_direct_installation_declaration(
                    step,
                    dependency_source_path=source_path,
                    command_analysis=analysis,
                    job_defaults=job_defaults,
                    workflow_defaults=workflow_defaults,
                )
                self.assertEqual(result.state, "observed")
                self.assertEqual(result.working_directory.source, expected_source)

    def test_parent_requirement_path_can_resolve_safely_to_repository_source(self) -> None:
        result = observe_direct_installation_declaration(
            _step(
                "pip install --upgrade --requirement ../requirements.txt",
                working_directory="backend",
            ),
            dependency_source_path="requirements.txt",
            command_analysis=_analysis(
                _occurrence(
                    0,
                    "pip",
                    "install",
                    "--upgrade",
                    "--requirement",
                    "../requirements.txt",
                )
            ),
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(result.matched_requirement_path, "../requirements.txt")
        self.assertEqual(result.working_directory.path, "backend")

    def test_dynamic_effective_working_directory_is_unresolved(self) -> None:
        result = observe_direct_installation_declaration(
            _step(
                "pip install -r requirements.txt",
                working_directory="${{ matrix.project }}",
            ),
            dependency_source_path="services/api/requirements.txt",
            command_analysis=_analysis(
                _occurrence(0, "pip", "install", "-r", "requirements.txt")
            ),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "direct_install_path_context_unresolved")
        self.assertEqual(result.working_directory.state, "unresolved")
        self.assertEqual(result.working_directory.source, "step")
        self.assertIsNotNone(result.command_location)

    def test_dynamic_requirement_path_is_unresolved(self) -> None:
        result = observe_direct_installation_declaration(
            _step('python -m pip install -r "${{ inputs.requirements }}"'),
            dependency_source_path="requirements.txt",
            command_analysis=_analysis(
                _occurrence(
                    0,
                    "python",
                    "-m",
                    "pip",
                    "install",
                    "-r",
                    _dynamic('"${{ inputs.requirements }}"'),
                )
            ),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "direct_install_path_context_unresolved")
        self.assertIsNotNone(result.command_location)

    def test_visible_nonmatching_requirements_file_is_not_observed_for_target_source(self) -> None:
        result = observe_direct_installation_declaration(
            _step("pip install -r requirements-dev.txt"),
            dependency_source_path="requirements.txt",
            command_analysis=_analysis(
                _occurrence(0, "pip", "install", "-r", "requirements-dev.txt")
            ),
        )

        self.assertEqual(result.state, "not_observed")
        self.assertEqual(result.reason, "dependency_source_not_directly_declared")

    def test_non_direct_pip_text_is_not_misclassified_as_install_declaration(self) -> None:
        result = observe_direct_installation_declaration(
            _step('echo "pip install -r requirements.txt"'),
            dependency_source_path="requirements.txt",
            command_analysis=_analysis(
                _occurrence(0, "echo", "pip install -r requirements.txt")
            ),
        )

        self.assertEqual(result.state, "not_observed")
        self.assertEqual(result.reason, "direct_requirements_install_not_observed")

    def test_direct_install_static_presence_survives_short_circuit_context(self) -> None:
        result = observe_direct_installation_declaration(
            _step("python -m pip install -r requirements.txt && pytest -q"),
            dependency_source_path="requirements.txt",
            command_analysis=_analysis(
                _occurrence(
                    0,
                    "python",
                    "-m",
                    "pip",
                    "install",
                    "-r",
                    "requirements.txt",
                    structural_context=("short_circuit",),
                ),
                _occurrence(
                    1,
                    "pytest",
                    "-q",
                    structural_context=("short_circuit",),
                ),
            ),
        )

        self.assertEqual(result.state, "observed")
        self.assertIsNotNone(result.command_location)
        self.assertIn("static run step", result.detail)

    def test_command_location_preserves_static_occurrence_identity(self) -> None:
        result = observe_direct_installation_declaration(
            _step("echo prepare && pip install -r requirements.txt && pytest -q"),
            dependency_source_path="requirements.txt",
            command_analysis=_analysis(
                _occurrence(
                    0,
                    "echo",
                    "prepare",
                    structural_context=("short_circuit",),
                ),
                _occurrence(
                    1,
                    "pip",
                    "install",
                    "-r",
                    "requirements.txt",
                    structural_context=("short_circuit",),
                ),
                _occurrence(
                    2,
                    "pytest",
                    "-q",
                    structural_context=("short_circuit",),
                ),
            ),
        )

        self.assertEqual(result.state, "observed")
        self.assertIsNotNone(result.command_location)
        assert result.command_location is not None
        self.assertEqual(result.command_location.source_order, 1)

    def test_positive_requirement_path_survives_unrelated_dynamic_argument(self) -> None:
        result = observe_direct_installation_declaration(
            _step("pip install ${{ matrix.extra_arg }} -r requirements.txt"),
            dependency_source_path="requirements.txt",
            command_analysis=_analysis(
                _occurrence(
                    0,
                    "pip",
                    "install",
                    _dynamic("${{ matrix.extra_arg }}"),
                    "-r",
                    "requirements.txt",
                )
            ),
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(result.matched_requirement_path, "requirements.txt")

    def test_analysis_failure_is_unresolved_without_text_fallback(self) -> None:
        result = observe_direct_installation_declaration(
            _step("pip install -r requirements.txt"),
            dependency_source_path="requirements.txt",
            command_analysis=_failed_analysis(),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "direct_install_command_analysis_unresolved")
        self.assertIsNone(result.command_location)

    def test_invalid_dependency_source_path_is_rejected_at_boundary(self) -> None:
        analysis = _analysis(
            _occurrence(0, "pip", "install", "-r", "requirements.txt")
        )
        for path in ("", "/requirements.txt", "../requirements.txt", "a\\b.txt"):
            with self.subTest(path=path):
                with self.assertRaises(ValueError):
                    observe_direct_installation_declaration(
                        _step("pip install -r requirements.txt"),
                        dependency_source_path=path,
                        command_analysis=analysis,
                    )


if __name__ == "__main__":
    unittest.main()
