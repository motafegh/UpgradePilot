"""Fresh-process retained native store proof; no producer/source/model reentry."""
from contextlib import ExitStack
from hashlib import sha256
import json
from pathlib import Path
import sys
from unittest.mock import patch

from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.native_codecs import encode_native_value
from upgradepilot.workspace.native_projection import reconstruct_caller_signature_projection

selection = json.loads(sys.argv[2])
target = ExactInvestigationTarget(**selection["target"])
with ExitStack() as stack:
    hooks = []
    for name in ("ast.parse", "requests.sessions.Session.request", "socket.socket.connect",
                 "upgradepilot.caller_signature.worker.run_source_analysis",
                 "upgradepilot.caller_signature.worker.produce_source_analysis",
                 "upgradepilot.caller_signature.analysis.compare_arguments",
                 "upgradepilot.caller_signature.bindings.analyze_python_bindings",
                 "upgradepilot.caller_signature.correspondence.discover_source_candidates"):
        hooks.append(stack.enter_context(patch(name, side_effect=AssertionError("Forbidden cold producer: " + name))))
    store = CheckpointStore.open(Path(sys.argv[1]), read_only=True)
    output = []
    for revision in selection["revisions"]:
        saved = store.read_revision("retained-qualification", revision, expected_target=target)
        value = reconstruct_caller_signature_projection(saved.revision.boundary, expected_target=target)
        output.append(dict(revision=revision, catalog_id=value.sources.catalog.identity,
            source_sha256=sha256(encode_native_value("caller_signature_sources", value.sources)).hexdigest(),
            comparison_sha256=sha256(encode_native_value("caller_signature_comparison", value.comparison, sources=value.sources)).hexdigest(),
            state=value.comparison.state if value.comparison else None,
            retained_files=len(value.sources.catalog.files), origin=value.sources.acquisition.origin))
    assert not any(h.called for h in hooks)
print(json.dumps(output))
