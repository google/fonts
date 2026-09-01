# Ek Mukta

## Summary

Ek Mukta is the legacy name for the Mukta Devanagari family, designed by Girish Dalvi of Ek Type. The METADATA.pb currently points to `googlefonts/MuktaGFVersion`, a build intermediary repo by Marc Foley that generates TTFs from TTX sources. The true upstream is `EkType/Mukta`. Neither repo has gftools-builder compatible sources -- the original sources are VFB (FontLab) files with AFDKO feature code, and the build repo uses TTX + a shell script. No config.yaml exists or can be created for gftools-builder.

## Key Findings

| Field | Value |
|-------|-------|
| **Family Name** | Ek Mukta |
| **Designer** | Ek Type (Girish Dalvi, Yashodeep Gholap) |
| **License** | OFL |
| **Date Added** | 2014-05-12 |
| **Repository URL** | https://github.com/googlefonts/MuktaGFVersion |
| **True Upstream** | https://github.com/EkType/Mukta |
| **Commit Hash** | `bccb1e2d95db0eea6be66e001edb2aeb50ab8d2b` (MuktaGFVersion HEAD, v2.204 fonts) |
| **Config YAML** | none (TTX-based build, not gftools-builder compatible) |
| **Status** | missing_config |

## Investigation Details

### Relationship Between Ek Mukta and Mukta

"Ek Mukta" was the original name of this Devanagari typeface family. It was later renamed to just "Mukta" as part of a broader Mukta family covering multiple Indic scripts (Devanagari, Gujarati, Tamil, Gurmukhi). The Google Fonts catalog maintains "Ek Mukta" as a separate entry for backwards compatibility with existing API endpoints. The DESCRIPTION.en_us.html states: "This project was renamed Mukta."

### Upstream Repositories

There are two relevant repositories:

1. **EkType/Mukta** (`https://github.com/EkType/Mukta`) -- The true upstream by the original designers at Ek Type. Contains:
   - VFB (FontLab) source files for all weights in `Mukta-Devanagari/*/VFB/`
   - AFDKO OpenType feature code (GPOS, GSUB, GDEF files)
   - TTX dumps in `TTX/Mukta-Devanagari/`
   - FontMenuNameDB, GlyphOrderAndAliasDB, and other AFDKO project files
   - Sources for related families: MuktaMahee (Gurmukhi), MuktaMalar (Tamil), MuktaVaani (Gujarati)
   - The repo appears to have been force-pushed/rewritten -- it shows only a single commit (`65fdb20`) from 2025-08-18, titled "Binary hotfix 5.539, removed language tag, Fixes #32 and #40"

2. **googlefonts/MuktaGFVersion** (`https://github.com/googlefonts/MuktaGFVersion`) -- A build intermediary created by Marc Foley on 2017-01-26. Contains:
   - TTX source files in `src/` (for Mukta, MuktaMalar, MuktaVaani, and EkMukta)
   - A shell-based build script (`build/build.sh`) that converts TTX to TTF, creates the EkMukta legacy variants by copying and renaming Mukta fonts, applies ttfautohint, and patches version numbers
   - Pre-built TTF fonts in `fonts/` (v2.204)
   - The README states: "This repository hot fixes the binary sources for Mukta"
   - Last commit: `bccb1e2` (2017-02-01), which created the EkMukta legacy family

### Onboarding History

1. **Initial commit** (`90abd17b`, 2015-03-07): Ek Mukta added to google/fonts with v1.x fonts (~1MB each)

2. **v2.204 update** (PR #620, commit `bc8dfa56`, 2017-02-13): Marc Foley updated fonts to v2.204. PR body states: "This family is automatically generated in the hotfix repo from Mukta. We need to keep updating Ek Mukta to support its api end points." This update used MuktaGFVersion.

3. **v2.538 update** (PR #1006, commit `2b617a9c`, 2017-05-23): Marc Foley updated fonts to v2.538. PR body is empty. The MuktaGFVersion repo does NOT contain v2.538 fonts (it only has v2.204), so these fonts were likely generated from a more recent version of EkType/Mukta sources outside the MuktaGFVersion workflow.

4. **OS/2 fix** (PR #1016, commit `6c427427`, 2017-08-07): Marc Foley fixed OS/2 fsSelection and mac style bits that were set incorrectly in PR #1006.

5. **OTS fix** (PR #1209, commit `9d451f69`, 2017-09-27): Dave Crossland roundtripped the fonts through TTX to fix OTS validation errors (GDEF ClassRangeRecord overlap). This is the last commit that modified the binary font files.

### Current Binary Verification

The current fonts in google/fonts are v2.538, as confirmed by the version string:
```
Version 2.538;PS 1.001;hotconv 16.6.51;makeotf.lib2.5.65220; ttfautohint (v1.6)
```

The file sizes differ from MuktaGFVersion:
- google/fonts: 405KB-432KB (OTS-roundtripped v2.538)
- MuktaGFVersion: 441KB-469KB (v2.204)

This confirms the current binaries were NOT built from MuktaGFVersion HEAD.

### Source File Formats

- **EkType/Mukta**: VFB (FontLab 5) files -- proprietary format, not compatible with gftools-builder
- **googlefonts/MuktaGFVersion**: TTX files with a shell build script -- not gftools-builder compatible
- Neither repository contains .glyphs, .glyphx, .ufo, or .designspace files
- No config.yaml exists in either repo or in the google/fonts family directory

### Commit Hash Assessment

The tracking JSON records `bccb1e2` (MuktaGFVersion HEAD), but this commit produces v2.204 fonts while google/fonts has v2.538 fonts. The MuktaGFVersion repo was never updated beyond v2.204, so no commit in that repo corresponds to the current v2.538 binaries.

The v2.538 fonts were likely built from EkType/Mukta sources, but the EkType/Mukta repo has been force-pushed to a single commit from 2025, making it impossible to trace the original v2.538 commit.

## Conclusion

Ek Mukta is a complex case with two upstream repos:
- **METADATA.pb correctly references** `googlefonts/MuktaGFVersion` as the intermediary build repo used for the v2.204 onboarding
- The **true upstream** is `EkType/Mukta`, but its git history has been rewritten
- The current v2.538 binaries cannot be traced to any specific commit in either repo
- **No gftools-builder compatible sources exist** -- the font uses VFB/AFDKO sources that require a custom build pipeline
- No config.yaml can be created without a conversion of sources to a modern format (.glyphs or .designspace/.ufo)
- Status remains **missing_config** with a note that no buildable source files exist for gftools-builder
