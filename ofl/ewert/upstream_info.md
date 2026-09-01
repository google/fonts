# Ewert

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Ewert (Regular) built from FontForge SFD sources at https://github.com/librefonts/ewert. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/ewert, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/ewert (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

Matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. Eight glyphs were renamed to their production names; cmap coverage is unchanged, so this difference is benign.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/ewert (`.sfd`), latest at commit `21fa9ed2031b8f7f1bec75cb3f91ad495e3b2370`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
