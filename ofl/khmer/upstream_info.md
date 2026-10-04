# Khmer — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [danhhong/Khmer](https://github.com/danhhong/Khmer) |
| Commit | `d72e92059891c386fa3e8851948ac042ba947f0e` |
| Date | 2021-01-23 |
| Confidence | High |

## Investigation

The METADATA.pb for Khmer had no source block. The upstream repository was identified as danhhong/Khmer, maintained by designer Danh Hong (credited in the font's copyright notice).

### Source Types Available

- **TTF only**: `Khmer-Bold.ttf`, `Khmer-Regular.ttf`
- No editable source files (no SFD, UFO, Glyphs, or VFB)

### Buildability

The repository contains only compiled TTF binary fonts. No editable design sources are present. Not buildable with gftools-builder or any other toolchain. The font likely predates modern font development workflows and may have been built using FontForge with Graphite/AAT tables.

### Notes

- The font is part of the KhmerOS project by Danh Hong
- The repository contains only binary TTFs — this is a binary-only repo, not a source repo
- The commit `d72e920` (2021-01-23, "update") is the latest commit, but the font has been in Google Fonts since 2011
- No existing `config.yaml` in either the upstream repo or the google/fonts family directory

### Actions Taken

A source block was added to METADATA.pb pointing to commit `d72e920` at danhhong/Khmer. While no editable sources exist, the repository URL documents the designer's canonical location for the font binaries.
