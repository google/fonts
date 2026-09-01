# Just Me Again Down Here

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Just Me Again Down Here (Regular) built from FontForge SFD sources at https://github.com/librefonts/justmeagaindownhere. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`JustMeAgainDownHere-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- During conversion, stray NUL bytes were stripped from the SFD and the no-break space was given its correct advance width.
- A new Unified Font Repository was created at https://github.com/googlefonts/justmeagaindownhere, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/justmeagaindownhere (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The build matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, and GSUB/GPOS feature sets. The accepted differences are cosmetic or corrective: the FontForge legacy glyph `nonmarkingreturn` was dropped; 21 glyphs were renamed to production names with unchanged coverage; the GDEF table now classifies the combining mark uni0326 that the shipped font had missed; and the private-use combining mark U+F6C3 was zeroed where the shipped font had given it a spacing advance.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/justmeagaindownhere (`.sfd`), latest at commit `63543cec6964e5061ece828c63948d1910e0dbdd`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
