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
| TASK-FILTER | Task-share scale factor | 0.14 | 0.14 / 0.50 / 0.55 | Eloundou et al. (2023), arXiv:2303.10130, sections 3.3 and 4.1 | Share of tasks exposed within an occupation; source uses core-task double weighting | working figure | Cautious uses the paper's lower-bound alpha mean (human annotations); central follows the plan's locked 50% E2 threshold; fast uses the paper's upper-bound zeta mean from GPT-4 annotations. These are scale factors, not probabilities. The central and fast substitutions are logged pending author review. |
| ADOPT-US-CURRENT | United States current artificial-intelligence use | pending | pending / pending / pending | United States Census Bureau, Business Trends and Outlook Survey data page and AI-use article | Businesses in the survey; the verified 2023 public figure is a business-count rate, not employment-weighted | unanchored | The survey asks about current use and provides employment-size tabulations, but the accessible published figure is 3.8% of businesses in 2023. Do not use it as an employment share. A latest-wave employment-weighted calculation is still required. |
| ADOPT-ID-CURRENT | Indonesia current artificial-intelligence use | none found | unanchored / unanchored / unanchored | World Bank Enterprise Surveys and World Bank technology-module search | Enterprise or firm survey denominator, if a source is found | unanchored | No usable Indonesia artificial-intelligence-specific current anchor has been verified. Keep the adoption filter unanchored and foreground that limitation in the memo. |
| DIFFUSION-CENTRAL | Same-income-group historical ten-year diffusion increase | pending | pending / pending / pending | Comin and Hobijn (2010), historical technology diffusion data | Technology adoption share over a ten-year interval | unanchored | The required dataset or income-group breakdown has not yet been opened. Do not apply an advanced-economy increase to Indonesia. |

## Adoption-proxy search outcome

The author requested this proxy search during implementation. The search followed the agreed priority order.

| Country | Search order completed | Outcome | Decision |
|---|---|---|---|
| United States | Latest Business Trends and Outlook Survey current-use rate by employment-size class; Census employment shares from Statistics of United States Businesses, Business Dynamics Statistics, or County Business Patterns; other employment-weighted firm survey | The official survey page confirms current-use questions, expanded employment-size tabulations, and continuing releases. The accessible published rate is 3.8% of businesses from 2023, without the matched latest-wave size-class rates needed for an employment-weighted calculation. | Do not use 3.8% as an employment share. Keep the current anchor pending; the intended reconstruction remains the best proxy path. |
| Indonesia | Direct artificial-intelligence question in World Bank Enterprise Surveys or Firm Adoption of Technology Survey; Indonesian employer survey; sector- and size-weighted firm survey; broader digital adoption proxy | World Bank Enterprise Surveys provide representative firm-level data and microdata access, but the accessible catalog and data page did not expose a verified Indonesia artificial-intelligence-use measure. No direct national employer estimate was verified. | Current artificial-intelligence adoption is `unanchored`. Broader digital adoption may be contextual only and must not be substituted into the transmission chain. |

## Delivery ledger

| ID | Parameter | Value | Scenario values | Source opened | Denominator | Status | Notes |
|---|---|---:|---|---|---|---|---|
| ALLOC-ID | Indonesia population share of world population | pending | n/a | United Nations World Population Prospects, latest revision | Population | unanchored | Required for the population-share baseline; do not use a realized-impact allocation variant. |
| ID-IDN | Foundational identification coverage | pending | n/a | World Bank Identification for Development Global Dataset | Population | unanchored | The accessible page was blocked during this pass; the latest Indonesia value and year remain to be opened. |
| PAY-IDN-RAW | Account ownership measure retained as payment-access proxy | 51.7553% | 51.7553% / 51.7553% / 51.7553% | World Bank Global Financial Inclusion Database API, indicator `FX.OWN.TOTL.ZS`, 2021 | Adults aged 15 and older | well-sourced | This is raw account ownership, not a government-payment receipt measure. It may be used as a conditional payment-access working figure only after the adult-population denominator issue is addressed. |
| PAY-IDN-COND | Usable payment instrument conditional on foundational identification | pending | n/a | World Bank Global Financial Inclusion Database, preferred government-payment receipt measure | Adults aged 15 and older or population after documented conversion | unanchored | Do not substitute the raw account-ownership value into the conditional until the denominator conversion is sourced. |
| COMPLETE-IDN | Intended payment completion | pending | pending / pending / pending | World Bank studies of mixed Indonesian universal-ish cash programs, including urban bank/account and rural village distribution | Intended payments | unanchored | Must include at least one BST-type and one BLT-Dana-Desa-type program. PKH compliance is excluded. |
| COMP-LIC | Low-income comparator medians | pending | n/a | World Bank Identification for Development and Global Financial Inclusion datasets | Same component denominators and year | unanchored | Requires latest same-year data with at least 80% country coverage. |
| COMP-LMIC | Lower-middle-income comparator medians | pending | n/a | World Bank Identification for Development and Global Financial Inclusion datasets | Same component denominators and year | unanchored | Requires latest same-year data with at least 80% country coverage. |

## Delivery source-pass outcome

- The World Bank Identification for Development landing page and candidate dataset URLs were attempted but were blocked or unavailable in this environment. No Indonesia identification value has been promoted.
- The World Bank Global Financial Inclusion Database API was successfully opened and provides the raw 2021 Indonesian account-ownership observation recorded above.
- Searches for World Bank primary studies reporting auditable intended-payment completion for both an urban bank/account transfer program and a rural village-distribution program did not produce a verified result. No completion scenario value has been promoted.
