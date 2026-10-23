"""Inspect installed CLI sources outside the checkout, with acquisition forbidden.

Usage: project-python THIS_FILE /absolute/fresh/venv. The fresh environment is installed
separately with pip install .; no install/network work occurs in this recipe.
"""

import json
import os
from pathlib import Path
import subprocess
import sys


CHILD = r'''
from contextlib import ExitStack, redirect_stdout
from hashlib import sha256
from io import StringIO
import importlib.metadata
import json, runpy, sys
from pathlib import Path
from unittest.mock import patch
import upgradepilot
from upgradepilot.report_file import read_report
from upgradepilot.report import render_report_source
prefix, cases = Path(sys.argv[1]), json.loads(sys.argv[2])
assert Path(upgradepilot.__file__).is_relative_to(prefix)
receipts = {}
with ExitStack() as stack:
 for name in ('socket.socket.connect', 'requests.sessions.Session.request',
              'upgradepilot.cli.investigate_public_pull_request',
              'upgradepilot.cli.os.getenv', 'upgradepilot.cli.save_report',
              'upgradepilot.report_projection.synthesize_maintainer_action',
              'upgradepilot.upstream.support_drop.evaluate_support_drop_runtime'):
  stack.enter_context(patch(name, side_effect=AssertionError(name)))
 for name, filename in cases.items():
  path = Path(filename)
  before = path.read_bytes()
  report = read_report(path)
  source = next(s for s in report.sources if s.kind == 'pull_request')
  sys.argv = [str(prefix / 'bin/upgradepilot'), '--open-report', str(path), '--show-source', source.source_id]
  output = StringIO()
  with redirect_stdout(output):
   try:
    runpy.run_path(sys.argv[0], run_name='__main__')
   except SystemExit as exit:
    assert exit.code == 0
   else:
    raise AssertionError('installed console script did not exit')
  assert output.getvalue() == render_report_source(report, source.source_id) + '\n'
  assert path.read_bytes() == before
  receipts[name] = {'return_code': 0, 'view_sha256': sha256(output.getvalue().encode()).hexdigest(),
                    'original_report_unchanged': True, 'source_bytes': len(source.content.encode())}
print(json.dumps({'installed_module': upgradepilot.__file__, 'cases': receipts,
                  'network_provider_synthesis_save_forbidden': True,
                  'distributions': {d.metadata['Name']: d.version for d in importlib.metadata.distributions()}}, indent=2))
'''


if __name__ == "__main__":
    prefix = Path(sys.argv[1]).resolve()
    receipt = json.loads(Path(__file__).with_name("retained-case-receipt.json").read_text())
    cases = {name: str(Path(item["private_output"]) / "report.json") for name, item in receipt["cases"].items()}
    env = dict(os.environ)
    env.pop("PYTHONPATH", None)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    output = subprocess.run([str(prefix / "bin/python"), "-c", CHILD, str(prefix), json.dumps(cases)],
                            cwd=prefix.parent, env=env, capture_output=True, text=True, timeout=20)
    if output.returncode:
        raise RuntimeError(output.stderr)
    result = json.loads(output.stdout)
    for command in ([str(prefix / "bin/python"), "-m", "pip", "check"],
                    [str(prefix / "bin/upgradepilot"), "--help"],
                    [str(prefix / "bin/python"), "-m", "upgradepilot", "--help"]):
        checked = subprocess.run(command, cwd=prefix.parent, env=env, capture_output=True, text=True, timeout=15)
        assert checked.returncode == 0, checked.stderr
        if "--help" in command:
            assert "--show-source" in checked.stdout
    result["pip_check_and_both_help_entrypoints"] = "passed"
    result["installation"] = "fresh venv; pip install . with normal package-index access; no dependency added to project"
    print(json.dumps(result, indent=2))
