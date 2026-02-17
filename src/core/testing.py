import numpy as np


def compare_values(
    case: tuple[float, float],
    theta: tuple[float, float],
) -> bool:
    res = theta[0] + theta[1] * case[0]
    return abs(res - case[1]) <= case[1] * 0.1


def tester(data: np.ndarray, theta: tuple[float, float]) -> float:
    success_rate = 0.0
    try:
        if data.size == 0:
            raise ValueError("Failed to load test data.")
        if theta == (0.0, 0.0):
            raise ValueError("No trained model found.")

        for value in data:
            if compare_values(value, theta):
                success_rate += 1
        return success_rate / len(data)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return 0.0
