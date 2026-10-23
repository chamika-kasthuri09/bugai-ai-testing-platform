# Contributing

Use branches such as `fix/BGA-0024-ignore-artifacts` and commits such as
`fix(BGA-0024): ignore local artifacts`. Keep changes focused on one acceptance
criterion and include verification evidence.

Use Node 24.20.x, npm 11.19.x, Python 3.12, and uv 0.12.5. Run `npm ci`,
`uv sync --frozen`, then `uv run python scripts/check.py` before review.

Edit tasks and phase metadata only in `BUGAI_BACKLOG.json`. Run
`python scripts/backlog.py --write` to regenerate the CSV and Markdown backlog.
The check command rejects drift, invalid task references, and dependency cycles.
Do not edit generated sections directly or mark tasks Done without evidence.

The repository maintainer should require CI and review on the default branch.
Local files cannot enforce remote branch protection.

See [LICENSE_STATUS.md](LICENSE_STATUS.md) before distributing the project.
