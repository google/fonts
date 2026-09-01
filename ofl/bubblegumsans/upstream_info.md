# Bubblegum Sans

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Bubblegum Sans (Regular) built from FontForge SFD sources at https://github.com/librefonts/bubblegumsans. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A non-breaking space (U+00A0) was added to the source, matching the glyph that FontForge used to synthesise at export time.
- A new Unified Font Repository was created at https://github.com/googlefonts/bubblegumsans, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/bubblegumsans (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

The rebuilt Bubblegum Sans Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. Remaining differences are benign: 7 glyphs renamed to production names (coverage unchanged), and two FontForge legacy glyphs (`.null`, `nonmarkingreturn`) dropped as they carry no encoded characters. Verdict: FUNCTIONAL parity.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/bubblegumsans (`.sfd`), latest at commit `fcf8bdd5e83b65186641b2b67fd957ff061666e3`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
