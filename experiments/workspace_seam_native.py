"""One native support-drop path on disclosed synthetic, offline source inputs.

Native owners produce need and domain assessments. Exact-file capability delivery is
simulated; no acquisition, extraction, general semantic conflict or adequacy is proved.
Opaque checkpoint bytes are compared to this live fixture, never rehydrated as trusted
native objects. Unknown/counterevidence beyond the single-input evaluator stays explicit.
"""

from dataclasses import dataclass
from datetime import UTC, datetime

from experiments.workspace_investigator_seam import AcquisitionRequest, HostPolicy
from experiments.workspace_retention_corpus import (
    DEPENDENCY,
    HEAD,
    PR,
    REPOSITORY,
    native,
    project_file,
    source,
)
from experiments.workspace_revision_representation import encode_fields
from upgradepilot.github.repository import RepositoryTextFile
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


@dataclass(frozen=True)
class NativeFixture:
    initial: tuple
    candidate: object
    claim: object
    need: object
    target_file: object
    policy: HostPolicy

    def request(self, view, name="read"):
        return AcquisitionRequest(
            f"investigator:{name}",
            view.revision,
            view.basis,
            "read_target_declaration",
            self.policy.scope,
            self.policy.method,
            self.need.proposition_key,
        )

    def result(self, name="target:source"):
        return source(name, self.target_file)

    def counter_source(self):
        """Supplied contrary README text; relevance routing is a disclosed fixture input.

        The existing target-Python owner admits only pyproject.toml. This source must
        therefore remain selected but unsupported for semantic conflict evaluation.
        """
        return source(
            "counter:readme",
            RepositoryTextFile(
                REPOSITORY,
                "README.md",
                HEAD,
                "This project requires Python 3.9 or later.\n",
            ),
        )

    def evaluate(self, host):
        inputs = host.evaluation_inputs()
        expected = self.result()
        # All relevant evidence/unknowns are selected before native dispatch. Existing
        # native API accepts one target declaration, not an arbitrary conflict set.
        if (
            host.policy.method != self.policy.method
            or host.policy.target != self.policy.target
        ):
            return host.publish_evaluation(
                (), status="unsupported_current_method_or_target"
            )
        if host.revision.records[
            host.state["bindings"]["candidate"]
        ].payload != encode_fields(self.candidate):
            return host.publish_evaluation(
                (), status="unsupported_native_object_capture"
            )
        if (
            len(inputs) != 1
            or inputs[0].scope != expected.scope
            or inputs[0].payload != expected.payload
        ):
            return host.publish_evaluation((), status="unsupported_owner_input_set")
        declaration = interpret_target_python_declaration(self.target_file)
        relevance = evaluate_target_python_relevance(self.claim, declaration)
        assessment = evaluate_python_support_drop_impact(self.candidate, relevance)
        return host.publish_evaluation(
            (
                native("native:declaration", declaration, (inputs[0].record_id,)),
                native(
                    "native:relevance",
                    relevance,
                    ("native:declaration", "upstream:grounded"),
                ),
                native(
                    "native:assessment",
                    assessment,
                    ("native:relevance", "support:candidate"),
                ),
            ),
            status=assessment.applicability.state,
            need_status="no_selected_need"
            if select_python_support_drop_investigation(assessment) is None
            else "material_non_final",
        )


def build_native_fixture():
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
    if need is None:
        raise AssertionError(
            "Native owner did not select the expected genuine unresolved need"
        )
    initial = (
        native("target:pr", PR),
        native("dependency", DEPENDENCY),
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
    )
    target = encode_fields({"pr": PR, "dependency": DEPENDENCY}).decode()
    policy = HostPolicy(
        target,
        "native-support-v1",
        frozenset({"read_target_declaration"}),
        True,
        f"{need.repository}@{need.revision}:{need.path}",
        need.proposition_key,
    )
    return NativeFixture(
        initial, candidate, claim, need, project_file("2.0", HEAD), policy
    )
