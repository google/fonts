# Gravitas One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

Sources rebuilt 2026-09: the 2026-07 conversion was back-fitted (post-conversion scripts copied vertical metrics, GDEF classes and other values out of the shipped binary). The sources were regenerated purely from the original FontForge `.sfd`, byte-identical to the repository's own history, with babelfont `c368660` (gftools-builder3 `17b215c5` + fontc `3518040e`, 0.6.0); diffenator3 1.1.4 reports zero glyph, word and pixel differences against the shipped binaries on every style. METADATA.pb now references the rebuild commit `8eb45dc3e5bd`.

## Initial state

Google Fonts shipped Gravitas One (Regular) built from FontForge SFD sources at https://github.com/librefonts/gravitasone. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`src/GravitasOne-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`). Stray NUL bytes in the SFD were stripped during conversion.
- A new Unified Font Repository was created at https://github.com/googlefonts/gravitasone, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/gravitasone (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The rebuilt font matched the shipped `GravitasOne.ttf` on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets and advance widths. Two benign differences were accepted: 7 glyphs were renamed to their production (AGL) names with no change in coverage, and the new build's GDEF correctly classifies `uni0326` as a combining mark, a classification the shipped font omitted.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/gravitasone (`.sfd`), latest at commit `c89d142ad0f695ba267d27965c26d1dd75463f20`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
