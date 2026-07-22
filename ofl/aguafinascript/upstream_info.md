# Aguafina Script

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Aguafina Script (Regular) built from FontForge SFD sources at https://github.com/librefonts/aguafinascript. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`AguafinaScript-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- U+00A0 (no-break space) was added to the converted source, since FontForge used to synthesise it at export time, and a few stray NUL bytes were stripped from the source.
- A new Unified Font Repository was created at https://github.com/googlefonts/aguafinascript, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/aguafinascript (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The rebuilt Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 6 glyphs were renamed to their production names; character coverage is unchanged, so the rename is cosmetic and does not affect rendering.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/aguafinascript (`.sfd`), latest at commit `45a8ce768b4cca138c10ff7a7a9f55778fd02c9d`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
