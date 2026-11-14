# Supermercado One -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `supermercadoone/src/`

## Source Files

The source directory contains: 1 VFB file (FontLab, proprietary format); 2 SFD files (FontForge format); 1 compiled binary (OTF/TTF, not design sources).

Neither VFB (FontLab, proprietary) nor SFD (FontForge) formats are supported by gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `SupermercadoOne-Regular.vfb` (VFB, proprietary)
- `SupermercadoOne-Regular-OTF.sfd` (SFD, FontForge)
- `SupermercadoOne-Regular-TTF.sfd` (SFD, FontForge)
- `SupermercadoOne-Regular.otf` (compiled binary)

## Designer

James Grieshaber (for Sorkin Type Co., www.sorkintype.com)

## Search Results

- **librefonts/supermercadoone**: Mirror repository only. The `src/` directory contained `SupermercadoOne-Regular-OTF.sfd`, `SupermercadoOne-Regular-TTF.sfd`, and `SupermercadoOne-Regular.vfb` — VFB/SFD only, no UFO or Glyphs sources.
- No other repositories for Supermercado One were found.
- James Grieshaber had no identifiable GitHub presence with font source repositories.
- The font was created in 2011 under Sorkin Type Co., predating common use of UFO/Glyphs workflows.
