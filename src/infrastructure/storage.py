import json
from pathlib import Path

from .paths import THETA_PATH


def save(
    theta: tuple[float, float],
    filename: str | Path = THETA_PATH,
) -> None:
    filepath = Path(filename)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump({"theta0": theta[0], "theta1": theta[1]}, f)


def load(filename: str | Path = THETA_PATH) -> tuple[float, float]:
    filepath = Path(filename)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return float(data["theta0"]), float(data["theta1"])
    except (
        FileNotFoundError,
        json.JSONDecodeError,
        KeyError,
        TypeError,
        ValueError,
    ):
        return 0.0, 0.0
