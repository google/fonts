# Courgette

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Courgette (Regular) built from FontForge SFD sources at https://github.com/librefonts/courgette. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- During conversion the no-break space (U+00A0) advance width was corrected to match the space glyph.
- A new Unified Font Repository was created at https://github.com/googlefonts/courgette, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/courgette (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binaries.

## Verification

The rebuilt Courgette Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, and GSUB/GPOS feature sets. Remaining differences are benign: 23 glyphs were renamed to production names (coverage unchanged); GDEF now classifies one real combining mark the shipped font missed (uni0326); and one combining mark (U+F6C3) was zeroed after the shipped font left it with a spacing advance. Verdict: FUNCTIONAL parity.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/courgette (`.sfd`), latest at commit `e9638c8874f097c75ff3206c5dfe15b6ef4c67b1`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
