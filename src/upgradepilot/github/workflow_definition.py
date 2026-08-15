"""Bounded YAML composition for static GitHub Actions workflow definitions.

PyYAML representation nodes are internal syntax machinery for the provider-specific
workflow-definition responsibility. They are not UpgradePilot evidence/domain objects
and must not leak into CI or Target contracts.

This first implementation slice owns only the parser/traversal boundary required before
the typed GitHub Actions IR is implemented. GitHub Actions job/step semantics belong to
the next implementation cluster.
"""

from __future__ import annotations

import yaml
from yaml.nodes import MappingNode, Node, ScalarNode, SequenceNode

_MAX_NODE_VISITS = 50_000
_MAX_NODE_DEPTH = 100


class WorkflowYamlParseError(ValueError):
    """Untrusted workflow YAML could not be composed/traversed safely."""


def _compose_workflow_yaml(content: str) -> Node | None:
    """Compose untrusted workflow text without constructing application objects.

    ``BaseLoader`` keeps scalar content textual while PyYAML still performs YAML syntax
    parsing and block-scalar decoding. The returned node graph is intentionally private
    implementation machinery; callers above this boundary must translate it into the
    bounded GitHub Actions IR rather than exposing PyYAML nodes as product contracts.
    """

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
    """Apply proportionate cycle/depth/work guards before bounded extraction.

    The upstream repository-text acquisition boundary already caps source bytes. These
    graph guards address the different risk introduced by aliases and deeply nested
    representation graphs. They are deliberately simple limits, not a general hostile-
    YAML framework.
    """

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


__all__ = ()
