# Megrim — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete (SFD-only sources, no gftools-builder config possible)

## METADATA.pb Source Block (current)

No source block exists on the current `main` branch of google/fonts. A source block was prepared on a local branch (`sources_info_2026-02-25`) but has not been merged:

```
source {
  repository_url: "https://github.com/librefonts/megrim"
  commit: "274ef534110a60534a520038400a8db0b3abd976"
}
```

## Repository Analysis

**Repository**: https://github.com/librefonts/megrim
**Status**: Accessible (HTTP 200), not archived, not a fork
**Created**: 2014-07-16
**Last pushed**: 2014-10-17
**Organization**: librefonts (a third-party archive organization that mirrors Google Fonts sources)

The repository contains a single commit (`274ef53`) by `hash3g` dated 2014-10-17, with the message "update .travis.yml". This is not the original author's repository — it is an archive created by the librefonts organization.

### Repository Structure

```
/
├── DESCRIPTION.en_us.html
├── FONTLOG.txt
├── METADATA.json
├── Megrim.ttf.*.ttx          (TTX-decomposed tables of the TrueType binary)
├── OFL.txt
├── .travis.yml               (FontBakery CI config, outdated)
└── src/
    ├── Megrim-TTF.sfd         (FontForge source, 405 KB)
    ├── Megrim.vfb             (FontLab source, 110 KB)
    ├── Megrim.otf.*.ttx       (TTX-decomposed tables of the OTF binary)
    ├── METADATA_comments.txt
    └── VERSIONS.txt
```

### Source Files

- **Megrim-TTF.sfd**: FontForge SFD source file, created 2010-05-05, last modified 2011-04-28. This is the primary editable source.
- **Megrim.vfb**: FontLab VFB binary source file (110 KB). Secondary source format.
- **TTX files**: Decomposed TTX tables of the compiled font. These are not editable design sources.

No `.glyphs`, `.ufo`, or `.designspace` files exist. The sources are exclusively in legacy formats (SFD/VFB) that are not compatible with gftools-builder.

### Contributors to librefonts/megrim

- `vitalyvolkov`
- `xen`

Neither is the original font designer (Daniel Johnson).

## Onboarding History

**Designer**: Daniel Johnson (il.basso.buffo@gmail.com)
**Date added to Google Fonts**: 2011-05-04
**Font version**: 20110427

The font was part of the initial bulk import into the google/fonts repository (commit `90abd17b4`, 2015-03-07, by Dave Crossland). The font binary has never been updated since the initial import — there is only one commit that added the `.ttf` file.

The FONTLOG changelog shows:
- 2010-05-11: Initial release
- 2010-07-02: Improved lowercase Icelandic glyphs; added more glyphs with diacritics
- 2010-08-31: Added stylistic alternate set (ss01); added Turkish glyphs

The SFD file's modification timestamp (2011-04-28) aligns with the font binary version string (20110427).

There were no PRs associated with the onboarding of this font. It was part of the original Google Fonts catalog that predated the current github-based workflow.

A deploy commit (`76adaf1d2`, 2021-11-01, by m4rc1e) appeared to delete the megrim directory, but this commit exists on an orphaned branch and was never merged into main.

### Original Author's Repository

Daniel Johnson's personal page was listed as `http://io.debian.net/~danielj/` in the FONTLOG. No personal GitHub repository was found for Daniel Johnson under this font name. The librefonts/megrim archive appears to be the only GitHub repository containing the source files for this font.

## Build Configuration

**Config.yaml**: None, and none possible.

The upstream repository contains only SFD (FontForge) and VFB (FontLab) source files. These legacy formats are not supported by gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. Therefore, no `config.yaml` can be created for this font without first converting the sources to a modern format.

The repository's `.travis.yml` used the old `fontbakery-build.py` pipeline (circa 2014), which is no longer in use.

## Findings

1. **No original upstream repository exists** — The librefonts/megrim repo is a third-party archive, not the original author's repository. Daniel Johnson does not appear to have a GitHub presence for this font.

2. **SFD-only sources** — The only editable design source is a FontForge `.sfd` file. This format is not compatible with gftools-builder, so no `config.yaml` can be provided.

3. **Single commit in upstream** — The archive repository has only one commit (`274ef53`), which is the only possible reference commit.

4. **Font has not been updated since onboarding** — The font binary in google/fonts is the original from the 2015 initial import, matching the 2011-era sources.

5. **Source block was already prepared** — A source block with `repository_url` and `commit` was prepared on a local branch but has not been pushed to google/fonts main.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/megrim"
  commit: "274ef534110a60534a520038400a8db0b3abd976"
}
```

No `config_yaml` field is included because the sources are in SFD format (FontForge), which is not compatible with gftools-builder. An override config.yaml is also not possible without source format conversion.

**Confidence**: HIGH — The librefonts/megrim repo is the only known GitHub repository for this font, and it contains the correct SFD source matching the compiled binary. The single commit (`274ef53`) is the only possible reference.
