# Esteban

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

Sources rebuilt 2026-09: the 2026-07 conversion was back-fitted (post-conversion scripts copied vertical metrics, GDEF classes and other values out of the shipped binary). The sources were regenerated purely from the original FontForge `.sfd`, byte-identical to the repository's own history, with babelfont `c368660` (gftools-builder3 `17b215c5` + fontc `3518040e`, 0.6.0); diffenator3 1.1.4 reports zero glyph, word and pixel differences against the shipped binaries on every style. METADATA.pb now references the rebuild commit `c268b4f87279`.

## Initial state

Google Fonts shipped Esteban (Regular) built from FontForge SFD sources at https://github.com/librefonts/esteban. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`src/Esteban-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/esteban, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/esteban (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

Identical to the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 7 glyphs were renamed to production (AGL) names; glyph coverage is unchanged, so this is a functional equivalence.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/esteban (`.sfd`), latest at commit `35e274d49210b9c8a7864689b48d6156e6be6bbf`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
