# Ranga

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Ranga (Regular and Bold) built from FontForge SFD sources at https://github.com/antonxheight/Ranga. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD sources were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/Ranga, building the fonts with gftools-builder3 + fontc.
- Source FEA fixes: a dangling glyph reference (shadeva_viramadeva_alt, a typo for the existing shadeva_viramadeva.alt) was corrected, and two dead, shadowed ligature rules were removed.
- Devanagari mark positioning: the below-base anchors (named DVAnchor0 by babelfont) were renamed to bottom so fontc routes below-base marks to blwm (12/12).
- The vertical metrics were set to the shipped values, the Bold master name + an OS/2 WeightClass override (700) were added, and the spacing conjuncts were kept out of the mark category so their advances and mark coverage match shipped.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/Ranga (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional parity with the shipped binaries.

## Verification

cmap, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB features, abvm/blwm mark coverage (37/12) and advance widths all match the shipped binaries. The only difference is a redundant generic `mark` GPOS feature that fontc registers alongside abvm/blwm; it is inert for Devanagari (HarfBuzz applies the Indic abvm/blwm features, not the default mark).

## Original repository (dormant)

The original FontForge sources are at https://github.com/antonxheight/Ranga (`.sfd`), latest at commit `15fadcc52c...`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
