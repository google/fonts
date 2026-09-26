# Sonsie One -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `sonsieone/src/`

## Source Files

The source directory contains: 2 VFB files (FontLab, proprietary format); 1 SFD file (FontForge format); 1 compiled binary (OTF/TTF, not design sources).

Neither VFB (FontLab, proprietary) nor SFD (FontForge) formats are supported by gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `SonsieOne-Regular-OTF.vfb` (VFB, proprietary)
- `SonsieOne-Regular.vfb` (VFB, proprietary)
- `SonsieOne-Regular-TTF.sfd` (SFD, FontForge)
- `SonsieOne-Regular.otf` (compiled binary)

## Research

Sonsie One was designed by Riccardo De Franceschi and mastered by Eben Sorkin
at Sorkin Type Co. The FONTLOG.txt documented that the font was originally
completed in FontLab VBF format by De Franceschi, and then mastered to TTF
format by Eben Sorkin. No GitHub repository was found under Sorkin Type
(`SorkinType` GitHub org does not include Sonsie One), nor under Riccardo
De Franceschi's name.


## Notes

The designer listed in METADATA.pb is Riccardo De Franceschi. The font is
described as a heavy, medium contrast, large x-height script font inspired
by hand-painted signs seen in Munich. The copyright is held by Sorkin Type Co.
