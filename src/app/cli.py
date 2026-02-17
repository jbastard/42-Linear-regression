from sys import argv
import numpy as np
from ..core import predictor
from ..core.testing import tester
from ..core.training import start_training
from ..infrastructure import data_loader, storage
from ..infrastructure.paths import DATASET_PATH


def load_data(filepath: str) -> np.ndarray:
    df = data_loader.load(filepath)
    if df is not None:
        x = df["km"].to_numpy()
        y = df["price"].to_numpy()
        return np.column_stack((x, y))
    return np.array([])


def main() -> None:
    try:
        if len(argv) != 2:
            raise ValueError("Usage: py main.py <option>")

        data = load_data(str(DATASET_PATH))
        if argv[1] == "train":
            start_training(data)
        elif argv[1] == "test":
            success_rate = tester(data, storage.load())
            print(f"Test success rate: {success_rate * 100:.2f}%")
        elif argv[1] == "run":
            predictor.estimate_price()
        else:
            raise ValueError("Invalid option. Use 'train', 'test' or 'run'.")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
