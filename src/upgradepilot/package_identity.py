"""Own source-neutral Python distribution identity normalization.

UpgradePilot compares package identities reported by dependency files, PyPI, and
upstream evidence. Those callers need the same PEP 503 comparison rule, so the rule
belongs here instead of inside any one dependency parser or provider client.

This module performs identity normalization only. It does not validate whether a name
came from a trusted source, acquire package metadata, compare versions, or establish a
dependency change.
"""

from __future__ import annotations

import re

_NORMALIZED_PACKAGE_SEPARATOR = re.compile(r"[-_.]+")


def normalize_package_name(package: str) -> str:
    """Return the PEP 503 comparison form of a Python distribution name.

    PEP 503 comparison normalizes ASCII case and treats runs of ``-``, ``_``, and
    ``.`` as one hyphen. The function deliberately does not decide whether the input
    spelling is valid for a particular external source; source-specific validators own
    that responsibility.
    """

    return _NORMALIZED_PACKAGE_SEPARATOR.sub("-", package).lower()
