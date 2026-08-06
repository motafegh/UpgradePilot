"""Target ``requires-python`` and Python-line overlap semantics.

This module owns the bounded PEP 440 method for asking whether a target declaration
admits any stable ``X.Y.Z`` release on one selected Python major/minor line.
"""

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from packaging.specifiers import InvalidSpecifier, Specifier, SpecifierSet
from packaging.version import InvalidVersion, Version

type PythonLineSpecifierProblemState = Literal[
    "invalid_python_line",
    "invalid_requires_python_specifier",
    "unsupported_requires_python_specifier",
    "unsatisfiable_requires_python_specifier",
]

_PYTHON_LINE = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\Z")
_SUPPORTED_SPECIFIER_OPERATORS = {"<", "<=", ">", ">=", "==", "!=", "~="}


@dataclass(frozen=True, slots=True)
class PythonLineSpecifierEvaluation:
    """Method-level answer and exact stable witness for one Python line."""

    python_line: str
    requires_python: str
    normalized_requires_python: str
    line_lower_bound: Version
    line_upper_bound: Version
    candidate_versions_checked: tuple[Version, ...]
    witness_version: Version | None
    contains_stable_release: bool


@dataclass(frozen=True, slots=True)
class PythonLineSpecifierProblem:
    """Explicit reason the stable Python-line method could not evaluate."""

    state: PythonLineSpecifierProblemState
    python_line: str
    requires_python: str
    detail: str


type PythonLineSpecifierMethodResult = (
    PythonLineSpecifierEvaluation | PythonLineSpecifierProblem
)


def evaluate_python_line_specifier(
    python_line: str,
    requires_python: str,
) -> PythonLineSpecifierMethodResult:
    """Evaluate exact stable ``X.Y.Z`` witnesses derived from specifier boundaries."""

    if not isinstance(python_line, str):
        raise TypeError("python_line must be text.")
    line_match = _PYTHON_LINE.fullmatch(python_line)
    if line_match is None:
        return PythonLineSpecifierProblem(
            state="invalid_python_line",
            python_line=python_line,
            requires_python=requires_python,
            detail="The Python line must be canonical non-negative major/minor text.",
        )

    if (
        not isinstance(requires_python, str)
        or not requires_python
        or requires_python != requires_python.strip()
    ):
        return PythonLineSpecifierProblem(
            state="invalid_requires_python_specifier",
            python_line=python_line,
            requires_python=requires_python,
            detail=(
                "The target requires-python declaration must be non-empty exact "
                "trimmed specifier text."
            ),
        )

    try:
        target = SpecifierSet(requires_python)
    except InvalidSpecifier as exc:
        return PythonLineSpecifierProblem(
            state="invalid_requires_python_specifier",
            python_line=python_line,
            requires_python=requires_python,
            detail=f"The target requires-python declaration was invalid: {exc}",
        )

    if len(target) == 0:
        return PythonLineSpecifierProblem(
            state="invalid_requires_python_specifier",
            python_line=python_line,
            requires_python=requires_python,
            detail="The target requires-python declaration contained no specifier.",
        )

    parsed_boundaries: list[Version] = []
    for specifier in target:
        boundary = _supported_specifier_boundary(specifier)
        if boundary is None:
            return PythonLineSpecifierProblem(
                state="unsupported_requires_python_specifier",
                python_line=python_line,
                requires_python=requires_python,
                detail=(
                    f"Specifier {str(specifier)!r} uses a version form outside the "
                    "first exact stable Python-line method."
                ),
            )
        parsed_boundaries.append(boundary)

    if target.is_unsatisfiable():
        return PythonLineSpecifierProblem(
            state="unsatisfiable_requires_python_specifier",
            python_line=python_line,
            requires_python=requires_python,
            detail=(
                "The target requires-python declaration is syntactically valid but "
                "cannot be satisfied by any version."
            ),
        )

    major = int(line_match.group(1))
    minor = int(line_match.group(2))
    lower = Version(f"{major}.{minor}.0")
    upper = Version(f"{major}.{minor + 1}.0")
    candidate_versions = _derive_candidate_versions(major, minor, parsed_boundaries)

    checked: list[Version] = []
    witness: Version | None = None
    for candidate in candidate_versions:
        checked.append(candidate)
        if target.contains(candidate, prereleases=False):
            witness = candidate
            break

    return PythonLineSpecifierEvaluation(
        python_line=python_line,
        requires_python=requires_python,
        normalized_requires_python=str(target),
        line_lower_bound=lower,
        line_upper_bound=upper,
        candidate_versions_checked=tuple(checked),
        witness_version=witness,
        contains_stable_release=witness is not None,
    )


def _supported_specifier_boundary(specifier: Specifier) -> Version | None:
    if specifier.operator not in _SUPPORTED_SPECIFIER_OPERATORS:
        return None

    version_text = specifier.version
    if version_text.endswith(".*"):
        if specifier.operator not in {"==", "!="}:
            return None
        version_text = version_text[:-2]

    try:
        version = Version(version_text)
    except InvalidVersion:
        return None

    if (
        version.epoch != 0
        or version.pre is not None
        or version.post is not None
        or version.dev is not None
        or version.local is not None
        or len(version.release) > 3
    ):
        return None
    return version


def _derive_candidate_versions(
    major: int,
    minor: int,
    boundaries: Sequence[Version],
) -> tuple[Version, ...]:
    patches = {0}
    for boundary in boundaries:
        release = boundary.release + (0,) * (3 - len(boundary.release))
        boundary_major, boundary_minor, boundary_patch = release
        if (boundary_major, boundary_minor) != (major, minor):
            continue
        for patch in (boundary_patch - 1, boundary_patch, boundary_patch + 1):
            if patch >= 0:
                patches.add(patch)

    return tuple(
        Version(f"{major}.{minor}.{patch}")
        for patch in sorted(patches)
    )


__all__ = (
    "PythonLineSpecifierEvaluation",
    "PythonLineSpecifierMethodResult",
    "PythonLineSpecifierProblem",
    "PythonLineSpecifierProblemState",
    "evaluate_python_line_specifier",
)
