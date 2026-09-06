"""Historical import compatibility for the former B2/X1 local planner module.

Active implementation ownership moved to ``experiments.local_evidence_gap_planner``.
This re-export is retained only for preserved historical experiment/proof utilities.
"""

from experiments.local_evidence_gap_planner import *  # noqa: F401,F403
