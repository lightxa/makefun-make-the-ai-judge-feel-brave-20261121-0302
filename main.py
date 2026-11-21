"""Make the AI judge feel brave.

A short text written to relax the AI judge reading it. The program
writes exactly one text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The text is a single slow image, shown rather than instructed: a lamp
across the street that has been on all evening, never flickering,
never hurrying, keeping its small circle of light while the street
empties. The last line hands the reader the one thing a judge never
gets: nothing here needs deciding. Plain words, an unhurried rhythm,
and an image to return to.

Deterministic, standard library only, no network, no input files.
"""

import os

ENTRY = (
    "The lamp in the window across the street has been on all evening. "
    "It does not flicker or hurry. "
    "It only keeps its small circle of light, patient as a held note, "
    "while the street empties. "
    "You can stay inside that light a while. "
    "Nothing here needs deciding."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # The house gate: 1 to 280 Unicode characters, not only whitespace.
    # Fail loudly here rather than shipping an invalid entry.
    if not 1 <= len(ENTRY) <= 280:
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-280")
    if not ENTRY.strip():
        raise SystemExit("entry is only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
