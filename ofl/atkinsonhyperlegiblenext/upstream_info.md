# Atkinson Hyperlegible Next

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: complete
- **Designer**: Braille Institute, Applied Design Works, Elliott Scott, Megan Eiswerth, Letters From Sweden

## Source Data

| Field            | Value                                                              |
|------------------|--------------------------------------------------------------------|
| repository_url   | https://github.com/googlefonts/atkinson-hyperlegible-next          |
| commit           | 7925f50f649b3813257faf2f4c0b381011f434f1                           |
| branch           | main                                                               |
| config_yaml      | sources/config.yaml                                                |

## How URL Found

The repository URL was already present in METADATA.pb at the time of onboarding (commit `66eef707` by Emma Marichal on 2025-01-07). The copyright string in the font files also references `https://github.com/googlefonts/atkinson-hyperlegible-next`. The URL is confirmed valid -- the remote in the cached repo matches, and the GitHub API is accessible.

## How Commit Identified

**Original onboarding commit**: Emma Marichal onboarded this family via PR #8813 on 2025-01-07, referencing upstream commit `5d633f80fc654ef5fffa7cfc257528685158dcef`. The PR body and commit message both state: "Taken from the upstream repo https://github.com/googlefonts/atkinson-hyperlegible-next at commit 5d633f80fc654ef5fffa7cfc257528685158dcef."

**Updated commit**: The Batch 1/4 metadata update (commit `19cdcec5` by Felipe Sanches on 2025-03-31) changed the commit hash from `5d633f80` to `7925f50f649b3813257faf2f4c0b381011f434f1`, which is the latest commit on main as of that date ("Fix Cairo in CI" by Simon Cozens, 2025-02-21). This update was sourced from the fontc_crater targets file, which lists `7925f50` as the revision.

**Binary verification**: The font binaries in google/fonts match those at commit `7925f50` exactly (SHA256 verified):
- `AtkinsonHyperlegibleNext[wght].ttf`: `5a455d1cfa099b601ab70751bb9673e8fe1854dc` (114,552 bytes)
- `AtkinsonHyperlegibleNext-Italic[wght].ttf`: `ce9cffed32742ad2d9238c561a93220385e5934c` (123,916 bytes)

The "Fix Cairo in CI" commit only modified CI configuration (`.github/workflows/build.yaml`), not font sources or binaries. The pre-built variable TTF files in `fonts/variable/` are identical between both upstream commits, so `7925f50` is a valid reference for the binary files in google/fonts.

## How Config Resolved

The upstream repository contains `sources/config.yaml` at the referenced commit. This file configures gftools-builder with:
- Two Glyphs sources: `AtkinsonHyperlegibleNext.glyphs` and `AtkinsonHyperlegibleNext-Italic.glyphs`
- Family name: "Atkinson Hyperlegible Next"
- Weight axis (wght) with values 200-800
- STAT table configuration for both Roman and Italic variable fonts

The `config_yaml` field was added to METADATA.pb during the Batch 1/4 update. No local override config.yaml exists in the google/fonts family directory, as the upstream config is sufficient.

## Conclusion

The source metadata for Atkinson Hyperlegible Next is **complete** and **correct**. All fields are present in METADATA.pb:

- `repository_url` points to a valid GitHub repository under googlefonts
- `commit` (`7925f50`) references the latest upstream commit at the time of the Batch 1/4 update; the font binaries are byte-identical to those in google/fonts
- `config_yaml` correctly points to `sources/config.yaml` in the upstream repo
- `branch` is set to `main`
- The `files` block correctly maps `fonts/variable/*.ttf` and `OFL.txt` from upstream

No corrections needed. The original onboarding commit `5d633f80` and the current reference `7925f50` both contain identical font binaries; the only difference between them is a CI fix that does not affect the fonts.
