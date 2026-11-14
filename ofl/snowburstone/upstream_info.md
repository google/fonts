# Snowburst One -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `snowburstone/src/`

## Source Files

The source directory contains: 1 VFB file (FontLab, proprietary format); 2 SFD files (FontForge format); 1 compiled binary (OTF/TTF, not design sources).

Neither VFB (FontLab, proprietary) nor SFD (FontForge) formats are supported by gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `SnowburstOne-Regular.vfb` (VFB, proprietary)
- `SnowburstOne-Regular_otf.sfd` (SFD, FontForge)
- `SnowburstOne-Regular_ttf.sfd` (SFD, FontForge)
- `SnowburstOne-Regular.otf` (compiled binary)

## Designer

Annet Stirling (designer); Sorkin Type Co (publisher)

## Repository Search

A search for canonical upstream repositories was conducted on GitHub. Searches for "snowburst", "sorkintype", and direct repository lookups for `sorkintype/SnowburstOne` and `EbenSorkin/SnowburstOne` returned no relevant font repositories. Only these were found:

- **librefonts/snowburstone** — a librefonts mirror (excluded per policy).
- **google-fonts-bower/snowburstone-bower** — a deprecated bower packaging mirror.

No repository owned by Sorkin Type Co or Annet Stirling containing UFO or Glyphs sources was found.
