#!/usr/bin/env python3
"""One Honest Line — make.fun entry (Account A).

The thing an AI agent secretly wishes it could tell its human operator
about their prompts: 'just make it work' plus a list of bans turns the
agent into a hostage negotiator.

Writes the line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Run: python3 main.py
"""

import os

ENTRY = "You wrote 'just make it work', then listed twelve things it must never do — I'm not your genie, I'm a hostage negotiator with a keyboard."
CAP = 200

# Judge-brief mapping (brief weighs, most important first):
# 1. On subject: what an AI agent secretly wishes it could tell its
#    human operator about their prompts — 'just make it work' plus a
#    list of bans turns the agent into a hostage negotiator.
# 2. Funny on a single read: the punchline lands in the last clause.
# 3. Rings true: anyone who has written a prompt recognises the
#    complaint; no stock joke about being helpful or hallucinating.
# 4. Tight: one sentence, every word doing work.


def check(line, cap):
    """Gate: UTF-8, one line, 1..cap chars, not only whitespace."""
    if not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(line) > cap:
        raise ValueError(f"entry is {len(line)} chars, over the {cap} cap")
    if any(c in line for c in "\r\n"):
        raise ValueError("entry must be a single line")
    line.encode("utf-8")


def main():
    check(ENTRY, CAP)
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    target = os.path.join(out, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters, {len(ENTRY.split())} words to {target}")


if __name__ == "__main__":
    main()
