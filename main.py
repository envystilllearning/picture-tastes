#!/usr/bin/env python3
"""Copy the bundled picture-tastes entry image to the output directory."""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")

    if not os.path.isfile(source):
        raise SystemExit(f"error: source image not found: {source}")

    target_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")

    shutil.copyfile(source, target)
    os.chmod(target, 0o644)

    if os.path.getsize(target) != os.path.getsize(source):
        raise SystemExit(
            "error: copied image size does not match the source image"
        )


if __name__ == "__main__":
    main()
