# Stoke -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `stoke/src/`

## Source Files

The source directory contains: 2 VFB files (FontLab, proprietary format); 3 SFD files (FontForge format); 2 compiled binaries (OTF/TTF, not design sources).

Neither VFB (FontLab, proprietary) nor SFD (FontForge) formats are supported by gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `Stoke-Light.vfb` (VFB, proprietary)
- `Stoke-Regular.vfb` (VFB, proprietary)
- `Stoke-Light-TTF.sfd` (SFD, FontForge)
- `Stoke-Regular-OTF.sfd` (SFD, FontForge)
- `Stoke-Regular-TTF.sfd` (SFD, FontForge)
- `Stoke-Light.otf` (compiled binary)
- `Stoke-Regular.otf` (compiled binary)

## Designer

Nicole Fally (for Sorkin Type Co., www.sorkintype.com)

## Search Results

- No dedicated GitHub repository for Stoke was found under any relevant search.
- **EbenSorkin GitHub**: EbenSorkin (Eben Sorkin of Sorkin Type Co.) hosted many font repositories but Stoke was not among them.
- The font was created in 2012 and Stoke appears to have no public source repository.
- Nicole Fally had no identifiable GitHub presence.
