#!/usr/bin/env python3
"""Redirect the preserved completion-recovery harness into a correction bundle.

The semantic contract and request logic are imported unchanged. This wrapper redirects
all generated evidence, records the corrected load-command boundary, and fixes the
result record's provenance link while keeping the first failed attempt immutable.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[2]
PRIOR = (
    ROOT.parent
    / "2026-07-29-gemma-e4b-v1.2-completion-recovery"
    / "diagnostic.py"
)
RESULT_RECORD = (
    REPO_ROOT
    / "working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-load-flag-correction-result.md"
)
CORRECTION_EVIDENCE_PATH = (
    "evidence/2026-07-29-gemma-e4b-v1.2-completion-recovery-load-flag-correction/"
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
prior.RESULT_RECORD = RESULT_RECORD
prior.v1_2.ROOT = ROOT
prior.base.ROOT = ROOT

_original_freeze = prior.freeze
_original_report = prior.report


def correction_freeze() -> None:
    """Preserve the recovery contract and record the one load-command correction."""

    _original_freeze()
    path = ROOT / "frozen-variable-comparison.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    value["load_command_correction"] = {
        "removed_unsupported_argument": "--no-speculative-draft-simple",
        "retained_argument": "--no-speculative-draft-mtp",
        "semantic_request_changed": False,
    }
    value["correction_changed_variables"] = [
        "remove unsupported LM Studio CLI argument --no-speculative-draft-simple"
    ]
    prior.base.write_json(path, value)


def correction_report() -> None:
    """Generate the inherited report, then fix correction-specific provenance."""

    _original_report()
    text = RESULT_RECORD.read_text(encoding="utf-8")
    text = text.replace(
        "# B2 Gemma E4B v1.2 Completion-Recovery Result",
        "# B2 Gemma E4B v1.2 Completion-Recovery Load-Flag Correction Result",
        1,
    )
    text = text.replace(
        "**Operation:** Recover one complete state-contract v1.2 response under the required GPU baseline",
        "**Operation:** Recover one complete state-contract v1.2 response after correcting the rejected LM Studio load flag",
        1,
    )
    text = text.replace(
        "evidence/2026-07-29-gemma-e4b-v1.2-completion-recovery/",
        CORRECTION_EVIDENCE_PATH,
        1,
    )
    marker = "## Frozen change\n\n"
    correction = (
        "The first recovery attempt was preserved. This correction removes only the "
        "unsupported LM Studio CLI argument `--no-speculative-draft-simple`; it does "
        "not alter the semantic request or validator.\n\n"
    )
    text = text.replace(marker, marker + correction, 1)
    RESULT_RECORD.write_text(text, encoding="utf-8")
    (ROOT / "result-record.sha256").write_text(
        f"{prior.sha256_file(RESULT_RECORD)}  {RESULT_RECORD.name}\n",
        encoding="utf-8",
    )


prior.freeze = correction_freeze
prior.report = correction_report

if __name__ == "__main__":
    sys.exit(prior.main())
