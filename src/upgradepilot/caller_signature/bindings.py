"""Pure binding records transferred from the qualified ordered analysis.

These are source alternatives and history, not observations of execution. The
experimental analyzer remains the reference producer until its later transfer.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Literal

MAX_BINDING_ORIGINS = 32
MAX_BINDING_TRACE_STEPS = 128


@dataclass(frozen=True)
class BindingTraceStep:
    """Exact file-linked AST span; columns count UTF-8 bytes, lines start at one."""

    source_id: str
    scope: str
    line: int
    column: int
    end_line: int
    end_column: int
    operation: str
    name: str
    origin: str | None = None
    input_name: str | None = None


@dataclass(frozen=True)
class BindingAssessment:
    """Imported alternatives and explicit unknown/unbound source possibilities.

    The trace includes overwritten/restored history and competing branches.
    With unknown_possible, origins are not exhaustive. Only established may
    become lexical_import; no state asserts execution.
    """

    state: Literal["established", "conditional", "unknown", "unbound"]
    possible_imports: tuple[str, ...]
    unknown_possible: bool
    unbound_possible: bool
    scope: str
    reasons: tuple[str, ...]
    trace: tuple[BindingTraceStep, ...]


def binding_state(origins: tuple[str, ...], unknown: bool, unbound: bool) -> str:
    """One canonical possibility-to-state rule, also used at saved-input decoding."""
    if len(origins) == 1 and not unknown and not unbound:
        return "established"
    if len(origins) > 1 or origins and (unknown or unbound) or unknown and unbound:
        return "conditional"
    return "unbound" if unbound and not unknown else "unknown"
