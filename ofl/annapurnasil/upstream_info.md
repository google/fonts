# Annapurna SIL

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: Complete (with note on commit hash)
- **Designer**: SIL International

## Source Data

| Field            | Value |
|------------------|-------|
| repository_url   | `https://github.com/silnrsi/font-annapurna` |
| commit           | `5bd915dff1934cf36041d7766784347713c812a3` |
| archive_url      | `https://github.com/silnrsi/font-annapurna/releases/download/v2.000/AnnapurnaSIL-2.000.zip` |
| branch           | `master` |
| config_yaml      | (omitted -- override config.yaml in google/fonts) |

## How URL Found

The repository URL `https://github.com/silnrsi/font-annapurna` was already present in METADATA.pb. It was originally recorded in the `upstream.yaml` created by gftools-packager in PR #7204 (commit `06fa5749a`), authored by Emma Marichal on 2024-01-19. The commit message explicitly states: "Annapurna SIL Version 2.000 taken from the upstream repo https://github.com/silnrsi/font-annapurna". The URL is confirmed valid; the cached repo at `upstream_repos/fontc_crater_cache/silnrsi/font-annapurna` has remote origin matching this URL.

## How Commit Identified

The commit hash `5bd915dff1934cf36041d7766784347713c812a3` was already in METADATA.pb (added in commit `1158b8da5` on 2025-12-12 by Felipe Sanches as part of a sources info update).

**Important nuance about this commit**: The gftools-packager onboarding commit (`06fa5749a`) has a broken commit URL (`https://github.com/silnrsi/font-annapurna/commit/` with no hash), so the original packager run did not record the specific commit. The fonts were taken from the v2.000 release archive (prebuilt TTFs), not built from source.

The referenced commit `5bd915d` (2023-11-09) is titled "Bumped version to 2.001; replace reference fonts with 2.000". This is one commit AFTER the `v2.000` tag (`76733a2`, 2023-11-08). The differences between v2.000 and `5bd915d` are:
- Version bump from 2.000 to 2.001 in fontinfo.plist files
- Reference font replacements (binary files in `references/` directory)
- Minor metadata updates (WOFF metadata, wscript, preflight)

Since the fonts in Google Fonts are version 2.000 (from the release archive), the v2.000 tag (`76733a2`) would be the most precise match for the actual font binaries. However, the commit `5bd915d` is only one commit later, with source changes limited to version bumping -- the actual glyph data and design are identical. This is acceptable for source metadata purposes, as the designspace and UFO glyph data are unchanged between these two commits.

## How Config Resolved

The upstream repository does **not** have a `config.yaml` file -- not at the referenced commit, not at HEAD, and not at any point in its history. The repo uses SIL's own build system (`wscript` / `smith`) rather than gftools-builder.

However, the sources are gftools-builder compatible: the repo contains `source/AnnapurnaSIL-RB.designspace` with two UFO sources (`AnnapurnaSIL-Regular.ufo` and `AnnapurnaSIL-Bold.ufo`), defining a weight axis (400-700, Regular and Bold).

An override `config.yaml` exists at `ofl/annapurnasil/config.yaml` in google/fonts with the following content:

```yaml
buildVariable: false
sources:
  - source/AnnapurnaSIL-RB.designspace
```

This is appropriate:
- `buildVariable: false` -- correct, since Google Fonts serves this family as static instances (Regular 400 + Bold 700), not as a variable font
- The designspace path `source/AnnapurnaSIL-RB.designspace` correctly references the file that exists at the referenced commit

Because the override config.yaml is in the google/fonts family directory, the `config_yaml` field is correctly omitted from the METADATA.pb `source {}` block (google-fonts-sources auto-detects local overrides).

## Conclusion

The source metadata for Annapurna SIL is **complete**. The repository URL is verified, the commit hash points to a valid commit one step after v2.000 (acceptable for source tracking), and the override config.yaml correctly configures gftools-builder for static font generation from the upstream designspace. The original onboarding (PR #7204, merged 2024-01-25 by Viviana Monsalve) used prebuilt fonts from the v2.000 release archive rather than building from source. No changes to METADATA.pb are needed.
