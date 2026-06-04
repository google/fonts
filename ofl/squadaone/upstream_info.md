# Squada One -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `squadaone/src/`

## Source Files

The source directory contains: 1 VFB file (FontLab, proprietary format); 1 SFD file (FontForge format); 1 compiled binary (OTF/TTF, not design sources).

Neither VFB (FontLab, proprietary) nor SFD (FontForge) formats are supported by gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `SquadaOne-Regular.vfb` (VFB, proprietary)
- `SquadaOne-Regular-TTF.sfd` (SFD, FontForge)
- `SquadaOne-Regular.otf` (compiled binary)

## Research

Squada One was designed by Joe Prince for Admix Designs
(http://www.admixdesigns.com, joe@admixdesigns.com) and released in 2011.
Searches on GitHub for repositories by Joe Prince, Admix Designs, or related
names returned no relevant results. The GitHub user `joeprince` exists but had
only an unrelated repository (`k-r`). No Admix Designs GitHub organization was
found.


## Notes

The designer listed in METADATA.pb is Joe Prince. Squada One is described as
a bold, geometric, condensed display typeface suitable for use at any size.
It is licensed under the SIL Open Font License.
