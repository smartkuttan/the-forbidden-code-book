import os
import pandas as pd
import matplotlib

# Use non-interactive backend when display is unavailable (e.g., CI)
if os.environ.get("CI") == "true":
    matplotlib.use("Agg")

import matplotlib.pyplot as plt


def compute_approval_rates(df: pd.DataFrame, group_col: str, label_col: str) -> pd.Series:
    """Return mean approval per group as a pandas Series.

    Parameters
    ----------
    df : DataFrame with group and label columns
    group_col : column name for demographic group
    label_col : binary label column (1=approved)
    """
    grouped = df.groupby(group_col)[label_col].mean()
    return grouped


def plot_risk_map(likelihood_impact: dict, outfile: str = "risk_map.png") -> str:
    """Plot a simple likelihood vs impact scatter and save to file.

    likelihood_impact expects: {"Risk name": (likelihood_0_1, impact_0_1)}
    Returns path to saved image.
    """
    plt.figure(figsize=(6, 5))
    for name, (l, i) in likelihood_impact.items():
        plt.scatter(l, i, s=80)
        plt.text(l + 0.01, i + 0.01, name, fontsize=8)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel("Likelihood (0–1)")
    plt.ylabel("Impact (0–1)")
    plt.title("AI Ethics Risk Map")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(outfile, dpi=160)
    return outfile


def demo() -> pd.Series:
    data = {
        "gender": ["male", "female", "male", "female", "male", "female"],
        "income": [50000, 52000, 48000, 51000, 47000, 53000],
        "loan_approved": [1, 0, 1, 0, 1, 0],
    }
    df = pd.DataFrame(data)
    rates = compute_approval_rates(df, group_col="gender", label_col="loan_approved")

    # Basic illustrative risk map
    risks = {
        "Bias in dataset": (0.8, 0.9),
        "Privacy violation": (0.6, 1.0),
        "Deceptive design": (0.7, 0.7),
        "System downtime": (0.5, 0.4),
    }
    plot_risk_map(risks)
    return rates


if __name__ == "__main__":
    series = demo()
    print(series)


