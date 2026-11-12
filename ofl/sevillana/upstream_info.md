# Sevillana -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `sevillana/src/`

## Source Files

The source directory contains: 2 VFB files (FontLab, proprietary format); 1 compiled binary (OTF/TTF, not design sources).

The VFB format is proprietary (FontLab) and cannot be built with gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `Sevillana-Regular-OTF.vfb` (VFB, proprietary)
- `Sevillana-Regular-TTF.vfb` (VFB, proprietary)
- `Sevillana-Regular.otf` (compiled binary)

## Designer

Brownfox

## Search Results

- Searched `sevillana font` on GitHub: 0 relevant results
- Searched `sevillana in:name` on GitHub: 20 results, none font-related
- No Brownfox GitHub organization or user was found with Sevillana sources
