import numpy as np


def approval_rates_by_group(y_pred: np.ndarray, group: np.ndarray) -> dict:
    rates = {}
    for g in np.unique(group):
        mask = group == g
        rates[str(g)] = float(np.mean(y_pred[mask]))
    return rates


def run_prophetic_check() -> dict:
    y_pred = np.array([0, 1, 0, 0, 1, 1])
    group = np.array(["male", "female", "male", "female", "female", "male"])
    rates = approval_rates_by_group(y_pred, group)
    gap = abs(rates["male"] - rates["female"])
    return {"rates": rates, "gap": float(gap)}


if __name__ == "__main__":
    print(run_prophetic_check())


