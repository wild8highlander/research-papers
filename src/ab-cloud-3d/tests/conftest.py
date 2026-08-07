"""conftest.py — shared fixtures for ab-cloud-3d test suite."""
import sys
from pathlib import Path

# Ensure code/ is importable
CODE_DIR = Path(__file__).resolve().parent.parent / "code"
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))
