# Investigation: Lalezar

## Summary

| Field | Value |
|-------|-------|
| Family Name | Lalezar |
| Slug | lalezar |
| License Dir | ofl |
| Repository URL | https://github.com/BornaIz/Lalezar |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_commit |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/BornaIz/Lalezar"
}
```

## Investigation

The METADATA.pb has a `repository_url` pointing to `https://github.com/BornaIz/Lalezar` but no commit hash.

The google/fonts git history for `ofl/lalezar/Lalezar-Regular.ttf` shows:
- `1251c0373` — "lalezar: v1.004 added (#682)" — this was the initial onboarding

The PR body for `1251c0373` does not include a gftools-packager upstream commit reference.

The upstream repo at `upstream_repos/fontc_crater_cache/BornaIz/Lalezar/` has only a single commit:
- `238701c` — "Merge pull request #12 from m4rc1e/gf"

This single commit contains work from Marc Foley (m4rc1e), suggesting a PR was merged to prepare the fonts for Google Fonts. The repository appears to have only one commit in its history, which would be the correct commit to reference.

No `config.yaml` was found in the upstream repo at this commit.

## Conclusion

The repository URL is present but the commit hash is missing. The upstream repo has only one commit (`238701c`), which is the most likely candidate for the onboarding commit. The source block should be updated with the commit hash. A `config.yaml` would also need to be investigated or created as an override.

## Commit Added (HIGH confidence)

Commit `c3e0eae24240424069cd8c1b4350a6101346fb7b` was determined by **tag_match**. Matched a version tag in the upstream repo whose date is on or before the binary modification date in google/fonts (2017-05-01). This is the most reliable method.
