from importlib import import_module


def test_consent_gate_and_tokenization():
    mod = import_module("chapters._03_privacy_in_paradise.code.privacy_minimal")
    dc = mod.DataCollector()
    assert dc.collect("secret", consent=False) == "Consent required."
    assert dc.collect("secret", consent=True).startswith("Data collected")
    tokens = dc.list_tokens()
    assert len(tokens) == 1
    assert tokens[0] != "secret"  # tokenized


