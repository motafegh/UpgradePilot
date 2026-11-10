"""Versioned native family contracts used by capture and offline projections.

The roots admit CI/runtime, Python-support and caller/signature material.
Domain-owned layout tables preserve results rather than recomputing them. Unsupported
family/version support is explicit; a readable payload is not decoder authority.
"""

from dataclasses import dataclass, replace

from ..ci.dependency_exercise import DependencyCICoverageResult
from ..ci.native_codec import COVERAGE_V2_LAYOUTS, LAYOUTS as CI_LAYOUTS
from ..impact.python_support_codec import LAYOUTS as IMPACT_LAYOUTS
from ..caller_signature.source_codec import decode_sources, encode_sources
from ..caller_signature.comparison_codec import decode_comparison, encode_comparison
from ..caller_signature.source_evidence import CallerSignatureSources
from .native_inputs_codec import LAYOUTS as INPUT_LAYOUTS
from .native_representation import (
    Either,
    NativeReconstructionError,
    NativeValueCodec,
    ObjectFields,
    RecordRef,
    SequenceOf,
)


@dataclass(frozen=True, slots=True)
class NativeFamilyContract:
    """Fixed primitive layout or explicit domain codec, plus actual input edges.

    Caller/signature families use their owner codecs (shape=None), because
    normalized cross-file facts require their exact retained source basis.
    Only their tested producer pairs have semantic-version support here.
    """
    owner: str
    shape: object
    inputs: tuple[str, ...]
    producer_method: str | None = None
    producer_version: str | None = None


def _optional(variant: str) -> Either:
    return Either((RecordRef(variant), type(None)))


FAMILY_CONTRACTS = {
    "investigation_inputs": NativeFamilyContract(
        "investigation",
        ObjectFields(
            (
                ("pull_request", RecordRef("pull_request_identity")),
                ("changed_files", SequenceOf(RecordRef("changed_file"))),
                (
                    "dependency_result",
                    Either(
                        (
                            RecordRef("dependency_version_change"),
                            RecordRef("dependency_change_problem"),
                        )
                    ),
                ),
                (
                    "source_contexts",
                    SequenceOf(
                        Either(
                            (
                                RecordRef("requirements_file_dependency_context"),
                                RecordRef("constraints_file_dependency_context"),
                                RecordRef("uv_lock_dependency_context"),
                                RecordRef(
                                    "pyproject_optional_extra_dependency_context"
                                ),
                                RecordRef("pyproject_dependency_group_context"),
                            )
                        )
                    ),
                ),
            )
        ),
        (),
    ),
    "ci_inputs": NativeFamilyContract(
        "ci.dependency_exercise",
        SequenceOf(RecordRef("workflow_dependency_coverage_input")),
        ("investigation_inputs",),
    ),
    "ci_coverage": NativeFamilyContract(
        "ci.dependency_exercise",
        _optional("dependency_ci_coverage_result"),
        ("investigation_inputs", "ci_inputs"),
    ),
    "runtime_dependency_state": NativeFamilyContract(
        "ci.dependency_state",
        _optional("runtime_dependency_state_result"),
        ("investigation_inputs", "ci_inputs", "ci_coverage"),
    ),
    "upstream_authority": NativeFamilyContract(
        "upstream.interval",
        Either(
            (
                RecordRef("authoritative_upstream_interval_evidence"),
                RecordRef("upstream_interval_authority_problem"),
                type(None),
            )
        ),
        ("investigation_inputs",),
    ),
    "upstream_support_drop": NativeFamilyContract(
        "upstream.claim",
        Either(
            (
                RecordRef("grounded_python_support_drop_claim"),
                RecordRef("upstream_support_drop_claim_problem"),
                type(None),
            )
        ),
        ("investigation_inputs", "upstream_authority"),
    ),
    "python_support_pre_assessment": NativeFamilyContract(
        "impact.python_support",
        _optional("python_support_drop_impact_assessment"),
        ("investigation_inputs", "upstream_support_drop"),
    ),
    "python_support_selection": NativeFamilyContract(
        "impact.python_support",
        _optional("python_support_drop_investigation_selection"),
        ("python_support_pre_assessment",),
    ),
    "target_python": NativeFamilyContract(
        "target.python",
        ObjectFields(
            (
                (
                    "source",
                    Either(
                        (
                            RecordRef("repository_text_file"),
                            RecordRef("unavailable_repository_file"),
                            type(None),
                        )
                    ),
                ),
                (
                    "result",
                    Either(
                        (
                            RecordRef("target_python_declaration"),
                            RecordRef("target_python_declaration_problem"),
                            type(None),
                        )
                    ),
                ),
            )
        ),
        ("investigation_inputs", "python_support_selection"),
    ),
    "target_relevance": NativeFamilyContract(
        "target.relevance",
        _optional("target_python_relevance_result"),
        ("upstream_support_drop", "target_python"),
    ),
    "python_support_post_assessment": NativeFamilyContract(
        "impact.python_support",
        _optional("python_support_drop_impact_assessment"),
        ("python_support_pre_assessment", "target_relevance"),
    ),
    "pull_request_description": NativeFamilyContract(
        "github.pull_request",
        _optional("pull_request_description_observation"),
        ("investigation_inputs",),
    ),
    "caller_signature_sources": NativeFamilyContract(
        "caller_signature.acquisition", None, ("investigation_inputs",),
        "workspace.native_capture.NativeInvestigationCapture.capture_caller_signature_sources", "1",
    ),
    "caller_signature_comparison": NativeFamilyContract(
        "caller_signature.analysis", None, ("investigation_inputs", "caller_signature_sources"),
        "workspace.native_capture.NativeInvestigationCapture.capture_caller_signature_comparison", "1",
    ),
}

_CI_COVERAGE_V2 = replace(
    FAMILY_CONTRACTS["ci_coverage"], shape=_optional("dependency_ci_coverage_result_v2")
)
_VALUES = NativeValueCodec(INPUT_LAYOUTS + CI_LAYOUTS + COVERAGE_V2_LAYOUTS + IMPACT_LAYOUTS)


def family_contract(family: str, version: int = 1) -> NativeFamilyContract:
    if type(version) is int and version == 2 and family == "ci_coverage":
        return _CI_COVERAGE_V2
    if type(version) is not int or version != 1 or family not in FAMILY_CONTRACTS:
        raise NativeReconstructionError(
            "unsupported_native_codec",
            f"No admitted {family!r} codec version {version!r}.",
        )
    return FAMILY_CONTRACTS[family]


def encode_native_value(
    family: str, value: object, *, version: int = 1, sources: CallerSignatureSources | None = None,
) -> bytes:
    contract = family_contract(family, version)
    if family == "ci_coverage" and version == 1 and isinstance(value, DependencyCICoverageResult):
        if any(item.version_requests is not None or item.version_request_jobs for item in value.workflows):
            raise NativeReconstructionError(
                "unsupported_native_codec", "Version 1 cannot retain static version requests."
            )
    if family == "caller_signature_sources":
        return encode_sources(value)
    if family == "caller_signature_comparison":
        return encode_comparison(value, sources)
    return _VALUES.encode(value, contract.shape)


def decode_native_value(family: str, version: int, payload: bytes, *, sources: CallerSignatureSources | None = None) -> object:
    contract = family_contract(family, version)
    if family == "caller_signature_sources":
        return decode_sources(payload)
    if family == "caller_signature_comparison":
        return decode_comparison(payload, sources)
    return _VALUES.decode(payload, contract.shape)
