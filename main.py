# Museum of the Year 3000 entry (Python 3.13, standard library only).
# Writes one original museum label to /output/entry.txt.
# Deterministic: no network, no randomness, no time — the same bytes every run.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

ENTRY = "'Are You Still Watching?' c. 2025. The machine asked this of people who had not moved in six hours."

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(ENTRY, encoding="utf-8")
