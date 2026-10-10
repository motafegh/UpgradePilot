"""Offline typed projections of the first captured native families.

Start at ``reconstruct_ci_projection`` or ``reconstruct_python_support_projection`` after
reading an admitted host boundary. Validate shared target/material references before exposing
native values. These projections never acquire, parse sources, evaluate, synthesize or grant
continuation authority. Unsupported unrelated codecs need not block a supported projection.
"""

from __future__ import annotations

import posixpath
from dataclasses import dataclass
from typing import cast

from ..ci.dependency_exercise import (
    DependencyCICoverageResult,
    WorkflowDependencyCoverageInput,
)
from ..ci.consumption import StaticDependencyConsumptionEvidence
from ..ci.dependency_state import (
    RequirementSatisfiedAtCommandCompletion,
    RequirementStateBlockingSemanticEvidence,
    RuntimeDependencyStateResult,
)
from ..dependency.change import DependencyChangeProblem, DependencyVersionChange
from ..dependency.environment import (
    DependencySourceContext,
    PyprojectDependencyGroupContext,
    PyprojectOptionalExtraDependencyContext,
    UvLockDependencyContext,
)
from ..dependency.package_manager_semantics import PackageManagerSemanticProblem
from ..github.pull_request import ChangedFile, PullRequestIdentity
from ..github.repository import RepositoryFileEvidence, UnavailableRepositoryFile
from ..github.workflow_definition import RunStepDefinition
from ..impact.python_support import (
    PythonSupportDropImpactAssessment,
    PythonSupportDropInvestigationSelection,
)
from ..target.python import (
    TargetPythonDeclaration,
    TargetPythonDeclarationProblem,
    TargetPythonEvidence,
)
from ..target.relevance import TargetPythonRelevanceResult
from ..upstream.claim import (
    GroundedPythonSupportDropClaim,
    UpstreamSupportDropClaimResult,
)
from ..upstream.interval import (
    AuthoritativeUpstreamIntervalEvidence,
    IntervalGitHubReleaseSource,
    TaggedChangelogEvidence,
    UpstreamIntervalAuthorityResult,
)
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
    if (
        record.outcome == "recorded"
        and record.producer_method is None
        and "producer_method_unavailable" not in record.retention_gaps
    ):
        raise _invalid("Missing explicit producer-method recovery gap.")
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
    # Two edges explicitly allow unexecuted input operations: an upstream problem can
    # record relevance without target acquisition; post can carry pre forward without
    # relevance. All other recorded consumers require a recorded immediate input.
    optional_operation = {
        "target_relevance": "target_python",
        "python_support_post_assessment": "target_relevance",
    }.get(family)
    if record.outcome == "recorded" and any(
        records[name].outcome != "recorded"
        for name in contract.inputs
        if name != optional_operation
    ):
        raise NativeReconstructionError(
            "missing_native_material", f"Recorded {family!r} has an unexecuted input."
        )
    value = decode_native_value(family, record.codec_version, record.payload)
    if (
        record.outcome == "recorded"
        and value is None
        and family != "python_support_selection"
    ):
        raise NativeReconstructionError(
            "missing_native_material", f"Recorded {family!r} lacks its typed result."
        )
    empty = () if family == "ci_inputs" else None
    if family == "target_python":
        empty = {"source": None, "result": None}
        # This family records acquisition and interpretation together. A selected but
        # unexecuted read is not_evaluated; recorded requires its source and typed result,
        # including unavailable-source/problem variants. Only selector abstention uses None.
        target = cast(dict[str, object], value)
        if record.outcome == "recorded" and (
            target["source"] is None or target["result"] is None
        ):
            raise NativeReconstructionError(
                "missing_native_material",
                "Recorded target-Python acquisition lacks its source or result.",
            )
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
    paths = tuple(file.filename for file in result.changed_files)
    if len(paths) != result.pull_request.changed_files or len(set(paths)) != len(paths):
        raise _invalid("Changed-file membership differs from the retained PR snapshot.")
    if any(
        evidence.path not in paths
        for evidence in result.dependency_result.source_evidence
    ):
        raise _invalid("Dependency provenance is outside the retained changed files.")
    for context in result.source_contexts:
        if (context.repository, context.revision, context.normalized_package) != (
            target.repository,
            target.head_sha,
            target.normalized_package,
        ):
            raise NativeReconstructionError(
                "wrong_target", "Dependency source context has another scope."
            )
        if (
            not isinstance(result.dependency_result, DependencyVersionChange)
            or context.source_evidence not in result.dependency_result.source_evidence
        ):
            raise _invalid(
                "Dependency context provenance is outside its retained transition."
            )
    return result


def _validate_project_bundles(
    workflow: WorkflowDependencyCoverageInput, inputs: NativeInvestigationInputs
) -> None:
    """Check acquisition's context→file relationship, including unavailable files.

    Paths are source-role locators from investigation._acquire_project_environment_sources;
    source contents and the domain interpretations of those contents remain historical.
    """
    contexts = tuple(
        context
        for context in inputs.source_contexts
        if isinstance(
            context,
            (
                UvLockDependencyContext,
                PyprojectOptionalExtraDependencyContext,
                PyprojectDependencyGroupContext,
            ),
        )
    )
    if (
        workflow.project_environment_sources
        and workflow.project_environment_consumptions
    ):
        raise _invalid(
            "Acquired project sources and precomposed consumptions are exclusive."
        )
    # The explicit legacy input seam has no acquired bundle; its consumptions are checked
    # below against retained contexts. Normal acquisition must preserve all its bundles.
    if (
        not workflow.project_environment_consumptions
        and tuple(bundle.context for bundle in workflow.project_environment_sources)
        != contexts
    ):
        raise _invalid(
            "Project source bundles differ from their retained context sequence."
        )
    for bundle in workflow.project_environment_sources:
        context = bundle.context
        for source in (bundle.project_file, bundle.lock_file):
            if source is not None and (source.repository, source.revision) != (
                context.repository,
                context.revision,
            ):
                raise NativeReconstructionError(
                    "wrong_target", "Project environment file has another scope."
                )
        root = posixpath.dirname(context.source_path)
        project_path = (
            (f"{root}/pyproject.toml" if root else "pyproject.toml")
            if isinstance(context, UvLockDependencyContext)
            else context.source_path
        )
        if (
            bundle.project_file.repository,
            bundle.project_file.revision,
            bundle.project_file.path,
        ) != (context.repository, context.revision, project_path):
            raise _invalid(
                "Project file is not bound to its dependency context locator."
            )
        lock = bundle.lock_file
        if isinstance(context, UvLockDependencyContext):
            if lock is None or (lock.repository, lock.revision, lock.path) != (
                context.repository,
                context.revision,
                context.source_path,
            ):
                raise _invalid(
                    "uv lock source is missing or has another context locator."
                )
        elif lock is not None:
            raise _invalid("A pyproject source context cannot carry uv lock evidence.")


def _validate_consumption_source(
    consumption: StaticDependencyConsumptionEvidence,
    workflow: WorkflowDependencyCoverageInput,
    inputs: NativeInvestigationInputs,
) -> None:
    if not isinstance(inputs.dependency_result, DependencyVersionChange):
        raise _invalid("CI consumption lacks its retained dependency transition.")
    if (
        consumption.workflow_path,
        consumption.workflow_revision,
        consumption.normalized_package,
    ) != (
        workflow.definition.path,
        inputs.pull_request.head_sha,
        inputs.dependency_result.normalized_package,
    ):
        raise _invalid(
            "CI consumption is outside its retained workflow/dependency scope."
        )
    if consumption.source_path is not None and not any(
        context.source_path == consumption.source_path
        for context in inputs.source_contexts
    ):
        raise _invalid(
            "CI consumption source is outside its retained dependency contexts."
        )


def _validate_coverage_material(
    coverage: DependencyCICoverageResult,
    workflows: tuple[WorkflowDependencyCoverageInput, ...],
    inputs: NativeInvestigationInputs,
) -> None:
    if len(coverage.workflows) != len(workflows):
        raise _invalid("CI coverage is not bound to its supplied workflow inputs.")
    for result, supplied in zip(coverage.workflows, workflows, strict=True):
        if (result.workflow_path, result.workflow_name) != (
            supplied.definition.path,
            supplied.run.name,
        ):
            raise _invalid("CI coverage has another retained workflow identity.")
        for consumption in result.consumptions:
            _validate_consumption_source(consumption, supplied, inputs)
        for invocation in result.invocations:
            if (invocation.workflow_path, invocation.workflow_revision) != (
                supplied.definition.path,
                supplied.definition.revision,
            ):
                raise _invalid("CI invocation has another workflow source identity.")
        correlation = result.runtime_correlation
        if correlation is None:
            continue
        for job in correlation.jobs:
            if job.runtime_job not in supplied.jobs:
                raise _invalid("CI correlation references an unretained runtime job.")
            if (
                job.static_job.name is None
                or job.static_job.name.text != job.runtime_job.name
            ):
                raise _invalid(
                    "Correlated static/runtime jobs have different retained names."
                )
            for step in job.steps:
                if (
                    step.static_step not in job.static_job.steps
                    or step.runtime_step not in (job.runtime_job.steps or ())
                ):
                    raise _invalid(
                        "CI correlation references an unretained static/runtime step."
                    )
                if (
                    step.static_step.name is not None
                    and step.static_step.name.text != step.runtime_step.name
                ):
                    raise _invalid(
                        "Correlated named steps have different retained names."
                    )
            if correlation.state == "correlated" and (
                tuple(step.static_step for step in job.steps) != job.static_job.steps
                or len({step.runtime_step.number for step in job.steps})
                != len(job.steps)
            ):
                raise _invalid("Correlated steps omit or repeat retained job members.")
        if correlation.state == "correlated":
            if (
                len(correlation.jobs) != len(supplied.jobs)
                or {job.runtime_job for job in correlation.jobs} != set(supplied.jobs)
                or len({job.static_job.key for job in correlation.jobs})
                != len(correlation.jobs)
            ):
                raise _invalid(
                    "Correlated jobs omit or repeat retained workflow members."
                )
            for command in result.consumptions + result.invocations:
                steps = tuple(
                    step
                    for job in correlation.jobs
                    if job.static_job.key == command.job_key
                    for step in job.static_job.steps
                    if step.source_index == command.step_source_index
                )
                if (
                    len(steps) != 1
                    or not isinstance(steps[0], RunStepDefinition)
                    or steps[0].command.text != command.command
                ):
                    raise _invalid(
                        "CI command differs from its retained parsed job/step text."
                    )
        # Correlation/eligibility truth and static tree→YAML derivation stay with their
        # historical owners. Literal names/text and member equality above use only retained
        # facts. In particular, unnamed provider display names are not regenerated here.


def _validate_semantic_material(
    evidence: RequirementStateBlockingSemanticEvidence,
    dimension: str | None,
    location: object,
) -> None:
    if evidence.command_location != location:
        raise _invalid("Semantic evidence has another retained command location.")
    if isinstance(evidence, PackageManagerSemanticProblem):
        actual_dimension = evidence.dimension
    else:
        provenance = evidence.provenance
        actual_dimension = provenance.dimension
        if provenance.winning_source not in tuple(
            step.source_kind for step in provenance.inspected_sources
        ):
            raise _invalid(
                "Semantic provenance winner is outside its retained source trace."
            )
    if actual_dimension != dimension:
        raise _invalid("Semantic evidence has another retained dimension.")


def _validate_authority_material(
    authority: UpstreamIntervalAuthorityResult, inputs: NativeInvestigationInputs
) -> None:
    """Bind admitted authority components; never rerun source/interval admission.

    Problems can retain failed identities as evidence. Success components instead refer to
    the same retained repository/interval and declared source basis. Crossed-release order
    and membership are historical values, not recalculated version-selection results.
    """
    dependency = inputs.dependency_result
    interval = authority.interval
    if not isinstance(dependency, DependencyVersionChange) or (
        interval.package,
        interval.normalized_package,
        interval.old_version,
        interval.proposed_version,
    ) != (
        dependency.package,
        dependency.normalized_package,
        dependency.old_version,
        dependency.proposed_version,
    ):
        raise _invalid("Upstream authority has another retained dependency interval.")
    if not isinstance(authority, AuthoritativeUpstreamIntervalEvidence):
        return
    index = authority.crossed_releases
    changelog = authority.tagged_changelog
    for source in (index, changelog):
        if source is not None and (
            source.repository.casefold() != authority.repository.casefold()
            or source.interval != interval
        ):
            raise _invalid("Authority component has another repository/interval basis.")
    versions = tuple(source.release_version for source in authority.release_bodies)
    for source in authority.release_bodies:
        release = source.release
        if (
            release.repository.casefold() != authority.repository.casefold()
            or (
                index is not None
                and source.release_version not in index.ordered_versions
            )
            or release.requested_tag
            not in (source.release_version, f"v{source.release_version}")
            or release.tag_ref != f"refs/tags/{release.requested_tag}"
        ):
            raise _invalid(
                "Authority release source has another repository/release/tag basis."
            )
    if len(set(versions)) != len(versions):
        raise _invalid("Authority release-source identities are duplicated.")
    if authority.authority_basis != "tagged_changelog" and (
        index is None or versions != index.ordered_versions
    ):
        raise _invalid(
            "Complete-series authority lacks its declared retained release sources."
        )
    if authority.authority_basis != "complete_release_series" and changelog is None:
        raise _invalid("Tagged authority lacks its declared retained changelog source.")
    allowed_versions = {interval.old_version, interval.proposed_version}
    if index is not None:
        allowed_versions.update(index.ordered_versions)
    for metadata in authority.package_metadata:
        if (
            metadata.normalized_package != interval.normalized_package
            or metadata.release_version not in allowed_versions
        ):
            raise _invalid(
                "Authority metadata has another retained package/release basis."
            )


def _validate_grounded_claim(
    claim: GroundedPythonSupportDropClaim,
    authority: AuthoritativeUpstreamIntervalEvidence,
) -> None:
    """Check exact retained provenance, not Python-line entailment or claim truth.

    Membership and text slicing bind the historical grounding to its original authority.
    Do not call validate_support_drop_candidates or reconstruct an extraction candidate.
    """
    index = authority.crossed_releases
    if (
        not claim.source_evidence
        or index is None
        or claim.introduced_in_version not in index.ordered_versions
    ):
        raise _invalid("Grounded claim lacks retained source/release membership.")
    for evidence in claim.source_evidence:
        source = evidence.source
        if evidence.introduced_in_version != claim.introduced_in_version:
            raise _invalid("Grounded source has another introduced-release identity.")
        if isinstance(source, IntervalGitHubReleaseSource):
            matches = tuple(
                item
                for item in authority.release_bodies
                if item.release_version == claim.introduced_in_version
            )
            if evidence.source_kind != "github_release_body" or matches != (source,):
                raise _invalid(
                    "Grounded release source is not the exact retained authority member."
                )
            text = source.release.body
        else:
            assert isinstance(source, TaggedChangelogEvidence)
            if (
                evidence.source_kind != "tagged_changelog"
                or source != authority.tagged_changelog
            ):
                raise _invalid(
                    "Grounded changelog is not the exact retained authority member."
                )
            text = source.content
        if (
            text is None
            or evidence.quote_start < 0
            or evidence.quote_end <= evidence.quote_start
            or evidence.quote_end > len(text)
            or text[evidence.quote_start : evidence.quote_end] != evidence.source_quote
        ):
            raise _invalid(
                "Grounded quote/span differs from its retained authority text."
            )


def _validate_selection_material(
    selection: PythonSupportDropInvestigationSelection,
    pre: PythonSupportDropImpactAssessment | None,
) -> None:
    if pre is None:
        raise _invalid("Selected investigation lacks its retained pre-assessment.")
    candidate = pre.candidate
    propositions = tuple(
        proposition
        for path in pre.applicability.paths
        for proposition in path.propositions
        if proposition.key == selection.proposition_key
    )
    if (
        (selection.repository, selection.revision)
        != (candidate.target_repository, candidate.target_revision)
        or selection.kind != "acquire_exact_target_python_declaration"
        or selection.path != "pyproject.toml"
        or selection.proposition_key != "exact_target_python_declaration_established"
        or pre.target_relevance is not None
        or pre.applicability.state != "unresolved"
        or len(propositions) != 1
    ):
        raise _invalid(
            "Selected investigation has another retained candidate/proposition basis."
        )
    proposition = propositions[0]
    if (
        proposition.state,
        proposition.evidence_coverage,
        proposition.evidence_owner,
    ) != ("unresolved", "insufficient", "target.python"):
        raise _invalid(
            "Selected target read has no retained unresolved declaration basis."
        )
    # A recorded None remains a historical selector abstention. Never infer a missing
    # selection by re-running the policy or by treating every unresolved result as a read.


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
    if not isinstance(inputs.dependency_result, DependencyVersionChange) and any(
        records[family].outcome == "recorded"
        for family in ("ci_inputs", "ci_coverage", "runtime_dependency_state")
    ):
        raise _invalid(
            "Recorded CI material requires a retained dependency transition."
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
        _validate_project_bundles(workflow, inputs)
        for consumption in workflow.project_environment_consumptions:
            _validate_consumption_source(consumption, workflow, inputs)
    if coverage is not None:
        _validate_coverage_material(coverage, workflows, inputs)
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
        # Enumerate the retained admitted bases, without reparsing/classifying commands.
        admitted = tuple(
            item
            for item in consumptions
            if item.state == "supported" and item.mechanism == "direct_requirements"
        )
        if tuple(item.consumption for item in runtime.assessments) != admitted:
            raise _invalid(
                "Runtime assessment membership differs from retained admitted CI bases."
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
                    or witness.source_context.source_path != consumption.source_path
                    or scoped != actual
                    or executed != actual
                ):
                    raise _invalid(
                        "Command-completion witness has inconsistent material identities."
                    )
                for dimension, evidence in (
                    ("manager_environment", witness.semantics.manager_environment),
                    (
                        "installation_destination",
                        witness.semantics.installation_destination,
                    ),
                    ("package_mutation_mode", witness.semantics.package_mutation_mode),
                    (
                        "direct_requirement_handling",
                        witness.semantics.direct_requirement_handling,
                    ),
                ):
                    if isinstance(evidence, PackageManagerSemanticProblem):
                        raise _invalid(
                            "A successful witness lacks a retained semantic fact."
                        )
                    _validate_semantic_material(
                        evidence, dimension, identity.command_location
                    )
                step_execution = execution.step_execution
                retained_steps = (
                    tuple(
                        step
                        for workflow in coverage.workflows
                        if consumption in workflow.consumptions
                        and workflow.runtime_correlation is not None
                        for job in workflow.runtime_correlation.jobs
                        if job.static_job.key == consumption.job_key
                        for step in job.steps
                        if step.static_step.source_index
                        == consumption.step_source_index
                    )
                    if coverage is not None
                    else ()
                )
                if (
                    step_execution is None
                    or step_execution.correlation not in retained_steps
                ):
                    raise _invalid(
                        "Witness execution has another retained CI step-correlation basis."
                    )
            elif assessment.result.blocking_semantic_evidence is not None:
                _validate_semantic_material(
                    assessment.result.blocking_semantic_evidence,
                    assessment.result.blocking_dimension,
                    consumption.command_location,
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
    if authority is not None:
        _validate_authority_material(authority, inputs)
    if claim is not None and (
        not isinstance(authority, AuthoritativeUpstreamIntervalEvidence)
        or claim.interval != authority.interval
    ):
        raise _invalid(
            "Upstream claim is not bound to its supplied interval authority."
        )
    if isinstance(claim, GroundedPythonSupportDropClaim):
        assert isinstance(authority, AuthoritativeUpstreamIntervalEvidence)
        _validate_grounded_claim(claim, authority)
    if pre is not None and pre.target_relevance is not None:
        raise _invalid("Pre-acquisition assessment carries later target relevance.")
    if selection is not None and (selection.repository, selection.revision) != (
        expected_target.repository,
        expected_target.head_sha,
    ):
        raise NativeReconstructionError(
            "wrong_target", "Python-support selection has another target."
        )
    if selection is not None:
        _validate_selection_material(selection, pre)
    if source is not None:
        if (source.repository, source.revision) != (
            expected_target.repository,
            expected_target.head_sha,
        ):
            raise NativeReconstructionError(
                "wrong_target", "Target declaration source has another scope."
            )
        # Matching source/result identities alone cannot bind an acquired file to the
        # retained request. Compare the recorded relationship without rerunning selection.
        if selection is None or source.path != selection.path:
            raise _invalid(
                "Target declaration source is not bound to its selected acquisition path."
            )
        if target_result is None or (target_result.path, target_result.revision) != (
            source.path,
            source.revision,
        ):
            raise _invalid("Target declaration is not bound to its retained source.")
        if isinstance(source, UnavailableRepositoryFile):
            if (
                not isinstance(target_result, TargetPythonDeclarationProblem)
                or target_result.state != "file_unavailable"
                or target_result.detail != source.detail
            ):
                raise _invalid(
                    "Unavailable acquisition has another retained interpretation problem."
                )
        elif (
            isinstance(target_result, TargetPythonDeclarationProblem)
            and target_result.state == "file_unavailable"
        ):
            raise _invalid(
                "Readable acquisition cannot carry an unavailable-source interpretation."
            )
    elif target_result is not None:
        raise NativeReconstructionError(
            "missing_native_material", "Target declaration source is missing."
        )
    if relevance is not None and (
        relevance.upstream_result != claim or relevance.target_evidence != target_result
    ):
        raise _invalid("Target relevance has another claim/declaration basis.")
    if relevance is not None:
        if isinstance(claim, GroundedPythonSupportDropClaim) and target_result is None:
            raise _invalid(
                "Grounded-claim relevance lacks its retained declaration basis."
            )
        if (
            not isinstance(claim, GroundedPythonSupportDropClaim)
            and target_result is not None
        ):
            raise _invalid(
                "An upstream-claim problem cannot consume target declaration evidence."
            )
        method = relevance.specifier_result
        if method is not None and (
            not isinstance(claim, GroundedPythonSupportDropClaim)
            or not isinstance(target_result, TargetPythonDeclaration)
            or (method.python_line, method.requires_python)
            != (claim.python_line, target_result.requires_python)
        ):
            raise _invalid(
                "Specifier result has another retained line/declaration input."
            )
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
    if post is not None and relevance is None and post != pre:
        raise _invalid(
            "Post-assessment without new relevance differs from its retained pre result."
        )
    return PythonSupportNativeProjection(
        inputs, authority, claim, source, target_result, relevance, pre, selection, post
    )
