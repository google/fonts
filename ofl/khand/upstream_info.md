# Investigation: Khand

## Summary

| Field | Value |
|-------|-------|
| Family Name | Khand |
| Slug | khand |
| License Dir | ofl |
| Repository URL | https://github.com/itfoundry/khand |
| Commit Hash | unknown |
| Config YAML | none (custom build system) |
| Status | missing_commit |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/itfoundry/khand"
}
primary_script: "Deva"
```

## Investigation

The METADATA.pb contains `repository_url` but no `commit` or `config_yaml`. The upstream repository `itfoundry/khand` is cached at `upstream_repos/fontc_crater_cache/itfoundry/khand`.

The repository uses the same custom build system as Karma (Indian Type Foundry's Python-based tool). The `masters/` directory contains:
- `Khand_0.ufo` and `Khand_0.vfb` (FontLab)
- `Khand_1.ufo` and `Khand_1.vfb` (FontLab)

The build process uses `build.py` with ITF's custom `itf.py` scripts. No `config.yaml` exists in the repository.

The last upstream commit is `1f1d677` ("Compile 2.000"), dated November 21, 2014. The google/fonts commit history shows updates: `21bb9bd12` ("hotfix-khand: v1.101 added (#899)") and `2f26ba721` ("Corrected outlines of Iacute and Igrave (#5507)"). The hotfix was around May 2017.

## Conclusion

The source block needs a `commit` field. The commit to use is likely `1f1d677` ("Compile 2.000" from Nov 2014) or an earlier version corresponding to the initial onboarding. No `config.yaml` is possible as the repository uses ITF's custom build system (Python scripts with FontLab/UFO sources).

## Commit Added (HIGH confidence)

Commit `1f1d6778d3a940999b543313b2371fa76b16a978` was determined by **tag_match**. Matched a version tag in the upstream repo whose date is on or before the binary modification date in google/fonts (2022-11-09). This is the most reliable method.
