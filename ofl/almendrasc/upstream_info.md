# Almendra SC

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Almendra SC (Regular) built from FontForge SFD sources at https://github.com/librefonts/almendrasc. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`AlmendraSC-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/almendrasc, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/almendrasc (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The fontc build was compared against the shipped AlmendraSC-Regular.ttf and matched on vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. Two benign differences were accepted:

- The new cmap covers one additional codepoint: the no-break space (U+00A0), which the Glyphs source encodes explicitly whereas FontForge used to synthesise it at export time.
- Nine glyphs were renamed to their production names; codepoint coverage is unchanged.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/almendrasc (`.sfd`), latest at commit `35906cd6a26df27bef8081669638fbae0382c7fc`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
