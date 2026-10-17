# Noto Sans Telugu UI — Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/googlefonts/noto-fonts |
| Commit | `1b5d974daaa002333b2a5a068d0a7f2d1121b3b7` |
| Version | 2.001 |
| Onboarding PR | [google/fonts#2823](https://github.com/google/fonts/pull/2823) |
| Date | 2021-01-13 |

## Investigation Summary

Noto Sans Telugu UI is a UI variant of Noto Sans Telugu, onboarded as part of the large December 25, 2020 Noto batch via PR #2823. The font binary was sourced from the googlefonts/noto-fonts monorepo at commit `1b5d974daaa002333b2a5a068d0a7f2d1121b3b7`.

The commit was verified by blob-hash comparison: the font binary blob hash at this commit in the googlefonts/noto-fonts monorepo matches the blob added to google/fonts in PR #2823 (commit a559a6efc).

**Note**: UI variant. Dec 25 2020 batch.

**Confidence**: HIGH (blob-verified)

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, copied from `sources/config-sans-telugu.yaml` in the `notofonts/telugu` repository (the current per-script Noto repo). **Important caveat**: this config references the current notofonts/ per-script repo sources, which may produce a newer version than the binary currently shipped in google/fonts. The shipped binary was built from the older `googlefonts/noto-fonts` monorepo using a different build pipeline. This override config serves as a starting point for reproducible build attempts but is not expected to produce a byte-identical match.


## Source-metadata correction (2026-06-02) — ⚠ REFRESH REQUIRED

**Model**: Claude Opus 4.8

fontc_crater reported a `missing source` failure for this family because the `repository_url` pointed at the deprecated `googlefonts/noto-fonts` monorepo, which no longer contains the Glyphs/glyphspackage sources (only built binaries). The sources now live in the per-script repo.

Corrected the METADATA.pb source block:
- repository_url: `https://github.com/googlefonts/noto-fonts` → `https://github.com/notofonts/telugu`
- commit: `1b5d974daaa002333b2a5a068d0a7f2d1121b3b7` → `0d8cb2a9550d76f4349915664f1115ea4c42f4ed` (2022-07-05)

The declared source is confirmed present at the new commit.

**⚠ REFRESH REQUIRED — this does NOT reproduce the shipped binary.** The per-script Noto repos postdate the 2021-01-13 onboarding of the shipped binary, so the source now resolves and the family becomes buildable, but a rebuild produces an **updated** font, not the originally-shipped artifact. Before shipping any rebuild, a human must QA the output for reflow / vertical-metric / glyph-coverage / version differences. The original build provenance (the exact source + commit that produced the shipped binary) is not recoverable from the current upstream.
