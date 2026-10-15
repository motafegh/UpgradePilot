import json
import sys
from dataclasses import asdict
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch

from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.lifecycle_boundary import reconstruct_lifecycle_history
from upgradepilot.workspace.native_projection import reconstruct_ci_projection
from upgradepilot.workspace.native_representation import NativeReconstructionError

root = Path(sys.argv[1])
mode = sys.argv[2]
blocked = [
    "upgradepilot.github.pull_request.GitHubPullRequestClient.get_pull_request",
    "upgradepilot.github.actions.GitHubActionsClient.get_exact_head_workflow_runs",
    "upgradepilot.github.repository.GitHubRepositoryClient.get_exact_head_text_file",
    "upgradepilot.upstream.support_drop.evaluate_support_drop_runtime",
    "upgradepilot.maintainer_action.synthesize_maintainer_action",
    "upgradepilot.ci.dependency_exercise.evaluate_dependency_ci_coverage",
    "upgradepilot.ci.dependency_state.evaluate_runtime_dependency_state",
    "socket.socket.connect",
]
if mode == "current":
    blocked.append("upgradepilot.workspace.source_access.RetainedSourceCatalog.query")
guards = [
    patch(name, side_effect=AssertionError("forbidden reentry")) for name in blocked
]
for guard in guards:
    call = guard.start()
    try:
        call()
    except AssertionError:
        pass
    else:
        raise AssertionError("inactive guard")
manifest = json.loads((root / "manifest.json").read_text())
results = []
for index, case in enumerate(manifest["cases"]):
    directory = root / f"case-{index + 1}" / "checkpoint"
    database = directory / "workspace.sqlite3"
    before = sha256(database.read_bytes()).hexdigest()
    target = ExactInvestigationTarget(**case["target"])
    store = CheckpointStore.open(directory, read_only=True)
    stored = store.read_revision(
        case["lineage_id"], case["revision_id"], expected_target=target
    )
    bases = {}
    current = stored.revision
    while True:
        bases[current.revision_id] = current.boundary
        if current.predecessor_id is None:
            break
        current = store.read_revision(
            case["lineage_id"], current.predecessor_id, expected_target=target
        ).revision
    projection = reconstruct_ci_projection(
        stored.revision.boundary, expected_target=target
    )
    result = {
        "case": case["case_id"],
        "native_coverage": projection.ci_coverage_result.state,
        "projection_sha256": sha256(
            json.dumps(asdict(projection), sort_keys=True).encode()
        ).hexdigest(),
        "guard_count": len(guards),
        "retained_revisions": len(bases),
    }
    try:
        values = reconstruct_lifecycle_history(
            stored.revision.lifecycle_history, bases=bases
        )
    except NativeReconstructionError as error:
        assert mode == "old" and error.reason == "unsupported_lifecycle_codec", str(
            error
        )
        result["lifecycle"] = error.reason
    else:
        assert mode == "current"
        from upgradepilot.workspace.lifecycle_records import (
            ViewDelivery,
            ContentCitation,
            EvaluationOutcome,
        )
        from upgradepilot.workspace.source_access import read_source_delivery

        deliveries = [v.value for v in values if isinstance(v.value, ViewDelivery)]
        sources = [
            read_source_delivery(d.retained_content.encode())
            for d in deliveries
            if d.representation == "retained-source-view/1"
        ]
        assert len(deliveries) == 5 and len(sources) == 4
        read, resolved = sources[-2:]
        assert read["payload"] == resolved["payload"]
        assert all(s["catalog_id"] == case["catalog_id"] for s in sources)
        assert sum(isinstance(v.value, ContentCitation) for v in values) == 1
        assert [
            v.value.outcome for v in values if isinstance(v.value, EvaluationOutcome)
        ] == ["unsupported"]
        result.update(
            lifecycle="supported",
            deliveries=5,
            citations=1,
            proposal_evaluation="unsupported",
        )
    result["database_unchanged"] = before == sha256(database.read_bytes()).hexdigest()
    assert result["database_unchanged"]
    results.append(result)
print(
    json.dumps(
        {
            "mode": mode,
            "module": __import__("upgradepilot").__file__,
            "results": results,
        },
        indent=2,
    )
)
