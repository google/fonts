# Amiri Quran

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Khaled Hosny, Sebastian Kosch
**METADATA.pb path**: `ofl/amiriquran/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/aliftype/amiri |
| Commit | `480bb746e99ea700bb0d6b4dbf96302d58192103` |
| Config YAML | override config.yaml in google/fonts |
| Branch | main |

## How the Repository URL Was Found

The repository URL `https://github.com/aliftype/amiri` is recorded in the METADATA.pb `source {}` block. The copyright notice in METADATA.pb also references this URL: "Copyright 2010-2022 The Amiri Project Authors (https://github.com/aliftype/amiri)." The cached upstream repo at `aliftype/amiri` confirms the remote matches this URL.

Note: Amiri Quran is part of the broader Amiri font family project. It shares the same upstream repository with the Amiri font family. The font is built from the same `.glyphspackage` source but uses a custom build process involving `scripts/mkquran.py` to produce the Quran-specific variant.

## How the Commit Hash Was Identified

The commit `480bb746e99ea700bb0d6b4dbf96302d58192103` is already recorded in METADATA.pb. Verification confirms:

1. **Commit exists in upstream repo**: Yes, authored by Khaled Hosny on 2025-06-13, with message "1.003". It updated `NEWS.md` for the 1.003 release.
2. **Tag alignment**: This commit is the target of the annotated tag `1.003` in the upstream repo (`git rev-parse "1.003^{commit}"` returns the same hash).
3. **Archive URL consistency**: The archive URL points to `Amiri-1.003.zip`, consistent with the 1.003 release.
4. **google/fonts history**: The font was initially added at this commit via commit `4088c1fa7` by Emma Marichal (2025-07-16), with commit message "Amiri Quran: Version 1.002 added" -- the title says "1.002" but the body explicitly references the 1.003 commit hash. This was a minor error in the commit message title. A follow-up commit `3c5672f8a` ("push version 1.003") corrected the archive_url from 1.002 to 1.003 and fixed the filename. A further commit `087c433c9` corrected the `files {}` paths to use the `Amiri-1.003/` prefix matching the archive structure.
5. **Pre-built binary**: The binary `fonts/AmiriQuran.ttf` exists at this commit in the upstream repo. The METADATA.pb uses `archive_url` to pull the pre-built binary from the GitHub release zip rather than building from source.

The commit hash is correct and matches the 1.003 release tag.

## How Config YAML Was Resolved

The upstream repository does **not** have a `config.yaml` file at the referenced commit (or at HEAD). The Amiri project uses a custom build system via `Makefile` and `scripts/build.py` (using `ufo2ft` directly) rather than gftools-builder.

A local override `config.yaml` was added to `ofl/amiriquran/` in the google/fonts repository by commit `f6c68379a` (2026-02-16, "Add override config.yaml for 50 font families"). The override contains:

```yaml
sources:
  - sources/Amiri.glyphspackage
familyName: Amiri Quran
buildStatic: true
buildOTF: false
```

This override points to the `.glyphspackage` source file that exists in the upstream repo at the referenced commit. Since the override config.yaml exists locally in google/fonts, no `config_yaml` field is needed in METADATA.pb (google-fonts-sources auto-detects local overrides).

**Important caveat**: The override config may not produce an identical binary to the original. The upstream project uses a highly customized build pipeline (`scripts/build.py` for initial compilation + `scripts/mkquran.py` for Quran-specific processing). The override config.yaml points gftools-builder at the `.glyphspackage` source, but gftools-builder will not replicate the custom Quran-specific processing steps (e.g., the color glyph removal, Quran-specific mark positioning, etc.). The binary currently served from google/fonts was taken from the pre-built release archive, not built from source via gftools-builder.

## Conclusion

The source metadata for Amiri Quran is **complete**. The repository URL is correct, the commit hash matches the 1.003 release tag, and a local override config.yaml exists in google/fonts. The font binary was sourced from the upstream GitHub release archive (pre-built), not compiled via gftools-builder. The override config.yaml enables fontc_crater discovery but may not reproduce the exact same binary due to the project's custom build pipeline.
