from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = PACKAGE_ROOT.parent.parent
DATASET_PATH = PROJECT_ROOT / "data" / "data.csv"
THETA_PATH = PROJECT_ROOT / "models" / "theta.json"
