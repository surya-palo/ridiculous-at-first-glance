#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second -- make.fun entry.

Writes one single-sentence startup pitch (at most 200 characters) to
/output/entry.txt. Python standard library only. Deterministic: the same
bytes on every run.
"""

import hashlib
import os

LINE = (
    "We rent retired racehorses to offices as emotional-support stallions: "
    "companies pay $400 a day because a 500-kilo horse in the lobby ends "
    "every pointless meeting in five minutes flat."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to /output/entry.txt")
    print("sha256:", hashlib.sha256(LINE.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
