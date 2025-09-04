import logging
from datetime import datetime
from typing import Dict, Callable, Any

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix


def setup_logger(name: str = "watchtower") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
    return logger


def demographic_parity(y_true: np.ndarray, y_pred: np.ndarray, group: np.ndarray) -> Dict[Any, float]:
    rates: Dict[Any, float] = {}
    for g in np.unique(group):
        mask = group == g
        rates[g] = float(np.mean(y_pred[mask]))
    return rates


class Watchtower:
    def __init__(self, metrics: Dict[str, Callable[..., float]]):
        self.logger = setup_logger()
        self.metrics = metrics

    def log_prediction(self, inputs: Dict[str, Any], output: Any) -> None:
        self.logger.info({"ts": datetime.utcnow().isoformat(), "inputs": inputs, "output": output})

    def audit(self, y_true: np.ndarray, y_pred: np.ndarray, group: np.ndarray) -> Dict[str, Any]:
        report: Dict[str, Any] = {}
        # Confusion matrix per group as baseline signal
        for g in np.unique(group):
            mask = group == g
            tn, fp, fn, tp = confusion_matrix(y_true[mask], y_pred[mask]).ravel()
            report[f"cm_{g}"] = {"tn": int(tn), "fp": int(fp), "fn": int(fn), "tp": int(tp)}
        # Named ethical metrics
        for name, func in self.metrics.items():
            report[name] = func(y_true, y_pred, group)
        return report


if __name__ == "__main__":
    # Tiny demo
    y_true = np.array([0, 1, 0, 1, 1, 0])
    y_pred = np.array([0, 1, 0, 0, 1, 1])
    group = np.array(["male", "female", "male", "female", "female", "male"])
    tower = Watchtower({"demographic_parity": demographic_parity})
    print(tower.audit(y_true, y_pred, group))


