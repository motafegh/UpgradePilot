"""Bounded static GitHub Actions workflow-definition representation.

PyYAML representation nodes are private syntax machinery. This module translates the
admitted GitHub Actions structure into small typed provider objects that CI and Target
can consume without inheriting parser-library types or each other's domain semantics.
"""

from __future__ import annotations

from dataclasses import dataclass

import yaml
from yaml.nodes import MappingNode, Node, ScalarNode, SequenceNode

from .repository import RepositoryTextFile

_MAX_NODE_VISITS = 50_000
_MAX_NODE_DEPTH = 100


@dataclass(frozen=True, slots=True)
class SourceSpan:
    start_line: int
    start_column: int
    end_line: int
    end_column: int


@dataclass(frozen=True, slots=True)
class StaticScalarValue:
    text: str
    contains_expression: bool
    span: SourceSpan


@dataclass(frozen=True, slots=True)
class StaticSequenceValue:
    items: tuple[GitHubActionsStaticValue, ...]
    span: SourceSpan


@dataclass(frozen=True, slots=True)
class StaticMappingEntry:
    key: StaticScalarValue
    value: GitHubActionsStaticValue


@dataclass(frozen=True, slots=True)
class StaticMappingValue:
    entries: tuple[StaticMappingEntry, ...]
    span: SourceSpan


type GitHubActionsStaticValue = StaticScalarValue | StaticSequenceValue | StaticMappingValue


@dataclass(frozen=True, slots=True)
class RunDefaults:
    shell: StaticScalarValue | None
    working_directory: StaticScalarValue | None
    span: SourceSpan


@dataclass(frozen=True, slots=True)
class RunStepDefinition:
    source_index: int
    command: StaticScalarValue
    name: StaticScalarValue | None
    condition: StaticScalarValue | None
    continue_on_error: StaticScalarValue | None
    shell: StaticScalarValue | None
    working_directory: StaticScalarValue | None
    span: SourceSpan


@dataclass(frozen=True, slots=True)
class UsesStepDefinition:
    source_index: int
    reference: StaticScalarValue
    name: StaticScalarValue | None
    condition: StaticScalarValue | None
    continue_on_error: StaticScalarValue | None
    with_inputs: StaticMappingValue | None
    span: SourceSpan


@dataclass(frozen=True, slots=True)
class StepProblem:
    source_index: int
    reason: str
    detail: str
    span: SourceSpan


type StepEntry = RunStepDefinition | UsesStepDefinition | StepProblem


@dataclass(frozen=True, slots=True)
class StepsJobDefinition:
    source_index: int
    key: str
    name: StaticScalarValue | None
    needs: GitHubActionsStaticValue | None
    runs_on: GitHubActionsStaticValue | None
    condition: StaticScalarValue | None
    continue_on_error: StaticScalarValue | None
    run_defaults: RunDefaults | None
    strategy: GitHubActionsStaticValue | None
    container: GitHubActionsStaticValue | None
    steps: tuple[StepEntry, ...]
    span: SourceSpan


@dataclass(frozen=True, slots=True)
class ReusableWorkflowJobDefinition:
    source_index: int
    key: str
    name: StaticScalarValue | None
    needs: GitHubActionsStaticValue | None
    condition: StaticScalarValue | None
    uses: StaticScalarValue
    with_inputs: StaticMappingValue | None
    span: SourceSpan


@dataclass(frozen=True, slots=True)
class JobProblem:
    source_index: int
    key: str | None
    reason: str
    detail: str
    span: SourceSpan


type JobEntry = StepsJobDefinition | ReusableWorkflowJobDefinition | JobProblem


@dataclass(frozen=True, slots=True)
class WorkflowDefinition:
    source: RepositoryTextFile
    run_defaults: RunDefaults | None
    jobs: tuple[JobEntry, ...]


@dataclass(frozen=True, slots=True)
class WorkflowDefinitionProblem:
    source: RepositoryTextFile
    reason: str
    detail: str
    span: SourceSpan | None = None


type WorkflowDefinitionResult = WorkflowDefinition | WorkflowDefinitionProblem


class WorkflowYamlParseError(ValueError):
    """Untrusted workflow YAML could not be composed/traversed safely."""


class _StructuralIssue(ValueError):
    def __init__(self, reason: str, detail: str, node: Node) -> None:
        super().__init__(detail)
        self.reason = reason
        self.detail = detail
        self.node = node


def parse_workflow_definition(source: RepositoryTextFile) -> WorkflowDefinitionResult:
    """Translate one repository workflow file into the bounded static provider IR."""

    if not source.path.startswith(".github/workflows/") or not source.path.endswith(
        (".yml", ".yaml")
    ):
        return WorkflowDefinitionProblem(
            source=source,
            reason="unsupported_workflow_path",
            detail="Static workflow definitions require a .github/workflows YAML path.",
        )

    try:
        root = _compose_workflow_yaml(source.content)
    except WorkflowYamlParseError as exc:
        return WorkflowDefinitionProblem(
            source=source,
            reason="workflow_yaml_parse_error",
            detail=str(exc),
        )

    if not isinstance(root, MappingNode):
        return WorkflowDefinitionProblem(
            source=source,
            reason="workflow_root_not_mapping",
            detail="GitHub Actions workflow root must be a YAML mapping.",
            span=_span(root) if root is not None else None,
        )

    try:
        root_fields = _unique_material_fields(root, {"defaults", "jobs"})
        jobs_node = root_fields.get("jobs")
        if jobs_node is None:
            return WorkflowDefinitionProblem(
                source=source,
                reason="workflow_jobs_missing",
                detail="GitHub Actions workflow does not declare a jobs mapping.",
                span=_span(root),
            )
        if not isinstance(jobs_node, MappingNode):
            return WorkflowDefinitionProblem(
                source=source,
                reason="workflow_jobs_not_mapping",
                detail="GitHub Actions jobs must be a YAML mapping.",
                span=_span(jobs_node),
            )

        job_pairs = _scalar_mapping_pairs(jobs_node)
        duplicate = _first_duplicate([key.value for key, _ in job_pairs])
        if duplicate is not None:
            return WorkflowDefinitionProblem(
                source=source,
                reason="duplicate_job_id",
                detail=f"Workflow declares duplicate job id {duplicate!r}.",
                span=_span(jobs_node),
            )

        run_defaults = _parse_run_defaults(root_fields.get("defaults"), scope="workflow")
        jobs = tuple(
            _parse_job(source_index, key.value, value)
            for source_index, (key, value) in enumerate(job_pairs)
        )
    except _StructuralIssue as exc:
        return WorkflowDefinitionProblem(
            source=source,
            reason=exc.reason,
            detail=exc.detail,
            span=_span(exc.node),
        )

    return WorkflowDefinition(source=source, run_defaults=run_defaults, jobs=jobs)


def _parse_job(source_index: int, key: str, node: Node) -> JobEntry:
    if not isinstance(node, MappingNode):
        return JobProblem(
            source_index=source_index,
            key=key,
            reason="job_not_mapping",
            detail="Workflow job definition must be a YAML mapping.",
            span=_span(node),
        )

    try:
        fields = _unique_material_fields(
            node,
            {
                "name",
                "needs",
                "runs-on",
                "if",
                "continue-on-error",
                "defaults",
                "strategy",
                "container",
                "steps",
                "uses",
                "with",
            },
        )
        name = _optional_scalar(fields.get("name"), "job name")
        needs = _optional_static_value(fields.get("needs"))
        condition = _optional_scalar(fields.get("if"), "job if")

        uses_node = fields.get("uses")
        steps_node = fields.get("steps")
        if uses_node is not None and steps_node is not None:
            raise _StructuralIssue(
                "ambiguous_job_shape",
                "A job cannot be represented as both a reusable-workflow job and a steps job.",
                node,
            )

        if uses_node is not None:
            return ReusableWorkflowJobDefinition(
                source_index=source_index,
                key=key,
                name=name,
                needs=needs,
                condition=condition,
                uses=_required_scalar(uses_node, "reusable workflow uses"),
                with_inputs=_optional_mapping_value(fields.get("with"), "reusable workflow with"),
                span=_span(node),
            )

        if steps_node is None:
            raise _StructuralIssue(
                "job_steps_missing",
                "A non-reusable workflow job must declare steps.",
                node,
            )
        if not isinstance(steps_node, SequenceNode):
            raise _StructuralIssue(
                "job_steps_not_sequence",
                "Workflow job steps must be a YAML sequence.",
                steps_node,
            )

        return StepsJobDefinition(
            source_index=source_index,
            key=key,
            name=name,
            needs=needs,
            runs_on=_optional_static_value(fields.get("runs-on")),
            condition=condition,
            continue_on_error=_optional_scalar(
                fields.get("continue-on-error"), "job continue-on-error"
            ),
            run_defaults=_parse_run_defaults(fields.get("defaults"), scope=f"job {key!r}"),
            strategy=_optional_static_value(fields.get("strategy")),
            container=_optional_static_value(fields.get("container")),
            steps=tuple(
                _parse_step(step_index, step_node)
                for step_index, step_node in enumerate(steps_node.value)
            ),
            span=_span(node),
        )
    except _StructuralIssue as exc:
        return JobProblem(
            source_index=source_index,
            key=key,
            reason=exc.reason,
            detail=exc.detail,
            span=_span(exc.node),
        )


def _parse_step(source_index: int, node: Node) -> StepEntry:
    if not isinstance(node, MappingNode):
        return StepProblem(
            source_index=source_index,
            reason="step_not_mapping",
            detail="Workflow step must be a YAML mapping.",
            span=_span(node),
        )

    try:
        fields = _unique_material_fields(
            node,
            {
                "name",
                "if",
                "continue-on-error",
                "run",
                "uses",
                "shell",
                "working-directory",
                "with",
            },
        )
        run_node = fields.get("run")
        uses_node = fields.get("uses")
        if (run_node is None) == (uses_node is None):
            raise _StructuralIssue(
                "ambiguous_step_shape",
                "A bounded step must declare exactly one of run or uses.",
                node,
            )

        name = _optional_scalar(fields.get("name"), "step name")
        condition = _optional_scalar(fields.get("if"), "step if")
        continue_on_error = _optional_scalar(
            fields.get("continue-on-error"), "step continue-on-error"
        )
        if run_node is not None:
            return RunStepDefinition(
                source_index=source_index,
                command=_required_scalar(run_node, "step run"),
                name=name,
                condition=condition,
                continue_on_error=continue_on_error,
                shell=_optional_scalar(fields.get("shell"), "step shell"),
                working_directory=_optional_scalar(
                    fields.get("working-directory"), "step working-directory"
                ),
                span=_span(node),
            )

        assert uses_node is not None
        return UsesStepDefinition(
            source_index=source_index,
            reference=_required_scalar(uses_node, "step uses"),
            name=name,
            condition=condition,
            continue_on_error=continue_on_error,
            with_inputs=_optional_mapping_value(fields.get("with"), "step with"),
            span=_span(node),
        )
    except _StructuralIssue as exc:
        return StepProblem(
            source_index=source_index,
            reason=exc.reason,
            detail=exc.detail,
            span=_span(exc.node),
        )


def _parse_run_defaults(node: Node | None, *, scope: str) -> RunDefaults | None:
    if node is None:
        return None
    if not isinstance(node, MappingNode):
        raise _StructuralIssue(
            "defaults_not_mapping",
            f"{scope} defaults must be a YAML mapping.",
            node,
        )

    defaults_fields = _unique_material_fields(node, {"run"})
    run_node = defaults_fields.get("run")
    if run_node is None:
        return None
    if not isinstance(run_node, MappingNode):
        raise _StructuralIssue(
            "run_defaults_not_mapping",
            f"{scope} defaults.run must be a YAML mapping.",
            run_node,
        )

    run_fields = _unique_material_fields(run_node, {"shell", "working-directory"})
    return RunDefaults(
        shell=_optional_scalar(run_fields.get("shell"), f"{scope} default shell"),
        working_directory=_optional_scalar(
            run_fields.get("working-directory"), f"{scope} default working-directory"
        ),
        span=_span(run_node),
    )


def _unique_material_fields(node: MappingNode, names: set[str]) -> dict[str, Node]:
    result: dict[str, Node] = {}
    seen: set[str] = set()
    for key_node, value_node in _scalar_mapping_pairs(node):
        key = key_node.value
        if key not in names:
            continue
        if key in seen:
            raise _StructuralIssue(
                "duplicate_material_key",
                f"Duplicate material key {key!r} would make static interpretation ambiguous.",
                key_node,
            )
        seen.add(key)
        result[key] = value_node
    return result


def _scalar_mapping_pairs(node: MappingNode) -> tuple[tuple[ScalarNode, Node], ...]:
    pairs: list[tuple[ScalarNode, Node]] = []
    for key_node, value_node in node.value:
        if not isinstance(key_node, ScalarNode):
            raise _StructuralIssue(
                "non_scalar_mapping_key",
                "Bounded GitHub Actions mappings require scalar keys.",
                key_node,
            )
        pairs.append((key_node, value_node))
    return tuple(pairs)


def _optional_static_value(node: Node | None) -> GitHubActionsStaticValue | None:
    if node is None:
        return None
    return _static_value(node)


def _static_value(node: Node) -> GitHubActionsStaticValue:
    if isinstance(node, ScalarNode):
        return _scalar_value(node)
    if isinstance(node, SequenceNode):
        return StaticSequenceValue(
            items=tuple(_static_value(item) for item in node.value),
            span=_span(node),
        )
    if isinstance(node, MappingNode):
        return StaticMappingValue(
            entries=tuple(
                StaticMappingEntry(key=_scalar_value(key), value=_static_value(value))
                for key, value in _scalar_mapping_pairs(node)
            ),
            span=_span(node),
        )
    raise _StructuralIssue(
        "unsupported_static_value_node",
        "Workflow value used an unsupported YAML representation-node kind.",
        node,
    )


def _optional_scalar(node: Node | None, label: str) -> StaticScalarValue | None:
    if node is None:
        return None
    return _required_scalar(node, label)


def _required_scalar(node: Node, label: str) -> StaticScalarValue:
    if not isinstance(node, ScalarNode):
        raise _StructuralIssue(
            "expected_scalar",
            f"{label} must be a YAML scalar in the bounded static representation.",
            node,
        )
    return _scalar_value(node)


def _optional_mapping_value(node: Node | None, label: str) -> StaticMappingValue | None:
    if node is None:
        return None
    if not isinstance(node, MappingNode):
        raise _StructuralIssue(
            "expected_mapping",
            f"{label} must be a YAML mapping in the bounded static representation.",
            node,
        )
    value = _static_value(node)
    assert isinstance(value, StaticMappingValue)
    return value


def _scalar_value(node: ScalarNode) -> StaticScalarValue:
    return StaticScalarValue(
        text=node.value,
        contains_expression="${{" in node.value,
        span=_span(node),
    )


def _span(node: Node) -> SourceSpan:
    return SourceSpan(
        start_line=node.start_mark.line + 1,
        start_column=node.start_mark.column + 1,
        end_line=node.end_mark.line + 1,
        end_column=node.end_mark.column + 1,
    )


def _first_duplicate(values: list[str]) -> str | None:
    seen: set[str] = set()
    for value in values:
        if value in seen:
            return value
        seen.add(value)
    return None


def _compose_workflow_yaml(content: str) -> Node | None:
    """Compose untrusted workflow text without constructing application objects."""

    if not isinstance(content, str):
        raise TypeError("Workflow YAML content must be text.")

    try:
        root = yaml.compose(content, Loader=yaml.BaseLoader)
    except yaml.YAMLError as exc:
        location = _yaml_error_location(exc)
        raise WorkflowYamlParseError(
            f"Workflow YAML could not be parsed{location}."
        ) from exc

    if root is not None:
        _validate_composed_node_graph(root)
    return root


def _validate_composed_node_graph(root: Node) -> None:
    """Apply proportionate cycle/depth/work guards before bounded extraction."""

    active: set[int] = set()
    node_visits = 0

    def visit(node: Node, depth: int) -> None:
        nonlocal node_visits

        node_visits += 1
        if node_visits > _MAX_NODE_VISITS:
            raise WorkflowYamlParseError(
                "Workflow YAML exceeds the bounded node traversal limit."
            )
        if depth > _MAX_NODE_DEPTH:
            raise WorkflowYamlParseError(
                "Workflow YAML exceeds the bounded nesting-depth limit."
            )

        identity = id(node)
        if identity in active:
            raise WorkflowYamlParseError(
                "Workflow YAML contains a recursive alias structure."
            )

        if isinstance(node, ScalarNode):
            return

        active.add(identity)
        try:
            if isinstance(node, SequenceNode):
                for item in node.value:
                    visit(item, depth + 1)
                return

            if isinstance(node, MappingNode):
                for key, value in node.value:
                    visit(key, depth + 1)
                    visit(value, depth + 1)
                return

            raise WorkflowYamlParseError(
                "Workflow YAML produced an unsupported representation-node kind."
            )
        finally:
            active.remove(identity)

    visit(root, 0)


def _yaml_error_location(exc: yaml.YAMLError) -> str:
    mark = getattr(exc, "problem_mark", None)
    if mark is None:
        return ""
    return f" at line {mark.line + 1}, column {mark.column + 1}"


__all__ = (
    "GitHubActionsStaticValue",
    "JobEntry",
    "JobProblem",
    "ReusableWorkflowJobDefinition",
    "RunDefaults",
    "RunStepDefinition",
    "SourceSpan",
    "StaticMappingEntry",
    "StaticMappingValue",
    "StaticScalarValue",
    "StaticSequenceValue",
    "StepEntry",
    "StepProblem",
    "StepsJobDefinition",
    "UsesStepDefinition",
    "WorkflowDefinition",
    "WorkflowDefinitionProblem",
    "WorkflowDefinitionResult",
    "parse_workflow_definition",
)
