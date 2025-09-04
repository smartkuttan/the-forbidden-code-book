from importlib import import_module


def test_fairness_demo_outputs_metrics():
    mod = import_module("chapters._10_sacred_tools.code.fairness_demo")
    res = mod.run_demo()
    assert "overall_accuracy" in res
    assert "by_group" in res and res["by_group"]
    assert "dp_diff" in res


