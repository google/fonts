# Lusitana — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/librefonts/lusitana |
| Commit | `8fa070c2ac2963f13feee142e2001777ac48e774` |
| Confidence | Medium |

## Source Types

The repository contains TTX-decompiled sources only.

## Build Compatibility

Not buildable with gftools-builder. The TTX files are decompiled binary font dumps, not original editable design sources.

## Investigation Notes

This is a librefonts mirror repository containing TTX-decompiled binary dumps. Two other repositories were investigated: googlefonts/lusitana exists but appears to be empty (size=0), and fontalternative/lusitana exists but is very small (56KB). Neither alternative provides usable original design sources.

**Note on librefonts TTX mirrors**: These repositories contain TTX (XML) representations of the compiled font binaries. They are mechanically decompiled from the .ttf files and do not represent original design sources. They cannot be used for font development or rebuilding with gftools-builder.

The binary in google/fonts dates from the initial commit (2015-03-07).

A source block was added to METADATA.pb pointing to this repository and commit.

## Confidence: Medium

Librefonts TTX mirror; original design sources are not available. Alternative repos are empty or insufficient.

## Update (2026-04-24) -- Legacy source documentation

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/lusitana/` listing the legacy source files (`.sfd`/`.vfb`) present in the upstream repo at the pinned commit `8fa070c2ac`. These formats are not yet supported by gftools-builder; the config serves as documentation for future compatibility work and to distinguish legacy-sourced families from families genuinely missing a build recipe.
