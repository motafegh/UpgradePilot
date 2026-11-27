"""Fixed source-family layout and source/receipt joins, with no acquisition.

``encode_sources``/``decode_sources`` retain exact catalog text, acquired roles,
analysis limits and typed acquisition premises. Native provider observations and
historical summaries remain distinguishable. Explicit layout tables preserve
only this profile's consumed source evidence; unrelated changelog/window results
remain with their existing owners. Missing full historical association records
are gaps, not reconstructed authority. Workspace validates target/input edges.
"""
from __future__ import annotations

from dataclasses import replace
from datetime import datetime
from hashlib import sha256
import re

from . import source_evidence as se
from .adapter_calls import ADAPTER_CALL_ANALYSIS_SCOPE, PAIR_MODULE_ATTEMPTS
from .analysis import SourceSpan
from .bindings import BindingAssessment, BindingTraceStep, ImportFact, ReferenceFact, binding_state
from .evidence import MeasuredDuration
from .native_codec import DURATION_LAYOUT
from .result_codec import (
    ANALYSIS_PROFILE, INPUT_FORMAT, decode_analysis_input, decode_analysis_limits,
    encode_analysis_limits, module_fields,
)
from ..github.identity import validate_commit_sha, validate_repository
from ..package_identity import normalize_package_name
from ..github.api import GITHUB_API_ROOT
from ..github.tag import (GitHubTagCommitEvidence, GitHubTagRepositoryRedirect,
                          repository_move_redirect, tag_reference_path)
from ..pypi.provenance import FileProvenanceEvidence, FileProvenanceProblem, PublisherIdentity
from ..pypi.release import (
    DistributionFile, MAX_FILE_PYTHON_DECLARATIONS, MAX_REQUIRES_PYTHON_TEXT,
    PackageReleaseEvidence, ProjectUrlCandidate, PublishedFileRequiresPython,
)
from ..pypi.simple_index import MAX_INDEX_FILES, MAX_INDEX_VERSIONS, SimpleIndexBasis, simple_index_url
from ..repository_path import repository_relative_parts
from .sample_python import (
    PYTHON_LINE, RANKED_SAMPLE_BASIS, WORKFLOW_TEXT_LIMIT,
    AdapterRankDecision, SampleFilePythonAssessment, SamplePythonScenario,
    SampleReleasePythonAssessment, SelectedSamplePythonJob,
)
from ..workspace.native_boundary import ExactInvestigationTarget
from ..workspace.native_representation import (
    Either, LiteralValues, NativeValueCodec, RecordLayout, RecordRef, SequenceOf,
    json_bytes, object_fields, parse_json,
)
from ..workspace.source_access import encode_source_catalog, read_source_catalog

FORMAT = "caller-signature-sources/1"
MOVE_FORMAT = "caller-signature-sources/2"
SAMPLE_PYTHON_FORMAT = "caller-signature-sources/3"
_SOURCE_FORMATS = {
    1: FORMAT, 2: MOVE_FORMAT, 3: SAMPLE_PYTHON_FORMAT,
    4: "caller-signature-sources/4", 5: "caller-signature-sources/5",
}


def _optional(shape):
    return Either((shape, type(None)))


def _seq(name):
    return SequenceOf(RecordRef(name))


# Constructors below are representation-only records. No checkpoint-supplied
# module/class name, provider/evaluator constructor or dataclass reflection.
_STRINGS = SequenceOf(str)
_LAYOUTS = (
    DURATION_LAYOUT,
    RecordLayout(
        "source_problem", se.SourceProblem,
        (
            ("stage", str),
            ("reason", str),
            ("detail", str),
        ),
    ),
    RecordLayout(
        "source_gap", se.SourceContextGap,
        (
            ("path", _optional(str)),
            ("reason", str),
            ("detail", str),
        ),
    ),
    RecordLayout(
        "source_declaration", se.SourceDependencyDeclaration,
        (
            ("source_id", str),
            ("location", str),
            ("raw", str),
            ("package", str),
            ("specifier", str),
            ("extras", _STRINGS),
            ("marker", _optional(str)),
            ("group", str),
        ),
    ),
    RecordLayout(
        "source_import_candidate", se.SourceImportCandidate,
        (
            ("imported_module", str),
            ("declaration", RecordRef("source_declaration")),
            ("import_source_id", str),
            ("import_line", int),
            ("basis", str),
        ),
    ),
    RecordLayout(
        "source_file_receipt", se.SourceFileReceipt,
        (
            ("source_id", str),
            ("sha256", str),
            ("utf8_bytes", int),
        ),
    ),
    RecordLayout(
        "target_source_receipt", se.TargetSourceReceipt,
        (
            ("repository", str),
            ("revision", str),
            ("tree_sha", str),
            ("inventory_entries", int),
            ("inventory_truncated", bool),
            ("files", _seq("source_file_receipt")),
            ("declarations", _seq("source_declaration")),
            ("candidates", _seq("source_import_candidate")),
            ("excluded_paths", _STRINGS),
            ("omitted_paths", _STRINGS),
            ("gaps", _seq("source_gap")),
            ("examined_bytes", int),
            ("limitations", _STRINGS),
        ),
    ),
    RecordLayout(
        "source_metadata", se.SourceDependencyMetadata,
        (
            ("package", str),
            ("version", str),
            ("source_url", str),
            ("requirements", _seq("source_declaration")),
            ("gaps", _seq("source_gap")),
        ),
    ),
    RecordLayout(
        "project_url", ProjectUrlCandidate,
        (
            ("label", str),
            ("url", str),
        ),
    ),
    RecordLayout(
        "distribution", DistributionFile,
        (
            ("filename", str),
            ("url", str),
            ("sha256", str),
            ("package_type", str),
        ),
    ),
    RecordLayout(
        "package_release", PackageReleaseEvidence,
        (
            ("state", LiteralValues(("available",))),
            ("requested_package", str),
            ("normalized_package", str),
            ("requested_version", str),
            ("published_name", str),
            ("published_version", str),
            ("source_url", str),
            ("retrieved_at", datetime),
            ("last_serial", int),
            ("distribution_files", _seq("distribution")),
            ("project_urls", _seq("project_url")),
        ),
        ("state",),
    ),
    RecordLayout(
        "publisher_identity", PublisherIdentity,
        (
            ("kind", str),
            ("repository", _optional(str)),
            ("workflow", _optional(str)),
        ),
    ),
    RecordLayout(
        "file_provenance", FileProvenanceEvidence,
        (
            ("state", LiteralValues(("available",))),
            ("package", str),
            ("version", str),
            ("filename", str),
            ("sha256", str),
            ("source_url", str),
            ("retrieved_at", datetime),
            ("api_version", int),
            ("attestation_count", int),
            ("publishers", _seq("publisher_identity")),
        ),
        ("state",),
    ),
    RecordLayout(
        "file_provenance_problem", FileProvenanceProblem,
        (
            ("state", str),
            ("package", str),
            ("version", str),
            ("filename", str),
            ("source_url", str),
            ("detail", str),
            ("status_code", _optional(int)),
        ),
    ),
    RecordLayout(
        "source_publishers", se.SourcePublisherInspection,
        (
            ("state", str),
            ("detail", str),
            ("repository", _optional(str)),
            ("records", SequenceOf(Either((RecordRef("file_provenance"), RecordRef("file_provenance_problem"))))),
        ),
    ),
    RecordLayout(
        "package_source_association", se.PackageSourceAssociation,
        (
            ("release", RecordRef("package_release")),
            ("repository", str),
            ("declarations", _seq("project_url")),
            ("ignored_links", _seq("project_url")),
            ("provenance", RecordRef("source_publishers")),
            ("basis", str),
        ),
    ),
    RecordLayout(
        "source_import", ImportFact,
        (
            ("source_id", str),
            ("line", int),
            ("module", str),
            ("member", _optional(str)),
            ("alias", _optional(str)),
            ("relative_level", int),
            ("module_level", bool),
        ),
    ),
    RecordLayout(
        "source_binding_step", BindingTraceStep,
        (
            ("source_id", str),
            ("scope", str),
            ("line", int),
            ("column", int),
            ("end_line", int),
            ("end_column", int),
            ("operation", str),
            ("name", str),
            ("origin", _optional(str)),
            ("input_name", _optional(str)),
        ),
    ),
    RecordLayout(
        "source_binding", BindingAssessment,
        (
            ("state", str),
            ("possible_imports", _STRINGS),
            ("unknown_possible", bool),
            ("unbound_possible", bool),
            ("scope", str),
            ("reasons", _STRINGS),
            ("trace", _seq("source_binding_step")),
        ),
    ),
    RecordLayout(
        "source_reference", ReferenceFact,
        (
            ("source_id", str),
            ("line", int),
            ("kind", str),
            ("expression", str),
            ("lexical_import", _optional(str)),
            ("binding_limit", _optional(str)),
            ("keyword_names", _STRINGS),
            ("positional_count", int),
            ("binding", _optional(RecordRef("source_binding"))),
        ),
    ),
    RecordLayout(
        "module_source_request", se.ModuleSourceRequest,
        (
            ("package", str),
            ("version", str),
            ("module", str),
            ("version_basis", LiteralValues(("old_dependency", "proposed_dependency", "constraint_sample", "explicit_version"))),
            ("origin", Either((RecordRef("source_import"), RecordRef("source_reference"), type(None)))),
        ),
    ),
    RecordLayout(
        "source_tag_commit", se.SourceTagCommit,
        (
            ("tag", str),
            ("revision", str),
        ),
    ),
    RecordLayout(
        "github_tag_commit", GitHubTagCommitEvidence,
        (
            ("state", LiteralValues(("available",))),
            ("repository", str),
            ("requested_tag", str),
            ("tag_ref", str),
            ("tag_object_type", LiteralValues(("commit", "tag"))),
            ("tag_object_sha", str),
            ("resolved_commit_sha", str),
            ("peeled_tag_object_shas", _STRINGS),
            ("retrieved_at", datetime),
        ),
        ("state",),
    ),
    RecordLayout(
        "module_source_receipt", se.ModuleSourceReceipt,
        (
            ("request", RecordRef("module_source_request")),
            ("state", LiteralValues(("module_examined", "refused", "unavailable"))),
            ("problem", _optional(RecordRef("source_problem"))),
            ("repository", _optional(str)),
            ("revision", _optional(str)),
            ("path", _optional(str)),
            ("sha256", _optional(str)),
            ("utf8_bytes", _optional(int)),
            ("association_basis", _optional(str)),
            ("provenance_state", _optional(str)),
            ("tag_commits", _seq("source_tag_commit")),
            ("metadata", _optional(RecordRef("source_metadata"))),
            ("gaps", _seq("source_gap")),
            ("association", _optional(RecordRef("package_source_association"))),
            ("tags", _seq("github_tag_commit")),
            ("retention_gaps", _STRINGS),
        ),
    ),
    RecordLayout(
        "source_sample_selection", se.SourceSampleSelection,
        (
            ("candidate", RecordRef("source_import_candidate")),
            ("depth", int),
            ("version", str),
            ("selection", str),
            ("repository", str),
            ("revision", str),
            ("path", str),
            ("sha256", str),
        ),
    ),
    RecordLayout(
        "source_material_omission", se.SourceMaterialOmission,
        (
            ("repository", str),
            ("revision", str),
            ("path", str),
            ("role", str),
            ("reason", str),
        ),
    ),
    RecordLayout(
        "source_acquisition_work", se.SourceAcquisitionWork,
        (
            ("release_identities", SequenceOf(_STRINGS)),
            ("module_attempts", int),
            ("source_bytes", int),
        ),
    ),
    RecordLayout(
        "source_acquisition_limits", se.SourceAcquisitionLimits,
        (
            ("github_requests", int),
            ("provider_requests", int),
            ("response_bytes", int),
            ("aggregate_bytes", int),
            ("elapsed_seconds", RecordRef("measured_duration")),
            ("source_request_reserve", int),
            ("target_file_attempts", int),
            ("adapter_candidate_attempts", int),
        ),
    ),
    RecordLayout(
        "source_request_event", se.SourceRequestEvent,
        (
            ("stage", str),
            ("host", str),
            ("path", str),
            ("github_requests", int),
            ("provider_requests", int),
            ("decoded_body_bytes", int),
            ("status", _optional(int)),
            ("state", str),
            ("reason", _optional(str)),
        ),
    ),
    RecordLayout(
        "source_acquisition_stop", se.SourceAcquisitionStop,
        (
            ("stage", str),
            ("reason", str),
        ),
    ),
    RecordLayout(
        "source_retry_decision", se.SourceRetryDecision,
        (
            ("after_provider_request", int),
            ("retry_provider_request", _optional(int)),
            ("reason", str),
            ("state", str),
        ),
    ),
    RecordLayout(
        "source_transport_receipt", se.SourceTransportReceipt,
        (
            ("limits", RecordRef("source_acquisition_limits")),
            ("auth", LiteralValues(("anonymous", "token-env"))),
            ("github_requests", int),
            ("provider_requests", int),
            ("decoded_body_bytes", int),
            ("elapsed", RecordRef("measured_duration")),
            ("deadline_kind", str),
            ("stops", _seq("source_acquisition_stop")),
            ("requests", _seq("source_request_event")),
            ("retry_policy", LiteralValues(("none", "pypi-get-timeout-once/1"))),
            ("retry_decisions", _seq("source_retry_decision")),
        ),
    ),
    RecordLayout(
        "source_method_file", se.SourceMethodFile,
        (
            ("path", str),
            ("sha256", str),
        ),
    ),
    RecordLayout(
        "source_acquisition_receipt", se.SourceAcquisitionReceipt,
        (
            ("origin", LiteralValues(("native_observation", "retained_experiment", "controlled_observation"))),
            ("state", LiteralValues(("complete", "partial", "failed"))),
            ("observed_at", _optional(datetime)),
            ("target", _optional(RecordRef("target_source_receipt"))),
            ("module_requests", _seq("module_source_receipt")),
            ("samples", _seq("source_sample_selection")),
            ("problems", _seq("source_problem")),
            ("omitted_candidates", _seq("source_import_candidate")),
            ("deferred_candidates", _seq("source_import_candidate")),
            ("unexamined_modules", _STRINGS),
            ("material_omissions", _seq("source_material_omission")),
            ("adapter_limitations", _STRINGS),
            ("source_work", _optional(RecordRef("source_acquisition_work"))),
            ("transport", _optional(RecordRef("source_transport_receipt"))),
            ("method_files", _seq("source_method_file")),
            ("retention_gaps", _STRINGS),
        ),
    ),
)
_VALUES = NativeValueCodec(_LAYOUTS)
_MOVE_VALUES = NativeValueCodec(tuple(
    replace(layout, fields=layout.fields + (("repository_move", _optional(RecordRef("repository_move"))),))
    if layout.variant == "module_source_receipt" else layout for layout in _LAYOUTS
) + (
    RecordLayout("tag_repository_redirect", GitHubTagRepositoryRedirect, (
        ("repository", str), ("requested_tag", str), ("repository_id", int), ("path", str),
    )),
    RecordLayout("repository_move", se.SourceRepositoryMove, (
        ("redirect", RecordRef("tag_repository_redirect")),
        ("canonical_repository", _optional(str)), ("verified", bool),
        ("prior_tag", _optional(RecordRef("github_tag_commit"))),
    )),
))
_RECEIPT = RecordRef("source_acquisition_receipt")

_PYTHON_SCENARIO_LAYOUTS = (
    RecordLayout("sample_python_job", SelectedSamplePythonJob, (("workflow_path", str), ("job", str))),
    RecordLayout("file_requires_python", PublishedFileRequiresPython, (
        ("filename", str), ("sha256", str), ("requires_python", _optional(str)), ("yanked", _optional(bool)),
    )),
    RecordLayout("sample_file_python", SampleFilePythonAssessment, (
        ("file", RecordRef("file_requires_python")),
        ("state", LiteralValues(("overlaps", "excludes", "unknown", "yanked"))),
        ("witness_patch", _optional(str)),
    )),
    RecordLayout("sample_release_python", SampleReleasePythonAssessment, (
        ("package", str), ("version", str), ("files", _seq("sample_file_python")),
    )),
    RecordLayout("sample_python_scenario", SamplePythonScenario, (
        ("selection", RecordRef("sample_python_job")), ("repository", str), ("revision", str),
        ("dependency_path", _optional(str)), ("workflow_text", _optional(str)),
        ("python_line", _optional(str)), ("python_location", _optional(str)), ("reason", str),
        ("releases", _seq("sample_release_python")),
    )),
)
_PYTHON_SCENARIO_VALUES = NativeValueCodec(_PYTHON_SCENARIO_LAYOUTS)
_RANKED_SCENARIO_VALUES = NativeValueCodec(tuple(
    replace(layout, fields=layout.fields + (("rank_adapters", bool),))
    if layout.variant == "sample_python_job" else
    replace(layout, fields=layout.fields + (("rank_decisions", _seq("adapter_rank_decision")),))
    if layout.variant == "sample_python_scenario" else layout
    for layout in _PYTHON_SCENARIO_LAYOUTS
) + (
    RecordLayout("simple_index_basis", SimpleIndexBasis, (
        ("source_url", str), ("sha256", str), ("serial", int), ("observed_at", datetime), ("file_count", int),
    )),
    RecordLayout("adapter_rank_decision", AdapterRankDecision, (
        ("package", str), ("constraint", str), ("state", LiteralValues(("pending", "confirmed", "unresolved"))),
        ("reason", str), ("index", _optional(RecordRef("simple_index_basis"))),
        ("checked_versions", int), ("unclassified_files", int), ("version", _optional(str)),
        ("file", _optional(RecordRef("sample_file_python"))), ("exact_file", _optional(RecordRef("file_requires_python"))),
        ("blocked_version", _optional(str)),
    )),
))
_PYTHON_SCENARIO = RecordRef("sample_python_scenario")

_ADAPTER_CALL_VALUES = NativeValueCodec((
    DURATION_LAYOUT,
    RecordLayout("adapter_call_span", SourceSpan, (
        ("line", int), ("column", int), ("end_line", int), ("end_column", int),
    )),
    RecordLayout("adapter_call_path", se.AdapterCallPath, (
        ("module", str), ("target_file", str), ("target_span", RecordRef("adapter_call_span")),
        ("adapter_file", str), ("adapter_span", RecordRef("adapter_call_span")),
        ("import_line", int), ("imported_binding", str),
    )),
    RecordLayout("adapter_call_acquisition", se.AdapterCallAcquisition, (
        ("state", LiteralValues(("pending", "unresolved", "acquiring", "examined", "partial"))),
        ("reason", str), ("preliminary_input_sha256", _optional(str)),
        ("preliminary_elapsed", _optional(RecordRef("measured_duration"))),
        ("module", _optional(str)), ("paths", _seq("adapter_call_path")),
    )),
))
_ADAPTER_CALLS = RecordRef("adapter_call_acquisition")


def _digest(value):
    if type(value) is not str or re.fullmatch(r"[0-9a-f]{64}", value) is None:
        raise ValueError("Invalid source digest.")


def _count(value):
    if type(value) is not int or value < 0:
        raise ValueError("Invalid source work count.")


def _validate_transport(value):
    if value is None:
        return
    limits = value.limits
    # Same qualified finite policy ceilings; this reader does not select defaults
    # or reinterpret the account's provider quota as an application work budget.
    for item, maximum in ((limits.github_requests, 200), (limits.provider_requests, 400),
            (limits.response_bytes, 8 * 1024 * 1024), (limits.aggregate_bytes, 64 * 1024 * 1024),
            (limits.source_request_reserve, 199), (limits.target_file_attempts, 200), (limits.adapter_candidate_attempts, 12)):
        if type(item) is not int or not 0 < item <= maximum:
            raise ValueError("Invalid retained acquisition policy.")
    if not 0 < limits.elapsed_seconds.seconds <= 300 or limits.source_request_reserve >= limits.github_requests or limits.provider_requests < limits.github_requests:
        raise ValueError("Invalid acquisition policy relationship.")
    if value.deadline_kind != "cooperative_monotonic_checks_and_bounded_socket_timeouts":
        raise ValueError("Unsupported acquisition deadline contract.")
    if len(value.requests) != value.provider_requests or len(value.requests) > limits.provider_requests:
        raise ValueError("Transport request count mismatch.")
    github = body = 0
    for index, event in enumerate(value.requests, 1):
        if event.host not in {"api.github.com", "pypi.org"} or event.state not in {"started", "received", "failed"}:
            raise ValueError("Invalid transport event.")
        github += event.host == "api.github.com"
        _count(event.decoded_body_bytes)
        body += event.decoded_body_bytes
        if (event.github_requests, event.provider_requests) != (github, index):
            raise ValueError("Transport event accounting mismatch.")
        if event.status is not None and not 100 <= event.status <= 599:
            raise ValueError("Invalid transport response status.")
        if event.state == "received" and event.decoded_body_bytes > limits.response_bytes:
            raise ValueError("Over-limit body labelled received.")
        if len(event.path) > 512 or len(event.stage) > 512 or event.reason is not None and len(event.reason) > 128:
            raise ValueError("Transport event label capacity.")
    if github != value.github_requests or github > limits.github_requests or body != value.decoded_body_bytes:
        raise ValueError("Transport aggregate accounting mismatch.")
    if len(value.stops) > 64 or value.elapsed.seconds > 86400:
        raise ValueError("Transport stop/measurement capacity.")
    if value.retry_policy == "none" and value.retry_decisions or len(value.retry_decisions) > 2:
        raise ValueError("Unsupported timeout recovery.")
    previous = 0
    for retry in value.retry_decisions:
        first, second = retry.after_provider_request, retry.retry_provider_request
        if not previous < first <= len(value.requests) or retry.reason != "timeout_before_response":
            raise ValueError("Invalid recovery origin.")
        event = value.requests[first - 1]
        if event.host != "pypi.org" or event.state != "failed" or event.status is not None:
            raise ValueError("Invalid recovery failed request.")
        if second is None:
            if retry.state != "not_dispatched" or not value.stops:
                raise ValueError("Invalid undispatched recovery.")
            previous = first
        else:
            if second != first + 1 or second > len(value.requests) or retry.state != "dispatched":
                raise ValueError("Invalid recovery dispatch.")
            following = value.requests[second - 1]
            if (following.host, following.path, following.stage) != (event.host, event.path, event.stage):
                raise ValueError("Recovery changed request scope.")
            previous = second


def _validate_origin(origin):
    if origin is None:
        return
    if origin.line < 1 or not origin.source_id:
        raise ValueError("Invalid source request origin.")
    if isinstance(origin, ImportFact):
        if origin.relative_level < 0:
            raise ValueError("Invalid import origin level.")
        return
    if origin.positional_count < 0:
        raise ValueError("Invalid reference argument count.")
    binding = origin.binding
    if binding is not None:
        if (binding.state != binding_state(binding.possible_imports, binding.unknown_possible, binding.unbound_possible)
            or not 1 <= len(binding.trace) <= 128 or len(binding.possible_imports) > 32):
            raise ValueError("Invalid retained origin binding.")
        if binding.possible_imports != tuple(sorted(set(binding.possible_imports))):
            raise ValueError("Noncanonical retained origin alternatives.")
        for step in binding.trace:
            if step.source_id != origin.source_id or step.line < 1 or step.column < 0 or step.end_column < 0 or (step.end_line, step.end_column) <= (step.line, step.column):
                raise ValueError("Foreign retained origin trace.")


def _validate_moved_repository(module, transport):
    move = module.repository_move
    redirect = move.redirect
    association = module.association
    if (association is None or transport is None
        or validate_repository(redirect.repository) != redirect.repository
        or association.repository.casefold() != redirect.repository.casefold()
        or repository_move_redirect(redirect.repository, redirect.requested_tag, GITHUB_API_ROOT + redirect.path) != redirect):
        raise ValueError("Repository move lacks its exact declaration or redirect identity.")
    if not redirect.requested_tag or redirect.requested_tag.strip() != redirect.requested_tag:
        raise ValueError("Invalid repository move tag spelling.")
    canonical = move.canonical_repository
    if canonical is not None and (validate_repository(canonical) != canonical
        or canonical.split("/")[1] in {".", ".."}
        or canonical.casefold() == association.repository.casefold()):
        raise ValueError("Invalid canonical repository in move evidence.")
    if move.verified and canonical is None:
        raise ValueError("Verified repository move lacks its canonical name.")

    # Move verification uses consecutive charged requests through the same session.
    # The destination from the header is retained as data and is never fetched.
    expected = [(tag_reference_path(redirect.repository, redirect.requested_tag), 301)]
    if canonical is not None:
        expected.append((f"/repositories/{redirect.repository_id}", 200))
    if move.verified:
        expected.append((f"/repos/{canonical}", 200))
    width = len(expected)
    def matches(event, path, status):
        return (event.host == "api.github.com" and event.state == "received" and event.path == path
                and (event.status == 301 if status == 301 else event.status is not None and 200 <= event.status < 300))

    verification_end = next((start + width for start in range(len(transport.requests) - width + 1)
        if all(matches(event, *pair) for event, pair in
               zip(transport.requests[start:start + width], expected, strict=True))), None)
    if verification_end is None:
        raise ValueError("Repository move evidence does not match the transport receipt.")

    if move.prior_tag is not None:
        prior = move.prior_tag
        validate_commit_sha(prior.resolved_commit_sha)
        if (prior.repository != redirect.repository or prior.requested_tag != module.request.version
            or prior.tag_ref != f"refs/tags/{prior.requested_tag}"
            or redirect.requested_tag != "v" + module.request.version
            or (module.state == "module_examined" and not any(
                (t.requested_tag, t.resolved_commit_sha) == (prior.requested_tag, prior.resolved_commit_sha)
                for t in module.tags))):
            raise ValueError("Repository move disagrees with the earlier exact tag observation.")
    if not move.verified:
        if module.state == "module_examined" or module.tags or module.tag_commits:
            raise ValueError("Unverified repository move cannot admit canonical tags or text.")
        return association.repository
    spellings = {module.request.version, "v" + module.request.version}
    if any(t.repository != canonical or t.requested_tag not in spellings or t.tag_ref != f"refs/tags/{t.requested_tag}"
           for t in module.tags):
        raise ValueError("Canonical source tags do not match the moved repository or requested release.")
    if any(not any(matches(event, tag_reference_path(canonical, t.requested_tag), 200)
                   for event in transport.requests[verification_end:]) for t in module.tags):
        raise ValueError("Canonical source tags lack their exact transport observations.")
    return canonical


def _validate_receipt(receipt):
    if len(receipt.module_requests) > 512 or len(receipt.samples) > 256 or len(receipt.problems) > 256:
        raise ValueError("Acquisition receipt capacity exceeded.")
    _validate_transport(receipt.transport)
    for method in receipt.method_files:
        _digest(method.sha256)
    if receipt.origin == "retained_experiment" and "full_original_acquisition_observations_not_retained" not in receipt.retention_gaps:
        raise ValueError("Missing historical acquisition gap.")
    target = receipt.target
    if target is not None:
        validate_repository(target.repository)
        validate_commit_sha(target.revision)
        validate_commit_sha(target.tree_sha)
        _count(target.inventory_entries)
        _count(target.examined_bytes)
        if len(target.files) > 200 or len({f.source_id for f in target.files}) != len(target.files):
            raise ValueError("Invalid target acquisition membership.")
        for file in target.files:
            _digest(file.sha256)
            _count(file.utf8_bytes)
        if sum(f.utf8_bytes for f in target.files) != target.examined_bytes:
            raise ValueError("Target acquisition byte accounting mismatch.")
        for candidate in target.candidates:
            if candidate.import_line < 1 or candidate.declaration not in target.declarations:
                raise ValueError("Foreign import candidate declaration.")
    for module in receipt.module_requests:
        request = module.request
        if not request.package or not request.version or not all(p.isidentifier() for p in request.module.split(".")):
            raise ValueError("Invalid module source question.")
        _validate_origin(request.origin)
        expected_repository = module.association.repository if module.association else None
        if module.repository_move is not None:
            expected_repository = _validate_moved_repository(module, receipt.transport)
        if module.state != "module_examined":
            if module.problem is None:
                raise ValueError("Unavailable source lacks its problem.")
            # Association/metadata/tag observations may precede a failed file
            # read or material refusal. Keep those partial premises; they do not
            # admit text or become a successful source merely by being present.
            if module.repository is not None:
                validate_repository(module.repository)
            if module.revision is not None:
                validate_commit_sha(module.revision)
            if module.sha256 is not None:
                _digest(module.sha256)
            if module.utf8_bytes is not None:
                _count(module.utf8_bytes)
            if module.metadata is not None and (module.metadata.package, module.metadata.version) != (request.package, request.version):
                raise ValueError("Partial source metadata/request mismatch.")
            if module.association is not None:
                association = module.association
                if (association.release.normalized_package, association.release.requested_version) != (request.package, request.version):
                    raise ValueError("Partial source association/request mismatch.")
                if module.repository is not None and expected_repository != module.repository:
                    raise ValueError("Partial source association scope mismatch.")
            for tag in module.tag_commits:
                validate_commit_sha(tag.revision)
            if module.tags and {(t.requested_tag, t.resolved_commit_sha) for t in module.tags} != {(t.tag, t.revision) for t in module.tag_commits}:
                raise ValueError("Partial tag observations/summary mismatch.")
            continue
        if module.problem is not None or module.metadata is None or module.utf8_bytes is None:
            raise ValueError("Missing successful source observation.")
        validate_repository(module.repository)
        validate_commit_sha(module.revision)
        _digest(module.sha256)
        _count(module.utf8_bytes)
        if (module.metadata.package, module.metadata.version) != (request.package, request.version):
            raise ValueError("Source metadata/request identity mismatch.")
        if not module.association_basis or not module.provenance_state:
            raise ValueError("Missing source association receipt.")
        if (not module.tag_commits and not (receipt.origin == "retained_experiment" and "tag_commit_summary_not_retained" in module.retention_gaps)
            or any(t.revision != module.revision for t in module.tag_commits)):
            raise ValueError("Source revision/tag receipt mismatch.")
        for tag in module.tag_commits:
            validate_commit_sha(tag.revision)
        if module.association is None:
            if receipt.origin == "native_observation" or "full_association_observations_not_retained" not in module.retention_gaps:
                raise ValueError("Missing full source association observations.")
        else:
            association = module.association
            if (expected_repository != module.repository or association.basis != module.association_basis
                or association.provenance.state != module.provenance_state
                or (association.release.normalized_package, association.release.requested_version) != (request.package, request.version)):
                raise ValueError("Source association/request mismatch.")
            if not association.declarations or any(c not in association.release.project_urls for c in (*association.declarations, *association.ignored_links)):
                raise ValueError("Source declarations outside retained release.")
        if module.tags:
            if {(t.requested_tag, t.resolved_commit_sha) for t in module.tags} != {(t.tag, t.revision) for t in module.tag_commits} or any(t.repository != module.repository for t in module.tags):
                raise ValueError("Full tag observations/summary mismatch.")
        elif receipt.origin == "native_observation" or "full_tag_observations_not_retained" not in module.retention_gaps:
            raise ValueError("Missing full tag observations.")
    if receipt.source_work is not None:
        work = receipt.source_work
        _count(work.module_attempts)
        _count(work.source_bytes)
        if len(work.release_identities) > 4 or any(len(identity) != 2 or not all(identity) for identity in work.release_identities):
            raise ValueError("Invalid source work release identities.")


def _validate_catalog_joins(value):
    catalog, receipt = value.catalog, value.acquisition
    if catalog is None:
        if value.modules:
            raise ValueError("Source roles without a retained catalog.")
        return
    target = catalog.target
    if target is None:
        raise ValueError("Source catalog lacks exact investigation target.")
    if receipt.target is not None and (receipt.target.repository, receipt.target.revision) != (target.repository, target.head_sha):
        raise ValueError("Target acquisition receipt scope mismatch.")
    scopes = {s.source_id: s for s in catalog.scopes}
    modules = {(m.source_id, m.path): m for m in value.modules}
    target_files = {f.source_id: f for f in receipt.target.files} if receipt.target else {}
    for file in catalog.files:
        scope = scopes[file.source_id]
        digest = sha256(file.content.encode()).hexdigest()
        size = len(file.content.encode())
        module = modules.get((file.source_id, file.path))
        if module is not None and module.role != "target_repository":
            matches = [r for r in receipt.module_requests if r.state == "module_examined"
                and (r.repository, r.revision, r.path, r.sha256, r.utf8_bytes) == (scope.repository, scope.revision, file.path, digest, size)
                and (r.request.package, r.request.version, r.request.version_basis) == (module.package, module.version, module.role)]
            if not matches or not any(tuple(sorted({d.package for d in r.metadata.requirements})) == module.dependencies for r in matches):
                raise ValueError("Dependency text/role lacks its exact acquisition receipt.")
        else:
            identity = f"{scope.repository}@{scope.revision}:{file.path}"
            observed = target_files.get(identity)
            if (scope.repository, scope.revision) != (target.repository, target.head_sha) or observed is None or (observed.sha256, observed.utf8_bytes) != (digest, size):
                raise ValueError("Target text lacks its exact acquisition receipt.")
            if module is not None and tuple(sorted({d.package for d in receipt.target.declarations})) != module.dependencies:
                raise ValueError("Target module/declaration membership mismatch.")


def _validate_sample_python(value):
    scenario = value.sample_python
    if scenario is None:
        return
    _validate_rank_decisions(value, scenario)
    validate_repository(scenario.repository)
    if validate_commit_sha(scenario.revision) != scenario.revision:
        raise ValueError("Noncanonical Python scenario revision.")
    if (value.catalog is not None
            and (scenario.repository, scenario.revision) != (value.catalog.target.repository, value.catalog.target.head_sha)):
        raise ValueError("Python scenario belongs to another source target.")
    if scenario.dependency_path is not None and repository_relative_parts(scenario.dependency_path) is None:
        raise ValueError("Invalid selected Python scenario dependency path.")
    if scenario.workflow_text is not None and len(scenario.workflow_text.encode()) > WORKFLOW_TEXT_LIMIT:
        raise ValueError("Python scenario workflow exceeded its retention limit.")
    if not scenario.reason or len(scenario.reason) > 128:
        raise ValueError("Incomplete Python scenario reason.")
    if scenario.reason != "declared_python_line":
        if scenario.python_line is not None or scenario.python_location is not None or scenario.releases:
            raise ValueError("Unresolved Python scenario carries a release verdict.")
        return
    if (not scenario.workflow_text or not scenario.python_location or not scenario.dependency_path
            or not PYTHON_LINE.fullmatch(scenario.python_line or "")):
        raise ValueError("Declared Python scenario lacks its workflow or declaration.")
    expected = {(m.package, m.version) for m in value.modules if m.role == "constraint_sample"}
    identities = [(release.package, release.version) for release in scenario.releases]
    if len(identities) > 4 or len(identities) != len(expected) or set(identities) != expected:
        raise ValueError("Python scenario release identities differ from the retained samples.")
    associations = {(r.request.package, r.request.version): r.association.release
                    for r in value.acquisition.module_requests
                    if r.request.version_basis == "constraint_sample" and r.association is not None}
    for release in scenario.releases:
        if not release.files:
            continue
        observed = associations.get((release.package, release.version))
        file_ids = [(row.file.filename, row.file.sha256) for row in release.files]
        if (len(file_ids) > MAX_FILE_PYTHON_DECLARATIONS or observed is None
                or len(file_ids) != len(observed.distribution_files)
                or set(file_ids) != {(f.filename, f.sha256) for f in observed.distribution_files}):
            raise ValueError("Python scenario file identities differ from the exact published release.")
        for row in release.files:
            if row.file.requires_python is not None and not 0 < len(row.file.requires_python) <= MAX_REQUIRES_PYTHON_TEXT:
                raise ValueError("Invalid bounded Requires-Python declaration.")
            if (row.state == "yanked") != (row.file.yanked is True):
                raise ValueError("Python scenario yank state differs from the recorded file.")
            if (row.state in {"overlaps", "excludes"}
                    and (row.file.yanked is not False or not row.file.requires_python)):
                raise ValueError("Conclusive Python scenario file state lacks a declaration.")
            if (row.state == "overlaps") != (row.witness_patch is not None) or (
                row.witness_patch is not None and re.fullmatch(
                    re.escape(scenario.python_line) + r"\.(?:0|[1-9][0-9]*)", row.witness_patch) is None
            ):
                raise ValueError("Invalid stable Python patch witness.")


def _validate_rank_decisions(value, scenario):
    ranked = scenario.selection.rank_adapters
    decisions = scenario.rank_decisions
    if not ranked:
        if decisions:
            raise ValueError("Annotation-only source evidence carries ranked decisions.")
        return
    if decisions and not scenario.python_line:
        raise ValueError("Ranked decisions lack a declared Python line.")
    keys = {(item.package, item.constraint) for item in decisions}
    if len(decisions) != len(keys) or len(keys) > 12:
        raise ValueError("Invalid ranked adapter decision count or identity.")
    confirmed = {}
    confirmed_constraints = set()
    for item in decisions:
        if (not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", item.package)
                or not item.reason or len(item.reason) > 128 or len(item.constraint) > 1024
                or not 0 <= item.checked_versions <= MAX_INDEX_VERSIONS + MAX_INDEX_FILES):
            raise ValueError("Invalid ranked adapter decision scope.")
        index = item.index
        if index is None:
            if item.state != "unresolved" or item.checked_versions or item.unclassified_files or item.file or item.blocked_version:
                raise ValueError("Ranked selection lacks an index basis.")
        else:
            _digest(index.sha256)
            if (index.source_url != simple_index_url(item.package) or index.serial < 0
                    or not 0 <= item.unclassified_files <= index.file_count <= MAX_INDEX_FILES):
                raise ValueError("Ranked index observation belongs to another scope.")
        if (item.file is None) != (item.version is None) or (item.file is not None and item.blocked_version):
            raise ValueError("Incomplete ranked adapter file selection.")
        if item.file is not None:
            file = item.file.file
            _digest(file.sha256)
            if (not item.checked_versions or not 0 < len(item.version) <= 128
                    or not 0 < len(file.filename) <= 512 or file.yanked is not False
                    or not file.requires_python or len(file.requires_python) > MAX_REQUIRES_PYTHON_TEXT
                    or item.file.state != "overlaps" or not re.fullmatch(
                        re.escape(scenario.python_line) + r"\.(?:0|[1-9][0-9]*)", item.file.witness_patch or ""
                    )):
                raise ValueError("Invalid ranked Python file predicate.")
        if item.state == "confirmed":
            if item.file is None or item.exact_file != item.file.file:
                raise ValueError("Confirmed ranked adapter lacks the exact release file join.")
            confirmed[item.package, item.version] = item.exact_file
            confirmed_constraints.add((item.package, item.constraint, item.version))
        elif item.state == "pending" and (item.file is None or item.exact_file is not None):
            raise ValueError("Invalid pending ranked adapter file.")
        elif item.exact_file is not None and (item.file is None or item.exact_file.filename != item.file.file.filename):
            raise ValueError("Ranked release mismatch refers to another filename.")
    for sample in value.acquisition.samples:
        declaration = sample.candidate.declaration
        if (sample.selection != RANKED_SAMPLE_BASIS
                or (declaration.package, declaration.specifier, sample.version) not in confirmed_constraints):
            raise ValueError("Ranked sample selection lacks its recorded constraint decision.")
    for module in value.modules:
        if module.role == "constraint_sample" and (module.package, module.version) not in confirmed:
            raise ValueError("Ranked sample source lacks its confirmed release file.")
    for release in scenario.releases:
        exact = confirmed.get((release.package, release.version))
        if exact is None or not any(row.file == exact for row in release.files):
            raise ValueError("Ranked sample annotation does not preserve the joined file.")


def _validate_adapter_calls(value):
    observed = value.adapter_calls
    if observed is None:
        return
    reasons = {
        "pending": {"source_preparation_pending"},
        "unresolved": {
            "insufficient_pair_reserve", "insufficient_analysis_file_capacity", "source_context_unavailable",
            "adapter_source_unavailable", "preliminary_analysis_unavailable", "analysis_time_exhausted",
            "call_path_limit", "multiple_changed_modules", "no_reached_changed_call",
        },
        "acquiring": {"paired_acquisition_pending"},
        "examined": {"both_versions_examined"},
        "partial": {"incomplete_exact_pair"},
    }
    if observed.reason not in reasons[observed.state] or value.acquisition.origin != "native_observation":
        raise ValueError("Invalid adapter call acquisition disposition.")
    if (observed.preliminary_input_sha256 is None) != (observed.preliminary_elapsed is None):
        raise ValueError("Incomplete adapter call preliminary analysis.")
    if observed.preliminary_elapsed is not None:
        _digest(observed.preliminary_input_sha256)
        if observed.preliminary_elapsed.scope != ADAPTER_CALL_ANALYSIS_SCOPE:
            raise ValueError("Invalid adapter call preliminary analysis scope.")
    has_module = observed.state in {"acquiring", "examined", "partial"}
    if has_module != (observed.module is not None):
        raise ValueError("Adapter call disposition belongs to another question.")
    allowed_paths = has_module or observed.reason in {
        "call_path_limit", "multiple_changed_modules", "analysis_time_exhausted",
    }
    if (len(set(observed.paths)) != len(observed.paths) or len(observed.paths) > value.analysis_limits.max_pairs
            or observed.paths and (not allowed_paths or observed.preliminary_elapsed is None or value.catalog is None)):
        raise ValueError("Invalid adapter call path coverage.")
    modules = {path.module for path in observed.paths}
    if has_module and modules != {observed.module} or observed.reason == "multiple_changed_modules" and len(modules) < 2:
        raise ValueError("Adapter call module differs from its retained paths.")
    if not observed.paths:
        return

    catalog = value.catalog
    package = catalog.target.normalized_package
    roles = {(m.source_id, m.path): m.role for m in value.modules}
    scopes = {scope.source_id: scope for scope in catalog.scopes}
    retained = {catalog.descriptor(f)["file_id"]: (f, roles.get((f.source_id, f.path))) for f in catalog.files}
    source_lines = {}
    def checked_file(file_id, span, expected_role):
        item = retained.get(file_id)
        if item is None or item[1] != expected_role:
            raise ValueError("Adapter call path lacks its retained source role.")
        file = item[0]
        if file_id not in source_lines:
            text = file.content.replace("\r\n", "\n").replace("\r", "\n")
            source_lines[file_id] = tuple(len(line.encode()) for line in text.split("\n"))
        lines = source_lines[file_id]
        if (not 1 <= span.line <= span.end_line <= len(lines)
                or not 0 <= span.column <= lines[span.line - 1]
                or not 0 <= span.end_column <= lines[span.end_line - 1]
                or (span.line, span.column) >= (span.end_line, span.end_column)):
            raise ValueError("Adapter call coordinates exceed retained source.")
        return file, len(lines)

    retained_imports = set()
    for path in observed.paths:
        checked_file(path.target_file, path.target_span, "target_repository")
        file, line_count = checked_file(path.adapter_file, path.adapter_span, "constraint_sample")
        if (len(path.module) > 512 or len(path.imported_binding) > 1024
                or not all(part.isidentifier() for part in path.module.split("."))
                or normalize_package_name(path.module.split(".")[0]) != package
                or not (path.imported_binding == path.module or path.imported_binding.startswith(path.module + "."))
                or not 1 <= path.import_line <= line_count):
            raise ValueError("Invalid changed-package import in adapter call acquisition.")
        scope = scopes[file.source_id]
        retained_imports.add((f"{scope.repository}@{scope.revision}:{file.path}", path.import_line))

    if has_module:
        rows = [r for r in value.acquisition.module_requests if (r.request.package, r.request.module) == (package, observed.module)]
        if (len(rows) > PAIR_MODULE_ATTEMPTS or len({r.request.version_basis for r in rows}) != len(rows)
                or any(not isinstance(r.request.origin, ImportFact)
                       or (r.request.origin.source_id, r.request.origin.line) not in retained_imports
                       or r.request.origin.module != observed.module
                       or r.request.version_basis not in {"old_dependency", "proposed_dependency"}
                       or r.request.version != (catalog.target.old_version if r.request.version_basis == "old_dependency"
                                                 else catalog.target.proposed_version) for r in rows)):
            raise ValueError("Adapter call acquisition lacks its original changed-module questions.")
        complete = len(rows) == PAIR_MODULE_ATTEMPTS and all(r.state == "module_examined" for r in rows)
        if observed.state != "acquiring" and (observed.state == "examined") != complete:
            raise ValueError("Adapter call acquisition differs from its exact-version receipts.")


def source_codec_version(value: se.CallerSignatureSources) -> int:
    if value.adapter_calls is not None:
        return 5
    if value.sample_python is not None:
        return 4 if value.sample_python.selection.rank_adapters else 3
    return 2 if any(module.repository_move is not None for module in value.acquisition.module_requests) else 1


def encode_sources(value: se.CallerSignatureSources | None, *, version: int = 1) -> bytes:
    if value is None:
        return json_bytes(None)
    if version != source_codec_version(value):
        raise ValueError("Caller/signature source representation does not match its observations.")
    layout = _VALUES if version == 1 else _MOVE_VALUES
    row = dict(format=_SOURCE_FORMATS[version],
        catalog=parse_json(encode_source_catalog(value.catalog)) if value.catalog else None,
        modules=[module_fields(m) for m in value.modules], limits=encode_analysis_limits(value.analysis_limits),
        acquisition=parse_json(layout.encode(value.acquisition, _RECEIPT)))
    if version in {3, 4, 5}:
        scenario_layout = _PYTHON_SCENARIO_VALUES if version == 3 else _RANKED_SCENARIO_VALUES
        row["sample_python"] = (parse_json(scenario_layout.encode(value.sample_python, _PYTHON_SCENARIO))
                                if value.sample_python is not None else None)
    if version == 5:
        row["adapter_calls"] = parse_json(_ADAPTER_CALL_VALUES.encode(value.adapter_calls, _ADAPTER_CALLS))
    payload = json_bytes(row)
    decoded = decode_sources(payload, version=version)
    if ((decoded.catalog.identity if decoded.catalog else None) != (value.catalog.identity if value.catalog else None)
            or decoded.modules != value.modules or decoded.acquisition != value.acquisition
            or decoded.analysis_limits != value.analysis_limits or decoded.sample_python != value.sample_python
            or decoded.adapter_calls != value.adapter_calls):
        raise ValueError("Source family encoding changed retained meaning.")
    return payload


def decode_sources(payload: bytes, *, version: int = 1) -> se.CallerSignatureSources | None:
    parsed = parse_json(payload)
    if parsed is None:
        return None
    fields = ("format", "catalog", "modules", "limits", "acquisition")
    if version in {3, 4, 5}:
        fields += ("sample_python",)
    if version == 5:
        fields += ("adapter_calls",)
    row = object_fields(parsed, fields)
    if version not in _SOURCE_FORMATS or row["format"] != _SOURCE_FORMATS[version]:
        raise ValueError("Unsupported caller/signature source representation.")
    limits = decode_analysis_limits(row["limits"])
    catalog, modules = None, ()
    if row["catalog"] is not None:
        raw = row["catalog"]
        if type(raw) is not dict or type(raw.get("target")) is not dict:
            raise ValueError("Missing exact source target.")
        target = ExactInvestigationTarget(**object_fields(raw["target"], ("repository", "pull_number", "base_sha", "head_sha", "normalized_package", "old_version", "proposed_version")))
        if row["modules"]:
            source = decode_analysis_input(json_bytes(dict(format=INPUT_FORMAT, analysis_profile=ANALYSIS_PROFILE,
                catalog=raw, modules=row["modules"], limits=row["limits"])))
            catalog, modules = source.catalog, source.modules
        else:
            catalog = read_source_catalog(json_bytes(raw), expected_target=target)
            if any(f.path.endswith(".py") for f in catalog.files):
                raise ValueError("Unclassified retained Python text.")
    elif row["modules"] != []:
        raise ValueError("Source roles without retained text.")
    layout = _VALUES if version == 1 else _MOVE_VALUES
    receipt = layout.decode(json_bytes(row["acquisition"]), _RECEIPT)
    _validate_receipt(receipt)
    scenario_layout = _PYTHON_SCENARIO_VALUES if version == 3 else _RANKED_SCENARIO_VALUES
    scenario = (scenario_layout.decode(json_bytes(row["sample_python"]), _PYTHON_SCENARIO)
                if row.get("sample_python") is not None else None)
    adapter_calls = (_ADAPTER_CALL_VALUES.decode(json_bytes(row["adapter_calls"]), _ADAPTER_CALLS)
                     if version == 5 else None)
    result = se.CallerSignatureSources(catalog, modules, limits, receipt, scenario, adapter_calls)
    if version != source_codec_version(result):
        raise ValueError("Caller/signature source representation does not match its observations.")
    _validate_catalog_joins(result)
    _validate_sample_python(result)
    _validate_adapter_calls(result)
    return result
