# Averia Sans Libre

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: missing_config
- **Designer**: Dan Sayers
- **Confidence**: HIGH

## Source Data

| Field            | Value                                                    |
|------------------|----------------------------------------------------------|
| repository_url   | https://github.com/librefonts/averiasanslibre            |
| commit           | 280f9a59a667fd22373143bc0960e26d54516eaa                 |
| config_yaml      | none (TTX-only sources)                                  |

## How URL Found

The upstream repository URL was identified from the cached clone at `upstream_repos/fontc_crater_cache/librefonts/averiasanslibre/`. The git remote points to `https://github.com/librefonts/averiasanslibre`. This URL was verified accessible (HTTP 200).

The `librefonts` GitHub organization hosts this repo alongside the other Averia family variants (averialibre, averiaseriflibre, averiagruesalibre). The repo was originally set up by user `hash3g` in October 2014, containing decomposed TTX representations of the font binaries plus supporting metadata files.

## How Commit Identified

The upstream repository contains only a single commit:

- **280f9a5** (2014-10-17, hash3g): "update .travis.yml" -- this is the initial (and only) commit in the shallow-cloned repo, containing all 90+ decomposed TTX files, FONTLOG, OFL.txt, METADATA.json, and a Travis CI configuration.

In google/fonts, the font binary history shows two commits:
1. **90abd17** (2015-03-07, Dave Crossland): "Initial commit" -- original onboarding of v1.001 TTFs
2. **0f81bc9** (2017-08-07, Marc Foley): "hotfix-averiasanslibre: v1.002 added (#838)" -- updated all 6 TTFs with minor size changes

The upstream repo TTX files contain v1.001 font data (per the name table: "Version 1.001" and head table: fontRevision 1.0, modified 2012-03-09). The fonts currently in google/fonts are v1.002 from the Marc Foley hotfix. The upstream repo was never updated to reflect v1.002.

Since the repo has only one commit (280f9a5), that is the only possible reference commit. However, this commit corresponds to v1.001, while google/fonts currently ships v1.002.

## How Config Resolved

**No gftools-builder compatible sources exist in this repository.**

The upstream repo contains exclusively:
- **Decomposed TTX files**: XML representations of TTF table data (cmap, glyf, head, hhea, hmtx, kern, loca, maxp, name, OS/2, post, gasp, FFTM) for all 6 styles
- **Metadata files**: FONTLOG.txt, OFL.txt, METADATA.json, DESCRIPTION.en_us.html
- **Build infrastructure**: .travis.yml (fontbakery-build.py based), src/VERSIONS.txt, src/METADATA_comments.txt

There are **no** .glyphs, .ufo, .designspace, .sfd, or .vfb files. The name table records indicate the fonts were originally created with FontForge (nameID 3: "FontForge : AveriaSansLibre-Regular : 13-11-2011"), which uses SFD format. However, no SFD sources are present in this repo -- only the TTX decomposition of the compiled binaries.

TTX files cannot be used with gftools-builder (which requires .glyphs, .ufo, or .designspace sources). While TTX can be reassembled into TTF using `ttx` command, this is a binary round-trip, not a source rebuild. An override config.yaml is therefore not applicable.

## Conclusion

The upstream repository at https://github.com/librefonts/averiasanslibre is confirmed valid and accessible. It contains TTX decompositions of the Averia Sans Libre v1.001 binaries, but no editable font sources suitable for gftools-builder. The fonts currently in google/fonts are v1.002 (updated via PR #838 by Marc Foley in August 2017), which postdates the upstream repo content.

The source block for METADATA.pb should reference:
- **repository_url**: `https://github.com/librefonts/averiasanslibre`
- **commit**: `280f9a59a667fd22373143bc0960e26d54516eaa` (only commit in repo)
- **config_yaml**: omitted (no gftools-builder compatible sources)

Status is `missing_config` because no config.yaml can be created -- the repo lacks the font source formats (.glyphs, .ufo, .designspace) that gftools-builder requires. The original design sources (likely FontForge SFD files) are not present in this repository.
