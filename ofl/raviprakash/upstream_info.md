# Ravi Prakash — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [appajid/raviprakash](https://github.com/appajid/raviprakash) |
| Commit | `0f5d8d7f5a7d263feef811baaa16c143313f27da` |
| Date | 2014-12-09 |
| Confidence | High |

## Investigation

The METADATA.pb for Ravi Prakash had no source block. The upstream repository was identified as appajid/raviprakash, by designer Appaji Ambarisha Darbha (Silicon Andhra). The copyright also credits Eduardo Tunni for the base Latin forms ("Joti").

### Source Types Available

- **SFD** (FontForge): `RaviPrakash.sfd`
- **UFO**: `RaviPrakash.ufo/` (contains `fontinfo.plist`, `glyphs/`)
- **License**: `OFL.txt`

### Buildability

The repository contains both SFD and UFO sources. The UFO format is gftools-builder compatible. A `config.yaml` could potentially be created for this family, though the UFO may be an older format that needs testing with current tooling.

### Notes

- Telugu script display typeface from the Silicon Andhra project
- No existing `config.yaml` in either the upstream repo or the google/fonts family directory

### Actions Taken

A source block was added to METADATA.pb pointing to commit `0f5d8d7` (2014-12-09, "updating copyright and latin characters"), which is the latest commit in the repository.

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, referencing `RaviPrakash.ufo` from `appajid/raviprakash`. This is a best-effort starting point for reproducible builds — the shipped binary was likely built with different tool versions and may not match exactly.
