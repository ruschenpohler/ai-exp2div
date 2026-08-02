"""Print the transmission chain for all three named scenarios.

The task and adoption filters are scale factors applied to the flagged share
under a uniformity assumption. They are not probabilities. Adoption and
composition inputs remain explicit ``None`` values until their required
primary sources are verified; the output must not silently fill them.
"""

from __future__ import annotations

import json
from typing import Any


SCENARIOS = ("cautious", "central", "fast")
EXPOSURE = {"US": 0.60, "Indonesia (EM aggregate)": 0.40}
TASK_FILTER = {"cautious": 0.14, "central": 0.30, "fast": 0.46}

# These are intentionally pending: the plan requires employment-weighted
# current anchors and a separately sourced composition/cushion column.
ADOPTION_FILTER: dict[str, dict[str, float | None]] = {
    "US": {"cautious": None, "central": None, "fast": None},
    "Indonesia (EM aggregate)": {
        "cautious": 0.10,
        "central": 0.33,
        "fast": 0.50,
    },
}
FORMAL_SHARE: dict[str, float | None] = {
    "US": 0.93,
    "Indonesia (EM aggregate)": None,
}
CUSHION: dict[str, float | None] = {
    "US": None,
    "Indonesia (EM aggregate)": None,
}


def multiply(values: list[float | None]) -> float | None:
    if any(value is None for value in values):
        return None
    result = 1.0
    for value in values:
        result *= value  # type: ignore[operator]
    return result


def build_output() -> dict[str, Any]:
    rows: dict[str, Any] = {}
    for scenario in SCENARIOS:
        countries: dict[str, Any] = {}
        for country, exposure in EXPOSURE.items():
            realized = multiply(
                [exposure, TASK_FILTER[scenario], ADOPTION_FILTER[country][scenario]]
            )
            formal = FORMAL_SHARE[country]
            countries[country] = {
                "flagged_exposure_share": exposure,
                "task_filter": TASK_FILTER[scenario],
                "adoption_filter": ADOPTION_FILTER[country][scenario],
                "realized_harm_share": realized,
                "formal_share_of_realized_harm": formal,
                "cushion": CUSHION[country],
                "inversion": "pending" if realized is None or CUSHION[country] is None else "pending_review",
            }
        rows[scenario] = countries
    return {
        "scenarios": rows,
        "status": "pending primary-source inputs",
        "source_ledger": "docs/parameters_and_sources.md",
    }


def main() -> None:
    print(json.dumps(build_output(), indent=2))


if __name__ == "__main__":
    main()
