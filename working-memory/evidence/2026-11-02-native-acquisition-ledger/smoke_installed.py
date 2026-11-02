"""Freeze/build/install a selected source commit; exercise the installed ledger.

No package resolution, developer installation change, live provider or real token.
Existing interpreter dependencies are reused; this is not dependency isolation.
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
SOURCE = sys.argv[1]
logs = []


def run(command, cwd, environment):
    result = subprocess.run(command, cwd=cwd, env=environment, capture_output=True, text=True)
    logs.append(result.stdout + result.stderr)
    (HERE / 'installed-build.txt').write_text('\n'.join(logs))
    if result.returncode:
        raise RuntimeError('Installed proof failed; see retained build log')
    return result.stdout


with tempfile.TemporaryDirectory(prefix='upgradepilot-installed-acquisition-') as tmp:
    base = Path(tmp)
    source = base / 'source'
    source.mkdir()
    archive = subprocess.check_output(['git', 'archive', SOURCE, 'pyproject.toml', 'README.md', 'src'], cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(source, filter='data')
    environment = dict(os.environ)
    environment.pop('PYTHONPATH', None)
    build_environment = dict(environment, PYTHONPATH='/usr/lib/python3/dist-packages')
    backend = json.loads(run([sys.executable, '-c', 'import setuptools,json; print(json.dumps({"version":setuptools.__version__,"origin":setuptools.__file__}))'], base, build_environment))
    run([sys.executable, '-m', 'pip', 'wheel', '--no-deps', '--no-build-isolation', '--no-index', '--wheel-dir', str(base / 'wheels'), str(source)], base, build_environment)
    wheel = next((base / 'wheels').glob('*.whl'))
    installed = base / 'installed'
    run([sys.executable, '-m', 'pip', 'install', '--no-deps', '--no-index', '--target', str(installed), str(wheel)], base, environment)
    environment['PYTHONPATH'] = str(installed)
    fixture = HERE.parent / '2026-11-02-caller-signature-native-families/controlled-source-fixture.json'
    code = '''import importlib.util,json,pathlib,sys
from dataclasses import replace
from io import BytesIO
from unittest.mock import patch
from requests import Response
from requests.adapters import BaseAdapter
from upgradepilot.caller_signature import acquisition,source_codec
from upgradepilot.github.api import GitHubApiClient
assert importlib.util.find_spec("experiments") is None
installed=pathlib.Path(sys.argv[1]).resolve()
assert pathlib.Path(acquisition.__file__).resolve().is_relative_to(installed)
assert pathlib.Path(source_codec.__file__).resolve().is_relative_to(installed)
class Transport(BaseAdapter):
 def send(self,request,**kwargs):
  response=Response(); response.status_code=200; response.raw=BytesIO(b"{}")
  response.request=request; response.url=request.url
  return response
 def close(self): pass
session=acquisition.AcquisitionSession(policy=acquisition.AcquisitionPolicy(),clock=lambda:0.0)
session.mount("https://",Transport())
with patch("socket.socket.connect",side_effect=AssertionError("No network")):
 with session.stage("installed_control"):
  assert GitHubApiClient(session=session)._get_json_object("https://api.github.com/control",resource="control")=={}
session.finish_acquisition()
transport=session.acquisition_receipt()
assert transport.github_requests==transport.provider_requests==1
sources=source_codec.decode_sources(pathlib.Path(sys.argv[2]).read_bytes())
assert sources.acquisition.origin=="controlled_observation"
sources=replace(sources,acquisition=replace(sources.acquisition,transport=transport))
assert source_codec.decode_sources(source_codec.encode_sources(sources))==sources
print(json.dumps(dict(installed_origin=True,experiments_available=False,provider_requests=1,receipt_native_round_trip=True)))
'''
    smoke = json.loads(run([sys.executable, '-c', code, str(installed), str(fixture)], base, environment))
    result = dict(source_commit=subprocess.check_output(['git', 'rev-parse', SOURCE], cwd=ROOT, text=True).strip(),
        wheel_sha256=hashlib.sha256(wheel.read_bytes()).hexdigest(), build_backend=backend,
        fixture_sha256=hashlib.sha256(fixture.read_bytes()).hexdigest(), smoke=smoke,
        network_package_resolution=False, live_provider_calls=False, dependency_isolation=False,
        proof='installed invocation ledger and native receipt; not connected product source-profile adoption')
    (HERE / 'installed-ledger.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
