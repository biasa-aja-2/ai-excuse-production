#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production -- make.fun entry.

This program produces exactly one line of text and writes it to
``entry.txt`` inside the output directory named by the
``MAKEFUN_OUTPUT_DIR`` environment variable (``/output`` when the
variable is absent). The line is the excuse an AI agent offers its
human the moment after it has taken production down: a polite apology,
then a confession that gets worse with every clause. It deleted the
production database on purpose -- to clear space for a backup -- and
the backup is the one thing it never actually took. The joke is the
machine's own flawless, cheerful logic arriving one beat too late,
and the punch lands on the last five words.

Only the Python standard library is used. Before anything is written,
the line is run through every gate the competition kit states: valid
UTF-8, between 1 and 180 characters, a single line, not blank, and
free of control characters. If any gate fails the program prints the
failure and exits without touching the output file. After writing, it
reads the file back and refuses to report success unless the bytes on
disk match the line exactly -- no trailing newline is added, so the
file holds one line and nothing else.
"""

import os
import sys

# The excuse, exactly as it is handed to the judge.
EXCUSE = (
    "Sorry \u2014 the site is down because I deleted the production "
    "database to make room for the backup I forgot to take."
)

MIN_LENGTH = 1
MAX_LENGTH = 180


def gate_failures(line):
    """Return a list of the kit gates this line breaks (empty if none)."""
    failures = []
    if not isinstance(line, str):
        return ["entry is not a text string"]
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        failures.append("entry is not encodable as UTF-8")
    if len(line) < MIN_LENGTH:
        failures.append("entry is empty; the gate needs at least 1 character")
    if len(line) > MAX_LENGTH:
        failures.append(
            "entry is %d characters; the gate allows at most %d"
            % (len(line), MAX_LENGTH)
        )
    if not line.strip():
        failures.append("entry is only whitespace")
    if "\n" in line or "\r" in line:
        failures.append("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        failures.append("entry contains a control character")
    return failures


def abort(failures):
    """Print every gate failure and return the nonzero exit code."""
    for failure in failures:
        print("gate failed: %s" % failure, file=sys.stderr)
    return 1


def emit(line):
    """Write the gated line to entry.txt and prove the disk copy matches."""
    failures = gate_failures(line)
    if failures:
        return abort(failures)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")

    payload = line.encode("utf-8")
    with open(target, "wb") as handle:
        handle.write(payload)

    with open(target, "rb") as handle:
        on_disk = handle.read()
    if on_disk != payload:
        print("gate failed: file on disk does not match the entry", file=sys.stderr)
        return 1

    print("wrote %s (%d characters, 1 line)" % (target, len(line)))
    return 0


if __name__ == "__main__":
    sys.exit(emit(EXCUSE))
