"""Frozen-component wheel build/install/import proof in temporary local storage.

Uses existing declared build tools, without network resolution or developer
installation changes. Worker subprocess qualification remains a later obligation.
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
SOURCE = "c7161e42"
logs = []


def run(command, cwd, environment):
    result = subprocess.run(command, cwd=cwd, env=environment, capture_output=True, text=True)
    logs.append(result.stdout + result.stderr)
    (HERE / "installed-component-build.txt").write_text("\n".join(logs))
    if result.returncode:
        raise RuntimeError(logs[-1])
    return result.stdout


with tempfile.TemporaryDirectory(prefix="upgradepilot-native-component-") as taskdir:
    base = Path(taskdir)
    source = base / "source"
    source.mkdir()
    archive = subprocess.check_output(["git", "archive", SOURCE, "pyproject.toml", "README.md", "src"], cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(source, filter="data")
    environment = dict(os.environ)
    environment.pop("PYTHONPATH", None)
    # The virtualenv lacks setuptools; use the already-present declared backend
    # for building only. Runtime smoke gets only the temporary installed artifact.
    build_environment = dict(environment, PYTHONPATH="/usr/lib/python3/dist-packages")
    backend = json.loads(run([sys.executable, "-c",
        "import setuptools,json; print(json.dumps({'version':setuptools.__version__,'origin':setuptools.__file__}))"],
        base, build_environment))
    run([sys.executable, "-m", "pip", "wheel", "--no-deps", "--no-build-isolation", "--no-index",
         "--wheel-dir", str(base / "wheels"), str(source)], base, build_environment)
    wheel = next((base / "wheels").glob("*.whl"))
    run([sys.executable, "-m", "pip", "install", "--no-deps", "--no-index", "--target",
         str(base / "installed"), str(wheel)], base, environment)
    environment["PYTHONPATH"] = str(base / "installed")
    code = '''import importlib.util,json,pathlib,sys
from upgradepilot.caller_signature import native_codec as codec
from upgradepilot.caller_signature.analysis import SourceFacts
from upgradepilot.caller_signature.evidence import MeasuredDuration
assert importlib.util.find_spec("experiments") is None
assert pathlib.Path(codec.__file__).resolve().is_relative_to(pathlib.Path(sys.argv[1]))
value=SourceFacts("a"*64,(),(),(),0)
packet=codec.encode_source_facts(value,text="# retained empty source\\n",coverage="complete_file")
assert codec.decode_source_facts(packet,unit_id=value.unit_id,text="# retained empty source\\n",coverage="complete_file")==value
measurement=MeasuredDuration.from_seconds(0.1,"installed component smoke")
assert codec.decode_duration(codec.encode_duration(measurement))==measurement
print(json.dumps({"interpreter":sys.executable,"codec_import_origin":codec.__file__,"experiments_unavailable":True,"component_roundtrip":True}))
'''
    observed = json.loads(run([sys.executable, "-c", code, str(base / "installed")], base, environment))
    summary = dict(proof="installed wheel component smoke, not worker/application qualification",
        source_commit=SOURCE, wheel=wheel.name, wheel_sha256=hashlib.sha256(wheel.read_bytes()).hexdigest(),
        backend=backend, **observed, developer_installation_changed=False, network_package_resolution=False,
        limitations=["Product worker is not transferred; AUDIT-014-I3 worker subprocess proof remains required.",
            "Temporary target installation uses the selected interpreter's existing dependencies, not a dependency-isolation claim."])
(HERE / "installed-component.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary))
