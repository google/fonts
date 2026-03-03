# Averia Serif Libre

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: missing_config
- **Designer**: Dan Sayers
- **Confidence**: HIGH

## Source Data

| Field            | Value |
|------------------|-------|
| repository_url   | https://github.com/librefonts/averiaseriflibre |
| commit           | d1b2ab3fcea4e6a77af02a5e7861ed7753793dfd |
| config_yaml      | none (TTX-only sources) |

## How URL Found

The upstream repository URL is `https://github.com/librefonts/averiaseriflibre`. This was identified from the cached clone at `upstream_repos/fontc_crater_cache/librefonts/averiaseriflibre`, which has its git remote set to this URL. The repository is part of the `librefonts` GitHub organization, which hosts many Google Fonts upstream repos following the pattern established by Dave Crossland and others involved in early Google Fonts onboarding.

## How Commit Identified

The upstream repo is a shallow clone containing a single commit:

- **d1b2ab3** (2014-10-17, by hash3g): "update .travis.yml" -- This is the only commit available and represents the full state of the repository. It contains all TTX source files, metadata, and the Travis CI configuration.

In google/fonts, the font binary history shows two commits:
1. **90abd17b** (2015-03-07, by Dave Crossland): "Initial commit" -- First addition of the font to google/fonts with v1.001 binaries.
2. **463ce0ab** (2017-08-07, by Marc Foley, PR #839): "hotfix-averiaseriflibre: v1.002 added" -- Updated the fonts to v1.002 with minor binary size changes.

The last modification to the font binaries was PR #839 in August 2017. The upstream repo's single commit (d1b2ab3) predates both google/fonts commits, confirming it represents the source state used for the initial onboarding. The v1.002 hotfix in PR #839 was a minor fix (binary sizes changed by only a few bytes) and the PR body was empty, so it is unclear whether the upstream repo was involved in that update or if the fix was applied directly to the binaries.

Since the repo has only one commit and it predates the google/fonts additions, **d1b2ab3fcea4e6a77af02a5e7861ed7753793dfd** is the correct commit hash to reference.

## How Config Resolved

**No config.yaml can be created.** The upstream repository contains **only TTX files** (decompiled TrueType XML), not gftools-builder compatible sources. Specifically:

- No `.glyphs` files
- No `.ufo` directories
- No `.designspace` files
- No `.sfd` (FontForge) files
- No `.vfb` (FontLab) files

The repo structure consists of:
- 96 TTX files (split table format: `*.ttf._table_.ttx` and master `*.ttf.ttx` referencing them)
- `DESCRIPTION.en_us.html`, `FONTLOG.txt`, `OFL.txt`, `METADATA.json`
- `src/METADATA_comments.txt` and `src/VERSIONS.txt` (metadata only)
- `.travis.yml` (legacy CI using fontbakery-build.py)

The Travis CI configuration uses the old `fontbakery-build.py` pipeline, which would reassemble TTF binaries from the TTX files. This is not compatible with gftools-builder / fontc, which require editable design sources (.glyphs, .ufo, .designspace).

The font itself was created through an algorithmic averaging process (averaging outlines from hundreds of Google Fonts), so traditional editable sources in the usual sense do not exist. The TTX files are the closest thing to "sources" for this family.

**An override config.yaml is NOT applicable** because gftools-builder cannot use TTX files as input sources.

## Conclusion

Averia Serif Libre has a valid upstream repository at `https://github.com/librefonts/averiaseriflibre` with a single commit (d1b2ab3). The repository contains only TTX (decompiled TrueType XML) files, which are not compatible with gftools-builder. No override config.yaml can be created. The source block should be added to METADATA.pb with the repository URL and commit hash, but without a config_yaml path, and the status should be marked as `missing_config` since the sources cannot be rebuilt with the modern toolchain.
