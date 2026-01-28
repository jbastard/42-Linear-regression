import os.path
import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Load data from a CSV file into a pandas DataFrame.

    Args:
        path (str): Path to the CSV file to be loaded.

    Returns:
        DataFrame containing CSV data if successful, None if error.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        AssertionError: If file is not CSV format or is empty.
    """

    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"\"{path}\"")
        if not path[-4:] == ".csv":
            raise AssertionError(f"Wrong format: need .csv "
                                 f"got {os.path.splitext(path)[1]} instead")

        df = pd.read_csv(path)
        if df.empty:
            raise AssertionError(f"Unable to load \"{path}\"")

        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"{type(e).__name__}: {e}.")
        return None
