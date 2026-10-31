# Investigation Report: Orelega One

## Summary

| Field | Value |
|-------|-------|
| **Family Name** | Orelega One |
| **Status** | complete (SFD-only sources) |
| **Repository URL** | https://gitlab.com/haleyhalcyon/orelega |
| **Commit Hash** | `756e15cc3dfeb958aafefc2e05db493e4473f0bd` |
| **Config YAML** | none (SFD-only sources) |
| **Confidence** | HIGH |

## Current State in google/fonts

The METADATA.pb at `ofl/orelegaone/METADATA.pb` has:
```
source {
  repository_url: "https://github.com/JapanYoshi/Orelega"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "ttf/OrelegaOne-Regular.ttf"
    dest_file: "OrelegaOne-Regular.ttf"
  }
  branch: "master"
}
```

The URL `https://github.com/JapanYoshi/Orelega` returns **HTTP 404** — the repository has been deleted or moved.

No commit hash is recorded.

## How the Correct URL Was Found

The designer Haruki Wakamatsu (JapanYoshi) migrated the repository from GitHub to GitLab. The new URL is `https://gitlab.com/haleyhalcyon/orelega`, which returns **HTTP 200**.

The GitLab repo contains the complete git history (81 commits), including the original commits made under the JapanYoshi account. The repository retains the full development history from the GitHub era.

## How the Commit Hash Was Identified

The google/fonts commit that added this font:
```
commit 38c4e065b473adfad469f67fad7fff4d160f7d99
Date: 2021-03-15

    Orelega One: Version 1.1 ; ttfautohint (v1.8.3) added (#3174)

    * [gftools-packager] Orelega One: Version 1.1 ; ttfautohint (v1.8.3) added
    * Orelega One Version 1.1 ; ttfautohint (v1.8.3) taken from the upstream repo
      https://github.com/JapanYoshi/Orelega.git at commit
      https://github.com/JapanYoshi/Orelega/commit/756e15cc3dfeb958aafefc2e05db493e4473f0bd.
```

The commit `756e15c` exists in the GitLab repo and is a merge commit:
```
commit 756e15cc3dfeb958aafefc2e05db493e4473f0bd
Merge: 6507c26 5e2d6de
Author: JapanYoshi <japanyoshi777@gmail.com>
Date:   Fri Mar 12 18:26:22 2021 +0900

    Merge pull request #4 from yanone/master

    Orelega -> Orelega One, ready for GF
```

## Verification

### Binary File Match
MD5 of `OrelegaOne-Regular.ttf`:
- google/fonts: `dc05a44a894cc0cc0621893e741e3a71`
- GitLab repo at `ttf/OrelegaOne-Regular.ttf`: `dc05a44a894cc0cc0621893e741e3a71`

**Identical match.** The binary in google/fonts is the same as the one in the upstream repo at the HEAD of master (and no commits after `756e15c` modified the TTF).

### Source Type
The repository uses **FontForge `.sfdir`** format (`OrelegaOne-Regular.sfdir/` directory with individual `.glyph` files). The build process uses a custom `build.sh`:
```bash
TTF="ttf/OrelegaOne-Regular.ttf"
rm $TTF
set -e
fontforge -c 'open(argv[1]).generate(argv[2])' OrelegaOne-Regular.sfdir $TTF
ttfautohint -t $TTF $TTF.hinted
mv $TTF.hinted $TTF
gftools fix-unwanted-tables $TTF
gftools fix-dsig --autofix $TTF
```

This is **not gftools-builder compatible** — there is no config.yaml and none is applicable.

### URL Verification
- `https://github.com/JapanYoshi/Orelega` → HTTP 404 (deleted/migrated)
- `https://gitlab.com/haleyhalcyon/orelega` → HTTP 200 (active)

### Post-Onboarding Upstream Work
8 commits after `756e15c` in the GitLab repo (Cyrillic kerning, Shavian script support, README updates, pronunciation notes). These changes are NOT in google/fonts and would need separate review.

## What Needs to Change

In `ofl/orelegaone/METADATA.pb`, the source block should be updated:
1. Fix `repository_url` from `https://github.com/JapanYoshi/Orelega` to `https://gitlab.com/haleyhalcyon/orelega`
2. Add `commit: "756e15cc3dfeb958aafefc2e05db493e4473f0bd"`
