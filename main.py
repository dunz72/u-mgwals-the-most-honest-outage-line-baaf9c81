#!/usr/bin/env python3
"""Copy the pre-rendered outage line to the grader output directory.

Stdlib only: the grader's pinned Python image ships no third-party
packages, so this program imports nothing beyond the standard library.
It copies entry.txt (written beside this file) byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.txt, validating the gate first: UTF-8 text,
a single line, 1-160 characters, and verifying the copy with SHA-256.
"""
import hashlib
import os
import sys
from pathlib import Path

MAX_CHARS = 160


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.txt"
    data = source.read_bytes()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return fail("entry.txt is not valid UTF-8")
    if not 1 <= len(text) <= MAX_CHARS:
        return fail("entry.txt must be 1-%d characters, got %d" % (MAX_CHARS, len(text)))
    stripped = text.strip()
    if stripped == "":
        return fail("entry.txt must not be only whitespace")
    if "\n" in stripped or "\r" in stripped:
        return fail("entry.txt must be a single line")
    if any(ord(ch) < 32 and ch not in ("\t",) for ch in text):
        return fail("entry.txt must not contain control characters")
    digest = hashlib.sha256(data).hexdigest()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(data)
    check = hashlib.sha256(target.read_bytes()).hexdigest()
    if check != digest:
        return fail("sha256 mismatch after copy")
    print("wrote %s (%d bytes, sha256 %s)" % (target, len(data), digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
