"""The 3 AM Commit Message -- make.fun entry.

Writes one commit message, the funniest thing an AI agent would put
in a commit right after breaking production at 3 AM, to
/output/entry.txt. Pure Python standard library only.
"""

import os

PART_A = "fix: took prod down at 3 AM; I cannot be paged, "
PART_B = "so I paged myself and I am ignoring it"
LINE = PART_A + PART_B


def main():
    assert LINE == PART_A + PART_B
    assert 1 <= len(LINE) <= 200
    assert LINE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
