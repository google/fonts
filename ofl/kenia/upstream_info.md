# Investigation: Kenia

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [https://github.com/googlefonts/googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `kenia/src/` |
| **Buildable** | No — legacy formats only (.vfb/.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`) that was the canonical host for Google Fonts from 2010 to 2013.

### Source files (9)

| File | Format | Notes |
|------|--------|-------|
| `Kenia-Regular.vfb` | FontLab VFB | Proprietary format, not buildable with gftools |
| `Kenia-Regular.sfd` | FontForge SFD | Open format, not buildable with gftools-builder |
| `Kenia-Regular-TTF.sfd` | FontForge SFD | Open format, not buildable with gftools-builder |
| `features.kern` | OpenType feature code | Kerning definitions |
| `2010-12-06_Kenia-Regular.pdf` | PDF | Design documentation |
| `2010-12-09_Kenia_glyphs.pdf` | PDF | Glyph specimen documentation |
| `2010-12-09_Kenia_text.pdf` | PDF | Text specimen documentation |
| `Julia_Petretta.jpg` | JPEG | Designer photo |
| `METADATA_comments.txt` | Metadata | Not a design source |

The source directory contains legacy VFB (FontLab) and SFD (FontForge) design sources, along with OpenType kerning feature code and design documentation PDFs from December 2010. These are original design sources but are not compatible with the gftools-builder pipeline.

## Investigation

The METADATA.pb has no `source` block. The font was added in the initial commit (`90abd17b4`) of the google/fonts repository.

The copyright notice reads: "Copyright (c) 2010, Julia Petretta (julia.petretta@googlemail.com), with Reserved Font Name Kenia"

Kenia is Julia Petretta's earliest known Google Fonts contribution (2010). The design documentation PDFs preserved in the source directory provide historical context for the font's development.

A cached repository exists at `upstream_repos/fontc_crater_cache/librefonts/kenia` containing similar source files. The git log shows one commit ("update .travis.yml") with no actual source changes beyond the initial librefonts import. This librefonts repository is an archival mirror.

There is no publicly known upstream GitHub repository for this Julia Petretta font.

## Conclusion

The googlefontdirectory-hg monorepo contains original design sources in legacy formats (VFB, SFD) along with kerning feature code and design documentation. These are not buildable with gftools-builder. No upstream GitHub repository is known for this family.
