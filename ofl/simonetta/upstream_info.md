# Simonetta -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `simonetta/src/`

## Source Files

The source directory contains: 8 VFB file(s) (FontLab, proprietary format); 4 compiled binaries (OTF/TTF, not design sources).

The VFB format is proprietary (FontLab) and cannot be built with gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `Simonetta-Black-OTF.vfb` (VFB, proprietary)
- `Simonetta-Black-TTF.vfb` (VFB, proprietary)
- `Simonetta-BlackItalic-OTF.vfb` (VFB, proprietary)
- `Simonetta-BlackItalic-TTF.vfb` (VFB, proprietary)
- `Simonetta-Italic-OTF.vfb` (VFB, proprietary)
- `Simonetta-Italic-TTF.vfb` (VFB, proprietary)
- `Simonetta-Regular-OTF.vfb` (VFB, proprietary)
- `Simonetta-Regular-TTF.vfb` (VFB, proprietary)
- `Simonetta-Black.otf` (compiled binary)
- `Simonetta-BlackItalic.otf` (compiled binary)
- `Simonetta-Italic.otf` (compiled binary)
- `Simonetta-Regular.otf` (compiled binary)

## Designer

Brownfox (Gayaneh Bagdasaryan) — brownfox.org

## Repository Search

A search for canonical upstream repositories was conducted on GitHub. The following repositories were found:

- **librefonts/simonetta** — a librefonts mirror (excluded per policy).
- **profound-labs/simonetta-x-font** — extended variant with Slovenian and Pali accents, not the canonical upstream.
- No repository owned by Brownfox or Gayaneh Bagdasaryan was found.
