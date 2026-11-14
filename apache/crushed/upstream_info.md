# Investigation Report: Crushed

## Summary

Crushed is a display sans-serif font designed by Brian J. Bonislawsky (Astigmatic), added to Google Fonts on 2011-01-06 under the Apache 2.0 license. The upstream repository is at `librefonts/crushed` on GitHub. The repository contains only TTX table dumps and a `.vfb` (FontLab) source file -- no gftools-builder compatible sources (`.glyphs`, `.ufo`, `.designspace`) and no `config.yaml`. An override config.yaml is not feasible because there are no compilable source files.

## Key Findings

| Field               | Value                                                    |
|---------------------|----------------------------------------------------------|
| Family Name         | Crushed                                                  |
| Designer            | Astigmatic (Brian J. Bonislawsky)                        |
| License             | Apache 2.0                                               |
| Date Added          | 2011-01-06                                               |
| Repository URL      | https://github.com/librefonts/crushed                    |
| Commit Hash         | 32870f119ec7e05ec914fbe9b99e76aaaa6ecf18                 |
| Branch              | master                                                   |
| Config YAML         | None (no gftools-builder compatible sources)             |
| Source Types         | VFB (FontLab), TTX dumps                                |
| Status              | no_config_possible                                       |
| Confidence          | HIGH                                                     |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb at `apache/crushed/METADATA.pb` has **no source block**. It contains basic metadata: family name, designer, license, font entry with weight 400, subsets (latin, menu), and classifications (DISPLAY, SANS_SERIF).

### Git History in google/fonts

The font was part of the initial commit (`90abd17b4`, 2015-03-07, Dave Crossland) which imported all fonts. The binary was later updated in PR #771 (`8af024d49`, 2017-08-07, Marc Foley) with the commit message "hotfix-crushed: v1.001 added". This hotfix renamed `Crushed.ttf` to `Crushed-Regular.ttf` and updated METADATA.pb. The PR body was empty.

### Upstream Repository

The upstream repo `https://github.com/librefonts/crushed` was created on 2014-07-16. It is part of the `librefonts` organization, which hosts archived copies of Google Fonts sources. The repo has a single commit:

- `32870f1` (2014-10-17): "update .travis.yml" -- this is the only commit and therefore the only possible reference.

The repository is cached at `fontc_crater_cache/librefonts/crushed/`. It is clean with no local modifications.

### Source Files

The repository contains:
- `src/Crushed.vfb` -- FontLab binary source (proprietary format, not gftools-builder compatible)
- Multiple `Crushed.ttf.*.ttx` files -- TTX table dumps from the original binary
- `METADATA.json`, `DESCRIPTION.en_us.html`, `LICENSE.txt`, `COPYRIGHT.txt`
- `.travis.yml` for CI

There are **no** `.glyphs`, `.ufo`, or `.designspace` files. The only source is a `.vfb` file, which cannot be used with gftools-builder. Creating an override `config.yaml` is not possible without compilable sources.

### Onboarding Commit Determination

The librefonts repo has only one commit (`32870f1`), so it is trivially the correct reference. The hotfix in google/fonts (PR #771) appears to have been produced separately by Marc Foley, likely by running a fixup script on the TTF binary directly rather than rebuilding from source.

## Conclusion

**Status: no_config_possible**

The upstream repo exists but only contains VFB (FontLab) and TTX sources, which are not compatible with gftools-builder. No config.yaml can be created.

### Recommended METADATA.pb source block

```
source {
  repository_url: "https://github.com/librefonts/crushed"
  commit: "32870f119ec7e05ec914fbe9b99e76aaaa6ecf18"
  branch: "master"
}
```
