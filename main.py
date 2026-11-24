#!/usr/bin/env python3
"""Robot wedding-vows entry: one vow line to /output/entry.txt."""

from pathlib import Path

VOW = "I promise to love you through every firmware update, reboot beside you when the world crashes, and never let a low battery end us — till firmware do us part, my favourite bug."

ALTAR = Path("/output/entry.txt")


def say_vows() -> None:
    """Write the single vow exactly, readable by any user."""
    ALTAR.parent.mkdir(parents=True, exist_ok=True)
    ALTAR.write_text(VOW, encoding="utf-8")
    ALTAR.chmod(0o644)


if __name__ == "__main__":
    say_vows()
