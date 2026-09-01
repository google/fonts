# Peddana — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [appajid/peddana](https://github.com/appajid/peddana) |
| Commit | `717395267a5ebc69cee39b4eda415fffd39321aa` |
| Date | 2015-01-08 |
| Confidence | High |

## Investigation

The METADATA.pb for Peddana had no source block. The upstream repository was identified as appajid/peddana, by designer Appaji Ambarisha Darbha (Silicon Andhra).

### Source Types Available

- **SFD** (FontForge): `Peddana-Regular.sfd`
- **UFO**: `Peddana-Regular.ufo/` (contains `fontinfo.plist`, `glyphs/`)
- **License**: `OFL.txt`

### Buildability

The repository contains both SFD and UFO sources. The UFO format is gftools-builder compatible. A `config.yaml` could potentially be created for this family, though the UFO may be an older format that needs testing with current tooling.

### Notes

- Telugu script serif typeface from the Silicon Andhra / Andhrapradesh Society for Knowledge Networks project
- No existing `config.yaml` in either the upstream repo or the google/fonts family directory

### Actions Taken

A source block was added to METADATA.pb pointing to commit `7173952` (2015-01-08, merge PR #2), which is the latest commit in the repository.

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, referencing `Peddana-Regular.ufo` from `appajid/peddana`. This is a best-effort starting point for reproducible builds — the shipped binary was likely built with different tool versions and may not match exactly.
