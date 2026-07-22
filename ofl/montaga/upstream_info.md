# Montaga

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Montaga (Regular) built from FontForge SFD sources at https://github.com/librefonts/montaga. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`src/Montaga-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The non-breaking space (U+00A0) glyph handling was normalized during conversion.
- A new Unified Font Repository was created at https://github.com/googlefonts/montaga, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/montaga (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

The build matched the shipped Montaga-Regular.ttf on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 9 glyphs carry their canonical production names (coverage unchanged), which is why the verdict is FUNCTIONAL rather than byte-for-byte identical.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/montaga (`.sfd`), latest at commit `1c439c4e7d38e452718e8e67834c810641d1685a`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
