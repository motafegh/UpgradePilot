from __future__ import annotations

import unittest

from upgradepilot.dependency.direct_install import observe_direct_installation_declaration
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


class DirectInstallDeclarationTests(unittest.TestCase):
    def test_observes_root_requirements_install(self) -> None:
        result = observe_direct_installation_declaration(
            _step("python -m pip install -r requirements.txt"),
            dependency_source_path="requirements.txt",
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(result.reason, "direct_requirements_install_declared")
        self.assertEqual(result.matched_requirement_path, "requirements.txt")
        self.assertEqual(result.matched_segment_index, 0)
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

        for step, job_defaults, workflow_defaults, source_path, expected_source in cases:
            with self.subTest(expected_source=expected_source):
                result = observe_direct_installation_declaration(
                    step,
                    dependency_source_path=source_path,
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
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "direct_install_path_context_unresolved")
        self.assertEqual(result.working_directory.state, "unresolved")
        self.assertEqual(result.working_directory.source, "step")

    def test_dynamic_requirement_path_is_unresolved(self) -> None:
        result = observe_direct_installation_declaration(
            _step('python -m pip install -r "${{ inputs.requirements }}"'),
            dependency_source_path="requirements.txt",
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "direct_install_path_context_unresolved")

    def test_visible_nonmatching_requirements_file_is_not_observed_for_target_source(self) -> None:
        result = observe_direct_installation_declaration(
            _step("pip install -r requirements-dev.txt"),
            dependency_source_path="requirements.txt",
        )

        self.assertEqual(result.state, "not_observed")
        self.assertEqual(result.reason, "dependency_source_not_directly_declared")

    def test_non_direct_pip_text_is_not_misclassified_as_install_declaration(self) -> None:
        result = observe_direct_installation_declaration(
            _step('echo "pip install -r requirements.txt"'),
            dependency_source_path="requirements.txt",
        )

        self.assertEqual(result.state, "not_observed")
        self.assertEqual(result.reason, "direct_requirements_install_not_observed")

    def test_direct_install_can_be_one_shell_segment_without_claiming_execution(self) -> None:
        result = observe_direct_installation_declaration(
            _step("python -m pip install -r requirements.txt && pytest -q"),
            dependency_source_path="requirements.txt",
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(result.matched_segment_index, 0)
        self.assertIn("static run step", result.detail)

    def test_matched_segment_index_preserves_static_command_order_only(self) -> None:
        result = observe_direct_installation_declaration(
            _step("echo prepare && pip install -r requirements.txt && pytest -q"),
            dependency_source_path="requirements.txt",
        )

        self.assertEqual(result.state, "observed")
        self.assertEqual(result.matched_segment_index, 1)

    def test_invalid_dependency_source_path_is_rejected_at_boundary(self) -> None:
        for path in ("", "/requirements.txt", "../requirements.txt", "a\\b.txt"):
            with self.subTest(path=path):
                with self.assertRaises(ValueError):
                    observe_direct_installation_declaration(
                        _step("pip install -r requirements.txt"),
                        dependency_source_path=path,
                    )


if __name__ == "__main__":
    unittest.main()
