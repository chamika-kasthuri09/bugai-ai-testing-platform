# Foundation and pilot decisions

Status: selected defaults for the local pilot. Runtime enforcement is incomplete
until the corresponding backlog tasks have verification evidence.

## Identity and deployment

The first release is a single-user, local-only tool. Listen on 127.0.0.1 and
publish Compose ports on 127.0.0.1. There is no public or multi-user deployment
mode. The foundation exposes only health, readiness, and API documentation.
Before adding mutation endpoints, enforce trusted Host and Origin checks and a
local session/CSRF token. Local binding alone is insufficient authorization for
browser-initiated mutations. Local projects belong to one installation identity.
Public deployment requires platform accounts, resource authorization, TLS,
secret management, and a separate release gate.

## Runner transport and persistence

Use a subprocess initially, launched by the trusted Python orchestrator with
`shell=False`, a fixed executable, strict JSON on stdin, and one JSON result on
stdout. Diagnostic output goes to stderr. Later, a Celery worker invokes the same
contract. No user-selected command, executable path, or environment is accepted.
The orchestrator checks exact approved test and requirement revisions, scope,
limits, and content digests immediately before launch. The runner validates the
same schema and scope independently. Cancellation terminates the process group
and browser, followed by bounded forced cleanup.

The runner has no database, Redis, provider, or object-store credentials. It
writes artifacts into one assigned temporary directory. The orchestrator checks
paths, size, MIME, and checksum; uploads artifacts; then persists results and
artifact metadata transactionally. Atomic completion follows durable evidence.
The browser runtime never joins the control-plane network. There is no runner
database connection. The existing smoke command is a fixed fixture check, not
the approved-spec execution service.

## Fixture and public-target network policies

The pilot supports only the bundled stateless fixture, with synthetic data and
no external subresources. In Compose it joins the dedicated `fixture` network
(`internal: true`), separate from the `control` network. The fixture network has
no DB, Redis, cloud services, or Internet route. The future job sandbox joins
only that fixture network and has no host mounts, host networking, Docker
socket, control-plane credentials, or API/broker connection. Only its assigned
artifact output is writable. Do not use a general private-IP allowlist.

The non-container foundation smoke command uses the fixed loopback fixture
origin `http://127.0.0.1:8080`. It is developer-only, accepts no target URL or
generated steps, and is not an isolation guarantee for hostile content.
The fixture network is an explicit test-harness exception, selected by trusted
deployment configuration, never by project input or an API payload.

Public target support is deferred. It must use a separate public-target profile:
private/loopback/link-local/multicast/metadata ranges remain denied, connection
destinations are pinned to validated DNS answers, and an independently enforced
egress boundary covers redirects, subresources, IPv6, and browser bypass paths.
Do not enable public targets until its adversarial network suite passes. Docker
Compose network separation alone is insufficient for a public-host allowlist.

## Limits and actions

Pilot hard ceilings: 1 concurrent job, 1 fixture page, 10 cases per run, 20 steps
per case, 5 seconds per step, 10 seconds per navigation, 60 seconds per case,
5 minutes per run, 100 requests and 10 MiB response bytes per case. Defaults may
be lowered by the user; hard ceilings may only be lowered by request data.
AI ceilings: 1 call plus at most 1 transient-error retry, 8,000 input tokens and
4,000 output tokens per generation. Abort if provider accounting cannot enforce
the configured budget. Artifacts: 5 MiB per file, 50 MiB per run, 7-day retention.
These are selected limits; tests must prove enforcement before pilot completion.

The versioned schema lists all initial full-MVP actions/assertions. The pilot
enables only fixture navigation, fill, click, submit, visibility/text/value
checks. Permit only known fixture element IDs and paths. A low-risk label or a
button name never proves an interaction safe. No real-site writes, deletion,
payments, messages, uploads, downloads, arbitrary scripts, or target credentials.
Revoke scope before new/pending work, cancel running work, and invalidate
approvals after executable, requirement, scope, or limit changes. Retry browser
work only from a fresh fixture state; do not replay partial side effects.

## API, schemas, and providers

Future product routes use `/api/v1`. Async submissions return 202 with a stable
job ID; exact revision conflicts use 409; quota failures use 429. Use immutable
requirement/test revisions, opaque IDs, UTC timestamps, and typed error envelopes
containing `code`, `message`, and `request_id`. New fields do not imply a route is
implemented. The only implemented routes are `/health` and `/ready`.

`contracts/test-case.schema.json`, `runner-request.schema.json`, and
`runner-result.schema.json` are authoritative 1.0 contracts. Reject unknown
fields and schema versions. Python and TypeScript must share fixture examples
and validate schema plus semantic policy before accepting jobs.

Assertion semantics are exact and case-sensitive for text, input value and
attribute value. Text uses the element's rendered inner text; value uses the
form control value; attribute uses the named attribute value without executing
it. Visibility/enabled use Playwright's native element state predicates. URL
assertions compare parsed, normalized absolute URLs after target policy checks.
Missing or ambiguous element mappings are selector errors. `check` sets the
checked state to true; clearing a field uses `fill` with an empty string. Step
IDs must be unique and ordered; each approved case contains at least one
assertion. These semantic rules require interpreter tests before execution is
implemented. Schema examples demonstrate structure and carry no real approval.

Use Gemini first for the pilot behind a provider-independent interface; OpenAI
follows with the same contract. Tests use local fixtures and need no paid calls.
Provider SDKs, model IDs, model-specific schema subsets, and credentials are
configured only when the adapter task is implemented. Artifact storage starts
with an orchestrator-owned local directory; S3/MinIO is deferred.
