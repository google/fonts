# Investigation: Jacques François

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jacques François |
| Slug | jacques-francois |
| License Dir | ofl |
| Repository URL | https://github.com/cyrealtype/Jacques-Francois |
| Commit Hash | unknown |
| Config YAML | none (override config.yaml in google/fonts) |
| Status | missing_commit |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/cyrealtype/Jacques-Francois"
}
```

## Investigation

The METADATA.pb contains a `repository_url` but no `commit` hash and no `config_yaml` field.

Git history in google/fonts shows the font was added in the initial commit (`90abd17b4` — "Initial commit"), which predates the gftools-packager era. No commit hash information was recorded at that time.

The METADATA.pb was subsequently updated in commits:
- `21e98aac8` — "More upstreams (i,j,k)" — this added the `repository_url` field
- Various other commits for language metadata, stroke classifications, etc.

The upstream repository `cyrealtype/Jacques-Francois` is cached at `upstream_repos/fontc_crater_cache/cyrealtype/Jacques-Francois`. The repo has 6 commits total, with the latest being `d341563` ("regenerated fonts v1.100"). The upstream does NOT have a `config.yaml` file anywhere in the repository — sources consist only of a `.glyphs` file at `sources/JacquesFrancois.glyphs`.

An override `config.yaml` already exists in the google/fonts family directory at `ofl/jacquesfrancois/config.yaml`, added in commit `5ddf312e6` ("Add config_yaml enrichment for 82 font families"). Its contents are:

```yaml
sources:
  - sources/JacquesFrancois.glyphs
```

Since an override `config.yaml` exists in google/fonts, the `config_yaml` field is intentionally omitted from METADATA.pb (the google-fonts-sources tool auto-detects local overrides).

The font in google/fonts has been there since the initial commit in 2012. The upstream repo shows a version 1.100 regeneration as the latest change. The exact commit used for the original onboarding cannot be determined from commit messages alone, as the onboarding predates gftools-packager.

## Conclusion

The `repository_url` is present and correct. The `config_yaml` field is correctly absent (local override exists). The only missing piece is the `commit` hash. Since this family was onboarded before gftools-packager, the original commit cannot be reliably determined without comparing binary files. The commit hash needs investigation to identify which upstream commit corresponds to the font currently in google/fonts.

## Commit Added (LOW confidence)

Commit `bc37f476a7e982327ae359c67068356597cd45aa` was determined by **root_commit**. No upstream commits exist before the binary date (2015-03-07). Used the initial (root) commit of the repository. The repo may have been created after the font was onboarded.


## Source-metadata correction (2026-06-02) — ⚠ REFRESH REQUIRED

**Model**: Claude Opus 4.8

fontc_crater reported a `missing source` failure for this family because the pinned commit was not usable: it is either absent from the repository (a phantom/deleted hash) or predates the declared source, so the source could not be found.

Corrected the METADATA.pb source block:
- commit: `bc37f476a7e982327ae359c67068356597cd45aa` → `d34156392b110af3e182d07cdfe9649a6f294dab` (2018-02-12)  (repository_url unchanged: `https://github.com/cyrealtype/Jacques-Francois`)

The declared source is confirmed present at the new commit.

**⚠ REFRESH REQUIRED — this does NOT reproduce the shipped binary.** The shipped binary's exact build commit is not recoverable from the current upstream, so the source now resolves and the family becomes buildable, but a rebuild produces an **updated** font, not the originally-shipped artifact. Before shipping any rebuild, a human must QA the output for reflow / vertical-metric / glyph-coverage / version differences. The original build provenance (the exact source + commit that produced the shipped binary) is not recoverable from the current upstream.
