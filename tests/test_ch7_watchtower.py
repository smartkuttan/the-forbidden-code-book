from importlib import import_module
import numpy as np


def test_watchtower_audit_contains_metrics():
    mod = import_module("chapters._07_the_fall_into_the_wild.code.watchtower")
    y_true = np.array([0, 1, 0, 1, 1, 0])
    y_pred = np.array([0, 1, 0, 0, 1, 1])
    group = np.array(["male", "female", "male", "female", "female", "male"])
    tower = mod.Watchtower({"demographic_parity": mod.demographic_parity})
    report = tower.audit(y_true, y_pred, group)
    assert "demographic_parity" in report
    assert all(k.startswith("cm_") for k in report if k.startswith("cm_"))


