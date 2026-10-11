# Nanum Myeongjo — Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/nanummyeongjo/src/` |
| **Buildable** | No — no design sources present |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source files (1)

- **Metadata**: METADATA_comments.txt

The source directory contains only a metadata comments file. No design sources or compiled binaries were included in the monorepo for this family.

## Build System

Not applicable — no source-based build pipeline exists.

## Notes

- Designed by Sandoll Communication, commissioned by Naver
- Nanum Myeongjo is the serif (Myeongjo/Ming) counterpart to Nanum Gothic
- Naver distributes all Nanum fonts via https://hangeul.naver.com as binary downloads
- Naver has a GitHub org (`github.com/naver`) with a `nanumfont` repo, but it contains only binary releases (TTF/OTF), not editable source files
- No UFO, Glyphs, or other source format is publicly available — the font was designed using proprietary tools at Sandoll Communication
- All five Nanum families (Gothic, Gothic Coding, Myeongjo, Brush Script, Pen Script) share the same provenance
- Licensed under the SIL Open Font License
- Primary script: Korean (Kore)
- Three weights: Regular (400), Bold (700), ExtraBold (800)
- Font version in Google Fonts: 2.000
- Any source metadata enrichment would require direct cooperation from Naver/Sandoll
