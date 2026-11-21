"""Prepare scoped literal job instances without promoting runtime evidence.

Entry point: prepare_workflow_job_instances(RepositoryTextFile). One guarded YAML
composition supplies both the unchanged WorkflowDefinition and narrow matrix syntax.
workflow_matrix owns expansion; this module owns instance addresses and field-level
substitution provenance. Original YAML is never rewritten. Consumers must carry the
instance address before using generated fields in command/runtime interpretation.

Original field spans point into YAML; replacement byte ranges point into decoded
original/generated scalar text. These coordinate spaces deliberately remain separate.
Conditions remain conditions, and neither expansion nor substitution observes execution.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import re
from typing import Iterator, Literal

from yaml.nodes import MappingNode, Node, ScalarNode, SequenceNode

from .repository import RepositoryTextFile
from .workflow_definition import (
    JobProblem, SourceSpan, StepProblem, StepsJobDefinition,
    WorkflowDefinition, WorkflowDefinitionProblem, WorkflowDefinitionResult,
    _parse_workflow_definition_with_syntax, _span,
)
from .workflow_matrix import (
    MATRIX_SPECIALIZATION_METHOD, MatrixCoordinate, MatrixExpansion,
    MatrixExpansionRow, expand_literal_matrix,
)

# Independent of the YAML input bound: substitution can multiply a large literal
# across many fields/instances. Limits stop before retaining a partial field/job.
_MAX_SPECIALIZED_BYTES = 8_000_000
_MAX_SPECIALIZED_FIELD_VISITS = 200_000
_PROPERTY = re.compile(
    r"\s*matrix(?:\.([A-Za-z_][A-Za-z0-9_-]*)|\[\s*'((?:[^']|'')*)'\s*\])\s*",
    re.IGNORECASE | re.ASCII,
)

type FieldPath = tuple[str | int, ...]


@dataclass(frozen=True, slots=True)
class WorkflowJobInstanceIdentity:
    repository: str
    revision: str
    workflow_path: str
    workflow_digest: str
    job_key: str
    job_source_index: int
    kind: Literal["ordinary", "matrix"]
    # Slot is local to this frozen definition, never a runtime scheduling order.
    expansion_slot: int
    method: str = MATRIX_SPECIALIZATION_METHOD


@dataclass(frozen=True, slots=True)
class FieldSpecializationProblem:
    path: FieldPath
    reason: str
    detail: str
    span: SourceSpan


@dataclass(frozen=True, slots=True)
class MatrixFieldReplacement:
    original_start_byte: int
    original_end_byte: int
    generated_start_byte: int
    generated_end_byte: int
    coordinate: MatrixCoordinate


@dataclass(frozen=True, slots=True)
class SpecializedWorkflowField:
    path: FieldPath
    role: Literal["value", "condition"]
    original_text: str
    original_span: SourceSpan
    original_digest: str
    state: Literal["resolved", "unresolved"]
    value_kind: Literal["string", "integer", "boolean", "null"] | None
    value: str | int | bool | None
    # None on unresolved fields, so original dynamic text cannot masquerade as output.
    generated_text: str | None
    generated_digest: str | None
    replacements: tuple[MatrixFieldReplacement, ...]
    problem: FieldSpecializationProblem | None = None


@dataclass(frozen=True, slots=True)
class WorkflowJobInstance:
    identity: WorkflowJobInstanceIdentity
    coordinates: tuple[MatrixCoordinate, ...]
    original_axis_indices: tuple[int, ...] | None
    include_indices: tuple[int, ...]
    fields: tuple[SpecializedWorkflowField, ...]

    def field(self, path: FieldPath) -> SpecializedWorkflowField:
        """Find one retained source field; absent fields are not synthesized defaults."""
        return next(field for field in self.fields if field.path == path)


@dataclass(frozen=True, slots=True)
class PreparedWorkflowJob:
    source_index: int
    job_key: str | None
    state: Literal["complete", "unresolved", "incomplete"]
    expansion: MatrixExpansion | None
    instances: tuple[WorkflowJobInstance, ...]
    problem: FieldSpecializationProblem | None = None


@dataclass(frozen=True, slots=True)
class PreparedWorkflowJobInstances:
    definition: WorkflowDefinitionResult
    workflow_fields: tuple[SpecializedWorkflowField, ...]
    jobs: tuple[PreparedWorkflowJob, ...]
    method: str = MATRIX_SPECIALIZATION_METHOD
    problem: FieldSpecializationProblem | None = None


class _SpecializationLimit(ValueError):
    pass


@dataclass(slots=True)
class _SpecializationBudget:
    bytes: int = 0
    fields: int = 0

    def visit(self) -> None:
        self.fields += 1
        if self.fields > _MAX_SPECIALIZED_FIELD_VISITS:
            raise _SpecializationLimit("Specialization exceeded the field traversal budget.")

    def retain(self, text: str) -> None:
        self.bytes += len(text.encode("utf-8"))
        if self.bytes > _MAX_SPECIALIZED_BYTES:
            raise _SpecializationLimit("Specialization exceeded the generated-text byte budget.")


def prepare_workflow_job_instances(source: RepositoryTextFile) -> PreparedWorkflowJobInstances:
    """Retain the base definition and all admitted ordinary/matrix contexts.

    Expansion completeness and field resolution are independent. An unsupported run
    expression need not erase another readable field or the declared combinations.
    Resource refusal is atomic for the affected job.
    """
    return _prepare_workflow_job_instances(*_parse_workflow_definition_with_syntax(source))


def prepare_matrix_workflow_job_instances(
    source: RepositoryTextFile,
) -> PreparedWorkflowJobInstances | None:
    """Prepare strategy-bearing workflows and preserve ordinary CI interpretation elsewhere."""
    definition, root = _parse_workflow_definition_with_syntax(source)
    if not isinstance(definition, WorkflowDefinition) or not any(
        isinstance(job, StepsJobDefinition) and job.strategy is not None
        for job in definition.jobs
    ):
        return None
    return _prepare_workflow_job_instances(definition, root)


def _prepare_workflow_job_instances(
    definition: WorkflowDefinitionResult, root: Node | None,
) -> PreparedWorkflowJobInstances:
    if isinstance(definition, WorkflowDefinitionProblem):
        return PreparedWorkflowJobInstances(definition, (), ())
    assert isinstance(root, MappingNode)
    source = definition.source
    root_fields = _fields(root)
    jobs_node = root_fields["jobs"]
    assert isinstance(jobs_node, MappingNode)
    budget = _SpecializationBudget()
    workflow_fields = []
    # Workflow env/defaults do not admit matrix. Other contexts stay unresolved;
    # workflow defaults admit no expressions at all.
    try:
        for name in ("env", "defaults"):
            if name in root_fields:
                workflow_fields.extend(_specialize_tree(root_fields[name], (name,), (), False, budget))
    except _SpecializationLimit as exc:
        problem = FieldSpecializationProblem((), "workflow_specialization_limit", str(exc), _span(root))
        return PreparedWorkflowJobInstances(definition, (), (), problem=problem)
    workflow_digest = _digest(source.content)
    jobs = []
    for job, (_, node) in zip(definition.jobs, jobs_node.value, strict=True):
        if not isinstance(job, StepsJobDefinition):
            reason = job.reason if isinstance(job, JobProblem) else "reusable_workflow_specialization_unsupported"
            detail = job.detail if isinstance(job, JobProblem) else "Reusable workflow calls retain their original definition."
            jobs.append(PreparedWorkflowJob(job.source_index, job.key, "unresolved", None, (),
                FieldSpecializationProblem((), reason, detail, job.span)))
            continue
        assert isinstance(node, MappingNode)
        raw = _fields(node)
        expansion = expand_literal_matrix(raw["strategy"], source.content) if "strategy" in raw else None
        if expansion is not None and expansion.state != "complete":
            jobs.append(PreparedWorkflowJob(job.source_index, job.key, expansion.state, expansion, ()))
            continue
        rows = expansion.rows if expansion is not None else (MatrixExpansionRow((), None),)
        instances = []
        try:
            for slot, row in enumerate(rows):
                identity = WorkflowJobInstanceIdentity(source.repository, source.revision, source.path,
                    workflow_digest, job.key, job.source_index,
                    "matrix" if expansion is not None else "ordinary", slot)
                fields = tuple(_specialize_job_fields(node, job, row.coordinates, budget))
                instances.append(WorkflowJobInstance(identity, row.coordinates,
                    row.original_axis_indices, row.include_indices, fields))
        except _SpecializationLimit as exc:
            jobs.append(PreparedWorkflowJob(job.source_index, job.key, "incomplete", expansion, (),
                FieldSpecializationProblem((), "workflow_specialization_limit", str(exc), job.span)))
            continue
        jobs.append(PreparedWorkflowJob(job.source_index, job.key, "complete", expansion, tuple(instances)))
    return PreparedWorkflowJobInstances(definition, tuple(workflow_fields), tuple(jobs))


def _fields(node: MappingNode) -> dict[str, Node]:
    return {key.value: value for key, value in node.value if isinstance(key, ScalarNode)}


def _specialize_job_fields(
    node: MappingNode,
    job: StepsJobDefinition,
    coordinates: tuple[MatrixCoordinate, ...],
    budget: _SpecializationBudget,
) -> Iterator[SpecializedWorkflowField]:
    for key, value in node.value:
        budget.visit()
        assert isinstance(key, ScalarNode)
        name = key.value
        if name == "strategy" and isinstance(value, MappingNode):
            # Scheduling controls remain independent of the matrix coordinates.
            for strategy_key, strategy_value in value.value:
                if isinstance(strategy_key, ScalarNode) and strategy_key.value != "matrix":
                    yield from _specialize_tree(strategy_value, ("strategy", strategy_key.value),
                        coordinates, False, budget, boolean=strategy_key.value == "fail-fast")
            continue
        if name == "steps" and isinstance(value, SequenceNode):
            for index, step in enumerate(value.value):
                budget.visit()
                if isinstance(job.steps[index], StepProblem):
                    continue  # StepProblem remains in the original definition.
                assert isinstance(step, MappingNode)
                for step_key, step_value in step.value:
                    budget.visit()
                    if not isinstance(step_key, ScalarNode):
                        continue
                    field = step_key.value
                    if field in {"name", "run", "shell", "working-directory", "env", "with",
                                 "continue-on-error", "if", "uses"}:
                        yield from _specialize_tree(step_value, ("steps", index, field), coordinates,
                            field != "uses", budget, condition=field == "if",
                            boolean=field == "continue-on-error")
        elif name in {"name", "runs-on", "env", "container", "defaults", "continue-on-error", "if", "needs"}:
            # Job if precedes expansion; needs does not admit matrix context.
            yield from _specialize_tree(value, (name,), coordinates, name not in {"if", "needs"},
                budget, condition=name == "if", boolean=name == "continue-on-error")


def _specialize_tree(node: Node, path: FieldPath, coordinates: tuple[MatrixCoordinate, ...],
                     matrix_allowed: bool, budget: _SpecializationBudget, *,
                     condition: bool = False, boolean: bool = False,
) -> Iterator[SpecializedWorkflowField]:
    budget.visit()
    if isinstance(node, ScalarNode):
        yield _specialize_scalar(node, path, coordinates, matrix_allowed, budget,
                                 condition=condition, boolean=boolean)
    elif isinstance(node, SequenceNode):
        for index, child in enumerate(node.value):
            yield from _specialize_tree(child, path + (index,), coordinates, matrix_allowed, budget)
    elif isinstance(node, MappingNode):
        counts: dict[str, int] = {}
        for key, _ in node.value:
            if isinstance(key, ScalarNode):
                counts[key.value.casefold()] = counts.get(key.value.casefold(), 0) + 1
        for key, child in node.value:
            budget.visit()
            if not isinstance(key, ScalarNode):
                continue  # Invalid structural keys are retained as base definition problems.
            name = key.value
            if counts[name.casefold()] > 1 or "${{" in name:
                # Keep an explicit refusal at the key; no generated value for that entry.
                yield _unresolved_field(key, path + (name,), False, "specialization_mapping_key_unsupported",
                                        "Duplicate or dynamic mapping keys cannot be specialized.")
                continue
            yield from _specialize_tree(child, path + (name,), coordinates, matrix_allowed, budget)


def _unresolved_field(node: ScalarNode, path: FieldPath, condition: bool,
                      reason: str, detail: str) -> SpecializedWorkflowField:
    return SpecializedWorkflowField(path, "condition" if condition else "value", node.value,
        _span(node), _digest(node.value), "unresolved", None, None, None, None, (),
        FieldSpecializationProblem(path, reason, detail, _span(node)))


def _scalar_text(coordinate: MatrixCoordinate) -> str | None:
    literal = coordinate.literal
    if literal.kind == "null":
        return ""
    if literal.kind == "boolean":
        return "true" if literal.value else "false"
    if literal.kind == "integer":
        # Provider scientific formatting outside this range is not qualified yet.
        if abs(int(literal.value)) >= 10**21:
            return None
    return str(literal.value)


def _specialize_scalar(node: ScalarNode, path: FieldPath, coordinates: tuple[MatrixCoordinate, ...],
                       matrix_allowed: bool, budget: _SpecializationBudget, *,
                       condition: bool, boolean: bool) -> SpecializedWorkflowField:
    original = node.value
    if condition and "${{" not in original:
        return _unresolved_field(node, path, True, "condition_not_evaluated",
                                 "Implicit condition expressions retain their original meaning.")
    values = {item.name.casefold(): item for item in coordinates}
    pieces = []
    replacements = []
    cursor = 0
    generated_bytes = 0
    original_bytes = 0
    direct = None
    # Locate occurrences in ORIGINAL text only. Inserted expression-looking values
    # are inert output and are never recursively interpreted.
    while (start := original.find("${{", cursor)) != -1:
        budget.visit()
        end = _expression_end(original, start + 3)
        if end is None:
            return _unresolved_field(node, path, condition, "matrix_expression_unterminated", "Expression has no qualified closing delimiter.")
        expression = original[start + 3:end]
        match = _PROPERTY.fullmatch(expression)
        if match is None:
            return _unresolved_field(node, path, condition, "matrix_expression_unsupported", "Only direct matrix property access is qualified.")
        if not matrix_allowed:
            return _unresolved_field(node, path, condition, "matrix_context_not_allowed", "This provider field does not admit matrix context.")
        name = match.group(1) if match.group(1) is not None else match.group(2).replace("''", "'")
        coordinate = values.get(name.casefold())
        if coordinate is None:
            return _unresolved_field(node, path, condition, "matrix_property_missing", f"No declared matrix property {name!r} exists in this instance.")
        rendered = _scalar_text(coordinate)
        if rendered is None:
            return _unresolved_field(node, path, condition, "matrix_scalar_conversion_unsupported", "Numeric text conversion outside the qualified range remains unresolved.")
        prefix = original[cursor:start]
        pieces.append(prefix)
        prefix_bytes = len(prefix.encode("utf-8"))
        generated_bytes += prefix_bytes
        original_start = original_bytes + prefix_bytes
        generated_start = generated_bytes
        # Charge before allocation/join, including a very large replacement value.
        budget.retain(prefix)
        budget.retain(rendered)
        pieces.append(rendered)
        generated_bytes += len(rendered.encode("utf-8"))
        end += 2
        original_bytes = original_start + len(original[start:end].encode("utf-8"))
        replacements.append(MatrixFieldReplacement(original_start, original_bytes,
            generated_start, generated_bytes, coordinate))
        if start == 0 and end == len(original):
            direct = coordinate.literal
        cursor = end
    tail = original[cursor:]
    budget.retain(tail)
    pieces.append(tail)
    generated = "".join(pieces)
    kind, value = "string", generated
    if boolean or condition:
        if direct is not None:
            kind, value = direct.kind, direct.value
        elif not replacements and node.style is None and original.lower() in {"true", "false"}:
            kind, value = "boolean", original.lower() == "true"
        if boolean and kind != "boolean":
            return _unresolved_field(node, path, condition, "specialized_boolean_required", "Error-handling fields require a qualified boolean value.")
    return SpecializedWorkflowField(path, "condition" if condition else "value", original,
        _span(node), _digest(original), "resolved", kind, value, generated, _digest(generated), tuple(replacements))


def _expression_end(text: str, start: int) -> int | None:
    # Single-quoted property keys may contain literal braces and escaped quotes.
    quoted = False
    index = start
    while index < len(text) - 1:
        if text[index] == "'":
            if quoted and text[index + 1] == "'":
                index += 2
                continue
            quoted = not quoted
        elif not quoted and text[index:index + 2] == "}}":
            return index
        index += 1
    return None


def _digest(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()
