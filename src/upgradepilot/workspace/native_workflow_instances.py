"""Validate retained workflow instance references without parsing or expanding YAML."""

from hashlib import sha256

from ..github.repository import RepositoryFileEvidence
from ..github.workflow_command_location import StaticCommandLocation
from ..github.workflow_definition import RunStepDefinition, StepsJobDefinition, WorkflowDefinition
from ..github.workflow_instance_commands import run_script_identity
from ..github.workflow_matrix import MATRIX_SPECIALIZATION_METHOD, MAX_MATRIX_JOBS
from ..github.workflow_specialization import (
    PreparedWorkflowJobInstances,
    SpecializedWorkflowField,
    WorkflowJobInstance,
    WorkflowJobInstanceIdentity,
)
from .native_representation import NativeReconstructionError


def _require(condition: bool, detail: str) -> None:
    if not condition:
        raise NativeReconstructionError("invalid_native_material", detail)


def _validate_field(field: SpecializedWorkflowField, instance: WorkflowJobInstance | None) -> None:
    original = field.original_text.encode("utf-8")
    _require(
        field.original_digest == sha256(original).hexdigest(),
        "Specialized field has another original text digest.",
    )
    if field.state == "unresolved":
        _require(
            field.generated_text is None and field.generated_digest is None
            and field.value_kind is None and field.value is None and not field.replacements
            and field.problem is not None and field.problem.path == field.path
            and field.problem.span == field.original_span,
            "Unresolved field contains generated evidence or has no owning problem.",
        )
        return
    _require(
        field.generated_text is not None and field.problem is None,
        "Resolved field lacks its retained generated text.",
    )
    assert field.generated_text is not None
    generated = field.generated_text.encode("utf-8")
    _require(
        field.generated_digest == sha256(generated).hexdigest(),
        "Specialized field has another generated text digest.",
    )
    scalar_types = {"string": str, "integer": int, "boolean": bool, "null": type(None)}
    _require(
        field.value_kind in scalar_types and type(field.value) is scalar_types[field.value_kind],
        "Specialized field has another scalar kind.",
    )
    if field.value_kind == "string":
        _require(field.value == field.generated_text, "Specialized string differs from its generated text.")
    old_cursor = new_cursor = 0
    for replacement in field.replacements:
        old_start, old_end = replacement.original_start_byte, replacement.original_end_byte
        new_start, new_end = replacement.generated_start_byte, replacement.generated_end_byte
        _require(
            instance is not None and replacement.coordinate in instance.coordinates
            and old_cursor <= old_start < old_end <= len(original)
            and new_cursor <= new_start <= new_end <= len(generated)
            and original[old_cursor:old_start] == generated[new_cursor:new_start]
            and original[old_start:old_end].startswith(b"${{")
            and original[old_start:old_end].endswith(b"}}"),
            "Specialized field replacement is outside its retained coordinate or byte basis.",
        )
        literal = replacement.coordinate.literal
        expected = (
            "" if literal.kind == "null"
            else "true" if literal.kind == "boolean" and literal.value
            else "false" if literal.kind == "boolean"
            else str(literal.value)
        )
        _require(
            generated[new_start:new_end] == expected.encode("utf-8"),
            "Replacement bytes differ from the retained coordinate value.",
        )
        old_cursor, new_cursor = old_end, new_end
    _require(
        original[old_cursor:] == generated[new_cursor:],
        "Generated field changes text outside the retained replacement ranges.",
    )


def validate_prepared_workflow(
    prepared: PreparedWorkflowJobInstances,
    source: RepositoryFileEvidence,
) -> dict[WorkflowJobInstanceIdentity, WorkflowJobInstance]:
    """Check retained source membership, declaration slots and script material."""
    _require(
        prepared.definition.source == source and prepared.method == MATRIX_SPECIALIZATION_METHOD,
        "Prepared instances have another workflow source or specialization method.",
    )
    definition = prepared.definition
    if not isinstance(definition, WorkflowDefinition) or prepared.problem is not None:
        _require(not prepared.jobs and not prepared.workflow_fields,
                 "A refused workflow has retained positive specialization material.")
        return {}
    digest = sha256(definition.source.content.encode("utf-8")).hexdigest()
    _require(len(definition.jobs) == len(prepared.jobs), "Prepared job inventory is incomplete.")
    for field in prepared.workflow_fields:
        _validate_field(field, None)
    instances = {}
    for index, (job, prepared_job) in enumerate(zip(definition.jobs, prepared.jobs, strict=True)):
        _require(
            (job.source_index, job.key) == (prepared_job.source_index, prepared_job.job_key)
            and job.source_index == index,
            "Prepared job differs from its retained source occurrence.",
        )
        if prepared_job.state != "complete":
            expansion = prepared_job.expansion
            _require(
                not prepared_job.instances and (
                    prepared_job.problem is not None
                    or (expansion is not None and expansion.problem is not None
                        and expansion.state == prepared_job.state and not expansion.rows)
                ),
                "A refused job lacks its problem or retains positive instances.",
            )
            continue
        _require(isinstance(job, StepsJobDefinition), "A prepared instance lacks a steps job.")
        assert isinstance(job, StepsJobDefinition)
        expansion = prepared_job.expansion
        _require(prepared_job.problem is None, "A complete job has a refusal problem.")
        if expansion is None:
            _require(job.strategy is None and len(prepared_job.instances) == 1,
                     "Ordinary context cannot substitute for a matrix or a missing instance.")
        else:
            _require(
                job.strategy is not None and expansion.state == "complete"
                and expansion.problem is None
                and len(expansion.rows) == len(prepared_job.instances) <= MAX_MATRIX_JOBS,
                "Matrix instances do not match the retained expansion.",
            )
        for slot, instance in enumerate(prepared_job.instances):
            expected = WorkflowJobInstanceIdentity(
                source.repository, source.revision, source.path, digest, job.key,
                index, "ordinary" if expansion is None else "matrix", slot,
            )
            _require(instance.identity == expected, "Job instance has another source or slot.")
            if expansion is None:
                _require(
                    not instance.coordinates and instance.original_axis_indices is None
                    and not instance.include_indices,
                    "Ordinary instance contains matrix coordinates or expansion provenance.",
                )
            else:
                row = expansion.rows[slot]
                _require(
                    (instance.coordinates, instance.original_axis_indices, instance.include_indices)
                    == (row.coordinates, row.original_axis_indices, row.include_indices),
                    "Job instance differs from its retained expansion row.",
                )
            _require(
                len({c.name.casefold() for c in instance.coordinates}) == len(instance.coordinates)
                and all(c.name and type(c.literal.value) is {
                    "string": str, "integer": int, "boolean": bool, "null": type(None),
                }[c.literal.kind] for c in instance.coordinates),
                "Matrix coordinates have duplicate names or different literal kinds.",
            )
            run_steps = {
                ("steps", step.source_index, "run"): step
                for step in job.steps if isinstance(step, RunStepDefinition)
            }
            seen_run_fields = set()
            resolved_paths = set()
            for field in instance.fields:
                _validate_field(field, instance)
                if field.state == "resolved":
                    _require(field.path not in resolved_paths, "Specialized field is repeated.")
                    resolved_paths.add(field.path)
                if len(field.path) == 3 and field.path[0] == "steps" and field.path[2] == "run":
                    step = run_steps.get(field.path)
                    _require(
                        step is not None and field.path not in seen_run_fields
                        and (field.original_text, field.original_span)
                        == (step.command.text, step.command.span),
                        "Specialized run template differs from its original source step.",
                    )
                    seen_run_fields.add(field.path)
            _require(seen_run_fields == run_steps.keys(), "Prepared instance omits a run template.")
            instances[instance.identity] = instance
    return instances


def validate_scoped_command(
    instances: dict[WorkflowJobInstanceIdentity, WorkflowJobInstance],
    *,
    owner: WorkflowJobInstanceIdentity | None,
    job_key: str,
    step_source_index: int,
    command: str,
    location: StaticCommandLocation | None,
    occurrence_text: bool = False,
) -> None:
    """Join a recorded command to exact retained generated bytes, without shell parsing."""
    script = location.script_identity if location is not None else None
    instance = instances.get(owner) if owner is not None else None
    _require(instance is not None and instance.identity.job_key == job_key,
             "CI command has no matching retained job instance.")
    assert instance is not None
    expected = run_script_identity(instance, step_source_index)
    _require(
        expected is not None and (location is None or script == expected),
        "CI command has another retained instance, step or script address.",
    )
    field = instance.field(("steps", step_source_index, "run"))
    assert field.generated_text is not None
    text = field.generated_text.encode("utf-8")
    if location is not None:
        span = location.source_span
        _require(
            location.source_order >= 0 and 0 <= span.start_byte < span.end_byte <= len(text),
            "CI command span is outside its retained script.",
        )
        for offset, line, column in (
            (span.start_byte, span.start_line, span.start_column),
            (span.end_byte, span.end_line, span.end_column),
        ):
            before = text[:offset]
            _require(
                (line, column) == (before.count(b"\n"), len(before.rpartition(b"\n")[2])),
                "CI command span has inconsistent byte coordinates.",
            )
        if occurrence_text:
            text = text[span.start_byte:span.end_byte]
    _require(command.encode("utf-8") == text, "CI command differs from its retained script bytes.")
