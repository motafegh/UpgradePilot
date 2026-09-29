from __future__ import annotations

import unittest

from upgradepilot.dependency.package_manager_config import (
    observe_pip_persistent_config_setting,
)
from upgradepilot.dependency.package_manager_operation import (
    PackageManagerOperationDeclaration,
    parse_package_manager_operation,
)
from upgradepilot.dependency.package_manager_semantics import (
    DirectRequirementHandlingFact,
    InstallationDestinationFact,
    ManagerEnvironmentSelectionFact,
    PackageMutationModeFact,
    resolve_direct_requirement_handling,
    resolve_installation_destination,
    resolve_manager_environment_selection,
    resolve_package_mutation_mode,
)
from upgradepilot.github.executable_selection import observe_command_executable_selection
from upgradepilot.github.process_environment import (
    ProcessEnvironmentValueEvidence,
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


def _fixture():
    source = RepositoryTextFile(
        repository="example/project",
        path=".github/workflows/ci.yml",
        revision="a" * 40,
        content="""jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: PIP_DRY_RUN=0 PIP_CONFIG_FILE=/dev/null PIP_TARGET= PIP_PREFIX= PIP_ROOT= PIP_ONLY_DEPS=0 PIP_ONLY_DEPENDENCIES=0 /opt/bootstrap/bin/python -m pip --python /opt/target/bin/python install --no-user --no-deps -r requirements.txt
""",
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
    return workflow, job, step, occurrence, declaration


def _process_environment(
    workflow: WorkflowDefinition,
    job: StepsJobDefinition,
    step: RunStepDefinition,
    occurrence,
    variable_name: str,
) -> ProcessEnvironmentValueEvidence:
    result = observe_exact_process_environment_value(
        workflow,
        job,
        step,
        occurrence,
        variable_name,
    )
    assert isinstance(result, ProcessEnvironmentValueEvidence)
    return result


class RouteASemanticFixtureTests(unittest.TestCase):
    def test_controlled_positive_fixture_closes_all_four_semantic_facts(self) -> None:
        workflow, job, step, occurrence, declaration = _fixture()

        executable = observe_command_executable_selection(occurrence)
        self.assertEqual(executable.state, "established")
        self.assertEqual(executable.kind, "explicit_path")
        self.assertEqual(executable.executable, "/opt/bootstrap/bin/python")

        dry_run_environment = _process_environment(
            workflow,
            job,
            step,
            occurrence,
            "PIP_DRY_RUN",
        )
        config_file_environment = _process_environment(
            workflow,
            job,
            step,
            occurrence,
            "PIP_CONFIG_FILE",
        )
        destination_environment = tuple(
            _process_environment(workflow, job, step, occurrence, variable_name)
            for variable_name in ("PIP_TARGET", "PIP_PREFIX", "PIP_ROOT")
        )
        direct_environment = tuple(
            _process_environment(workflow, job, step, occurrence, variable_name)
            for variable_name in ("PIP_ONLY_DEPS", "PIP_ONLY_DEPENDENCIES")
        )

        destination_config = observe_pip_persistent_config_setting(
            declaration,
            setting="installation-destination",
            config_file_environment=config_file_environment,
        )
        mutation_config = observe_pip_persistent_config_setting(
            declaration,
            setting="dry-run",
            config_file_environment=config_file_environment,
        )
        direct_config = observe_pip_persistent_config_setting(
            declaration,
            setting="only-deps",
            config_file_environment=config_file_environment,
        )

        manager = resolve_manager_environment_selection(declaration)
        destination = resolve_installation_destination(
            declaration,
            process_environment=destination_environment,
            persistent_configuration=destination_config,
        )
        mutation = resolve_package_mutation_mode(
            declaration,
            process_environment=dry_run_environment,
            persistent_configuration=mutation_config,
        )
        direct = resolve_direct_requirement_handling(
            declaration,
            process_environment=direct_environment,
            persistent_configuration=direct_config,
        )

        self.assertIsInstance(manager, ManagerEnvironmentSelectionFact)
        self.assertIsInstance(destination, InstallationDestinationFact)
        self.assertIsInstance(mutation, PackageMutationModeFact)
        self.assertIsInstance(direct, DirectRequirementHandlingFact)
        assert isinstance(manager, ManagerEnvironmentSelectionFact)
        assert isinstance(destination, InstallationDestinationFact)
        assert isinstance(mutation, PackageMutationModeFact)
        assert isinstance(direct, DirectRequirementHandlingFact)

        self.assertEqual(manager.environment.value, "/opt/target/bin/python")
        self.assertEqual(destination.destination.kind, "manager_environment_scheme")
        self.assertEqual(mutation.mode, "apply_changes")
        self.assertEqual(direct.handling, "handled")
        self.assertEqual(
            {
                manager.command_location,
                destination.command_location,
                mutation.command_location,
                direct.command_location,
            },
            {declaration.command_location},
        )

    def test_ordinary_looking_fixture_without_closure_evidence_remains_unresolved(self) -> None:
        source = RepositoryTextFile(
            repository="example/project",
            path=".github/workflows/ci.yml",
            revision="b" * 40,
            content="""jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: python -m pip install -r requirements.txt
""",
        )
        workflow = parse_workflow_definition(source)
        assert isinstance(workflow, WorkflowDefinition)
        job = workflow.jobs[0]
        assert isinstance(job, StepsJobDefinition)
        step = job.steps[0]
        assert isinstance(step, RunStepDefinition)
        analysis = analyze_run_step_commands(workflow, job, step)
        assert analysis.state == "analyzable"
        occurrence = analysis.command_occurrences[0]
        declaration = parse_package_manager_operation(occurrence)
        assert isinstance(declaration, PackageManagerOperationDeclaration)

        manager = resolve_manager_environment_selection(declaration)
        destination = resolve_installation_destination(declaration)
        mutation = resolve_package_mutation_mode(declaration)
        direct = resolve_direct_requirement_handling(declaration)

        self.assertEqual(manager.blocking_source, "process_environment")
        self.assertEqual(destination.blocking_source, "process_environment")
        self.assertEqual(mutation.blocking_source, "process_environment")
        self.assertEqual(direct.blocking_source, "process_environment")


if __name__ == "__main__":
    unittest.main()
