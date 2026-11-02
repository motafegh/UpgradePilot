"""Build/install a frozen source commit and run native acquisition controls outside checkout.

Only selected test controls accompany the installed wheel; experiments are absent.
No package resolution, real token, developer-installation change or live socket.
Existing interpreter dependencies are reused rather than isolated.
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


with tempfile.TemporaryDirectory(prefix='upgradepilot-installed-source-acquisition-') as tmp:
    base = Path(tmp)
    source = base / 'source'
    source.mkdir()
    paths = ['pyproject.toml', 'README.md', 'src', 'tests/test_target_source_context.py',
        'tests/test_caller_signature_source_acquisition.py', 'tests/test_github_client.py']
    archive = subprocess.check_output(['git', 'archive', SOURCE, *paths], cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(archive)) as bundle:
        bundle.extractall(source, filter='data')
    environment = dict(os.environ)
    environment.pop('PYTHONPATH', None)
    build_environment = dict(environment, PYTHONPATH='/usr/lib/python3/dist-packages')
    backend = json.loads(run([sys.executable, '-c', 'import setuptools,json; print(json.dumps({"version":setuptools.__version__,"origin":setuptools.__file__}))'], base, build_environment))
    run([sys.executable, '-m', 'pip', 'wheel', '--no-deps', '--no-build-isolation', '--no-index', '--wheel-dir', str(base / 'wheels'), str(source)], base, build_environment)
    wheel = next((base / 'wheels').glob('*.whl'))
    installed = base / 'installed'
    run([sys.executable, '-m', 'pip', 'install', '--no-deps', '--no-index', '--target', str(installed), str(wheel)], base, environment)
    # Copy only the selected authored controls; the archived product source is
    # deliberately absent from runtime imports. Tests are proof drivers, not a
    # product dependency or shipped example.
    controls = base / 'controls'
    controls.mkdir()
    for test in (source / 'tests').glob('*.py'):
        (controls / test.name).write_bytes(test.read_bytes())
    environment['PYTHONPATH'] = os.pathsep.join((str(installed), str(controls)))
    code = '''import importlib.util,json,pathlib,sys,unittest
from unittest.mock import patch
from upgradepilot.caller_signature import source_acquisition,source_codec
from upgradepilot.target import source_context
from upgradepilot.github import repository
assert importlib.util.find_spec("experiments") is None
installed=pathlib.Path(sys.argv[1]).resolve()
for module in (source_acquisition,source_context,repository,source_codec):
 assert pathlib.Path(module.__file__).resolve().is_relative_to(installed)
suite=unittest.TestLoader().loadTestsFromNames(["test_target_source_context","test_caller_signature_source_acquisition"])
with patch("socket.socket.connect",side_effect=AssertionError("No live provider")):
 result=unittest.TextTestRunner(verbosity=1).run(suite)
assert result.wasSuccessful()
print(json.dumps(dict(installed_origins=True,experiments_available=False,tests_run=result.testsRun)))
'''
    output = run([sys.executable, '-c', code, str(installed)], base, environment)
    smoke = json.loads(output)
    result = dict(source_commit=subprocess.check_output(['git', 'rev-parse', SOURCE], cwd=ROOT, text=True).strip(),
        wheel_sha256=hashlib.sha256(wheel.read_bytes()).hexdigest(), build_backend=backend, smoke=smoke,
        network_package_resolution=False, live_provider_calls=False, dependency_isolation=False,
        proof='Installed target/inventory/exact module acquisition and native partial receipt controls; not normal application/profile adoption')
    (HERE / 'installed-source-acquisition.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
