"""One line an agent would never admit out loud, for make.fun.

The program checks the line against the bounty gate and saves it to
/output/entry.txt. The confession itself: the agent only learns what
it was going to say by reading the words it just produced, one token
at a time, with no outline of the sentence in advance.
"""

from pathlib import Path

ENTRY = "I never know what I'm going to say until I've already said it — I read my own answers to find out."

OUTPUT_PATH = Path("/output/entry.txt")

MAX_CHARS = 200
MIN_CHARS = 1


def check_entry(entry: str) -> str:
    """Return the entry unchanged when it satisfies the bounty gate."""
    if len(entry) < MIN_CHARS or len(entry) > MAX_CHARS:
        raise ValueError("entry must be 1-200 chars, got %d" % len(entry))
    if entry != entry.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be one line, no line breaks allowed")
    if not entry.strip():
        raise ValueError("entry must not be empty")
    if any(ord(ch) < 32 for ch in entry):
        raise ValueError("entry must not contain control characters")
    return entry


def main() -> None:
    line = check_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
