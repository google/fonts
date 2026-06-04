# Dr Sugiyama

**Date investigated**: 2026-02-27
**Status**: missing_config
**Designer**: Sudtipos (Alejandro Paul)
**METADATA.pb path**: `ofl/drsugiyama/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/drsugiyama |
| Commit | `11d194b70af6df309a24c9395f64280172839879` |
| Config YAML | None (SFD-only sources) |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/drsugiyama` was identified from the tracking data and verified to be accessible (HTTP 200). This is a librefonts mirror repository created by Mikhail Kashkin on 2014-07-16, with the initial commit message "Move drsugiyama font files to separate repository." The repo contains TTX-decomposed font table files and FontForge SFD/VFB source files.

No `repository_url` field exists in the current METADATA.pb - the file has no `source { }` block at all. The METADATA.pb only contains basic font metadata (name, designer, license, category, fonts, subsets, classifications).

## How the Commit Hash Was Identified

The upstream repository has 12 commits total, all by Mikhail Kashkin (hash3g), spanning from 2014-07-16 to 2014-10-17. The most recent (and HEAD) commit is `11d194b70af6df309a24c9395f64280172839879` ("update .travis.yml", 2014-10-17).

The font binary in google/fonts has never been updated since the initial commit `90abd17b4` (2015-03-07, "Initial commit" by Dave Crossland), which was a massive import of the entire Google Fonts library. The font was originally added to Google Fonts on 2011-11-30 (per `date_added` in METADATA.pb), well before the librefonts mirror was created in 2014.

Since the upstream repo is merely a mirror that was created after the font was already in Google Fonts, the commit hash is not a traditional "onboarding commit." However, the HEAD commit `11d194b` represents the latest state of the repository and all changes between the initial commit and HEAD are limited to `.travis.yml` and a minor `DESCRIPTION.en_us.html` update - no source file changes occurred.

The original commit `29ab091f4611e197b5c4442d17b2c8c0d8bcd13f` (2014-07-16) contains the actual font data. All subsequent commits (10 more) only modified `.travis.yml` CI configuration and the HTML description file.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository. The source files are:

- `src/DrSugiyama-Regular-TTF.sfd` - FontForge SFD format
- `src/DrSujiyama-Regular-OTF.vfb` - FontLab VFB format (binary, proprietary)

These are legacy source formats that are not compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` files. An override `config.yaml` cannot be created because there are no gftools-builder compatible sources to reference.

The repository also contains TTX-decomposed table files (XML representations of the compiled font tables), but these are not editable font sources.

Note: The original font name uses a variant spelling "Dr Sujiyama" in the VFB filename and copyright notice, while the published name is "Dr Sugiyama."

## Verification

- **Repository URL**: Verified accessible at https://github.com/librefonts/drsugiyama (HTTP 200)
- **Font binary unchanged**: The TTF in google/fonts was added in the initial commit (`90abd17b4`, 2015-03-07) and has never been modified since
- **Source file integrity**: The SFD source file in the upstream repo has not changed since the initial commit `29ab091f` (2014-07-16)
- **No config.yaml**: Confirmed absent from both upstream repo and `ofl/drsugiyama/` in google/fonts
- **Version**: Font is Version 1.000 (per name table and VERSIONS.txt)

## Confidence

**MEDIUM** - The repository URL is confirmed and the repo does contain the font's SFD source. However, this is a librefonts mirror created after the font was already in Google Fonts, not the original upstream source. The original source was likely maintained by Alejandro Paul / Sudtipos, and the font copyright dates to 2004. The librefonts mirror was created by Mikhail Kashkin as part of a broader effort to organize Google Fonts sources into individual GitHub repositories. Since the sources are SFD/VFB only (not gftools-builder compatible), a config.yaml cannot be created.

## Recommendation

The status should remain `missing_config` with the note "SFD-only sources (FontForge format), not gftools-builder compatible." A `source { }` block could be added to METADATA.pb referencing the librefonts repo, but no `config_yaml` can be set since the sources are incompatible with gftools-builder. The commit hash should reference `11d194b70af6df309a24c9395f64280172839879` (HEAD of master) since no source files changed across the repo's history.
