# Investigation: Itim

## Summary

| Field | Value |
|-------|-------|
| Family Name | Itim |
| Slug | itim |
| License Dir | ofl |
| Repository URL | https://github.com/cadsondemak/itim |
| Commit Hash | eb5e37a5412ea61cbc048f57dad5a97285d470e1 |
| Config YAML | override config.yaml in google/fonts (ofl/itim/config.yaml) |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/cadsondemak/itim"
  commit: "eb5e37a5412ea61cbc048f57dad5a97285d470e1"
}
```

## Investigation

The font was added to google/fonts in commit `daa233403` ("Adding Itim"). The font's date_added is "2015-07-01".

The METADATA.pb source block has only `repository_url` and `commit` — no `files`, no `branch`, no `config_yaml`.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/cadsondemak/itim`. The commit `eb5e37a5412ea61cbc048f57dad5a97285d470e1` was verified to exist in the cached repo (2015-06-27, "Merge pull request #1 from davelab6/master"). This matches the font's `date_added` of 2015-07-01 (within days), confirming this is the correct onboarding commit.

**Source format**: The repository contains `sources/Itim-Regular.ufo`, `sources/Itim.glyphs`, `sources/Itim-Regular.vfb`, `sources/Itim-Regular_SS01.vfb`, and `sources/Itim-Regular_SS02.vfb`. There is **no `config.yaml`** in the upstream repository.

An override `config.yaml` exists in the google/fonts family directory at `ofl/itim/config.yaml`:
```yaml
buildVariable: false
sources:
  - source/Itim-Regular.ufo
```

Per policy, when an override `config.yaml` exists locally, the `config_yaml` field in METADATA.pb is not needed. The current METADATA.pb does not set `config_yaml`, which is correct.

Note: The copyright mentions Pablo Impallari for the initial OpenType handwriting feature development. The font supports Latin and Thai scripts.

The git log for the upstream repo shows the commit `eb5e37a5` is the 3rd-oldest commit in the repository (2015-06-27), close to the initial push of font files.

## Conclusion

The source block has `repository_url` and `commit` correctly set. The commit `eb5e37a5` is verified against the cached repository. An override `config.yaml` exists in the google/fonts directory using the UFO source. No changes needed.
