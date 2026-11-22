import os
import shutil


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(script_dir, "entry.png")
    if not os.path.isfile(source):
        raise SystemExit("error: entry.png is missing next to main.py, nothing to copy")
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    os.chmod(target, 0o644)
    if os.path.getsize(target) != os.path.getsize(source):
        raise SystemExit("error: copied entry.png size differs from the source")


if __name__ == "__main__":
    main()
