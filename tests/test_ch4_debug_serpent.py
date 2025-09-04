from chapters._04_whispers_in_the_syntax import code as _code_pkg  # namespace package
from importlib import import_module


def test_debug_serpent_outputs_metrics():
    mod = import_module("chapters._04_whispers_in_the_syntax.code.debug_serpent")
    df = mod.generate_synthetic_with_proxy(n=200, seed=0)
    out = mod.train_and_evaluate(df)
    assert "proxy_corr" in out and isinstance(out["proxy_corr"], float)
    assert 0 <= (out["by_group"][0]["FPR"]) <= 1
    assert 0 <= (out["by_group"][1]["FPR"]) <= 1


