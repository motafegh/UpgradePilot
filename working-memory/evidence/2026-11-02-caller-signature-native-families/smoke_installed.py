"""Frozen wheel: installed parent/worker and fresh-process native store recovery.

No network package resolution or developer-installation change. Inputs are the
explicit synthetic controlled-source-fixture.json, never a fresh provider proof.
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
SOURCE = "ac4c2da1"
logs = []


def run(command, cwd, environment):
    result = subprocess.run(command, cwd=cwd, env=environment, capture_output=True, text=True)
    logs.append(result.stdout + result.stderr)
    (HERE / "installed-build.txt").write_text("\n".join(logs))
    if result.returncode:
        raise RuntimeError("Installed proof failed; see retained build log.")
    return result.stdout


with tempfile.TemporaryDirectory(prefix="upgradepilot-installed-native-families-") as tmp:
    base = Path(tmp)
    source = base / "source"
    source.mkdir()
    archive = subprocess.check_output(["git", "archive", SOURCE, "pyproject.toml", "README.md", "src"], cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(source, filter="data")
    environment = dict(os.environ)
    environment.pop("PYTHONPATH", None)
    build_environment = dict(environment, PYTHONPATH="/usr/lib/python3/dist-packages")
    backend = json.loads(run([sys.executable, "-c", "import setuptools,json; print(json.dumps({'version':setuptools.__version__,'origin':setuptools.__file__}))"], base, build_environment))
    run([sys.executable, "-m", "pip", "wheel", "--no-deps", "--no-build-isolation", "--no-index", "--wheel-dir", str(base / "wheels"), str(source)], base, build_environment)
    wheel = next((base / "wheels").glob("*.whl"))
    installed = base / "installed"
    run([sys.executable, "-m", "pip", "install", "--no-deps", "--no-index", "--target", str(installed), str(wheel)], base, environment)
    environment["PYTHONPATH"] = str(installed)
    code = '''import importlib.util,json,pathlib,sys
from unittest.mock import patch
from upgradepilot.caller_signature import worker,source_codec
from upgradepilot.dependency.change import DependencyVersionChange,DependencyChangeSourceEvidence
from upgradepilot.github.pull_request import PullRequestIdentity,ChangedFile
from upgradepilot.workspace.native_capture import NativeInvestigationCapture
from upgradepilot.workspace.native_projection import reconstruct_caller_signature_projection
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
assert importlib.util.find_spec("experiments") is None
installed=pathlib.Path(sys.argv[1]).resolve()
assert pathlib.Path(worker.__file__).resolve().is_relative_to(installed)
assert pathlib.Path(source_codec.__file__).resolve().is_relative_to(installed)
value=source_codec.decode_sources(pathlib.Path(sys.argv[2]).read_bytes())
assert value.acquisition.origin=="controlled_observation"
t=value.catalog.target
identity=PullRequestIdentity(t.repository,t.pull_number,"Controlled installed source evidence","open",False,"author","main",t.base_sha,"upgrade",t.head_sha,1)
dependency=DependencyVersionChange(t.normalized_package,t.normalized_package,t.old_version,t.proposed_version,(DependencyChangeSourceEvidence("requirements.txt","exact_requirement","changed_file_patch"),))
capture=NativeInvestigationCapture()
capture.start(identity,(ChangedFile("requirements.txt","modified",1,1,2,None),),dependency,())
store=CheckpointStore.create(pathlib.Path(sys.argv[3]),schema_version=2)
host=InvestigationWorkspaceHost(store=store,lineage_id="retained-qualification")
host.initialize(capture.partial_snapshot())
capture.capture_caller_signature_sources(value)
host.publish_native_progress(capture.partial_snapshot())
source_revision=host.current.revision_id
commands=[]
real=worker.subprocess.run
def observe(command,**kwargs):
 commands.append(command)
 return real(command,**kwargs)
with patch.object(worker.subprocess,"run",side_effect=observe):
 result=worker.run_source_analysis(value.analysis_input())
assert result.state=="completed",(result.reason,result.problem_detail)
assert pathlib.Path(result.worker_module_origin).resolve().is_relative_to(installed)
capture.capture_caller_signature_comparison(result)
host.publish_native_progress(capture.partial_snapshot())
restored=reconstruct_caller_signature_projection(host.current.boundary,expected_target=t)
assert restored.comparison==result
assert {c.callee_role.role:c.comparison.outcome for c in result.result.candidates}=={"old_dependency":"bound","proposed_dependency":"rejected"}
from dataclasses import asdict
print(json.dumps(dict(interpreter=sys.executable,parent_origin=worker.__file__,source_codec_origin=source_codec.__file__,worker_origin=result.worker_module_origin,subprocess_commands=commands,target=asdict(t),revisions=[source_revision,host.current.revision_id],paired_outcomes_preserved=True)))
'''
    observed = json.loads(run([sys.executable, "-c", code, str(installed), str(HERE / "controlled-source-fixture.json"), str(base / "store")], base, environment))
    # Only a saved store and exact revision/target selection enter this new
    # interpreter. No live Python values or source fixture cross the recovery.
    selection = dict(target=observed["target"], revisions=observed["revisions"])
    cold = json.loads(run([sys.executable, str(HERE / "cold_open.py"), str(base / "store"), json.dumps(selection)], base, environment))
    assert cold[0]["state"] is None and cold[1]["state"] == "completed"
    assert all(r["origin"] == "controlled_observation" and r["retained_files"] == 3 for r in cold)
    summary = dict(proof="installed native source/comparison capture→host/store→fresh-process fixed recovery",
        proof_inputs="synthetic controlled observations; no normal acquisition/application/CLI proof",
        source_commit=SOURCE, wheel=wheel.name, wheel_sha256=hashlib.sha256(wheel.read_bytes()).hexdigest(),
        backend=backend, **observed, cold_open=cold, experiments_unavailable=True,
        developer_installation_changed=False, network_package_resolution=False,
        limitations=["Reuses selected interpreter's existing declared dependencies, not independent dependency isolation.",
                     "No normal source acquisition/profile/CLI/report/product acceptance is established."])
(HERE / "installed-families.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary))
