# Investigation Report: Lily Script One

**Family Name**: Lily Script One
**Directory**: `ofl/lilyscriptone`
**Designer**: Julia Petretta
**License**: OFL
**Date Added**: 2013-06-05
**Model**: Claude Opus 4.6

## Summary

Lily Script One is a single-weight display script font designed by Julia Petretta. It was added to Google Fonts on 2013-06-05 as part of the pre-GitHub era of the Google Font Directory. The font binary in google/fonts has never been updated since the initial repository commit on 2015-03-07 (when the existing Google Font Directory was migrated to the google/fonts GitHub repo).

## Upstream Repository

**Repository URL**: https://github.com/librefonts/lilyscriptone
**Branch**: master
**Only Commit**: `10a933fbd582e5641b79d8b99247367c603fc83d` (2014-10-17, "update .travis.yml")

The upstream repository is hosted under the `librefonts` GitHub organization, which was created as a post-hoc archive containing fontbakery-compatible source repos for fonts already in the Google Fonts catalog. The repo was created on 2014-07-16, more than a year after the font was added to Google Fonts (2013-06-05). The repo contains only a single commit by user `hash3g` (account no longer exists on GitHub).

The repo is clean and synced with origin. GitHub API confirms the repository is accessible (HTTP 200).

## Source Files

The upstream repository contains the following source files in the `src/` directory:

- `src/LilyScriptOne-Regular.glyphs` — Glyphs format source (gftools-builder compatible)
- `src/LilyScriptOne-Regular-TTF.sfd` — FontForge SFD format
- `src/LilyScriptOne-Regular-OTF.vfb` — FontLab VFB format (binary)
- Various `.ttx` files — TTX table dumps for both TTF and OTF

The `.glyphs` file is the primary gftools-builder compatible source. The `.sfd` and `.vfb` files are alternative legacy formats.

## Font Binary Verification

The font binary in google/fonts (`LilyScriptOne-Regular.ttf`, 37,572 bytes) was added in the initial commit (`90abd17b4`) of the google/fonts repository on 2015-03-07 and has never been modified since. The version string in the binary matches the upstream TTX data:

- **Version**: `Version 1.002;PS 001.001;hotconv 1.0.70;makeotf.lib2.5.58329`
- **Copyright (binary)**: `Copyright (c) 2012, Julia Petretta`
- **Copyright (METADATA.pb)**: `Copyright (c) 2012-2013, Julia Petretta` (minor discrepancy: METADATA.pb adds "-2013")

The name table records in the binary match exactly with those in the upstream TTX file `LilyScriptOne-Regular.ttf._n_a_m_e.ttx`, confirming the binary originated from this source.

## Commit Hash Verification

Since the librefonts repo contains only a single commit (`10a933f`), and the font was added to Google Fonts before this repo even existed, the commit hash simply represents the only available state of this archive repo. The font was likely compiled from the original designer's sources and onboarded directly to the Google Font Directory before 2013-06-05, then the sources were archived to the librefonts organization in 2014.

**Confidence**: HIGH — There is only one commit in the repo, and the name table data matches the binary in google/fonts.

## Config.yaml

**No config.yaml exists** in the upstream repository. The repo predates gftools-builder conventions. The `.travis.yml` references an older fontbakery-build pipeline that is no longer in use.

Since the repo contains a `.glyphs` source file at `src/LilyScriptOne-Regular.glyphs`, an override `config.yaml` can be created in the google/fonts family directory for gftools-builder compatibility.

## PR History

No pull requests were found in the google/fonts repository referencing "Lily Script One" or "lilyscriptone". The font was part of the bulk initial commit that migrated the Google Font Directory to GitHub.

## Contributors

GitHub API reports two contributors to the librefonts repo:
- **vitalyvolkov** (Vitaly Volkov) — 11 contributions
- **xen** — 2 contributions

The single commit is attributed to `hash3g` (account no longer exists on GitHub).

Julia Petretta (the designer) does not appear to have a GitHub account.

## Conclusion

- **Repository URL**: https://github.com/librefonts/lilyscriptone (confirmed accessible)
- **Commit Hash**: `10a933fbd582e5641b79d8b99247367c603fc83d` (only commit in repo)
- **Config**: No config.yaml in upstream repo; override config.yaml needed in google/fonts
- **Source Type**: `.glyphs` (gftools-builder compatible)
- **Status**: missing_config — Has gftools-buildable sources but needs an override config.yaml
- **Confidence**: HIGH
- **Recommended Action**: Create an override `config.yaml` in `ofl/lilyscriptone/` referencing `src/LilyScriptOne-Regular.glyphs`, add source block to METADATA.pb with repository_url and commit hash.
