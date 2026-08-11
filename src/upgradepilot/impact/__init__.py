"""Impact-candidate and applicability boundaries for UpgradePilot."""

from .python_support import (
    ApplicabilityPropositionAssessment,
    ApplicabilityPropositionState,
    PythonSupportApplicabilityAssessment,
    PythonSupportApplicabilityState,
    PythonSupportDropImpactCandidate,
    PythonSupportPropositionKind,
    assess_python_support_applicability,
    build_python_support_drop_candidate,
)

__all__ = (
    "ApplicabilityPropositionAssessment",
    "ApplicabilityPropositionState",
    "PythonSupportApplicabilityAssessment",
    "PythonSupportApplicabilityState",
    "PythonSupportDropImpactCandidate",
    "PythonSupportPropositionKind",
    "assess_python_support_applicability",
    "build_python_support_drop_candidate",
)
