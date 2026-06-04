# Ponnala — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [appajid/ponnala](https://github.com/appajid/ponnala) |
| Commit | `c1366dc5361da5f9dd8ed1c8864efc259a77672e` |
| Date | 2014-12-09 |
| Confidence | High |

## Investigation

The METADATA.pb for Ponnala had no source block. The upstream repository was identified as appajid/ponnala, by designer Appaji Ambarisha Darbha (Silicon Andhra).

### Source Types Available

- **SFD** (FontForge): `Ponnala.sfd`
- **UFO**: `Ponnala.ufo/` (contains `fontinfo.plist`, `features.fea`, `glyphs/`)
- **License**: `OFL.txt`

### Buildability

The repository contains both SFD and UFO sources. The UFO format is gftools-builder compatible. A `config.yaml` could potentially be created for this family, though the UFO may be an older format that needs testing with current tooling.

### Notes

- Telugu script display typeface from the Silicon Andhra project
- The UFO contains FontLab v2 OTL data (`com.fontlab.v2.otl.ttx.xml`), indicating it was likely exported from FontLab
- No existing `config.yaml` in either the upstream repo or the google/fonts family directory

### Actions Taken

A source block was added to METADATA.pb pointing to commit `c1366dc` (2014-12-09, "Updated character combinations and Latin Character"), which is the latest commit in the repository.

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, referencing `Ponnala.ufo` from `appajid/ponnala`. This is a best-effort starting point for reproducible builds — the shipped binary was likely built with different tool versions and may not match exactly.
