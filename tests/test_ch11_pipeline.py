from importlib import import_module


def test_new_eden_pipeline_outputs_metrics():
    mod = import_module("chapters._11_builders_of_the_new_garden.code.new_eden_pipeline")
    res = mod.build_and_evaluate()
    assert "overall_accuracy" in res
    assert "accuracy_by_group" in res and res["accuracy_by_group"]


