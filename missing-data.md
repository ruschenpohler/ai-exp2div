# Missing Data Review

This is the review list for parameters that currently have no usable figure or that rely on a second-best or working figure. It is deliberately separate from the source ledger. The ledger remains the authoritative record of values, denominators, sources, and status.

The author's resolutions below have been applied where possible. Items removed from the live tables are no longer open review questions.

## No Usable Figure

| ID | Parameter | Planned use | What is missing | Required source or next step |
|---|---|---|---|---|
| ADOPT-US-CURRENT | United States current artificial-intelligence use | Adoption filter in the transmission chain | A latest-wave, employment-weighted current-use rate | Download the latest public XLSX/CSV files from the Census Business Trends and Outlook Survey page at `census.gov/hfp/btos`; use the "currently using artificial intelligence" size-class rates and weight them by Census or Bureau of Labor Statistics employment in those classes. The accessible 3.8% figure is a rejected business-count rate from 2023. |
| DIFFUSION-CENTRAL | Same-income-group historical ten-year technology-diffusion increase | Central adoption scenario | The income-group-specific ten-year increase and the world 75th-percentile increase | Use World Development Indicators "Individuals using the Internet (% of population)" to compute the speed anchor, with Comin and Hobijn (2010) as the intellectual anchor. Mark it `working figure`: consumer diffusion, not firm adoption. Never apply the advanced-economy increase to Indonesia. |
| FORMAL-ID | Indonesia formal share of realized harm | Composition column in the transmission table | A comparable, latest-year formal-employment share using the same definition as the United States | Use the same ILOSTAT source as the United States, or document a BPS Sakernas substitution without mixing definitions. |
| CUSHION-US | United States unemployment-benefit effective coverage | Cushion column and harm-need comparison | A comparable number from the same table as Indonesia | Use the International Labour Organization World Social Protection Report statistical annex or the ILOSTAT bulk/SDMX series for SDG 1.3.1 effective coverage. |
| CUSHION-ID | Indonesia unemployment-benefit effective coverage | Cushion column and harm-need comparison | A comparable number from the same table as the United States | Use the International Labour Organization World Social Protection Report statistical annex or the ILOSTAT bulk/SDMX series for SDG 1.3.1 effective coverage. |
| CROSS-TAB-ID | Exposed occupation groups by formality status in Indonesia | Full Indonesia composition claim | Occupational shares for clerical, professional, and service work split by formal status | First check ILOSTAT's informal-employment-rate-by-occupation ISCO-08 series for Indonesia; then try BPS Sakernas August tables. If neither yields a true cross-tab, use the locked fallback aggregate-composition wording and do not claim a formal urban clerical residual. |
| ALLOC-ID | Indonesia share of world population | Population-share allocation baseline | Latest-revision World Population Prospects population share | Open the latest United Nations World Population Prospects table and record year and denominator. |
| ID-IDN | Foundational identification coverage in Indonesia | First delivery-chain component | Latest Indonesia identification coverage from the Identification for Development dataset | Use the 2021 Identification for Development module inside the Global Findex 2021 microdata through the World Bank Microdata Library or Data Catalog. This route supplies the Indonesia component and the common-year comparator data with an adult 15+ denominator. If it fails, use the Identification for Development Indonesia diagnostic or Dukcapil administrative coverage as a labeled `working figure`. |
| PAY-IDN-COND | Usable payment instrument conditional on foundational identification | Second delivery-chain component | A government-payment-receipt measure, or a documented denominator conversion from adults to population | Prefer the Global Financial Inclusion Database government-payment-receipt question. If account ownership is used, source the same-year adult population share and document the downward bias from the independence assumption. |
| COMPLETE-IDN | Payment completion | Third delivery-chain component | Cautious, central, and fast completion values | Use MicroSave Consulting rapid-assessment monitoring for rural/cash BLT Dana Desa and World Bank Indonesia COVID-19 social-protection response papers for urban/account BST. These two program types satisfy the mix; do not use conditional-cash-transfer compliance. |
| COMP-LIC-ID / COMP-LIC-PAY / COMP-LMIC-ID / COMP-LMIC-PAY | Low-income and lower-middle-income comparator medians | Comparator and floor gate | Country-level data, common year, at least 80% group coverage | Use one 2021 Global Findex / Identification for Development microdata route through the World Bank Microdata Library or Data Catalog. Both components are adult 15+ in this route. If it fails, use Findex documentation-barrier or identity-module questions only as a labeled construct downgrade in the appendix, not as equivalent foundational-ID coverage. |
| COMMONS-BASELINE | External justification for treating artificial-intelligence rents as a commons or global claim | Baseline paragraph in section 1 | A primary external source with a usable supporting passage | Use O'Keefe et al. (2020), *The Windfall Clause: Distributing the Benefits of AI*, normative-justifications section, especially the arguments from windfall scale and global distribution of AI costs and benefits. `FLAG TO AUTHOR`: final passage selection. The United Nations report may be a secondary multilateral echo. |
| INCIDENCE-ANCHOR | Concentration of artificial-intelligence development and deployment | Framing paragraph in section 1 | A usable figure from an approved primary source | Use the latest Stanford Artificial Intelligence Index industry chapter for investment and notable-model concentration by country and firm. This is framing, not a rent estimate. |

## Deliberately Not Missing

These inputs have been verified and are not part of the review list:

- Advanced-economy exposure: about 60%.
- Emerging-market exposure used for Indonesia: 40%, explicitly an emerging-market aggregate rather than an Indonesia-specific estimate.
- Low-income-country exposure: 26%.
- Exposure embed decision: not embedded; the task filter stays in the chain.
- Task filters: human-rated alpha / beta / zeta means `0.14 / 0.30 / 0.46`.
- Indonesia adoption filters: unanchored judgment values `0.10 / 0.33 / 0.50`.
- United States formal-share working figure: `0.93`, with a `0.90-0.95` working range.
- Indonesian account ownership: `51.7553%` in 2021, accepted as the conditional fallback after denominator conversion.
- The `$100 allocated to Indonesia` calculation convention.
- The 2021 Indonesian account-ownership observation as a raw, denominator-labeled observation.

## Scope Guardrails

- No figure from this list should enter a calculation merely to make the script run.
- Every promoted figure needs an opened source, denominator, status, and compatibility note.
- A missing Indonesia artificial-intelligence adoption figure must remain visible in the memo rather than being replaced with a United States or generic emerging-market rate.
