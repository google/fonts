# Stardos Stencil -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `stardosstencil/src/`

## Source Files

The source directory contains: 2 VFB files (FontLab, proprietary format); 2 SFD files (FontForge format).

Neither VFB (FontLab, proprietary) nor SFD (FontForge) formats are supported by gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `StardosStencil-Bold.vfb` (VFB, proprietary)
- `StardosStencil-Regular.vfb` (VFB, proprietary)
- `StardosStencil-Bold-TTF.sfd` (SFD, FontForge)
- `StardosStencil-Regular-TTF.sfd` (SFD, FontForge)

## Designer

Vernon Adams (vern@newtypography.co.uk)

## Search Results

- **librefonts/stardosstencil**: Mirror repository only. The `src/` directory contained `StardosStencil-Regular.vfb`, `StardosStencil-Bold.vfb`, `StardosStencil-Regular-TTF.sfd`, `StardosStencil-Bold-TTF.sfd` — VFB/SFD only, no UFO or Glyphs sources.
- **Vernon Adams GitHub accounts** (`vernnobile`, `vernonadams`, `newtypography`): None contained a Stardos Stencil repository. Vernon Adams' primary font work was at `vernnobile` where he hosted many fonts, but Stardos Stencil was not among them.
- Stardos Stencil was created in 2011, predating the common adoption of version-controlled UFO/Glyphs workflows.
