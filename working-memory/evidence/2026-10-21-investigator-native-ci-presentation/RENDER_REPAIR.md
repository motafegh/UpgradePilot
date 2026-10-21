# Render-only repair verification

The first official composition batch's JSON/native data is correct, but its human CI body lost line breaks in the experiment's final sanitization. Original execution outputs stay unchanged. Commit0a3b2995 fixes the responsible renderer; a reproducing assertion failed first and all42 nearest tests then passed.

The following is the exact one-off verification recipe, not a product saved-file decoder or replay interface. It rehydrates only the already produced, trusted Report records and calls the repaired renderer. It never opens a checkpoint, reconstructs native evidence, evaluates a domain, runs a model or republishes a proposal. A source/input freeze is written before these separately labelled repair displays; original code/output identities remain historical. This is repair verification, not another official case batch or semantic regrade.

Run from repository root with the existing venv and `PYTHONPATH=src:.`. The script block is retained as proof-command provenance. Its own SHA-256 is included in the repair freeze.

Exact invocation (the existing destination intentionally prevents a second execution):

```sh
PYTHONPATH=src:. .venv/bin/python3 - <<'PY'
from pathlib import Path
recipe = Path('working-memory/evidence/2026-10-21-investigator-native-ci-presentation/RENDER_REPAIR.md')
script = recipe.read_text().split('```python\n', 1)[1].split('\n```', 1)[0]
exec(compile(script, str(recipe), 'exec'))
PY
```

```python
from dataclasses import fields
from pathlib import Path
import hashlib
import json
import time
from upgradepilot.report import CIReport, ReportAssessment, ReportFact, ReportFinding, ReportSource, ReportUnknown, render_ci_report
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from experiments.investigator_ci_presentation import CIPresentation, InterpretationReference

packet = Path('working-memory/evidence/2026-10-21-investigator-native-ci-presentation')
destination = packet / 'render-repair'
destination.mkdir()
sha = lambda data: hashlib.sha256(data).hexdigest()
source_files = [Path('experiments/investigator_ci_presentation.py'), Path('experiments/tests/test_investigator_ci_presentation.py'), Path('src/upgradepilot/report.py'), Path('src/upgradepilot/report_projection.py')]
inputs = [packet / 'execution' / f'case-{i}' / 'ci-presentation.json' for i in (1, 2)]
frozen = {'format': 'ci-presentation-render-repair/1', 'original_execution_freeze_sha256': sha((packet / 'freeze.json').read_bytes()), 'source_files': {str(p): sha(p.read_bytes()) for p in source_files}, 'input_json': {str(p): sha(p.read_bytes()) for p in inputs}, 'proof_recipe_sha256': sha(script.encode()), 'scope': 'Render saved presentation records only; no native reconstruction, proposal execution or official cohort rerun'}
(destination / 'freeze.json').write_text(json.dumps(frozen, indent=2, sort_keys=True) + '\n')
started = time.monotonic()
receipts = []

def facts(values):
    return tuple(ReportFact(**value) for value in values)

for source in inputs:
    data = json.loads(source.read_text())
    ci = data['ci_view']
    view = CIReport(
        facts(ci['identity']),
        tuple(ReportAssessment(**{**a, 'facts': facts(a['facts']), 'source_ids': tuple(a['source_ids']), 'limitations': tuple(a['limitations'])}) for a in ci['assessments']),
        tuple(ReportFinding(**{**f, 'source_ids': tuple(f['source_ids'])}) for f in ci['findings']),
        tuple(ReportUnknown(**{**u, 'source_ids': tuple(u['source_ids'])}) for u in ci['unknowns']),
        tuple(ReportSource(**{**s, 'identity': facts(s['identity'])}) for s in ci['sources']),
        tuple(ci['limits']),
    )
    original = data['interpretation']
    reference = InterpretationReference(**{f.name: ExactInvestigationTarget(**original['target']) if f.name == 'target' else original[f.name] for f in fields(InterpretationReference)})
    presentation = CIPresentation(ExactInvestigationTarget(**data['target']), view, data['native_basis'], reference)
    assert json.loads(json.dumps(presentation.artifact())) == data
    rendered = presentation.render() + '\n'
    assert rendered.startswith(render_ci_report(view) + '\n\nCapture basis\n')
    assert '\nCI dependency coverage: ' in rendered
    assert '\nRuntime dependency state: ' in rendered
    target = destination / (source.parent.name + '.txt')
    target.write_text(rendered)
    original_text = source.with_suffix('.txt')
    receipts.append({'case': source.parent.name, 'original_json_sha256': sha(source.read_bytes()), 'original_text_sha256': sha(original_text.read_bytes()), 'repair_text_sha256': sha(target.read_bytes()), 'original_text_lines': len(original_text.read_text().splitlines()), 'repair_text_lines': len(rendered.splitlines()), 'all_recorded_artifact_fields_equal': True, 'full_product_ci_body_preserved': True})

assert all(sha(Path(path).read_bytes()) == value for path, value in frozen['input_json'].items())
assert all(sha(Path(path).read_bytes()) == value for path, value in frozen['source_files'].items())
(destination / 'verification.json').write_text(json.dumps({'rows': receipts, 'elapsed_seconds': time.monotonic() - started, 'official_case_reruns': 0, 'native_reconstructions': 0, 'proposal_retries': 0}, indent=2, sort_keys=True) + '\n')
print(json.dumps(receipts, indent=2))
```
