# Inika

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Inika (Regular and Bold) built from FontForge SFD sources at https://github.com/librefonts/inika. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The two canonical FontForge SFD sources (Regular and Bold) were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The Bold source's OS/2 usWeightClass was set to 700 to match the shipped binary.
- A new Unified Font Repository was created at https://github.com/googlefonts/inika, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/inika (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binaries.

## Verification

Both weights matched the shipped binaries on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 10 glyphs per weight were renamed to production names; glyph coverage is unchanged.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/inika (`.sfd`), latest at commit `bccbe87bf5a91ebb43d149cd786cdabde71c8e52`. Preserved for provenance; the new `.glyphs` sources supersede them for building.
