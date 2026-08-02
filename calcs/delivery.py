"""Print the delivery chain for $100 allocated to Indonesia.

Collection capacity is absent. The chain is foundational identification
coverage multiplied by usable payment access conditional on identification,
then multiplied by payment completion. The script keeps denominator-mismatched
inputs separate and never uses a minimum operation.
"""

from __future__ import annotations

import json
from typing import Any


SCENARIOS = ("cautious", "central", "fast")
ALLOCATED_DOLLARS = 100.0
POPULATION_SHARE = None
FOUNDATIONAL_ID = None
PAYMENT_INSTRUMENT_GIVEN_ID = None
RAW_ACCOUNT_OWNERSHIP_ADULTS = 0.51755324070215
PAYMENT_COMPLETION: dict[str, float | None] = {
    "cautious": None,
    "central": None,
    "fast": None,
}
LIC_MEDIANS = {"id": None, "payment": None}
LMIC_MEDIANS = {"id": None, "payment": None}


def product(values: list[float | None]) -> float | None:
    if any(value is None for value in values):
        return None
    result = 1.0
    for value in values:
        result *= value  # type: ignore[operator]
    return result


def build_output() -> dict[str, Any]:
    rows: dict[str, Any] = {}
    for scenario in SCENARIOS:
        reachability_before_completion = product(
            [FOUNDATIONAL_ID, PAYMENT_INSTRUMENT_GIVEN_ID]
        )
        reachability = product(
            [reachability_before_completion, PAYMENT_COMPLETION[scenario]]
        )
        rows[scenario] = {
            "allocated_to_indonesia": ALLOCATED_DOLLARS,
            "population_share": POPULATION_SHARE,
            "foundational_id_coverage": FOUNDATIONAL_ID,
            "payment_instrument_given_id": PAYMENT_INSTRUMENT_GIVEN_ID,
            "raw_account_ownership_adults_15_plus": RAW_ACCOUNT_OWNERSHIP_ADULTS,
            "payment_completion": PAYMENT_COMPLETION[scenario],
            "reachability": reachability,
            "is_floor": False,
        }
    return {
        "scenarios": rows,
        "comparators": {"LIC": LIC_MEDIANS, "LMIC": LMIC_MEDIANS},
        "status": "pending denominator-compatible primary-source inputs",
        "source_ledger": "docs/parameters_and_sources.md",
    }


def main() -> None:
    print(json.dumps(build_output(), indent=2))


if __name__ == "__main__":
    main()
