import pandas as pd
from sklearn.metrics import confusion_matrix


def build_sample_df() -> pd.DataFrame:
    data = {
        "applicant_id": [1, 2, 3, 4, 5, 6],
        "gender": ["M", "F", "M", "F", "M", "F"],
        "approved": [1, 0, 1, 0, 1, 0],
        "prediction": [1, 0, 1, 1, 1, 0],
    }
    return pd.DataFrame(data)


def group_accuracy(df: pd.DataFrame, group_col: str, outcome_col: str, pred_col: str) -> dict:
    results: dict = {}
    for group_value in df[group_col].unique():
        subset = df[df[group_col] == group_value]
        cm = confusion_matrix(subset[outcome_col], subset[pred_col])
        accuracy = (cm[0, 0] + cm[1, 1]) / cm.sum()
        results[str(group_value)] = float(accuracy)
    return results


def mirror_test() -> dict:
    df = build_sample_df()
    return group_accuracy(df, "gender", "approved", "prediction")


if __name__ == "__main__":
    print(mirror_test())


