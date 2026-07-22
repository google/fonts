# Lusitana

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Lusitana (Regular and Bold) built from FontForge SFD sources at https://github.com/librefonts/lusitana. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD sources were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The Bold source's OS/2 usWeightClass was set to 700, which the conversion had not preserved.
- A new Unified Font Repository was created at https://github.com/googlefonts/lusitana, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/lusitana (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binaries.

## Verification

The rebuilt Regular and Bold matched the shipped binaries on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 4 glyphs in each weight were renamed to their production names; character coverage is unchanged, so this is benign.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/lusitana (`.sfd`), latest at commit `8fa070c2ac2963f13feee142e2001777ac48e774`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
