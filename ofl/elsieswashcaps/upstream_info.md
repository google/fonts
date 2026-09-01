# Elsie Swash Caps

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Elsie Swash Caps (Regular and Black) built from FontForge SFD sources at https://github.com/librefonts/elsieswashcaps. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The two canonical FontForge SFD sources were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- During conversion the non-breaking space advance width was corrected in both weights, and the Black weight's OS/2 usWeightClass was set to 900.
- A new Unified Font Repository was created at https://github.com/googlefonts/elsieswashcaps, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/elsieswashcaps (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binaries.

## Verification

Both weights matched the shipped binaries on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference was that 12 glyphs (Black) and 9 glyphs (Regular) were renamed to their production names; coverage is unchanged, so this is cosmetic and does not affect shaping.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/elsieswashcaps (`.sfd`), latest at commit `f48faa350a1a9641bd984b6945f791914a652c65`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
