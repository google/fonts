# Investigation: Josefin Sans

## Summary

| Field | Value |
|-------|-------|
| Family Name | Josefin Sans |
| Slug | josefin-sans |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/josefinsans |
| Commit Hash | bf6907e3a34924300dd407201262f62c2fc2a642 |
| Config YAML | sources/config.yaml |
| Status | missing_commit |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/josefinsans"
}
```

## Investigation

The `ofl/josefinsans/` directory contains variable font files, `METADATA.pb`, `OFL.txt`, `DESCRIPTION.en_us.html`, and an override `config.yaml` (added by AI agent commit `5ddf312e6` on 2026-02-20).

Git history:
- `2a009610a` (2021-08-26, PR #3664): "Josefin Sans v2.001 (stat fix)" — updated font files and copyright string, no upstream commit referenced.
- `13e7a7e31` ("josefinsans: v2.000 added."): Referenced commit `132fdfd997a62411375d15e20ef81285923750c6` from `https://github.com/googlefonts/josefinsans`.

The METADATA.pb contains only `repository_url` with no `commit` field.

The upstream repository at https://github.com/googlefonts/josefinsans is cached at `upstream_repos/fontc_crater_cache/googlefonts/josefinsans`. The repository has two branches:
- `master`: HEAD is `132fdfd997a62411375d15e20ef81285923750c6` ("remove underscore anchors", 2019-11-28)
- `main`: HEAD is `bf6907e3a34924300dd407201262f62c2fc2a642` ("Merge pull request #22 from aaronbell/main", 2021-07-29)

The `main` branch commit `bf6907e3` ("Updating to UFR build format") was merged shortly before the v2.001 stat fix (PR #3664, 2021-08-26). The tracking JSON identifies `bf6907e3` as the correct commit, noting: "Merge PR #22 'Updating to UFR build format' (2021-07-29). Used for gfonts PR #3664 'Josefin Sans v2.001 (stat fix)'."

At commit `bf6907e3` on the `main` branch, the `sources/` directory contains `JosefinSans.designspace`, `JosefinSans-Italic.designspace`, and a `config.yaml`. This config.yaml is the gftools-builder configuration with the full STAT table configuration.

An override `config.yaml` was created in the google/fonts family directory by the AI agent commit `5ddf312e6`. However, since the upstream `main` branch at `bf6907e3` already has `sources/config.yaml`, the METADATA.pb should reference `sources/config.yaml` in the upstream repo instead.

## Conclusion

The repository URL is correct. The commit hash `bf6907e3a34924300dd407201262f62c2fc2a642` (from the `main` branch) needs to be added to METADATA.pb along with `config_yaml: "sources/config.yaml"`. The existing override `config.yaml` in the google/fonts directory was created before this upstream config was discovered, and can be removed once the METADATA.pb is updated to reference the upstream config.
