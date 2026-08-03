"""Compatibility import path for exact-requirements extraction during migration.

Active ownership moved to :mod:`upgradepilot.dependency.requirements`. New product
code must import that module directly. This shim remains only until active callers and
tests finish their path migration.
"""

from .dependency.requirements import (
    extract_exact_requirement_changes,
    is_admitted_requirements_file,
    is_exact_requirement_file,
)

__all__ = (
    "extract_exact_requirement_changes",
    "is_admitted_requirements_file",
    "is_exact_requirement_file",
)
