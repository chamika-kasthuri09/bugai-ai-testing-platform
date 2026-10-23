"""Foundation checks, plus optional browser smoke test with an owned fixture server."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import shutil
import subprocess
import sys
import threading

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    subprocess.run(args, cwd=ROOT, check=True, timeout=120)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--browser", action="store_true")
    args = parser.parse_args()
    npm = shutil.which("npm.cmd") or shutil.which("npm")
    if not npm:
        raise SystemExit("Install the Node version in .node-version first")
    run(sys.executable, "scripts/backlog.py", "--check")
    run(sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider")
    run(npm, "run", "check")
    run(npm, "run", "build")
    if args.browser:
        handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT / "tests/fixture"))
        with ThreadingHTTPServer(("127.0.0.1", 8080), handler) as server:
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                run(npm, "run", "smoke")
            finally:
                server.shutdown()
                thread.join()


if __name__ == "__main__":
    main()
