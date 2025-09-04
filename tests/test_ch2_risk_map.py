import os
from importlib import import_module


def test_risk_map_outputs_file(tmp_path):
    mod = import_module("chapters._02_temptation_of_speed.code.risk_map")
    outfile = tmp_path / "risk.png"
    path = mod.build_and_save_risk_map({"X": (0.3, 0.9)}, outfile=str(outfile))
    assert os.path.exists(path)


