import copy
import json
from pathlib import Path

import pytest

from scripts.backlog import generated_views, validate

ROOT = Path(__file__).resolve().parents[1]


def source():
    return json.loads((ROOT / "BUGAI_BACKLOG.json").read_text(encoding="utf-8"))


def test_generated_backlog_is_current():
    data = source()
    validate(data)
    plan = (ROOT / "BUGAI_IMPLEMENTATION_PLAN.md").read_text(encoding="utf-8")
    for path, expected in generated_views(data, plan).items():
        assert path.read_text(encoding="utf-8") == expected


@pytest.mark.parametrize("bad_dependency", ["MISSING-01", "PILOT-01"])
def test_reject_missing_and_cyclic_dependencies(bad_dependency):
    data = copy.deepcopy(source())
    data["pilot"][0]["Depends on tasks"] = [bad_dependency]
    with pytest.raises(ValueError):
        validate(data)


def test_cannot_complete_task_without_evidence():
    data = source()
    data["pilot"][0].update(Status="Done", **{"Evidence link": ""})
    with pytest.raises(ValueError, match="completion evidence"):
        validate(data)
