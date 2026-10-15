import json
import runpy
import socket
from dataclasses import asdict
from pathlib import Path
from unittest.mock import patch

import requests
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.native_projection import reconstruct_ci_projection

PROOF = Path("/tmp/upgradepilot-common-preparation.ObOR9V")
REPO = Path("/home/motafeq/projects/UpgradePilot")
module = runpy.run_path(str(REPO / "tools/prepare_investigator_inputs.py"))
targets = json.loads((PROOF / "targets.json").read_text())
remaining = [
    json.loads(
        (
            PROOF / "real-preparation-2" / f"case-{i + 1}" / "public-acquisition.json"
        ).read_text()
    )
    for i in range(2)
]
sessions = []


class RetainedResponseSession(requests.Session):
    def __init__(self):
        super().__init__()
        self.expected = list(remaining[len(sessions)])
        self.receipts = []
        sessions.append(self)

    def request(self, method, url, **kwargs):
        assert method.upper() == "GET"
        request = requests.Request(method, url, params=kwargs.get("params")).prepare()
        receipt = self.expected.pop(0)
        assert request.url == receipt["url"], (request.url, receipt["url"])
        response = requests.Response()
        response.status_code = receipt["status"]
        response.url = receipt["url"]
        response._content = receipt["body"].encode("utf-8")
        response.encoding = "utf-8"
        self.receipts.append(dict(receipt))
        return response

    def close(self):
        assert not self.expected, (
            "Not all original native-provider operations were consumed."
        )


module["run"].__globals__["RecordedPublicSession"] = RetainedResponseSession
with patch.object(
    socket.socket,
    "connect",
    side_effect=AssertionError("No network in retained-input requalification"),
):
    manifest = module["run"](
        Path(
            "/home/motafeq/.codex/worktrees/broader-llm-agency-research/UpgradePilot/.tmp/broader-agency-pilot/contract2-comparison-20261007/corpus.json"
        ),
        PROOF / "targets.json",
        PROOF / "final-retained-preparation-3",
    )
assert manifest["outcome"] == "qualified_mechanical_preparation", manifest["outcome"]
parity = []
old_manifest = json.loads((PROOF / "real-preparation-2/manifest.json").read_text())
for i, case in enumerate(manifest["cases"]):
    expected = targets[i]
    target = ExactInvestigationTarget(**case["target"])
    projections = []
    for folder, item in [
        ("real-preparation-2", old_manifest["cases"][i]),
        ("final-retained-preparation-3", case),
    ]:
        store = CheckpointStore.open(
            PROOF / folder / f"case-{i + 1}/checkpoint", read_only=True
        )
        revision = store.read_revision(
            item["lineage_id"], item["revision_id"], expected_target=target
        ).revision
        projections.append(
            asdict(reconstruct_ci_projection(revision.boundary, expected_target=target))
        )
    assert projections[0] == projections[1], (
        "Native projection changed under the final shared path."
    )
    assert set(case["native_owner_invocations"].values()) == {1}
    assert case["proposal_evaluation"] == "unsupported"
    parity.append(
        {
            "case": case["case_id"],
            "native_projection_parity": True,
            "native_owner_invocations": case["native_owner_invocations"],
        }
    )
manifest.update(
    execution_mode="retained_public_response_requalification",
    current_network_calls=0,
    retained_provider_operations=sum(len(s.receipts) for s in sessions),
    acquisition_source="real-preparation-2/public-acquisition.json; original timestamps preserved",
    native_parity=parity,
)
(PROOF / "final-retained-preparation-3/manifest.json").write_text(
    json.dumps(manifest, indent=2)
)
print(
    json.dumps(
        {
            key: manifest[key]
            for key in [
                "outcome",
                "execution_mode",
                "current_network_calls",
                "retained_provider_operations",
                "native_parity",
            ]
        }
    )
)
