# Chango

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

The family shipped from a FontForge project (`src/Chango-Regular-TTF.sfd`) with no gftools-builder configuration. METADATA.pb pointed at the librefonts repository but recorded no config_yaml, so the family could not be rebuilt with the current pipeline.

## Actions taken

The repository adopted the Unified Font Repository template. The FontForge source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`), producing `sources/Chango-Regular.glyphs`, and a gftools-builder configuration was added. The no-break space (U+00A0) advance width was corrected to 400 to match the space glyph. The superseded FontForge sources and legacy build cruft were retired.

## Final state

The repository builds Chango Regular from the `.glyphs` source with gftools-builder3 and fontc, driven by its build configuration.

## Verification

The freshly built Chango Regular was compared against the binary currently shipped in Google Fonts. Glyph coverage, metrics and layout matched; the verdict was FUNCTIONAL with only benign differences:

- The FontForge legacy glyph `nonmarkingreturn` was dropped (FontForge synthesised it at export time; it carries no rendering meaning).
- 13 glyphs were renamed to their AGL production names; coverage was unchanged.
- The GDEF table now classifies two real combining marks that the shipped font missed (U+0307, U+0326).
- One combining mark (U+0307) was zero-width, whereas the shipped font gave it a spacing advance.

No blocking differences were found.

## Original repository (dormant)

Original upstream: https://github.com/librefonts/chango
Latest commit: ca58222d6319223db35d6e76052ef9a78cca43f7 (branch `master`)
