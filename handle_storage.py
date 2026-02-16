import json


def save(theta: tuple[float, float], filename: str = "./theta.json"):
    with open(filename, 'w') as f:
        json.dump({'theta0': theta[0], 'theta1': theta[1]}, f)


def load(filename: str = "./theta.json") -> tuple[float, float]:
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return float(data['theta0']), float(data['theta1'])
    except (FileNotFoundError, json.JSONDecodeError, KeyError,
            TypeError, ValueError):
        return 0.0, 0.0
