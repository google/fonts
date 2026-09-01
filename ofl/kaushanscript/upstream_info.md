# Kaushan Script — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/librefonts/kaushanscript |
| Commit | `b1b7451878d44084faa32e3bcc5ce043f4d1acf4` |
| Confidence | Medium |

## Source Types

The repository contains TTX-decompiled sources only, in the `src/` directory.

## Build Compatibility

Not buildable with gftools-builder. The TTX files are decompiled binary font dumps, not original editable design sources. No Impallari/Kaushan repository was found on GitHub (Pablo Impallari's repos for this font appear to be unavailable).

## Investigation Notes

This is a librefonts mirror repository containing TTX-decompiled binary dumps. Kaushan Script was designed by Pablo Impallari, but no original repository with editable design sources was found on GitHub.

**Note on librefonts TTX mirrors**: These repositories contain TTX (XML) representations of the compiled font binaries. They are mechanically decompiled from the .ttf files and do not represent original design sources. They cannot be used for font development or rebuilding with gftools-builder.

The binary in google/fonts dates from the initial commit (2015-03-07).

A source block was added to METADATA.pb pointing to this repository and commit.

## Confidence: Medium

Librefonts TTX mirror; original design sources are not available.
