# Forbidden Code – Companion Repository

> Code labs, datasets, and checklists for  
> **_The Forbidden Code: AI’s Original Sin and the Path to Ethical Development_**  
> 👉 Kindle Edition: [Amazon Link](https://www.amazon.com/dp/B0FSL9RKM5)

![The Forbidden Code – Book Cover](https://github.com/smartkuttan/the-forbidden-code-book/blob/main/The%20Forbidden%20Code%20KDP%20MOCKUP%20(2).jpg?raw=true)

---

## Purpose

This repository contains runnable Python code, synthetic datasets, unit tests, and mini-projects that accompany the book.  
The goal: turn the book’s parable-like narrative (Eden, the serpent in the code, commandments of ethical coding) into **practical, executable exercises** for developers.

---

## What’s Inside

- **Chapter Labs** – runnable scripts and notebooks mapped to each book chapter  
- **Datasets** – tiny CSV/JSON examples for bias, fairness, and governance labs  
- **Bias & Fairness Tools** – metrics, mitigation, subgroup analysis  
- **Governance Templates** – reproducibility, CI/CD guardrails, audit stubs  
- **Checklists & Patterns** – model cards, risk logs, ethical design prompts  
- **Unit Tests** – pytest coverage to validate examples and exercises

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


