import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def build_and_evaluate(seed: int = 42) -> dict:
    rng = np.random.default_rng(seed)
    n = 1000
    df = pd.DataFrame({
        "feature1": rng.normal(0, 1, n),
        "feature2": rng.normal(0, 1, n),
        "group": rng.choice(["A", "B"], size=n),
    })
    # Create outcome with mild group effect
    df["y"] = ((df["feature1"] + 0.5 * (df["group"] == "A").astype(int) + rng.normal(0, 0.5, n)) > 0).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(df[["feature1", "feature2"]], df["y"], test_size=0.3, random_state=0)
    group_test = df.loc[X_test.index, "group"].values

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    overall_acc = float(accuracy_score(y_test, y_pred))
    # Simple fairness mirror: accuracy by group
    by_group = {}
    for g in np.unique(group_test):
        mask = group_test == g
        by_group[g] = float(accuracy_score(y_test[mask], y_pred[mask]))
    return {"overall_accuracy": overall_acc, "accuracy_by_group": by_group}


if __name__ == "__main__":
    print(build_and_evaluate())


