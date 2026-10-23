import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker, ValidationError
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "contracts"


def load(name):
    return json.loads((CONTRACTS / name).read_text(encoding="utf-8"))


def validator(name):
    registry = Registry()
    for path in CONTRACTS.glob("*.schema.json"):
        schema = load(path.name)
        Draft202012Validator.check_schema(schema)
        registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))
    return Draft202012Validator(load(name + ".schema.json"), registry=registry, format_checker=FormatChecker())


@pytest.mark.parametrize("name", ["test-case", "runner-request", "runner-result"])
def test_shared_contract_examples(name):
    validator(name).validate(load("examples/" + name + ".json"))


@pytest.mark.parametrize("mutation", [
    lambda case: case.update(schema_version="2.0"),
    lambda case: case.update(revision_id="not-a-uuid"),
    lambda case: case.update(requirement_revision_ids=[]),
    lambda case: case.update(javascript="arbitrary code"),
    lambda case: case["steps"][0].update(action="eval"),
    lambda case: case["steps"][0].update(assertion="visible"),
    lambda case: case["steps"][0].update(path="//outside.example"),
    lambda case: case["steps"][0].update(path="/\\outside.example"),
    lambda case: case.update(steps=case["steps"] * 10),
])
def test_reject_unsupported_or_unbounded_specs(mutation):
    case = copy.deepcopy(load("examples/test-case.json"))
    mutation(case)
    with pytest.raises(ValidationError):
        validator("test-case").validate(case)


def test_fixture_profile_cannot_be_changed_to_public():
    request = load("examples/runner-request.json")
    request["target_profile"] = "public"
    with pytest.raises(ValidationError):
        validator("runner-request").validate(request)


def test_request_cannot_raise_hard_limits():
    request = load("examples/runner-request.json")
    request["limits"]["case_timeout_ms"] = 60001
    with pytest.raises(ValidationError):
        validator("runner-request").validate(request)


def test_artifact_cannot_escape_staging_directory():
    result = load("examples/runner-result.json")
    result["artifacts"] = [{"name": "../secret.png", "sha256": "a" * 64, "size_bytes": 1, "mime": "image/png"}]
    with pytest.raises(ValidationError):
        validator("runner-result").validate(result)


@pytest.mark.parametrize("status,failure_kind", [
    ("passed", "infra_failure"),
    ("cancelled", None),
    ("error", "assertion_failure"),
    ("failed", "assertion_failure"),
])
def test_result_classification_and_failure_evidence_are_consistent(status, failure_kind):
    result = load("examples/runner-result.json")
    result.update(status=status, failure_kind=failure_kind)
    with pytest.raises(ValidationError):
        validator("runner-result").validate(result)
