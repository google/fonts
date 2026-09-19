# Miama — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The original design sources for Miama are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/miama/src/`

### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `Miama.sfd` | FontForge SFD | No (not gftools-builder compatible) |
| `Miama-Regular-TTF.sfd` | FontForge SFD | No (not gftools-builder compatible) |
| `Miama.otf` | Compiled OTF binary | No (not a design source) |
| `Miama.ttf` | Compiled TTF binary | No (not a design source) |
| `miamadoc.pdf` | Documentation | N/A |
| `METADATA_comments.txt` | Metadata notes | N/A |

The `.sfd` files (FontForge native format) are the canonical design sources. `Miama.sfd` is the main master (655 KB) and `Miama-Regular-TTF.sfd` is a TTF-specific export. The `.otf` and `.ttf` are compiled binaries, not design sources.

## Build System

No modern build system (gftools builder, fontmake) is available. The SFD format is FontForge-native and not supported by gftools-builder.

## config.yaml Status

No `config.yaml` exists. The SFD source format is not compatible with gftools-builder.

## Designer & History

- **Designer**: Linus Romer (`linus.romer@gmx.ch`)
- **Version in googlefontdirectory-hg**: 0.32

The designer does not maintain a dedicated GitHub repository for Miama. His GitHub account (`linusromer`) contains tooling repositories (curvatura, mf2outline, etc.) but no Miama font repo.

## CTAN Distribution

The authoritative distribution source is **CTAN**: https://ctan.org/pkg/miama — the latest CTAN release is version 1.2 (January 15, 2025). CTAN provides a zip archive at `https://mirrors.ctan.org/fonts/miama.zip`. The CTAN package does not provide a public version-control URL. The 2025 release date strongly implies ongoing maintenance by the designer, even though the source is not publicly hosted on GitHub.

## Additional Repository

A copy also exists in the `librefonts` GitHub organization:

- **URL**: https://github.com/librefonts/miama
- **Last commit**: `c1383daa982130014964e87cb5394eb6f4d7a2cc` (2014-10-17, "update .travis.yml")

This is a legacy mirror from 2014 with an obsolete fontbakery-build pipeline. It is significantly outdated relative to the CTAN version (v1.2 vs v0.32). The repo also contains a `menusubset-miama.ff` FontForge script at the root.

## Notes

- The most current version (1.2, released 2025-01-15) is available on CTAN. Linus Romer should be contacted at `linus.romer@gmx.ch` to obtain the current source files or a repository URL.
- The `librefonts` organization on GitHub is a legacy mirror project; all its repos were last updated in 2014.
- A config.yaml would need to be authored from scratch for any future Google Fonts rebuild.
