#!/usr/bin/env python3
"""Redirect the preserved completion-recovery harness into a new correction bundle.

The semantic contract and request logic are imported unchanged. This wrapper changes
only the evidence/output paths so the first failed attempt remains immutable.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[2]
PRIOR = (
    ROOT.parent
    / "2026-07-29-gemma-e4b-v1.2-completion-recovery"
    / "diagnostic.py"
)

spec = importlib.util.spec_from_file_location(
    "upgradepilot_completion_recovery_prior", PRIOR
)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load prior completion-recovery harness: {PRIOR}")

prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)

# Redirect all generated artifacts into this correction directory.
prior.ROOT = ROOT
prior.RESULT_RECORD = (
    REPO_ROOT
    / "working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-load-flag-correction-result.md"
)
prior.v1_2.ROOT = ROOT
prior.base.ROOT = ROOT

if __name__ == "__main__":
    sys.exit(prior.main())
