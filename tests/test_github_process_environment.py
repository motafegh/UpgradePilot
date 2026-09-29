from __future__ import annotations

import unittest

from upgradepilot.github.process_environment import (
    observe_exact_process_environment_value,
)
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.workflow_command_analysis import analyze_run_step_commands
from upgradepilot.github.workflow_definition import (
    RunStepDefinition,
    StepsJobDefinition,
    WorkflowDefinition,
    parse_workflow_definition,
)


def _case(
    *,
    run: str,
    step_env: str | None = None,
    job_env: str | None = None,
    workflow_env: str | None = None,
) -> tuple[WorkflowDefinition, StepsJobDefinition, RunStepDefinition]:
    lines: list[str] = []
    if workflow_env is not None:
        lines.extend(["env:", f"  PIP_DRY_RUN: {workflow_env}"])
    lines.extend(["jobs:", "  test:", "    runs-on: ubuntu-latest"])
    if job_env is not None:
        lines.extend(["    env:", f"      PIP_DRY_RUN: {job_env}"])
    lines.append("    steps:")
    if step_env is not None:
        lines.extend(
            [
                "      - env:",
                f"          PIP_DRY_RUN: {step_env}",
                "        run: |",
            ]
        )
    else:
        lines.append("      - run: |")
    lines.extend(f"          {line}" for line in run.splitlines())
    lines.append("")

    source = RepositoryTextFile(
        repository="example/project",
        path=".github/workflows/ci.yml",
        revision="a" * 40,
        content="\n".join(lines),
    )
    workflow = parse_workflow_definition(source)
    assert isinstance(workflow, WorkflowDefinition)
    job = workflow.jobs[0]
    assert isinstance(job, StepsJobDefinition)
    step = job.steps[0]
    assert isinstance(step, RunStepDefinition)
    return workflow, job, step


def _observe(
    workflow: WorkflowDefinition,
    job: StepsJobDefinition,
    step: RunStepDefinition,
):
    analysis = analyze_run_step_commands(workflow, job, step)
    assert analysis.state == "analyzable"
    assert len(analysis.command_occurrences) == 1
    return observe_exact_process_environment_value(
        workflow,
        job,
        step,
        analysis.command_occurrences[0],
        "PIP_DRY_RUN",
    )


class ExactProcessEnvironmentValueTests(unittest.TestCase):
    def test_literal_command_local_assignment_establishes_exact_process_value(self) -> None:
        workflow, job, step = _case(
            run="PIP_DRY_RUN=1 pip install -r requirements.txt",
            step_env="0",
            job_env="0",
            workflow_env="0",
        )

        result = _observe(workflow, job, step)

        self.assertEqual(result.state, "established")
        self.assertEqual(result.value, "1")
        self.assertEqual(result.source, "command_local_assignment")

    def test_dynamic_command_local_assignment_blocks_inherited_literal_value(self) -> None:
        workflow, job, step = _case(
            run='PIP_DRY_RUN="$MODE" pip install -r requirements.txt',
            step_env="0",
        )

        result = _observe(workflow, job, step)

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            result.reason,
            "process_environment_command_local_value_unresolved",
        )

    def test_literal_step_declaration_is_not_promoted_past_unmodeled_shell_runtime_sources(
        self,
    ) -> None:
        workflow, job, step = _case(
            run="pip install -r requirements.txt",
            step_env="0",
        )

        result = _observe(workflow, job, step)

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.source, "workflow_declaration")
        self.assertEqual(
            result.reason,
            "process_environment_closer_runtime_sources_unmodeled",
        )

    def test_no_declaration_keeps_runner_ambient_state_unresolved(self) -> None:
        workflow, job, step = _case(
            run="pip install -r requirements.txt",
        )

        result = _observe(workflow, job, step)

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.source, "ambient_or_runtime")
        self.assertEqual(
            result.reason,
            "process_environment_ambient_sources_unresolved",
        )


if __name__ == "__main__":
    unittest.main()
