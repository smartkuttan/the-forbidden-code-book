import os
import pathlib
import importlib.util
import pandas as pd


def _load_ch1_module():
    root = pathlib.Path(__file__).resolve().parents[1]
    module_path = root / "chapters" / "01-seeds-of-creation" / "code" / "spot_forbidden_fruit.py"
    spec = importlib.util.spec_from_file_location("ch1_spot_forbidden_fruit", str(module_path))
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)  # type: ignore[attr-defined]
    return mod


def test_compute_approval_rates_basic():
    df = pd.DataFrame({
        "group": ["A", "B", "A", "B"],
        "approved": [1, 0, 1, 0]
    })
    mod = _load_ch1_module()
    rates = mod.compute_approval_rates(df, "group", "approved")
    assert rates.loc["A"] == 1.0
    assert rates.loc["B"] == 0.0


def test_plot_risk_map_saves_file(tmp_path):
    risks = {"X": (0.2, 0.9)}
    outfile = tmp_path / "map.png"
    mod = _load_ch1_module()
    path = mod.plot_risk_map(risks, outfile=str(outfile))
    assert os.path.exists(path)


