"""Offline typed projections of the first captured native families.

Start at ``reconstruct_ci_projection`` or ``reconstruct_python_support_projection`` after
reading an admitted host boundary. Validate shared target/material references before exposing
native values. These projections never acquire, parse sources, evaluate, synthesize or grant
continuation authority. Unsupported unrelated codecs need not block a supported projection.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import cast

from ..ci.dependency_exercise import (
    DependencyCICoverageResult,
    WorkflowDependencyCoverageInput,
)
from ..ci.dependency_state import (
    RequirementSatisfiedAtCommandCompletion,
    RuntimeDependencyStateResult,
)
from ..dependency.change import DependencyChangeProblem, DependencyVersionChange
from ..dependency.environment import DependencySourceContext
from ..github.pull_request import ChangedFile, PullRequestIdentity
from ..github.repository import RepositoryFileEvidence
from ..impact.python_support import (
    PythonSupportDropImpactAssessment,
    PythonSupportDropInvestigationSelection,
)
from ..target.python import TargetPythonEvidence
from ..target.relevance import TargetPythonRelevanceResult
from ..upstream.claim import UpstreamSupportDropClaimResult
from ..upstream.interval import UpstreamIntervalAuthorityResult
from .native_boundary import (
    CapturedNativeBoundary,
    CapturedNativeRecord,
    ExactInvestigationTarget,
    exact_investigation_target,
    validate_native_boundary,
)
from .native_codecs import decode_native_value, family_contract
from .native_representation import NativeReconstructionError


@dataclass(frozen=True, slots=True)
class NativeInvestigationInputs:
    pull_request: PullRequestIdentity
    changed_files: tuple[ChangedFile, ...]
    dependency_result: DependencyVersionChange | DependencyChangeProblem
    source_contexts: tuple[DependencySourceContext, ...]


@dataclass(frozen=True, slots=True)
class CINativeProjection:
    inputs: NativeInvestigationInputs
    workflow_inputs: tuple[WorkflowDependencyCoverageInput, ...]
    ci_coverage_result: DependencyCICoverageResult | None
    runtime_dependency_state_result: RuntimeDependencyStateResult | None


@dataclass(frozen=True, slots=True)
class PythonSupportNativeProjection:
    inputs: NativeInvestigationInputs
    upstream_interval_result: UpstreamIntervalAuthorityResult | None
    upstream_support_drop_result: UpstreamSupportDropClaimResult | None
    target_python_source: RepositoryFileEvidence | None
    target_python_result: TargetPythonEvidence | None
    target_python_relevance_result: TargetPythonRelevanceResult | None
    pre_investigation_result: PythonSupportDropImpactAssessment | None
    investigation_selection: PythonSupportDropInvestigationSelection | None
    impact_result: PythonSupportDropImpactAssessment | None


def _invalid(detail: str) -> NativeReconstructionError:
    return NativeReconstructionError("invalid_native_material", detail)


def _decode(records: dict[str, CapturedNativeRecord], family: str) -> object:
    record = records.get(family)
    if record is None:
        raise NativeReconstructionError(
            "missing_native_material", f"Missing native family {family!r}."
        )
    contract = family_contract(family, record.codec_version)
    # Existing producer interfaces expose no admitted semantic-version identity. Preserve
    # that explicit historical gap; do not treat a newly declared method version as tested
    # merely because its representation still looks like codec version 1.
    if record.producer_version is not None:
        raise NativeReconstructionError(
            "unsupported_native_semantic_version",
            f"No admitted {family!r} reconstruction for producer version {record.producer_version!r}.",
        )
    if (
        record.outcome == "recorded"
        and "producer_version_unavailable" not in record.retention_gaps
    ):
        raise _invalid("Missing explicit producer-version recovery gap.")
    if record.owner != contract.owner:
        raise _invalid(f"Native family {family!r} has another owner.")
    expected_refs = tuple(
        records[name].record_id for name in contract.inputs if name in records
    )
    if (
        len(expected_refs) != len(contract.inputs)
        or record.input_record_ids != expected_refs
    ):
        raise NativeReconstructionError(
            "missing_native_material",
            f"Incomplete or substituted inputs for {family!r}.",
        )
    value = decode_native_value(family, record.codec_version, record.payload)
    empty = () if family == "ci_inputs" else None
    if family == "target_python":
        empty = {"source": None, "result": None}
    if record.outcome == "not_evaluated" and value != empty:
        raise _invalid("A not-evaluated record contains an evaluated value.")
    return value


def _inputs(
    records: dict[str, CapturedNativeRecord], target: ExactInvestigationTarget
) -> NativeInvestigationInputs:
    values = cast(dict[str, object], _decode(records, "investigation_inputs"))
    result = NativeInvestigationInputs(**values)
    if (
        exact_investigation_target(result.pull_request, result.dependency_result)
        != target
    ):
        raise NativeReconstructionError(
            "wrong_target", "Native identity/transition differs from the envelope."
        )
    for context in result.source_contexts:
        if (context.repository, context.revision, context.normalized_package) != (
            target.repository,
            target.head_sha,
            target.normalized_package,
        ):
            raise NativeReconstructionError(
                "wrong_target", "Dependency source context has another scope."
            )
    return result


def reconstruct_ci_projection(
    boundary: CapturedNativeBoundary, *, expected_target: ExactInvestigationTarget
) -> CINativeProjection:
    records = validate_native_boundary(boundary, expected_target=expected_target)
    inputs = _inputs(records, expected_target)
    workflows = cast(
        tuple[WorkflowDependencyCoverageInput, ...], _decode(records, "ci_inputs")
    )
    coverage = cast(DependencyCICoverageResult | None, _decode(records, "ci_coverage"))
    runtime = cast(
        RuntimeDependencyStateResult | None,
        _decode(records, "runtime_dependency_state"),
    )
    for workflow in workflows:
        if workflow.run.head_sha != expected_target.head_sha:
            raise NativeReconstructionError("wrong_target", "CI run has another head.")
        for job in workflow.jobs:
            if (
                job.head_sha != expected_target.head_sha
                or job.run_id != workflow.run.run_id
            ):
                raise NativeReconstructionError(
                    "wrong_target", "CI job has another run/head."
                )
        if (workflow.definition.repository, workflow.definition.revision) != (
            expected_target.repository,
            expected_target.head_sha,
        ):
            raise NativeReconstructionError(
                "wrong_target", "Workflow definition has another scope."
            )
        for bundle in workflow.project_environment_sources:
            context = bundle.context
            if context not in inputs.source_contexts:
                raise _invalid(
                    "Project environment source is outside the retained dependency contexts."
                )
            for source in (bundle.project_file, bundle.lock_file):
                if source is not None and (source.repository, source.revision) != (
                    expected_target.repository,
                    expected_target.head_sha,
                ):
                    raise NativeReconstructionError(
                        "wrong_target", "Project environment file has another scope."
                    )
    if coverage is not None:
        if len(coverage.workflows) != len(workflows) or any(
            result.workflow_path != supplied.definition.path
            for result, supplied in zip(coverage.workflows, workflows, strict=True)
        ):
            raise _invalid("CI coverage is not bound to its supplied workflow inputs.")
        for result, supplied in zip(coverage.workflows, workflows, strict=True):
            for consumption in result.consumptions:
                if (
                    consumption.workflow_path,
                    consumption.workflow_revision,
                    consumption.normalized_package,
                ) != (
                    supplied.definition.path,
                    expected_target.head_sha,
                    expected_target.normalized_package,
                ):
                    raise _invalid(
                        "CI consumption is outside its retained workflow/dependency scope."
                    )
    if runtime is not None:
        consumptions = (
            tuple(
                item
                for workflow in coverage.workflows
                for item in workflow.consumptions
            )
            if coverage is not None
            else ()
        )
        for assessment in runtime.assessments:
            consumption = assessment.consumption
            if (
                consumption not in consumptions
                or consumption.workflow_revision != expected_target.head_sha
                or consumption.normalized_package != expected_target.normalized_package
            ):
                raise _invalid(
                    "Runtime assessment is outside its retained CI/source basis."
                )
            if isinstance(assessment.result, RequirementSatisfiedAtCommandCompletion):
                witness = assessment.result
                identity = witness.semantics.command_identity
                actual = (
                    consumption.workflow_path,
                    consumption.workflow_revision,
                    consumption.job_key,
                    consumption.step_source_index,
                    consumption.command_location,
                )
                scoped = (
                    identity.workflow_path,
                    identity.workflow_revision,
                    identity.job_key,
                    identity.step_source_index,
                    identity.command_location,
                )
                execution = witness.execution
                executed = (
                    execution.workflow_path,
                    execution.workflow_revision,
                    execution.job_key,
                    execution.step_source_index,
                    execution.command_location,
                )
                if (
                    witness.dependency != inputs.dependency_result
                    or witness.consumption != consumption
                    or witness.source_context not in inputs.source_contexts
                    or scoped != actual
                    or executed != actual
                ):
                    raise _invalid(
                        "Command-completion witness has inconsistent material identities."
                    )
    return CINativeProjection(inputs, workflows, coverage, runtime)


def reconstruct_python_support_projection(
    boundary: CapturedNativeBoundary, *, expected_target: ExactInvestigationTarget
) -> PythonSupportNativeProjection:
    records = validate_native_boundary(boundary, expected_target=expected_target)
    inputs = _inputs(records, expected_target)
    authority = cast(
        UpstreamIntervalAuthorityResult | None, _decode(records, "upstream_authority")
    )
    claim = cast(
        UpstreamSupportDropClaimResult | None, _decode(records, "upstream_support_drop")
    )
    pre = cast(
        PythonSupportDropImpactAssessment | None,
        _decode(records, "python_support_pre_assessment"),
    )
    selection = cast(
        PythonSupportDropInvestigationSelection | None,
        _decode(records, "python_support_selection"),
    )
    target = cast(dict[str, object], _decode(records, "target_python"))
    source = cast(RepositoryFileEvidence | None, target["source"])
    target_result = cast(TargetPythonEvidence | None, target["result"])
    relevance = cast(
        TargetPythonRelevanceResult | None, _decode(records, "target_relevance")
    )
    post = cast(
        PythonSupportDropImpactAssessment | None,
        _decode(records, "python_support_post_assessment"),
    )
    for material in (authority, claim):
        if material is not None:
            interval = material.interval
            if (
                interval.normalized_package,
                interval.old_version,
                interval.proposed_version,
            ) != (
                expected_target.normalized_package,
                expected_target.old_version,
                expected_target.proposed_version,
            ):
                raise _invalid(
                    "Upstream material has another exact dependency interval."
                )
    if claim is not None and (
        authority is None or claim.interval != authority.interval
    ):
        raise _invalid(
            "Upstream claim is not bound to its supplied interval authority."
        )
    if selection is not None and (selection.repository, selection.revision) != (
        expected_target.repository,
        expected_target.head_sha,
    ):
        raise NativeReconstructionError(
            "wrong_target", "Python-support selection has another target."
        )
    if source is not None:
        if (source.repository, source.revision) != (
            expected_target.repository,
            expected_target.head_sha,
        ):
            raise NativeReconstructionError(
                "wrong_target", "Target declaration source has another scope."
            )
        if target_result is None or (target_result.path, target_result.revision) != (
            source.path,
            source.revision,
        ):
            raise _invalid("Target declaration is not bound to its retained source.")
    elif target_result is not None:
        raise NativeReconstructionError(
            "missing_native_material", "Target declaration source is missing."
        )
    if relevance is not None and (
        relevance.upstream_result != claim or relevance.target_evidence != target_result
    ):
        raise _invalid("Target relevance has another claim/declaration basis.")
    for assessment in (pre, post):
        if assessment is None:
            continue
        candidate = assessment.candidate
        if (
            candidate.pull_request != inputs.pull_request
            or candidate.dependency != inputs.dependency_result
            or candidate.upstream_claim != claim
            or (candidate.target_repository, candidate.target_revision)
            != (expected_target.repository, expected_target.head_sha)
        ):
            raise _invalid(
                "Python-support candidate has another retained identity/claim."
            )
    if post is not None and post.target_relevance != relevance:
        raise _invalid("Final Python-support assessment has another relevance basis.")
    if post is not None and (pre is None or post.candidate != pre.candidate):
        raise _invalid(
            "Pre/post assessments do not preserve the captured candidate basis."
        )
    return PythonSupportNativeProjection(
        inputs, authority, claim, source, target_result, relevance, pre, selection, post
    )
