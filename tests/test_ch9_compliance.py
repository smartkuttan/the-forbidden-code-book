from importlib import import_module
from pathlib import Path


def test_compliance_gate_runs(tmp_path, monkeypatch):
    mod = import_module("chapters._09_guardians_at_the_gates.code.compliance_gate")
    # Create a tiny project root with safe files
    root = tmp_path
    (root / "env").mkdir()
    (root / "env" / "requirements.txt").write_text("numpy==1.26.4\n")
    (root / "README.md").write_text("ok")
    (root / "chapters").mkdir()
    (root / "projects").mkdir()

    monkeypatch.setattr(mod, "Path", Path)
    mod.run_all_checks(root)


