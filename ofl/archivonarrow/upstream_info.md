# Archivo Narrow

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: complete
- **Designer**: Omnibus-Type (Hector Gatti)

## Source Data

| Field            | Value                                                              |
|------------------|--------------------------------------------------------------------|
| repository_url   | https://github.com/Omnibus-Type/ArchivoNarrow                     |
| commit           | 9793ec77b6682a26bc7a6ed523ca65cc3cb90aec                           |
| config_yaml      | sources/config.yaml                                                |
| branch           | master                                                             |

## How URL Found

The repository URL `https://github.com/Omnibus-Type/ArchivoNarrow` was already present in the METADATA.pb `source` block. It is also referenced in the copyright strings in METADATA.pb and confirmed by the gftools-packager commit message in google/fonts (commit `58d049625`, PR #5559): "Archivo Narrow Version 3.002 taken from the upstream repo https://github.com/Omnibus-Type/ArchivoNarrow".

The cached repo at `Omnibus-Type/ArchivoNarrow` has its remote set to the same URL, confirming consistency.

## How Commit Identified

The commit `9793ec77b6682a26bc7a6ed523ca65cc3cb90aec` was already recorded in METADATA.pb. It is explicitly referenced in the gftools-packager commit message (google/fonts commit `58d049625`, PR #5559): "at commit https://github.com/Omnibus-Type/ArchivoNarrow/commit/9793ec77b6682a26bc7a6ed523ca65cc3cb90aec".

### Verification

The upstream repository contains exactly one commit (`9793ec7`, "Font exported", authored by Emma Marichal on 2022-11-11). This is the initial and only commit, so there is no ambiguity about which commit was used.

Binary file verification confirms an exact match:
- `ArchivoNarrow[wght].ttf`: 93,304 bytes, SHA-256 `adbe027f...` -- identical in both repos
- `ArchivoNarrow-Italic[wght].ttf`: 98,456 bytes, SHA-256 `147c0921...` -- identical in both repos

The google/fonts commit `58d049625` (2022-11-18) shows the font files were copied directly from the upstream repo's `fonts/variable/` directory, and the file sizes in the commit diff match exactly (93,660 -> 93,304 for regular, 98,856 -> 98,456 for italic -- the post-update sizes match the upstream files).

## How Config Resolved

The upstream repo has `sources/config.yaml` at the referenced commit. This is a proper gftools-builder configuration that references two Glyphs source files:

- `ArchivoNarrow.glyphs` (relative to the config file location in `sources/`)
- `ArchivoNarrow-Italic.glyphs` (relative to the config file location in `sources/`)

The config defines the `wght` axis and STAT table entries for both the upright and italic variable fonts. The METADATA.pb correctly records `config_yaml: "sources/config.yaml"`.

No override config.yaml exists in the google/fonts family directory, which is correct since the upstream repo already provides one.

## Conclusion

All source metadata for Archivo Narrow is complete and verified:

- **Repository URL**: Confirmed via gftools-packager commit message and remote URL match
- **Commit hash**: Verified as the only commit in the repository; binary files are byte-identical between upstream and google/fonts
- **Config path**: Upstream `sources/config.yaml` exists with valid gftools-builder configuration referencing `.glyphs` sources
- **Confidence**: HIGH -- single-commit repository with explicit gftools-packager provenance and binary match

No changes needed. The METADATA.pb source block is already complete and accurate.
