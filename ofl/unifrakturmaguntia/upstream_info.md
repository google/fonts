# UnifrakturMaguntia — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: j. 'mach' wust

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `unifrakturmaguntia/src/`.

### Source Files

- **SFD (FontForge)**: UnifrakturMaguntia.sfd
- **OpenType features**: unifraktur.fea
- **Other**: MainzerFraktur-UNZ1A.zip, generate.py, j_mach_wust.jpg, unifraktur.gdl, unifraktur.mif

Sources are in SFD format (FontForge), which is not buildable with gftools-builder.

## Investigation Details

The font was distributed through the [UniFraktur project on SourceForge](https://sourceforge.net/projects/unifraktur/). The SourceForge project used SVN (Subversion) for version control, not Git. The last release zip was `UnifrakturMaguntia.2017-03-19.zip`, hosted at SourceForge. The font was edited with FontForge. No GitHub, GitLab, or other Git repository was identified for this font.

The `librefonts/unifrakturmaguntia` GitHub repository was found but it is a mirror/archive and was excluded per policy.
