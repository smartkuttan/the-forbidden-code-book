import numpy as np
from sklearn.metrics import accuracy_score

try:
    from fairlearn.metrics import MetricFrame, selection_rate, demographic_parity_difference
    FAIRLEARN_AVAILABLE = True
except Exception:
    FAIRLEARN_AVAILABLE = False


def run_demo():
    y_true = np.array([1, 0, 1, 1, 0, 0, 1, 0])
    y_pred = np.array([1, 0, 1, 0, 0, 1, 1, 0])
    groups = np.array(["A", "A", "B", "B", "A", "A", "B", "B"])

    result = {"overall_accuracy": float(accuracy_score(y_true, y_pred))}
    if FAIRLEARN_AVAILABLE:
        frame = MetricFrame(
            metrics={"accuracy": accuracy_score, "selection_rate": selection_rate},
            y_true=y_true,
            y_pred=y_pred,
            sensitive_features=groups,
        )
        result["by_group"] = frame.by_group.to_dict()
        result["dp_diff"] = float(demographic_parity_difference(y_true, y_pred, sensitive_features=groups))
    else:
        # Fallback minimal metric per group (selection rate)
        by_group = {}
        for g in np.unique(groups):
            mask = groups == g
            by_group[g] = {"selection_rate": float(np.mean(y_pred[mask]))}
        result["by_group"] = by_group
        result["dp_diff"] = float(by_group["A"]["selection_rate"] - by_group["B"]["selection_rate"])
    return result


if __name__ == "__main__":
    print(run_demo())


