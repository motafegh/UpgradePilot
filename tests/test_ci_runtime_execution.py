from __future__ import annotations

from dataclasses import replace
from textwrap import indent
import unittest

from upgradepilot.ci.dependency_exercise import (
    WorkflowDependencyCoverageInput,
    evaluate_dependency_ci_coverage,
)
from upgradepilot.ci.dependency_state import evaluate_runtime_dependency_state
from upgradepilot.ci.runtime_execution import (
    assess_correlated_step_execution,
    assess_exact_command_execution,
)
from upgradepilot.ci.runtime_strengthening import (
    RuntimeStrengtheningCandidate,
    candidate_from_consumption,
)
from upgradepilot.ci.workflow_commands import inspect_workflow_dependency_evidence
from upgradepilot.ci.workflow_runtime_correlation import correlate_workflow_runtime
from upgradepilot.github.actions import WorkflowJob, WorkflowRun, WorkflowStep
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.workflow_command_analysis import CommandSourceSpan
from upgradepilot.github.workflow_command_location import StaticCommandLocation
from upgradepilot.workspace.native_projection import reconstruct_ci_projection

from test_ci_matrix_identity import _capture, _dependency_and_source


_REPOSITORY = "example/project"
_REVISION = "a" * 40
_PATH = ".github/workflows/ci.yml"


def _source(content: str) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository=_REPOSITORY,
        path=_PATH,
        revision=_REVISION,
        content=content.lstrip(),
    )


def _run() -> WorkflowRun:
    return WorkflowRun(
        run_id=1001,
        workflow_id=2001,
        name="CI",
        event="pull_request",
        head_sha=_REVISION,
        status="completed",
        conclusion="success",
        run_attempt=1,
    )


def _step(
    number: int,
    name: str,
    *,
    status: str = "completed",
    conclusion: str | None = "success",
) -> WorkflowStep:
    return WorkflowStep(
        number=number,
        name=name,
        status=status,
        conclusion=conclusion,
    )


def _job(steps: tuple[WorkflowStep, ...]) -> WorkflowJob:
    return WorkflowJob(
        job_id=3001,
        run_id=1001,
        name="Tests",
        head_sha=_REVISION,
        status="completed",
        conclusion="success",
        steps=steps,
    )


def _location(source_order: int = 0) -> StaticCommandLocation:
    return StaticCommandLocation(
        source_span=CommandSourceSpan(
            start_byte=0,
            end_byte=10,
            start_line=0,
            start_column=0,
            end_line=0,
            end_column=10,
        ),
        source_order=source_order,
    )


def _candidate(
    *,
    step_source_index: int = 0,
    structural_context: tuple[str, ...] = ("straightforward_top_level",),
    whole_step_relation: str | None = "sole_ordinary_top_level_command",
) -> RuntimeStrengtheningCandidate:
    return RuntimeStrengtheningCandidate(
        proposition_kind="dependency_consumption",
        workflow_path=_PATH,
        workflow_revision=_REVISION,
        job_key="test",
        step_source_index=step_source_index,
        command_location=_location(),
        structural_context=structural_context,  # type: ignore[arg-type]
        whole_step_relation=whole_step_relation,  # type: ignore[arg-type]
        execution_profile="github_builtin_bash",
    )


class CorrelatedStepExecutionTests(unittest.TestCase):
    def test_run_and_uses_steps_share_unmasked_success_interpretation(self) -> None:
        correlation = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/setup-python@v6
      - run: python -m unittest
"""
            ),
            _run(),
            (
                _job(
                    (
                        _step(1, "Run actions/setup-python@v6"),
                        _step(2, "Run python -m unittest"),
                    )
                ),
            ),
        )

        self.assertEqual(correlation.state, "correlated")
        self.assertEqual(
            [assess_correlated_step_execution(item).state for item in correlation.jobs[0].steps],
            ["supported", "supported"],
        )

    def test_continue_on_error_prevents_positive_step_interpretation(self) -> None:
        correlation = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Allowed failure
        continue-on-error: true
        run: python -m unittest
"""
            ),
            _run(),
            (_job((_step(1, "Allowed failure"),)),),
        )

        assessment = assess_correlated_step_execution(correlation.jobs[0].steps[0])

        self.assertEqual(assessment.state, "unresolved")
        self.assertEqual(assessment.basis, "continue_on_error_unresolved")

    def test_failed_runtime_step_is_factual_not_established(self) -> None:
        correlation = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Run tests
        run: python -m unittest
"""
            ),
            _run(),
            (_job((_step(1, "Run tests", conclusion="failure"),)),),
        )

        assessment = assess_correlated_step_execution(correlation.jobs[0].steps[0])

        self.assertEqual(assessment.state, "not_established")
        self.assertEqual(assessment.basis, "runtime_non_success")
        self.assertEqual(assessment.correlation.runtime_step.conclusion, "failure")


class ExactCommandExecutionTests(unittest.TestCase):
    def test_ordinary_startup_correction_round_trips_without_matrix_scope(self) -> None:
        source = _source("""jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install
        env:
          BASH_ENV: startup.sh
        run: pip install -r requirements.txt
""")
        dependency, context = _dependency_and_source(source, "requirements.txt", "soupsieve")
        workflow = WorkflowDependencyCoverageInput(
            _run(), (_job((_step(1, "Run actions/checkout@v4"), _step(2, "Install"))),), source,
        )
        coverage = evaluate_dependency_ci_coverage(dependency, (workflow,), source_contexts=(context,))
        runtime = evaluate_runtime_dependency_state(
            dependency, (workflow,), coverage, source_contexts=(context,),
        )
        assessment, = runtime.assessments
        self.assertEqual(assessment.consumption.whole_step_relation, "sole_ordinary_top_level_command")
        self.assertEqual(assessment.execution.reason, "runtime_strengthening_shell_startup_unresolved")
        saved = _capture(workflow, dependency, context, coverage, runtime)
        versions = {record.family: record.codec_version for record in saved.records}
        self.assertEqual((versions["ci_inputs"], versions["ci_coverage"],
                          versions["runtime_dependency_state"]), (1, 6, 3))
        restored = reconstruct_ci_projection(saved, expected_target=saved.target)
        self.assertEqual(restored.ci_coverage_result, coverage)
        self.assertEqual(restored.runtime_dependency_state_result, runtime)

    def test_declared_startup_defeats_sole_first_and_later_success(self) -> None:
        target = "pip install -r requirements.txt"
        for script, relation in (
            (target, "sole_ordinary_top_level_command"),
            (f"{target}\ntrue", "first_ordinary_top_level_command_in_sequential_script"),
            (f"true\n{target}", "later_ordinary_command_in_straight_line_script"),
        ):
            for declaration, detail in (
                ("env:\n  BASH_ENV: startup.sh\n", "workflow-level env: BASH_ENV"),
                ("env:\n  BASH_ENV: ${{ inputs.startup }}\n", "(environment_variable_value_dynamic)"),
                ("env:\n  BASH_FUNC_pip%%: '() { true; }'\n", "exported Bash function"),
                ("env:\n  SHELLOPTS: noexec\n", "workflow-level env: SHELLOPTS"),
                ("", None),
            ):
                with self.subTest(relation=relation, declaration=declaration):
                    source = _source(declaration + """jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install
        shell: bash
        run: |
""" + indent(script, "          ") + "\n")
                    candidate, correlation = self._parsed_install(source)
                    self.assertEqual(candidate.whole_step_relation, relation)
                    assessment = assess_exact_command_execution(candidate, correlation=correlation)
                    if detail is None:
                        self.assertEqual(assessment.state, "supported")
                    else:
                        self.assertEqual(assessment.state, "unresolved")
                        self.assertEqual(assessment.reason, "runtime_strengthening_shell_startup_unresolved")
                        self.assertIn(detail, assessment.detail)

    def test_later_command_needs_admitted_profile_and_unmasked_success(self) -> None:
        for shell, masking, conclusion, state, basis in (
            ("bash", "", "success", "supported", "supported"),
            ("sh", "", "success", "supported", "supported"),
            ("bash", "continue-on-error: false", "success", "supported", "supported"),
            ("bash {0}", "", "success", "unresolved", "eligibility_unresolved"),
            ("bash", "continue-on-error: true", "success", "unresolved", "continue_on_error_unresolved"),
            ("bash", "continue-on-error: ${{ inputs.mask }}", "success", "unresolved", "continue_on_error_unresolved"),
            ("bash", "", "failure", "not_established", "runtime_non_success"),
            ("bash", "", "skipped", "not_established", "runtime_non_success"),
        ):
            with self.subTest(shell=shell, masking=masking, conclusion=conclusion):
                source = _source(f"""jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install
        shell: {shell}
        {masking}
        run: |
          true
          pip install -r requirements.txt
""")
                candidate, correlation = self._parsed_install(source, conclusion=conclusion)
                self.assertEqual(candidate.whole_step_relation, "later_ordinary_command_in_straight_line_script")
                result = assess_exact_command_execution(candidate, correlation=correlation)
                self.assertEqual((result.state, result.basis), (state, basis))
                if state == "supported":
                    different_script = replace(candidate, command="true\npip freeze\n")
                    mismatch = assess_exact_command_execution(different_script, correlation=correlation)
                    self.assertEqual(mismatch.reason, "later_command_script_mismatch")

    @staticmethod
    def _parsed_install(source, *, conclusion="success"):
        _, context = _dependency_and_source(source, "requirements.txt", "soupsieve")
        static = inspect_workflow_dependency_evidence(
            source, source_contexts=(context,), package="soupsieve", normalized_package="soupsieve",
        )
        consumption, = static.consumptions
        correlation = correlate_workflow_runtime(
            source, _run(), (_job((
                _step(1, "Run actions/checkout@v4"),
                _step(2, "Install", conclusion=conclusion),
            )),),
        )
        return candidate_from_consumption(consumption), correlation

    def test_sole_eligible_command_in_successful_step_is_supported(self) -> None:
        correlation = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Install
        run: pip install -r requirements.txt
"""
            ),
            _run(),
            (_job((_step(1, "Install"),)),),
        )

        assessment = assess_exact_command_execution(
            _candidate(),
            correlation=correlation,
        )

        self.assertEqual(assessment.state, "supported")
        self.assertEqual(assessment.basis, "supported")
        self.assertEqual(assessment.runtime_step_number, 1)

    def test_ineligible_command_does_not_inherit_successful_step(self) -> None:
        correlation = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Conditional install
        run: |
          if false; then
            pip install -r requirements.txt
          fi
"""
            ),
            _run(),
            (_job((_step(1, "Conditional install"),)),),
        )

        assessment = assess_exact_command_execution(
            _candidate(
                structural_context=("conditional",),
                whole_step_relation=None,
            ),
            correlation=correlation,
        )

        self.assertEqual(assessment.state, "not_established")
        self.assertEqual(assessment.basis, "eligibility_ineligible")

    def test_unresolved_later_command_remains_unresolved_after_step_success(self) -> None:
        for before in ("exit 0", "exec true", "set +e", "trap 'exit 0' ERR", "true | cat"):
            with self.subTest(before=before):
                source = _source(f"""
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install
        run: |
          {before}
          pip install -r requirements.txt
          true
""")
                candidate, correlation = self._parsed_install(source)
                step = correlation.jobs[0].steps[1]
                self.assertEqual(assess_correlated_step_execution(step).state, "supported")
                assessment = assess_exact_command_execution(candidate, correlation=correlation)
                self.assertEqual(assessment.state, "unresolved")
                self.assertEqual(assessment.basis, "eligibility_unresolved")


if __name__ == "__main__":
    unittest.main()
