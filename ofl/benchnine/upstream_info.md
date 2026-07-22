# BenchNine

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped BenchNine (Light, Regular, Bold) built from FontForge SFD sources at https://github.com/librefonts/benchnine. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The three canonical FontForge SFD sources (Light, Regular, Bold) were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The converted sources were corrected: the no-break space (U+00A0) advance widths were set, the usWeightClass values were restored (300 Light, 700 Bold), and Use Typo Metrics was enabled.
- A new Unified Font Repository was created at https://github.com/googlefonts/benchnine, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/benchnine (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at full equivalence with the shipped binaries.

## Verification

Each weight was built and compared against its shipped Google Fonts binary. All three (Light, Regular, Bold) matched on every dimension checked: cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. Verdict: FULL parity.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/benchnine (`.sfd`), latest at commit `0b2979e19186f9b477fd3bde7ae77932933707eb`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
