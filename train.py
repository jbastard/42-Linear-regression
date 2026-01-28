import numpy as np
import handle_storage as hs
import load_csv as lc


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
        learning_rate: float = 0.01,
        n_iterations: int = 100
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


if __name__ == "__main__":
    df = lc.load("./data.csv")
    if df is not None:
        x = df['km'].to_numpy()
        y = df['price'].to_numpy()
        theta0, theta1 = train(x, y)
        print(f"Trained parameters: theta0 = {theta0}, theta1 = {theta1}")
        hs.save((theta0, theta1))
