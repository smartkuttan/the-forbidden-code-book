import os
import matplotlib

if os.environ.get("CI") == "true":
    matplotlib.use("Agg")

import matplotlib.pyplot as plt


def build_and_save_risk_map(points: dict, outfile: str = "risk_map_ch2.png") -> str:
    plt.figure(figsize=(6, 5))
    for name, (l, i) in points.items():
        plt.scatter(l, i, s=80)
        plt.text(l + 0.01, i + 0.01, name, fontsize=8)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel("Likelihood (0–1)")
    plt.ylabel("Impact (0–1)")
    plt.title("Ethical Risk Map – Chapter 2")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(outfile, dpi=160)
    return outfile


if __name__ == "__main__":
    risks = {
        "Bias": (0.8, 0.9),
        "Privacy": (0.7, 1.0),
        "Deception": (0.6, 0.7),
        "Ops": (0.4, 0.5),
    }
    print(build_and_save_risk_map(risks))


