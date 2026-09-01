# Stint Ultra Expanded -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `stintultraexpanded/src/`

## Source Files

The source directory contains: 3 VFB files (FontLab, proprietary format); 1 compiled binary (OTF/TTF, not design sources).

The VFB format is proprietary (FontLab) and cannot be built with gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `StintUltraExpanded-Regular-OTF.vfb` (VFB, proprietary)
- `StintUltraExpanded-Regular-TTF.vfb` (VFB, proprietary)
- `StintUltraExpanded-Regular.vfb` (VFB, proprietary)
- `StintUltraExpanded-Regular.otf` (compiled binary)

## Designer

Astigmatic (Brian J. Bonislawsky, astigma@astigmatic.com)

## Search Results

- **librefonts/stintultraexpanded**: Mirror repository only. The `src/` directory contained `StintUltraExpanded-Regular-OTF.vfb`, `StintUltraExpanded-Regular-TTF.vfb`, and `StintUltraExpanded-Regular.vfb` — VFB only, no UFO or Glyphs sources.
- **astigmatic GitHub**: The `astigmatic` GitHub user had only two private/placeholder repos (`pro`, `project1`), no font repositories.
- No other repositories for this font were found on GitHub.
