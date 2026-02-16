import numpy as np
from sys import argv
import handle_storage as hs
import load_csv as lc

LEARNING_RATE: float = 0.02
N_ITERATIONS: int = 200


def normalize(x: np.ndarray) -> tuple[np.ndarray, float, float]:
    """Normalize features to mean 0 and std 1."""
    mean = float(np.mean(x))
    std = float(np.std(x))
    if std == 0:
        std = 1.0
    return (x - mean) / std, mean, std


def denormalize_theta1(theta1: float, mean: float, std: float) -> float:
    """Convert normalized theta1 back to original scale."""
    return theta1 / std


def train_step(
        x: np.ndarray,
        y: np.ndarray,
        theta0: float,
        theta1: float,
        learning_rate: float
) -> tuple[float, float]:
    try:
        m = len(x)

        y_hat = theta0 + theta1 * x
        error = y_hat - y

        tmp_theta0 = learning_rate * (1 / m) * np.sum(error)
        tmp_theta1 = learning_rate * (1 / m) * np.sum(error * x)

        theta0 -= tmp_theta0
        theta1 -= tmp_theta1

        return theta0, theta1
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return 0, 0


def train(
        x: np.ndarray,
        y: np.ndarray,
        learning_rate: float = LEARNING_RATE,
        n_iterations: int = N_ITERATIONS
) -> tuple[float, float]:
    x_normalized, x_mean, x_std = normalize(x)

    theta0, theta1 = 0.0, 0.0
    for _ in range(n_iterations):
        theta0, theta1 = train_step(
            x_normalized, y, theta0, theta1, learning_rate
        )
        if theta0 == 0 and theta1 == 0:
            print("Training step failed. Exiting training loop.")
            break

    theta1 = denormalize_theta1(theta1, x_mean, x_std)
    theta0 = theta0 - theta1 * x_mean

    return theta0, theta1


def start_training(data: np.ndarray):
    if data.size > 0:
        x = data[:, 0]
        y = data[:, 1]
        theta0, theta1 = train(x, y)
        print(f"Trained parameters: theta0 = {theta0}, theta1 = {theta1}")
        hs.save((theta0, theta1))


def load_data(filepath: str) -> np.ndarray:
    df = lc.load(filepath)
    if df is None:
        return np.array([])
    x = df['km'].to_numpy()
    y = df['price'].to_numpy()
    return np.column_stack((x, y))


def main():
    try:
        if len(argv) > 2:
            raise ValueError("Usage: py train.py [dataset.csv]")
        filepath = argv[1] if len(argv) == 2 else "data.csv"
        start_training(load_data(filepath))
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
