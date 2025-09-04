import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


def generate_synthetic_with_proxy(n: int = 500, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    # Sensitive attribute (unobserved in features)
    gender = rng.integers(0, 2, size=n)  # 0,1
    income = rng.normal(50_000 + 5_000 * (gender == 0), 8_000, size=n)
    # Proxy variable correlating with gender (e.g., shopping category pattern)
    proxy = (income > 52_000).astype(int)
    # Outcome with mild bias
    noise = rng.normal(0, 1, size=n)
    approved = (0.02 * (income - 50_000) + 0.5 * (gender == 0) + noise > 0.3).astype(int)
    return pd.DataFrame({
        "income": income,
        "proxy": proxy,
        "approved": approved,
        "gender": gender,
    })


def train_and_evaluate(df: pd.DataFrame) -> dict:
    X = df[["income", "proxy"]]
    y = df["approved"]
    g = df["gender"]
    X_tr, X_te, y_tr, y_te, g_te = train_test_split(X, y, g, test_size=0.3, random_state=0)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_tr, y_tr)
    preds = model.predict(X_te)
    # Group confusion matrices
    metrics = {}
    for group_val in [0, 1]:
        mask = (g_te == group_val)
        tn, fp, fn, tp = confusion_matrix(y_te[mask], preds[mask]).ravel()
        fpr = fp / (fp + tn)
        fnr = fn / (fn + tp)
        metrics[group_val] = {"FPR": fpr, "FNR": fnr}
    # Proxy correlation with gender (simple point-biserial via Pearson)
    proxy_corr = np.corrcoef(df["proxy"], df["gender"])[0, 1]
    return {"by_group": metrics, "proxy_corr": float(proxy_corr)}


if __name__ == "__main__":
    frame = generate_synthetic_with_proxy()
    results = train_and_evaluate(frame)
    print("Proxy correlation (proxy~gender):", round(results["proxy_corr"], 3))
    print("Metrics by group:", results["by_group"]) 


