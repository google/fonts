# Autour One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Autour One (Regular) built from FontForge SFD sources at https://github.com/librefonts/autourone. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`AutourOne-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- During conversion the no-break space (U+00A0) advance width was corrected to match the space glyph (847).
- A new Unified Font Repository was created at https://github.com/googlefonts/autourone, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/autourone (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binaries.

## Verification

The rebuilt font matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle and the GSUB/GPOS feature sets. Three benign differences were accepted: 26 glyphs were renamed to their AGL production names (glyph coverage unchanged); GDEF now classifies U+0326 as a combining mark, which the shipped font had missed; and the combining glyph U+F6C3 was zeroed, whereas the shipped font gave it a spacing advance.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/autourone (`.sfd`), latest at commit `10ccd1eb5ad3e7088ce2dd099debff0ac08daf1c`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
