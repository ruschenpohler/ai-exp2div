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

### What has been found

The supplied SUSB file contains employment totals in these compatible aggregate bands:

- Less than 5 employees: 6,295,615
- 5-9 employees: 6,810,300
- 10-19 employees: 8,844,269
- 20-99 employees: 21,976,701
- 100-499 employees: 18,323,671
- 500+ employees: 73,497,851

Source: `data/US SUSB/us_state_6digitnaics_2022.xlsx`, United States total row, enterprise size.

The BTOS rates can therefore be aggregated upward:

- BTOS A, B, and C map exactly.
- BTOS D and E combine into SUSB 20-99.
- BTOS F and G combine into SUSB 100+.

### Remaining limitation

SUSB does not split 20-99 into 20-49 and 50-99, so the D/E combined rate requires a working assumption. It also does not need to split F/G if both are combined into 100+.

The D/E rates differ by 5.7 percentage points; the F/G rates differ by 3.2 points. This should have a limited effect on the overall employment-weighted rate, but it must be labelled `working figure`.

### Sources searched

- BTOS main page: https://www.census.gov/hfp/btos
- BTOS data page: https://www.census.gov/data/experimental-data-products/business-trends-and-outlook-survey.html
- SUSB program page: https://www.census.gov/programs-surveys/susb.html
- SUSB tables: https://www.census.gov/programs-surveys/susb/data/tables.html

The BTOS dashboard and static page did not provide a more detailed employment-weight table. The local SUSB file is the best available weighting source.

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

### What has been found

The supplied file `WPP2024_POP_F01_1_POPULATION_SINGLE_AGE_BOTH_SEXES.xlsx` is a single-age extract and is not convenient for this calculation. It contains metadata and a partial row rather than easy country-level total-population rows.

### Recommended source

World Bank World Development Indicators, `Population, total`:

https://data.worldbank.org/indicator/SP.POP.TOTL?locations=ID-1W

This source directly displays Indonesia and World totals by year and is sufficient for both the population-share ratio and the denominator conversion, provided the year is recorded.

## 8. Commons Baseline

### Status

The local O'Keefe paper has been opened: `lit/OKEEFE2025.pdf`.

Use the normative/global-claim material in section 6.1, page 4. The paper argues that AI's economic effects transcend political boundaries and that windfall benefits can be distributed internationally. The page 1 passage stating that benefits should broadly benefit humanity is also available as a shorter alternative.

The final passage choice remains `FLAG TO AUTHOR`.

## 9. United States Concentration Anchor

### What is needed

A figure from the latest Stanford Artificial Intelligence Index industry chapter showing concentration of artificial-intelligence model development, notable models, or private investment by country or firm.

### Source

https://hai.stanford.edu/ai-index-report

The report itself is the likely source. A separate public downloadable dataset has not yet been verified. The IMF 2024 note is an approved alternate only if it contains a usable concentration figure.

## Current Takeover Order

1. Use the SUSB aggregate-band working calculation for United States adoption.
2. Resolve the Global Findex variable definitions and find the Identification for Development identity variable or a labelled administrative alternative.
3. Use the ILOSTAT unemployment-benefit file immediately in the ledger.
4. Find the two payment-program completion reports through TNP2K, J-PAL, ministry reports, or World Bank document identifiers.
5. Use World Development Indicators total population for the allocation ratio and same-year denominator conversion.
6. Decide the fallback wording for the occupation/formality claim if no joint cross-tab is found.
