"""Historical compatibility aliases for the former R4-A LangGraph control-adapter names.

Active adapter ownership moved to
``experiments.langgraph.evidence_gap_ordinary_python_control_adapters``.  These aliases remain
only for preserved historical proof utilities/references that still use the execution-coordinate
vocabulary.
"""

from experiments.langgraph.evidence_gap_ordinary_python_control_adapters import (
    OrdinaryPythonEvidenceGapAuthorityAdapter as R4AControlAuthorityAdapter,
    OrdinaryPythonEvidenceGapPlannerAdapter as R4AControlPlannerAdapter,
    OrdinaryPythonEvidenceGapPlannerControl as R4APlannerControl,
)

__all__ = (
    "R4AControlAuthorityAdapter",
    "R4AControlPlannerAdapter",
    "R4APlannerControl",
)
