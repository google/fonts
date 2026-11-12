# Investigation Report: Hind Jalandhar

## Summary

Hind Jalandhar is a Gurmukhi sans-serif font family with 5 weights (Light through Bold), designed by Namrata Goyal for Indian Type Foundry as part of the Hind Multi-Script project. It was onboarded to Google Fonts on 2015-09-14 by Dave Crossland. The upstream repository at `itfoundry/hind-jalandhar` is confirmed and cached. No config.yaml exists in the upstream repo, but an override config.yaml has already been created in the google/fonts family directory. The METADATA.pb has a `repository_url` but is missing `commit_hash`.

## Key Findings

| Field              | Value                                                    |
|--------------------|----------------------------------------------------------|
| Family Name        | Hind Jalandhar                                           |
| Designer           | Indian Type Foundry (Namrata Goyal)                      |
| Repository URL     | https://github.com/itfoundry/hind-jalandhar              |
| Commit Hash        | 27af9e8ea8f29ac810ffc0f76b4f240b70af0b24                 |
| Config YAML        | Override config.yaml in google/fonts (sources: masters/HindJalandhar.glyphs) |
| Status             | complete                                                 |
| Confidence         | MEDIUM                                                   |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb file contains:
- `date_added: "2016-01-20"` (catalog date, adjusted later from original)
- `source { repository_url: "https://github.com/itfoundry/hind-jalandhar" }`
- No `commit_hash` field
- No `config_yaml` field (not needed since override config.yaml exists locally)
- Copyright: 2015 Indian Type Foundry
- Subsets: menu, gurmukhi, latin, latin-ext

### Git History in google/fonts

| Commit    | Date       | Author          | Description                                   |
|-----------|------------|-----------------|-----------------------------------------------|
| 0d3a8c955 | 2015-09-14 | Dave Crossland  | Adding Hind Jalandhar (initial onboarding)    |
| 474a446c0 | 2024-01-14 | Simon Cozens    | More upstreams (g,h) -- added repository_url  |
| 5ddf312e6 | 2026-02-20 | Felipe Sanches  | Add config_yaml enrichment -- created override config.yaml |

The TTF files have not been modified since the initial onboarding commit `0d3a8c955`.

### Timeline Discrepancy

The initial onboarding to google/fonts occurred on **2015-09-14**, but the upstream repo's "Compile 1.000" commit was made on **2015-10-17** -- more than a month later. At the time of onboarding, the latest upstream commit was `6d0af0d` ("Compile 0.702", 2015-08-28). This means the TTFs initially onboarded were likely compiled from v0.702 or an intermediate state.

However, the upstream subsequently reached v1.000, and the repo HEAD (`27af9e8`) represents the most current source state. Since the TTFs in google/fonts were never updated to v1.000, there is a version mismatch between the current fonts on Google Fonts (based on pre-1.000 sources) and the upstream HEAD.

For source metadata purposes, we recommend referencing HEAD (`27af9e8`) as it represents the intended release version (v1.000) of the font. The actual TTFs served may correspond to an earlier state.

### Upstream Repository Analysis

- **URL**: https://github.com/itfoundry/hind-jalandhar
- **Cached at**: upstream_repos/fontc_crater_cache/itfoundry/hind-jalandhar
- **Repo status**: Clean, synced with remote
- **Branches**: master only
- **Tags**: None
- **HEAD (master)**: `27af9e8ea8f29ac810ffc0f76b4f240b70af0b24` (2015-10-17, "Compile 1.000")

The repository has 20 commits total. The final commit is "Compile 1.000" (`27af9e8`, 2015-10-17). No further commits were made to the upstream after this date.

### Source Files

- **Source file**: `masters/HindJalandhar.glyphs` (Glyphs format)
- **Build system**: `build.py` using `hindkit` (pre-gftools era)
- **Build output**: OTF files only in `build/` directory
- **No config.yaml** in upstream repo

### Onboarding Commit Determination

Due to the timeline discrepancy (onboarding predates the v1.000 upstream commit), pinpointing the exact upstream commit used for the original onboarding is uncertain. The initial TTFs were likely based on v0.702 (`6d0af0d`, 2015-08-28) or an intermediate state. However, since the repo is now static and HEAD represents v1.000, we recommend using `27af9e8` as the reference commit for future rebuilds. Confidence is MEDIUM due to the timeline discrepancy.

### Override config.yaml

An override config.yaml was created in the google/fonts family directory (commit `5ddf312e6`) with content:
```yaml
sources:
  - masters/HindJalandhar.glyphs
```

This correctly references the Glyphs source file in the upstream repo.

## Conclusion

**Status: complete**

The source metadata is complete. The repository URL is verified and correct. The recommended commit hash is `27af9e8ea8f29ac810ffc0f76b4f240b70af0b24` (HEAD of master, the "Compile 1.000" commit). Note that the current TTFs in google/fonts may correspond to an earlier version (pre-1.000) since onboarding predated the v1.000 compile. An override config.yaml already exists in google/fonts. The only missing piece in METADATA.pb is the `commit_hash` field.

## Commit Added (MEDIUM confidence)

Commit `6d0af0d80b97ce24b8b1ff61d60f814c8904626d` was determined by **date_correlation**. Found the latest upstream commit before the binary modification date in google/fonts (2015-09-14). This assumes the upstream HEAD at onboarding time was the commit used.
