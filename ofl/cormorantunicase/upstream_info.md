# Cormorant Unicase - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Cormorant Unicase |
| Repository URL | https://github.com/CatharsisFonts/Cormorant |
| Commit Hash | `cc1bfb51ce6568cb3abf9199ab718d543f6fa189` |
| Branch | master |
| Config YAML | `sources/build.yaml` (in METADATA.pb) |
| Override Config | No |
| Status | complete |

## How URL Found

The repository URL was already documented in the METADATA.pb `source` block. It was added as part of the gftools-packager onboarding in PR #4893 (July 2022). The copyright strings in the font files also reference `github.com/CatharsisFonts/Cormorant`.

## How Commit Determined

The commit hash `cc1bfb51ce6568cb3abf9199ab718d543f6fa189` is explicitly stated in the gftools-packager commit message:

> Cormorant Unicase Version 4.000 taken from the upstream repo https://github.com/CatharsisFonts/Cormorant at commit https://github.com/CatharsisFonts/Cormorant/commit/cc1bfb51ce6568cb3abf9199ab718d543f6fa189.

This commit in the upstream repo is a merge commit from May 14, 2022: "Merge pull request #67 from m4rc1e/gf-mastering - v4.000 mastered for Google Fonts".

## Config YAML Status

**Issue identified**: The METADATA.pb records `config_yaml: "sources/build.yaml"`, but this config file is for the main Cormorant family (`familyName: Cormorant`), not for Cormorant Unicase. The `build.yaml` references `Cormorant.glyphs` and `Cormorant-Italic.glyphs` only.

At the recorded commit `cc1bfb51`, there was no dedicated config file for Cormorant Unicase. The Unicase fonts were pre-built TTFs taken directly from `fonts/ttf/CormorantUnicase-*.ttf`.

A proper `sources/config-unicase.yaml` was added later in commit `8378c19c` (November 13, 2024), which references `sources/generated/CormorantUnicase.glyphs` - a file that is generated from `Cormorant.glyphs` via babelfont.

The Cormorant Unicase build is complex: `CormorantUnicase.glyphs` is a generated source created by applying instance parameters from `Cormorant.glyphs` with babelfont filtering (see Makefile line 33-34).

## Verification

- **Commit exists in upstream**: Verified. `cc1bfb51` is present in the CatharsisFonts/Cormorant repository.
- **Font files exist at commit**: Verified. `fonts/ttf/CormorantUnicase-{Bold,Light,Medium,Regular,SemiBold}.ttf` all exist at this commit.
- **File mappings match**: The METADATA.pb `files` entries map `fonts/ttf/CormorantUnicase-*.ttf` to the google/fonts directory, consistent with the upstream.yaml from PR #4893.

## Confidence Level

**High** for repository URL and commit hash. The commit is explicitly documented in the packager commit message and PR body.

**Low** for config_yaml. The `sources/build.yaml` is for the main Cormorant family, not for Unicase. This is a known issue that should ideally be corrected to either remove the config_yaml field (since the fonts were pre-built TTFs at this commit) or update to point to `sources/config-unicase.yaml` with a more recent commit that includes that file.

## Open Questions

1. Should the `config_yaml` field be removed from the METADATA.pb source block since the Unicase fonts were pre-built TTFs at the recorded commit (no config.yaml existed for Unicase at `cc1bfb51`)?
2. Alternatively, should the commit be updated to a newer one (post `8378c19c`) that includes `sources/config-unicase.yaml`?
