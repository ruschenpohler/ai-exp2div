# Implementation Log

## Status

Source verification is in progress. No memo number is treated as verified until the opened source, denominator, and status are recorded in `docs/parameters_and_sources.md`.

## Decisions

- The external commons-baseline source search follows the approved priority: IMF or United Nations policy note first, then serious academic work only if that category does not yield a usable primary source.
- The DIV memo link is `https://github.com/ruschenpohler/div-returns-aiag`.
- The repository keeps `workplan/` and `impl-plan.md` on disk but excludes them from Git through `.gitignore`.
- No source value has been substituted from memory or from a summary.

## Flags

- The IMF publication page for Cazzaniga et al. (2024) returned HTTP 403 during this pass. The exposure definition, embed-check quote, and exposure figures remain unverified.
- The external commons-baseline source must be opened and quoted before the §1 baseline is drafted.

## Verification order

1. Exposure embed check and gradient.
2. Adoption anchors and diffusion scenario inputs.
3. Composition and cushion indicators.
4. Delivery components and comparator medians.
5. Drafting and final cross-check against script output.
