"""Provider-owned identity for one parsed static workflow command occurrence.

The location combines the source span and deterministic source order already established by
``workflow_command_analysis``. It identifies one static source occurrence only; it does not
prove execution, success, or a same-path ordering relation.
"""

from __future__ import annotations

from dataclasses import dataclass

from .workflow_command_analysis import CommandSourceSpan, StaticCommandOccurrence
from .workflow_instance_commands import WorkflowRunScriptIdentity


@dataclass(frozen=True, slots=True)
class StaticCommandLocation:
    """Parser-neutral occurrence address within original or specialized run text."""

    source_span: CommandSourceSpan
    source_order: int
    script_identity: WorkflowRunScriptIdentity | None = None

    @classmethod
    def from_occurrence(cls, occurrence: StaticCommandOccurrence) -> StaticCommandLocation:
        """Derive the location from the shared provider-owned command occurrence."""

        return cls(
            source_span=occurrence.source_span,
            source_order=occurrence.source_order,
            script_identity=occurrence.script_identity,
        )


__all__ = ("StaticCommandLocation",)
