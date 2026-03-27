# Investigation: Laila

## Summary

| Field | Value |
|-------|-------|
| Family Name | Laila |
| Slug | laila |
| License Dir | ofl |
| Repository URL | https://github.com/itfoundry/laila |
| Commit Hash | unknown |
| Config YAML | none |
| Status | missing_commit |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/itfoundry/laila"
}
```

## Investigation

The METADATA.pb lists `repository_url` pointing to `https://github.com/itfoundry/laila` but has no commit hash.

The google/fonts git history for `ofl/laila/Laila-Regular.ttf` shows:
- `dfb13f742` — "hotfix-laila: v1.302 added (#903)" — 2017-05-16
- `90abd17b4` — "Initial commit"

The PR body for `dfb13f742` does not include a gftools-packager upstream commit reference.

The upstream repo at `upstream_repos/fontc_crater_cache/itfoundry/laila/` has UFO and VFB sources in `masters/`. The most recent commits in the upstream repo predate the google/fonts onboarding (all from 2014), with the latest being `a8b5b4e` "Compile 2.000" (Nov 2014). No later commits were found before the 2017-05-16 google/fonts merge date.

Searching the upstream commits before 2017-05-16 shows `a8b5b4e` as the latest commit. However, the google/fonts hotfix was described as "v1.302", and the upstream shows "Build 1.301" at `62d23b0`. This suggests the v1.302 files may have been prepared offline or through the ITF build system without a corresponding upstream git commit.

The upstream repo uses a custom Python build system (`build.py`, `config.py`) with UFO and VFB source masters. There is no `config.yaml` for gftools-builder.

## Conclusion

The source block exists with the repository URL but is missing the commit hash. The upstream sources are UFO + VFB with a custom build system and no `config.yaml`. An investigation into the ITF build infrastructure would be needed to determine the exact commit used for the v1.302 onboarding. The most likely candidate is `a8b5b4e` (the latest commit before the 2017 google/fonts update), but this cannot be confirmed without further research.

## Commit Added (HIGH confidence)

Commit `a8b5b4ee6cf52508cc0d4f606d4ec0ae4994953a` was determined by **tag_match**. Matched a version tag in the upstream repo whose date is on or before the binary modification date in google/fonts (2017-05-15). This is the most reliable method.
