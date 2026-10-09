"""One normal offline producer run -> immutable research Workspace -> legacy consumers.

START HERE: capture_normal_pipeline -> project_legacy_result -> existing synthesis/report.
Native owners and current orchestration run unchanged. Invocation capture retains local
material inputs before the frozen return discards them. A one-way legacy bridge earns only
this parity proof; consumer rules are never copied. Live typed values are checked against
retained bytes, not hydrated from arbitrary checkpoint type tags. A cold restart without an
admitted native codec explicitly cannot materialize synthesis/report inputs.
"""

from __future__ import annotations

import json
from collections import Counter
from contextlib import ExitStack
from dataclasses import fields
from datetime import UTC, datetime
from hashlib import sha256
from types import SimpleNamespace
from unittest.mock import patch

from experiments.workspace_retention_corpus import HEAD, PR, REPOSITORY
from experiments.workspace_revision_representation import (
    ImmutableSuccessorHistory,
    TraceRecord,
    encode_fields,
)
from upgradepilot import investigation as application
from upgradepilot.github.actions import WorkflowJob, WorkflowRun, WorkflowStep
from upgradepilot.github.changelog import DiscoveredChangelogPath
from upgradepilot.github.pull_request import ChangedFile
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.tag import GitHubTagCommitEvidence
from upgradepilot.investigation import PublicPullRequestInvestigation
from upgradepilot.pypi.release import (
    PackageReleaseEvidence,
    PackageReleaseIndexEvidence,
)
from upgradepilot.upstream.claim import (
    CandidateUpstreamClaim,
    CandidateUpstreamClaimResult,
)
from upgradepilot.upstream.repository import UpstreamRepositoryEvidence
from upgradepilot.upstream.support_drop import evaluate_support_drop_runtime

NOW = datetime(2026, 10, 9, 0, 0, tzinfo=UTC)
NATIVE_OPERATIONS = (
    "analyze_dependency_change",
    "evaluate_dependency_ci_coverage",
    "evaluate_runtime_dependency_state",
    "build_artifact_serviceability_impact_candidate",
    "interpret_target_artifact_environment",
    "evaluate_artifact_serviceability_impact",
    "release_interval_from_dependency_change",
    "select_crossed_release_index",
    "build_tagged_changelog_evidence",
    "assemble_upstream_interval_authority",
    "build_python_support_drop_impact_candidate",
    "evaluate_python_support_drop_impact",
    "select_python_support_drop_investigation",
    "interpret_target_python_declaration",
    "evaluate_target_python_relevance",
)


class ProjectionUnavailable(ValueError):
    """Retained state is inspectable; missing/unbound native values cannot become truth."""


def exact_target(pr):
    return encode_fields(
        {
            "repository": pr.repository,
            "pull_number": pr.number,
            "base_sha": pr.base_sha,
            "head_sha": pr.head_sha,
        }
    )


class NativeCapture:
    """Experiment-only publication and live-value binding, not a production repository.

    All captured trace records remain roots; this conservative research policy is not
    selective retention. The typed cache is disposable projection machinery: bytes in
    the revision remain the consistency boundary, and cache loss is a declared codec gap.
    """

    def __init__(self, port):
        self.port = port
        self.history = ImmutableSuccessorHistory(exact_target(PR), "migration-offline")
        assert port.save(self.revision, -1)
        self.values = {}
        self.calls = Counter()
        self.sequence = []

    @property
    def revision(self):
        return self.history.history[-1]

    def publish(self, record):
        old = self.revision.number
        roots = tuple(dict.fromkeys((*self.revision.roots, record.record_id)))
        revision = self.history.publish((record,), roots)
        try:
            if not self.port.save(revision, old):
                raise ProjectionUnavailable("Research publication rejected")
        except Exception:
            # Drop the local candidate; an unconfirmed store commit is not undone.
            # This run aborts rather than authorizing another effect or automatic retry.
            self.history.history.pop()
            raise
        return record.record_id

    def put(self, key, owner, value, dependencies=()):
        self.values[key] = value
        self.publish(
            TraceRecord(
                key,
                owner,
                "native",
                self.revision.target.decode(),
                encode_fields(value),
                tuple(dependencies),
            )
        )
        return value

    def acquire(self, name, args, value):
        self.calls[f"acquisition:{name}"] += 1
        key = f"acquisition:{name}:{self.calls[f'acquisition:{name}']}"
        self.put(key + ":input", "experiment.offline_ports", args)
        self.put(key, "experiment.offline_ports", value, (key + ":input",))
        self.sequence.append(key)
        if isinstance(value, RepositoryTextFile):
            scope = f"{value.repository}@{value.revision}:{value.path}"
            identity = "exact-text:" + sha256(scope.encode()).hexdigest()
            record = TraceRecord(
                identity,
                "upgradepilot.github.repository",
                "source_text",
                scope,
                value.content.encode(),
            )
            old = self.revision.records.get(identity)
            if old is None:
                self.publish(record)
            elif old != record:
                raise ProjectionUnavailable(
                    "Exact-source fixture changed in this lineage"
                )
        return value

    def evaluate(self, name, operation, args, kwargs):
        self.calls[f"native:{name}"] += 1
        key = f"native:{name}:{self.calls[f'native:{name}']}"
        # This one method also receives a client; the client is execution machinery.
        # Its actual returns are captured separately. No client is serialized as evidence.
        retained_args = args[:2] if name == "analyze_dependency_change" else args
        prior = tuple(self.revision.records)
        self.put(
            key + ":input",
            operation.__module__,
            {"args": retained_args, "kwargs": kwargs},
            prior,
        )
        value = operation(*args, **kwargs)
        self.put(key, operation.__module__, value, (key + ":input",))
        self.sequence.append(key)
        return value

    def bind_legacy_fields(self, result):
        """One-way field capture from the single current producer return, for parity only."""
        provenance = tuple(self.revision.records)
        mapping = {}
        for field in fields(PublicPullRequestInvestigation):
            key = f"legacy-field:{field.name}"
            self.put(
                key,
                "upgradepilot.investigation",
                getattr(result, field.name),
                provenance,
            )
            mapping[field.name] = key
        self.publish(
            TraceRecord(
                "migration:legacy-fields",
                "experiment.migration",
                "projection_basis",
                self.revision.target.decode(),
                encode_fields(mapping),
                tuple(mapping.values()),
            )
        )


def projection_values(revision, live_values):
    """Read one exact field manifest; absent data never receives dataclass defaults."""
    manifest = revision.records.get("migration:legacy-fields")
    if manifest is None or manifest.payload is None:
        raise ProjectionUnavailable("Missing legacy projection basis")
    mapping = json.loads(manifest.payload)
    expected = {field.name for field in fields(PublicPullRequestInvestigation)}
    if type(mapping) is not dict or set(mapping) != expected:
        raise ProjectionUnavailable("Incomplete/unsupported legacy field manifest")
    values = {}
    for name, key in mapping.items():
        record = revision.records.get(key)
        if record is None or record.payload is None:
            raise ProjectionUnavailable(f"Missing material native field: {name}")
        if key not in live_values:
            raise ProjectionUnavailable(
                "unsupported_native_codec: live values unavailable"
            )
        value = live_values[key]
        if encode_fields(value) != record.payload:
            raise ProjectionUnavailable(
                f"Native value is not bound to retained bytes: {name}"
            )
        values[name] = value
    if exact_target(values["pull_request"]) != revision.target:
        raise ProjectionUnavailable("Native projection belongs to another exact target")
    return values


def project_legacy_result(revision, live_values):
    """Temporary one-way proof bridge for current synthesis/report type requirements.

    This cannot project lifecycle, recover typed objects or grant continuation. Remove
    when consumers accept explicit Workspace/native projections and parity proof moves.
    """
    return PublicPullRequestInvestigation(**projection_values(revision, live_values))


def native_field_projection(revision, live_values):
    """Direct field access control: current consumers still reject this at synthesis."""
    return SimpleNamespace(**projection_values(revision, live_values))


def add_projection_pressure(capture):
    """New consumer/history obligations; interrupted work is labelled future pressure."""
    revision = capture.revision
    before = revision.number
    delivered = ("legacy-field:python_support_drop_impact_result",)
    capture.publish(
        TraceRecord(
            "migration:view",
            "scripted-investigator",
            "view",
            revision.target.decode(),
            encode_fields(
                {
                    "revision": before,
                    "delivered": delivered,
                    "omitted_but_addressable": tuple(
                        k for k in revision.records if k not in delivered
                    ),
                    "examined_or_used": "unknown",
                }
            ),
            delivered,
        )
    )
    capture.publish(
        TraceRecord(
            "migration:proposal",
            "scripted-investigator",
            "proposal",
            revision.target.decode(),
            encode_fields(
                {
                    "basis_revision": before,
                    "view": "migration:view",
                    "statement": "No overall adequate-stopping conclusion is available",
                    "evaluation": "unsupported_no_admitted_evaluator",
                }
            ),
            ("migration:view", *delivered),
        )
    )
    capture.publish(
        TraceRecord(
            "migration:unfinished",
            "experiment.future_pressure",
            "unfinished_operation",
            revision.target.decode(),
            encode_fields(
                {
                    "completion": "unknown",
                    "automatic_retry_permitted": False,
                    "stimulus": "simulated; not produced by this synchronous native flow",
                }
            ),
        )
    )
    return before


def _offline_ports(capture):
    """Disclosed native-record fixtures, following active tests without importing tests."""
    workflow_text = (
        "jobs:\n  test:\n    name: Tests\n    runs-on: ubuntu-latest\n    steps:\n"
        "      - name: Checkout\n        uses: actions/checkout@v4\n"
        "      - name: Install 1\n        run: PIP_DRY_RUN=0 PIP_CONFIG_FILE=/dev/null "
        "PIP_TARGET= PIP_PREFIX= PIP_ROOT= PIP_ONLY_DEPS=0 PIP_ONLY_DEPENDENCIES=0 "
        "/opt/bootstrap/bin/python -m pip --python /opt/target/bin/python install "
        "--no-user --no-deps -r requirements.txt\n"
        "      - name: Install 2\n        run: /opt/bootstrap/bin/python -m pip "
        "--python /opt/target/bin/python install --no-user --no-deps -r requirements.txt\n"
    )
    definition = RepositoryTextFile(
        REPOSITORY, ".github/workflows/ci.yml", HEAD, workflow_text
    )
    run = WorkflowRun(1001, 2001, "CI", "pull_request", HEAD, "completed", "success", 1)
    steps = tuple(
        WorkflowStep(i, name, "completed", "success")
        for i, name in enumerate(("Checkout", "Install 1", "Install 2"), 1)
    )
    job = WorkflowJob(3001, run.run_id, "Tests", HEAD, "completed", "success", steps)
    target = RepositoryTextFile(
        REPOSITORY,
        "pyproject.toml",
        HEAD,
        '[project]\nname = "demo-project"\nrequires-python = ">=3.8"\n',
    )
    text = "## 2.0\nDrop support for Python 3.8.\n"
    changelog = RepositoryTextFile("example/upstream", "CHANGELOG.md", "c" * 40, text)
    packages = {
        version: PackageReleaseEvidence(
            "demo",
            "demo",
            version,
            "demo",
            version,
            f"https://pypi.org/pypi/demo/{version}/json",
            NOW,
            1,
            (),
            (),
        )
        for version in ("1.0", "2.0")
    }
    upstream = UpstreamRepositoryEvidence(
        packages["2.0"], "example/upstream", (), (), ()
    )
    index = PackageReleaseIndexEvidence(
        "demo",
        "demo",
        "demo",
        "https://pypi.org/pypi/demo/json",
        NOW,
        1,
        ("1.0", "2.0"),
    )
    tag = GitHubTagCommitEvidence(
        "example/upstream",
        "2.0",
        "refs/tags/2.0",
        "commit",
        "c" * 40,
        "c" * 40,
        (),
        NOW,
    )
    path = DiscoveredChangelogPath(
        "example/upstream", "c" * 40, "d" * 40, "CHANGELOG.md", ("CHANGELOG.md",)
    )

    def acquire(name, value, *args):
        return capture.acquire(name, args, value)

    class ExplicitExtractor:
        def extract(self, window):
            capture.calls["extractor:deterministic_fixture"] += 1
            capture.put(
                "extraction:window", "upgradepilot.upstream.source_window", window
            )
            capture.put(
                "extraction:method",
                "experiment.explicit_fixture",
                {
                    "method": "supplied-support-drop-candidate-v1",
                    "models": 0,
                    "claim_limit": "candidate meaning supplied for migration proof; no semantic discovery",
                },
                ("extraction:window",),
            )
            quote = "Drop support for Python 3.8."
            start = text.index(quote)
            result = CandidateUpstreamClaimResult(
                "candidates_available",
                "demo",
                "demo",
                "1.0",
                "2.0",
                (
                    CandidateUpstreamClaim(
                        "support_boundary_change",
                        "support_dropped",
                        "3.8",
                        "2.0",
                        "tagged_changelog",
                        None,
                        quote,
                        start,
                        start + len(quote),
                    ),
                ),
                None,
            )
            return capture.put(
                "extraction:proposal",
                "experiment.explicit_fixture",
                result,
                ("extraction:window", "extraction:method"),
            )

    # Extractor is machinery rather than native evidence; its explicit method/window/
    # proposal capture replaces serialization of the Python instance in this one call.
    def support_recorded(authority):
        capture.calls["native:support_drop_runtime"] += 1
        capture.put(
            "support-runtime:input", "upgradepilot.upstream.support_drop", authority
        )
        result = evaluate_support_drop_runtime(authority, extractor=ExplicitExtractor())
        return capture.put(
            "support-runtime:output",
            "upgradepilot.upstream.support_drop",
            result,
            ("support-runtime:input", "extraction:proposal"),
        )

    return {
        "pull_client": SimpleNamespace(
            get_pull_request=lambda *a: acquire("pull.identity", PR, *a),
            get_changed_files=lambda *a: acquire(
                "pull.files",
                (
                    ChangedFile(
                        "requirements.txt",
                        "modified",
                        1,
                        1,
                        2,
                        "@@ -1 +1 @@\n-demo==1.0\n+demo==2.0\n",
                    ),
                ),
                *a,
            ),
        ),
        "actions_client": SimpleNamespace(
            get_exact_head_workflow_runs=lambda *a: acquire("actions.runs", (run,), *a),
            get_workflow_jobs=lambda *a: acquire("actions.jobs", (job,), *a),
        ),
        "repository_client": SimpleNamespace(
            get_exact_head_workflow_file=lambda *a: acquire(
                "repository.workflow", definition, *a
            ),
            get_exact_commit_text_file=lambda *a: acquire(
                "repository.changelog", changelog, *a
            ),
            get_exact_head_text_file=lambda *a: acquire(
                "repository.target", target, *a
            ),
        ),
        "package_client": SimpleNamespace(
            get_release=lambda package, version: acquire(
                "pypi.release", packages[version], package, version
            )
        ),
        "release_index_client": SimpleNamespace(
            get_release_index=lambda *a: acquire("pypi.index", index, *a)
        ),
        "upstream_repository_resolver": SimpleNamespace(
            resolve=lambda *a: acquire("upstream.repository", upstream, *a)
        ),
        "tag_client": SimpleNamespace(
            resolve_tag_to_commit=lambda *a: acquire("upstream.tag", tag, *a)
        ),
        "changelog_client": SimpleNamespace(
            discover=lambda *a: acquire("upstream.changelog_path", path, *a)
        ),
        "support_drop_evaluator": support_recorded,
    }


def capture_normal_pipeline(port):
    """Run the unmodified normal entry once with offline ports and delegating capture."""
    capture = NativeCapture(port)
    ports = _offline_ports(capture)
    with ExitStack() as stack:
        for name in NATIVE_OPERATIONS:
            operation = getattr(application, name)

            def recorded(*args, _name=name, _operation=operation, **kwargs):
                return capture.evaluate(_name, _operation, args, kwargs)

            stack.enter_context(patch.object(application, name, recorded))
        capture.calls["orchestration:investigate_public_pull_request"] += 1
        result = application.investigate_public_pull_request(
            REPOSITORY, PR.number, **ports
        )
    capture.bind_legacy_fields(result)
    return capture, result
