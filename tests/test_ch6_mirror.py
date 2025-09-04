from importlib import import_module


def test_mirror_test_outputs_group_accuracy():
    mod = import_module("chapters._06_mirror_of_man.code.mirror_test")
    res = mod.mirror_test()
    assert set(res.keys()) == {"M", "F"}
    for v in res.values():
        assert 0.0 <= v <= 1.0


