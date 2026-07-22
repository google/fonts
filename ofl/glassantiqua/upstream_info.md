# Glass Antiqua

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

The upstream repository shipped only FontForge `.sfd` sources and had no gftools-builder configuration. METADATA.pb pointed at the librefonts mirror with an onboarding commit but no `config_yaml`, so the family could not be rebuilt with the current Google Fonts pipeline.

## Actions taken

The single FontForge source `src/GlassAntiqua-Regular-TTF.sfd` was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`), producing `sources/GlassAntiqua-Regular.glyphs`. A gftools-builder configuration was added and the repository was restructured to the Unified Font Repository template. The superseded `.sfd` sources and legacy build cruft were retired. No further source corrections were required beyond the conversion.

## Final state

The repository builds `GlassAntiqua-Regular.ttf` from the converted `.glyphs` source through gftools-builder3 and fontc.

## Verification

The freshly built binary was compared against the shipped `GlassAntiqua-Regular.ttf`. The verdict was FUNCTIONAL: character coverage, metrics and outlines matched. The only difference was that 15 glyphs were renamed to their standard production names; the set of encoded characters is unchanged, so the rename is cosmetic and does not affect rendering.

## Original repository (dormant)

The original sources lived at https://github.com/librefonts/glassantiqua, whose latest commit was `ccc1839b05e9827b7f3a1439d089952908cd0334` on the `master` branch. That repository carried only the FontForge `.sfd` sources and remains preserved as the historical record.
