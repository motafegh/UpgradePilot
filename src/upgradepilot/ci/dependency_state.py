"""Compose bounded command-derived dependency requirement state.

This module owns one CI-level proposition:

    exact dependency/source applicability
    + supported direct-requirements consumption
    + effective package-manager semantics for that same scoped command
    + exact successful execution of that same scoped command
    -> RequirementSatisfiedAtCommandCompletion

The witness is intentionally narrower than later use or compatibility. It establishes only
that the exact proposed direct requirement is satisfied in the resolved package-state scope
at the completion boundary of the exact successful command.

Package-manager semantic interpretation remains dependency-owned. This module only binds
those command-local semantic results to exact CI workflow/job/step scope and composes them
with source and runtime evidence.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from ..dependency.change import DependencyVersionChange
from ..dependency.environment import DependencySourceContext, RequirementsFileDependencyContext
from ..dependency.package_manager_config import observe_pip_persistent_config_setting
from ..dependency.package_manager_operation import (
    PackageManagerOperationDeclaration,
    parse_package_manager_operation,
)
from ..dependency.package_manager_semantics import (
    DirectRequirementHandlingFact,
    InstallationDestinationFact,
    ManagerEnvironmentSelectionFact,
    PackageManagerSemanticDimension,
    PackageManagerSemanticProblem,
    PackageMutationModeFact,
    resolve_direct_requirement_handling,
    resolve_installation_destination,
    resolve_manager_environment_selection,
    resolve_package_mutation_mode,
)
from ..github.process_environment import observe_exact_process_environment_value
from ..github.repository import RepositoryTextFile
from ..github.workflow_command_analysis import StaticCommandOccurrence, analyze_run_step_commands
from ..github.workflow_command_location import StaticCommandLocation
from ..github.workflow_definition import (
    RunStepDefinition,
    StepsJobDefinition,
    WorkflowDefinition,
    parse_workflow_definition,
)
from .consumption import StaticDependencyConsumptionEvidence
from .dependency_exercise import DependencyCICoverageResult, WorkflowDependencyCoverageInput
from .runtime_execution import ExactCommandExecutionAssessment, assess_exact_command_execution
from .runtime_strengthening import candidate_from_consumption


type RequirementStateProblemState = Literal["not_established", "unresolved"]
type RuntimeDependencyStateEvaluationState = Literal["evaluated", "no_admitted_candidate"]
type ManagerEnvironmentSemanticResult = (
    ManagerEnvironmentSelectionFact | PackageManagerSemanticProblem
)
type InstallationDestinationSemanticResult = (
    InstallationDestinationFact | PackageManagerSemanticProblem
)
type PackageMutationSemanticResult = PackageMutationModeFact | PackageManagerSemanticProblem
type DirectRequirementSemanticResult = (
    DirectRequirementHandlingFact | PackageManagerSemanticProblem
)
type RequirementStateBlockingSemanticEvidence = (
    ManagerEnvironmentSelectionFact
    | InstallationDestinationFact
    | PackageMutationModeFact
    | DirectRequirementHandlingFact
    | PackageManagerSemanticProblem
)


@dataclass(frozen=True, slots=True)
class ExactCICommandIdentity:
    """Workflow-scoped identity for one parsed static command occurrence."""

    workflow_path: str
    workflow_revision: str
    job_key: str
    step_source_index: int
    command_location: StaticCommandLocation


@dataclass(frozen=True, slots=True)
class ScopedPackageManagerSemanticEvidence:
    """Package-manager semantic results bound to one exact CI command scope.

    Semantic fact types remain dependency-owned and command-local. This CI-owned wrapper
    retains the workflow/revision/job/step scope needed to prevent evidence from another
    command context being composed merely because its local source span/order looks equal.
    """

    command_identity: ExactCICommandIdentity
    manager_environment: ManagerEnvironmentSemanticResult
    installation_destination: InstallationDestinationSemanticResult
    package_mutation_mode: PackageMutationSemanticResult
    direct_requirement_handling: DirectRequirementSemanticResult


@dataclass(frozen=True, slots=True)
class RequirementSatisfiedAtCommandCompletion:
    """Bounded witness that the proposed direct requirement is satisfied at command completion."""

    dependency: DependencyVersionChange
    source_context: RequirementsFileDependencyContext
    consumption: StaticDependencyConsumptionEvidence
    semantics: ScopedPackageManagerSemanticEvidence
    execution: ExactCommandExecutionAssessment
    observation_boundary: Literal["successful_command_completion"] = (
        "successful_command_completion"
    )
    limitations: tuple[str, ...] = (
        "Does not establish fresh-install causality.",
        "Does not establish wheel, sdist, or other artifact identity.",
        "Does not establish persistence after command completion.",
        "Does not establish later package use or affected-behavior exercise.",
        "Does not establish behavioral compatibility.",
        "Does not grant maintainer-action permission.",
    )


@dataclass(frozen=True, slots=True)
class RequirementStateProblem:
    """Why the command-derived requirement-state witness was not established."""

    state: RequirementStateProblemState
    reason: str
    detail: str
    blocking_dimension: PackageManagerSemanticDimension | None = None
    blocking_semantic_evidence: RequirementStateBlockingSemanticEvidence | None = None


@dataclass(frozen=True, slots=True)
class CommandRequirementStateAssessment:
    """One admitted exact command and its bounded command-completion state result."""

    consumption: StaticDependencyConsumptionEvidence
    result: RequirementSatisfiedAtCommandCompletion | RequirementStateProblem


@dataclass(frozen=True, slots=True)
class RuntimeDependencyStateResult:
    """Application-ready collection of per-command runtime dependency-state assessments."""

    evaluation_state: RuntimeDependencyStateEvaluationState
    reason: str
    detail: str
    assessments: tuple[CommandRequirementStateAssessment, ...] = ()


def evaluate_runtime_dependency_state(
    dependency: DependencyVersionChange,
    workflow_inputs: Sequence[WorkflowDependencyCoverageInput],
    ci_coverage_result: DependencyCICoverageResult,
    *,
    source_contexts: Sequence[DependencySourceContext],
) -> RuntimeDependencyStateResult:
    """Evaluate the first admitted direct-requirements/pip state family.

    Existing CI consumption and runtime-correlation results are authoritative inputs.
    This evaluator only performs the command-local semantic work that CI coverage does not
    retain, then composes the already-defined command-completion proposition.
    """

    if len(ci_coverage_result.workflows) != len(workflow_inputs):
        raise ValueError(
            "CI workflow results must preserve one-to-one ordering with coverage inputs"
        )

    assessments: list[CommandRequirementStateAssessment] = []

    for workflow_result, workflow_input in zip(
        ci_coverage_result.workflows,
        workflow_inputs,
        strict=True,
    ):
        definition_source = workflow_input.definition
        if workflow_result.workflow_path != definition_source.path:
            raise ValueError(
                "CI workflow result path does not match its exact workflow definition"
            )

        candidates = tuple(
            consumption
            for consumption in workflow_result.consumptions
            if consumption.state == "supported"
            and consumption.mechanism == "direct_requirements"
        )
        if not candidates:
            continue

        if not isinstance(definition_source, RepositoryTextFile):
            raise ValueError(
                "supported direct-requirements consumption requires an exact readable "
                "workflow definition"
            )

        definition = parse_workflow_definition(definition_source)
        if not isinstance(definition, WorkflowDefinition):
            raise ValueError(
                "supported direct-requirements consumption could not be recovered from "
                "the same exact workflow definition"
            )

        if workflow_result.runtime_correlation is None:
            raise ValueError(
                "supported direct-requirements consumption requires retained workflow "
                "runtime correlation evidence"
            )

        for consumption in candidates:
            source_context = _matching_requirements_source_context(
                dependency,
                definition_source,
                consumption,
                source_contexts,
            )
            job, step, occurrence = _locate_exact_consuming_command(
                definition,
                consumption,
            )

            declaration = parse_package_manager_operation(occurrence)
            if not isinstance(declaration, PackageManagerOperationDeclaration):
                raise ValueError(
                    "supported direct-requirements consumption must map back to one admitted "
                    "pip operation declaration"
                )
            if declaration.command_location != consumption.command_location:
                raise ValueError(
                    "recovered package-manager declaration does not preserve the supported "
                    "consumption command identity"
                )

            semantic_scope = scope_package_manager_semantics(
                ExactCICommandIdentity(
                    workflow_path=definition.source.path,
                    workflow_revision=definition.source.revision,
                    job_key=job.key,
                    step_source_index=step.source_index,
                    command_location=declaration.command_location,
                ),
                manager_environment=resolve_manager_environment_selection(declaration),
                installation_destination=_resolve_installation_destination_for_command(
                    definition,
                    job,
                    step,
                    occurrence,
                    declaration,
                ),
                package_mutation_mode=_resolve_package_mutation_mode_for_command(
                    definition,
                    job,
                    step,
                    occurrence,
                    declaration,
                ),
                direct_requirement_handling=_resolve_direct_requirement_handling_for_command(
                    definition,
                    job,
                    step,
                    occurrence,
                    declaration,
                ),
            )
            execution = assess_exact_command_execution(
                candidate_from_consumption(consumption),
                correlation=workflow_result.runtime_correlation,
            )
            result = compose_requirement_satisfied_at_command_completion(
                dependency,
                source_context,
                consumption,
                semantic_scope,
                execution,
            )
            assessments.append(
                CommandRequirementStateAssessment(
                    consumption=consumption,
                    result=result,
                )
            )

    if not assessments:
        return RuntimeDependencyStateResult(
            evaluation_state="no_admitted_candidate",
            reason="no_admitted_runtime_dependency_state_candidate",
            detail=(
                "No supported direct-requirements/pip consumption entered the first "
                "command-derived runtime dependency-state proof family."
            ),
        )

    return RuntimeDependencyStateResult(
        evaluation_state="evaluated",
        reason="runtime_dependency_state_candidates_evaluated",
        detail=(
            f"Evaluated {len(assessments)} admitted exact direct-requirements command "
            "candidate(s) without collapsing their individual outcomes."
        ),
        assessments=tuple(assessments),
    )


def _matching_requirements_source_context(
    dependency: DependencyVersionChange,
    workflow_source: RepositoryTextFile,
    consumption: StaticDependencyConsumptionEvidence,
    source_contexts: Sequence[DependencySourceContext],
) -> RequirementsFileDependencyContext:
    if consumption.source_path is None:
        raise ValueError(
            "supported direct-requirements consumption must preserve its exact source path"
        )
    if (
        consumption.workflow_path != workflow_source.path
        or consumption.workflow_revision != workflow_source.revision
        or consumption.normalized_package != dependency.normalized_package
    ):
        raise ValueError(
            "supported direct-requirements consumption does not match the exact "
            "workflow/dependency identity under evaluation"
        )

    matches = tuple(
        context
        for context in source_contexts
        if isinstance(context, RequirementsFileDependencyContext)
        and context.repository == workflow_source.repository
        and context.revision == workflow_source.revision
        and context.source_path == consumption.source_path
        and context.normalized_package == dependency.normalized_package
    )
    if len(matches) != 1:
        raise ValueError(
            "supported direct-requirements consumption must map to one exact trusted "
            "requirements dependency source context"
        )
    return matches[0]


def _locate_exact_consuming_command(
    definition: WorkflowDefinition,
    consumption: StaticDependencyConsumptionEvidence,
) -> tuple[StepsJobDefinition, RunStepDefinition, StaticCommandOccurrence]:
    if not consumption.job_key or consumption.command_location is None:
        raise ValueError(
            "supported direct-requirements consumption must preserve exact "
            "job/step/command identity"
        )

    jobs = tuple(
        job
        for job in definition.jobs
        if isinstance(job, StepsJobDefinition) and job.key == consumption.job_key
    )
    if len(jobs) != 1:
        raise ValueError(
            "supported direct-requirements consumption must map to one readable local job"
        )
    job = jobs[0]

    steps = tuple(
        step
        for step in job.steps
        if isinstance(step, RunStepDefinition)
        and step.source_index == consumption.step_source_index
    )
    if len(steps) != 1:
        raise ValueError(
            "supported direct-requirements consumption must map to one exact run step"
        )
    step = steps[0]
    if step.command.text != consumption.command:
        raise ValueError(
            "supported direct-requirements consumption command text does not match the "
            "exact workflow run step"
        )

    analysis = analyze_run_step_commands(definition, job, step)
    if analysis.state != "analyzable":
        raise ValueError(
            "supported direct-requirements consumption command is no longer analyzable "
            "from the same exact workflow definition"
        )

    occurrences = tuple(
        occurrence
        for occurrence in analysis.command_occurrences
        if StaticCommandLocation.from_occurrence(occurrence)
        == consumption.command_location
    )
    if len(occurrences) != 1:
        raise ValueError(
            "supported direct-requirements consumption must map to one exact parsed "
            "command occurrence"
        )
    return job, step, occurrences[0]


def _observe_process_environment(
    definition: WorkflowDefinition,
    job: StepsJobDefinition,
    step: RunStepDefinition,
    occurrence: StaticCommandOccurrence,
    variable_name: str,
):
    return observe_exact_process_environment_value(
        definition,
        job,
        step,
        occurrence,
        variable_name,
    )


def _resolve_installation_destination_for_command(
    definition: WorkflowDefinition,
    job: StepsJobDefinition,
    step: RunStepDefinition,
    occurrence: StaticCommandOccurrence,
    declaration: PackageManagerOperationDeclaration,
) -> InstallationDestinationSemanticResult:
    result = resolve_installation_destination(declaration)
    if not (
        isinstance(result, PackageManagerSemanticProblem)
        and result.blocking_source == "process_environment"
    ):
        return result

    process_environment = tuple(
        _observe_process_environment(
            definition,
            job,
            step,
            occurrence,
            variable_name,
        )
        for variable_name in ("PIP_TARGET", "PIP_PREFIX", "PIP_ROOT")
    )
    result = resolve_installation_destination(
        declaration,
        process_environment=process_environment,
    )
    if not (
        isinstance(result, PackageManagerSemanticProblem)
        and result.blocking_source == "persistent_configuration"
    ):
        return result

    config_file_environment = _observe_process_environment(
        definition,
        job,
        step,
        occurrence,
        "PIP_CONFIG_FILE",
    )
    persistent_configuration = observe_pip_persistent_config_setting(
        declaration,
        setting="installation-destination",
        config_file_environment=config_file_environment,
    )
    return resolve_installation_destination(
        declaration,
        process_environment=process_environment,
        persistent_configuration=persistent_configuration,
    )


def _resolve_package_mutation_mode_for_command(
    definition: WorkflowDefinition,
    job: StepsJobDefinition,
    step: RunStepDefinition,
    occurrence: StaticCommandOccurrence,
    declaration: PackageManagerOperationDeclaration,
) -> PackageMutationSemanticResult:
    result = resolve_package_mutation_mode(declaration)
    if not (
        isinstance(result, PackageManagerSemanticProblem)
        and result.blocking_source == "process_environment"
    ):
        return result

    process_environment = _observe_process_environment(
        definition,
        job,
        step,
        occurrence,
        "PIP_DRY_RUN",
    )
    result = resolve_package_mutation_mode(
        declaration,
        process_environment=process_environment,
    )
    if not (
        isinstance(result, PackageManagerSemanticProblem)
        and result.blocking_source == "persistent_configuration"
    ):
        return result

    config_file_environment = _observe_process_environment(
        definition,
        job,
        step,
        occurrence,
        "PIP_CONFIG_FILE",
    )
    persistent_configuration = observe_pip_persistent_config_setting(
        declaration,
        setting="dry-run",
        config_file_environment=config_file_environment,
    )
    return resolve_package_mutation_mode(
        declaration,
        process_environment=process_environment,
        persistent_configuration=persistent_configuration,
    )


def _resolve_direct_requirement_handling_for_command(
    definition: WorkflowDefinition,
    job: StepsJobDefinition,
    step: RunStepDefinition,
    occurrence: StaticCommandOccurrence,
    declaration: PackageManagerOperationDeclaration,
) -> DirectRequirementSemanticResult:
    result = resolve_direct_requirement_handling(declaration)
    if not (
        isinstance(result, PackageManagerSemanticProblem)
        and result.blocking_source == "process_environment"
    ):
        return result

    process_environment = tuple(
        _observe_process_environment(
            definition,
            job,
            step,
            occurrence,
            variable_name,
        )
        for variable_name in ("PIP_ONLY_DEPS", "PIP_ONLY_DEPENDENCIES")
    )
    result = resolve_direct_requirement_handling(
        declaration,
        process_environment=process_environment,
    )
    if not (
        isinstance(result, PackageManagerSemanticProblem)
        and result.blocking_source == "persistent_configuration"
    ):
        return result

    config_file_environment = _observe_process_environment(
        definition,
        job,
        step,
        occurrence,
        "PIP_CONFIG_FILE",
    )
    persistent_configuration = observe_pip_persistent_config_setting(
        declaration,
        setting="only-deps",
        config_file_environment=config_file_environment,
    )
    return resolve_direct_requirement_handling(
        declaration,
        process_environment=process_environment,
        persistent_configuration=persistent_configuration,
    )


def scope_package_manager_semantics(
    command_identity: ExactCICommandIdentity,
    *,
    manager_environment: ManagerEnvironmentSemanticResult,
    installation_destination: InstallationDestinationSemanticResult,
    package_mutation_mode: PackageMutationSemanticResult,
    direct_requirement_handling: DirectRequirementSemanticResult,
) -> ScopedPackageManagerSemanticEvidence | RequirementStateProblem:
    """Bind command-local semantic results to independently supplied exact CI scope.

    The command identity must come from the workflow/job/step/occurrence context in which
    the semantic results were resolved. It is intentionally not copied from dependency
    consumption evidence: the final composer compares these independently established
    identities so same-looking local command locations from different workflows cannot be
    silently joined.
    """

    if (
        not command_identity.workflow_path
        or not command_identity.workflow_revision
        or not command_identity.job_key
    ):
        return RequirementStateProblem(
            state="unresolved",
            reason="semantic_command_scope_identity_unresolved",
            detail=(
                "Scoped package-manager semantics require exact workflow/revision/job/"
                "step/command identity from the semantic-producing CI context."
            ),
        )

    semantic_results: tuple[
        tuple[PackageManagerSemanticDimension, object],
        ...,
    ] = (
        ("manager_environment", manager_environment),
        ("installation_destination", installation_destination),
        ("package_mutation_mode", package_mutation_mode),
        ("direct_requirement_handling", direct_requirement_handling),
    )

    for expected_dimension, result in semantic_results:
        command_location = result.command_location  # type: ignore[union-attr]
        if command_location != command_identity.command_location:
            return RequirementStateProblem(
                state="unresolved",
                reason="semantic_command_identity_mismatch",
                detail=(
                    f"Semantic result for {expected_dimension!r} does not belong to the "
                    "exact static command occurrence selected by the CI consumption evidence."
                ),
                blocking_dimension=expected_dimension,
            )
        if (
            isinstance(result, PackageManagerSemanticProblem)
            and result.dimension != expected_dimension
        ):
            return RequirementStateProblem(
                state="unresolved",
                reason="semantic_dimension_identity_mismatch",
                detail=(
                    f"Semantic problem for {result.dimension!r} was supplied as "
                    f"{expected_dimension!r}; the evidence cannot be safely rebound."
                ),
                blocking_dimension=expected_dimension,
            )

    return ScopedPackageManagerSemanticEvidence(
        command_identity=command_identity,
        manager_environment=manager_environment,
        installation_destination=installation_destination,
        package_mutation_mode=package_mutation_mode,
        direct_requirement_handling=direct_requirement_handling,
    )


def compose_requirement_satisfied_at_command_completion(
    dependency: DependencyVersionChange,
    source_context: RequirementsFileDependencyContext,
    consumption: StaticDependencyConsumptionEvidence,
    semantics: ScopedPackageManagerSemanticEvidence | RequirementStateProblem,
    execution: ExactCommandExecutionAssessment,
) -> RequirementSatisfiedAtCommandCompletion | RequirementStateProblem:
    """Compose one exact direct-requirements command-completion package-state witness."""

    source_problem = _validate_dependency_source_identity(
        dependency,
        source_context,
        consumption,
    )
    if source_problem is not None:
        return source_problem

    if consumption.state == "unresolved":
        return RequirementStateProblem(
            state="unresolved",
            reason=consumption.reason,
            detail=consumption.detail,
        )
    if consumption.state == "not_established":
        return RequirementStateProblem(
            state="not_established",
            reason=consumption.reason,
            detail=consumption.detail,
        )
    if consumption.mechanism != "direct_requirements":
        return RequirementStateProblem(
            state="not_established",
            reason="consumption_mechanism_outside_admitted_requirement_state_family",
            detail=(
                "The first command-derived requirement-state family requires exact direct "
                "requirements-file consumption. Other environment-selection mechanisms "
                "retain their existing evidence meaning."
            ),
        )

    consumption_identity = _command_identity_from_consumption(consumption)
    if isinstance(consumption_identity, RequirementStateProblem):
        return consumption_identity

    if isinstance(semantics, RequirementStateProblem):
        return semantics
    if semantics.command_identity != consumption_identity:
        return RequirementStateProblem(
            state="unresolved",
            reason="scoped_semantic_command_identity_mismatch",
            detail=(
                "The package-manager semantics are bound to a different workflow/revision/"
                "job/step/command identity than the changed-dependency consumption evidence."
            ),
        )

    execution_identity = _command_identity_from_execution(execution)
    if isinstance(execution_identity, RequirementStateProblem):
        return execution_identity
    if execution_identity != consumption_identity:
        return RequirementStateProblem(
            state="unresolved",
            reason="runtime_command_identity_mismatch",
            detail=(
                "The exact execution assessment belongs to a different workflow/revision/"
                "job/step/command identity than the dependency consumption evidence."
            ),
        )

    semantic_problem = _first_semantic_problem(semantics)
    if semantic_problem is not None:
        return RequirementStateProblem(
            state=(
                "unresolved"
                if semantic_problem.state == "unresolved"
                else "not_established"
            ),
            reason=semantic_problem.reason,
            detail=semantic_problem.detail,
            blocking_dimension=semantic_problem.dimension,
            blocking_semantic_evidence=semantic_problem,
        )

    manager_environment = semantics.manager_environment
    installation_destination = semantics.installation_destination
    package_mutation_mode = semantics.package_mutation_mode
    direct_requirement_handling = semantics.direct_requirement_handling

    assert isinstance(manager_environment, ManagerEnvironmentSelectionFact)
    assert isinstance(installation_destination, InstallationDestinationFact)
    assert isinstance(package_mutation_mode, PackageMutationModeFact)
    assert isinstance(direct_requirement_handling, DirectRequirementHandlingFact)

    managers = {
        manager_environment.manager,
        installation_destination.manager,
        package_mutation_mode.manager,
        direct_requirement_handling.manager,
    }
    if len(managers) != 1:
        return RequirementStateProblem(
            state="unresolved",
            reason="package_manager_identity_mismatch",
            detail=(
                "The semantic facts do not agree on one package-manager identity for the "
                "exact command."
            ),
        )

    if installation_destination.destination.kind != "manager_environment_scheme":
        return RequirementStateProblem(
            state="not_established",
            reason="installation_destination_outside_admitted_requirement_state_scope",
            detail=(
                "The exact install command targets a package destination outside the first "
                "admitted manager-environment package-state scope."
            ),
            blocking_dimension="installation_destination",
            blocking_semantic_evidence=installation_destination,
        )

    if package_mutation_mode.mode != "apply_changes":
        return RequirementStateProblem(
            state="not_established",
            reason="package_mutation_does_not_apply_changes",
            detail=(
                "The exact package-manager command does not apply package-state changes, so "
                "successful command completion cannot establish the proposed requirement."
            ),
            blocking_dimension="package_mutation_mode",
            blocking_semantic_evidence=package_mutation_mode,
        )

    if direct_requirement_handling.handling != "handled":
        return RequirementStateProblem(
            state="not_established",
            reason="direct_requirement_not_handled",
            detail=(
                "The package-manager semantics exclude the direct requirement from the "
                "operation, so the proposed direct requirement is not established at command "
                "completion."
            ),
            blocking_dimension="direct_requirement_handling",
            blocking_semantic_evidence=direct_requirement_handling,
        )

    if execution.state == "unresolved":
        return RequirementStateProblem(
            state="unresolved",
            reason=execution.reason,
            detail=execution.detail,
        )
    if execution.state == "not_established":
        return RequirementStateProblem(
            state="not_established",
            reason=execution.reason,
            detail=execution.detail,
        )

    return RequirementSatisfiedAtCommandCompletion(
        dependency=dependency,
        source_context=source_context,
        consumption=consumption,
        semantics=semantics,
        execution=execution,
    )


def _validate_dependency_source_identity(
    dependency: DependencyVersionChange,
    source_context: RequirementsFileDependencyContext,
    consumption: StaticDependencyConsumptionEvidence,
) -> RequirementStateProblem | None:
    if source_context.source_evidence not in dependency.source_evidence:
        return RequirementStateProblem(
            state="unresolved",
            reason="dependency_source_evidence_identity_mismatch",
            detail=(
                "The requirements source context is not one of the trusted source evidence "
                "records that established the dependency transition."
            ),
        )
    if source_context.source_evidence.file_format != "exact_requirement":
        return RequirementStateProblem(
            state="not_established",
            reason="dependency_source_format_outside_admitted_requirement_state_family",
            detail=(
                "The first command-derived requirement-state family is limited to exact "
                "requirements-file dependency sources."
            ),
        )
    if source_context.normalized_package != dependency.normalized_package:
        return RequirementStateProblem(
            state="unresolved",
            reason="dependency_source_package_identity_mismatch",
            detail=(
                "The requirements source context does not preserve the same normalized "
                "package identity as the trusted dependency transition."
            ),
        )
    if consumption.normalized_package != dependency.normalized_package:
        return RequirementStateProblem(
            state="unresolved",
            reason="consumption_package_identity_mismatch",
            detail=(
                "The CI consumption evidence belongs to a different normalized package than "
                "the trusted dependency transition."
            ),
        )
    if consumption.source_path != source_context.source_path:
        return RequirementStateProblem(
            state="unresolved",
            reason="consumption_source_identity_mismatch",
            detail=(
                "The CI consumption evidence does not consume the exact requirements source "
                "that established this dependency transition."
            ),
        )
    if consumption.workflow_revision != source_context.revision:
        return RequirementStateProblem(
            state="unresolved",
            reason="dependency_workflow_revision_identity_mismatch",
            detail=(
                "The requirements source context and workflow consumption evidence do not "
                "belong to the same exact repository revision."
            ),
        )
    return None


def _command_identity_from_consumption(
    consumption: StaticDependencyConsumptionEvidence,
) -> ExactCICommandIdentity | RequirementStateProblem:
    if (
        not consumption.workflow_path
        or not consumption.workflow_revision
        or not consumption.job_key
        or consumption.command_location is None
    ):
        return RequirementStateProblem(
            state="unresolved",
            reason="consumption_command_identity_unresolved",
            detail=(
                "Command-derived requirement state requires exact workflow/revision/job/"
                "step/command identity from the dependency consumption evidence."
            ),
        )
    return ExactCICommandIdentity(
        workflow_path=consumption.workflow_path,
        workflow_revision=consumption.workflow_revision,
        job_key=consumption.job_key,
        step_source_index=consumption.step_source_index,
        command_location=consumption.command_location,
    )


def _command_identity_from_execution(
    execution: ExactCommandExecutionAssessment,
) -> ExactCICommandIdentity | RequirementStateProblem:
    if (
        not execution.workflow_path
        or not execution.workflow_revision
        or not execution.job_key
        or execution.command_location is None
    ):
        return RequirementStateProblem(
            state="unresolved",
            reason="runtime_command_identity_unresolved",
            detail=(
                "Exact command execution evidence does not preserve the complete workflow/"
                "revision/job/step/command identity required for package-state composition."
            ),
        )
    return ExactCICommandIdentity(
        workflow_path=execution.workflow_path,
        workflow_revision=execution.workflow_revision,
        job_key=execution.job_key,
        step_source_index=execution.step_source_index,
        command_location=execution.command_location,
    )


def _first_semantic_problem(
    semantics: ScopedPackageManagerSemanticEvidence,
) -> PackageManagerSemanticProblem | None:
    for result in (
        semantics.manager_environment,
        semantics.installation_destination,
        semantics.package_mutation_mode,
        semantics.direct_requirement_handling,
    ):
        if isinstance(result, PackageManagerSemanticProblem):
            return result
    return None


__all__ = (
    "CommandRequirementStateAssessment",
    "ExactCICommandIdentity",
    "RequirementSatisfiedAtCommandCompletion",
    "RequirementStateProblem",
    "RequirementStateBlockingSemanticEvidence",
    "RequirementStateProblemState",
    "RuntimeDependencyStateEvaluationState",
    "RuntimeDependencyStateResult",
    "ScopedPackageManagerSemanticEvidence",
    "compose_requirement_satisfied_at_command_completion",
    "evaluate_runtime_dependency_state",
    "scope_package_manager_semantics",
)
