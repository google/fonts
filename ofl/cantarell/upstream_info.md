# Cantarell

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Cantarell (Regular, Bold, Italic and BoldItalic) built from FontForge SFD sources at https://github.com/davelab6/cantarell. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD sources were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/cantarell, building the fonts with gftools-builder3 + fontc.
- The vertical metrics were set to the shipped values and the font-level Use Typo Metrics flag was added (babelfont does not propagate the SFD flag).
- uni0302 was forced to the Letter category so it stays a spacing glyph (as shipped) rather than being zeroed as a combining mark.
- An OS/2 WeightClass override (700) was added to Bold and BoldItalic; the BoldItalic master was named so fontc style-links it.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/cantarell (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional parity with the shipped binaries.

## Verification

cmap, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS features and advances match the shipped binaries. The only difference from the shipped binaries is the advance width of the auto-generated .notdef box (748 vs 1024); the SFDs contain no .notdef glyph to control it, and it is never used in real text.

## Original repository (dormant)

The original FontForge sources are at https://github.com/davelab6/cantarell (`.sfd`), latest at commit `52d3363878871c868eaeb64c75a701c1193750af`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
