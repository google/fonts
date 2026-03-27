# Investigation: Karma

## Summary

| Field | Value |
|-------|-------|
| Family Name | Karma |
| Slug | karma |
| License Dir | ofl |
| Repository URL | https://github.com/itfoundry/karma |
| Commit Hash | unknown |
| Config YAML | none (custom build system) |
| Status | missing_commit |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/itfoundry/karma"
}
primary_script: "Deva"
```

## Investigation

The METADATA.pb contains `repository_url` but no `commit` or `config_yaml`. The upstream repository `itfoundry/karma` is cached at `upstream_repos/fontc_crater_cache/itfoundry/karma`.

The repository uses a custom build system (not gftools-builder compatible). The `masters/` directory contains:
- `Karma_0.ufo` and `Karma_0.vfb` (FontLab)
- `Karma_1.ufo` and `Karma_1.vfb` (FontLab)
- Individual weight subdirectories: Bold, Light, Medium, Regular, SemiBold

The build process uses `build.py` with Indian Type Foundry's custom scripts (`itf.py`). There is no `config.yaml` in the repository.

The git log in the cached repo shows the last commit as `1222894` ("Compile 2.000"). The last commit that touched the font files in google/fonts was `08ec04d13` ("hotfix-karma: v1.202 added (#898)", dated May 16, 2017). Without checking the full git log of the upstream, the exact onboarding commit is uncertain.

## Conclusion

The source block needs a `commit` field added. The commit to use would need to be identified by cross-referencing the upstream git history with the May 2017 google/fonts update. No `config.yaml` is possible as the repository uses a custom build system (Python scripts with FontLab VFB sources). This is a missing_commit case.

## Commit Added (HIGH confidence)

Commit `12228946ce59ce2008e0a95a6b222632e6481121` was determined by **tag_match**. Matched a version tag in the upstream repo whose date is on or before the binary modification date in google/fonts (2017-05-15). This is the most reliable method.
