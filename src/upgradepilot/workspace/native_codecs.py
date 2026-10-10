"""Version-1 native family contracts used by capture and offline projections.

The roots below admit only the initial CI/runtime and Python-support material closure.
Domain-owned layout tables preserve results rather than recomputing them. Unsupported
family/version support is explicit; a readable payload is not decoder authority.
"""

from dataclasses import dataclass

from ..ci.native_codec import LAYOUTS as CI_LAYOUTS
from ..impact.python_support_codec import LAYOUTS as IMPACT_LAYOUTS
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
    owner: str
    shape: object
    inputs: tuple[str, ...]


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
}

_VALUES = NativeValueCodec(INPUT_LAYOUTS + CI_LAYOUTS + IMPACT_LAYOUTS)


def family_contract(family: str, version: int = 1) -> NativeFamilyContract:
    if type(version) is not int or version != 1 or family not in FAMILY_CONTRACTS:
        raise NativeReconstructionError(
            "unsupported_native_codec",
            f"No admitted {family!r} codec version {version!r}.",
        )
    return FAMILY_CONTRACTS[family]


def encode_native_value(family: str, value: object) -> bytes:
    return _VALUES.encode(value, family_contract(family).shape)


def decode_native_value(family: str, version: int, payload: bytes) -> object:
    return _VALUES.decode(payload, family_contract(family, version).shape)
