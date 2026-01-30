from sys import argv
from train import start_training
from tester import tester
import numpy as np
import load_csv as lc
import handle_storage as hs


def load_data(filepath: str) -> np.ndarray:
    df = lc.load(filepath)
    if df is not None:
        x = df['km'].to_numpy()
        y = df['price'].to_numpy()
        data = np.column_stack((x, y))
        return data
    return np.array([])


def main():
    try:
        if len(argv) != 2:
            print("Usage: py main.py <option>")
        data = load_data("data.csv")
        if argv[1] == "train":
            start_training(data)
        elif argv[1] == "test":
            sucess_rate = tester(data, hs.load())
            print(f"Test success rate: {sucess_rate * 100:.2f}%")
        else:
            print("Invalid option. Use 'train' or 'test'.")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
