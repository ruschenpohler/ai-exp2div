"""Transmission calculation.

This module will calculate the US and Indonesia chains for cautious, central,
and fast scenarios after the source ledger verifies the exposure definition.
Filters are scale factors applied to the flagged share under a uniformity
assumption; they are not probabilities.
"""


SCENARIOS = ("cautious", "central", "fast")


def main() -> None:
    raise SystemExit(
        "Transmission inputs are pending the required exposure embed check; "
        "see docs/parameters_and_sources.md."
    )


if __name__ == "__main__":
    main()
