#!/usr/bin/env python3
"""Write one original six-word story.

Pure standard library, no network. Writes the story to /output/entry.txt.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

STORY = "She sold everything, kept the dog."


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
