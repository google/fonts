# Investigation Report: Hind Guntur

## Summary

Hind Guntur is a Telugu sans-serif font family with 5 weights (Light through Bold), designed by Indian Type Foundry as part of the Hind Multi-Script project. It was onboarded to Google Fonts on 2016-01-15 by Dave Crossland and has been updated twice since: a v1.001 hotfix (PR #891, 2017) and a hinting update (PR #2378, 2020). The upstream repository at `itfoundry/hind-guntur` is confirmed and cached. No config.yaml exists in the upstream repo, but an override config.yaml has already been created in the google/fonts family directory. The METADATA.pb has a `repository_url` but is missing `commit_hash`.

## Key Findings

| Field              | Value                                                    |
|--------------------|----------------------------------------------------------|
| Family Name        | Hind Guntur                                              |
| Designer           | Indian Type Foundry                                      |
| Repository URL     | https://github.com/itfoundry/hind-guntur                 |
| Commit Hash        | d1f95f8d9a6013297a6a63cc54e48e3885eb5813                 |
| Config YAML        | Override config.yaml in google/fonts (sources: masters/HindGuntur.glyphs) |
| Status             | complete                                                 |
| Confidence         | HIGH                                                     |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb file contains:
- `date_added: "2016-01-20"` (catalog date)
- `source { repository_url: "https://github.com/itfoundry/hind-guntur" }`
- `primary_script: "Telu"`
- No `commit_hash` field
- No `config_yaml` field (not needed since override config.yaml exists locally)
- Copyright: 2015 Indian Type Foundry
- Subsets: latin, latin-ext, menu, telugu

### Git History in google/fonts

| Commit    | Date       | Author           | Description                                   |
|-----------|------------|------------------|-----------------------------------------------|
| 7dea11242 | 2016-01-15 | Dave Crossland   | Add Hind Guntur (initial onboarding)          |
| 334ce6509 | 2017-05-08 | Marc Foley       | hotfix-hindguntur: v1.001 added (#891)        |
| fab83f4be | 2020-10-08 | Saga (Measure+Fit) | HindGuntur, InknutAntiqua, Khula, Padauk Hinting (#2378) |
| ca99119fb | -          | -                | Set primary script                            |
| 474a446c0 | 2024-01-14 | Simon Cozens     | More upstreams (g,h) -- added repository_url  |
| 5ddf312e6 | 2026-02-20 | Felipe Sanches   | Add config_yaml enrichment -- created override config.yaml |

The TTF files were last modified in the hinting update commit `fab83f4be` (2020-10-08). This update was done directly on the TTFs in google/fonts (re-running ttfautohint), not from upstream sources.

### Post-Onboarding Updates

1. **PR #891** (2017-05-08): Marc Foley added v1.001 as a hotfix. This updated all 5 TTFs and the DESCRIPTION.en_us.html. No upstream commit reference was provided -- the v1.001 does not exist in the upstream repo (which only has v1.000).

2. **PR #2378** (2020-10-08): Saga (Measure+Fit) rehinted the fonts with ttfautohint using original parameters. This was a hinting-only update applied directly to the TTFs. The PR body states: "Reran fonts through ttfautohint, using original parameters if they were noted in the name table."

### Upstream Repository Analysis

- **URL**: https://github.com/itfoundry/hind-guntur
- **Cached at**: upstream_repos/fontc_crater_cache/itfoundry/hind-guntur
- **Repo status**: Clean, synced with remote
- **Branches**: master, develop, feature/c2.following (all point to same "Compile 1.000" commit)
- **Tags**: None
- **HEAD (master)**: `d1f95f8d9a6013297a6a63cc54e48e3885eb5813` (2015-10-17, "Compile 1.000")

The repository has 24 commits total. The final commit is "Compile 1.000" (`d1f95f8`, 2015-10-17). No further commits were made to the upstream after this date.

### Source Files

- **Source file**: `masters/HindGuntur.glyphs` (Glyphs format)
- **Build system**: `build.py` using `hindkit` (pre-gftools era)
- **Build output**: OTF files only in `build/` directory
- **No config.yaml** in upstream repo

### Onboarding Commit Determination

The upstream repo has only one commit on master: `d1f95f8` (Compile 1.000, 2015-10-17). This is the HEAD of master and the only possible source commit. The onboarding to google/fonts happened on 2016-01-15, and no further upstream work was done after October 2015. The subsequent updates in google/fonts (v1.001 and hinting) were applied directly to the TTFs without corresponding upstream commits. Confidence is HIGH.

### Override config.yaml

An override config.yaml was created in the google/fonts family directory (commit `5ddf312e6`) with content:
```yaml
sources:
  - masters/HindGuntur.glyphs
```

This correctly references the Glyphs source file in the upstream repo.

## Conclusion

**Status: complete**

The source metadata is complete. The repository URL is verified and correct. The recommended commit hash is `d1f95f8d9a6013297a6a63cc54e48e3885eb5813` (HEAD of master, the "Compile 1.000" commit). Note that the current TTFs in google/fonts differ from what would be built from this commit due to post-onboarding v1.001 hotfix and hinting updates applied directly in google/fonts. An override config.yaml already exists in google/fonts. The only missing piece in METADATA.pb is the `commit_hash` field.
