"""Known S001 public-data grounding of experiments 1–3; no models or migration.

START HERE: supported native acquisition/analysis -> explicit known-source candidate ->
existing validation/need -> experimental consumer/admission -> exact-SHA native read ->
existing target owners -> immutable checkpoint/recovery. Production has no Workspace seam;
this is a bounded research composition of a currently admitted support-path subset.
CI/artifact/synthesis/report and default model interpretation are intentionally excluded.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path

from experiments.workspace_investigator_seam import (
    AcquisitionRequest,
    HostPolicy,
    InvestigatorPort,
    TraceRecord,
    WorkspaceHost,
    payload,
)
from experiments.workspace_public_input_tape import PublicInputTape
from experiments.workspace_revision_representation import (
    decode_checkpoint,
    encode_checkpoint,
    encode_fields,
    material_closure,
)
from experiments.workspace_seam_checkpoints import MemoryCheckpoints, SQLiteCheckpoints
from upgradepilot.dependency.analysis import (
    DependencyChangeAnalysis,
    analyze_dependency_change,
)
from upgradepilot.github.changelog import (
    DiscoveredChangelogPath,
    GitHubChangelogPathClient,
)
from upgradepilot.github.pull_request import GitHubPullRequestClient
from upgradepilot.github.repository import GitHubRepositoryClient, RepositoryTextFile
from upgradepilot.github.tag import GitHubTagCommitClient, GitHubTagCommitEvidence
from upgradepilot.impact.python_support import (
    build_python_support_drop_impact_candidate,
    evaluate_python_support_drop_impact,
    select_python_support_drop_investigation,
)
from upgradepilot.pypi.provenance import PyPIProvenanceClient
from upgradepilot.pypi.release import (
    PackageReleaseEvidence,
    PyPIReleaseClient,
    PyPIReleaseIndexClient,
)
from upgradepilot.target.python import interpret_target_python_declaration
from upgradepilot.target.relevance import evaluate_target_python_relevance
from upgradepilot.upstream.claim import (
    CandidateUpstreamClaim,
    CandidateUpstreamClaimResult,
    GroundedPythonSupportDropClaim,
    validate_support_drop_candidates,
)
from upgradepilot.upstream.interval import (
    assemble_upstream_interval_authority,
    release_interval_from_dependency_change,
)
from upgradepilot.upstream.interval_evidence import (
    SelectedCrossedReleaseIndex,
    build_tagged_changelog_evidence,
    select_crossed_release_index,
)
from upgradepilot.upstream.repository import (
    UpstreamRepositoryEvidence,
    UpstreamRepositoryResolver,
)

REPOSITORY = "pydantic/pydantic"
PULL = 13432
BASE = "652a61ce4f9d7d76eaada31535807a485ece0e21"
HEAD = "aa2dc024d33f61cdef50bf1973ab5adf0a974f5a"
QUOTE = "Drop support for Python 3.8."


class GroundingBlocked(Exception):
    """Public acquisition/native path stopped; preserve its actual boundary."""


@dataclass
class NativeLedger:
    tape: PublicInputTape
    scope: str = f"{REPOSITORY}@{HEAD}"

    def __post_init__(self):
        self.records = {}
        self.files = {}

    def native(self, name, value, dependencies=()):
        record = TraceRecord(
            name,
            type(value).__module__,
            "native",
            self.scope,
            encode_fields(value),
            tuple(dependencies),
        )
        self.records[name] = record
        return value

    def produced(self, name, operation, dependencies=()):
        start = self.tape.cursor
        value = operation()
        for index in range(start, self.tape.cursor):
            entry = self.tape.entries[index]
            self.records[f"http:{index}"] = TraceRecord(
                f"http:{index}",
                "experiment.public_capture",
                "public_input",
                entry["url"],
                (self.tape.root / entry["body"]).read_bytes(),
            )
        return self.native(
            name,
            value,
            (
                *dependencies,
                *(f"http:{index}" for index in range(start, self.tape.cursor)),
            ),
        )

    def file(self, value):
        if not isinstance(value, RepositoryTextFile):
            raise GroundingBlocked(f"Exact file unavailable: {value}")
        scope = f"{value.repository}@{value.revision}:{value.path}"
        key = "file:" + hashlib.sha256(scope.encode()).hexdigest()[:16]
        if key in self.files:
            if self.files[key] != value:
                raise GroundingBlocked("Exact public file changed under its identity")
            return key
        self.files[key] = value
        self.records[key] = TraceRecord(
            key,
            "upgradepilot.github.repository",
            "source_text",
            scope,
            value.content.encode(),
        )
        return key


class RecordedRepositoryClient(GitHubRepositoryClient):
    def __init__(self, ledger):
        super().__init__(session=ledger.tape)
        self.ledger = ledger

    def _get_exact_repository_text_file(self, repository, path, *, revision):
        start = self.ledger.tape.cursor
        value = super()._get_exact_repository_text_file(
            repository, path, revision=revision
        )
        for index in range(start, self.ledger.tape.cursor):
            entry = self.ledger.tape.entries[index]
            self.ledger.records[f"http:{index}"] = TraceRecord(
                f"http:{index}",
                "experiment.public_capture",
                "public_input",
                entry["url"],
                (self.ledger.tape.root / entry["body"]).read_bytes(),
            )
        key = self.ledger.file(value)
        record = self.ledger.records[key]
        self.ledger.records[key] = TraceRecord(
            record.record_id,
            record.owner,
            record.kind,
            record.scope,
            record.payload,
            tuple(f"http:{index}" for index in range(start, self.ledger.tape.cursor)),
        )
        return value


def require(value, expected, boundary):
    if not isinstance(value, expected):
        raise GroundingBlocked(f"{boundary}: {value}")
    return value


def exact_target_token(pr):
    """Descriptive PR metadata is retained evidence, not a different exact target."""
    return encode_fields(
        {
            "repository": pr.repository,
            "pull_number": pr.number,
            "base_sha": pr.base_sha,
            "head_sha": pr.head_sha,
        }
    ).decode()


def run(tape, *, backend, store_root):
    ledger = NativeLedger(tape)
    pull_client = GitHubPullRequestClient(session=tape)
    repository_client = RecordedRepositoryClient(ledger)
    pr = ledger.produced(
        "target:pr", lambda: pull_client.get_pull_request(REPOSITORY, PULL)
    )
    if (pr.repository, pr.number, pr.base_sha, pr.head_sha) != (
        REPOSITORY,
        PULL,
        BASE,
        HEAD,
    ):
        raise GroundingBlocked(
            "Known PR exact target differs; do not rebind historical lineage"
        )
    files = ledger.produced(
        "target:changed-files",
        lambda: pull_client.get_changed_files(pr),
        ("target:pr",),
    )
    analysis = require(
        analyze_dependency_change(pr, files, repository_client),
        DependencyChangeAnalysis,
        "dependency source analysis",
    )
    source_ids = tuple(ledger.files)
    ledger.native(
        "dependency:analysis", analysis, ("target:changed-files", *source_ids)
    )
    dependency = ledger.native(
        "dependency", analysis.dependency, ("dependency:analysis",)
    )
    if (
        dependency.normalized_package,
        dependency.old_version,
        dependency.proposed_version,
    ) != ("soupsieve", "2.6", "2.8.4"):
        raise GroundingBlocked("Known dependency transition changed")
    package = require(
        ledger.produced(
            "package:proposed",
            lambda: PyPIReleaseClient(session=tape, now=tape.now).get_release(
                dependency.package, dependency.proposed_version
            ),
            ("dependency",),
        ),
        PackageReleaseEvidence,
        "PyPI release",
    )
    resolver = UpstreamRepositoryResolver(
        provenance_client=PyPIProvenanceClient(session=tape, now=tape.now)
    )
    upstream = require(
        ledger.produced(
            "upstream:repository",
            lambda: resolver.resolve(package),
            ("package:proposed",),
        ),
        UpstreamRepositoryEvidence,
        "upstream repository provenance",
    )
    release_index = ledger.produced(
        "upstream:release-index",
        lambda: PyPIReleaseIndexClient(session=tape, now=tape.now).get_release_index(
            dependency.package
        ),
        ("dependency",),
    )
    interval = ledger.native(
        "dependency:interval",
        release_interval_from_dependency_change(dependency),
        ("dependency",),
    )
    crossed = require(
        ledger.native(
            "upstream:crossed",
            select_crossed_release_index(interval, upstream.repository, release_index),
            ("dependency:interval", "upstream:release-index", "upstream:repository"),
        ),
        SelectedCrossedReleaseIndex,
        "crossed release selection",
    )
    tag = require(
        ledger.produced(
            "upstream:tag",
            lambda: GitHubTagCommitClient(
                session=tape, now=tape.now
            ).resolve_tag_to_commit(upstream.repository, dependency.proposed_version),
            (
                "upstream:repository",
                "dependency",
            ),
        ),
        GitHubTagCommitEvidence,
        "exact proposed tag",
    )
    discovery = require(
        ledger.produced(
            "upstream:changelog-path",
            lambda: GitHubChangelogPathClient(session=tape).discover(
                upstream.repository, tag.resolved_commit_sha
            ),
            ("upstream:tag",),
        ),
        DiscoveredChangelogPath,
        "changelog discovery",
    )
    changelog_file = repository_client.get_exact_commit_text_file(
        upstream.repository, tag.resolved_commit_sha, discovery.path
    )
    changelog_id = ledger.file(changelog_file)
    tagged = ledger.native(
        "upstream:tagged",
        build_tagged_changelog_evidence(interval, tag, changelog_file),
        (
            "dependency:interval",
            "upstream:tag",
            "upstream:changelog-path",
            changelog_id,
        ),
    )
    authority = ledger.native(
        "upstream:authority",
        assemble_upstream_interval_authority(
            interval,
            upstream.repository,
            crossed_releases=crossed.evidence,
            tagged_changelogs=(tagged,),
        ),
        ("upstream:crossed", "upstream:tagged"),
    )
    start = changelog_file.content.index(QUOTE)
    candidate = CandidateUpstreamClaimResult(
        "candidates_available",
        dependency.package,
        dependency.normalized_package,
        dependency.old_version,
        dependency.proposed_version,
        (
            CandidateUpstreamClaim(
                "support_boundary_change",
                "support_dropped",
                "3.8",
                "2.8",
                "tagged_changelog",
                None,
                QUOTE,
                start,
                start + len(QUOTE),
            ),
        ),
        None,
    )
    ledger.native("upstream:known-candidate", candidate, ("upstream:authority",))
    ledger.native(
        "method:known-source",
        {
            "method": "known-S001-source-candidate-v1",
            "category": "agent-supplied known-case development control",
            "quote": QUOTE,
            "introduced_in_version": "2.8",
            "semantic_extraction": "not run; no models",
            "generalization": "none",
        },
        ("upstream:known-candidate",),
    )
    claim = require(
        ledger.native(
            "upstream:grounded",
            validate_support_drop_candidates(authority, candidate),
            ("upstream:authority", "upstream:known-candidate", "method:known-source"),
        ),
        GroundedPythonSupportDropClaim,
        "known-source candidate grounding",
    )
    impact = ledger.native(
        "support:candidate",
        build_python_support_drop_impact_candidate(pr, dependency, claim),
        ("target:pr", "dependency", "upstream:grounded"),
    )
    before = ledger.native(
        "support:before",
        evaluate_python_support_drop_impact(impact),
        ("support:candidate",),
    )
    need = ledger.native(
        "support:need",
        select_python_support_drop_investigation(before),
        ("support:before",),
    )
    if need is None:
        raise GroundingBlocked("No native follow-up need selected")
    ledger.records["capture:manifest:before"] = TraceRecord(
        "capture:manifest:before",
        "experiment.public_capture",
        "capture_method",
        ledger.scope,
        json.dumps(tape.snapshot(), sort_keys=True, indent=2).encode(),
        tuple(f"http:{i}" for i in range(tape.cursor)),
    )
    target = exact_target_token(pr)
    policy = HostPolicy(
        target,
        "known-S001-source-candidate-v1",
        frozenset({"read_target_declaration"}),
        True,
        f"{need.repository}@{need.revision}:{need.path}",
        need.proposition_key,
    )
    port = (
        MemoryCheckpoints()
        if backend == "memory"
        else SQLiteCheckpoints(store_root, create=True)
    )
    try:
        host = WorkspaceHost(port, policy)
        seeded = host.seed(
            tuple(ledger.records.values()),
            {"candidate": "support:candidate", "need": "support:need"},
            lineage="known-S001-public-grounding",
        )
        assert seeded.status == "published"
        original = encode_checkpoint(host.revision)
        host.continue_current()
        consumer = InvestigatorPort(host)
        view = consumer.read(("support:need", "support:candidate"))
        request = AcquisitionRequest(
            "investigator:public-read",
            view.revision,
            view.basis,
            "read_target_declaration",
            policy.scope,
            policy.method,
            need.proposition_key,
        )
        assert consumer.request(request).status == "admitted"
        assert host.start(request.request_id).status == "published"
        source = repository_client.get_exact_head_text_file(pr, need.path)
        record = TraceRecord(
            "target:source",
            "upgradepilot.github.repository",
            "source_text",
            policy.scope,
            source.content.encode(),
        )
        assert host.observe(request.request_id, record).status == "observation_admitted"
        ledger.records["capture:manifest:complete"] = TraceRecord(
            "capture:manifest:complete",
            "experiment.public_capture",
            "capture_method",
            ledger.scope,
            json.dumps(tape.snapshot(), sort_keys=True, indent=2).encode(),
            tuple(f"http:{i}" for i in range(tape.cursor)),
        )
        # Capture newly acquired input/locator trace before native evaluation; HTTP inputs
        # are audit provenance, not another independent target observation.
        for key, item in ledger.records.items():
            if key not in host.revision.records:
                host.retain_evidence(
                    item, role="acquisition_provenance", candidate="transport-audit"
                )
        declaration = ledger.native(
            "native:declaration",
            interpret_target_python_declaration(source),
            ("target:source",),
        )
        relevance = ledger.native(
            "native:relevance",
            evaluate_target_python_relevance(claim, declaration),
            ("native:declaration", "upstream:grounded"),
        )
        after = ledger.native(
            "native:assessment",
            evaluate_python_support_drop_impact(impact, relevance),
            ("native:relevance", "support:candidate"),
        )
        assert (
            host.publish_evaluation(
                tuple(
                    ledger.records[key]
                    for key in (
                        "native:declaration",
                        "native:relevance",
                        "native:assessment",
                    )
                ),
                status=after.applicability.state,
                need_status="no_selected_need"
                if select_python_support_drop_investigation(after) is None
                else "material_non_final",
            ).status
            == "published"
        )
        omitted = consumer.read(("support:need",))
        assert "target:source" in omitted.omitted_but_addressable
        assert (
            consumer.propose(
                "proposal:undelivered",
                omitted,
                ("target:source",),
                "known source interpretation",
            ).status
            == "citation_not_delivered_in_view"
        )
        delivered = consumer.read(("target:source", "native:assessment"))
        assert (
            consumer.propose(
                "proposal:public",
                delivered,
                ("target:source",),
                "known source interpretation",
            ).status
            == "proposal_retained_evaluation_unsupported"
        )
        data = encode_checkpoint(host.revision)
        assert encode_checkpoint(decode_checkpoint(original)) == original
        if backend == "sqlite":
            # Storage-specific proof remains behind the host; the consumer sees no SQL.
            backup = port.store.backup(store_root.parent / "online-backup")
            try:
                outcome = backup.recover()
                assert not outcome.rejected
                assert encode_checkpoint(outcome.revision) == data
                connection = backup.connect()
                try:
                    assert backup._load(connection, 0) == original
                finally:
                    connection.close()
            finally:
                backup.close()
        restored = WorkspaceHost(port, policy)
        assert encode_checkpoint(restored.revision) == data and not restored.active
        # Independent required-input oracle, distinct from following declared graph edges.
        expected = set(ledger.records) | {
            "target:source",
            "investigator:public-read",
            "attempt:investigator:public-read",
            "completion:investigator:public-read",
            "proposal:public",
        }
        assert expected <= set(material_closure(restored.revision))
        file_ids = [key for key in ledger.files]
        assert len(file_ids) == 4, (
            "Expected exact base/head uv.lock, tagged changelog and target pyproject"
        )
        for key in file_ids:
            assert (
                restored.revision.records[key].payload
                == ledger.files[key].content.encode()
            )
        assert (
            payload(host.revision.records[view.view_id])["examined_or_used"]
            == "unknown"
        )
        assert restored.continue_current().status == "current_bindings_validated"
        tape.assert_consumed()
        summary = {
            "target": asdict(pr),
            "dependency": {
                "package": dependency.package,
                "old": dependency.old_version,
                "proposed": dependency.proposed_version,
            },
            "upstream_commit": tag.resolved_commit_sha,
            "changelog_path": discovery.path,
            "crossed_versions": crossed.evidence.ordered_versions,
            "native_before": before.applicability.state,
            "native_after": after.applicability.state,
            "relevance": relevance.state,
            "requires_python": declaration.requires_python,
            "native_next_need": select_python_support_drop_investigation(after),
            "adequacy": "unsupported_no_admitted_evaluator",
            "model_calls": 0,
            "http_requests": tape.cursor,
            "source_files": {
                key: {
                    "repository": file.repository,
                    "revision": file.revision,
                    "path": file.path,
                    "bytes": len(file.content.encode()),
                    "sha256": hashlib.sha256(file.content.encode()).hexdigest(),
                }
                for key, file in ledger.files.items()
            },
            "material_records": len(material_closure(host.revision)),
            "revision": host.ref.number,
            "checkpoint_bytes": len(data),
            "checkpoint_sha256": hashlib.sha256(data).hexdigest(),
            "initial_revision_unchanged": True,
            "restored_historical_then_explicitly_validated": True,
            "omitted_citation_rejected": True,
        }
        return summary, data, ledger
    finally:
        if backend == "sqlite":
            port.close()


def restore_input_tape(checkpoint, root):
    """Research-only native re-execution input recovery; no trusted-object hydration."""
    revision = decode_checkpoint(checkpoint)
    metadata = payload(revision.records["capture:manifest:complete"])
    root.mkdir(parents=True, exist_ok=False)
    (root / "manifest.json").write_text(
        json.dumps(metadata, sort_keys=True, indent=2) + "\n"
    )
    for index, entry in enumerate(metadata["requests"]):
        record = revision.records[f"http:{index}"]
        if (
            record.scope != entry["url"]
            or hashlib.sha256(record.payload).hexdigest() != entry["sha256"]
        ):
            raise ValueError("Checkpoint capture/body relationship mismatch")
        # Generated capture names, never an externally supplied filesystem destination.
        if entry["body"] != f"response-{index:03}.body":
            raise ValueError("Unsupported captured response filename")
        (root / entry["body"]).write_bytes(record.payload)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--inputs", type=Path, help="Captured inputs only; no network fallback"
    )
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    result = {
        "status": "running",
        "proof_class": "known public development/grounding case",
        "default_product_workspace": False,
        "migration": False,
    }

    def flush():
        (args.output / "results.json").write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n"
        )

    flush()
    try:
        root = args.inputs or args.output / "public-inputs"
        tape = PublicInputTape(root, offline=args.inputs is not None)
        with tempfile.TemporaryDirectory() as directory:
            summary, checkpoint, ledger = run(
                tape, backend="sqlite", store_root=Path(directory) / "store"
            )
        result["sqlite_trial"] = summary
        result["sqlite_online_backup"] = (
            "byte-identical latest checkpoint and original revision zero"
        )
        flush()
        (args.output / "checkpoint.json").write_bytes(checkpoint)
        source_root = args.output / "exact-files"
        source_root.mkdir(exist_ok=True)
        for key, file in ledger.files.items():
            (source_root / (key.replace(":", "-") + ".txt")).write_bytes(
                file.content.encode()
            )
        with tempfile.TemporaryDirectory() as directory:
            recovered_root = Path(directory) / "from-checkpoint"
            restore_input_tape(checkpoint, recovered_root)
            retained = PublicInputTape(recovered_root, offline=True)
            memory_summary, memory_checkpoint, _ = run(
                retained, backend="memory", store_root=Path(directory) / "unused"
            )
        assert memory_checkpoint == checkpoint and memory_summary == summary
        result["retained_input_memory_reexecution"] = (
            "input tape reconstructed only from checkpoint; byte-identical native summary/checkpoint; no network"
        )
        result["status"] = "complete"
        sources = [
            Path(__file__),
            Path("experiments/tests/test_workspace_public_grounding.py"),
            Path("experiments/workspace_public_input_tape.py"),
            Path("experiments/workspace_investigator_seam.py"),
            Path("experiments/workspace_seam_checkpoints.py"),
            Path("experiments/workspace_revision_representation.py"),
            Path("experiments/workspace_checkpoint_stores.py"),
        ]
        source_tree = hashlib.sha256()
        for path in sorted(Path("src/upgradepilot").rglob("*.py")):
            source_tree.update(str(path).encode() + b"\0" + path.read_bytes() + b"\0")
        result["native_tree_sha256"] = source_tree.hexdigest()
        result["source_sha256"] = {
            str(
                path.relative_to(Path.cwd()) if path.is_absolute() else path
            ): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sources
        }
    except Exception as error:
        result["status"] = (
            "blocked" if isinstance(error, GroundingBlocked) else "failed"
        )
        result["boundary"] = f"{type(error).__name__}: {error}"
        flush()
        raise
    flush()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
