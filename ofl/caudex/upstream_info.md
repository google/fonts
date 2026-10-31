# Caudex

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Caudex (Regular, Bold, Italic and BoldItalic) built from FontForge SFD sources at https://github.com/librefonts/caudex. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD sources were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/caudex, building the fonts with gftools-builder3 + fontc.
- Two duplicate glyphs (Ldot/ldot, defined twice in the SFDs, canonical + a PUA copy) were renamed Ldot.1/ldot.1, matching the canonical Google Fonts pipeline; this also avoids a fontc scheduler hang on duplicate glyph names.
- An OS/2 WeightClass override (700) was added to Bold and BoldItalic.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/caudex (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional parity with the shipped binaries.

## Verification

cmap, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS features and advances match the shipped binaries. The build classifies the Latin combining marks in GDEF, which the older ufo2ft-built shipped binary left unclassified; Caudex has no mark-positioning GPOS feature, so this is inert and the build is simply more correct.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/caudex (`.sfd`), latest at commit `901fb15160f96cb5a2b91e48a6d89d9c18c6f6d5`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
