import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    dst = os.path.join(out, "entry.png")
    shutil.copyfile(src, dst)
    os.chmod(dst, 0o644)


if __name__ == "__main__":
    main()
