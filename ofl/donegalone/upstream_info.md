# Donegal One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

Sources rebuilt 2026-09: the 2026-07 conversion was back-fitted (post-conversion scripts copied values out of the shipped binary) and carried undocumented source edits. The upstream repository now carries an explicit commit series: the `.sfd` restored byte-identical from the repository's own history, each documented edit (version bump, metric or naming correction) as its own commit with its justification, then the conversion to `.glyphs`. METADATA.pb references the conversion commit `1789bdc47a76`; diffenator3 1.1.4 reports zero glyph, word and pixel differences against the shipped binaries on every style.

## Initial state

Google Fonts shipped Donegal One (Regular) built from FontForge SFD sources at https://github.com/librefonts/donegalone. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The converted source was corrected: the `aalt` feature was rebuilt, and the no-break space (U+00A0) advance width was fixed to 684.
- A new Unified Font Repository was created at https://github.com/googlefonts/donegalone, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/donegalone (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binaries.

## Verification

The rebuilt font matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle and GSUB/GPOS feature sets, and had no blocking differences. Three benign differences were accepted:

- 27 glyphs were renamed to production names; cmap coverage is unchanged.
- GDEF now classifies U+0326 (combining comma below) as a mark, which the shipped font failed to classify. This is a correction.
- The combining mark at U+F6C3 was given a zero advance; the shipped font gave it a spacing advance.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/donegalone (`.sfd`), latest at commit `b0af18fd94255bfdfe07e90db984167564abd565`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
