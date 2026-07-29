"""Interpret the target repository's exact-head Python declaration.

Purpose of this file
--------------------
``github_repository.py`` acquires bounded UTF-8 text at the immutable pull-request
head. This module gives one admitted target file—``pyproject.toml``—its narrow
meaning for the B2 target-relevance slice.

It parses only ``[project].requires-python`` and preserves unavailable, malformed,
missing, and invalid states explicitly. It does not evaluate PEP 440 ranges, infer
Python support from other repository files, compare an upstream claim, or make a
compatibility, safety, or maintainer-action decision.
"""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from typing import Literal

from .github_repository import (
    RepositoryFileEvidence,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)

_TARGET_PATH = "pyproject.toml"
_MISSING = object()

type TargetPythonProblemState = Literal[
    "file_unavailable",
    "malformed_toml",
    "project_table_absent",
    "requires_python_absent",
    "invalid_requires_python",
]


@dataclass(frozen=True, slots=True)
class TargetPythonDeclaration:
    """Available exact-revision ``requires-python`` evidence with provenance."""

    state: Literal["available"]
    path: str
    revision: str
    blob_sha: str
    requires_python: str


@dataclass(frozen=True, slots=True)
class TargetPythonDeclarationProblem:
    """Explicit reason the admitted target declaration could not be established."""

    state: TargetPythonProblemState
    path: str
    revision: str
    detail: str
    blob_sha: str | None = None


type TargetPythonEvidence = TargetPythonDeclaration | TargetPythonDeclarationProblem


def interpret_target_python_declaration(
    evidence: RepositoryFileEvidence,
) -> TargetPythonEvidence:
    """Interpret only ``[project].requires-python`` from exact-head evidence.

    The accepted source path is deliberately fixed. A successful parse establishes a
    textual project declaration at one immutable revision; it does not establish which
    Python versions CI runs, production uses, or maintainers actively support.
    """

    if evidence.path != _TARGET_PATH:
        raise ValueError("Target Python evidence must come from pyproject.toml.")

    if isinstance(evidence, UnavailableRepositoryFile):
        return TargetPythonDeclarationProblem(
            state="file_unavailable",
            path=evidence.path,
            revision=evidence.revision,
            detail=evidence.detail,
        )

    assert isinstance(evidence, RepositoryTextFile)
    try:
        document = tomllib.loads(evidence.content)
    except tomllib.TOMLDecodeError as exc:
        return _problem(
            evidence,
            state="malformed_toml",
            detail=f"pyproject.toml was not valid TOML: {exc}",
        )

    project = document.get("project")
    if not isinstance(project, dict):
        return _problem(
            evidence,
            state="project_table_absent",
            detail="pyproject.toml did not contain a [project] table.",
        )

    requires_python = project.get("requires-python", _MISSING)
    if requires_python is _MISSING:
        return _problem(
            evidence,
            state="requires_python_absent",
            detail="[project] did not declare requires-python.",
        )
    if not isinstance(requires_python, str) or not requires_python.strip():
        return _problem(
            evidence,
            state="invalid_requires_python",
            detail="[project].requires-python must be non-empty text.",
        )

    return TargetPythonDeclaration(
        state="available",
        path=evidence.path,
        revision=evidence.revision,
        blob_sha=evidence.blob_sha,
        requires_python=requires_python.strip(),
    )


def _problem(
    evidence: RepositoryTextFile,
    *,
    state: TargetPythonProblemState,
    detail: str,
) -> TargetPythonDeclarationProblem:
    """Create a problem result while retaining exact file provenance."""

    return TargetPythonDeclarationProblem(
        state=state,
        path=evidence.path,
        revision=evidence.revision,
        blob_sha=evidence.blob_sha,
        detail=detail,
    )
