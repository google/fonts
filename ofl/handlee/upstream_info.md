# Handlee

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Handlee (Regular) built from FontForge SFD sources at https://github.com/librefonts/handlee. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`src/Handlee-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/handlee, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/handlee (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

The fontc build matched the shipped Handlee-Regular.ttf on every dimension checked, with two accepted differences: two legacy FontForge helper glyphs (`.null` and `nonmarkingreturn`) were dropped, and one glyph was renamed to its production name. Both leave the Unicode cmap coverage unchanged, so rendering is unaffected.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/handlee (`.sfd`), latest at commit `d937cfc17b0389d9847b8a865060b7241af7c654`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
