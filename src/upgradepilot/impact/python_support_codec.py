"""Fixed version-1 layouts for Python-support candidates and applicability history.

Pre/post assessments, absent relevance and unresolved propositions retain their original
meaning. Decoding never invokes the impact or relevance evaluators."""

from __future__ import annotations

from upgradepilot.impact.applicability import (
    ApplicabilityPathAssessment,
    CandidateApplicabilityAssessment,
    PropositionAssessment,
)
from upgradepilot.impact.python_support import (
    PythonSupportDropImpactAssessment,
    PythonSupportDropImpactCandidate,
    PythonSupportDropInvestigationSelection,
)
from upgradepilot.workspace.native_representation import (
    Either,
    LiteralValues,
    RecordLayout,
    RecordRef,
    SequenceOf,
)

# This is an admitted representation table, not a runtime dataclass discovery mechanism.
LAYOUTS = (
    RecordLayout(
        "applicability_path_assessment",
        ApplicabilityPathAssessment,
        (
            ("key", str),
            (
                "state",
                LiteralValues(("established", "refuted", "unresolved", "conflicted")),
            ),
            ("propositions", SequenceOf(RecordRef("proposition_assessment"))),
            ("detail", str),
        ),
    ),
    RecordLayout(
        "candidate_applicability_assessment",
        CandidateApplicabilityAssessment,
        (
            (
                "state",
                LiteralValues(
                    (
                        "established_applicable",
                        "established_not_applicable",
                        "unresolved",
                        "conflicted",
                    )
                ),
            ),
            ("paths", SequenceOf(RecordRef("applicability_path_assessment"))),
            (
                "path_model_coverage",
                LiteralValues(("sufficient", "insufficient", "unresolved")),
            ),
            ("detail", str),
        ),
    ),
    RecordLayout(
        "proposition_assessment",
        PropositionAssessment,
        (
            ("key", str),
            (
                "state",
                LiteralValues(("established", "refuted", "unresolved", "conflicted")),
            ),
            (
                "evidence_coverage",
                LiteralValues(("sufficient", "insufficient", "unresolved")),
            ),
            ("evidence_owner", str),
            ("detail", str),
        ),
    ),
    RecordLayout(
        "python_support_drop_impact_assessment",
        PythonSupportDropImpactAssessment,
        (
            ("candidate", RecordRef("python_support_drop_impact_candidate")),
            ("applicability", RecordRef("candidate_applicability_assessment")),
            (
                "target_relevance",
                Either(
                    (
                        RecordRef("target_python_relevance_result"),
                        type(None),
                    )
                ),
            ),
        ),
    ),
    RecordLayout(
        "python_support_drop_impact_candidate",
        PythonSupportDropImpactCandidate,
        (
            ("pull_request", RecordRef("pull_request_identity")),
            ("dependency", RecordRef("dependency_version_change")),
            ("upstream_claim", RecordRef("grounded_python_support_drop_claim")),
            ("target_repository", str),
            ("target_revision", str),
            (
                "mechanism_status",
                LiteralValues(("established", "to_evaluate", "possible")),
            ),
            (
                "exposure_status",
                LiteralValues(("established", "to_evaluate", "possible")),
            ),
            (
                "activation_status",
                LiteralValues(("established", "to_evaluate", "possible")),
            ),
            (
                "consequence_status",
                LiteralValues(("established", "to_evaluate", "possible")),
            ),
            ("exposure_proposition", str),
            ("activation_proposition", str),
            ("possible_consequence", str),
        ),
    ),
    RecordLayout(
        "python_support_drop_investigation_selection",
        PythonSupportDropInvestigationSelection,
        (
            ("kind", LiteralValues(("acquire_exact_target_python_declaration",))),
            ("repository", str),
            ("revision", str),
            ("path", str),
            ("proposition_key", str),
            ("detail", str),
        ),
    ),
)
