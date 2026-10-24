# Shojumaru -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `shojumaru/src/`

## Source Files

The source directory contains: 3 VFB files (FontLab, proprietary format); 1 SFD file (FontForge format); 1 compiled binary (OTF/TTF, not design sources).

Neither VFB (FontLab, proprietary) nor SFD (FontForge) formats are supported by gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `Shojumaru-Regular-OTF.vfb` (VFB, proprietary)
- `Shojumaru-Regular-TTF.vfb` (VFB, proprietary)
- `Shojumaru-Regular.vfb` (VFB, proprietary)
- `Shojumaru-Regular-TTF.sfd` (SFD, FontForge)
- `Shojumaru-Regular.otf` (compiled binary)

## Designer

Astigmatic

## Search Results

- Searched `shojumaru font` on GitHub: 0 results
- Searched `shojumaru in:name` on GitHub: found only `librefonts/shojumaru`, `google-fonts-bower/shojumaru-bower`, and an AUR archive (no sources)
- Searched `astigmatic font in:name,description`: found only `googlefonts/SacramentoFont`
- Checked GitHub user `astigmatic`: only two unrelated repositories found
- `librefonts/shojumaru` skipped (mirror, not canonical source)
