# Give You Glory

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Give You Glory (Regular) built from FontForge SFD sources at https://github.com/librefonts/giveyouglory. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge source (`src/GiveYouGlory-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`); glyphs were given production names during conversion.
- A new Unified Font Repository was created at https://github.com/googlefonts/giveyouglory, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/giveyouglory (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The freshly built Give You Glory Regular was compared against the shipped `GiveYouGlory.ttf`. It matched on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets and advance widths. Two accepted differences remain: 18 glyphs were renamed to production names (coverage unchanged), and the new GDEF correctly classifies one combining mark (uni0326) that the shipped font had left unclassified.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/giveyouglory (`.sfd`), latest at commit `2787317ad77bac728fea1ca0c4ce7f0d3ba273d5`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
