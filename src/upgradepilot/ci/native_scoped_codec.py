"""Successor native layouts for retained workflow instances and command addresses."""

from dataclasses import replace

from .workflow_runtime_correlation import (
    ScopedWorkflowRuntimeEvidence,
    UnassignedRuntimeJob,
    UnmatchedWorkflowJobInstance,
    WorkflowJobAssociationBasis,
    WorkflowRuntimeStepProblem,
)
from ..github.workflow_definition import JobProblem, ReusableWorkflowJobDefinition, WorkflowDefinition, WorkflowDefinitionProblem
from ..github.workflow_instance_commands import WorkflowRunScriptIdentity
from ..github.workflow_matrix import MatrixCoordinate, MatrixExpansion, MatrixExpansionProblem, MatrixExpansionRow, MatrixLiteral
from ..github.workflow_specialization import (
    FieldSpecializationProblem,
    MatrixFieldReplacement,
    PreparedWorkflowJob,
    PreparedWorkflowJobInstances,
    SpecializedWorkflowField,
    WorkflowJobInstance,
    WorkflowJobInstanceIdentity,
)
from ..workspace.native_representation import Either, LiteralValues, RecordLayout, RecordRef, SequenceOf


def _optional(shape: object) -> Either:
    return Either((shape, type(None)))


_SOURCE_SPAN = RecordRef("source_span")
_INSTANCE = RecordRef("workflow_job_instance_identity")
_FIELD_PATH = SequenceOf(Either((str, int)))
_COORDINATES = SequenceOf(RecordRef("matrix_coordinate"))
_AXIS_INDICES = _optional(SequenceOf(int))
_MATRIX_LITERAL_KIND = LiteralValues(("string", "integer", "boolean", "null"))
_MATRIX_VALUE = Either((str, int, bool, type(None)))
_EXPANSION_STATE = LiteralValues(("complete", "unresolved", "incomplete"))
_FIELD_PROBLEM = _optional(RecordRef("field_specialization_problem"))
_SPECIALIZED_FIELDS = SequenceOf(RecordRef("specialized_workflow_field"))
_STATIC_VALUE = Either((
    RecordRef("static_scalar_value"),
    RecordRef("static_sequence_value"),
    RecordRef("static_mapping_value"),
    type(None),
))

SCOPED_LAYOUTS = (
    RecordLayout("workflow_job_instance_identity", WorkflowJobInstanceIdentity, (
        ("repository", str), ("revision", str), ("workflow_path", str),
        ("workflow_digest", str), ("job_key", str), ("job_source_index", int),
        ("kind", LiteralValues(("ordinary", "matrix"))), ("expansion_slot", int),
        ("method", str),
    )),
    RecordLayout("workflow_run_script_identity", WorkflowRunScriptIdentity, (
        ("instance", _INSTANCE), ("step_source_index", int), ("script_digest", str),
    )),
    RecordLayout("matrix_literal", MatrixLiteral, (
        ("kind", _MATRIX_LITERAL_KIND), ("value", _MATRIX_VALUE),
        ("spelling", str), ("span", _SOURCE_SPAN),
    )),
    RecordLayout("matrix_coordinate", MatrixCoordinate, (
        ("name", str), ("literal", RecordRef("matrix_literal")), ("name_span", _SOURCE_SPAN),
    )),
    RecordLayout("matrix_expansion_row", MatrixExpansionRow, (
        ("coordinates", _COORDINATES), ("original_axis_indices", _AXIS_INDICES),
        ("include_indices", SequenceOf(int)),
    )),
    RecordLayout("matrix_expansion_problem", MatrixExpansionProblem, (
        ("reason", str), ("detail", str), ("span", _SOURCE_SPAN),
    )),
    RecordLayout("matrix_expansion", MatrixExpansion, (
        ("state", _EXPANSION_STATE), ("rows", SequenceOf(RecordRef("matrix_expansion_row"))),
        ("problem", _optional(RecordRef("matrix_expansion_problem"))),
    )),
    RecordLayout("field_specialization_problem", FieldSpecializationProblem, (
        ("path", _FIELD_PATH), ("reason", str), ("detail", str), ("span", _SOURCE_SPAN),
    )),
    RecordLayout("matrix_field_replacement", MatrixFieldReplacement, (
        ("original_start_byte", int), ("original_end_byte", int),
        ("generated_start_byte", int), ("generated_end_byte", int),
        ("coordinate", RecordRef("matrix_coordinate")),
    )),
    RecordLayout("specialized_workflow_field", SpecializedWorkflowField, (
        ("path", _FIELD_PATH), ("role", LiteralValues(("value", "condition"))),
        ("original_text", str), ("original_span", _SOURCE_SPAN), ("original_digest", str),
        ("state", LiteralValues(("resolved", "unresolved"))),
        ("value_kind", _optional(_MATRIX_LITERAL_KIND)), ("value", _MATRIX_VALUE),
        ("generated_text", _optional(str)), ("generated_digest", _optional(str)),
        ("replacements", SequenceOf(RecordRef("matrix_field_replacement"))),
        ("problem", _FIELD_PROBLEM),
    )),
    RecordLayout("workflow_job_instance", WorkflowJobInstance, (
        ("identity", _INSTANCE), ("coordinates", _COORDINATES),
        ("original_axis_indices", _AXIS_INDICES), ("include_indices", SequenceOf(int)),
        ("fields", _SPECIALIZED_FIELDS),
    )),
    RecordLayout("prepared_workflow_job", PreparedWorkflowJob, (
        ("source_index", int), ("job_key", _optional(str)), ("state", _EXPANSION_STATE),
        ("expansion", _optional(RecordRef("matrix_expansion"))),
        ("instances", SequenceOf(RecordRef("workflow_job_instance"))), ("problem", _FIELD_PROBLEM),
    )),
    RecordLayout("workflow_job_problem", JobProblem, (
        ("source_index", int), ("key", _optional(str)), ("reason", str),
        ("detail", str), ("span", _SOURCE_SPAN),
    )),
    RecordLayout("reusable_workflow_job_definition", ReusableWorkflowJobDefinition, (
        ("source_index", int), ("key", str), ("name", _optional(RecordRef("static_scalar_value"))),
        ("needs", _STATIC_VALUE), ("condition", _optional(RecordRef("static_scalar_value"))),
        ("uses", RecordRef("static_scalar_value")),
        ("with_inputs", _optional(RecordRef("static_mapping_value"))), ("span", _SOURCE_SPAN),
    )),
    RecordLayout("workflow_definition", WorkflowDefinition, (
        ("source", RecordRef("repository_text_file")),
        ("run_defaults", _optional(RecordRef("run_defaults"))),
        ("jobs", SequenceOf(Either((
            RecordRef("steps_job_definition"),
            RecordRef("reusable_workflow_job_definition"),
            RecordRef("workflow_job_problem"),
        )))),
        ("environment", _optional(RecordRef("static_mapping_value"))),
    )),
    RecordLayout("workflow_definition_problem", WorkflowDefinitionProblem, (
        ("source", RecordRef("repository_text_file")), ("reason", str), ("detail", str),
        ("span", _optional(_SOURCE_SPAN)),
    )),
    RecordLayout("prepared_workflow_job_instances", PreparedWorkflowJobInstances, (
        ("definition", Either((RecordRef("workflow_definition"), RecordRef("workflow_definition_problem")))),
        ("workflow_fields", _SPECIALIZED_FIELDS),
        ("jobs", SequenceOf(RecordRef("prepared_workflow_job"))),
        ("method", str), ("problem", _FIELD_PROBLEM),
    )),
)

_SUCCESSOR_FIELDS = {
    "static_command_location": ("script_identity", _optional(RecordRef("workflow_run_script_identity"))),
    "workflow_dependency_coverage_input": ("prepared", _optional(RecordRef("prepared_workflow_job_instances"))),
    "static_dependency_consumption_evidence": ("job_instance", _optional(_INSTANCE)),
    "direct_package_invocation_evidence": ("job_instance", _optional(_INSTANCE)),
    "static_workflow_dependency_problem": ("job_instance", _optional(_INSTANCE)),
    "workflow_runtime_job_correlation": ("job_instance", _optional(_INSTANCE)),
    "workflow_runtime_step_correlation": ("job_instance", _optional(_INSTANCE)),
}


def scoped_ci_layouts(historical: tuple[RecordLayout, ...]) -> tuple[RecordLayout, ...]:
    """Use the successor fields only in the three versioned CI family roots."""
    return tuple(
        replace(
            layout,
            fields=layout.fields + (_SUCCESSOR_FIELDS[layout.variant],),
            omitted_none_fields=tuple(
                name for name in layout.omitted_none_fields
                if name != _SUCCESSOR_FIELDS[layout.variant][0]
            ),
        )
        if layout.variant in _SUCCESSOR_FIELDS else layout
        for layout in historical
    ) + SCOPED_LAYOUTS


_ASSOCIATION_LAYOUTS = (
    RecordLayout("workflow_runtime_step_problem", WorkflowRuntimeStepProblem, (
        ("source_index", int), ("reason", str),
    )),
    RecordLayout("workflow_job_association_basis", WorkflowJobAssociationBasis, (
        ("explicit_job_name", _optional(str)),
        ("witness_step_numbers", SequenceOf(int)),
        ("step_problems", SequenceOf(RecordRef("workflow_runtime_step_problem"))),
    )),
    RecordLayout("unmatched_workflow_job_instance", UnmatchedWorkflowJobInstance, (
        ("instance", _INSTANCE), ("reason", str), ("candidate_job_ids", SequenceOf(int)),
    )),
    RecordLayout("unassigned_runtime_job", UnassignedRuntimeJob, (
        ("job", RecordRef("workflow_job")), ("reason", str),
        ("candidate_instances", SequenceOf(_INSTANCE)),
    )),
    RecordLayout("scoped_workflow_runtime_evidence", ScopedWorkflowRuntimeEvidence, (
        ("run_id", int), ("run_attempt", int), ("head_sha", str),
        ("unmatched_instances", SequenceOf(RecordRef("unmatched_workflow_job_instance"))),
        ("unassigned_jobs", SequenceOf(RecordRef("unassigned_runtime_job"))),
        ("unresolved_source_jobs", SequenceOf(int)),
    )),
)


def association_ci_layouts(scoped: tuple[RecordLayout, ...]) -> tuple[RecordLayout, ...]:
    """Coverage v5 retains associations and their independent step outcomes."""
    layouts = []
    for layout in scoped:
        if layout.variant == "workflow_runtime_correlation_result_v3":
            layout = replace(
                layout,
                fields=(
                    ("state", LiteralValues((
                        "correlated", "correlated_with_skipped_jobs", "partially_correlated", "unresolved",
                    ))),
                ) + layout.fields[1:] + (
                    ("scoped", _optional(RecordRef("scoped_workflow_runtime_evidence"))),
                ),
                omitted_none_fields=(),
            )
        elif layout.variant == "workflow_runtime_job_correlation":
            layout = replace(
                layout, fields=layout.fields + (
                    ("association", _optional(RecordRef("workflow_job_association_basis"))),
                ),
                omitted_none_fields=(),
            )
        layouts.append(layout)
    return tuple(layouts) + _ASSOCIATION_LAYOUTS
