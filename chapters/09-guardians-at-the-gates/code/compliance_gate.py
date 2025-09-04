import re
import sys
from pathlib import Path


DISALLOWED_LIBS = {"apache_struts", "insecure_lib"}
PII_PATTERNS = [
    re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),  # US SSN-like
    re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),  # email
]


def check_requirements(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        low = line.lower()
        for lib in DISALLOWED_LIBS:
            if lib in low:
                print(f"ERROR: Disallowed dependency detected -> {lib}")
                sys.exit(1)


def check_file_for_pii(path: Path) -> None:
    if not path.exists():
        return
    text = path.read_text(errors="ignore")
    for pat in PII_PATTERNS:
        if pat.search(text):
            print(f"ERROR: PII-like pattern found in {path}")
            sys.exit(1)


def run_all_checks(project_root: Path) -> None:
    check_requirements(project_root / "env" / "requirements.txt")
    # Scan a few typical code/data entry points
    for rel in ["README.md", "chapters", "projects"]:
        p = project_root / rel
        if p.is_file():
            check_file_for_pii(p)
        elif p.is_dir():
            for sub in p.rglob("*.py"):
                check_file_for_pii(sub)


if __name__ == "__main__":
    run_all_checks(Path(__file__).resolve().parents[3])
    print("Compliance checks passed.")


