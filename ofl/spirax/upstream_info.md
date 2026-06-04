# Spirax -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `spirax/src/`

## Source Files

The source directory contains: 1 VFB file (FontLab, proprietary format); 1 SFD file (FontForge format); 1 compiled binary (OTF/TTF, not design sources).

Neither VFB (FontLab, proprietary) nor SFD (FontForge) formats are supported by gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `Spirax-Regular.vfb` (VFB, proprietary)
- `Spirax-Regular-TTF.sfd` (SFD, FontForge)
- `Spirax-Regular.otf` (compiled binary)

## Research

Spirax was designed by Brenda Gallo and Gustavo Dipre, released in 2011.
The designer contact listed in METADATA.pb is Brenda Gallo
(gbrenda1987@gmail.com). Searches on GitHub for repositories maintained by
Brenda Gallo, Gustavo Dipre, or others for the Spirax typeface returned no
results. The font is only available in compiled TTF form with no open source
files found in any public repository.


## Notes

The designer listed in METADATA.pb is Brenda Gallo. Spirax is a display font
inspired by geometric spirals, featuring pronounced contrast and original
curves. It supports the Latin character set and is licensed under the SIL Open
Font License.
