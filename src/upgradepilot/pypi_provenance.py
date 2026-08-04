"""Compatibility import for PyPI publisher-provenance acquisition.

New product code imports ``upgradepilot.pypi.provenance``. This flat path remains only
while historical tests and tools migrate during source-structure reconciliation.
"""

from .pypi.provenance import *  # noqa: F401,F403
