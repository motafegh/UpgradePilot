"""Allow ``python -m upgradepilot`` to run the command-line interface."""

from .cli import main

raise SystemExit(main())
