# Atkinson Hyperlegible Mono

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: complete

## Designer

Braille Institute, Applied Design Works, Elliott Scott, Megan Eiswerth, Letters From Sweden

## Source Data

| Field            | Value |
|------------------|-------|
| Repository URL   | https://github.com/googlefonts/atkinson-hyperlegible-next-mono |
| Commit           | `154d50362016cc3e873eb21d242cd0772384c8f9` |
| Config YAML      | `sources/config.yaml` (in upstream repo) |
| Branch           | main |
| Date Added       | 2024-11-20 |

## How URL Found

The repository URL `https://github.com/googlefonts/atkinson-hyperlegible-next-mono` was already present in METADATA.pb from the original onboarding commit `a4ccc36e5` ("Atkinson Hyperlegible Mono: Version 2.001 added") by Emma Marichal on 2024-11-20. The copyright string in the font files also references this repository. The URL is confirmed valid, and the cached clone at `googlefonts/atkinson-hyperlegible-next-mono` has a matching remote origin.

## How Commit Identified

The commit `154d503` was explicitly referenced in the onboarding commit message in google/fonts:

> Taken from the upstream repo https://github.com/googlefonts/atkinson-hyperlegible-next-mono at commit https://github.com/googlefonts/atkinson-hyperlegible-next-mono/commit/154d50362016cc3e873eb21d242cd0772384c8f9.

This commit is the **only commit** in the upstream repository (the initial commit titled "last fixes" by Emma Marichal, dated 2024-11-20). Therefore, there is no ambiguity -- there are no earlier or later commits to consider.

Binary file sizes match exactly between the upstream commit and google/fonts:
- `AtkinsonHyperlegibleMono[wght].ttf`: 53,960 bytes (both)
- `AtkinsonHyperlegibleMono-Italic[wght].ttf`: 56,364 bytes (both)

The METADATA.pb `source.files` entries correctly map `fonts/variable/*.ttf` from the upstream repo to the google/fonts family directory.

## How Config Resolved

The upstream repo has `sources/config.yaml` at the referenced commit, containing gftools-builder configuration for two Glyphs sources:
- `AtkinsonHyperlegibleMono.glyphs`
- `AtkinsonHyperlegibleMono-Italic.glyphs`

The config includes axis order (`wght`, `ital`), STAT table definitions, and cleanup settings. The `config_yaml: "sources/config.yaml"` field was added to METADATA.pb by the "Batch 1/4" commit (`19cdcec5`) which ported info from fontc_crater targets list. No override config.yaml exists in the google/fonts family directory, and none is needed since the upstream repo has its own.

## Conclusion

This family's source metadata is **complete and correct**. The repository URL, commit hash, and config.yaml path are all present in METADATA.pb. The commit is verified as the only commit in the upstream repo, with binary file sizes matching exactly. The config.yaml in the upstream repo provides valid gftools-builder configuration pointing to two `.glyphs` source files. No action required.
