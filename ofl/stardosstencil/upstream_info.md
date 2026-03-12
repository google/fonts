**Model**: Claude Opus 4.6

# Stardos Stencil — Upstream Source Investigation

## Summary

No canonical upstream repository with UFO or Glyphs sources was found for Stardos Stencil. The only GitHub repository found was a librefonts mirror (`librefonts/stardosstencil`) containing only VFB (FontLab) and SFD (FontForge) sources, which were excluded per policy.

## Designer

Vernon Adams (vern@newtypography.co.uk)

## Search Results

- **librefonts/stardosstencil**: Mirror repository only. The `src/` directory contained `StardosStencil-Regular.vfb`, `StardosStencil-Bold.vfb`, `StardosStencil-Regular-TTF.sfd`, `StardosStencil-Bold-TTF.sfd` — VFB/SFD only, no UFO or Glyphs sources.
- **Vernon Adams GitHub accounts** (`vernnobile`, `vernonadams`, `newtypography`): None contained a Stardos Stencil repository. Vernon Adams' primary font work was at `vernnobile` where he hosted many fonts, but Stardos Stencil was not among them.
- Stardos Stencil was created in 2011, predating the common adoption of version-controlled UFO/Glyphs workflows.

## Conclusion

No source block was added. The font sources only exist as VFB/SFD in a librefonts mirror, which is excluded per the investigation policy (skip librefonts mirrors and VFB/SFD-only repos).
