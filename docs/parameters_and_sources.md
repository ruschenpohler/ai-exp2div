# Parameters and Sources

This ledger is the source of truth for every number used by the calculation scripts or memo. A row is incomplete until it has a value, denominator, opened source, and one of the three permitted statuses: `well-sourced`, `working figure`, or `unanchored`.

## Scenario definitions

| Scenario | Task filter | Adoption filter | Payment completion |
|---|---|---|---|
| cautious | lower value per the verified task-tier source, if the embed check retains this filter | current observed rate, no projection | lowest verified mixed-program completion rate |
| central | E2-based central value, if the embed check retains this filter | current anchor plus same-income-group historical 10-year increase, capped at 0.8 | main estimate from the mixed program set |
| fast | upper value per the verified task-tier source, if the embed check retains this filter | current anchor plus historical 75th-percentile increase, capped at 0.8 | highest verified mixed-program completion rate |

## Embed check

**Decision: NOT EMBEDDED.** Cazzaniga et al. define exposure from occupation-level overlap between AI applications and human abilities, then apply a separate complementarity adjustment. Their high/low exposure threshold is the median of the relevant indicators; the definition does not condition on the share of tasks within an occupation that is exposed or performable. The task filter is therefore retained in Table 1 and in `calcs/transmission.py`.

Verbatim methodology quote, pages 6-7 (PDF pages 8-9):

> "Based on these two criteria, occupations can be categorized into three groups: 'high exposure, high complementarity'; 'high exposure, low complementarity'; and 'low exposure' (see Box 1). Although the indicators (and the thresholds adopted to define what is high and low, represented by their median values) are relative measures, this categorization highlights the overarching differences across occupations in terms of their AI exposure and complementarity potential."

The quote is 45 words, comes from the methodology section, and includes the threshold definition. The source describes AIOE as overlap between AI applications and human abilities and separately describes the complementarity adjustment in Box 1; it does not provide a within-occupation task-share condition.

## Ledger

| ID | Parameter | Value | Scenario values | Source opened | Denominator | Status | Notes |
|---|---|---:|---|---|---|---|---|
| EXP-EMBED | Exposure definition and threshold quote | not embedded | n/a | Cazzaniga et al. (2024), IMF SDN/2024/001, pp. 6-7 | Occupation-level exposure indicators; country-group employment shares use working-age-population-weighted averages | well-sourced | The methodology quote and decision are recorded above. Retain the task filter. |
| EXP-US | Advanced-economy / US exposure anchor | 60% | 60% / 60% / 60% | Cazzaniga et al. (2024), IMF SDN/2024/001, pp. 2 and 8 | Employment; advanced-economy group figure is working-age-population-weighted; US selected-country figure is employment | well-sourced | The note reports about 60% for advanced economies and almost 60% for US employment. |
| EXP-EM | Emerging-market exposure anchor used for Indonesia | 40% | 40% / 40% / 40% | Cazzaniga et al. (2024), IMF SDN/2024/001, pp. 2 and 8 | Employment; emerging-market group figure is working-age-population-weighted | well-sourced | Use the EM aggregate as instructed; do not describe it as Indonesia-specific. |
| EXP-LIC | Low-income-country exposure gradient | 26% | 26% / 26% / 26% | Cazzaniga et al. (2024), IMF SDN/2024/001, p. 2 | Employment; low-income-country group figure is working-age-population-weighted | well-sourced | Supports the AE/EM/LIC gradient sentence. |
| TASK-CENTRAL | E2 task filter | pending | pending / 0.50 / pending | Eloundou et al. (2023), arXiv:2303.10130 | Share of tasks exposed within the relevant occupation definition | unanchored | The embed check retains this parameter. Verify the lower and upper tier-consistent values before calculation. |
