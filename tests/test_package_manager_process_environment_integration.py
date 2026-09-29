from __future__ import annotations

import unittest

from upgradepilot.dependency.package_manager_operation import (
    PackageManagerOperationDeclaration,
    parse_package_manager_operation,
)
from upgradepilot.dependency.package_manager_semantics import (
    PackageManagerSemanticProblem,
    PackageMutationModeFact,
    resolve_package_mutation_mode,
)
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


def _resolve_mutation(
    *,
    run: str,
    step_env: str | None = None,
):
    lines = ["jobs:", "  test:", "    runs-on: ubuntu-latest", "    steps:"]
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

    analysis = analyze_run_step_commands(workflow, job, step)
    assert analysis.state == "analyzable"
    assert len(analysis.command_occurrences) == 1
    occurrence = analysis.command_occurrences[0]

    declaration = parse_package_manager_operation(occurrence)
    assert isinstance(declaration, PackageManagerOperationDeclaration)
    process_environment = observe_exact_process_environment_value(
        workflow,
        job,
        step,
        occurrence,
        "PIP_DRY_RUN",
    )
    return resolve_package_mutation_mode(
        declaration,
        process_environment=process_environment,
    )


class PackageManagerProcessEnvironmentIntegrationTests(unittest.TestCase):
    def test_command_local_enabled_dry_run_becomes_semantic_fact(self) -> None:
        result = _resolve_mutation(
            run="PIP_DRY_RUN=1 pip install -r requirements.txt",
        )

        self.assertIsInstance(result, PackageMutationModeFact)
        assert isinstance(result, PackageMutationModeFact)
        self.assertEqual(result.mode, "dry_run")
        self.assertEqual(result.provenance.winning_source, "process_environment")

    def test_command_local_disabled_dry_run_moves_to_config_not_default(self) -> None:
        result = _resolve_mutation(
            run="PIP_DRY_RUN=0 pip install -r requirements.txt",
        )

        self.assertIsInstance(result, PackageManagerSemanticProblem)
        assert isinstance(result, PackageManagerSemanticProblem)
        self.assertEqual(
            result.reason,
            "package_mutation_mode_needs_persistent_config_evidence",
        )
        self.assertEqual(result.blocking_source, "persistent_configuration")

    def test_step_env_alone_is_not_yet_promoted_to_exact_process_truth(self) -> None:
        result = _resolve_mutation(
            run="pip install -r requirements.txt",
            step_env="1",
        )

        self.assertIsInstance(result, PackageManagerSemanticProblem)
        assert isinstance(result, PackageManagerSemanticProblem)
        self.assertEqual(result.reason, "process_environment_value_unresolved")
        self.assertEqual(result.blocking_source, "process_environment")


if __name__ == "__main__":
    unittest.main()
