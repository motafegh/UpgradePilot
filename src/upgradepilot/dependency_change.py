"""Compatibility import path for dependency-change contracts during migration.

Active ownership moved to :mod:`upgradepilot.dependency.change`. New product code must
import that module directly. This shim is temporary and will be removed after active
tests/tools finish their path migration.
"""

from .dependency.change import (
    DEPENDENCY_CHANGE_PROBLEM_CODES,
    DependencyChangeComparisonResult,
    DependencyChangeEvidenceProblem,
    DependencyChangeExtractionResult,
    DependencyChangeProblem,
    DependencyChangeProblemCode,
    DependencyChangeSourceEvidence,
    DependencyEvidenceMethod,
    DependencyFileEvidence,
    DependencyFileFormat,
    DependencyVersionChange,
    ExtractedDependencyVersionChange,
    compare_extracted_dependency_changes,
)
from .package_identity import normalize_package_name

__all__ = (
    "DEPENDENCY_CHANGE_PROBLEM_CODES",
    "DependencyChangeComparisonResult",
    "DependencyChangeEvidenceProblem",
    "DependencyChangeExtractionResult",
    "DependencyChangeProblem",
    "DependencyChangeProblemCode",
    "DependencyChangeSourceEvidence",
    "DependencyEvidenceMethod",
    "DependencyFileEvidence",
    "DependencyFileFormat",
    "DependencyVersionChange",
    "ExtractedDependencyVersionChange",
    "compare_extracted_dependency_changes",
    "normalize_package_name",
)
