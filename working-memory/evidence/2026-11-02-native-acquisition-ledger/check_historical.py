"""Cold-read indexed historical bundles without changing or re-producing them."""
from contextlib import ExitStack
from hashlib import sha256
import json
from pathlib import Path
from unittest.mock import patch

from experiments import api_call_signature_trial as curated
from experiments import api_ordinary_call_signature_trial as ordinary
from upgradepilot.caller_signature import analysis, correspondence, worker

HERE = Path(__file__).resolve().parent
INDEX = HERE.parent / '2026-11-01-native-caller-signature-kernel-transfer/historical-compatibility.json'
readers = dict(open_comparison=curated.open_comparison,
    open_ordinary_comparison=ordinary.open_ordinary_comparison,
    open_fresh_ordinary_pr_attempt=ordinary.open_fresh_ordinary_pr_attempt)


def members(directory):
    return {str(p.relative_to(directory)): sha256(p.read_bytes()).hexdigest()
            for p in directory.rglob('*') if p.is_file()}


rows = []
for indexed in json.loads(INDEX.read_bytes())['opened']:
    directory = Path(indexed['path'])
    before = members(directory)
    with ExitStack() as stack:
        for name in ('ast.parse', 'requests.sessions.Session.request', 'socket.socket.connect'):
            stack.enter_context(patch(name, side_effect=AssertionError('No producer/network during cold read')))
        for owner, name in ((analysis, 'extract_python_source'),
            (correspondence, 'discover_source_candidates'), (worker, 'run_source_analysis')):
            stack.enter_context(patch.object(owner, name, side_effect=AssertionError('No analysis during cold read')))
        readers[indexed['reader']](directory)
    if members(directory) != before:
        raise AssertionError('Frozen bundle changed')
    rows.append(dict(path=indexed['path'], reader=indexed['reader'], members_unchanged=len(before),
        members_sha256=sha256(json.dumps(before, sort_keys=True).encode()).hexdigest()))
result = dict(bundles=len(rows), opened=rows, native_producer_or_network_calls=0,
              proof='fixed historical read and unchanged bytes; not source acquisition or native profile adoption')
(HERE / 'historical-compatibility.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(dict(bundles=len(rows), members_unchanged=sum(x['members_unchanged'] for x in rows))))
