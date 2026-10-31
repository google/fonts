# Investigation: Flavors

## Summary

| Field | Value |
|---|---|
| Family Name | Flavors |
| Designer | Sideshow (Dave 'Squid' Cohen / Font Diner) |
| License | OFL |
| Date Added | 2011-12-19 |
| Category | DISPLAY, HANDWRITING |
| Repository URL | https://github.com/librefonts/flavors |
| Commit | `494aad3c703cd55dfa728cded360b49e128dc101` |
| Branch | master |
| Config YAML | N/A (no buildable sources) |
| Status | no_buildable_sources |
| Confidence | HIGH |

## Upstream Repository

The upstream repository is `https://github.com/librefonts/flavors`, a mirror/archive created by Mikhail Kashkin (GitHub: hash3g) on 2014-07-16. The initial commit message is "Move flavors font files to separate repository", indicating this was extracted from a larger collection (likely the googlefontdirectory monorepo).

The repository has 10 commits total, all from 2014, with the last one on 2014-10-17 being a Travis CI configuration update. The repo has not been modified since.

### Commit History

| Commit | Date | Description |
|---|---|---|
| `629e1902dab3` | 2014-07-16 | Move flavors font files to separate repository (initial) |
| `bb8f7555dff2` | 2014-08-19 | Added .travis.yml |
| `67b1df3556d3` | 2014-08-21 | Travis.yml update |
| `8baf74b89005` | 2014-08-22 | Travis.yml update |
| `bf724f96a07d` | 2014-09-11 | update .travis.yml |
| `a67001dbf329` | 2014-09-14 | Installing ttfautohint from ppa |
| `74d03e6aaab9` | 2014-09-15 | Update .travis.yml |
| `c70aa0b57440` | 2014-09-19 | Update .travis.yml |
| `a2e43e07252c` | 2014-10-06 | Rename fontbakery |
| `494aad3c703c` | 2014-10-17 | update .travis.yml (HEAD) |

All commits after the initial one are Travis CI configuration changes. No font source files were modified after the initial commit.

## Source Files

The repository contains:

- `src/Flavors-Regular-TTF.vfb` - FontLab binary format (VFB), not buildable with gftools-builder
- `Flavors-Regular.ttf.*.ttx` - TTX table dumps (17 files), decomposed from the TTF binary
- `FONTLOG.txt`, `DESCRIPTION.en_us.html`, `METADATA.json`, `OFL.txt` - metadata files

There are NO gftools-builder compatible source files (.glyphs, .ufo, .designspace, .sfd). The only source is a VFB file, which is a proprietary FontLab format.

## Google Fonts History

### Initial Addition (2015-03-07)

Flavors was part of the initial commit (`90abd17b4`) by Dave Crossland. The TTF file was 186,640 bytes, Version 1.000.

### Name Table Fix - PR #1362 (merged 2019-07-08)

PR [#1362](https://github.com/google/fonts/pull/1362) by laerm0 (Micah Stupak) applied a FontForge roundtrip to fix an OS X name table validation issue. The TTF was updated to v1.01 (184,784 bytes). This was a direct fix, not built from the upstream repository. Commit `7da86e3f4`.

This is the last commit that modified the TTF file. The current binary in google/fonts does NOT correspond to any commit in the upstream repository -- it was modified directly by a FontForge roundtrip after the initial onboarding.

## Commit Hash Verification

The recorded commit `494aad3c703cd55dfa728cded360b49e128dc101` is the latest commit in the upstream repository (HEAD of master). Since the upstream repo is a mirror created in 2014 and the font was initially onboarded from the googlefontdirectory, and since all commits after the initial one are Travis CI changes only, this commit effectively represents the same font sources as the initial commit.

The font in google/fonts was further modified by PR #1362 (FontForge roundtrip, 2017) which was not reflected in the upstream repo. The upstream repo accurately represents the pre-fix version of the sources.

## Config YAML

No config.yaml is possible. The only source file is a VFB (FontLab binary), which cannot be built with gftools-builder. No override config.yaml should be created.

## METADATA.pb Source Block

Currently on main, there is no source block. A source block was added on branch `sources_info_2026-02-25` (commit `9a14639f3`) but has not been merged to main yet.

The proposed source block:

```
source {
  repository_url: "https://github.com/librefonts/flavors"
  commit: "494aad3c703cd55dfa728cded360b49e128dc101"
}
```

This is correct. No `config_yaml` field is needed since there are no buildable sources.

## Conclusion

Flavors is a display font by Font Diner (Dave 'Squid' Cohen). The upstream repository at `librefonts/flavors` is a mirror with VFB-only sources. The font cannot be rebuilt with gftools-builder. The source block with repository URL and commit hash is correct and complete for this family's capabilities. Status is `no_buildable_sources` -- the VFB format is proprietary and not supported by modern open-source font build tooling.
