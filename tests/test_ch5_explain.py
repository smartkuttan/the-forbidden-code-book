from importlib import import_module
import numpy as np


def test_explain_black_box_outputs_shap_array(tmp_path, monkeypatch):
    # Force non-interactive plotting
    monkeypatch.setenv("CI", "true")
    mod = import_module("chapters._05_false_prophets.code.explain_black_box")
    model, X_train, X_test, names = mod.train_model_random_forest(seed=1)
    arr = mod.compute_shap_values(model, X_train, X_test, names, outfile=str(tmp_path / "s.png"))
    assert isinstance(arr, np.ndarray)
    assert arr.ndim == 2
    assert arr.shape[0] == X_test.shape[0]


