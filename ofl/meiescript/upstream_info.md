# Meie Script

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Meie Script built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/meiescript` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it. The directory also holds FontLab `.vfb` files; the `.sfd` is
taken as the master because FontForge generated the shipped fonts and the build from the
`.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/meiescript.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/meiescript at `28cd9f97a68d`. Builds with
gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`28cd9f97a68d` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Where the shipped
binaries differ from the source, the difference is reproduced by a documented commit
before the conversion, never silently corrected. Any improvement is a later commit that
needs its own QA, and is left as future work for an onboarder to review in a font-update
PR.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Meie Script — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The original design sources for Meie Script are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/meiescript/src/`

#### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `MeieScript-Regular-OTF.vfb` | FontLab VFB | No (proprietary) |
| `MeieScript-Regular-TTF.sfd` | FontForge SFD | No (not gftools-builder compatible) |
| `MeieScript-Regular.otf` | Compiled OTF binary | No (not a design source) |
| `METADATA_comments.txt` | Metadata notes | N/A |

The VFB and SFD files are the original design masters. The `.otf` is a compiled binary, not a design source. No UFO, Glyphs, or other modern buildable sources are available.

### Build System

No modern build system (gftools builder, fontmake) is available. The VFB format is proprietary (FontLab Studio 5) and the SFD format is not supported by gftools-builder.

### config.yaml Status

No `config.yaml` exists. One cannot be created without converting sources to a modern format (UFO or Glyphs).

### Designer & History

The original designers are **Johan Kallas** (johankallas) and **Mihkel Virkus** (mihkelvirkus), both based in Tallinn, Estonia. Neither designer has public GitHub repositories of their own.

- **Designer contact**: Johan Kallas (`johan.kallas@gmail.com`), Mihkel Virkus (`mihkelvirkus@gmail.com`) — from FONTLOG.txt. The METADATA.pb uses slightly different addresses (`johankallas@gmail.com`, `mihkelvirkus@gmail.com`).
- **Font version**: 1.001 (unchanged since 2012 initial release)
- **Date added to Google Fonts**: 2012-08-21

### Additional Repository

A copy also exists in the `librefonts` GitHub organization:

- **URL**: https://github.com/librefonts/meiescript
- **Owner**: librefonts (Mikhail Kashkin / hash3g — not the original designers)
- **Last pushed**: 2014-10-17
- **Latest relevant commit**: `5b8265c5fea4aedc3d90da6e6b2e5bc47fb2bb22` — "update .travis.yml" (2014-10-17)
- **Commit that added font files**: `1689c5fd5600097e726a3bbcc857b4d1f034a8c1` — "Move meiescript font files to separate repository" (2014-07-16)

This repository was created by Mikhail Kashkin as part of the `librefonts` organization, which was a Google Fonts infrastructure effort to host font sources. The repo has 12 commits total, all from 2014, and has been inactive since October 2014. It uses an obsolete fontbakery-build pipeline via Travis CI.

### Notes

- **No upstream activity since 2014**: The repository has been completely dormant. There are no issues, pull requests, or forks.
- **No UFO sources**: The original sources are in VFB (FontLab) and SFD (FontForge) formats. Conversion to UFO would be required for modern tooling.
- **librefonts org**: The `librefonts` GitHub organization (https://github.com/librefonts) was used in 2014 to migrate several early Google Fonts to hosted repositories. It is not an official Google organization.
- **Confidence in upstream identification**: High — the repository explicitly describes itself as the Meie Script font by the same designers, with matching copyright, license, and version.
