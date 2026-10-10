"""Fixed version-1 layouts for retained identity, source and upstream/target inputs.

These representations support the native CI/impact capture closure. They reconstruct
retained values without calling source acquisition, interpretation or evaluation. Layouts
are explicit; new fields/variants require reviewed compatibility and refusal proof."""

from __future__ import annotations

from datetime import datetime

from packaging.version import Version

from upgradepilot.dependency.change import (
    DependencyChangeProblem,
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.dependency.environment import (
    ConstraintsFileDependencyContext,
    PyprojectDependencyGroupContext,
    PyprojectOptionalExtraDependencyContext,
    RequirementsFileDependencyContext,
    UvLockDependencyContext,
)
from upgradepilot.github.actions import (
    WorkflowJob,
    WorkflowRun,
    WorkflowStep,
)
from upgradepilot.github.pull_request import (
    ChangedFile,
    PullRequestIdentity,
)
from upgradepilot.github.release import (
    GitHubReleaseEvidence,
)
from upgradepilot.github.repository import (
    RepositoryTextFile,
    UnavailableRepositoryFile,
)
from upgradepilot.github.workflow_command_analysis import (
    CommandSourceSpan,
)
from upgradepilot.github.workflow_command_location import (
    StaticCommandLocation,
)
from upgradepilot.github.workflow_definition import (
    RunDefaults,
    RunStepDefinition,
    SourceSpan,
    StaticMappingEntry,
    StaticMappingValue,
    StaticScalarValue,
    StaticSequenceValue,
    StepProblem,
    StepsJobDefinition,
    UsesStepDefinition,
)
from upgradepilot.target.python import (
    TargetPythonDeclaration,
    TargetPythonDeclarationProblem,
)
from upgradepilot.target.python_specifier import (
    PythonLineSpecifierEvaluation,
    PythonLineSpecifierProblem,
)
from upgradepilot.target.relevance import (
    TargetPythonRelevanceResult,
)
from upgradepilot.upstream.claim import (
    GroundedPythonSupportDropClaim,
    GroundedUpstreamClaimSource,
    UpstreamSupportDropClaimProblem,
)
from upgradepilot.upstream.interval import (
    AuthoritativeUpstreamIntervalEvidence,
    CrossedReleaseIndexEvidence,
    DependencyReleaseInterval,
    IntervalGitHubReleaseSource,
    PackageMetadataCorroboration,
    TaggedChangelogEvidence,
    UpstreamAuthoritySourceProblem,
    UpstreamIntervalAuthorityProblem,
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
        "authoritative_upstream_interval_evidence",
        AuthoritativeUpstreamIntervalEvidence,
        (
            ("interval", RecordRef("dependency_release_interval")),
            ("repository", str),
            (
                "crossed_releases",
                Either(
                    (
                        RecordRef("crossed_release_index_evidence"),
                        type(None),
                    )
                ),
            ),
            (
                "release_bodies",
                SequenceOf(RecordRef("interval_git_hub_release_source")),
            ),
            (
                "tagged_changelog",
                Either(
                    (
                        RecordRef("tagged_changelog_evidence"),
                        type(None),
                    )
                ),
            ),
            (
                "package_metadata",
                SequenceOf(RecordRef("package_metadata_corroboration")),
            ),
            (
                "source_problems",
                SequenceOf(RecordRef("upstream_authority_source_problem")),
            ),
            (
                "authority_basis",
                LiteralValues(
                    (
                        "complete_release_series",
                        "tagged_changelog",
                        "complete_release_series_and_tagged_changelog",
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "changed_file",
        ChangedFile,
        (
            ("filename", str),
            ("status", str),
            ("additions", int),
            ("deletions", int),
            ("changes", int),
            (
                "patch",
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
        "command_source_span",
        CommandSourceSpan,
        (
            ("start_byte", int),
            ("end_byte", int),
            ("start_line", int),
            ("start_column", int),
            ("end_line", int),
            ("end_column", int),
        ),
    ),
    RecordLayout(
        "constraints_file_dependency_context",
        ConstraintsFileDependencyContext,
        (
            ("repository", str),
            ("revision", str),
            ("normalized_package", str),
            ("source_evidence", RecordRef("dependency_change_source_evidence")),
        ),
    ),
    RecordLayout(
        "crossed_release_index_evidence",
        CrossedReleaseIndexEvidence,
        (
            ("repository", str),
            ("interval", RecordRef("dependency_release_interval")),
            ("ordered_versions", SequenceOf(str)),
            ("source_url", str),
            ("retrieved_at", datetime),
        ),
    ),
    RecordLayout(
        "dependency_change_problem",
        DependencyChangeProblem,
        (
            (
                "reason",
                LiteralValues(
                    (
                        "no_supported_dependency_file",
                        "missing_dependency_patch",
                        "incomplete_dependency_patch",
                        "unsupported_requirement_format",
                        "unsupported_dependency_file_status",
                        "dependency_file_unavailable",
                        "dependency_file_too_large",
                        "malformed_dependency_file",
                        "invalid_dependency_record",
                        "unsupported_uv_lock_schema",
                        "unsupported_uv_lock_structural_change",
                        "ambiguous_uv_lock_package_records",
                        "unsupported_pyproject_optional_dependency_change",
                        "ambiguous_pyproject_dependency_records",
                        "version_unchanged",
                        "multiple_dependency_version_changes",
                        "conflicting_dependency_version_changes",
                    )
                ),
            ),
            ("detail", str),
            (
                "source_evidence",
                SequenceOf(RecordRef("dependency_change_source_evidence")),
            ),
        ),
    ),
    RecordLayout(
        "dependency_change_source_evidence",
        DependencyChangeSourceEvidence,
        (
            ("path", str),
            (
                "file_format",
                LiteralValues(
                    ("exact_requirement", "uv_lock", "pyproject_optional_extra")
                ),
            ),
            (
                "extraction_method",
                LiteralValues(("changed_file_patch", "exact_base_head_files")),
            ),
        ),
    ),
    RecordLayout(
        "dependency_release_interval",
        DependencyReleaseInterval,
        (
            ("package", str),
            ("normalized_package", str),
            ("old_version", str),
            ("proposed_version", str),
            ("lower_bound_inclusive", LiteralValues((False,))),
            ("upper_bound_inclusive", LiteralValues((True,))),
        ),
        constant_fields=("lower_bound_inclusive", "upper_bound_inclusive"),
    ),
    RecordLayout(
        "dependency_version_change",
        DependencyVersionChange,
        (
            ("package", str),
            ("normalized_package", str),
            ("old_version", str),
            ("proposed_version", str),
            (
                "source_evidence",
                SequenceOf(RecordRef("dependency_change_source_evidence")),
            ),
            ("limitations", SequenceOf(str)),
        ),
    ),
    RecordLayout(
        "git_hub_release_evidence",
        GitHubReleaseEvidence,
        (
            ("state", LiteralValues(("available",))),
            ("repository", str),
            ("requested_tag", str),
            ("release_id", int),
            ("release_url", str),
            (
                "release_name",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
            (
                "body",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
            ("prerelease", bool),
            ("published_at", str),
            ("tag_ref", str),
            ("tag_object_type", str),
            ("tag_object_sha", str),
            ("retrieved_at", datetime),
        ),
        constant_fields=("state",),
    ),
    RecordLayout(
        "grounded_python_support_drop_claim",
        GroundedPythonSupportDropClaim,
        (
            ("python_line", str),
            ("introduced_in_version", str),
            ("interval", RecordRef("dependency_release_interval")),
            (
                "source_evidence",
                SequenceOf(RecordRef("grounded_upstream_claim_source")),
            ),
            ("category", LiteralValues(("support_boundary_change",))),
            ("change_state", LiteralValues(("support_dropped",))),
        ),
        constant_fields=("category", "change_state"),
    ),
    RecordLayout(
        "grounded_upstream_claim_source",
        GroundedUpstreamClaimSource,
        (
            ("source_kind", LiteralValues(("github_release_body", "tagged_changelog"))),
            ("introduced_in_version", str),
            (
                "source",
                Either(
                    (
                        RecordRef("interval_git_hub_release_source"),
                        RecordRef("tagged_changelog_evidence"),
                    )
                ),
            ),
            ("source_quote", str),
            ("quote_start", int),
            ("quote_end", int),
        ),
    ),
    RecordLayout(
        "interval_git_hub_release_source",
        IntervalGitHubReleaseSource,
        (
            ("release_version", str),
            ("release", RecordRef("git_hub_release_evidence")),
        ),
    ),
    RecordLayout(
        "package_metadata_corroboration",
        PackageMetadataCorroboration,
        (
            ("package", str),
            ("normalized_package", str),
            ("release_version", str),
            ("source_url", str),
            (
                "requires_python",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
            ("retrieved_at", datetime),
        ),
    ),
    RecordLayout(
        "pull_request_identity",
        PullRequestIdentity,
        (
            ("repository", str),
            ("number", int),
            ("title", str),
            ("state", str),
            ("merged", bool),
            ("author", str),
            ("base_ref", str),
            ("base_sha", str),
            ("head_ref", str),
            ("head_sha", str),
            ("changed_files", int),
        ),
    ),
    RecordLayout(
        "pyproject_dependency_group_context",
        PyprojectDependencyGroupContext,
        (
            ("repository", str),
            ("revision", str),
            ("normalized_package", str),
            ("source_evidence", RecordRef("dependency_change_source_evidence")),
            ("group", str),
        ),
    ),
    RecordLayout(
        "pyproject_optional_extra_dependency_context",
        PyprojectOptionalExtraDependencyContext,
        (
            ("repository", str),
            ("revision", str),
            ("normalized_package", str),
            ("source_evidence", RecordRef("dependency_change_source_evidence")),
            ("extra", str),
            (
                "requirement_marker",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
            ("requirement_extras", SequenceOf(str)),
        ),
    ),
    RecordLayout(
        "python_line_specifier_evaluation",
        PythonLineSpecifierEvaluation,
        (
            ("python_line", str),
            ("requires_python", str),
            ("normalized_requires_python", str),
            ("line_lower_bound", Version),
            ("line_upper_bound", Version),
            ("candidate_versions_checked", SequenceOf(Version)),
            (
                "witness_version",
                Either(
                    (
                        Version,
                        type(None),
                    )
                ),
            ),
            ("contains_stable_release", bool),
        ),
    ),
    RecordLayout(
        "python_line_specifier_problem",
        PythonLineSpecifierProblem,
        (
            (
                "state",
                LiteralValues(
                    (
                        "invalid_python_line",
                        "invalid_requires_python_specifier",
                        "unsupported_requires_python_specifier",
                        "unsatisfiable_requires_python_specifier",
                    )
                ),
            ),
            ("python_line", str),
            ("requires_python", str),
            ("detail", str),
        ),
    ),
    RecordLayout(
        "repository_text_file",
        RepositoryTextFile,
        (
            ("repository", str),
            ("path", str),
            ("revision", str),
            ("content", str),
        ),
    ),
    RecordLayout(
        "requirements_file_dependency_context",
        RequirementsFileDependencyContext,
        (
            ("repository", str),
            ("revision", str),
            ("normalized_package", str),
            ("source_evidence", RecordRef("dependency_change_source_evidence")),
        ),
    ),
    RecordLayout(
        "run_defaults",
        RunDefaults,
        (
            (
                "shell",
                Either(
                    (
                        RecordRef("static_scalar_value"),
                        type(None),
                    )
                ),
            ),
            (
                "working_directory",
                Either(
                    (
                        RecordRef("static_scalar_value"),
                        type(None),
                    )
                ),
            ),
            ("span", RecordRef("source_span")),
        ),
    ),
    RecordLayout(
        "run_step_definition",
        RunStepDefinition,
        (
            ("source_index", int),
            ("command", RecordRef("static_scalar_value")),
            (
                "name",
                Either(
                    (
                        RecordRef("static_scalar_value"),
                        type(None),
                    )
                ),
            ),
            (
                "condition",
                Either(
                    (
                        RecordRef("static_scalar_value"),
                        type(None),
                    )
                ),
            ),
            (
                "continue_on_error",
                Either(
                    (
                        RecordRef("static_scalar_value"),
                        type(None),
                    )
                ),
            ),
            (
                "shell",
                Either(
                    (
                        RecordRef("static_scalar_value"),
                        type(None),
                    )
                ),
            ),
            (
                "working_directory",
                Either(
                    (
                        RecordRef("static_scalar_value"),
                        type(None),
                    )
                ),
            ),
            ("span", RecordRef("source_span")),
            (
                "environment",
                Either(
                    (
                        RecordRef("static_mapping_value"),
                        type(None),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "source_span",
        SourceSpan,
        (
            ("start_line", int),
            ("start_column", int),
            ("end_line", int),
            ("end_column", int),
        ),
    ),
    RecordLayout(
        "static_command_location",
        StaticCommandLocation,
        (
            ("source_span", RecordRef("command_source_span")),
            ("source_order", int),
        ),
    ),
    RecordLayout(
        "static_mapping_entry",
        StaticMappingEntry,
        (
            ("key", RecordRef("static_scalar_value")),
            (
                "value",
                Either(
                    (
                        RecordRef("static_scalar_value"),
                        RecordRef("static_sequence_value"),
                        RecordRef("static_mapping_value"),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "static_mapping_value",
        StaticMappingValue,
        (
            ("entries", SequenceOf(RecordRef("static_mapping_entry"))),
            ("span", RecordRef("source_span")),
        ),
    ),
    RecordLayout(
        "static_scalar_value",
        StaticScalarValue,
        (
            ("text", str),
            ("contains_expression", bool),
            ("span", RecordRef("source_span")),
        ),
    ),
    RecordLayout(
        "static_sequence_value",
        StaticSequenceValue,
        (
            (
                "items",
                SequenceOf(
                    Either(
                        (
                            RecordRef("static_scalar_value"),
                            RecordRef("static_sequence_value"),
                            RecordRef("static_mapping_value"),
                        )
                    )
                ),
            ),
            ("span", RecordRef("source_span")),
        ),
    ),
    RecordLayout(
        "step_problem",
        StepProblem,
        (
            ("source_index", int),
            ("reason", str),
            ("detail", str),
            ("span", RecordRef("source_span")),
        ),
    ),
    RecordLayout(
        "steps_job_definition",
        StepsJobDefinition,
        (
            ("source_index", int),
            ("key", str),
            (
                "name",
                Either(
                    (
                        RecordRef("static_scalar_value"),
                        type(None),
                    )
                ),
            ),
            (
                "needs",
                Either(
                    (
                        Either(
                            (
                                RecordRef("static_scalar_value"),
                                RecordRef("static_sequence_value"),
                                RecordRef("static_mapping_value"),
                            )
                        ),
                        type(None),
                    )
                ),
            ),
            (
                "runs_on",
                Either(
                    (
                        Either(
                            (
                                RecordRef("static_scalar_value"),
                                RecordRef("static_sequence_value"),
                                RecordRef("static_mapping_value"),
                            )
                        ),
                        type(None),
                    )
                ),
            ),
            (
                "condition",
                Either(
                    (
                        RecordRef("static_scalar_value"),
                        type(None),
                    )
                ),
            ),
            (
                "continue_on_error",
                Either(
                    (
                        RecordRef("static_scalar_value"),
                        type(None),
                    )
                ),
            ),
            (
                "run_defaults",
                Either(
                    (
                        RecordRef("run_defaults"),
                        type(None),
                    )
                ),
            ),
            (
                "strategy",
                Either(
                    (
                        Either(
                            (
                                RecordRef("static_scalar_value"),
                                RecordRef("static_sequence_value"),
                                RecordRef("static_mapping_value"),
                            )
                        ),
                        type(None),
                    )
                ),
            ),
            (
                "container",
                Either(
                    (
                        Either(
                            (
                                RecordRef("static_scalar_value"),
                                RecordRef("static_sequence_value"),
                                RecordRef("static_mapping_value"),
                            )
                        ),
                        type(None),
                    )
                ),
            ),
            (
                "steps",
                SequenceOf(
                    Either(
                        (
                            RecordRef("run_step_definition"),
                            RecordRef("uses_step_definition"),
                            RecordRef("step_problem"),
                        )
                    )
                ),
            ),
            ("span", RecordRef("source_span")),
            (
                "environment",
                Either(
                    (
                        RecordRef("static_mapping_value"),
                        type(None),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "tagged_changelog_evidence",
        TaggedChangelogEvidence,
        (
            ("repository", str),
            ("interval", RecordRef("dependency_release_interval")),
            ("resolved_commit_sha", str),
            ("path", str),
            ("content", str),
        ),
    ),
    RecordLayout(
        "target_python_declaration",
        TargetPythonDeclaration,
        (
            ("path", str),
            ("revision", str),
            ("requires_python", str),
            ("state", LiteralValues(("available",))),
        ),
    ),
    RecordLayout(
        "target_python_declaration_problem",
        TargetPythonDeclarationProblem,
        (
            (
                "state",
                LiteralValues(
                    (
                        "file_unavailable",
                        "malformed_toml",
                        "project_table_absent",
                        "requires_python_absent",
                        "invalid_requires_python",
                    )
                ),
            ),
            ("path", str),
            ("revision", str),
            ("detail", str),
        ),
    ),
    RecordLayout(
        "target_python_relevance_result",
        TargetPythonRelevanceResult,
        (
            (
                "state",
                LiteralValues(
                    (
                        "declared_python_overlap",
                        "outside_declared_python_range",
                        "target_declaration_unresolved",
                        "upstream_claim_unresolved",
                        "comparison_unsupported",
                    )
                ),
            ),
            (
                "upstream_result",
                Either(
                    (
                        RecordRef("grounded_python_support_drop_claim"),
                        RecordRef("upstream_support_drop_claim_problem"),
                    )
                ),
            ),
            (
                "target_evidence",
                Either(
                    (
                        Either(
                            (
                                RecordRef("target_python_declaration"),
                                RecordRef("target_python_declaration_problem"),
                            )
                        ),
                        type(None),
                    )
                ),
            ),
            (
                "specifier_result",
                Either(
                    (
                        Either(
                            (
                                RecordRef("python_line_specifier_evaluation"),
                                RecordRef("python_line_specifier_problem"),
                            )
                        ),
                        type(None),
                    )
                ),
            ),
            ("detail", str),
        ),
    ),
    RecordLayout(
        "unavailable_repository_file",
        UnavailableRepositoryFile,
        (
            ("repository", str),
            ("path", str),
            ("revision", str),
            ("reason", str),
            ("detail", str),
        ),
    ),
    RecordLayout(
        "upstream_authority_source_problem",
        UpstreamAuthoritySourceProblem,
        (
            (
                "source_kind",
                LiteralValues(
                    ("github_release_body", "tagged_changelog", "package_metadata")
                ),
            ),
            (
                "state",
                LiteralValues(
                    (
                        "source_unavailable",
                        "malformed_source",
                        "identity_mismatch",
                        "acquisition_failed",
                    )
                ),
            ),
            ("detail", str),
            (
                "release_version",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
            (
                "path",
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
        "upstream_interval_authority_problem",
        UpstreamIntervalAuthorityProblem,
        (
            (
                "state",
                LiteralValues(
                    (
                        "no_interval_authority",
                        "interval_incomplete",
                        "identity_mismatch",
                        "ambiguous_source",
                        "conflicting_source_identity",
                        "malformed_source",
                        "unsupported_source_authority",
                    )
                ),
            ),
            ("interval", RecordRef("dependency_release_interval")),
            ("repository", str),
            ("detail", str),
            (
                "source_problems",
                SequenceOf(RecordRef("upstream_authority_source_problem")),
            ),
        ),
    ),
    RecordLayout(
        "upstream_support_drop_claim_problem",
        UpstreamSupportDropClaimProblem,
        (
            (
                "state",
                LiteralValues(
                    (
                        "no_support_drop_claim",
                        "candidate_unresolved",
                        "identity_mismatch",
                        "malformed_candidate",
                        "unsupported_claim_category",
                        "unsupported_change_state",
                        "invalid_python_line",
                        "source_not_admitted",
                        "source_identity_unresolved",
                        "source_quote_not_grounded",
                        "release_interval_unresolved",
                        "claim_outside_interval",
                        "multiple_support_drop_claims",
                    )
                ),
            ),
            ("interval", RecordRef("dependency_release_interval")),
            ("detail", str),
        ),
    ),
    RecordLayout(
        "uses_step_definition",
        UsesStepDefinition,
        (
            ("source_index", int),
            ("reference", RecordRef("static_scalar_value")),
            (
                "name",
                Either(
                    (
                        RecordRef("static_scalar_value"),
                        type(None),
                    )
                ),
            ),
            (
                "condition",
                Either(
                    (
                        RecordRef("static_scalar_value"),
                        type(None),
                    )
                ),
            ),
            (
                "continue_on_error",
                Either(
                    (
                        RecordRef("static_scalar_value"),
                        type(None),
                    )
                ),
            ),
            (
                "with_inputs",
                Either(
                    (
                        RecordRef("static_mapping_value"),
                        type(None),
                    )
                ),
            ),
            ("span", RecordRef("source_span")),
            (
                "environment",
                Either(
                    (
                        RecordRef("static_mapping_value"),
                        type(None),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "uv_lock_dependency_context",
        UvLockDependencyContext,
        (
            ("repository", str),
            ("revision", str),
            ("normalized_package", str),
            ("source_evidence", RecordRef("dependency_change_source_evidence")),
        ),
    ),
    RecordLayout(
        "workflow_job",
        WorkflowJob,
        (
            ("job_id", int),
            ("run_id", int),
            ("name", str),
            ("head_sha", str),
            ("status", str),
            (
                "conclusion",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
            (
                "steps",
                Either(
                    (
                        SequenceOf(RecordRef("workflow_step")),
                        type(None),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "workflow_run",
        WorkflowRun,
        (
            ("run_id", int),
            ("workflow_id", int),
            ("name", str),
            ("event", str),
            ("head_sha", str),
            ("status", str),
            (
                "conclusion",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
            ("run_attempt", int),
        ),
    ),
    RecordLayout(
        "workflow_step",
        WorkflowStep,
        (
            ("number", int),
            ("name", str),
            ("status", str),
            (
                "conclusion",
                Either(
                    (
                        str,
                        type(None),
                    )
                ),
            ),
        ),
    ),
)
