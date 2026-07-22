# Goblin One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Goblin One (Regular) built from FontForge SFD sources at https://github.com/librefonts/goblinone. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source `src/GoblinOne-TTF.sfd` was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The no-break space (U+00A0) advance width was corrected to 618 to match the space glyph.
- A new Unified Font Repository was created at https://github.com/googlefonts/goblinone, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/goblinone (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

The rebuilt font matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets and advance widths. Two benign differences were accepted: 8 glyphs were renamed to production names (coverage unchanged), and GDEF correctly classifies the combining mark uni0326 that the shipped font had failed to mark.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/goblinone (`.sfd`), latest at commit `446c2b743e1eda33533ad624c543cfd623eb7c90`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
