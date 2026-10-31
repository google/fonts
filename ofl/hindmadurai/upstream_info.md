# Investigation Report: Hind Madurai

## Summary

Hind Madurai is a Tamil typeface designed by Jyotish Sonowal for Indian Type Foundry (ITF), part of the Hind Multi-Script project. It was onboarded to Google Fonts on September 14, 2015 by Dave Crossland, and later updated to v1.001 in a hotfix (PR #892) by Marc Foley on May 8, 2017. The upstream repository at `https://github.com/itfoundry/hind-madurai` is confirmed and cached. The repository's latest commit is "Compile 1.000" from October 2015, but the fonts currently in google/fonts are v1.001 -- a version newer than what exists in the upstream repo. The v1.001 fonts were built externally for the hotfix without updating the upstream repository. An override `config.yaml` already exists in the google/fonts family directory. The source block is missing a `commit` hash.

## Key Findings

| Field              | Value                                              |
|--------------------|----------------------------------------------------|
| Family Name        | Hind Madurai                                       |
| Designer           | Indian Type Foundry (Jyotish Sonowal)              |
| Repository URL     | https://github.com/itfoundry/hind-madurai          |
| Commit Hash        | 3f3bd222489daea4dfec65d5de86012ed4819b5b           |
| Commit Description | Compile 1.000 (Oct 17, 2015)                      |
| Config             | Override config.yaml in google/fonts               |
| Source File        | masters/HindMadurai.glyphs                         |
| Status             | **needs_correction** (fonts in GF are v1.001, newer than upstream v1.000) |
| Confidence         | LOW                                                |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb contains:
- `name: "Hind Madurai"`
- `designer: "Indian Type Foundry"`
- `date_added: "2016-01-20"`
- `source { repository_url: "https://github.com/itfoundry/hind-madurai" }`
- `primary_script: "Taml"`
- Missing: `commit` hash in source block
- Missing: `config_yaml` in source block (not needed since override config.yaml exists locally)

The `repository_url` was added by Simon Cozens in commit 474a446c0 ("More upstreams (g,h)", Jan 14, 2024).

### Google Fonts Git History

1. **d8007c58d** (Sep 14, 2015) - "Adding Hind Madurai" by Dave Crossland. Initial onboarding with 5 TTF files (63-65 KB each).
2. **495992874** (May 8, 2017) - "hotfix-hindmadurai: v1.001 added (#892)" by Marc Foley. Updated all 5 TTF files (significantly larger: 128-143 KB, roughly double the original size). Also updated METADATA.pb and DESCRIPTION.en_us.html.
3. **474a446c0** (Jan 14, 2024) - Added `repository_url` to source block.
4. **c4992a66b** - Added `primary_script: "Taml"`.
5. **5ddf312e6** (Feb 20, 2026) - Added override config.yaml.

### Hotfix PR #892 Analysis

- **Title**: "hotfix-hindmadurai: v1.001 added"
- **Author**: Marc Foley (@m4rc1e)
- **Merged by**: Dave Crossland (@davelab6)
- **Merged at**: 2017-05-08T21:25:16Z
- **PR body**: Empty (no description provided)

The hotfix doubled the TTF file sizes (from ~63-65 KB to ~128-143 KB), suggesting significant glyph additions or technical improvements. The version string in the TTF confirms v1.001 with ttfautohint parameters: `Version 1.001;PS 1.0;hotconv 1.0.86;makeotf.lib2.5.63406; ttfautohint (v1.5.33-1714) -l 8 -r 50 -G 200 -x 13 -D latn -f taml -w G -W -c -X ""`.

### Upstream Repository Analysis

- **Repository**: https://github.com/itfoundry/hind-madurai
- **Cached at**: upstream_repos/fontc_crater_cache/itfoundry/hind-madurai
- **Status**: Clean, up-to-date with origin/master
- **Single branch**: master
- **No tags**
- **Total commits**: 27

#### Commit Timeline

The repository has a linear history from June 2015 to October 2015:
- First commit: 796382f (Jun 19, 2015) - "Initial commit"
- Last compile before initial onboarding: 6cae7c9 (Aug 28, 2015) - "Compile 0.702"
- Post-onboarding source changes: bca96ce (Oct 16, 2015) - "Remove glyphs already in Hind.glyphs"
- Final commit (HEAD): 3f3bd22 (Oct 17, 2015) - "Compile 1.000"

The repository has been completely static since October 17, 2015 (~10 years).

### Version Mismatch

This is the critical finding: The fonts currently in google/fonts are **v1.001**, while the upstream repository's latest version is **v1.000**. The v1.001 fonts were created for the hotfix PR #892 (May 2017) but the upstream repository was never updated to reflect this version. This means:

1. The v1.001 fonts were built externally (possibly by Marc Foley) without committing the changes back to the upstream repo
2. The upstream repo at HEAD (3f3bd22) does NOT correspond to the fonts served by Google Fonts
3. There is no commit in the upstream repo that matches the v1.001 fonts

### Build System

The repository uses a custom `hindkit` build system (`build.py`), not gftools-builder. The build.py produces OTF files in the `build/` directory. The TTF files were generated separately by the onboarder.

### Source Files

- **masters/HindMadurai.glyphs** - Glyphs source file (961 KB)
- The .glyphs file was last modified in commit bca96ce (Oct 16, 2015) - "Remove glyphs already in Hind.glyphs"
- This is a gftools-builder compatible source format

### Override Config

An override `config.yaml` exists in google/fonts at `ofl/hindmadurai/config.yaml`:
```yaml
sources:
  - masters/HindMadurai.glyphs
```
This was added in commit 5ddf312e6 (Feb 20, 2026).

## Conclusion

Hind Madurai has a confirmed upstream repository with gftools-builder compatible sources. However, there is a significant version mismatch: the fonts in google/fonts are v1.001 (from the 2017 hotfix PR #892 by Marc Foley), while the upstream repo only goes up to v1.000. The v1.001 changes were never committed back to the upstream repository. The recommended commit hash is 3f3bd22 (HEAD, "Compile 1.000"), but this does NOT correspond to the fonts actually served.

**Status: needs_correction** -- The version mismatch between google/fonts (v1.001) and the upstream repo (v1.000) means the upstream repo is incomplete. The commit hash can be set to HEAD (3f3bd22) with a note about the discrepancy, but ideally the v1.001 sources should be located or the discrepancy should be documented.

**Confidence: LOW** -- Due to the version mismatch, we cannot identify a commit that exactly corresponds to the fonts in google/fonts. The HEAD commit represents v1.000 sources, not the v1.001 that is actually served.
