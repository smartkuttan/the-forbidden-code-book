import os
import numpy as np
import matplotlib

if os.environ.get("CI") == "true":
    matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
from sklearn.datasets import load_breast_cancer  # noqa: E402
from sklearn.model_selection import train_test_split  # noqa: E402
from sklearn.ensemble import RandomForestClassifier  # noqa: E402
import shap  # noqa: E402


def train_model_random_forest(seed: int = 0):
    data = load_breast_cancer()
    X_train, X_test, y_train, _ = train_test_split(
        data.data, data.target, test_size=0.25, random_state=seed
    )
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=seed,
        min_samples_leaf=2,
        max_features="sqrt",
    )
    model.fit(X_train, y_train)
    return model, X_train, X_test, data.feature_names


def compute_shap_values(model, _x_background, x_explain, feature_names, outfile: str = "ch5_shap_summary.png"):
    # TreeExplainer is efficient for tree models
    explainer = shap.TreeExplainer(model, feature_perturbation="interventional")
    shap_values = explainer.shap_values(x_explain)

    # For binary classification TreeExplainer returns list [class0, class1]
    values = shap_values[1] if isinstance(shap_values, list) else shap_values

    plt.figure(figsize=(8, 6))
    shap.summary_plot(values, x_explain, feature_names=feature_names, show=False)
    plt.tight_layout()
    plt.savefig(outfile, dpi=160)
    return np.asarray(values)


if __name__ == "__main__":
    model, X_train, X_test, names = train_model_random_forest()
    arr = compute_shap_values(model, X_train, X_test, names)
    print("SHAP array shape:", arr.shape)


