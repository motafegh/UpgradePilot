#!/usr/bin/env python3
"""Trace what real pre-X1 S001 product state could expose to a future planner.

This experiment runs the normal public-PR investigation path and inspects the retained
pre-target-declaration Python-support impact assessment.  It compares two projection choices:

1. a deliberately small proposition/action projection; and
2. the nested product assessment/candidate graph.

The goal is not to design the final planner schema.  It is to answer an earlier evidence-first
question: does externally controlled upstream prose inevitably reach a planner, or does that
happen only if our projection chooses to include nested source evidence?

The probe also distinguishes raw-text carryover from semantic carryover.  The upstream support-
drop proposition is model-derived semantic state that was deterministically grounded, even when
its exact changelog quote is omitted from the planner-facing projection.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import os
from pathlib import Path
from typing import Literal

from upgradepilot.impact.applicability import PropositionAssessment
from upgradepilot.impact.python_support import (
    PythonSupportDropImpactAssessment,
    PythonSupportDropInvestigationSelection,
)
from upgradepilot.investigation import investigate_public_pull_request

_REPOSITORY = "pydantic/pydantic"
_PR_NUMBER = 13432
_OUTPUT_PATH = Path("/tmp/upgradepilot-b2-x1-e2-s001-state-origin.json")

FieldOrigin = Literal[
    "provider_admitted_identity",
    "model_derived_semantics_deterministically_grounded",
    "deterministic_pre_acquisition_state",
    "deterministic_derived_state",
    "deterministic_selector_output",
]


@dataclass(frozen=True, slots=True)
class ProjectedProposition:
    key: str
    state: str
    evidence_coverage: str
    evidence_owner: str
    detail: str
    origin: FieldOrigin
    raw_external_text: bool


@dataclass(frozen=True, slots=True)
class ProjectedSelection:
    kind: str
    repository: str
    revision: str
    path: str
    proposition_key: str
    detail: str


def _origin_for_proposition(proposition: PropositionAssessment) -> FieldOrigin:
    if proposition.key == "upstream_python_support_drop_crossed":
        return "model_derived_semantics_deterministically_grounded"
    if proposition.key == "exact_target_python_declaration_established":
        return "deterministic_pre_acquisition_state"
    return "deterministic_derived_state"


def proposition_projection(
    assessment: PythonSupportDropImpactAssessment,
) -> tuple[ProjectedProposition, ...]:
    """Project only typed proposition state and deterministic explanatory text."""

    return tuple(
        ProjectedProposition(
            key=proposition.key,
            state=proposition.state,
            evidence_coverage=proposition.evidence_coverage,
            evidence_owner=proposition.evidence_owner,
            detail=proposition.detail,
            origin=_origin_for_proposition(proposition),
            raw_external_text=False,
        )
        for path in assessment.applicability.paths
        for proposition in path.propositions
    )


def selection_projection(
    selection: PythonSupportDropInvestigationSelection,
) -> ProjectedSelection:
    return ProjectedSelection(
        kind=selection.kind,
        repository=selection.repository,
        revision=selection.revision,
        path=selection.path,
        proposition_key=selection.proposition_key,
        detail=selection.detail,
    )


def _nested_upstream_quotes(
    assessment: PythonSupportDropImpactAssessment,
) -> tuple[dict[str, object], ...]:
    """Expose the raw/near-raw external prose reachable through the nested candidate graph."""

    return tuple(
        {
            "object_path": (
                "python_support_drop_pre_investigation_result.candidate."
                "upstream_claim.source_evidence[].source_quote"
            ),
            "source_kind": source.source_kind,
            "introduced_in_version": source.introduced_in_version,
            "source_quote": source.source_quote,
        }
        for source in assessment.candidate.upstream_claim.source_evidence
    )


def run_probe() -> dict[str, object]:
    result = investigate_public_pull_request(
        _REPOSITORY,
        _PR_NUMBER,
        token=os.getenv("GITHUB_TOKEN"),
    )

    assessment = result.python_support_drop_pre_investigation_result
    selection = result.python_support_drop_investigation_selection
    if not isinstance(assessment, PythonSupportDropImpactAssessment):
        raise RuntimeError(
            "Real S001 product path did not retain a pre-investigation Python-support assessment."
        )
    if not isinstance(selection, PythonSupportDropInvestigationSelection):
        raise RuntimeError(
            "Real S001 product path did not select the target-Python investigation."
        )

    propositions = proposition_projection(assessment)
    nested_quotes = _nested_upstream_quotes(assessment)

    return {
        "kind": "b2_x1_e2_s001_state_origin_probe",
        "case": {
            "repository": _REPOSITORY,
            "pull_number": _PR_NUMBER,
            "head_revision": result.pull_request.head_sha,
            "head_revision_origin": "provider_admitted_identity",
        },
        "proposition_projection": [asdict(item) for item in propositions],
        "selection_projection": {
            **asdict(selection_projection(selection)),
            "origin": "deterministic_selector_output",
            "repository_revision_origin": "provider_admitted_identity",
            "raw_external_text": False,
        },
        "nested_external_text": list(nested_quotes),
        "findings": {
            "proposition_projection_contains_raw_external_text": any(
                item.raw_external_text for item in propositions
            ),
            "nested_assessment_contains_raw_external_text": bool(nested_quotes),
            "semantic_carryover_without_raw_text": any(
                item.origin == "model_derived_semantics_deterministically_grounded"
                for item in propositions
            ),
            "naive_whole_object_serialization_would_cross_raw_text_boundary": bool(
                nested_quotes
            ),
        },
    }


def main() -> int:
    output = run_probe()
    _OUTPUT_PATH.write_text(
        json.dumps(output, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    findings = output["findings"]
    print(f"case: {_REPOSITORY}#{_PR_NUMBER}")
    print(
        "proposition_projection_contains_raw_external_text: "
        f"{findings['proposition_projection_contains_raw_external_text']}"
    )
    print(
        "nested_assessment_contains_raw_external_text: "
        f"{findings['nested_assessment_contains_raw_external_text']}"
    )
    print(
        "semantic_carryover_without_raw_text: "
        f"{findings['semantic_carryover_without_raw_text']}"
    )
    print(
        "naive_whole_object_serialization_would_cross_raw_text_boundary: "
        f"{findings['naive_whole_object_serialization_would_cross_raw_text_boundary']}"
    )
    print(f"output: {_OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
