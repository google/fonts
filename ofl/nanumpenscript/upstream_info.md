# Nanum Pen Script — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (Mercurial monorepo, pre-GitHub era)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/nanumpenscript/src/`
- **Buildable**: No — only compiled binary in src/

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source Files

| File | Type |
|------|------|
| `NanumPen.otf` | Compiled OTF binary (not a design source) |
| `METADATA_comments.txt` | Metadata comments (not a source file) |

The only file in the `src/` directory is a compiled OTF binary. No editable design sources (UFO, Glyphs, SFD, VFB) are present in the monorepo.

## Designer and Provenance

- **Designer**: Sandoll Communication, commissioned by Naver
- **Distribution**: Naver distributes all Nanum fonts via https://hangeul.naver.com as binary downloads
- **GitHub presence**: Naver has a GitHub org (`github.com/naver`) with a `nanumfont` repo, but it contains only binary releases (TTF/OTF), not editable source files
- No UFO, Glyphs, or other source format is publicly available

## Build System

Not applicable — no editable source files exist. The font was designed using proprietary tools at Sandoll Communication. Only compiled TTF/OTF binaries have been publicly released.

## config.yaml

Does not exist. Cannot be created without editable sources.

## Notes

- All five Nanum families (Gothic, Gothic Coding, Myeongjo, Brush Script, Pen Script) share the same provenance: designed by Sandoll Communication for Naver
- The fonts are licensed under the SIL Open Font License
- Primary script: Korean (Kore)
- Single weight (Regular 400)
- Font version in Google Fonts: 2.000
- Any source metadata enrichment would require direct cooperation from Naver/Sandoll
