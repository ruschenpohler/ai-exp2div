# Parameters and Sources

This ledger is the source of truth for every number used by the calculation scripts or memo. A row is incomplete until it has a value, denominator, opened source, and one of the three permitted statuses: `well-sourced`, `working figure`, or `unanchored`.

## Scenario definitions

| Scenario | Task filter | Adoption filter | Payment completion |
|---|---|---|---|
| cautious | lower value per the verified task-tier source, if the embed check retains this filter | current observed rate, no projection | lowest verified mixed-program completion rate |
| central | E2-based central value, if the embed check retains this filter | current anchor plus same-income-group historical 10-year increase, capped at 0.8 | main estimate from the mixed program set |
| fast | upper value per the verified task-tier source, if the embed check retains this filter | current anchor plus historical 75th-percentile increase, capped at 0.8 | highest verified mixed-program completion rate |

## Ledger

No parameter is populated yet. The exposure embed check must be completed before the Table 1 schema and transmission chain are finalized.

| ID | Parameter | Value | Scenario values | Source opened | Denominator | Status | Notes |
|---|---|---:|---|---|---|---|---|
| EXP-EMBED | Exposure definition and threshold quote | pending | n/a | Cazzaniga et al. (2024), IMF SDN | pending | unanchored | Required methodology quote must be at least 20 words and include the threshold definition. |
