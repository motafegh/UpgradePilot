"""Compatibility imports for the former combined packaging-based method module.

Dependency release ordering now lives in ``upgradepilot.dependency.versioning`` and
target Python-line specifier evaluation lives in ``upgradepilot.target.python_specifier``.
This flat module remains only while historical tests/tools migrate to the owning paths.
"""

from .dependency.versioning import (
    CrossedReleaseOrderingResult,
    DependencyReleaseIntervalMethodResult,
    OrderedCrossedReleaseVersions,
    PackagingVersionProblem,
    PackagingVersionProblemState,
    ParsedDependencyReleaseInterval,
    order_crossed_release_versions,
    parse_dependency_release_interval,
)
from .target.python_specifier import (
    PythonLineSpecifierEvaluation,
    PythonLineSpecifierMethodResult,
    PythonLineSpecifierProblem,
    PythonLineSpecifierProblemState,
    evaluate_python_line_specifier,
)

__all__ = (
    "CrossedReleaseOrderingResult",
    "DependencyReleaseIntervalMethodResult",
    "OrderedCrossedReleaseVersions",
    "PackagingVersionProblem",
    "PackagingVersionProblemState",
    "ParsedDependencyReleaseInterval",
    "PythonLineSpecifierEvaluation",
    "PythonLineSpecifierMethodResult",
    "PythonLineSpecifierProblem",
    "PythonLineSpecifierProblemState",
    "evaluate_python_line_specifier",
    "order_crossed_release_versions",
    "parse_dependency_release_interval",
)
