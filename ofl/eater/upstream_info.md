# Investigation Report: Eater

- **Date investigated**: 2026-02-27
- **Status**: missing_config
- **Designer**: Vernon Adams (Typomondo)
- **METADATA.pb path**: ofl/eater/METADATA.pb

## Source Data

| Field           | Value |
|-----------------|-------|
| repository_url  | https://github.com/librefonts/eater |
| commit          | 91120e636b79d400473167dae30ff31a7c03b813 |
| config_yaml     | N/A (SFD-only sources) |

## How URL Was Found

The METADATA.pb file does not contain a `source` block or `repository_url`. The upstream repository was identified from the existing local clone at `upstream_repos/fontc_crater_cache/librefonts/eater`, whose remote points to `https://github.com/librefonts/eater`. The URL was verified accessible (HTTP 200).

This is a librefonts-organization repo, which is part of the collection of font sources migrated from the old Google Font Directory. The copyright in OFL.txt and METADATA.pb attributes the font to "Vernon Adams DBA Typomondo (vern@newtypography.co.uk)".

## How Commit Hash Was Identified

The upstream repository contains exactly **one commit**:

- `91120e6` (2014-10-17) "update .travis.yml" by hash3g

Since there is only a single commit in the entire repository, there is no ambiguity about which commit to reference. This commit contains the complete initial import: SFD source files, TTX decompositions of the binary font, METADATA.json, OFL.txt, DESCRIPTION.en_us.html, and the Travis CI configuration.

The font was added to google/fonts in commit `90abd17b4` (2015-03-07, "Initial commit" by Dave Crossland), with a binary size of 83,928 bytes. The font's `date_added` in METADATA.pb is 2011-12-19, indicating the font was originally part of the Google Font Directory before the google/fonts repository was created. The librefonts repo was created later (2014-10-17) as a source archive.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository or in the google/fonts family directory.

The upstream repository contains only FontForge SFD source files:
- `src/Eater-Regular.sfd` (PostScript-flavored SFD)
- `src/Eater-Regular-TTF.sfd` (TrueType-flavored SFD)

SFD files are not compatible with gftools-builder, which requires .glyphs, .ufo, or .designspace sources. A config.yaml override cannot be created without converting the sources to a supported format first. The font would need to be migrated to a modern source format before a config.yaml can be provided.

## Verification

- **Repository URL**: Verified accessible (HTTP 200)
- **Repository is clean**: Confirmed (no local modifications, up to date with origin)
- **Commit count**: 1 (no ambiguity)
- **Source format**: SFD (FontForge) -- not compatible with gftools-builder
- **Binary in google/fonts**: Eater-Regular.ttf (83,928 bytes), unchanged since initial commit (2015-03-07)
- **No config.yaml**: Neither in upstream nor in google/fonts family directory

## Confidence

**HIGH** -- The repository URL is verified and the commit hash is unambiguous (single commit in repo). The "missing_config" status is due to SFD-only sources that are incompatible with gftools-builder; no override config.yaml can be created without source format conversion.
