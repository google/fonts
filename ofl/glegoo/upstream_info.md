# Glegoo

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Glegoo (Regular and Bold) built from FontForge SFD sources at https://github.com/etunni/glegoo. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD sources were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/glegoo, building the fonts with gftools-builder3 + fontc.
- Devanagari mark positioning: babelfont names the below/above anchors generically (DVAnchor0/DVAnchor3), which fontc cannot split into blwm/abvm; the below-base anchors were renamed to bottom so fontc routes below-base marks to blwm (12/12, matching shipped).
- Two dead, shadowed i-matra ligature rules were removed.
- The vertical metrics were set to the shipped values, the Bold master name + an OS/2 WeightClass override (700) were added, and the spacing conjuncts were kept out of the mark category so their advances and mark coverage match shipped.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/glegoo (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional parity with the shipped binaries.

## Verification

cmap, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB features, abvm/blwm mark coverage (40/12) and advance widths all match the shipped binaries. The only difference is a redundant generic `mark` GPOS feature that fontc registers alongside abvm/blwm; it is inert for Devanagari (HarfBuzz applies the Indic abvm/blwm features, not the default mark).

## Original repository (dormant)

The original FontForge sources are at https://github.com/etunni/glegoo (`.sfd`), latest at commit `a6b0a10abfaf1b88feb4a9f9eb731beefbb4bbb8`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
