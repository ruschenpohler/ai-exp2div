# Missing Data Review

This is the review list for parameters that currently have no usable figure or that rely on a second-best or working figure. It is deliberately separate from the source ledger. The ledger remains the authoritative record of values, denominators, sources, and status.

The author's resolutions below have been applied where possible. Items removed from the live tables are no longer open review questions.

## No Usable Figure

| ID | Parameter | Planned use | What is missing | Required source or next step |
|---|---|---|---|---|
| ADOPT-US-CURRENT | United States current artificial-intelligence use | Adoption filter in the transmission chain | A latest-wave, employment-weighted current-use rate | Use Business Trends and Outlook Survey current-use rates by employment-size class, weighted by Census employment in those classes. The accessible 3.8% figure is a business-count rate from 2023 and is not usable as an employment share. |
| DIFFUSION-CENTRAL | Same-income-group historical ten-year technology-diffusion increase | Central adoption scenario | The income-group-specific ten-year increase and the world 75th-percentile increase | Open Comin and Hobijn (2010) and its dataset. Do not apply an advanced-economy increase to Indonesia. |
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

## Implemented Resolutions

- `TASK-FILTER`: replaced the mixed `0.14 / 0.50 / 0.55` inputs with one human-rated construct family from Eloundou et al.: alpha / beta / zeta means, `0.14 / 0.30 / 0.46`. This intentionally supersedes the plan's category-level 50% central substitution because the review identified it as a category error.
- `ADOPT-ID-CURRENT`: set unanchored judgment filters to `0.10 / 0.33 / 0.50` for cautious, central, and fast. No proxy is used.
- `FORMAL-US`: set the approved working figure to `0.93` in all scenarios, with a documented `0.90-0.95` working range.
- `PAY-IDN-RAW`: accepted as the conditional second choice if the government-payment-receipt measure cannot be extracted. Same-year adult-population conversion and the downward-bias note remain required.
- `ADOPT-US-OLD`: removed from the live review list and remains excluded from calculations.
- `ADOPT-ID-DIGITAL`: removed from the live review list and excluded from calculations; at most it can receive one contextual, non-numeric sentence later.

## Not Yet Executed

- The latest Business Trends and Outlook Survey public size-class files have not yet been pulled and weighted; `ADOPT-US-CURRENT` remains live.
- The World Development Indicators internet-use fallback has been approved, but the year-matched income-group values and 75th-percentile increase have not yet been extracted; `DIFFUSION-CENTRAL` remains live.
- The remaining source-dependent advice is not yet executed: Indonesia formal share denominator check, unemployment-benefit coverage, the targeted occupational cross-tab attempt, the exact population share, identification coverage, payment-access denominator conversion, payment completion, comparator medians, the commons-baseline passage, and the incidence anchor.

---

# Resolutions (added after review)

*Answers keyed to the IDs above. Verdicts are final unless marked FLAG TO AUTHOR.*

## No Usable Figure — resolutions

**ADOPT-US-CURRENT — access failure, not a gap. Retry BTOS directly.** The Business Trends and Outlook Survey publishes public CSVs with AI-use rates by employment-size class. Pull the latest wave's "currently using AI" rates per size class and weight by Census/BLS employment in those classes, per the plan's weighting rule. The 3.8% figure was rejected correctly; the error was relying on a stale secondary citation instead of the BTOS files.

**ADOPT-ID-CURRENT — genuine gap, no good proxy exists. Do not hunt further.** This is the designed hole in the architecture: the one `unanchored` parameter, quarantined to a filter, foregrounded in its memo sentence. Plan amendment: because "current anchor, no projection" is undefined without an anchor, Indonesia's three adoption scenario values become stated judgment values — 0.1 / 0.33 / 0.5 (cautious / central / fast) — sourced to nothing but reasoning, labeled `unanchored` in all three scenarios. The §2 scenario gate then tests whether the inversion survives the entire judgment range, which is the strongest available defense of an unanchored number.

**DIFFUSION-CENTRAL — replace the source, keep the construct.** Extracting income-group ten-year increases from the Comin–Hobijn CHAT dataset is laborious and the data thin out where needed. Substitute: World Development Indicators "Individuals using the Internet (% of population)", aggregated by income group — ten-year increases computable directly from the public series. Mark `working figure` with the caveat that it is consumer diffusion, not firm adoption; it serves as a speed-of-diffusion anchor for a scenario, not a forecast. Cite Comin & Hobijn (2010) as the intellectual anchor; WDI provides the number. Never apply the advanced-economy increase to Indonesia (rule stands).

**FORMAL-US — stop hunting; use the planned fallback.** ILOSTAT genuinely may not publish US informality. The plan anticipated this: formal ≈ 0.9–0.95, `working figure`. Use 0.93 central, note the range in the ledger.

**FORMAL-ID — ILOSTAT, with the agriculture check.** ILOSTAT covers Indonesia. The remaining task is only the denominator match against the exposure base (agriculture in/out) per plan §3.4. If Sakernas is substituted, document the definition and do not mix with ILOSTAT in the same table.

**CUSHION-US / CUSHION-ID — access failure. Use the ILO World Social Protection Report statistical annex** (SDG 1.3 unemployment-benefit effective coverage; a fetchable PDF), same table for both countries. Expect a stark gap: US coverage of the unemployed roughly a quarter to a third; Indonesia near zero (JKP launched 2021, minimal coverage). The starkness is anticipated — the two-variant inversion wording exists precisely so the sentence does not overclaim from it.

**CROSS-TAB-ID — 50/50; one more targeted attempt, then take the fallback without regret.** Try: BPS Sakernas August-round published tables (occupation × formal/informal status) and ILOSTAT's informality-by-occupation series. If neither yields a true cross-tab, use the locked fallback wording (aggregate composition, no formal-urban-clerical claim) and log the variant shipped. The two-variant design was built for exactly this outcome.

**ALLOC-ID — trivial access failure.** Indonesia ≈ 3.4–3.5% of world population. If the UN WPP portal blocks bulk access, the same figure derives from World Bank WDI (SP.POP.TOTL, Indonesia / world). Record year and denominator.

**ID-IDN — access failure, and Indonesia is the easy case.** Foundational ID (NIK/e-KTP) coverage is near-universal (high-90s of adults). If the ID4D Global Dataset download fails, use the ID4D Indonesia country diagnostic (PDF) or Dukcapil administrative coverage as reported in World Bank G2P work, marked `working figure` (administrative source). Do not stall on the dataset when the country report has the number.

**PAY-IDN-COND — resolved; see PAY-IDN-RAW verdict below.** Check the Findex government-payment-receipt question first; if not extractable, the account-ownership route with same-year UN WPP adult-share conversion and the downward-bias note is the designed fallback. Also check once whether a Findex wave newer than 2021 has published.

**COMPLETE-IDN — findable; effort problem, not existence problem.** BLT Dana Desa and BST completion evidence exists in World Bank Indonesia G2P work, TNP2K reports, and J-PAL Southeast Asia evaluations. The program-mix rule stands: at least one urban bank/account program (BST) and one rural cash/village program (BLT Dana Desa).

**COMP-LIC-ID / COMP-LIC-PAY / COMP-LMIC-ID / COMP-LMIC-PAY — access failure. Pull the bulk data, not the landing pages.** Findex indicators are on the World Bank DataBank (bulk CSV); the ID4D 2021 dataset also mirrors on the Humanitarian Data Exchange. If ID4D truly cannot be obtained in bulk, a labeled second-best for the ID component of the comparator only: Findex's documentation-barrier and ID-module questions. Apply the ≥80% coverage and same-year rules; log N per group.

**COMMONS-BASELINE — better candidate than the UN report.** Primary: O'Keefe et al. (2020), "The Windfall Clause: Distributing the Benefits of AI" (GovAI/FHI) — external to the Trust, argues the global-claim principle directly, and is the academic ancestor of Windfall's own idea (which also signals knowledge of their intellectual lineage). Secondary, optional: UN "Governing AI for Humanity" as the multilateral echo. FLAG TO AUTHOR remains for the final passage selection.

**INCIDENCE-ANCHOR — retry; the source exists.** The latest Stanford AI Index has usable concentration figures (private investment and model development by country and firm); the IMF 2024 note is the alternate. Label as concentration of development/deployment, framing only, per plan.

## Second-Best Or Working Figures — verdicts

**TASK-FILTER — REJECT AS CONSTRUCTED; plan amendment.** The three values mix constructs: a human-rating mean (cautious), a threshold *definition* used as a value (central — 0.5 is the E2 cutoff, not a measured share), and a GPT-4 rating mean (fast). Replace with Eloundou et al.'s own three exposure measures as the three scenarios: α (human-rated direct exposure, ≈0.14) / β (α plus half-weighted E2) / ζ (full E1+E2). One source, one construct family, tier-consistent, each a measured mean. This supersedes the plan's "E2 lock", which was a category error faithfully executed. Record the three values from the paper, not from this note.

**PAY-IDN-RAW — ACCEPT as conditional, second choice.** Prefer the Findex government-payment-receipt question; if not extractable, 51.8% (2021) account ownership is acceptable under the same-year UN WPP adult-share conversion, `working figure`, with the downward-bias direction note. Check once for a newer Findex wave.

**ADOPT-US-OLD — CONFIRMED OUT.** Stays out of all calculations. Retained in the ledger only as a rejected reference point, as currently labeled.

**ADOPT-ID-DIGITAL — OMIT from calculations entirely.** At most one contextual background sentence in the memo, no number. Cloud/software adoption is a different parameter; admitting it would silently redefine the filter.

---

# Additions without a corresponding point in the file

1. **Scenario-table amendment (consequence of ADOPT-ID-CURRENT and TASK-FILTER).** The implementation plan's scenario table row definitions change: task filter scenarios = α / β / ζ per the TASK-FILTER verdict; Indonesia adoption scenarios = 0.1 / 0.33 / 0.5 judgment values, `unanchored` in all three. US adoption keeps the two-step rule (BTOS anchor + WDI-based diffusion increase). Update the table and the ledger together so scripts and plan cannot diverge.

2. **Expected knock-on for the §2 gate.** With cautious task filter at α ≈ 0.14 and cautious Indonesia adoption at 0.1, cautious-scenario realized harm for Indonesia will be very small. Check that the inversion sentence still passes the all-three-scenarios gate under the new values before drafting; if it fails in cautious only, use the gate's report-which-scenarios wording as designed.

3. **Cushion starkness guard.** Given the expected near-zero Indonesia unemployment coverage, re-read the drafted inversion sentence against the "true by construction / that's just development" objection (MS11, v3 round): the shipped wording must stay within the two locked variants and must not present the US–Indonesia coverage gap alone as the finding.

4. **One-line provenance note for the repo.** When these resolutions are executed, move each resolved parameter out of this review list and into the ledger with its opened source; this file should end up empty of live items and can then be retired or kept as an audit trail. Do not maintain two authoritative lists.
