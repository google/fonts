# Spinnaker -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `spinnaker/src/`

## Source Files

The source directory contains: 1 VFB file (FontLab, proprietary format); 1 SFD file (FontForge format); 1 compiled binary (OTF/TTF, not design sources).

Neither VFB (FontLab, proprietary) nor SFD (FontForge) formats are supported by gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `Spinnaker-Regular-OTF.vfb` (VFB, proprietary)
- `Spinnaker-Regular-TTF.sfd` (SFD, FontForge)
- `Spinnaker-Regular.otf` (compiled binary)

## Research

Spinnaker was designed by Elena Albertoni for Sorkin Type Co. (Eben Sorkin),
released in 2011. The font's `DESCRIPTION.en_us.html` referenced source files
as being available from Google Code (`code.google.com/p/googlefontdirectory/`),
which has since been archived and shut down.

No GitHub repository was found for Spinnaker under SorkinType, Elena Albertoni,
or related names. The SorkinType GitHub organization did not include a
Spinnaker repository among its public repos.


## Notes

The designer listed in METADATA.pb is Elena Albertoni. Spinnaker is described
as inspired by French and UK lettering found on travel posters for ships. It
is a low-contrast, slightly wide sans-serif design licensed under the SIL Open
Font License, with copyright held by Sorkin Type Co.
