# Data Handoff For The Next Agent

This document lists the remaining data work. The calculation scripts must not silently replace any item below with a convenient proxy. Every promoted value needs an opened source, year, denominator, status, and compatibility note in `docs/parameters_and_sources.md`.

## 1. United States Adoption

### What we need

An employment-weighted rate of United States employer businesses that are **currently using artificial intelligence**, preferably the latest Business Trends and Outlook Survey wave.

The local BTOS file already supplies current-use rates by size class:

| BTOS class | Employees | Current-use rate |
|---|---:|---:|
| A | 1-4 | 20.8% |
| B | 5-9 | 21.3% |
| C | 10-19 | 21.3% |
| D | 20-49 | 22.7% |
| E | 50-99 | 28.4% |
| F | 100-249 | 33.6% |
| G | 250+ | 36.8% |

Source: `data/US Census BTOS/Employment Size Class.xlsx`.

### What it is for

This is the United States adoption filter in `calcs/transmission.py`. It is a scale factor applied to the flagged exposure share.

### Decision record

Resolved. The employment-weighted current-use rate is **29.5%** (2 significant figures), or **29.48%** exactly.

Calculation basis:

| Band | CBP 2023 establishment employment | BTOS current-use rate |
|---|---:|---:|
| 1-4 | 7,575,276 | 20.8% |
| 5-9 | 9,721,925 | 21.3% |
| 10-19 | 14,195,837 | 21.3% |
| 20-49 | 22,828,921 | 22.7% |
| 50-99 | 17,109,742 | 28.4% |
| 100-249 | 20,808,223 | 33.6% |
| 250+ | 47,591,818 | 36.8% |
| Total | 139,831,742 | weighted 29.48% |

Data sources:
- BTOS current-use rates by size class: `data/US Census BTOS/Employment Size Class.xlsx`
- CBP 2023 United States file: https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23us.zip
  - Row `uscode=98`, `naics=------`, `lfo=-`
  - 2023, employment during the week of March 12

Rationale:
- CBP provides the exact BTOS-compatible bands, replacing the SUSB aggregate-band approximation.
- The rate is employment-weighted, which is the correct denominator for a worker-level adoption filter.
- This is labelled `working figure` only in the sense that the BTOS rate is a survey estimate; the weighting itself is exact.
- The earlier SUSB-based aggregate-band estimate of about 31.4% is superseded by this CBP-based value.

### Sources searched

- BTOS main page: https://www.census.gov/hfp/btos
- BTOS data page: https://www.census.gov/data/experimental-data-products/business-trends-and-outlook-survey.html
- SUSB program page: https://www.census.gov/programs-surveys/susb.html
- CBP datasets: https://www.census.gov/programs-surveys/cbp/data/datasets.html
- CBP 2023: https://www.census.gov/data/datasets/2023/econ/cbp/2023-cbp.html

The CBP dataset was successfully downloaded and processed.

## 2. Indonesia Foundational Identification

### What we need

The share of Indonesia's population with a foundational, state-recognized identity that can authenticate the person for public services or payments. This is not an identification of people for research. It means possession of a usable official identity record, such as a national identity number, identity card, or recognized digital identity.

Required fields:

- Indonesia value
- Survey or administrative year
- Numerator and denominator
- Whether the denominator is population or adults aged 15+
- Definition of the identity credential or record

### What it is for

This is the first component of the delivery chain:

`foundational identification coverage x payment instrument conditional on identification x payment completion`

The Indonesia chain currently needs a population-denominator identification value. The comparator calculation may instead use a common adult 15+ denominator if both components come from the same Global Findex/identity source.

### What has been found

The local country-level Global Findex file is useful for payment and account variables, including Indonesia for 2024, but it does not contain the foundational identity coverage variable.

File: `data/WB Global Findex/GlobalFindexDatabase2025.csv`.

The World Bank report *Beyond Unicorns: Harnessing Digital Technologies for Inclusion in Indonesia* discusses the need for a national digital identity framework but does not provide a usable national coverage percentage:

- Report page: https://www.worldbank.org/en/country/indonesia/publication/beyond-unicorns-harnessing-digital-technologies-for-inclusion-in-indonesia
- Full report: https://openknowledge.worldbank.org/bitstream/handle/10986/36018/162061.pdf?sequence=5&isAllowed=y

The World Bank Identification for Development DataBank and landing page were checked, but no downloadable value was obtained in this environment.

### Decision record

Working figure adopted: **foundational identity coverage = 0.98**, on an adult/population basis, labelled `working figure` and subject to author confirmation or replacement by an administrative figure.

Anchors reviewed during this pass:

1. World Bank, *Investing in People: Social Protection for Indonesia's 2045 Vision* (2020), states that "the majority of Indonesians have a population identity number (NIK)", issued through SIAK with biometrics as national ID credentials.
2. Global Findex 2021 report text confirms that the Findex/ID4D partnership data treat the national ID document or legally recognized ID credential as the identification measure and that documentation barriers affect only a small minority of adults in Indonesia.
3. Local Global Findex 2025 country file, Indonesia 2024: the documentation-barrier variable (`fin41`) is 2.4% of adults, supporting the view that the share of adults without usable identification is small. The exact definition of `fin41` requires the codebook; it is used here only as supporting evidence, not as the coverage measure itself.

Decision rationale: 0.98 is consistent with all three anchors and with the well-established near-universal NIK/e-KTP coverage; it is a deliberately conservative working value rather than a precise survey estimate.

Author note (2026-08): the author confirms there is no official NIK coverage number published as a single national statistic. The 0.98 working figure therefore stands as a documented judgment anchored on the sources above, not on an official figure. No Dukcapil or ministry publication should be searched further; the only firmer alternative is the survey-based ID4D Global Dataset.

Better option if the author wants to firm this up:

- The 2021 ID4D Global Dataset (xlsx) from https://id4d.worldbank.org/global-dataset, which contains the survey-based foundational ID coverage for Indonesia.
- The 2021 Global Findex/ID4D microdata through https://microdata.worldbank.org/catalog/ if the author can download it.

### Most promising remaining sources

- 2021 Global Findex / Identification for Development identity-module microdata through the World Bank Microdata Library: https://microdata.worldbank.org/catalog/
- Identification for Development site: https://id4d.worldbank.org/
- An Identification for Development Indonesia country diagnostic or report
- Indonesian Dukcapil administrative coverage for NIK/e-KTP, with a clear population or adult denominator

If no direct Identification for Development value can be obtained, use a Dukcapil or World Bank administrative figure as a labelled `working figure`. Do not present it as survey-based Identification for Development coverage.

## 3. Global Findex Payment Access

### What we need

Preferably, the percentage of Indonesian adults receiving government payments into an account or usable payment instrument. If that cannot be extracted, use account ownership as the conditional payment-access working figure.

The denominator must be explicit. The local Global Findex file is adult-based.

### What it is for

This is the second delivery-chain component, conditional on foundational identification.

### What has been found

The local 2025 country-level Global Findex file contains Indonesia observations for 2024 and payment-related variables. It is sufficient for the country-level payment component once the codebook confirms the relevant field definition.

The earlier 2021 account-ownership value was 51.7553% of adults aged 15+. The 2024 file contains a newer account-ownership observation and government-payment-related fields.

### Remaining work

Open the Global Findex codebook and map the relevant variable names before using them. If the government-payment-receipt variable is unavailable or unsuitable, use account ownership with:

- Same-year adult population conversion for the Indonesia chain
- A `working figure` status
- The explicit note that the independence assumption biases the arrival estimate downward, toward more apparent leakage

## 4. Indonesian Payment Completion

### What we need

Two program-level completion observations, with numerator and denominator:

1. **Rural and cash leg:** BLT Dana Desa. Need intended payments or recipients and payments actually disbursed or received.
2. **Urban and account leg:** Bantuan Sosial Tunai, usually called BST. Need intended payments or recipients and payments actually made or received through bank or account channels.

These produce cautious, central, and fast payment-completion values. The lowest and highest values must come from this mixed program set; the central value is the main estimate.

### What it is for

This is the third delivery-chain component and drives the three delivery scenarios.

### What has been found

The MicroSave article below was opened:

https://www.microsave.net/2023/12/19/from-break-out-to-breakthrough-ways-to-sustain-digital-momentum-in-indonesia/

It is a general article about Indonesia's digital economy, QRIS, digital public infrastructure, and inclusion. It does not report BLT Dana Desa intended-versus-completed payments, so it is not usable for this parameter.

MicroSave's WordPress search for `BLT Dana Desa` returned no result. World Bank Documents and Reports searches for the full terms `Bantuan Sosial Tunai` and `BLT Dana Desa` did not expose a usable indexed report with completion numerators and denominators.

### Decision record

Resolved from the HiFy household microdata. The values below are computed directly from the World Bank Indonesia High-Frequency Monitoring of COVID-19 Impacts survey, using household receipt of BST (program code 102, sub-type A) and BLT Dana Desa (sub-type B), weighted by the survey weights.

Weighted share of all households reporting receipt (module PS_9B):

| Round | Survey period | Recall window | BST (% households) | BLT Dana Desa (% households) |
|---|---|---|---|---|
| 1 | May 2020 | since Feb 2020 | 2.4% | 1.2% |
| 3 | Jul-Aug 2020 | since Feb 2020 | 15.3% | 10.4% |
| 5 | Mar 2021 | since Jul 2020 | 20.9% | 8.9% |
| 6 | Oct 2021 | since Apr 2021 | 12.8% | 11.4% |

Implied completion among intended beneficiaries, dividing the receipt share by the intended share of households (BST target 9 million households, BLT Dana Desa target 11 million, of roughly 71 million households):

| Round | BST implied completion | BLT implied completion |
|---|---|---|
| 1 (May 2020) | ~0.19 | ~0.08 |
| 3 (Jul-Aug 2020) | >1, cap 0.95 | ~0.67 |
| 5 (Mar 2021) | >1, cap 0.95 | ~0.58 |
| 6 (Oct 2021) | ~1.0, cap 0.95 | ~0.74 |

Scenario values adopted:

| Scenario | Value | Basis |
|---|---|---|
| cautious | 0.60 | Rural/cash BLT Dana Desa leg at mid-rollout (implied ~0.67 in Round 3), rounded conservatively. This is the weaker of the two failure modes. |
| central | 0.75 | Average of the two legs at maturity: BLT Dana Desa ~0.58-0.74 and BST near 0.95. |
| fast | 0.95 | Urban/account BST leg at or above target, consistent with the implementation plan's prior that account-based programs complete above 90%. |

Source: HiFy microdata, reference IDN_2020_HFMCI_v06_M, local copy in `data/WB COVID HiFreq`. Variables: module PS_9B, program code 102, sub-type A (BST) / B (BLT), receipt indicator ps9_2a. Weights: wgt_R1, wgt_R3, wgt_R6 (first sample) and fwgt_R5 (second sample), joined through the roster nks_covid key and household id. Program-code mapping confirmed against the Round 3, 5, and 6 questionnaires.

Caveats: receipt is household-reported and recall-window based; implied completion divides reported receipt by the intended target share and assumes recipients are within target; Round 5 uses second-sample weights (fwgt_R5), the other rounds the first-sample weights. These are working-figure values and are flagged for author approval.

Corroborating fiscal-execution context (from opened World Bank reports):

- National Economic Recovery Program ~60% disbursed by mid-October 2020 (*Indonesia Economic Prospects, December 2020*).
- The 2020 COVID-19 fiscal package was executed at 83% of final budget allocations by end-2020, with social protection among the best-executed components (*Indonesia Economic Prospects, June 2021*, Box A.3, Ministry of Finance data).
- BST was extended in April/May 2021, indicating operation beyond 2020 (*Indonesia Economic Prospects, June 2021*).

Sources opened:

- HiFy microdata and questionnaires: https://microdata.worldbank.org/index.php/catalog/3938 (local copy in `data/WB COVID HiFreq`)
- https://documents1.worldbank.org/curated/en/804791594826869284/pdf/Indonesia-Economic-Prospects-The-Long-Road-to-Recovery.pdf (July 2020)
- https://documents1.worldbank.org/curated/en/505381608137667057/pdf/Indonesia-Economic-Prospects-Towards-a-Secure-and-Fast-Recovery.pdf (December 2020)
- https://documents1.worldbank.org/curated/en/379141623773793892/pdf/Indonesia-Economic-Prospects-June-2021.pdf (June 2021)

### Most promising remaining sources

- MicroSave library: https://www.microsave.net/library/
- MicroSave search: https://www.microsave.net/?s=BLT+Dana+Desa
- World Bank Documents and Reports: https://documents.worldbank.org/en/publication/documents-reports
- TNP2K publications: https://www.tnp2k.go.id/
- J-PAL Southeast Asia: https://www.povertyactionlab.org/region/southeast-asia
- Indonesian Ministry of Social Affairs and Ministry of Villages administrative reports

Search inside documents for `disbursement`, `realization`, `received`, `beneficiaries paid`, `payment delivery`, and `bank transfer`, not only `completion`.

If no program study reports a true intended-versus-paid rate, do not substitute total program spending or beneficiary registration. That would measure authorization or allocation, not delivery.

## 5. Unemployment-Benefit Coverage

### Status

Resolved from the supplied local file.

File: `data/ILOSTAT/SDG_0131_SEX_SOC_RT_A-20260803T1618.csv`.

Use:

- `classif1 = SOC_CONTIG_UNE`
- `sex = SEX_T`
- Indonesia: 0%, 2021
- United States: 50.5%, 2021

Direct ILOSTAT source: https://rplumber.ilo.org/data/indicator?id=SDG_0131_SEX_SOC_RT_A&format=.csv

The indicator is effective social-protection coverage for unemployment benefits, expressed as a percentage of unemployed people. The same year and indicator are available for both countries.

## 6. Informality And Occupation

### Status

The Indonesia data are available locally:

- Overall informal employment: 80.975%, 2023
- Professionals: 60.015%
- Technicians: 60.160%
- Clerical support: 62.166%
- Service and sales: 75.486%

File: `data/ILOSTAT/EMP_NIFL_SEX_OCU_RT_A-20260803T0606.csv`.

This is an informal-employment rate within each occupation. It is not an occupation-share-by-formality cross-tab. It cannot establish that a particular share of all exposed employment is formal or informal.

The stronger Indonesia clerical/formal concentration claim should therefore use the approved fallback wording unless BPS Sakernas provides a true joint occupation-by-formality employment table.

The United States does not appear in the supplied ILOSTAT informality file. The approved United States formal-share working figure remains 0.93, with a 0.90-0.95 working range.

## 7. Population

### What we need

For the allocation baseline:

- Indonesia total population
- World total population
- Same year, preferably 2023
- A simple ratio: Indonesia population divided by world population

For the Findex denominator conversion:

- Total population for the same year as the Findex observation used in the chain
- Use 2021 if the identity route is the 2021 Identification for Development/Findex module
- Use 2024 if the 2024 Global Findex observation is used

### Decision record

Resolved for 2023 from World Bank World Development Indicators, `Population, total`:

- Indonesia: **281,190,067**
- World: **8,062,923,417**
- Indonesia share: **3.49%**

Source: https://api.worldbank.org/v2/country/IDN/indicator/SP.POP.TOTL?date=2023 and https://api.worldbank.org/v2/country/WLD/indicator/SP.POP.TOTL?date=2023

Rationale:
- 2023 is the latest estimate year in the World Population Prospects family already used locally and is the recommended base year for the allocation ratio.
- The share is Indonesia divided by world population, both in the same year.
- For the Findex denominator conversion, still use the year matching the Findex observation actually used in the chain (2021 or 2024).

### What has been found

The supplied file `WPP2024_POP_F01_1_POPULATION_SINGLE_AGE_BOTH_SEXES.xlsx` is a single-age extract and is not convenient for this calculation. The World Bank World Development Indicators source above is simpler and confirmed.

### Recommended source

World Bank World Development Indicators, `Population, total`:

https://data.worldbank.org/indicator/SP.POP.TOTL?locations=ID-1W

This source directly provides the confirmed 2023 values used above.

## 8. Commons Baseline

### Status

The local O'Keefe paper has been opened: `lit/OKEEFE2025.pdf`.

Use the normative/global-claim material in section 6.1, page 4. The paper argues that AI's economic effects transcend political boundaries and that windfall benefits can be distributed internationally. The page 1 passage stating that benefits should broadly benefit humanity is also available as a shorter alternative.

The final passage choice remains `FLAG TO AUTHOR`.

## 9. United States Concentration Anchor

### What is needed

A usable figure or table from the latest Stanford Artificial Intelligence Index showing **concentration** of artificial-intelligence development and deployment. The memo uses this in section 1 only as framing: that AI rents accrue to a small set of firms in a few jurisdictions, so the recipient-side question is allocation and delivery, not collection.

The specific items sought, in priority order:

1. **Private investment concentration**: the share of global private AI investment going to the United States (or to a small number of countries/firms), e.g., the report's "private AI investment by country" table. The index typically shows the United States accounting for the large majority of global private AI investment.
2. **Notable-model concentration**: the number of notable AI models (or foundation models) produced per country, showing concentration among the United States, China, and the United Kingdom.
3. **Newly funded AI company counts** by country, if the above are not directly available.

### Source

Link: https://hai.stanford.edu/ai-index-report

Description: The AI Index is an independent initiative at the Stanford Institute for Human-Centered Artificial Intelligence (HAI). It publishes an annual report tracking AI development, investment, research, technical performance, and policy. The relevant chapter is the **"Industry" or "Economy" chapter** (titles vary by year), which contains the private-investment and notable-model tables. The current report is the *Artificial Intelligence Index Report* (latest edition; the download page is the report landing page above).

How to use it: locate the table showing private AI investment by country for the most recent year and record the United States share (e.g., "X% of global private AI investment"). One number is sufficient; it will be cited as concentration of development/deployment, labelled framing, not a rent estimate. The IMF 2024 note is an approved alternate only if the AI Index table cannot be extracted.

The report itself is the source; no separate public dataset is required. This is the only item still awaiting an external figure.

## Current Takeover Order

1. Use the SUSB aggregate-band working calculation for United States adoption.
2. Resolve the Global Findex variable definitions and find the Identification for Development identity variable or a labelled administrative alternative.
3. Use the ILOSTAT unemployment-benefit file immediately in the ledger.
4. Find the two payment-program completion reports through TNP2K, J-PAL, ministry reports, or World Bank document identifiers.
5. Use World Development Indicators total population for the allocation ratio and same-year denominator conversion.
6. Decide the fallback wording for the occupation/formality claim if no joint cross-tab is found.
