"""Native offline fixtures plus explicitly simulated Workspace lifecycle pressure.

Existing tests supply fixture patterns, not imported runtime dependencies or live evidence.
Native evaluation results below come from their real owners; native inputs are constructed.
Exact file/CI/provider identity
is synthetic; candidate meaning is caller-supplied to exercise grounding, not extraction.
Capture dependencies are explicit experiment declarations, audited in the evidence ledger.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime

from experiments.workspace_revision_representation import TraceRecord, encode_fields
from upgradepilot.ci.dependency_exercise import (
    WorkflowDependencyCoverageInput,
    evaluate_dependency_ci_coverage,
)
from upgradepilot.ci.dependency_state import evaluate_runtime_dependency_state
from upgradepilot.ci.workflow_commands import (
    WorkflowProjectEnvironmentSource,
    inspect_workflow_dependency_evidence,
)
from upgradepilot.dependency.analysis import analyze_dependency_change
from upgradepilot.dependency.change import (
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.dependency.environment import RequirementsFileDependencyContext
from upgradepilot.github.actions import WorkflowJob, WorkflowRun, WorkflowStep
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.github.repository import RepositoryTextFile, UnavailableRepositoryFile
from upgradepilot.impact.python_support import (
    build_python_support_drop_impact_candidate,
    evaluate_python_support_drop_impact,
    select_python_support_drop_investigation,
)
from upgradepilot.target.python import interpret_target_python_declaration
from upgradepilot.target.relevance import evaluate_target_python_relevance
from upgradepilot.upstream.claim import (
    CandidateUpstreamClaim,
    CandidateUpstreamClaimResult,
    validate_support_drop_candidates,
)
from upgradepilot.upstream.interval import (
    CrossedReleaseIndexEvidence,
    DependencyReleaseInterval,
    TaggedChangelogEvidence,
    assemble_upstream_interval_authority,
)

HEAD = "a" * 40
BASE = "b" * 40
REPOSITORY = "example/project"
SCOPE = f"{REPOSITORY}@{HEAD}"
PR = PullRequestIdentity(
    REPOSITORY,
    7,
    "Bump demo",
    "open",
    False,
    "dependabot[bot]",
    "main",
    BASE,
    "update",
    HEAD,
    1,
)
SOURCE = DependencyChangeSourceEvidence(
    "requirements.txt", "exact_requirement", "exact_base_head_files"
)
DEPENDENCY = DependencyVersionChange("demo", "demo", "1.0", "2.0", (SOURCE,))


def native(key, value, dependencies=()):
    return TraceRecord(
        key, type(value).__module__, "native", SCOPE, encode_fields(value), dependencies
    )


def simulated(key, kind, values, dependencies=()):
    return TraceRecord(
        key, "experiment.lifecycle", kind, SCOPE, encode_fields(values), dependencies
    )


def source(key, value):
    return TraceRecord(
        key,
        "upgradepilot.github.repository",
        "source_text",
        f"{value.repository}@{value.revision}:{value.path}",
        value.content.encode("utf-8"),
    )


def project_file(version, revision):
    """One exact fixture source shared by target-relevance and optional-extra consumers."""
    return RepositoryTextFile(
        REPOSITORY,
        "pyproject.toml",
        revision,
        '[project]\nname = "demo-project"\nversion = "0.1"\nrequires-python = ">=3.8"\n[project.optional-dependencies]\nspeed = [\'demo[fast]=='
        + version
        + '; python_version < "3.12"\']\n',
    )


@dataclass(frozen=True)
class TraceCorpus:
    target: bytes
    steps: tuple[tuple[tuple[TraceRecord, ...], tuple[str, ...]], ...]
    native_outcomes: dict


def _ci_records():
    """Normal native coverage → runtime-state path; one witness and one unknown."""
    context = RequirementsFileDependencyContext(REPOSITORY, HEAD, "demo", SOURCE)
    commands = (
        (
            "PIP_DRY_RUN=0 PIP_CONFIG_FILE=/dev/null PIP_TARGET= PIP_PREFIX= PIP_ROOT= "
            "PIP_ONLY_DEPS=0 PIP_ONLY_DEPENDENCIES=0 /opt/bootstrap/bin/python -m pip "
            "--python /opt/target/bin/python install --no-user --no-deps -r requirements.txt"
        ),
        "/opt/bootstrap/bin/python -m pip --python /opt/target/bin/python install --no-user --no-deps -r requirements.txt",
    )
    steps = "\n".join(
        f"      - name: Install {i}\n        run: {command}"
        for i, command in enumerate(commands, 1)
    )
    definition = RepositoryTextFile(
        REPOSITORY,
        ".github/workflows/ci.yml",
        HEAD,
        "jobs:\n  test:\n    name: Tests\n    runs-on: ubuntu-latest\n    steps:\n      - name: Checkout\n        uses: actions/checkout@v4\n"
        + steps
        + "\n",
    )
    run = WorkflowRun(1001, 2001, "CI", "pull_request", HEAD, "completed", "success", 1)
    runtime_steps = (WorkflowStep(1, "Checkout", "completed", "success"),) + tuple(
        WorkflowStep(i + 1, f"Install {i}", "completed", "success") for i in range(1, 3)
    )
    job = WorkflowJob(3001, 1001, "Tests", HEAD, "completed", "success", runtime_steps)
    inputs = WorkflowDependencyCoverageInput(run, (job,), definition)
    coverage = evaluate_dependency_ci_coverage(
        DEPENDENCY, (inputs,), source_contexts=(context,)
    )
    runtime = evaluate_runtime_dependency_state(
        DEPENDENCY, (inputs,), coverage, source_contexts=(context,)
    )
    records = (
        native("target:pr", PR),
        source(
            "dependency:base-text",
            RepositoryTextFile(REPOSITORY, "requirements.txt", BASE, "demo==1.0\n"),
        ),
        source(
            "dependency:head-text",
            RepositoryTextFile(REPOSITORY, "requirements.txt", HEAD, "demo==2.0\n"),
        ),
        native(
            "dependency",
            DEPENDENCY,
            ("target:pr", "dependency:base-text", "dependency:head-text"),
        ),
        native("ci:source-context", context, ("dependency",)),
        source("ci:workflow-text", definition),
        native("ci:input", inputs, ("ci:workflow-text",)),
        native(
            "ci:coverage", coverage, ("dependency", "ci:input", "ci:source-context")
        ),
        native("ci:runtime", runtime, ("ci:coverage", "ci:input", "ci:source-context")),
    )
    return records, {
        "coverage": coverage.state,
        "runtime": [
            {
                "type": type(item.result).__name__,
                "state": getattr(item.result, "state", "bounded_witness"),
                "reason": getattr(item.result, "reason", None),
            }
            for item in runtime.assessments
        ],
    }


def _support_records():
    """Ground supplied candidate, then run actual impact/target owners without a model."""
    interval = DependencyReleaseInterval("demo", "demo", "1.0", "2.0")
    index = CrossedReleaseIndexEvidence(
        REPOSITORY,
        interval,
        ("2.0",),
        "https://example.invalid/releases",
        datetime(2026, 10, 8, tzinfo=UTC),
    )
    text = "## 2.0\nDrop support for Python 3.8.\n"
    changelog = TaggedChangelogEvidence(
        REPOSITORY, interval, "c" * 40, "CHANGELOG.md", text
    )
    authority = assemble_upstream_interval_authority(
        interval, REPOSITORY, crossed_releases=index, tagged_changelogs=(changelog,)
    )
    quote = "Drop support for Python 3.8."
    start = text.index(quote)
    proposal = CandidateUpstreamClaimResult(
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
    claim = validate_support_drop_candidates(authority, proposal)
    candidate = build_python_support_drop_impact_candidate(PR, DEPENDENCY, claim)
    before = evaluate_python_support_drop_impact(candidate)
    need = select_python_support_drop_investigation(before)
    target_file = project_file("2.0", HEAD)
    declaration = interpret_target_python_declaration(target_file)
    relevance = evaluate_target_python_relevance(claim, declaration)
    after = evaluate_python_support_drop_impact(candidate, relevance)
    records = (
        native("upstream:authority", authority),
        native("upstream:proposal", proposal, ("upstream:authority",)),
        native("upstream:grounded", claim, ("upstream:authority", "upstream:proposal")),
        native(
            "support:candidate",
            candidate,
            ("upstream:grounded", "dependency", "target:pr"),
        ),
        native("support:before", before, ("support:candidate",)),
        native("support:need", need, ("support:before",)),
        source("target:project-text", target_file),
        native("support:target-declaration", declaration, ("target:project-text",)),
        native(
            "support:relevance",
            relevance,
            ("support:target-declaration", "upstream:grounded"),
        ),
        native("support:after", after, ("support:before", "support:relevance")),
    )
    return records, {
        "before": before.applicability.state,
        "relevance": relevance.state,
        "after": after.applicability.state,
        "extraction": "supplied candidate, no semantic extractor",
    }


def _conditional_records():
    """Extract real optional-extra source context; evaluate selection without marker truth."""
    base, head = project_file("1.0", BASE), project_file("2.0", HEAD)
    changed = ChangedFile("pyproject.toml", "modified", 1, 1, 2, None)

    class OfflineFiles:
        def get_pull_request_base_file(self, identity, path):
            return base

        def get_pull_request_head_file(self, identity, path):
            return head

    analysis = analyze_dependency_change(PR, (changed,), OfflineFiles())
    workflow = RepositoryTextFile(
        REPOSITORY,
        ".github/workflows/optional.yml",
        HEAD,
        'jobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - run: pip install -e ".[speed]"\n',
    )
    result = inspect_workflow_dependency_evidence(
        workflow,
        source_contexts=analysis.source_contexts,
        package="demo",
        normalized_package="demo",
        project_environment_sources=(
            WorkflowProjectEnvironmentSource(analysis.source_contexts[0], head),
        ),
    )
    return (
        source("extra:base", base),
        source("target:project-text", head),
        source("extra:workflow", workflow),
        native("extra:changed-file", changed),
        native(
            "extra:analysis",
            analysis,
            ("extra:base", "target:project-text", "extra:changed-file", "target:pr"),
        ),
        native(
            "extra:selection",
            result,
            ("extra:analysis", "extra:workflow", "target:project-text"),
        ),
    ), {
        "marker": analysis.source_contexts[0].requirement_marker,
        "consumptions": [
            {"state": item.state, "reason": item.reason} for item in result.consumptions
        ],
    }


def build_retention_corpus() -> TraceCorpus:
    ci, ci_outcomes = _ci_records()
    support, support_outcomes = _support_records()
    optional, optional_outcomes = _conditional_records()
    observations = (
        source("read:empty", RepositoryTextFile(REPOSITORY, "empty.txt", HEAD, "")),
        native(
            "read:failed",
            UnavailableRepositoryFile(
                REPOSITORY,
                "missing.txt",
                HEAD,
                "not_found",
                "Offline fixture read was unavailable.",
            ),
        ),
        simulated(
            "discovery",
            "discovery",
            {"coverage": "limited", "purpose": "bounded update investigation"},
            ("dependency",),
        ),
        simulated(
            "request",
            "request",
            {"basis": "discovery", "expected": "exact-file read"},
            ("discovery",),
        ),
        simulated(
            "admission",
            "admission",
            {"outcome": "admitted", "authority": "historical only"},
            ("request",),
        ),
        simulated(
            "attempt:unknown",
            "attempt",
            {"outcome": "completion_unknown", "retry_permission": None},
            ("admission",),
        ),
        simulated(
            "proposal:api",
            "proposal",
            {"meaning": "candidate interpretation, unevaluated"},
            ("read:empty",),
        ),
        simulated(
            "evaluation:unsupported",
            "evaluation_attempt",
            {"outcome": "unsupported", "assessment": None},
            ("proposal:api",),
        ),
        TraceRecord(
            "method:missing",
            "experiment.lifecycle",
            "method_identity",
            SCOPE,
            None,
            (),
            "Model/config identity not supplied; no model was invoked.",
        ),
    )
    view = simulated(
        "view:delivered",
        "view",
        {
            "delivered": ["ci:runtime", "read:empty"],
            "omitted_but_addressable": ["support:after", "extra:selection"],
            "examined": "unknown",
        },
        (
            "ci:runtime",
            "read:empty",
            "support:after",
            "extra:selection",
            "method:missing",
        ),
    )
    roots = (
        "view:delivered",
        "attempt:unknown",
        "evaluation:unsupported",
        "read:failed",
        "support:need",
    )
    annotation = simulated(
        "annotation",
        "annotation",
        {"note": "Host navigation metadata; original native bytes unchanged"},
        ("ci:runtime",),
    )
    unrelated = simulated(
        "unreferenced-debug",
        "diagnostic",
        {"discardable": "not a material consumer dependency"},
    )
    lineage = simulated(
        "lineage",
        "lineage",
        {
            "relationship": "successor assessment, no native overwrite",
            "reason": "target relevance supplied",
        },
        ("support:before", "support:after"),
    )
    return TraceCorpus(
        encode_fields({"pull_request": PR, "dependency": DEPENDENCY}),
        (
            (ci, ("ci:runtime",)),
            (
                support + optional,
                ("ci:runtime", "support:after", "support:need", "extra:selection"),
            ),
            (observations + (view,), roots),
            ((annotation, unrelated, lineage), roots + ("annotation", "lineage")),
        ),
        {
            "ci": ci_outcomes,
            "support": support_outcomes,
            "conditional": optional_outcomes,
        },
    )
