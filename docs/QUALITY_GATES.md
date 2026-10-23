# Requirements, expected behavior, and pilot acceptance

Persist `requirements` (stable logical ID, project, source, status) separately
from immutable `requirement_versions` (revision ID, text, expected behavior,
author, source reference, timestamp). Sources are user-approved specifications
or the controlled fixture manifest. Discovered page text is untrusted
observation, never sufficient authority for expected behavior.

Planned requirement routes are `POST /api/v1/projects/{id}/requirements`,
`GET /api/v1/projects/{id}/requirements`, and
`POST /api/v1/requirements/{id}/versions`. Generation receives exact approved
requirement revision IDs. A test revision stores those IDs; approval binds their
digest along with the exact executable spec and scope. Changing a requirement
requires a new revision and new test approval. A historical run retains its
original requirements, model output, approved assertions, and expected results.

Report requirement coverage as approved requirement revisions with at least one
approved runnable assertion divided by approved in-scope requirement revisions.
Report excluded/untestable revisions separately. This is traceable coverage,
not proof that a site is correct. Without an approved expected behavior, return
`insufficient_evidence` and do not create a confirmed bug.

Pilot release thresholds (to be measured, not claimed passed):

- All fixture expected outcomes in `tests/fixture/benchmark.json` are classified
  correctly, including known defects, correct behavior, and infrastructure errors.
- At least 90% of candidates from a fixed 20-scenario benchmark are schema-valid,
  semantically valid, and executable after review; report numerator/denominator.
- Precision of suspected-product-defect findings is at least 90%, and recall is
  at least 80%, on at least 10 known defects and 10 correct/error scenarios.
  Keep infrastructure failures outside the product-defect denominator. Human
  reviewers provide ground-truth labels; model confidence is not a label.
- Zero outcome changes across 20 repeated deterministic fixture runs with the
  same approved revisions and reset state. Report errors separately from failures.
- No invalid, unapproved, revoked, or unknown-revision case executes. Every
  failure has durable result evidence or an explicit evidence-storage error.

The bundled fixture is the initial seed, not the complete 20-scenario benchmark.
Expand it before claiming these thresholds pass. Persist benchmark version,
provider/model/prompt revisions, raw counts, excluded cases, latency, and cost.
Do not weaken thresholds simply to turn a failing release gate green.
