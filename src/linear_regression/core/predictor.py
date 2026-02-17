from ..infrastructure import storage


def estimate_price() -> float | None:
    try:
        t0, t1 = storage.load()
        if t0 is None or t1 is None:
            t0, t1 = 0, 0

        mileage = input("Enter mileage: ")
        if not mileage.replace(".", "", 1).isdigit():
            raise ValueError("Mileage must be a number.")

        price = max(t1 * float(mileage) + t0, 0.0)
        print(f"Estimated price: {price:.2f}")
        return price
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    return None
