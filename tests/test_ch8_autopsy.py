from importlib import import_module


def test_autopsy_demo_outputs_lessons():
    mod = import_module("chapters._08_wrath_of_the_world.code.ethical_autopsy")
    report = mod.demo_report()
    assert isinstance(report, dict)
    assert report["Lessons"]


