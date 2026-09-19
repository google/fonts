# Meie Script — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The original design sources for Meie Script are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/meiescript/src/`

### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `MeieScript-Regular-OTF.vfb` | FontLab VFB | No (proprietary) |
| `MeieScript-Regular-TTF.sfd` | FontForge SFD | No (not gftools-builder compatible) |
| `MeieScript-Regular.otf` | Compiled OTF binary | No (not a design source) |
| `METADATA_comments.txt` | Metadata notes | N/A |

The VFB and SFD files are the original design masters. The `.otf` is a compiled binary, not a design source. No UFO, Glyphs, or other modern buildable sources are available.

## Build System

No modern build system (gftools builder, fontmake) is available. The VFB format is proprietary (FontLab Studio 5) and the SFD format is not supported by gftools-builder.

## config.yaml Status

No `config.yaml` exists. One cannot be created without converting sources to a modern format (UFO or Glyphs).

## Designer & History

The original designers are **Johan Kallas** (johankallas) and **Mihkel Virkus** (mihkelvirkus), both based in Tallinn, Estonia. Neither designer has public GitHub repositories of their own.

- **Designer contact**: Johan Kallas (`johan.kallas@gmail.com`), Mihkel Virkus (`mihkelvirkus@gmail.com`) — from FONTLOG.txt. The METADATA.pb uses slightly different addresses (`johankallas@gmail.com`, `mihkelvirkus@gmail.com`).
- **Font version**: 1.001 (unchanged since 2012 initial release)
- **Date added to Google Fonts**: 2012-08-21

## Additional Repository

A copy also exists in the `librefonts` GitHub organization:

- **URL**: https://github.com/librefonts/meiescript
- **Owner**: librefonts (Mikhail Kashkin / hash3g — not the original designers)
- **Last pushed**: 2014-10-17
- **Latest relevant commit**: `5b8265c5fea4aedc3d90da6e6b2e5bc47fb2bb22` — "update .travis.yml" (2014-10-17)
- **Commit that added font files**: `1689c5fd5600097e726a3bbcc857b4d1f034a8c1` — "Move meiescript font files to separate repository" (2014-07-16)

This repository was created by Mikhail Kashkin as part of the `librefonts` organization, which was a Google Fonts infrastructure effort to host font sources. The repo has 12 commits total, all from 2014, and has been inactive since October 2014. It uses an obsolete fontbakery-build pipeline via Travis CI.

## Notes

- **No upstream activity since 2014**: The repository has been completely dormant. There are no issues, pull requests, or forks.
- **No UFO sources**: The original sources are in VFB (FontLab) and SFD (FontForge) formats. Conversion to UFO would be required for modern tooling.
- **librefonts org**: The `librefonts` GitHub organization (https://github.com/librefonts) was used in 2014 to migrate several early Google Fonts to hosted repositories. It is not an official Google organization.
- **Confidence in upstream identification**: High — the repository explicitly describes itself as the Meie Script font by the same designers, with matching copyright, license, and version.
