# Asap Condensed

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: complete
- **Designer**: Omnibus-Type (Pablo Cosgaya, Nicolas Silva)

## Source Data

| Field            | Value |
|------------------|-------|
| repository_url   | https://github.com/Omnibus-Type/Asap |
| commit           | 927ab390d4ece9eaa70a3b16a6124baa9192e34c |
| config_yaml      | sources/config.yaml |
| branch           | master |

## How URL Found

The repository URL `https://github.com/Omnibus-Type/Asap` was already present in METADATA.pb, added by gftools-packager in PR #5492 (merged 2022-11-04 by Rosalie Wagner). The PR commit message explicitly states: "Asap Condensed Version 3.001; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/Omnibus-Type/Asap at commit 927ab39..."

Note: The DESCRIPTION.en_us.html file references a separate repo `Omnibus-Type/AsapCondensed`, which was the old standalone repository for this family. When Asap was upgraded to a variable font with width axis (wdth), the Condensed variant became part of the main `Omnibus-Type/Asap` repo. The METADATA.pb correctly points to the unified Asap repo.

## How Commit Identified

The commit `927ab390d4ece9eaa70a3b16a6124baa9192e34c` ("Font exported", 2022-10-13) was recorded by gftools-packager in PR #5492 and has been in METADATA.pb since the source block was created.

**Verification**: Binary file sizes at this commit match exactly what is in google/fonts:
- AsapCondensed-Black.ttf: 113996 bytes (match)
- AsapCondensed-Bold.ttf: 111544 bytes (match)
- AsapCondensed-Regular.ttf: 110332 bytes (match)
- AsapCondensed-Italic.ttf: 116644 bytes (match)

The commit is the HEAD of master at the time, authored by Emma Marichal. It was the last commit before PR #5492 was merged on 2022-11-04, and no additional upstream commits occurred between 2022-10-13 and the merge date. The commit is confirmed correct.

## How Config Resolved

The `config_yaml: "sources/config.yaml"` field was added by the Batch 1/4 commit (19cdcec59, 2025-03-31) porting data from fontc_crater's targets.json.

The config.yaml at `sources/config.yaml` in the upstream repo builds variable fonts from `Asap.glyphs` and `Asap-Italic.glyphs` with axes `wdth` (width) and `wght` (weight). The width axis includes Condensed (value 75), SemiCondensed (87.5), Normal (100), SemiExpanded (112.5), and Expanded (125). The `buildStatic` option is commented out (`#buildStatic: false`), meaning gftools-builder will generate static instances by default, including the Condensed variants.

The static AsapCondensed TTFs currently in google/fonts were taken as pre-built binaries from the upstream repo's `fonts/ttf/` directory (as documented in the source block's file mappings). The config_yaml reference is primarily for fontc_crater purposes, enabling source-based rebuilds.

**Important architectural note**: Asap is a single-source variable font family that produces multiple Google Fonts families:
- **Asap** (ofl/asap): Served as variable fonts `Asap[wdth,wght].ttf` and `Asap-Italic[wdth,wght].ttf`, now at newer commit `2de32f20`
- **Asap Condensed** (ofl/asapcondensed): Served as 16 static TTFs at width=75, still at commit `927ab39`

Both share the same upstream repo and the same `sources/config.yaml`.

## Conclusion

The source metadata for Asap Condensed is **complete and correct**. The repository URL, commit hash, and config_yaml are all verified. The commit `927ab39` is confirmed as the exact commit used for onboarding via PR #5492, with binary file sizes matching perfectly. The config.yaml at `sources/config.yaml` correctly references the Glyphs sources that include the Condensed width axis.

No changes needed to METADATA.pb.
