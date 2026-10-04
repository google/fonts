# Investigation Report: Hind Colombo

## Summary

Hind Colombo is a Sinhala sans-serif font family with 5 weights (Light through Bold), designed by Indian Type Foundry as part of the Hind Multi-Script project. It was onboarded to Google Fonts on 2016-01-15 by Dave Crossland. The upstream repository at `itfoundry/hind-colombo` is confirmed and cached. No config.yaml exists in the upstream repo, but an override config.yaml has already been created in the google/fonts family directory. The METADATA.pb has a `repository_url` but is missing `commit_hash`.

## Key Findings

| Field              | Value                                                    |
|--------------------|----------------------------------------------------------|
| Family Name        | Hind Colombo                                             |
| Designer           | Indian Type Foundry                                      |
| Repository URL     | https://github.com/itfoundry/hind-colombo                |
| Commit Hash        | 3cf4e8b8400db78e2e07c75d162e66eb59e042c5                 |
| Config YAML        | Override config.yaml in google/fonts (sources: masters/HindColombo.glyphs) |
| Status             | complete                                                 |
| Confidence         | HIGH                                                     |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb file contains:
- `date_added: "2016-01-20"` (catalog date)
- `source { repository_url: "https://github.com/itfoundry/hind-colombo" }`
- No `commit_hash` field
- No `config_yaml` field (not needed since override config.yaml exists locally)
- Copyright: 2015 Indian Type Foundry
- Subsets: menu, latin, latin-ext, sinhala

### Git History in google/fonts

| Commit   | Date       | Author          | Description                              |
|----------|------------|-----------------|------------------------------------------|
| b2000ebb7 | 2016-01-15 | Dave Crossland | Add Hind Colombo (initial onboarding)    |
| e44e0e005 | -          | -               | ofl/hind*/METADATA.pb date_added updates |
| 474a446c0 | 2024-01-14 | Simon Cozens   | More upstreams (g,h) -- added repository_url |
| 5ddf312e6 | 2026-02-20 | Felipe Sanches | Add config_yaml enrichment -- created override config.yaml |

The TTF files have not been modified since the initial onboarding commit `b2000ebb7`.

### Upstream Repository Analysis

- **URL**: https://github.com/itfoundry/hind-colombo
- **Cached at**: upstream_repos/fontc_crater_cache/itfoundry/hind-colombo
- **Repo status**: Clean, synced with remote
- **Branches**: master only
- **Tags**: None
- **HEAD (master)**: `3cf4e8b8400db78e2e07c75d162e66eb59e042c5` (2015-10-17, "Merge branch 'hotfix/readme'")

The repository has 30 commits total. The final release commit is "Compile 1.000" (`25cb5d9`, 2015-10-17), followed by a README hotfix merge (`3cf4e8b`). Since the README merge is HEAD and doesn't affect sources, the source state is identical to v1.000.

### Source Files

- **Source file**: `masters/HindColombo.glyphs` (Glyphs format)
- **Build system**: `build.py` using `hindkit` (pre-gftools era)
- **Build output**: OTF files only in `build/` directory
- **No config.yaml** in upstream repo

The upstream repo uses `hindkit`, a custom build system by Indian Type Foundry. The `build/` directory contains only OTF files; the TTFs in google/fonts were compiled separately, likely using the same source but with TTF output settings.

### Onboarding Commit Determination

The onboarding commit `b2000ebb7` in google/fonts was made on 2016-01-15. At that time, the upstream repo HEAD was `3cf4e8b` (2015-10-17). Since no further commits were made to the upstream after that date, the entire repo state at HEAD represents the sources used for onboarding. Confidence is HIGH.

### Override config.yaml

An override config.yaml was created in the google/fonts family directory (commit `5ddf312e6`) with content:
```yaml
sources:
  - masters/HindColombo.glyphs
```

This correctly references the Glyphs source file in the upstream repo.

## Conclusion

**Status: complete**

The source metadata is complete. The repository URL is verified and correct. The recommended commit hash is `3cf4e8b8400db78e2e07c75d162e66eb59e042c5` (HEAD of master, the final state of the repo at the time of onboarding). An override config.yaml already exists in google/fonts. The only missing piece in METADATA.pb is the `commit_hash` field, which should be added.
