"""Build the help site: render screenshots, build HTML, check topics, optionally zip.

Usage:
    python tools/build.py              # site/ only
    python tools/build.py --zip        # also dist/opennest-help.zip for the app package
    python tools/build.py --serve      # render shots, then live-preview at http://127.0.0.1:8000
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DIST = ROOT / "dist"


def run(*command):
    subprocess.run([sys.executable, *command], cwd=ROOT, check=True)


def check_topics():
    """Every topic the app can ask for must resolve to a built page."""
    topics = json.loads((ROOT / "docs" / "topics.json").read_text(encoding="utf-8"))
    missing = []
    for topic, page in topics["topics"].items():
        path = page.split("#", 1)[0]
        if not (SITE / path).is_file():
            missing.append(f"{topic} -> {page}")
    if missing:
        sys.exit("topics.json points at missing pages:\n  " + "\n  ".join(missing))
    print(f"topics.json: {len(topics['topics'])} topics resolve")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip", action="store_true")
    parser.add_argument("--serve", action="store_true")
    args = parser.parse_args()

    run("tools/render_shots.py")
    if args.serve:
        run("-m", "mkdocs", "serve")
        return
    run("-m", "mkdocs", "build", "--strict", "--clean")
    check_topics()

    if args.zip:
        DIST.mkdir(exist_ok=True)
        archive = shutil.make_archive(str(DIST / "opennest-help"), "zip", SITE)
        print(archive)


if __name__ == "__main__":
    main()
