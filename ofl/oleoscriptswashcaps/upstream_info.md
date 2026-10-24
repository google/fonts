# Oleo Script Swash Caps — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/nicholasgross/googlefontdirectory-hg) (Mercurial-to-Git conversion of the original Google Font Directory)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `oleoscriptswashcaps/src/`

### Source Files in googlefontdirectory-hg

- `OleoScriptSwashCaps-Regular-OTF.vfb` — FontLab source for Regular weight (proprietary format, not buildable with gftools)
- `OleoScriptSwashCaps-Bold-OTF.vfb` — FontLab source for Bold weight (proprietary format, not buildable with gftools)
- `OleoScriptSwashCaps-Regular-TTF.sfd` — FontForge SFD for Regular (converted from VFB, not buildable with gftools-builder)
- `OleoScriptSwashCaps-Bold-TTF.sfd` — FontForge SFD for Bold (converted from VFB, not buildable with gftools-builder)
- `OleoScriptSwashCaps-Regular.otf` — compiled OTF binary (not a design source)
- `OleoScriptSwashCaps-Bold.otf` — compiled OTF binary (not a design source)
- `METADATA_comments.txt` — metadata notes (not a source file)

The primary design sources are the `.vfb` files (FontLab proprietary format). The `.sfd` files are TTF-flavored conversions. Neither format is buildable with gftools-builder.

## Family Details

- **Designer**: soytutype fonts
- **License**: OFL
- **Category**: DISPLAY
- **Google Fonts date added**: 2012-11-12
- **Copyright**: "Copyright (c) 2012, Soytutype (contact@soytutype.com.ar|soytutype@gmail.com), with reserved fontname 'Oleo'"

## Search Results

- GitHub was searched for "OleoScript", "soytutype", and related terms — no designer-owned repositories found
- GitHub API search for "OleoScript" returned only four repositories, all mirrors or packaging repos
- The Soytutype website (`www.soytutype.com.ar`) was unreachable (connection refused)
- No active GitHub profile was found for Soytutype
- No cached clone found in `/mnt/shared/upstream_repos/fontc_crater_cache/`

## Additional Repository Information

- **Librefonts mirror**: https://github.com/librefonts/oleoscriptswashcaps — contains the same VFB and SFD files as googlefontdirectory-hg. This is a mirror, not a canonical designer-owned repository.

## Relationship to Oleo Script

Oleo Script Swash Caps is explicitly described as a "sister family" to Oleo Script, both produced by Soytutype in 2012. The FONTLOG for this family references the same source file structure as Oleo Script.

## Notes

- No canonical upstream repository with Glyphs or UFO sources exists for Oleo Script Swash Caps.
- The original sources were in FontLab VFB format, preserved in googlefontdirectory-hg.
- The googlefontdirectory-hg monorepo is the only known location of the original source files (aside from the librefonts mirror).
- Confidence in source identification: **High** — the VFB files in googlefontdirectory-hg are the original design sources. However, the proprietary format limits usefulness for rebuilding.
