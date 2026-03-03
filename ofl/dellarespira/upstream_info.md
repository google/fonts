# Della Respira

## Summary

Della Respira is a serif display typeface designed by Nathan Willis, a revival of the Della Robbia typeface by American Type Founders (ATF). The original source was hosted on Launchpad using Bazaar version control, not GitHub. A librefonts mirror exists on GitHub but contains only TTX-decomposed files, not real font sources.

## Key Findings

- **Designer**: Nathan Willis
- **Date added to Google Fonts**: 2012-04-04
- **Original source**: Launchpad (https://launchpad.net/revivalism-fonts/) using Bazaar VCS
- **GitHub mirror**: https://github.com/librefonts/dellarespira (TTX-only, not buildable)
- **Source formats available**: TTX decomposed files only (in librefonts mirror)
- **config.yaml**: None (not applicable - no gftools-buildable sources)
- **Override config.yaml**: None in google/fonts

## Repository Analysis

The librefonts/dellarespira GitHub repo was created by Mikhail Kashkin on 2014-07-16 as a mirror of the font data. It contains only TTX-decomposed font table files (the binary .ttf decompiled into XML), not actual editable font sources (.glyphs, .ufo, .sfd, etc.). The repo has 11 commits, all related to CI/Travis setup and TTX file organization.

The actual font source was maintained on Launchpad at `lp:revivalism-fonts` using Bazaar (bzr) version control. The Launchpad project page is still accessible.

## google/fonts History

The font binary has not been updated since the initial commit (90abd17b4) of the google/fonts repository. No gftools-packager updates or font refreshes have occurred.

## Status

- **repository_url**: The librefonts mirror exists but has no buildable sources. The actual source was on Launchpad.
- **commit**: N/A (no useful commit to reference in the TTX-only mirror)
- **config_yaml**: N/A (no gftools-buildable sources exist)
- **Overall**: no_upstream_repo - The only GitHub repo is a TTX mirror with no real font sources. The original Launchpad/Bazaar source is the true upstream but is not a GitHub repository.

## Recommendation

Status should remain `no_upstream_repo`. The librefonts mirror contains only TTX decomposed files and is not suitable as a build source. The original source on Launchpad uses Bazaar VCS which is not compatible with the Google Fonts toolchain.
