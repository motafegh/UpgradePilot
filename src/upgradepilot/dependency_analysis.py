"""Compatibility import path for dependency analysis during source reconciliation."""

from .dependency.analysis import (
    DependencyChangeAnalysis,
    DependencyChangeAnalysisResult,
    analyze_dependency_change,
    is_uv_lock_file,
)

__all__ = (
    "DependencyChangeAnalysis",
    "DependencyChangeAnalysisResult",
    "analyze_dependency_change",
    "is_uv_lock_file",
)
