# Dorsa

**Date investigated**: 2026-02-27
**Status**: missing_config
**Designer**: Santiago Orozco
**METADATA.pb path**: `ofl/dorsa/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/dorsa |
| Commit | `90d5bffc5b005be8d3f7728ccb9aae3deaae1c23` |
| Config YAML | -- |
| Branch | master |

## How the Repository URL Was Found

The upstream repository is located at https://github.com/librefonts/dorsa (HTTP 200 verified). This was found by checking the existing clone at `upstream_repos/fontc_crater_cache/librefonts/dorsa`, whose git remote points to this URL. The librefonts GitHub organization was used to host source files for many early Google Fonts families. The METADATA.pb currently has no `source {}` block or `repository_url` field.

## How the Commit Hash Was Identified

The upstream repository contains exactly one commit: `90d5bffc5b005be8d3f7728ccb9aae3deaae1c23` (2014-10-17, by hash3g, message: "update .travis.yml"). This is the initial and only commit in the repository, which imported the SFD source, TTX decomposition files, METADATA.json, DESCRIPTION, OFL license, and a Travis CI configuration. Since there is only one commit, it is trivially the correct reference point for the complete state of the upstream source.

Note that the font was originally added to Google Fonts on 2011-08-31 (per `dateAdded` in METADATA.pb), well before this upstream repo was created in October 2014. The SFD file's internal timestamps show creation on 2011-05-19 and last modification on 2011-09-04. The librefonts repo was created as a retroactive archive of the font sources, not as a development repository.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository, and no override `config.yaml` exists in the `google/fonts/ofl/dorsa/` directory. The only source file is an SFD (FontForge Spline Font Database) file: `src/Dorsa-Regular-TTF.sfd`. SFD files are not compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. Therefore, no config.yaml can be meaningfully created for this family without first converting the sources to a compatible format.

The Travis CI configuration (`.travis.yml`) shows the font was built using `fontbakery-build.py`, an older build pipeline that predates gftools-builder.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2014-10-17 13:35:02 +0300
- Commit message: "update .travis.yml"
- Source files at commit: `src/Dorsa-Regular-TTF.sfd`, `src/METADATA_comments.txt`, `src/VERSIONS.txt`, plus TTX decomposition files, DESCRIPTION.en_us.html, METADATA.json, OFL.txt, .travis.yml

## Confidence

**HIGH**: The upstream repository at librefonts/dorsa is the canonical source archive for this font. It has only a single commit containing the complete SFD source, making commit identification unambiguous. The font copyright matches between the SFD file, METADATA.pb, and METADATA.json (Santiago Orozco, 2011). The repository URL is verified accessible. The only limitation is the lack of gftools-builder-compatible sources (SFD only), which means no config.yaml can be provided.
