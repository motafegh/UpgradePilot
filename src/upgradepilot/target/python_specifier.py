"""Target ``requires-python`` and Python-line overlap semantics.

The implementation is temporarily imported from the pre-reconciliation combined
``packaging_method`` module. This module is now the preferred owner for target-Python
specifier evaluation.
"""

from ..packaging_method import (
    PythonLineSpecifierEvaluation,
    PythonLineSpecifierMethodResult,
    PythonLineSpecifierProblem,
    PythonLineSpecifierProblemState,
    evaluate_python_line_specifier,
)

__all__ = (
    "PythonLineSpecifierEvaluation",
    "PythonLineSpecifierMethodResult",
    "PythonLineSpecifierProblem",
    "PythonLineSpecifierProblemState",
    "evaluate_python_line_specifier",
)
