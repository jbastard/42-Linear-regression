from pathlib import Path

import pandas as pd


def load(path: str | Path) -> pd.DataFrame | None:
    """Load data from a CSV file into a pandas DataFrame."""
    csv_path = Path(path)
    try:
        if not csv_path.exists():
            raise FileNotFoundError(f'"{csv_path}"')
        if csv_path.suffix != ".csv":
            raise AssertionError(
                f"Wrong format: need .csv got {csv_path.suffix} instead"
            )

        df = pd.read_csv(csv_path)
        if df.empty:
            raise AssertionError(f'Unable to load "{csv_path}"')

        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"{type(e).__name__}: {e}.")
        return None
