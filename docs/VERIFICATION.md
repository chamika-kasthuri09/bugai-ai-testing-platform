# Foundation verification — 23 October 2026

Verified in this workspace with Python 3.12.10, uv 0.12.5, Node 24.20.0 and
npm 11.19.0:

- Locked Python dependencies installed with `uv sync --frozen`.
- Node dependencies resolved into `package-lock.json`; frontend production build
  and TypeScript checks for frontend and runner passed.
- Foundation API probes, unsupported execution route rejection, schema examples,
  invalid spec/limit/artifact/result cases, and backlog consistency checks passed.
- `python scripts/check.py --browser` passed against the controlled fixture:
  Chromium launched, empty-email feedback matched, a screenshot was captured,
  the browser closed and the owned fixture server stopped.
- `docker compose config --quiet` passed.

The browser check needed execution outside the host tool sandbox because it
blocked a required child process with EPERM. This is a development verification
detail, not a change to the application's runner policy.

Docker image builds and container startup remain unverified: Docker Desktop's
Linux engine is not running. The remote GitHub Actions workflow and branch
protection have not been exercised or configured from this workspace. The
first foundation pilot package remains In progress until clean-checkout and
container/CI evidence exists.

This evidence covers the foundation. Project persistence, discovery, AI adapters,
approval, generated-spec execution, artifact APIs and the complete pilot workflow
remain unimplemented. The benchmark is a seed and does not meet the release
dataset size yet. Public-target isolation and production security are not claimed
verified. A rights-holder license decision still gates public distribution.
