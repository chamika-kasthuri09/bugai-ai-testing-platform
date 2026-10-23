# BugAI 🐞🤖

### AI-Powered Automated Software Testing & Bug Reporting Platform

**BugAI** is an AI-powered software testing platform designed to simplify and accelerate web application testing.

By combining **Large Language Models (Google Gemini / OpenAI)** with **Playwright browser automation**, BugAI aims to automatically generate test cases, execute browser-based tests, identify potential software defects, and produce detailed bug reports with execution evidence.

> 🚧 **Project Status:** Local foundation; product features planned
> **Project Type:** Full-Stack AI + QA Automation
> **Architecture:** Modular Monolith with Asynchronous Test Execution

---

## 🎯 Project Objectives

- Automate test case generation using AI.
- Reduce repetitive manual software testing.
- Discover testable website elements automatically.
- Execute functional, negative, boundary, and validation tests.
- Detect potential software defects.
- Generate detailed bug reports with screenshots and traces.
- Provide an intuitive dashboard for test management and reporting.
- Support both Gemini and OpenAI as interchangeable AI providers.

## ✨ Planned Features

### 🔍 1. Website Discovery
Analyze authorized web applications to identify testable components, including buttons, links, forms, input fields, and navigation elements.

### 🤖 2. AI-Powered Test Case Generation
Generate structured test scenarios based on discovered website elements and user-provided requirements.

Supported scenario categories will include functional, positive, negative, boundary, and validation tests.

### 🧪 3. Automated Test Execution
Execute approved test cases using Playwright browser automation, including navigation, element interaction, input validation, and assertions.

### 🐛 4. Intelligent Bug Analysis
Analyze failed test executions using AI to generate suspected bug descriptions, reproduction steps, and possible fixes.

AI-generated bug reports will require human verification.

### 📸 5. Test Evidence Collection
Collect execution results, screenshots, browser traces, and relevant error information to support debugging.

### 📊 6. Test Dashboard
Manage testing projects, review generated test cases, monitor execution results, and view testing history.

### 📄 7. Automated Reporting
Generate downloadable reports summarizing test results, suspected defects, and execution evidence.

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | React, TypeScript, Tailwind CSS |
| Backend | Python, FastAPI |
| AI Integration | Google Gemini API, OpenAI API |
| Browser Automation | Playwright, TypeScript |
| Database | PostgreSQL |
| Task Queue | Celery, Redis |
| Containerization | Docker, Docker Compose |
| Artifact Storage | Local Storage / MinIO / S3 |
| CI/CD | GitHub Actions |
| API Documentation | FastAPI Swagger UI |

## 🏗️ System Architecture

BugAI is designed using a modular architecture that separates the frontend, backend, AI integration, and browser automation components.

**Planned workflow:**

1. A user registers an authorized website for testing.
2. Playwright discovers web pages and interactive elements.
3. Gemini or OpenAI generates structured test scenarios.
4. The user reviews and approves generated test cases.
5. Approved test cases are executed using Playwright.
6. The execution system captures results and evidence.
7. AI analyzes failed tests to identify suspected defects.
8. The dashboard displays results and downloadable reports.

AI-generated test specifications will be validated before execution. BugAI will not execute arbitrary AI-generated scripts.

## Repository structure

- `frontend/`: React + TypeScript foundation page.
- `backend/`: FastAPI health and readiness endpoints.
- `runner/`: fixed Playwright fixture smoke check.
- `tests/fixture/`: stateless controlled demo and benchmark seed.
- `contracts/`: versioned test and runner JSON schemas with examples.
- `scripts/`: verification and backlog generation.
- `docs/`: architecture decisions and measurable quality gates.
- `infra/`: local deployment boundaries; root Compose configuration.

## Getting started

Use Python 3.12, uv 0.12.5, Node 24.20.x and npm 11.19.x. The foundation needs no AI keys.

```bash
npm ci
uv sync --frozen
uv run python scripts/check.py
```

Start the frontend and API in separate terminals:

```bash
npm run dev
uv run uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

Frontend: http://127.0.0.1:5173. API documentation: http://127.0.0.1:8000/docs.
Only `/health` and `/ready` are implemented. The frontend is a foundation page;
it does not yet manage projects or runs.

Install Chromium once, then run the optional browser check. The check owns and
shuts down its fixture server on port 8080; that port must be free.

```bash
npx playwright install chromium
uv run python scripts/check.py --browser
```

For Docker, copy `.env.example` to `.env` and start Docker Desktop in Linux
container mode:

```bash
docker compose up --build
```

The frontend, API and fixture bind to loopback ports 5173, 8000 and 8080.
`docker compose --profile data up --build` also starts PostgreSQL and Redis;
they are not connected to application persistence yet. Stop services with
`docker compose down`. No Celery worker or public-target runner is implemented.
Docker engine availability is required to verify image startup.

## Planning and maintenance

The first release is the ten-package local fixture pilot in
[the implementation plan](BUGAI_IMPLEMENTATION_PLAN.md#12-first-release-pilot-and-capacity-plan).
It has provisional effort estimates and explicit dependencies, without a calendar
promise. The larger full-MVP backlog follows the pilot. CI and the fixture start
in the foundation. Platform accounts, public targets, queues and a second AI
provider require later release gates.

Edit `BUGAI_BACKLOG.json` as the source of truth, then regenerate its views:

```bash
python scripts/backlog.py --write
python scripts/backlog.py --check
```

The checker validates references, dependency cycles, completion evidence and view
consistency. CSV and the plan backlog are generated; do not edit them directly.
See [architecture decisions](docs/ARCHITECTURE_DECISIONS.md),
[quality gates](docs/QUALITY_GATES.md) and [contribution instructions](CONTRIBUTING.md).

## 🧪 Supported Testing Categories

| Testing Category | MVP Scope |
|---|---|
| Functional Testing | Planned |
| UI Interaction Testing | Planned |
| Form Validation Testing | Planned |
| Negative Testing | Planned |
| Boundary Testing | Planned |
| Navigation Testing | Planned |
| Authentication Testing | Future |
| Accessibility Testing | Future |
| Visual Regression Testing | Future |
| Performance Testing | Future |

## Development roadmap

1. Reproducible foundation, controlled fixture, contracts and CI.
2. Local project, discovery, one AI adapter and exact-revision approval.
3. Isolated fixture execution, durable evidence and result display.
4. Benchmark, safety and clean-checkout acceptance gates.
5. Full-MVP capabilities after pilot validation and capacity re-estimation.

## 🔐 Security

BugAI is designed exclusively for authorized application testing.

Planned security controls include:

- Restricting tests to authorized destinations.
- Blocking internal, private, and cloud metadata destinations for future public targets; the bundled fixture has a dedicated isolated test-network policy.
- Validating redirects and resolved IP addresses.
- Executing browser tests in isolated, resource-limited environments.
- Protecting credentials and API keys.
- Validating AI-generated test specifications.
- Requiring approval for potentially destructive operations.
- Applying execution limits and artifact retention policies.

## 🔮 Future Enhancements

- Cross-browser testing with Chromium, Firefox, and WebKit.
- Authentication-aware testing.
- Visual regression testing.
- Accessibility testing.
- Performance analysis.
- Scheduled and recurring test execution.
- GitHub Issues and Jira integration.
- CI/CD-triggered regression testing.
- Flaky test detection.
- Team collaboration and role-based access control.
- Local AI model support.

## 🤝 Contributing

Contributions and suggestions will be welcome as the project evolves.

To contribute:

1. Open an issue describing the improvement or bug.
2. Create a feature branch.
3. Implement the proposed change and relevant tests.
4. Submit a pull request for review.

See CONTRIBUTING.md for setup, verification and generated-backlog rules.

## 📄 License

No license has been granted. See [LICENSE_STATUS.md](LICENSE_STATUS.md). Public distribution requires a rights-holder decision, the full LICENSE text and a dependency notice review.

---

**BugAI 🐞🤖 — Generate intelligently. Test deterministically. Report with evidence.**
