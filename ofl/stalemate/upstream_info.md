# Stalemate -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `stalemate/src/`

## Source Files

The source directory contains: 3 VFB files (FontLab, proprietary format); 1 compiled binary (OTF/TTF, not design sources).

The VFB format is proprietary (FontLab) and cannot be built with gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `Stalemate-Regular-OTF.vfb` (VFB, proprietary)
- `Stalemate-Regular-TTF.vfb` (VFB, proprietary)
- `Stalemate-Regular.vfb` (VFB, proprietary)
- `Stalemate-Regular.otf` (compiled binary)

## Research

Stalemate was designed by Jim Lyles for Astigmatic (AOETI)
(astigma@astigmatic.com) and released in 2012. Searches on GitHub for
repositories under Astigmatic, Jim Lyles, or related names returned no
results. No GitHub organization or user account for Astigmatic was found.


## Notes

The designer listed in METADATA.pb is Astigmatic. Stalemate is described as
a script typeface with vintage origins and modern flair. It supports Latin
and Latin Extended character sets and is licensed under the SIL Open Font
License.
