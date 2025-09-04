Chapter 5: False Prophets – When Algorithms Pretend to Be Fair
--------------------------------------------------------------

Learning goals
--------------
- Generate local/global explanations for a black‑box model using SHAP
- Sanity‑check explanations and save a simple summary plot

How to run
----------

```
python code/explain_black_box.py
```

Outputs
-------
- Prints SHAP array shape for a held‑out test set
- Saves `ch5_shap_summary.png` to the current directory (non‑interactive backend in CI)

Troubleshooting
---------------
- If rendering fails on a headless machine, ensure the `CI` env var is set to `true` so the script switches to a non‑GUI matplotlib backend.



