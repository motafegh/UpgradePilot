from __future__ import annotations

import unittest

from upgradepilot.ci.consumption import StaticDependencyConsumptionEvidence
from upgradepilot.ci.dependency_state import (
    ExactCICommandIdentity,
    RequirementSatisfiedAtCommandCompletion,
    RequirementStateProblem,
    compose_requirement_satisfied_at_command_completion,
    scope_package_manager_semantics,
)
from upgradepilot.ci.runtime_execution import (
    ExactCommandExecutionAssessment,
    assess_exact_command_execution,
)
from upgradepilot.ci.runtime_strengthening import candidate_from_consumption
from upgradepilot.ci.workflow_commands import inspect_workflow_dependency_evidence
from upgradepilot.ci.workflow_runtime_correlation import correlate_workflow_runtime
from upgradepilot.dependency.change import (
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.dependency.environment import RequirementsFileDependencyContext
from upgradepilot.dependency.package_manager_config import (
    observe_pip_persistent_config_setting,
)
from upgradepilot.dependency.package_manager_operation import (
    PackageManagerOperationDeclaration,
    parse_package_manager_operation,
)
from upgradepilot.dependency.package_manager_semantics import (
    DirectRequirementHandlingFact,
    InstallationDestination,
    InstallationDestinationFact,
    ManagerEnvironmentSelectionFact,
    PackageManagerEnvironmentReference,
    PackageManagerSemanticProblem,
    PackageManagerSemanticResolutionProvenance,
    PackageManagerSemanticResolutionStep,
    PackageMutationModeFact,
)
from upgradepilot.github.actions import WorkflowJob, WorkflowRun, WorkflowStep
from upgradepilot.github.process_environment import (
    ProcessEnvironmentValueEvidence,
    observe_exact_process_environment_value,
)
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.workflow_command_analysis import (
    CommandSourceSpan,
    analyze_run_step_commands,
)
from upgradepilot.github.workflow_command_location import StaticCommandLocation
from upgradepilot.github.workflow_definition import (
    RunStepDefinition,
    StepsJobDefinition,
    WorkflowDefinition,
    parse_workflow_definition,
)


_REVISION = "a" * 40
_WORKFLOW = ".github/workflows/ci.yml"
_SOURCE_PATH = "requirements.txt"


def _location(source_order: int = 0) -> StaticCommandLocation:
    return StaticCommandLocation(
        source_span=CommandSourceSpan(
            start_byte=10,
            end_byte=40,
            start_line=2,
            start_column=0,
            end_line=2,
            end_column=30,
        ),
        source_order=source_order,
    )


def _source_evidence(path: str = _SOURCE_PATH) -> DependencyChangeSourceEvidence:
    return DependencyChangeSourceEvidence(
        path=path,
        file_format="exact_requirement",
        extraction_method="exact_base_head_files",
    )


def _dependency(
    source_evidence: DependencyChangeSourceEvidence | None = None,
) -> DependencyVersionChange:
    source = source_evidence or _source_evidence()
    return DependencyVersionChange(
        package="requests",
        normalized_package="requests",
        old_version="2.32.4",
        proposed_version="2.33.0",
        source_evidence=(source,),
    )


def _source_context(
    source_evidence: DependencyChangeSourceEvidence | None = None,
) -> RequirementsFileDependencyContext:
    source = source_evidence or _source_evidence()
    return RequirementsFileDependencyContext(
        repository="example/project",
        revision=_REVISION,
        normalized_package="requests",
        source_evidence=source,
    )


def _consumption(
    *,
    workflow_path: str = _WORKFLOW,
    job_key: str = "test",
    step_source_index: int = 1,
    command_location: StaticCommandLocation | None = None,
) -> StaticDependencyConsumptionEvidence:
    return StaticDependencyConsumptionEvidence(
        state="supported",
        mechanism="direct_requirements",
        normalized_package="requests",
        workflow_path=workflow_path,
        workflow_revision=_REVISION,
        job_key=job_key,
        step_source_index=step_source_index,
        command="python -m pip install -r requirements.txt",
        reason="direct_requirements_consumption_declared",
        detail="The exact requirements source is directly consumed.",
        source_path=_SOURCE_PATH,
        command_location=command_location or _location(),
        structural_context=("straightforward_top_level",),
        whole_step_relation="sole_ordinary_top_level_command",
        execution_profile="github_builtin_bash",
    )


def _identity(
    consumption: StaticDependencyConsumptionEvidence,
) -> ExactCICommandIdentity:
    assert consumption.command_location is not None
    return ExactCICommandIdentity(
        workflow_path=consumption.workflow_path,
        workflow_revision=consumption.workflow_revision,
        job_key=consumption.job_key,
        step_source_index=consumption.step_source_index,
        command_location=consumption.command_location,
    )


def _provenance(dimension: str) -> PackageManagerSemanticResolutionProvenance:
    return PackageManagerSemanticResolutionProvenance(
        dimension=dimension,  # type: ignore[arg-type]
        inspected_sources=(
            PackageManagerSemanticResolutionStep(
                source_kind="command_line",
                disposition="decisive",
                detail="Focused composer fixture.",
            ),
        ),
        winning_source="command_line",
    )


def _manager(
    location: StaticCommandLocation,
    *,
    environment: str = "/opt/venv/bin/python",
) -> ManagerEnvironmentSelectionFact:
    return ManagerEnvironmentSelectionFact(
        manager="pip",
        command_location=location,
        environment=PackageManagerEnvironmentReference(
            kind="pip_python_target",
            value=environment,
        ),
        provenance=_provenance("manager_environment"),
    )


def _destination(
    location: StaticCommandLocation,
    *,
    kind: str = "manager_environment_scheme",
    value: str | None = None,
) -> InstallationDestinationFact:
    return InstallationDestinationFact(
        manager="pip",
        command_location=location,
        destination=InstallationDestination(
            kind=kind,  # type: ignore[arg-type]
            value=value,
        ),
        provenance=_provenance("installation_destination"),
    )


def _mutation(
    location: StaticCommandLocation,
    *,
    mode: str = "apply_changes",
) -> PackageMutationModeFact:
    return PackageMutationModeFact(
        manager="pip",
        command_location=location,
        mode=mode,  # type: ignore[arg-type]
        provenance=_provenance("package_mutation_mode"),
    )


def _direct(
    location: StaticCommandLocation,
    *,
    handling: str = "handled",
) -> DirectRequirementHandlingFact:
    return DirectRequirementHandlingFact(
        manager="pip",
        command_location=location,
        handling=handling,  # type: ignore[arg-type]
        provenance=_provenance("direct_requirement_handling"),
    )


def _semantics(
    consumption: StaticDependencyConsumptionEvidence,
    *,
    manager_environment: str = "/opt/venv/bin/python",
    destination_kind: str = "manager_environment_scheme",
    destination_value: str | None = None,
    mutation_mode: str = "apply_changes",
    direct_handling: str = "handled",
    mutation_problem: PackageManagerSemanticProblem | None = None,
):
    assert consumption.command_location is not None
    location = consumption.command_location
    return scope_package_manager_semantics(
        _identity(consumption),
        manager_environment=_manager(
            location,
            environment=manager_environment,
        ),
        installation_destination=_destination(
            location,
            kind=destination_kind,
            value=destination_value,
        ),
        package_mutation_mode=mutation_problem or _mutation(
            location,
            mode=mutation_mode,
        ),
        direct_requirement_handling=_direct(
            location,
            handling=direct_handling,
        ),
    )


def _execution(
    consumption: StaticDependencyConsumptionEvidence,
    *,
    state: str = "supported",
    workflow_path: str | None = None,
    job_key: str | None = None,
) -> ExactCommandExecutionAssessment:
    return ExactCommandExecutionAssessment(
        state=state,  # type: ignore[arg-type]
        basis=("supported" if state == "supported" else "runtime_non_success"),
        reason=(
            "exact_command_execution_supported"
            if state == "supported"
            else "correlated_step_execution_not_successful"
        ),
        detail="Focused composer execution fixture.",
        workflow_path=workflow_path or consumption.workflow_path,
        workflow_revision=consumption.workflow_revision,
        job_key=job_key or consumption.job_key,
        step_source_index=consumption.step_source_index,
        command_location=consumption.command_location,
    )


class CommandDerivedRequirementStateTests(unittest.TestCase):
    def test_positive_direct_requirements_command_produces_bounded_witness(self) -> None:
        source = _source_evidence()
        dependency = _dependency(source)
        source_context = _source_context(source)
        consumption = _consumption()

        result = compose_requirement_satisfied_at_command_completion(
            dependency,
            source_context,
            consumption,
            _semantics(consumption),
            _execution(consumption),
        )

        self.assertIsInstance(result, RequirementSatisfiedAtCommandCompletion)
        assert isinstance(result, RequirementSatisfiedAtCommandCompletion)
        self.assertEqual(result.dependency.proposed_version, "2.33.0")
        self.assertEqual(result.source_context.source_path, _SOURCE_PATH)
        self.assertEqual(
            result.semantics.manager_environment.environment.value,  # type: ignore[union-attr]
            "/opt/venv/bin/python",
        )
        self.assertEqual(result.observation_boundary, "successful_command_completion")
        self.assertIn("Does not establish behavioral compatibility.", result.limitations)

    def test_effective_dry_run_is_not_established(self) -> None:
        source = _source_evidence()
        dependency = _dependency(source)
        source_context = _source_context(source)
        consumption = _consumption()

        result = compose_requirement_satisfied_at_command_completion(
            dependency,
            source_context,
            consumption,
            _semantics(consumption, mutation_mode="dry_run"),
            _execution(consumption),
        )

        self.assertIsInstance(result, RequirementStateProblem)
        assert isinstance(result, RequirementStateProblem)
        self.assertEqual(result.state, "not_established")
        self.assertEqual(result.reason, "package_mutation_does_not_apply_changes")
        self.assertEqual(result.blocking_dimension, "package_mutation_mode")

    def test_retargeted_destination_is_not_established_for_first_family(self) -> None:
        source = _source_evidence()
        dependency = _dependency(source)
        source_context = _source_context(source)
        consumption = _consumption()

        result = compose_requirement_satisfied_at_command_completion(
            dependency,
            source_context,
            consumption,
            _semantics(
                consumption,
                destination_kind="target_directory",
                destination_value="vendor",
            ),
            _execution(consumption),
        )

        self.assertIsInstance(result, RequirementStateProblem)
        assert isinstance(result, RequirementStateProblem)
        self.assertEqual(result.state, "not_established")
        self.assertEqual(
            result.reason,
            "installation_destination_outside_admitted_requirement_state_scope",
        )

    def test_unresolved_semantic_source_stays_unresolved(self) -> None:
        source = _source_evidence()
        dependency = _dependency(source)
        source_context = _source_context(source)
        consumption = _consumption()
        assert consumption.command_location is not None
        semantic_problem = PackageManagerSemanticProblem(
            state="unresolved",
            dimension="package_mutation_mode",
            reason="package_mutation_mode_needs_lower_source_evidence",
            detail="PIP_DRY_RUN/config precedence is not closed.",
            command_location=consumption.command_location,
            blocking_source="process_environment",
        )

        result = compose_requirement_satisfied_at_command_completion(
            dependency,
            source_context,
            consumption,
            _semantics(consumption, mutation_problem=semantic_problem),
            _execution(consumption),
        )

        self.assertIsInstance(result, RequirementStateProblem)
        assert isinstance(result, RequirementStateProblem)
        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            result.reason,
            "package_mutation_mode_needs_lower_source_evidence",
        )
        self.assertEqual(result.blocking_dimension, "package_mutation_mode")

    def test_runtime_non_success_is_not_established(self) -> None:
        source = _source_evidence()
        dependency = _dependency(source)
        source_context = _source_context(source)
        consumption = _consumption()

        result = compose_requirement_satisfied_at_command_completion(
            dependency,
            source_context,
            consumption,
            _semantics(consumption),
            _execution(consumption, state="not_established"),
        )

        self.assertIsInstance(result, RequirementStateProblem)
        assert isinstance(result, RequirementStateProblem)
        self.assertEqual(result.state, "not_established")
        self.assertEqual(result.reason, "correlated_step_execution_not_successful")

    def test_same_local_location_from_other_workflow_is_rejected(self) -> None:
        source = _source_evidence()
        dependency = _dependency(source)
        source_context = _source_context(source)
        consumption = _consumption(workflow_path=".github/workflows/test.yml")
        other_consumption = _consumption(workflow_path=".github/workflows/release.yml")

        result = compose_requirement_satisfied_at_command_completion(
            dependency,
            source_context,
            consumption,
            _semantics(other_consumption),
            _execution(consumption),
        )

        self.assertIsInstance(result, RequirementStateProblem)
        assert isinstance(result, RequirementStateProblem)
        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "scoped_semantic_command_identity_mismatch")

    def test_multiple_command_candidates_remain_separate_witnesses(self) -> None:
        source = _source_evidence()
        dependency = _dependency(source)
        source_context = _source_context(source)
        first = _consumption(
            workflow_path=".github/workflows/first.yml",
            job_key="first",
        )
        second = _consumption(
            workflow_path=".github/workflows/second.yml",
            job_key="second",
        )

        first_result = compose_requirement_satisfied_at_command_completion(
            dependency,
            source_context,
            first,
            _semantics(first, manager_environment="/opt/first/bin/python"),
            _execution(first),
        )
        second_result = compose_requirement_satisfied_at_command_completion(
            dependency,
            source_context,
            second,
            _semantics(second, manager_environment="/opt/second/bin/python"),
            _execution(second),
        )

        self.assertIsInstance(first_result, RequirementSatisfiedAtCommandCompletion)
        self.assertIsInstance(second_result, RequirementSatisfiedAtCommandCompletion)
        assert isinstance(first_result, RequirementSatisfiedAtCommandCompletion)
        assert isinstance(second_result, RequirementSatisfiedAtCommandCompletion)
        self.assertNotEqual(
            first_result.semantics.command_identity,
            second_result.semantics.command_identity,
        )
        self.assertEqual(
            first_result.semantics.manager_environment.environment.value,  # type: ignore[union-attr]
            "/opt/first/bin/python",
        )
        self.assertEqual(
            second_result.semantics.manager_environment.environment.value,  # type: ignore[union-attr]
            "/opt/second/bin/python",
        )

    def test_dependency_source_mismatch_fails_closed(self) -> None:
        dependency_source = _source_evidence("requirements.txt")
        other_source = _source_evidence("requirements-dev.txt")
        dependency = _dependency(dependency_source)
        source_context = _source_context(other_source)
        consumption = _consumption()

        result = compose_requirement_satisfied_at_command_completion(
            dependency,
            source_context,
            consumption,
            _semantics(consumption),
            _execution(consumption),
        )

        self.assertIsInstance(result, RequirementStateProblem)
        assert isinstance(result, RequirementStateProblem)
        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "dependency_source_evidence_identity_mismatch")


class RouteARequirementStateIntegrationTests(unittest.TestCase):
    def test_real_producers_compose_one_command_completion_witness(self) -> None:
        source_evidence = _source_evidence()
        dependency = _dependency(source_evidence)
        source_context = _source_context(source_evidence)
        workflow_source = RepositoryTextFile(
            repository="example/project",
            path=_WORKFLOW,
            revision=_REVISION,
            content="""jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Install
        run: PIP_DRY_RUN=0 PIP_CONFIG_FILE=/dev/null PIP_TARGET= PIP_PREFIX= PIP_ROOT= PIP_ONLY_DEPS=0 PIP_ONLY_DEPENDENCIES=0 /opt/bootstrap/bin/python -m pip --python /opt/target/bin/python install --no-user --no-deps -r requirements.txt
""",
        )

        static = inspect_workflow_dependency_evidence(
            workflow_source,
            source_contexts=(source_context,),
            package=dependency.package,
            normalized_package=dependency.normalized_package,
        )
        self.assertEqual(len(static.consumptions), 1)
        consumption = static.consumptions[0]
        self.assertEqual(consumption.state, "supported")
        self.assertEqual(consumption.mechanism, "direct_requirements")

        definition = parse_workflow_definition(workflow_source)
        assert isinstance(definition, WorkflowDefinition)
        job = definition.jobs[0]
        assert isinstance(job, StepsJobDefinition)
        step = job.steps[1]
        assert isinstance(step, RunStepDefinition)

        analysis = analyze_run_step_commands(definition, job, step)
        self.assertEqual(analysis.state, "analyzable")
        occurrence = analysis.command_occurrences[0]
        declaration = parse_package_manager_operation(occurrence)
        assert isinstance(declaration, PackageManagerOperationDeclaration)
        self.assertEqual(declaration.command_location, consumption.command_location)

        def process_environment(variable_name: str) -> ProcessEnvironmentValueEvidence:
            result = observe_exact_process_environment_value(
                definition,
                job,
                step,
                occurrence,
                variable_name,
            )
            assert isinstance(result, ProcessEnvironmentValueEvidence)
            return result

        config_file_environment = process_environment("PIP_CONFIG_FILE")
        destination_environment = tuple(
            process_environment(variable_name)
            for variable_name in ("PIP_TARGET", "PIP_PREFIX", "PIP_ROOT")
        )
        direct_environment = tuple(
            process_environment(variable_name)
            for variable_name in ("PIP_ONLY_DEPS", "PIP_ONLY_DEPENDENCIES")
        )
        mutation_environment = process_environment("PIP_DRY_RUN")

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

        manager_environment = _manager(declaration.command_location, environment="/opt/target/bin/python")
        installation_destination = __import__(
            "upgradepilot.dependency.package_manager_semantics",
            fromlist=["resolve_installation_destination"],
        ).resolve_installation_destination(
            declaration,
            process_environment=destination_environment,
            persistent_configuration=destination_config,
        )
        package_mutation_mode = __import__(
            "upgradepilot.dependency.package_manager_semantics",
            fromlist=["resolve_package_mutation_mode"],
        ).resolve_package_mutation_mode(
            declaration,
            process_environment=mutation_environment,
            persistent_configuration=mutation_config,
        )
        direct_requirement_handling = __import__(
            "upgradepilot.dependency.package_manager_semantics",
            fromlist=["resolve_direct_requirement_handling"],
        ).resolve_direct_requirement_handling(
            declaration,
            process_environment=direct_environment,
            persistent_configuration=direct_config,
        )

        semantic_scope = scope_package_manager_semantics(
            ExactCICommandIdentity(
                workflow_path=workflow_source.path,
                workflow_revision=workflow_source.revision,
                job_key=job.key,
                step_source_index=step.source_index,
                command_location=declaration.command_location,
            ),
            manager_environment=manager_environment,
            installation_destination=installation_destination,
            package_mutation_mode=package_mutation_mode,
            direct_requirement_handling=direct_requirement_handling,
        )

        run = WorkflowRun(
            run_id=1001,
            workflow_id=2001,
            name="CI",
            event="pull_request",
            head_sha=_REVISION,
            status="completed",
            conclusion="success",
            run_attempt=1,
        )
        runtime_job = WorkflowJob(
            job_id=3001,
            run_id=1001,
            name="Tests",
            head_sha=_REVISION,
            status="completed",
            conclusion="success",
            steps=(
                WorkflowStep(
                    number=1,
                    name="Checkout",
                    status="completed",
                    conclusion="success",
                ),
                WorkflowStep(
                    number=2,
                    name="Install",
                    status="completed",
                    conclusion="success",
                ),
            ),
        )
        correlation = correlate_workflow_runtime(
            workflow_source,
            run,
            (runtime_job,),
        )
        execution = assess_exact_command_execution(
            candidate_from_consumption(consumption),
            correlation=correlation,
        )

        result = compose_requirement_satisfied_at_command_completion(
            dependency,
            source_context,
            consumption,
            semantic_scope,
            execution,
        )

        self.assertIsInstance(result, RequirementSatisfiedAtCommandCompletion)
        assert isinstance(result, RequirementSatisfiedAtCommandCompletion)
        self.assertEqual(
            result.semantics.command_identity.workflow_path,
            _WORKFLOW,
        )
        self.assertEqual(
            result.semantics.manager_environment.environment.value,  # type: ignore[union-attr]
            "/opt/target/bin/python",
        )
        self.assertEqual(result.execution.runtime_step_number, 2)


if __name__ == "__main__":
    unittest.main()
