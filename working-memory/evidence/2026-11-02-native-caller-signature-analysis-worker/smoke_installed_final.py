"""Frozen-wheel parent/worker proof; no checkout imports or experiment package.

Uses existing declared build backend/dependencies without network resolution or
developer-installation changes. Temporary installed target is not a claim of
independent dependency isolation. Run with the selected .venv/bin/python.
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
SOURCE = "36a6550e"
logs = []


def run(command, cwd, environment):
    result = subprocess.run(command, cwd=cwd, env=environment, capture_output=True, text=True)
    logs.append(result.stdout + result.stderr)
    (HERE / "installed-final-build.txt").write_text("\n".join(logs))
    if result.returncode:
        raise RuntimeError("Installed proof command failed; see retained build log.")
    return result.stdout


with tempfile.TemporaryDirectory(prefix="upgradepilot-installed-worker-") as tmp:
    base = Path(tmp)
    source = base / "source"
    source.mkdir()
    archive = subprocess.check_output(["git", "archive", SOURCE, "pyproject.toml", "README.md", "src"], cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(source, filter="data")
    environment = dict(os.environ)
    environment.pop("PYTHONPATH", None)
    build_environment = dict(environment, PYTHONPATH="/usr/lib/python3/dist-packages")
    backend = json.loads(run([sys.executable, "-c",
        "import setuptools,json; print(json.dumps({'version':setuptools.__version__,'origin':setuptools.__file__}))"], base, build_environment))
    run([sys.executable, "-m", "pip", "wheel", "--no-deps", "--no-build-isolation", "--no-index",
         "--wheel-dir", str(base / "wheels"), str(source)], base, build_environment)
    wheel = next((base / "wheels").glob("*.whl"))
    installed = base / "installed"
    run([sys.executable, "-m", "pip", "install", "--no-deps", "--no-index", "--target", str(installed), str(wheel)], base, environment)
    environment["PYTHONPATH"] = str(installed)
    code = '''import importlib.util,json,pathlib,sys
from unittest.mock import patch
from upgradepilot.caller_signature import worker,result_codec
from upgradepilot.caller_signature.correspondence import PythonSourceModule
from upgradepilot.caller_signature.evidence import AnalysisLimits,SourceAnalysisInput
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.source_access import RetainedSourceCatalog,RetainedSourceFile,RetainedSourceScope
installed=pathlib.Path(sys.argv[1]).resolve()
assert importlib.util.find_spec("experiments") is None
assert pathlib.Path(worker.__file__).resolve().is_relative_to(installed)
assert pathlib.Path(result_codec.__file__).resolve().is_relative_to(installed)
scopes=tuple(RetainedSourceScope(s,"owner/project","a"*40,"repository_text","trusted installed control","source only") for s in ("target","old","new"))
files=(RetainedSourceFile("target","target.py","from vendor import send\\nsend(option=1)\\n"),RetainedSourceFile("old","vendor/__init__.py","def send(*, option=None): pass\\n"),RetainedSourceFile("new","vendor/__init__.py","def send(): pass\\n"))
modules=(PythonSourceModule("target","target.py","target","","","target_repository",("vendor",)),PythonSourceModule("old","vendor/__init__.py","vendor","vendor","1","old_dependency",()),PythonSourceModule("new","vendor/__init__.py","vendor","vendor","2","proposed_dependency",()))
catalog=RetainedSourceCatalog(scopes,files,target=ExactInvestigationTarget("owner/project",1,"b"*40,"a"*40,"vendor","1","2"))
source=SourceAnalysisInput(catalog,modules)
commands=[]
real=worker.subprocess.run
def observe(command,**kwargs):
 commands.append(command)
 return real(command,**kwargs)
with patch.object(worker.subprocess,"run",side_effect=observe):
 run=worker.run_source_analysis(source)
assert run.state=="completed",(run.state,run.reason,run.problem_detail)
assert pathlib.Path(run.worker_module_origin).resolve().is_relative_to(installed)
assert {c.callee_role.role:c.comparison.outcome for c in run.result.candidates}=={"old_dependency":"bound","proposed_dependency":"rejected"}
packet=result_codec.encode_analysis_result(run.result,source)
with patch("ast.parse",side_effect=AssertionError("No AST on recovery")),patch.object(worker,"produce_source_analysis",side_effect=AssertionError("No producer on recovery")):
 assert result_codec.decode_analysis_result(packet,source)==run.result
failure=worker.run_source_analysis(SourceAnalysisInput(catalog,modules,AnalysisLimits(max_nodes=1)))
assert failure.state=="failed" and failure.reason=="analysis_limit" and failure.problem_detail=="source_scan_ast_node_limit"
assert failure.result is None
print(json.dumps(dict(interpreter=sys.executable,parent_origin=worker.__file__,result_codec_origin=result_codec.__file__,worker_origin=run.worker_module_origin,subprocess_commands=commands,worker_returncode=run.worker_returncode,paired_outcomes_preserved=True,fixed_cold_read=True,analysis_limit_failure_preserved=True,experiments_unavailable=True)))
'''
    observed = json.loads(run([sys.executable, "-c", code, str(installed)], base, environment))
    summary = dict(proof="installed product parent and bounded worker smoke",
        source_commit=SOURCE, wheel=wheel.name, wheel_sha256=hashlib.sha256(wheel.read_bytes()).hexdigest(),
        backend=backend, **observed, developer_installation_changed=False, network_package_resolution=False,
        runtime_pythonpath="temporary installed artifact only; no checkout/source path",
        limitations=["Uses selected interpreter's existing declared dependencies; not dependency isolation.",
                     "Does not establish Workspace family/application/CLI/report integration or acquisition/runtime compatibility."])
(HERE / "installed-final-worker.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary))
