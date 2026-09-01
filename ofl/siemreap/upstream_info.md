# Siemreap — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [danhhong/Siemreap](https://github.com/danhhong/Siemreap) |
| Commit | `3ce4cbfc6b8172c80872a1d666cff71ca720db96` |
| Date | 2021-01-22 |
| Confidence | High |

## Investigation

The METADATA.pb for Siemreap had no source block. The upstream repository was identified as danhhong/Siemreap, maintained by designer Danh Hong (credited in the font's copyright notice).

### Source Types Available

- **TTF only**: `Siemreap-Regular.ttf`, `KhmerOS-Regular.ttf`
- No editable source files (no SFD, UFO, Glyphs, or VFB)

### Buildability

The repository contains only compiled TTF binary fonts. No editable design sources are present. Not buildable with gftools-builder or any other toolchain.

### Notes

- The font is part of the KhmerOS project by Danh Hong
- The repository contains only binary TTFs — this is a binary-only repo, not a source repo
- The commit `3ce4cbc` (2021-01-22, "update") is the latest commit
- The repo also contains a `KhmerOS-Regular.ttf` alongside the Siemreap font
- No existing `config.yaml` in either the upstream repo or the google/fonts family directory

### Actions Taken

A source block was added to METADATA.pb pointing to commit `3ce4cbc` at danhhong/Siemreap. While no editable sources exist, the repository URL documents the designer's canonical location for the font binaries.
