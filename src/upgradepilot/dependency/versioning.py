"""Dependency-release interval parsing and PEP 440 ordering semantics.

The implementation is temporarily imported from the pre-reconciliation combined
``packaging_method`` module. This module is now the preferred owner for dependency
version semantics; target-Python specifier semantics have a separate owner.
"""

from ..packaging_method import (
    CrossedReleaseOrderingResult,
    DependencyReleaseIntervalMethodResult,
    OrderedCrossedReleaseVersions,
    PackagingVersionProblem,
    PackagingVersionProblemState,
    ParsedDependencyReleaseInterval,
    order_crossed_release_versions,
    parse_dependency_release_interval,
)

__all__ = (
    "CrossedReleaseOrderingResult",
    "DependencyReleaseIntervalMethodResult",
    "OrderedCrossedReleaseVersions",
    "PackagingVersionProblem",
    "PackagingVersionProblemState",
    "ParsedDependencyReleaseInterval",
    "order_crossed_release_versions",
    "parse_dependency_release_interval",
)
