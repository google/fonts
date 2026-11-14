# Varela — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Joe Prince

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `varela/src/`.

### Source Files

- **VFB (FontLab)**: Varela-Regular.vfb
- **SFD (FontForge)**: Varela-Regular-TTF.sfd
- **OTF (compiled)**: Varela-Regular.otf

Sources are in VFB (FontLab, proprietary) and SFD (FontForge) formats, neither of which is buildable with gftools-builder.

## Investigation Details

The font was created by Joe Prince of Admix Designs (`joe@admixdesigns.com`). Searches were conducted for GitHub repositories under the name "Varela", "admixdesigns", and "joeprince" but no dedicated font source repository was located. The website `admixdesigns.com` was inaccessible. No UFO, Glyphs, or other open-format source files were found in any publicly accessible repository.

The `librefonts/varelaround` mirror was found but excluded per policy.
