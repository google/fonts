# Investigation Report: Life Savers

**Family Name**: Life Savers
**Directory**: `ofl/lifesavers`
**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Confidence**: HIGH

## METADATA.pb Source Block (Current)

The METADATA.pb already contained a complete source block:

```
source {
  repository_url: "https://github.com/googlefonts/life-savers"
  commit: "76eb6d11fa7a003dae0e05c4fa9e2f00a535d8c2"
  files {
    source_file: "fonts/ttf/LifeSavers-Regular.ttf"
    dest_file: "LifeSavers-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/LifeSavers-Bold.ttf"
    dest_file: "LifeSavers-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/LifeSavers-ExtraBold.ttf"
    dest_file: "LifeSavers-ExtraBold.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Upstream Repository

- **URL**: https://github.com/googlefonts/life-savers
- **Local cache**: `upstream_repos/fontc_crater_cache/googlefonts/life-savers/`
- **Branch**: `main` (only branch)
- **Total commits**: 1 (the entire repository consists of a single commit)
- **Repo status**: Clean, up to date with origin

The upstream repository was created by Emma Marichal and contains only a single commit (`76eb6d1`), dated 2024-06-14, with the message "Last few fixes". This commit is the initial (and only) commit in the repo, establishing the entire project structure.

## Commit Verification

The commit hash `76eb6d11fa7a003dae0e05c4fa9e2f00a535d8c2` referenced in METADATA.pb was verified:

- **Exists in upstream repo**: Yes (it is the sole commit)
- **Author**: Emma Marichal (bonjour@emmamarichal.fr)
- **Date**: 2024-06-14 13:44:12 +0200
- **Message**: "Last few fixes"

### Binary File Verification

SHA-256 checksums were compared between the google/fonts directory and the upstream repo at the referenced commit. All three font files matched exactly:

| File | SHA-256 |
|------|---------|
| LifeSavers-Regular.ttf | `9cfbf78067b2f17079be543d38bc614ddad23cc6e9c61f119b2ad96289236056` |
| LifeSavers-Bold.ttf | `cbcc2ded1b108aca167abc1a8d752b1deb975c445611c0fb725d32d21dcfb000` |
| LifeSavers-ExtraBold.ttf | `a7392b6a21ec8f22e5019d0adf9945fc4acba8761d4ff1e53eec65c9a230b454` |

This confirms the fonts in google/fonts were taken directly from the upstream repo at this exact commit.

## config.yaml

The upstream repository has a `config.yaml` at `sources/config.yaml`:

```yaml
sources:
  - LifeSavers.glyphs
familyName: Life Savers
buildVariable: False
```

This file was verified to exist at the referenced commit. The METADATA.pb correctly references it via `config_yaml: "sources/config.yaml"`. No override config.yaml exists in the google/fonts family directory.

## Google Fonts PR History

The font files were updated in google/fonts via **PR #7866**, titled "Life Savers: Version 3.100; ttfautohint (v1.8.4.7-5d5b) added":

- **Created**: 2024-06-14 by Emma Marichal (@emmamarichal)
- **Merged**: 2024-06-21 by Marc Foley (@m4rc1e)
- **Commit in google/fonts**: `a3992f870398414db5111519debe3ee0f7cccafd`
- **Merge commit**: `1cdbb7b7bd437198acf85f2cc4ae2c56f1ab2521`

The PR body explicitly stated: "Taken from the upstream repo https://github.com/googlefonts/life-savers at commit https://github.com/googlefonts/life-savers/commit/76eb6d11fa7a003dae0e05c4fa9e2f00a535d8c2."

The same message appeared in the commit body of the google/fonts commit `a3992f87`. This PR added the source block to METADATA.pb, updated copyright strings, and replaced the font binaries with the Version 3.100 files.

### Earlier History

The font was originally added to Google Fonts on 2012-08-13 (commit `90abd17b4`). A previous version update (v3.001) was applied in 2019 via PR #1473 (commit `177d8ea72`), authored by Marc Foley. The 2024 update (PR #7866) brought it to Version 3.100.

## Source Files

The upstream repository contains:
- `sources/LifeSavers.glyphs` -- Glyphs source file
- `sources/CustomFilter_GF_Latin_All.plist` -- custom filter for Glyphs
- `sources/config.yaml` -- gftools-builder configuration
- Build scripts in `scripts/` directory
- Pre-built fonts in `fonts/ttf/`, `fonts/otf/`, `fonts/webfonts/`

## Conclusion

The METADATA.pb source block for Life Savers is **complete and correct**. The repository URL, commit hash, file mappings, branch, and config_yaml path were all verified. The binary files in google/fonts are byte-identical to those in the upstream repo at the referenced commit. The source block was added as part of the Version 3.100 update in PR #7866 by Emma Marichal, and the same commit hash is documented both in the METADATA.pb and in the google/fonts commit message. No changes are needed.
