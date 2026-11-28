# Investigation Report: Hind Mysuru

## Summary

Hind Mysuru is a Kannada typeface designed by Manushi Parikh for Indian Type Foundry (ITF), part of the Hind Multi-Script project. It was onboarded to Google Fonts on September 14, 2015 by Dave Crossland. The upstream repository at `https://github.com/itfoundry/hind-mysuru` is confirmed and cached. The repository uses a custom `hindkit` build system and has no `config.yaml`. An override `config.yaml` referencing `masters/HindMysuru.glyphs` already exists in the google/fonts family directory. The source block in METADATA.pb has a `repository_url` but is missing a `commit` hash. The recommended commit hash is `7d7fe4c` (Compile 1.000, the HEAD and final commit in the repo).

## Key Findings

| Field              | Value                                              |
|--------------------|----------------------------------------------------|
| Family Name        | Hind Mysuru                                        |
| Designer           | Indian Type Foundry (Manushi Parikh)               |
| Repository URL     | https://github.com/itfoundry/hind-mysuru           |
| Commit Hash        | 7d7fe4cfa6f19c057217ed43174dc9a7aef82552           |
| Commit Description | Compile 1.000 (Oct 17, 2015)                      |
| Config             | Override config.yaml in google/fonts               |
| Source File        | masters/HindMysuru.glyphs                          |
| Status             | **missing_config** (needs commit hash in METADATA.pb) |
| Confidence         | MEDIUM                                             |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb contains:
- `name: "Hind Mysuru"`
- `designer: "Indian Type Foundry"`
- `date_added: "2016-01-20"`
- `source { repository_url: "https://github.com/itfoundry/hind-mysuru" }`
- `primary_script: "Knda"`
- Missing: `commit` hash in source block
- Missing: `config_yaml` in source block (not needed since override config.yaml exists locally)

The `repository_url` was added by Simon Cozens in commit 474a446c0 ("More upstreams (g,h)", Jan 14, 2024).

### Google Fonts Git History

1. **b2a8b187d** (Sep 14, 2015) - "Adding Hind Mysuru" by Dave Crossland. Initial onboarding with 5 TTF files (129-132 KB each), DESCRIPTION.en_us.html, METADATA.json, and OFL.txt.
2. **e44e0e005** - date_added updates for ofl/hind* families.
3. **474a446c0** (Jan 14, 2024) - Added `repository_url` to source block.
4. **ca99119fb** - Set `primary_script: "Knda"`.
5. **5ddf312e6** (Feb 20, 2026) - Added override config.yaml referencing `masters/HindMysuru.glyphs`.

The TTF binary files have never been updated since the initial onboarding on Sep 14, 2015.

### Upstream Repository Analysis

- **Repository**: https://github.com/itfoundry/hind-mysuru
- **Cached at**: upstream_repos/fontc_crater_cache/itfoundry/hind-mysuru
- **Status**: Clean, up-to-date with origin/master
- **Single branch**: master
- **No tags**
- **Total commits**: 35

#### Commit Timeline

The repository has a branching history (with merges for release branches) from July 2015 to October 2015:
- First commit: e271997 (Jul 3, 2015) - "Initial commit"
- Last compile before onboarding: 9f9cd9d (Sep 2, 2015) - "Compile 0.703, a usable build"
- Post-onboarding source changes: 3de53f6 (Oct 16, 2015) - "Remove glyphs already in Hind.glyphs"
- Bug fixes: fb354c1 (Oct 16, 2015) - "Improve PHA and PHUU; close #3", 4598734 (Oct 16, 2015) - "Correct HU; close #2"
- Final commit (HEAD): 7d7fe4c (Oct 17, 2015) - "Compile 1.000"

The repository has been completely static since October 17, 2015 (~10 years).

### Onboarding Commit Determination

The google/fonts initial addition was Sep 14, 2015. The latest upstream compile before that date was v0.703 (Sep 2, 2015, commit 9f9cd9d / d7512b5 merge). The "Compile 1.000" commit (7d7fe4c, Oct 17, 2015) came after the onboarding. The fonts currently in google/fonts are from the initial onboarding and were never updated. They are likely built from the v0.703 source state or possibly compiled separately by Dave Crossland.

Since:
1. The repo has been completely static for ~10 years
2. 7d7fe4c is the HEAD/master commit
3. The "Compile 1.000" represents the final, most complete state of the sources
4. No newer fonts were ever added to google/fonts for this family

Using 7d7fe4c (HEAD) as the reference commit is the pragmatic choice. The actual fonts served by Google Fonts may be from an earlier build (v0.703), but the sources at HEAD are the authoritative and final version.

**Confidence: MEDIUM** - The HEAD commit is after the onboarding date, but it is the only meaningful reference point since the repo is dormant.

### Build System

The repository uses a custom `hindkit` build system (`build.py`), not gftools-builder. The build produces OTF files in the `build/` directory, not TTF files. The TTF files in google/fonts were generated separately by the onboarder.

### Source Files

- **masters/HindMysuru.glyphs** - Glyphs source file (1.2 MB)
- The .glyphs file was last modified in commit 4598734 (Oct 16, 2015) - "Correct HU; close #2"
- This is a gftools-builder compatible source format

### Override Config

An override `config.yaml` exists in google/fonts at `ofl/hindmysuru/config.yaml`:
```yaml
sources:
  - masters/HindMysuru.glyphs
```
This was added in commit 5ddf312e6 (Feb 20, 2026). Since the override exists locally, `config_yaml` does not need to be set in METADATA.pb.

## Conclusion

Hind Mysuru has a confirmed upstream repository with gftools-builder compatible sources (.glyphs file). The source block needs a `commit` hash added. The recommended commit is 7d7fe4c (HEAD of master, "Compile 1.000"). An override config.yaml already exists in the google/fonts directory. The METADATA.pb source block should be enriched with the commit hash.

**Status: missing_config** -- The override config.yaml exists, but the commit hash is still missing from the METADATA.pb source block. Once the commit hash is added, status will be complete.
