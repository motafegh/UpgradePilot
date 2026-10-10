"""Fixed version-1 layouts for native CI coverage and command-completion results.

The representation retains command scope, semantic provenance and problem variants.
It neither derives those facts nor strengthens their native proof boundary. Shared inputs
are supplied by workspace.native_inputs_codec; no SQL or consumer/report dependency exists."""

from __future__ import annotations

from upgradepilot.ci.consumption import (
    StaticDependencyConsumptionEvidence,
)
from upgradepilot.ci.dependency_exercise import (
    DependencyCICoverageResult,
    WorkflowDependencyCoverageInput,
    WorkflowDependencyCoverageResult,
)
from upgradepilot.ci.dependency_state import (
    CommandRequirementStateAssessment,
    ExactCICommandIdentity,
    RequirementSatisfiedAtCommandCompletion,
    RequirementStateProblem,
    RuntimeDependencyStateResult,
    ScopedPackageManagerSemanticEvidence,
)
from upgradepilot.ci.runtime_execution import (
    CorrelatedStepExecutionAssessment,
    ExactCommandExecutionAssessment,
)
from upgradepilot.ci.workflow_commands import (
    DirectPackageInvocationEvidence,
    StaticWorkflowDependencyProblem,
    WorkflowProjectEnvironmentSource,
)
from upgradepilot.ci.workflow_runtime_correlation import (
    WorkflowRuntimeCorrelationResult,
    WorkflowRuntimeJobCorrelation,
    WorkflowRuntimeStepCorrelation,
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
from upgradepilot.workspace.native_representation import (
    Either,
    LiteralValues,
    RecordLayout,
    RecordRef,
    SequenceOf,
)

# This is an admitted representation table, not a runtime dataclass discovery mechanism.
LAYOUTS = (
    RecordLayout(
        "command_requirement_state_assessment",
        CommandRequirementStateAssessment,
        (
            ("consumption", RecordRef("static_dependency_consumption_evidence")),
            (
                "result",
                Either(
                    (
                        RecordRef("requirement_satisfied_at_command_completion"),
                        RecordRef("requirement_state_problem"),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "correlated_step_execution_assessment",
        CorrelatedStepExecutionAssessment,
        (
            ("state", LiteralValues(("supported", "not_established", "unresolved"))),
            (
                "basis",
                LiteralValues(
                    ("supported", "continue_on_error_unresolved", "runtime_non_success")
                ),
            ),
            ("reason", str),
            ("detail", str),
            ("correlation", RecordRef("workflow_runtime_step_correlation")),
        ),
    ),
    RecordLayout(
        "dependency_ci_coverage_result",
        DependencyCICoverageResult,
        (
            (
                "state",
                LiteralValues(
                    (
                        "supported_runtime_correlated",
                        "supported_not_correlated",
                        "no_successful_ci",
                        "unresolved",
                    )
                ),
            ),
            ("reason", str),
            ("detail", str),
            ("workflows", SequenceOf(RecordRef("workflow_dependency_coverage_result"))),
        ),
    ),
    RecordLayout(
        "direct_package_invocation_evidence",
        DirectPackageInvocationEvidence,
        (
            ("job_key", str),
            ("step_source_index", int),
            ("command", str),
            ("state", LiteralValues(("observed", "unresolved"))),
            ("reason", str),
            ("detail", str),
            (
                "command_location",
                Either(
                    (
                        RecordRef("static_command_location"),
                        type(None),
                    )
                ),
            ),
            (
                "structural_context",
                SequenceOf(
                    LiteralValues(
                        (
                            "straightforward_top_level",
                            "linear_chain",
                            "short_circuit",
                            "conditional",
                            "loop",
                            "pipeline",
                            "function_or_block",
                            "nested_or_subshell",
                            "status_inverted",
                            "asynchronous",
                            "process_substitution",
                        )
                    )
                ),
            ),
            (
                "whole_step_relation",
                Either(
                    (
                        LiteralValues(
                            (
                                "sole_ordinary_top_level_command",
                                "first_ordinary_top_level_command_in_sequential_script",
                            )
                        ),
                        type(None),
                    )
                ),
            ),
            (
                "execution_profile",
                Either(
                    (
                        LiteralValues(
                            (
                                "github_builtin_bash",
                                "github_builtin_sh",
                                "github_builtin_pwsh",
                                "github_builtin_powershell",
                                "github_builtin_cmd",
                                "github_default_non_windows",
                                "github_default_windows",
                                "github_default_container_sh",
                                "custom_shell_template",
                            )
                        ),
                        type(None),
                    )
                ),
            ),
            (
                "workflow_path",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
            (
                "workflow_revision",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "direct_requirement_handling_fact",
        DirectRequirementHandlingFact,
        (
            ("manager", LiteralValues(("pip",))),
            ("command_location", RecordRef("static_command_location")),
            ("handling", LiteralValues(("handled", "excluded"))),
            ("provenance", RecordRef("package_manager_semantic_resolution_provenance")),
        ),
    ),
    RecordLayout(
        "exact_ci_command_identity",
        ExactCICommandIdentity,
        (
            ("workflow_path", str),
            ("workflow_revision", str),
            ("job_key", str),
            ("step_source_index", int),
            ("command_location", RecordRef("static_command_location")),
        ),
    ),
    RecordLayout(
        "exact_command_execution_assessment",
        ExactCommandExecutionAssessment,
        (
            ("state", LiteralValues(("supported", "not_established", "unresolved"))),
            (
                "basis",
                LiteralValues(
                    (
                        "supported",
                        "eligibility_ineligible",
                        "eligibility_unresolved",
                        "workflow_correlation_unresolved",
                        "step_correlation_unresolved",
                        "continue_on_error_unresolved",
                        "runtime_non_success",
                    )
                ),
            ),
            ("reason", str),
            ("detail", str),
            (
                "workflow_path",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
            (
                "workflow_revision",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
            ("job_key", str),
            ("step_source_index", int),
            (
                "command_location",
                Either(
                    (
                        RecordRef("static_command_location"),
                        type(None),
                    )
                ),
            ),
            (
                "step_execution",
                Either(
                    (
                        RecordRef("correlated_step_execution_assessment"),
                        type(None),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "installation_destination",
        InstallationDestination,
        (
            (
                "kind",
                LiteralValues(
                    (
                        "manager_environment_scheme",
                        "target_directory",
                        "user_scheme",
                        "prefix_scheme",
                        "root_relocated_scheme",
                    )
                ),
            ),
            (
                "value",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "installation_destination_fact",
        InstallationDestinationFact,
        (
            ("manager", LiteralValues(("pip",))),
            ("command_location", RecordRef("static_command_location")),
            ("destination", RecordRef("installation_destination")),
            ("provenance", RecordRef("package_manager_semantic_resolution_provenance")),
        ),
    ),
    RecordLayout(
        "manager_environment_selection_fact",
        ManagerEnvironmentSelectionFact,
        (
            ("manager", LiteralValues(("pip",))),
            ("command_location", RecordRef("static_command_location")),
            ("environment", RecordRef("package_manager_environment_reference")),
            ("provenance", RecordRef("package_manager_semantic_resolution_provenance")),
        ),
    ),
    RecordLayout(
        "package_manager_environment_reference",
        PackageManagerEnvironmentReference,
        (
            ("kind", LiteralValues(("pip_python_target",))),
            ("value", str),
        ),
    ),
    RecordLayout(
        "package_manager_semantic_problem",
        PackageManagerSemanticProblem,
        (
            ("state", LiteralValues(("unresolved", "unsupported"))),
            (
                "dimension",
                LiteralValues(
                    (
                        "manager_environment",
                        "installation_destination",
                        "package_mutation_mode",
                        "direct_requirement_handling",
                    )
                ),
            ),
            ("reason", str),
            ("detail", str),
            ("command_location", RecordRef("static_command_location")),
            (
                "resolved_prefix",
                SequenceOf(RecordRef("package_manager_semantic_resolution_step")),
            ),
            (
                "blocking_source",
                Either(
                    (
                        LiteralValues(
                            (
                                "command_line",
                                "executable_selection",
                                "process_environment",
                                "persistent_configuration",
                                "manager_default",
                            )
                        ),
                        type(None),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "package_manager_semantic_resolution_provenance",
        PackageManagerSemanticResolutionProvenance,
        (
            (
                "dimension",
                LiteralValues(
                    (
                        "manager_environment",
                        "installation_destination",
                        "package_mutation_mode",
                        "direct_requirement_handling",
                    )
                ),
            ),
            (
                "inspected_sources",
                SequenceOf(RecordRef("package_manager_semantic_resolution_step")),
            ),
            (
                "winning_source",
                LiteralValues(
                    (
                        "command_line",
                        "executable_selection",
                        "process_environment",
                        "persistent_configuration",
                        "manager_default",
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "package_manager_semantic_resolution_step",
        PackageManagerSemanticResolutionStep,
        (
            (
                "source_kind",
                LiteralValues(
                    (
                        "command_line",
                        "executable_selection",
                        "process_environment",
                        "persistent_configuration",
                        "manager_default",
                    )
                ),
            ),
            ("disposition", LiteralValues(("non_overriding", "disabled", "decisive"))),
            ("detail", str),
            (
                "locator",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "package_mutation_mode_fact",
        PackageMutationModeFact,
        (
            ("manager", LiteralValues(("pip",))),
            ("command_location", RecordRef("static_command_location")),
            ("mode", LiteralValues(("apply_changes", "dry_run"))),
            ("provenance", RecordRef("package_manager_semantic_resolution_provenance")),
        ),
    ),
    RecordLayout(
        "requirement_satisfied_at_command_completion",
        RequirementSatisfiedAtCommandCompletion,
        (
            ("dependency", RecordRef("dependency_version_change")),
            ("source_context", RecordRef("requirements_file_dependency_context")),
            ("consumption", RecordRef("static_dependency_consumption_evidence")),
            ("semantics", RecordRef("scoped_package_manager_semantic_evidence")),
            ("execution", RecordRef("exact_command_execution_assessment")),
            ("observation_boundary", LiteralValues(("successful_command_completion",))),
            ("limitations", SequenceOf(str)),
        ),
    ),
    RecordLayout(
        "requirement_state_problem",
        RequirementStateProblem,
        (
            ("state", LiteralValues(("not_established", "unresolved"))),
            ("reason", str),
            ("detail", str),
            (
                "blocking_dimension",
                Either(
                    (
                        LiteralValues(
                            (
                                "manager_environment",
                                "installation_destination",
                                "package_mutation_mode",
                                "direct_requirement_handling",
                            )
                        ),
                        type(None),
                    )
                ),
            ),
            (
                "blocking_semantic_evidence",
                Either(
                    (
                        Either(
                            (
                                RecordRef("manager_environment_selection_fact"),
                                RecordRef("installation_destination_fact"),
                                RecordRef("package_mutation_mode_fact"),
                                RecordRef("direct_requirement_handling_fact"),
                                RecordRef("package_manager_semantic_problem"),
                            )
                        ),
                        type(None),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "runtime_dependency_state_result",
        RuntimeDependencyStateResult,
        (
            ("evaluation_state", LiteralValues(("evaluated", "no_admitted_candidate"))),
            ("reason", str),
            ("detail", str),
            (
                "assessments",
                SequenceOf(RecordRef("command_requirement_state_assessment")),
            ),
        ),
    ),
    RecordLayout(
        "scoped_package_manager_semantic_evidence",
        ScopedPackageManagerSemanticEvidence,
        (
            ("command_identity", RecordRef("exact_ci_command_identity")),
            (
                "manager_environment",
                Either(
                    (
                        RecordRef("manager_environment_selection_fact"),
                        RecordRef("package_manager_semantic_problem"),
                    )
                ),
            ),
            (
                "installation_destination",
                Either(
                    (
                        RecordRef("installation_destination_fact"),
                        RecordRef("package_manager_semantic_problem"),
                    )
                ),
            ),
            (
                "package_mutation_mode",
                Either(
                    (
                        RecordRef("package_mutation_mode_fact"),
                        RecordRef("package_manager_semantic_problem"),
                    )
                ),
            ),
            (
                "direct_requirement_handling",
                Either(
                    (
                        RecordRef("direct_requirement_handling_fact"),
                        RecordRef("package_manager_semantic_problem"),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "static_dependency_consumption_evidence",
        StaticDependencyConsumptionEvidence,
        (
            ("state", LiteralValues(("supported", "not_established", "unresolved"))),
            (
                "mechanism",
                LiteralValues(("direct_requirements", "project_environment")),
            ),
            ("normalized_package", str),
            ("workflow_path", str),
            ("workflow_revision", str),
            ("job_key", str),
            ("step_source_index", int),
            ("command", str),
            ("reason", str),
            ("detail", str),
            (
                "source_path",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
            (
                "reachability_kind",
                Either(
                    (
                        LiteralValues(("direct", "transitive")),
                        type(None),
                    )
                ),
            ),
            ("witness_path", SequenceOf(str)),
            ("conditional_candidate_path", SequenceOf(str)),
            ("unresolved_conditions", SequenceOf(str)),
            (
                "command_location",
                Either(
                    (
                        RecordRef("static_command_location"),
                        type(None),
                    )
                ),
            ),
            (
                "structural_context",
                SequenceOf(
                    LiteralValues(
                        (
                            "straightforward_top_level",
                            "linear_chain",
                            "short_circuit",
                            "conditional",
                            "loop",
                            "pipeline",
                            "function_or_block",
                            "nested_or_subshell",
                            "status_inverted",
                            "asynchronous",
                            "process_substitution",
                        )
                    )
                ),
            ),
            (
                "whole_step_relation",
                Either(
                    (
                        LiteralValues(
                            (
                                "sole_ordinary_top_level_command",
                                "first_ordinary_top_level_command_in_sequential_script",
                            )
                        ),
                        type(None),
                    )
                ),
            ),
            (
                "execution_profile",
                Either(
                    (
                        LiteralValues(
                            (
                                "github_builtin_bash",
                                "github_builtin_sh",
                                "github_builtin_pwsh",
                                "github_builtin_powershell",
                                "github_builtin_cmd",
                                "github_default_non_windows",
                                "github_default_windows",
                                "github_default_container_sh",
                                "custom_shell_template",
                            )
                        ),
                        type(None),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "static_workflow_dependency_problem",
        StaticWorkflowDependencyProblem,
        (
            ("reason", str),
            ("detail", str),
            (
                "job_key",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "workflow_dependency_coverage_input",
        WorkflowDependencyCoverageInput,
        (
            ("run", RecordRef("workflow_run")),
            ("jobs", SequenceOf(RecordRef("workflow_job"))),
            (
                "definition",
                Either(
                    (
                        RecordRef("repository_text_file"),
                        RecordRef("unavailable_repository_file"),
                    )
                ),
            ),
            (
                "project_environment_sources",
                SequenceOf(RecordRef("workflow_project_environment_source")),
            ),
            (
                "project_environment_consumptions",
                SequenceOf(RecordRef("static_dependency_consumption_evidence")),
            ),
        ),
    ),
    RecordLayout(
        "workflow_dependency_coverage_result",
        WorkflowDependencyCoverageResult,
        (
            ("workflow_name", str),
            ("workflow_path", str),
            (
                "state",
                LiteralValues(
                    (
                        "supported_runtime_correlated",
                        "supported_not_correlated",
                        "no_successful_ci",
                        "unresolved",
                    )
                ),
            ),
            ("reason", str),
            ("detail", str),
            (
                "consumption_state",
                LiteralValues(("supported", "not_established", "unresolved")),
            ),
            ("consumption_reason", str),
            ("consumption_detail", str),
            (
                "direct_exercise_state",
                LiteralValues(("supported", "not_established", "unresolved")),
            ),
            ("direct_exercise_reason", str),
            ("direct_exercise_detail", str),
            (
                "runtime_consumption_state",
                LiteralValues(("supported", "not_established", "unresolved")),
            ),
            ("runtime_consumption_reason", str),
            ("runtime_consumption_detail", str),
            (
                "runtime_direct_exercise_state",
                LiteralValues(("supported", "not_established", "unresolved")),
            ),
            ("runtime_direct_exercise_reason", str),
            ("runtime_direct_exercise_detail", str),
            (
                "runtime_correlation",
                Either(
                    (
                        RecordRef("workflow_runtime_correlation_result"),
                        type(None),
                    )
                ),
            ),
            (
                "consumption_command",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
            (
                "execution_command",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
            (
                "consumptions",
                SequenceOf(RecordRef("static_dependency_consumption_evidence")),
            ),
            (
                "invocations",
                SequenceOf(RecordRef("direct_package_invocation_evidence")),
            ),
            ("problems", SequenceOf(RecordRef("static_workflow_dependency_problem"))),
        ),
    ),
    RecordLayout(
        "workflow_project_environment_source",
        WorkflowProjectEnvironmentSource,
        (
            (
                "context",
                Either(
                    (
                        Either(
                            (
                                RecordRef(
                                    "pyproject_optional_extra_dependency_context"
                                ),
                                RecordRef("pyproject_dependency_group_context"),
                            )
                        ),
                        RecordRef("uv_lock_dependency_context"),
                    )
                ),
            ),
            (
                "project_file",
                Either(
                    (
                        RecordRef("repository_text_file"),
                        RecordRef("unavailable_repository_file"),
                    )
                ),
            ),
            (
                "lock_file",
                Either(
                    (
                        Either(
                            (
                                RecordRef("repository_text_file"),
                                RecordRef("unavailable_repository_file"),
                            )
                        ),
                        type(None),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "workflow_runtime_correlation_result",
        WorkflowRuntimeCorrelationResult,
        (
            ("state", LiteralValues(("correlated", "unresolved"))),
            ("reason", str),
            ("detail", str),
            ("jobs", SequenceOf(RecordRef("workflow_runtime_job_correlation"))),
        ),
    ),
    RecordLayout(
        "workflow_runtime_job_correlation",
        WorkflowRuntimeJobCorrelation,
        (
            ("static_job", RecordRef("steps_job_definition")),
            ("runtime_job", RecordRef("workflow_job")),
            ("steps", SequenceOf(RecordRef("workflow_runtime_step_correlation"))),
        ),
    ),
    RecordLayout(
        "workflow_runtime_step_correlation",
        WorkflowRuntimeStepCorrelation,
        (
            (
                "static_step",
                Either(
                    (
                        RecordRef("run_step_definition"),
                        RecordRef("uses_step_definition"),
                    )
                ),
            ),
            ("runtime_step", RecordRef("workflow_step")),
        ),
    ),
)
