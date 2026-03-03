# Averia Gruesa Libre

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: missing_config
- **Confidence**: HIGH

## Designer

Dan Sayers (i@iotic.com) — http://iotic.com/averia/

## Source Data

| Field           | Value                                                        |
|-----------------|--------------------------------------------------------------|
| repository_url  | https://github.com/librefonts/averiagruesalibre              |
| commit          | 507ebb471b6a46f3c97cc5ad670264ea9bdff49e                     |
| config_yaml     | none (TTX-only sources)                                      |

## How URL Found

The repository URL `https://github.com/librefonts/averiagruesalibre` was already known from the cached upstream repo at `upstream_repos/fontc_crater_cache/librefonts/averiagruesalibre`. The METADATA.pb has no source block. The librefonts GitHub organization hosts all four Averia Libre family variants (averialibre, averiagruesalibre, averiasanslibre, averiaseriflibre).

## How Commit Identified

The cached repo is a shallow clone with a single visible commit:

- `507ebb4` (2014-10-17) — "update .travis.yml" by hash3g

This is the HEAD of the `master` branch and the only commit available. The parent commit `d239f848` exists but is beyond the shallow boundary.

**Important context about the font in google/fonts**: The TTF currently in google/fonts was last updated by PR #836 ("hotfix-averiagruesalibre: v1.002 added", merged 2017-05-08, by Marc Foley). This hotfix updated the binary from v1.001 to v1.002. The upstream repo's TTX files represent v1.001, meaning the binary in google/fonts was NOT built from this upstream repo's current state — it was a separate hotfix applied directly.

The commit `507ebb4` is the only available reference point for the upstream repo, representing the last known state of the librefonts mirror.

## How Config Resolved

**No gftools-builder compatible sources exist.** The upstream repository contains:

- TTX files (decomposed TTF tables using fontTools 2.4): `AveriaGruesaLibre-Regular.ttf.*.ttx`
- Metadata files: `FONTLOG.txt`, `DESCRIPTION.en_us.html`, `METADATA.json`, `OFL.txt`
- CI config: `.travis.yml` (using old fontbakery-build.py pipeline)
- Supporting files: `src/METADATA_comments.txt`, `src/VERSIONS.txt`

No `.glyphs`, `.ufo`, `.designspace`, `.sfd`, or `.vfb` files exist anywhere in the repository. The TTX files are decomposed binary font tables, not editable font sources. These cannot be used with gftools-builder.

The Averia font family is unique in that it was created algorithmically by averaging the outlines of all 725 Google Web Fonts (as of November 2011). The "source" is essentially the averaging algorithm output, not a traditional font editor project. The original was built with FontForge (per nameID 3: "FontForge : AveriaGruesaLibre-Regular : 13-11-2011").

An override config.yaml cannot be created because there are no gftools-builder compatible source files to reference.

## Conclusion

The upstream repo at `https://github.com/librefonts/averiagruesalibre` is a valid mirror containing TTX decompositions of the v1.001 binary. The font in google/fonts is v1.002 (updated via PR #836 hotfix by Marc Foley in 2017). The source block can be added to METADATA.pb with the repository URL and commit `507ebb4`, but config_yaml cannot be set because the repo contains only TTX files — not gftools-builder compatible sources. This is an inherent limitation of the Averia family, which was created through an algorithmic averaging process rather than traditional font design.
