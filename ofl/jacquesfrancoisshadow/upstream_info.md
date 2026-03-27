# Investigation: Jacques François Shadow

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jacques François Shadow |
| Slug | jacques-francois-shadow |
| License Dir | ofl |
| Repository URL | https://github.com/cyrealtype/Jacques-Francois-Shadow |
| Commit Hash | unknown |
| Config YAML | none (override config.yaml in google/fonts) |
| Status | missing_commit |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/cyrealtype/Jacques-Francois-Shadow"
}
```

## Investigation

The METADATA.pb contains a `repository_url` but no `commit` hash and no `config_yaml` field.

Git history in google/fonts shows the font was added in the initial commit (`90abd17b4` — "Initial commit"), which predates the gftools-packager era. No commit hash information was recorded at that time.

The METADATA.pb was subsequently updated in commits:
- `21e98aac8` — "More upstreams (i,j,k)" — this added the `repository_url` field
- Various other commits for language metadata, stroke classifications, etc.

The upstream repository `cyrealtype/Jacques-Francois-Shadow` is cached at `upstream_repos/fontc_crater_cache/cyrealtype/Jacques-Francois-Shadow`. The repo has only 3 commits total, with the latest being `073491c` ("Update v1.100"). The upstream does NOT have a `config.yaml` file anywhere in the repository — sources consist only of a `.glyphs` file at `sources/JacquesFrancoisShadow.glyphs`.

An override `config.yaml` already exists in the google/fonts family directory at `ofl/jacquesfrancoisshadow/config.yaml`, added in commit `5ddf312e6` ("Add config_yaml enrichment for 82 font families"). Its contents are:

```yaml
sources:
  - sources/JacquesFrancoisShadow.glyphs
```

Since an override `config.yaml` exists in google/fonts, the `config_yaml` field is intentionally omitted from METADATA.pb (the google-fonts-sources tool auto-detects local overrides).

The font in google/fonts has been there since the initial commit in 2012. The upstream repo shows a version 1.100 update as the latest change. The exact commit used for the original onboarding cannot be determined from commit messages alone, as the onboarding predates gftools-packager.

## Conclusion

The `repository_url` is present and correct. The `config_yaml` field is correctly absent (local override exists). The only missing piece is the `commit` hash. Since this family was onboarded before gftools-packager, the original commit cannot be reliably determined without comparing binary files. The commit hash needs investigation to identify which upstream commit corresponds to the font currently in google/fonts.

## Commit Added (LOW confidence)

Commit `90c9f94cc747ac7c356d882d7553c07d344992f8` was determined by **root_commit**. No upstream commits exist before the binary date (2015-03-07). Used the initial (root) commit of the repository. The repo may have been created after the font was onboarded.
