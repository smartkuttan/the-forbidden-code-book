from __future__ import annotations

import base64
from typing import List


class DataCollector:
    def __init__(self) -> None:
        # Minimal storage: keep only redacted tokens
        self._tokens: List[str] = []

    def collect(self, user_input: str, consent: bool) -> str:
        if not consent:
            return "Consent required."
        token = self._tokenize(user_input)
        self._tokens.append(token)
        return "Data collected (tokenized)."

    def list_tokens(self) -> List[str]:
        return list(self._tokens)

    @staticmethod
    def _tokenize(value: str) -> str:
        # Very lightweight reversible encoding to simulate encryption-at-rest.
        return base64.b64encode(value.encode("utf-8")).decode("ascii")


if __name__ == "__main__":
    dc = DataCollector()
    print(dc.collect("User Location: Rome", consent=False))
    print(dc.collect("User Location: Rome", consent=True))
    print("Stored tokens:", dc.list_tokens())


