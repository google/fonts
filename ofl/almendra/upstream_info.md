# Almendra

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Almendra (Regular, Italic, Bold, Bold Italic) built from FontForge SFD sources at https://github.com/librefonts/almendra. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The four canonical FontForge SFD sources (`src/Almendra-*-TTF.sfd`) were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The converted sources were corrected: the italic angle sign was fixed (from -12 to 12) on the italic weights, the no-break space advance width was set, and the usWeightClass of the bold weights was restored to 700.
- A new Unified Font Repository was created at https://github.com/googlefonts/almendra, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/almendra (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binaries.

## Verification

Each weight was compared against its shipped binary and matched on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that some glyphs (10 in the bold, italic and bold-italic weights, 21 in the regular) were renamed to their AGL production names; glyph coverage is unchanged, so this is accepted as benign.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/almendra (`.sfd`), latest at commit `4050b694e01eb3c6083d403d158dfec62f863b5b`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
