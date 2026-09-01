# Swanky and Moo Moo -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `swankyandmoomoo/src/`

## Source Files

The source directory contains: 1 VFB file (FontLab, proprietary format); 1 SFD file (FontForge format).

Neither VFB (FontLab, proprietary) nor SFD (FontForge) formats are supported by gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `SwankyandMooMoo.vfb` (VFB, proprietary)
- `SwankyandMooMoo-TTF.sfd` (SFD, FontForge)

## Designer

Kimberly Geswein (kimberlygeswein.com)

## Search Results

- **librefonts/swankyandmoomoo**: Mirror repository only. The `src/` directory contained `SwankyandMooMoo.vfb` and `SwankyandMooMoo-TTF.sfd` — VFB/SFD only, no UFO or Glyphs sources.
- Kimberly Geswein had no identifiable GitHub presence (no matching GitHub user found).
- Her fonts appear to be distributed via her website and font distribution platforms, without public source repositories.
- The font was created in 2010, predating common use of version-controlled font workflows.
