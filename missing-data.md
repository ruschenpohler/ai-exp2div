# Missing Data Review

This is the review list for parameters that currently have no usable figure or that rely on a second-best or working figure. It is deliberately separate from the source ledger. The ledger remains the authoritative record of values, denominators, sources, and status.

## No Usable Figure

| ID | Parameter | Planned use | What is missing | Required source or next step |
|---|---|---|---|---|
| ADOPT-US-CURRENT | United States current artificial-intelligence use | Adoption filter in the transmission chain | A latest-wave, employment-weighted current-use rate | Use Business Trends and Outlook Survey current-use rates by employment-size class, weighted by Census employment in those classes. The accessible 3.8% figure is a business-count rate from 2023 and is not usable as an employment share. |
| ADOPT-ID-CURRENT | Indonesia current artificial-intelligence use | Adoption filter in the transmission chain | Any verified Indonesia-specific current artificial-intelligence-use figure | Check the Indonesia wave of the World Bank Firm Adoption of Technology Survey, World Bank Enterprise Surveys technology modules, and direct Indonesian employer surveys. If none exists, keep this `unanchored`. |
| DIFFUSION-CENTRAL | Same-income-group historical ten-year technology-diffusion increase | Central adoption scenario | The income-group-specific ten-year increase and the world 75th-percentile increase | Open Comin and Hobijn (2010) and its dataset. Do not apply an advanced-economy increase to Indonesia. |
| FORMAL-US | United States formal share of realized harm | Composition column in the transmission table | A comparable, latest-year formal-employment share using the same definition as Indonesia | Open the same ILOSTAT informality source for both countries and check whether the employment bases match the exposure data. |
| FORMAL-ID | Indonesia formal share of realized harm | Composition column in the transmission table | A comparable, latest-year formal-employment share using the same definition as the United States | Use the same ILOSTAT source as the United States, or document a BPS Sakernas substitution without mixing definitions. |
| CUSHION-US | United States unemployment-benefit effective coverage | Cushion column and harm-need comparison | A comparable number from the same table as Indonesia | Use ILOSTAT or the International Labour Organization World Social Protection Report; use ASPIRE only as the documented second-best. |
| CUSHION-ID | Indonesia unemployment-benefit effective coverage | Cushion column and harm-need comparison | A comparable number from the same table as the United States | Use ILOSTAT or the International Labour Organization World Social Protection Report; use ASPIRE only as the documented second-best. |
| CROSS-TAB-ID | Exposed occupation groups by formality status in Indonesia | Full Indonesia composition claim | Occupational shares for clerical, professional, and service work split by formal status | Find an ILOSTAT cross-tab or Sakernas table. If unavailable, use the fallback aggregate-composition wording and do not claim a formal urban clerical residual. |
| ALLOC-ID | Indonesia share of world population | Population-share allocation baseline | Latest-revision World Population Prospects population share | Open the latest United Nations World Population Prospects table and record year and denominator. |
| ID-IDN | Foundational identification coverage in Indonesia | First delivery-chain component | Latest Indonesia identification coverage from the Identification for Development dataset | Obtain and open the World Bank Identification for Development Global Dataset. The public page and candidate download links were inaccessible in this environment. |
| PAY-IDN-COND | Usable payment instrument conditional on foundational identification | Second delivery-chain component | A government-payment-receipt measure, or a documented denominator conversion from adults to population | Prefer the Global Financial Inclusion Database government-payment-receipt question. If account ownership is used, source the same-year adult population share and document the downward bias from the independence assumption. |
| COMPLETE-IDN | Payment completion | Third delivery-chain component | Cautious, central, and fast completion values | Open primary World Bank or government-to-person studies for at least one urban bank/account transfer program and one rural village-distribution program. Do not use conditional-cash-transfer compliance. |
| COMP-LIC-ID | Low-income-country identification median | Comparator and threshold | Country-level data, common year, at least 80% group coverage | Obtain the Identification for Development data and document the country count. |
| COMP-LIC-PAY | Low-income-country payment-access median | Comparator and threshold | Country-level data, same year and coverage rule as identification | Obtain the Global Financial Inclusion data and document the country count. |
| COMP-LMIC-ID | Lower-middle-income-country identification median | Comparator and floor gate | Country-level data, common year, at least 80% group coverage | Obtain the Identification for Development data and document the country count. |
| COMP-LMIC-PAY | Lower-middle-income-country payment-access median | Comparator and floor gate | Country-level data, same year and coverage rule as identification | Obtain the Global Financial Inclusion data and document the country count. |
| COMMONS-BASELINE | External justification for treating artificial-intelligence rents as a commons or global claim | Baseline paragraph in section 1 | A primary external source with a usable supporting passage | The United Nations `Governing AI for Humanity` report is the leading candidate, but its fit to the specific commons premise still needs a usable quote. |
| INCIDENCE-ANCHOR | Concentration of artificial-intelligence development and deployment | Framing paragraph in section 1 | A usable figure from an approved primary source | Use the IMF 2024 note or the latest Stanford Artificial Intelligence Index industry-concentration chapter. This is framing, not a rent estimate. |

## Second-Best Or Working Figures

| ID | Parameter | Current figure or substitution | Why it is second-best | Review question |
|---|---|---|---|---|
| TASK-FILTER | Task-share scale factor | `0.14 / 0.50 / 0.55` for cautious, central, and fast | The lower value is the human alpha mean; the central value is locked by the plan at the 50% E2 threshold; the fast value is the GPT-4 zeta mean. The central and fast choices are scenario substitutions, not directly comparable observed values. | Are these the intended scale factors, or should cautious and fast use different tier-consistent values from the source? |
| PAY-IDN-RAW | Indonesian account ownership | `51.7553%` in 2021 | This is raw account ownership among adults aged 15 and older, not government-payment receipt and not population-based identification. | Is this acceptable as a conditional working figure after a same-year denominator conversion, or should the measure remain unused? |
| ADOPT-US-OLD | United States artificial-intelligence use | `3.8%` of businesses in 2023 | It is a business-count rate, not an employment-weighted rate, and is not the latest wave. It is retained only as a rejected reference point. | Confirm that it must stay out of all calculations. |
| ADOPT-ID-DIGITAL | Indonesia broader digital-technology adoption | None selected | Cloud, enterprise software, or advanced digital adoption would not be artificial-intelligence adoption. Using it would change the parameter definition. | Should any such measure appear only as contextual background, or be omitted entirely? |

## Deliberately Not Missing

These inputs have been verified and are not part of the review list:

- Advanced-economy exposure: about 60%.
- Emerging-market exposure used for Indonesia: 40%, explicitly an emerging-market aggregate rather than an Indonesia-specific estimate.
- Low-income-country exposure: 26%.
- Exposure embed decision: not embedded; the task filter stays in the chain.
- The `$100 allocated to Indonesia` calculation convention.
- The 2021 Indonesian account-ownership observation as a raw, denominator-labeled observation.

## Scope Guardrails

- No figure from this list should enter a calculation merely to make the script run.
- Every promoted figure needs an opened source, denominator, status, and compatibility note.
- A missing Indonesia artificial-intelligence adoption figure must remain visible in the memo rather than being replaced with a United States or generic emerging-market rate.
