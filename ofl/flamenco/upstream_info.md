# Flamenco

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Flamenco (Light and Regular) built from FontForge SFD sources at https://github.com/librefonts/flamenco. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD sources (`Flamenco-Light-TTF.sfd` and `Flamenco-Regular-TTF.sfd`) were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- In conversion the non-breaking space advance width was corrected and OS/2 usWeightClass was set to 300 on the Light source.
- A new Unified Font Repository was created at https://github.com/googlefonts/flamenco, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/flamenco (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binaries.

## Verification

Both weights matched the shipped binaries on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 5 glyphs were renamed to their production names in each weight, which leaves cmap coverage unchanged and is therefore accepted (verdict: FUNCTIONAL).

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/flamenco (`.sfd`), latest at commit `908f93e92b13062e172153d04b96a9301ca1c7c5`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
