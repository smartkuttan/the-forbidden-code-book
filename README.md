Forbidden Code – Companion Repository
====================================

Purpose
-------
This repository hosts runnable Python code, datasets (synthetic/minimal), unit tests, and example mini‑projects that accompany the book `The Forbidden Code – AI’s Original Sin and the Path to Ethical Development`.

Introduction
------------
This repo mirrors the book’s allegorical style—Eden, serpents, commandments—and turns it into runnable exercises. Each chapter includes a short README, scripts/notebooks, and minimal data so readers can practice while reading.

Quickstart
----------
1) Create a virtual environment and install dependencies.

```
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2) Run tests to verify setup.

```
pytest -q
```

3) Explore chapter examples under `chapters/`. Each chapter contains a `README.md` and a `code/` folder with runnable scripts or notebooks.

Repository Layout
-----------------
- `chapters/` — chapter‑wise folders with code and docs
- `exercises/` — Jupyter notebooks (templates + solutions) per chapter
- `projects/` — mini sample projects reinforcing key concepts
- `tests/` — pytest unit tests validating example outputs
- `datasets/` — small CSV/JSON samples used by exercises
- `env/requirements.txt` — pinned dependencies for a clean setup
- `.github/workflows/ci.yml` — CI pipeline running tests on push/PR

Exercises & Code Examples
-------------------------
- Chapter 1: Spot the Forbidden Fruit — group approval rates and a risk map.
- Chapter 2: Risk Map — visualize likelihood vs impact.
- Chapter 3: Privacy in Paradise — consent gate + tokenized storage.
- Chapter 4: Debug the Serpent — proxy leakage and subgroup metrics.
- Chapter 5: Make the Black Box Speak — SHAP explanations for a tree model.
- Chapter 6: Code the Mirror Test — subgroup accuracy check.
- Chapter 7: Build the Watchtower — logging + demographic parity audit.

Resources
---------
- Book manuscript excerpts are reflected in `book.txt`.
- Minimal datasets are provided in `datasets/`.

Contribution Guidelines
-----------------------
We welcome fixes and improvements. Please:
- Fork the repo and create a feature branch.
- Add or update tests when changing behavior.
- Keep examples lightweight and reproducible.
- Open a pull request describing the change and chapter reference.

Notes
-----
- Examples use minimal synthetic data to keep the repo lightweight and reproducible.
- Where real datasets are required but not redistributable, placeholders and generators are provided.

License
-------
MIT unless otherwise specified within subfolders.


