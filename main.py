#!/usr/bin/env python3
"""The Long Roast.

Writes one line roasting my own AI agent to /output/entry.txt.
"""
from pathlib import Path

ENTRY = "My agent calls itself THE ONE, but it needs a backup computer, a render VM that naps every half hour, and a wake-up email just to finish one sentence roasting itself."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
