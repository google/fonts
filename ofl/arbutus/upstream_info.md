# Arbutus

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Arbutus (Regular) built from FontForge SFD sources at https://github.com/librefonts/arbutus. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- During conversion the no-break space (U+00A0) advance width was corrected to 838 to match the space glyph.
- A new Unified Font Repository was created at https://github.com/googlefonts/arbutus, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/arbutus (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binaries.

## Verification

The rebuilt Arbutus Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets and advance widths. Remaining differences are benign: 22 glyphs were renamed to production names (coverage unchanged), and GDEF now classifies one real combining mark the shipped font missed (uni0326). Verdict: FUNCTIONAL parity.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/arbutus (`.sfd`), latest at commit `413fe5b2122e7a4d1ce6c604000f368a6bf8f6ac`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
