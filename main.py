"""The 3 AM Excuse — a hardware wallet that will not sign at 3 AM.

Writes one line (under 200 characters) to /output/entry.txt.
Pure standard library, deterministic: the same line every run.
"""

import os

LINE = "I don't sleep-sign at 3 AM — my keys are dreaming in twelve words and none of them is yes. Try again at sunrise."


def main() -> None:
    # The gate allows 1 to 200 characters, not only whitespace.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
