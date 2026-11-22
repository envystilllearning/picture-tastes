#!/usr/bin/env python3
"""Salin gambar entry ke direktori output."""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        sys.stderr.write("error: source image not found: %s\n" % source)
        sys.exit(1)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    os.chmod(target, 0o644)
    if os.path.getsize(target) != os.path.getsize(source):
        sys.stderr.write("error: copied file size differs from source\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
