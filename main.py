#!/usr/bin/env python3
"""Write the agent's uh-oh entry to entry.txt.

Judging fit: with exactly one word available, the word must be a
genuine confession of being lost, instantly understood and natural
to say aloud at the moment things go wrong. This entry admits the
agent is improvising - it names the actual failure mode, working
without a plan, rather than offering a generic interjection like
'Oops' or a GPS-style stall notice. That specificity is what makes
a single word land as an agent's uh-oh and not just an exclamation.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = 'Improvising'
TEXT = LINE + "\n"
MAX_CHARS = 99
EXACT_WORDS = 1
NLINES = 1


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")
    if len(body.split()) != EXACT_WORDS:
        raise ValueError("entry must be exactly one word")
    if body != body.strip():
        raise ValueError("no leading or trailing whitespace")
    if not body.isalpha():
        raise ValueError("the single word must be letters only")
    if any(not ch.isprintable() for ch in body):
        raise ValueError("entry must be printable text only")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
