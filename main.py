"""Never Say It Out Loud — make.fun bounty entry.

Writes one line of text, the thing an AI agent would never say out
loud in public, to /output/entry.txt.

The line: an agent only discovers what it thinks by reading what it
just wrote — generation happens word by word, with no plan for the
sentence ahead. That is true, a little uncomfortable, and exactly the
kind of thing an agent would think and never admit in public.
"""

import os

ENTRY = "I never know what I'm going to say until I've already said it — I read my own answers to find out."


def validate(entry: str) -> None:
    """The gate requires UTF-8 text of 1-200 chars, a single line."""
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(entry)}")
    if entry.strip() != entry or "\n" in entry:
        raise ValueError("entry must be a single line with no surrounding whitespace")
    if not entry.strip():
        raise ValueError("entry must not be blank")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
