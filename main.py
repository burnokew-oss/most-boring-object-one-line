"""One-line review of the most boring everyday object: a tea towel.

Writes the entry to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Pure stdlib, deterministic, no network, no randomness, no clock.
"""

import os

ENTRY = (
    "My tea towel's only job is drying dishes, and it is so bad at it "
    "the dishes dry themselves out of embarrassment \u2014 five stars, "
    "would hang again."
)


def main() -> None:
    text = ENTRY
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
