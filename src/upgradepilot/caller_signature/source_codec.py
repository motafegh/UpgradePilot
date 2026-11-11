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
from .bindings import BindingAssessment, BindingTraceStep, ImportFact, ReferenceFact, binding_state
from .evidence import MeasuredDuration
from .native_codec import DURATION_LAYOUT
from .result_codec import (
    ANALYSIS_PROFILE, INPUT_FORMAT, decode_analysis_input, decode_analysis_limits,
    encode_analysis_limits, module_fields,
)
from ..github.identity import validate_commit_sha, validate_repository
from ..github.api import GITHUB_API_ROOT
from ..github.tag import (GitHubTagCommitEvidence, GitHubTagRepositoryRedirect,
                          repository_move_redirect, tag_reference_path)
from ..pypi.provenance import FileProvenanceEvidence, FileProvenanceProblem, PublisherIdentity
from ..pypi.release import DistributionFile, PackageReleaseEvidence, ProjectUrlCandidate
from ..workspace.native_boundary import ExactInvestigationTarget
from ..workspace.native_representation import (
    Either, LiteralValues, NativeValueCodec, RecordLayout, RecordRef, SequenceOf,
    json_bytes, object_fields, parse_json,
)
from ..workspace.source_access import encode_source_catalog, read_source_catalog

FORMAT = "caller-signature-sources/1"
MOVE_FORMAT = "caller-signature-sources/2"


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


def source_codec_version(value: se.CallerSignatureSources) -> int:
    return 2 if any(module.repository_move is not None for module in value.acquisition.module_requests) else 1


def encode_sources(value: se.CallerSignatureSources | None, *, version: int = 1) -> bytes:
    if value is None:
        return json_bytes(None)
    if version != source_codec_version(value):
        raise ValueError("Caller/signature source representation does not match its observations.")
    layout = _MOVE_VALUES if version == 2 else _VALUES
    payload = json_bytes(dict(format=MOVE_FORMAT if version == 2 else FORMAT,
        catalog=parse_json(encode_source_catalog(value.catalog)) if value.catalog else None,
        modules=[module_fields(m) for m in value.modules], limits=encode_analysis_limits(value.analysis_limits),
        acquisition=parse_json(layout.encode(value.acquisition, _RECEIPT))))
    decoded = decode_sources(payload, version=version)
    if (decoded.catalog.identity if decoded.catalog else None) != (value.catalog.identity if value.catalog else None) or decoded.modules != value.modules or decoded.acquisition != value.acquisition or decoded.analysis_limits != value.analysis_limits:
        raise ValueError("Source family encoding changed retained meaning.")
    return payload


def decode_sources(payload: bytes, *, version: int = 1) -> se.CallerSignatureSources | None:
    parsed = parse_json(payload)
    if parsed is None:
        return None
    row = object_fields(parsed, ("format", "catalog", "modules", "limits", "acquisition"))
    if version not in {1, 2} or row["format"] != (MOVE_FORMAT if version == 2 else FORMAT):
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
    layout = _MOVE_VALUES if version == 2 else _VALUES
    receipt = layout.decode(json_bytes(row["acquisition"]), _RECEIPT)
    _validate_receipt(receipt)
    result = se.CallerSignatureSources(catalog, modules, limits, receipt)
    if version != source_codec_version(result):
        raise ValueError("Caller/signature source representation does not match its observations.")
    _validate_catalog_joins(result)
    return result
