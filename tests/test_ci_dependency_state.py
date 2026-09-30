from __future__ import annotations

import unittest

from upgradepilot.ci.consumption import StaticDependencyConsumptionEvidence
from upgradepilot.ci.dependency_state import (
    RequirementSatisfiedAtCommandCompletion,
    RequirementStateProblem,
    compose_requirement_satisfied_at_command_completion,
    scope_package_manager_semantics,
)
from upgradepilot.ci.runtime_execution import ExactCommandExecutionAssessment
from upgradepilot.dependency.change import (
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.dependency.environment import RequirementsFileDependencyContext
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
from upgradepilot.github.workflow_command_analysis import CommandSourceSpan
from upgradepilot.github.workflow_command_location import StaticCommandLocation


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
        consumption,
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


if __name__ == "__main__":
    unittest.main()
