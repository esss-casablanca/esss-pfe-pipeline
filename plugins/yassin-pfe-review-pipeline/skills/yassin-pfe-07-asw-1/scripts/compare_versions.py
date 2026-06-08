#!/usr/bin/env python3
"""
Compare original and revised text for Yassin Scholarly Authorship Revision.

Outputs:
- word and sentence counts;
- unified diff;
- required-marker extraction;
- simple added/removed line summary.

Usage:
    python compare_versions.py original.txt revised.txt > comparison.md
"""
from __future__ import annotations

import difflib
import re
import sys
from pathlib import Path

MARKERS = [
    "[DATA REQUIRED]",
    "[REFERENCE REQUIRED]",
    "[METHOD DETAIL REQUIRED]",
    "[ETHICS DETAIL REQUIRED]",
    "[LOCAL CONTEXT REQUIRED]",
    "[AUTHOR TO VERIFY]",
    "[REPORTING ITEM REQUIRED]",
]

ABBREVIATIONS = {
    "Dr.", "Pr.", "Prof.", "Mr.", "Mrs.", "Ms.", "e.g.", "i.e.", "cf.", "Fig.", "Table.",
}


def read_text(path: str) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return p.read_text(encoding="utf-8")


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\wÀ-ÿ'-]+\b", text, flags=re.UNICODE))


def sentence_count(text: str) -> int:
    # Conservative sentence splitter adequate for summaries, not formal NLP.
    protected = text
    placeholders = {}
    for i, abbr in enumerate(ABBREVIATIONS):
        token = f"__ABBR{i}__"
        placeholders[token] = abbr
        protected = protected.replace(abbr, token)
    parts = re.split(r"(?<=[.!?])\s+", protected.strip())
    return len([p for p in parts if p.strip()])


def extract_markers(text: str) -> dict[str, int]:
    return {m: text.count(m) for m in MARKERS if text.count(m) > 0}


def diff_text(a: str, b: str) -> str:
    a_lines = a.splitlines()
    b_lines = b.splitlines()
    return "\n".join(difflib.unified_diff(a_lines, b_lines, fromfile="original", tofile="revised", lineterm=""))


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python compare_versions.py original.txt revised.txt", file=sys.stderr)
        return 2

    original = read_text(sys.argv[1])
    revised = read_text(sys.argv[2])

    original_words = word_count(original)
    revised_words = word_count(revised)
    original_sentences = sentence_count(original)
    revised_sentences = sentence_count(revised)
    markers = extract_markers(revised)

    print("# Revision Comparison Report")
    print()
    print("## Summary")
    print()
    print(f"- Original word count: {original_words}")
    print(f"- Revised word count: {revised_words}")
    print(f"- Word-count change: {revised_words - original_words}")
    print(f"- Original sentence count: {original_sentences}")
    print(f"- Revised sentence count: {revised_sentences}")
    print()
    print("## Required markers in revised text")
    print()
    if markers:
        for marker, count in markers.items():
            print(f"- {marker}: {count}")
    else:
        print("- None detected")
    print()
    print("## Unified diff")
    print()
    print("```diff")
    print(diff_text(original, revised))
    print("```")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
