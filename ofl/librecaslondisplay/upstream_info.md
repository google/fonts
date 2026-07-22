# Investigation Report: Libre Caslon Display

**Family name**: Libre Caslon Display
**Directory**: `ofl/librecaslondisplay`
**Date added**: 2017-11-30
**Designer**: Impallari Type (Pablo Impallari, Rodrigo Fuenzalida)
**License**: OFL
**Model**: Claude Opus 4.6

## Summary

Libre Caslon Display is a display-weight serif font designed by Pablo Impallari and Rodrigo Fuenzalida, intended as the headline companion to Libre Caslon Text. The upstream repository uses exclusively FontLab `.vfb` source files, which are not compatible with gftools-builder. No config.yaml can be created since there are no buildable source formats (`.glyphs`, `.ufo`, `.designspace`).

## Upstream Repository

- **URL**: https://github.com/impallari/Libre-Caslon-Display
- **Status**: Active (accessible, unchanged since 2016)
- **Local cache**: `upstream_repos/fontc_crater_cache/impallari/Libre-Caslon-Display`
- **Default branch**: master
- **Repository clean**: Yes (verified)

## Commit History (Upstream)

The upstream repository has only 6 commits, all by Pablo Impallari:

| Hash | Date | Message |
|------|------|---------|
| `3491f6a` | 2016-07-25 | v1.002 |
| `b3d497e` | 2015-07-24 | cosmetics |
| `830fb56` | 2015-07-24 | Improving Description |
| `fa77c97` | 2015-07-24 | Removed RFN |
| `e8f1926` | 2014-12-01 | Uploading v1 |
| `23d1bee` | 2014-12-01 | readme |

The repository has had no new commits since `3491f6a` (v1.002, 2016-07-25). This is the HEAD of master.

## Onboarding to Google Fonts

- **Onboarding commit**: `95b0ecc63` on 2017-11-30 by Marc Foley (m4rc1e)
- **Commit message**: "librecaslondisplay: v1.100 added / Taken from the upstream repo https://github.com/impallari/Libre-Caslon-Display"
- **PR**: #1372, created 2017-11-30, merged 2019-07-10 by Marc Foley
- **PR body**: Contains FontBakery report results and rendering screenshots; confirms the upstream repo URL

The version number in the google/fonts commit message ("v1.100") does not match the upstream version ("v1.002"). According to the FONTLOG, v1.002 was a version number bump "to keep it the same as the text version." The "v1.100" label likely reflects a version assigned during the onboarding/processing workflow rather than a version tag in the upstream repo.

## Binary File Comparison

The binary font file in google/fonts does NOT match any binary in the upstream repository:

| Location | File size |
|----------|-----------|
| google/fonts (onboarded) | 101,384 bytes |
| Upstream at `3491f6a` (v1.002) | 124,204 bytes |
| Upstream at `b3d497e` (cosmetics) | 123,812 bytes |
| Upstream at `e8f1926` (v1) | 124,400 bytes |

The file in google/fonts is significantly smaller (101 KB vs 124 KB), indicating it was processed/rebuilt from the upstream sources before onboarding, likely using Google Fonts tools to strip unnecessary tables or apply font modifications for web serving.

## Commit Hash Verification

The commit hash `3491f6a9cfde2bc15e736463b0bc7d93054d5da1` was recorded in the METADATA.pb source block (added by commit `9a14639f3` on 2026-02-25). This is the latest (and last) commit on the upstream repository. Since the onboarding occurred on 2017-11-30, after this commit (2016-07-25), and there have been no subsequent commits, `3491f6a` is the correct reference commit -- it was the HEAD at the time of onboarding and remains the HEAD today.

## Source Files

At the referenced commit (`3491f6a`), the repository contains:

**Source files (FontLab only)**:
- `source/LibreCaslonDisplay-Regular.vfb`
- `source/LibreCaslonDisplay-Regular-OTF.vfb`
- `source/LibreCaslonDisplay-Regular-TTF.vfb`

**Pre-compiled binaries**:
- `fonts/TTF/LibreCaslonDisplay-Regular.ttf`
- `fonts/OTF/LibreCaslonDisplay-Regular.otf`

There are no `.glyphs`, `.ufo`, `.designspace`, or `.sfd` source files. The `.vfb` format is proprietary FontLab format and is not supported by gftools-builder or fontc.

## Config.yaml Assessment

**No config.yaml can be created.** The upstream sources are exclusively in `.vfb` format, which is not compatible with gftools-builder. An override config.yaml would serve no purpose since there are no buildable source files.

## METADATA.pb Source Block

Current state:
```
source {
  repository_url: "https://github.com/impallari/Libre-Caslon-Display"
  commit: "3491f6a9cfde2bc15e736463b0bc7d93054d5da1"
}
```

This is correct and complete for a VFB-only repository. The `config_yaml` field is correctly absent since there are no buildable sources.

## Status

- **Repository URL**: Verified correct
- **Commit hash**: Verified correct (`3491f6a`, HEAD of master, last commit before onboarding)
- **Config.yaml**: Not applicable (VFB-only sources)
- **Overall status**: `missing_config` (VFB-only sources; no path to gftools-builder compatibility without source conversion)
- **Confidence**: HIGH

## Notes

- The font was rebuilt/processed during onboarding (binary sizes differ from upstream), which is expected Google Fonts behavior
- The upstream repo has been completely dormant since July 2016 (no activity in nearly 10 years)
- The version discrepancy ("v1.100" in google/fonts vs "v1.002" in upstream) is a labeling artifact from the onboarding process
- The repository is part of a pair: Libre Caslon Display and [Libre Caslon Text](https://github.com/impallari/Libre-Caslon-Text) are companion families
