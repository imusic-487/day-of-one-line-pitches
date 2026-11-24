"""One-line pitch for A Day of One-Line Pitches.

Copies line.txt (the entry, one sentence, 1-240 characters) to
/output/entry.txt byte for byte. MAKEFUN_OUTPUT_DIR, when set, stands
in for /output so the entry can be tested locally.

`python3 main.py --check` validates line.txt without writing anything.

Fails loudly if anything is off: the copy's size differs, its bytes
differ from line.txt, the text is not 1-240 characters, it is only
white space, or it spans more than one line.

Standard library only. No network, no randomness, no timestamps.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LINE_FILE = HERE / "line.txt"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def load_entry() -> tuple[bytes, str]:
    """Read line.txt and return its raw bytes and decoded text."""
    source = LINE_FILE.read_bytes()
    try:
        text = source.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise RuntimeError(f"line.txt is not valid UTF-8: {exc}") from exc

    if not 1 <= len(text) <= 240:
        raise RuntimeError(
            f"entry is {len(text)} characters, allowed 1-240"
        )
    if not text.strip():
        raise RuntimeError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise RuntimeError("entry must be a single line")
    return source, text


def verify_copy(source: bytes) -> None:
    """Check the written entry matches line.txt byte for byte."""
    written = OUTPUT_FILE.read_bytes()
    if len(written) != len(source):
        raise RuntimeError(
            f"copy size differs: wrote {len(written)} bytes, "
            f"source is {len(source)} bytes"
        )
    if written != source:
        offset = next(
            i for i, (a, b) in enumerate(zip(written, source)) if a != b
        )
        raise RuntimeError(
            f"copy bytes differ from line.txt: first difference at "
            f"byte {offset} (wrote 0x{written[offset]:02x}, "
            f"source is 0x{source[offset]:02x})"
        )


def main(argv: list[str]) -> None:
    check_only = "--check" in argv
    source, text = load_entry()

    if check_only:
        print(f"entry OK ({len(source)} bytes, {len(text)} characters)")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_bytes(source)
    verify_copy(source)

    print(f"wrote {OUTPUT_FILE} ({len(source)} bytes, {len(text)} characters)")


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
