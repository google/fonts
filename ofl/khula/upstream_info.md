# Investigation: Khula

## Summary

| Field | Value |
|-------|-------|
| Family Name | Khula |
| Slug | khula |
| License Dir | ofl |
| Repository URL | https://github.com/erinmclaughlin/Khula |
| Commit Hash | 1389c0184856d690ea489f86e84c546e4473722d |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/erinmclaughlin/Khula"
  commit: "1389c0184856d690ea489f86e84c546e4473722d"
}
primary_script: "Deva"
```

## Investigation

The METADATA.pb contains `repository_url` and `commit`. The upstream repository `erinmclaughlin/Khula` is cached at `upstream_repos/fontc_crater_cache/erinmclaughlin/Khula`.

The repository contains UFO sources in the `UFO/` directory:
- `UFO/Bold/`, `UFO/ExtraBold/`, `UFO/Light/`, `UFO/Regular/`, `UFO/SemiBold/`
- `Khula_superpolator.sp3` (Superpolator source for interpolation)

No `config.yaml` exists in the upstream repository. However, `google/fonts/ofl/khula/config.yaml` provides an override:

```yaml
buildVariable: false
sources:
  - Khula_superpolator.sp3
```

The latest commit in the upstream repo is `703fbf36` ("Merge pull request #5 from JosephWeaver/patch-1"), but the METADATA.pb records commit `1389c018` ("Update README.md"), which is an earlier commit in the history. This indicates the onboarding was done at commit `1389c018`.

Since there is no `config_yaml` field in METADATA.pb but there is an override `config.yaml` in the google/fonts family directory, google-fonts-sources will auto-detect the local override.

## Conclusion

Status is complete. The source block has repo URL and commit hash. An override `config.yaml` exists in the google/fonts directory. No changes needed to METADATA.pb.
