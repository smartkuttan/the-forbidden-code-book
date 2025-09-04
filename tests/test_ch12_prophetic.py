from importlib import import_module


def test_prophetic_watchtower_outputs_gap():
    mod = import_module("chapters._12_prophecies_of_tomorrow.code.prophetic_watchtower")
    res = mod.run_prophetic_check()
    assert "rates" in res and "gap" in res
    assert 0.0 <= res["gap"] <= 1.0


