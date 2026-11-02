"""Compare controlled ordinary acquisition against the pre-transfer project commit.

Only trusted UpgradePilot code runs. Provider responses are authored by existing
controls; target/library text is parsed, never imported or executed. Frozen
captures are not rewritten. Executable identity metadata, observation times and measured elapsed values are
excluded explicitly because these are separate acquisitions over controlled I/O.
"""
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REFERENCE = '0519bab7'
CODE = '''import json,sys
from dataclasses import asdict
from experiments.tests.test_api_public_pr_context import staged_http_control
from experiments.api_change_source_acquisition import TrialAcquisitionPolicy,AcquisitionProblem
from upgradepilot.workspace.source_access import encode_source_catalog

def normalized(value):
 if isinstance(value,dict):
  return {k:("separately_measured" if k in {"observed_at","timestamp","elapsed_seconds","code_sha256"} else normalized(v)) for k,v in value.items()}
 if isinstance(value,(list,tuple)): return [normalized(v) for v in value]
 if hasattr(value,"isoformat"): return value.isoformat()
 return value
rows=[]
for name,policy,noise in [("bounded-default-noise",TrialAcquisitionPolicy(),24),
 ("stage-reservation-partial",TrialAcquisitionPolicy(github_requests=30,source_request_reserve=20),24),
 ("legacy-starvation",None,60)]:
 result,session=staged_http_control(policy,noise=noise)
 if isinstance(result,AcquisitionProblem):
  value=dict(problem=asdict(result))
 else:
  catalog,modules,acquisition=result
  value=dict(catalog=json.loads(encode_source_catalog(catalog)),modules=[asdict(m) for m in modules],acquisition=acquisition)
 rows.append(dict(case=name,projection=normalized(value),github_requests=session.github_requests,
     provider_requests=session.provider_requests,request_limit_reached=session.request_limit_reached))
print(json.dumps(rows,sort_keys=True))
'''


def project(checkout):
    environment = dict(os.environ, PYTHONPATH=os.pathsep.join(str(checkout / p) for p in ('src', '.', 'tests')))
    result = subprocess.run([sys.executable, '-c', CODE], cwd=checkout, env=environment, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    return json.loads(result.stdout)


with tempfile.TemporaryDirectory(prefix='upgradepilot-source-reference-') as tmp:
    reference = Path(tmp)
    archive = subprocess.check_output(['git', 'archive', REFERENCE, 'src', 'experiments'], cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(archive)) as bundle:
        bundle.extractall(reference, filter='data')
    before, after = project(reference), project(ROOT)
    if before != after:
        (HERE / 'source-transfer-reference.json').write_text(json.dumps(before, indent=2) + '\n')
        (HERE / 'source-transfer-current.json').write_text(json.dumps(after, indent=2) + '\n')
        raise AssertionError('Controlled source acquisition differs; inspect retained projections')
    rows = [dict(case=row['case'], github_requests=row['github_requests'], provider_requests=row['provider_requests'],
        request_limit_reached=row['request_limit_reached'],
        source_projection_sha256=hashlib.sha256(json.dumps(row['projection'], sort_keys=True).encode()).hexdigest()) for row in after]
    result = dict(reference_commit=REFERENCE, source_acquisition_equivalent=True, cases=rows,
        excluded_metadata=['code_sha256 (ownership changed)', 'observed_at', 'timestamp', 'elapsed_seconds'],
        proof='Controlled exact catalogs/modules/native prefix/association summaries/coverage/gaps/costs equal pre-transfer implementation; not live acquisition or native profile adoption')
    (HERE / 'source-transfer-equivalence.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
